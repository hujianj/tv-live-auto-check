#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Purge every configured TV playlist from jsDelivr after Git propagation."""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import time
from dataclasses import dataclass
from urllib.request import Request

from network_safety import public_urlopen
from publication_config import purge_files


@dataclass(frozen=True)
class PurgeResult:
    url: str
    ok: bool
    attempts: int
    status: str = ""
    error: str = ""


def build_purge_urls(repo: str, branch: str, files: list[str]) -> list[str]:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError(f"invalid GitHub repository name: {repo!r}")
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", branch) or ".." in branch:
        raise ValueError(f"invalid Git branch name: {branch!r}")
    urls: list[str] = []
    for path in files:
        urls.append(f"https://purge.jsdelivr.net/gh/{repo}/{path}")
        urls.append(f"https://purge.jsdelivr.net/gh/{repo}@{branch}/{path}")
    return urls


def purge_url(url: str, timeout: int = 20, retries: int = 3) -> PurgeResult:
    last_error = ""
    last_status = ""
    for attempt in range(1, max(1, retries) + 1):
        request = Request(
            url,
            headers={"User-Agent": "tv-live-auto-check-jsdelivr-purge", "Accept": "application/json"},
        )
        try:
            with public_urlopen(request, timeout=timeout) as response:
                payload = response.read(1_000_000)
            decoded = json.loads(payload.decode("utf-8")) if payload else {}
            last_status = str(decoded.get("status") or "")
            if last_status == "finished":
                return PurgeResult(url, True, attempt, status=last_status)
            last_error = f"unexpected purge status: {last_status or 'empty'}"
        except Exception as exc:
            last_error = repr(exc)[:300]
        if attempt < max(1, retries):
            time.sleep(float(attempt))
    return PurgeResult(url, False, max(1, retries), status=last_status, error=last_error)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="owner/repository")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--pre-wait", type=float, default=0.0)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args(argv)
    if args.pre_wait < 0 or args.timeout < 1 or args.retries < 1 or args.workers < 1:
        raise SystemExit("pre-wait must be >= 0; timeout/retries/workers must be >= 1")

    if args.pre_wait:
        print(f"Waiting {args.pre_wait:g}s for Git publication to propagate before jsDelivr purge.", flush=True)
        time.sleep(args.pre_wait)

    urls = build_purge_urls(args.repo, args.branch, purge_files())
    results: list[PurgeResult] = []
    with cf.ThreadPoolExecutor(max_workers=min(args.workers, len(urls))) as executor:
        futures = [executor.submit(purge_url, url, args.timeout, args.retries) for url in urls]
        for future in cf.as_completed(futures):
            result = future.result()
            results.append(result)
            print(
                f"jsDelivr purge {'OK' if result.ok else 'FAIL'} attempts={result.attempts} "
                f"status={result.status or '-'} url={result.url} {result.error}",
                flush=True,
            )
    failed = [result for result in results if not result.ok]
    print(json.dumps({"purged": len(results) - len(failed), "failed": len(failed)}, sort_keys=True))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
