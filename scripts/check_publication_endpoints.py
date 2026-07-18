#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify that freshly published playlist aliases serve the exact new bytes."""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.request import Request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from network_safety import public_urlopen
from validate_playlist import validate_text


@dataclass(frozen=True)
class Endpoint:
    name: str
    url: str
    retries: int
    hard_raw: bool = False
    television_compatible: bool = False


@dataclass
class EndpointResult:
    name: str
    url: str
    hard_raw: bool
    television_compatible: bool
    ok: bool = False
    attempts: int = 0
    size: int = 0
    sha256: str = ""
    error: str = ""


def endpoint_matrix(repo: str, branch: str) -> list[Endpoint]:
    owner, name = repo.split("/", 1)
    path = "ku9-live.txt"
    raw_path = "live-curated.txt"
    return [
        Endpoint("github_raw", f"https://raw.githubusercontent.com/{repo}/{branch}/{raw_path}", 30, hard_raw=True),
        Endpoint("github_pages", f"https://{owner}.github.io/{name}/{raw_path}", 12),
        Endpoint("ghproxy_raw", f"https://gh-proxy.com/raw.githubusercontent.com/{repo}/{branch}/{raw_path}", 12, television_compatible=True),
        Endpoint("jsdelivr_cdn", f"https://cdn.jsdelivr.net/gh/{repo}/{path}", 12, television_compatible=True),
        Endpoint("jsdelivr_gcore", f"https://gcore.jsdelivr.net/gh/{repo}@{branch}/{path}", 8, television_compatible=True),
        Endpoint("jsdelivr_testingcf", f"https://testingcf.jsdelivr.net/gh/{repo}@{branch}/{path}", 8, television_compatible=True),
    ]


def build_request(url: str) -> Request:
    """Build the exact request a television subscription will use.

    Do not append a cache-busting query parameter here.  A unique query string
    can miss the stale canonical CDN object and falsely report success while
    the URL configured on the television still serves old bytes.
    """
    return Request(
        url,
        headers={
            "User-Agent": "tv-live-auto-check-publication-smoke",
            "Accept": "text/plain,*/*",
            # Deliberately omit Cache-Control/Pragma. The gate must observe the
            # canonical cache object a television fetches, not force a special
            # revalidation path that could hide stale CDN bytes.
            "Connection": "close",
        },
    )


def fetch_bytes(url: str, timeout: int, max_bytes: int) -> bytes:
    with public_urlopen(build_request(url), timeout=timeout) as response:
        data = response.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise ValueError(f"endpoint response exceeded {max_bytes} bytes")
    return data


def check_endpoint(endpoint: Endpoint, expected_hash: str, timeout: int, max_bytes: int, retry_wait: float) -> EndpointResult:
    result = EndpointResult(endpoint.name, endpoint.url, endpoint.hard_raw, endpoint.television_compatible)
    for attempt in range(1, endpoint.retries + 1):
        result.attempts = attempt
        try:
            data = fetch_bytes(endpoint.url, timeout, max_bytes)
            result.size = len(data)
            result.sha256 = hashlib.sha256(data).hexdigest()
            validate_text(data.decode("utf-8", "strict"), require_categories=True)
            if result.sha256 == expected_hash:
                result.ok = True
                result.error = ""
                return result
            result.error = "stale hash"
        except Exception as exc:
            result.error = repr(exc)[:300]
        if attempt < endpoint.retries:
            time.sleep(retry_wait)
    return result


def render_report(results: list[EndpointResult], expected_size: int, expected_hash: str) -> str:
    raw_ok = any(item.ok and item.hard_raw for item in results)
    tv_ok = any(item.ok and item.television_compatible for item in results)
    lines = [
        "# CDN and publication endpoint health report",
        "",
        f"Expected size: {expected_size}",
        f"Expected SHA256: {expected_hash}",
        f"Authoritative GitHub Raw current: {raw_ok}",
        f"At least one television-compatible endpoint current: {tv_ok}",
        "",
        "| Endpoint | Current | TV compatible | Attempts | Size | SHA256 | URL | Error |",
        "|---|---:|---:|---:|---:|---|---|---|",
    ]
    for item in results:
        lines.append(
            f"| {item.name} | {item.ok} | {item.television_compatible} | {item.attempts} | "
            f"{item.size} | {item.sha256} | {item.url} | {item.error.replace('|', '/')} |"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="owner/repository")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--expected", default=str(ROOT / "live-curated.txt"))
    parser.add_argument("--report", default=str(ROOT / "cdn-health-report.md"))
    parser.add_argument("--json", dest="json_path", default=str(ROOT / "cdn-health-report.json"))
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--retry-wait", type=float, default=10.0)
    args = parser.parse_args(argv)

    expected = Path(args.expected).read_bytes()
    validate_text(expected.decode("utf-8", "strict"), require_categories=True)
    expected_hash = hashlib.sha256(expected).hexdigest()
    max_bytes = max(2_000_000, len(expected) * 3)
    endpoints = endpoint_matrix(args.repo, args.branch)
    with cf.ThreadPoolExecutor(max_workers=len(endpoints)) as executor:
        futures = [
            executor.submit(check_endpoint, endpoint, expected_hash, args.timeout, max_bytes, args.retry_wait)
            for endpoint in endpoints
        ]
        results = [future.result() for future in futures]
    report = render_report(results, len(expected), expected_hash)
    Path(args.report).write_text(report, encoding="utf-8", newline="\n")
    Path(args.json_path).write_text(
        json.dumps(
            {
                "expected_size": len(expected),
                "expected_sha256": expected_hash,
                "raw_current": any(item.ok and item.hard_raw for item in results),
                "television_endpoint_current": any(item.ok and item.television_compatible for item in results),
                "endpoints": [asdict(item) for item in results],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(report)
    if not any(item.ok and item.hard_raw for item in results):
        print("GitHub Raw publication is not current", file=sys.stderr)
        return 1
    if not any(item.ok and item.television_compatible for item in results):
        print("No television-compatible publication endpoint is current", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
