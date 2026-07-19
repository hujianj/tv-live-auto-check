#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify that freshly published playlist aliases serve the exact new bytes.

The endpoint inventory and timing policy live in config/publication.json. The
checker deliberately requests canonical URLs without cache-busting parameters,
so the result reflects what a television fetches.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.request import Request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from network_safety import public_urlopen
from publication_config import endpoint_urls, load_publication_config
from validate_playlist import validate_text


@dataclass(frozen=True)
class Endpoint:
    name: str
    url: str
    retries: int
    hard_raw: bool = False
    television_compatible: bool = False
    required_primary: bool = False
    timeout_seconds: int = 30
    endpoint_deadline_seconds: int = 120
    path: str = ""


@dataclass
class EndpointResult:
    name: str
    url: str
    hard_raw: bool
    television_compatible: bool
    required_primary: bool
    ok: bool = False
    attempts: int = 0
    size: int = 0
    sha256: str = ""
    error: str = ""
    status_code: int | None = None
    cache_control: str = ""
    age: str = ""
    etag: str = ""
    elapsed_seconds: float = 0.0
    deadline_seconds: int = 0
    path: str = ""


def endpoint_matrix(repo: str, branch: str) -> list[Endpoint]:
    return [
        Endpoint(
            name=str(item["name"]),
            url=str(item["url"]),
            retries=int(item["retries"]),
            hard_raw=bool(item.get("hard_raw", False)),
            television_compatible=bool(item.get("television_compatible", False)),
            required_primary=bool(item.get("required_primary", False)),
            timeout_seconds=int(item.get("timeout_seconds", 30)),
            endpoint_deadline_seconds=int(item.get("endpoint_deadline_seconds", 120)),
            path=str(item.get("path", "")),
        )
        for item in endpoint_urls(repo, branch, ROOT)
    ]


def build_request(url: str) -> Request:
    """Build the exact request a television subscription will use."""
    return Request(
        url,
        headers={
            "User-Agent": "tv-live-auto-check-publication-smoke",
            "Accept": "text/plain,*/*",
            # Do not add Cache-Control/Pragma or a query string. A cache-busting
            # request could falsely hide stale bytes at the canonical TV URL.
            "Connection": "close",
        },
    )


def fetch_bytes(url: str, timeout: int, max_bytes: int) -> tuple[bytes, dict[str, object]]:
    started = time.monotonic()
    with public_urlopen(build_request(url), timeout=timeout) as response:
        data = response.read(max_bytes + 1)
        headers = response.headers
        metadata: dict[str, object] = {
            "status_code": getattr(response, "status", None),
            "cache_control": headers.get("Cache-Control", ""),
            "age": headers.get("Age", ""),
            "etag": headers.get("ETag", ""),
            "elapsed_seconds": round(time.monotonic() - started, 3),
        }
    if len(data) > max_bytes:
        raise ValueError(f"endpoint response exceeded {max_bytes} bytes")
    return data, metadata


def check_endpoint(
    endpoint: Endpoint,
    expected_hash: str,
    timeout: int | None,
    max_bytes: int,
    retry_wait: float,
) -> EndpointResult:
    result = EndpointResult(
        endpoint.name,
        endpoint.url,
        endpoint.hard_raw,
        endpoint.television_compatible,
        endpoint.required_primary,
        deadline_seconds=endpoint.endpoint_deadline_seconds,
        path=endpoint.path,
    )
    started = time.monotonic()
    request_timeout = int(timeout or endpoint.timeout_seconds)
    for attempt in range(1, endpoint.retries + 1):
        remaining = endpoint.endpoint_deadline_seconds - (time.monotonic() - started)
        if remaining <= 0:
            result.error = "endpoint deadline exceeded before attempt"
            break
        result.attempts = attempt
        try:
            data, metadata = fetch_bytes(endpoint.url, max(1, min(request_timeout, int(remaining))), max_bytes)
            result.size = len(data)
            result.sha256 = hashlib.sha256(data).hexdigest()
            result.status_code = metadata.get("status_code") if isinstance(metadata.get("status_code"), int) else None
            result.cache_control = str(metadata.get("cache_control", ""))
            result.age = str(metadata.get("age", ""))
            result.etag = str(metadata.get("etag", ""))
            result.elapsed_seconds += float(metadata.get("elapsed_seconds", 0.0) or 0.0)
            validate_text(data.decode("utf-8", "strict"), require_categories=True)
            if result.sha256 == expected_hash:
                result.ok = True
                result.error = ""
                break
            result.error = "stale hash"
        except Exception as exc:
            result.error = repr(exc)[:300]
        remaining = endpoint.endpoint_deadline_seconds - (time.monotonic() - started)
        if result.ok or attempt >= endpoint.retries or remaining <= 0:
            break
        time.sleep(min(float(retry_wait), max(0.0, remaining)))
    result.elapsed_seconds = round(time.monotonic() - started, 3)
    if not result.ok and not result.error:
        result.error = "endpoint check failed"
    return result


def health_flags(results: list[EndpointResult]) -> dict[str, bool]:
    required_primary = [item for item in results if item.required_primary]
    return {
        "raw_current": any(item.ok and item.hard_raw for item in results),
        "required_primary_endpoint_current": bool(required_primary) and all(item.ok for item in required_primary),
        "television_endpoint_current": any(item.ok and item.television_compatible for item in results),
    }


def publication_gate_failures(results: list[EndpointResult]) -> list[str]:
    flags = health_flags(results)
    failures: list[str] = []
    if not flags["raw_current"]:
        failures.append("GitHub Raw publication is not current")
    if not flags["required_primary_endpoint_current"]:
        required = [item for item in results if item.required_primary]
        failed = ", ".join(item.name for item in required if not item.ok) or "missing configuration"
        failures.append(f"Required primary television endpoint is not current: {failed}")
    if not flags["television_endpoint_current"]:
        failures.append("No television-compatible publication endpoint is current")
    return failures


def render_report(results: list[EndpointResult], expected_size: int, expected_hash: str) -> str:
    flags = health_flags(results)
    lines = [
        "# CDN and publication endpoint health report",
        "",
        f"Expected size: {expected_size}",
        f"Expected SHA256: {expected_hash}",
        f"Authoritative GitHub Raw current: {flags['raw_current']}",
        f"Required primary television endpoint current: {flags['required_primary_endpoint_current']}",
        f"At least one television-compatible endpoint current: {flags['television_endpoint_current']}",
        "",
        "| Endpoint | Path | Current | Required primary | TV compatible | Attempts | Size | SHA256 | Status | Cache-Control | Age | Elapsed | URL | Error |",
        "|---|---|---:|---:|---:|---:|---:|---|---:|---|---|---:|---|---|",
    ]
    for item in results:
        error = item.error.replace("|", "/")
        lines.append(
            f"| {item.name} | {item.path} | {item.ok} | {item.required_primary} | {item.television_compatible} | "
            f"{item.attempts} | {item.size} | {item.sha256} | {item.status_code or ''} | "
            f"{item.cache_control.replace('|', '/')} | {item.age} | {item.elapsed_seconds:.3f} | {item.url} | {error} |"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    config = load_publication_config(ROOT)
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="owner/repository")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--expected", default=str(ROOT / config["authoritative_raw_file"]))
    parser.add_argument("--report", default=str(ROOT / "cdn-health-report.md"))
    parser.add_argument("--json", dest="json_path", default=str(ROOT / "cdn-health-report.json"))
    parser.add_argument("--timeout", type=int, default=0, help="override per-request timeout; 0 uses config")
    parser.add_argument("--retry-wait", type=float, default=5.0)
    parser.add_argument("--global-deadline", type=int, default=240)
    args = parser.parse_args(argv)

    expected = Path(args.expected).read_bytes()
    validate_text(expected.decode("utf-8", "strict"), require_categories=True)
    expected_hash = hashlib.sha256(expected).hexdigest()
    max_bytes = max(2_000_000, len(expected) * 3)
    endpoints = endpoint_matrix(args.repo, args.branch)
    results_by_index: dict[int, EndpointResult] = {}
    started = time.monotonic()
    executor = cf.ThreadPoolExecutor(max_workers=len(endpoints))
    futures = {
        executor.submit(check_endpoint, endpoint, expected_hash, args.timeout or None, max_bytes, args.retry_wait): index
        for index, endpoint in enumerate(endpoints)
    }
    try:
        for future in cf.as_completed(futures, timeout=args.global_deadline):
            index = futures[future]
            try:
                results_by_index[index] = future.result()
            except Exception as exc:
                endpoint = endpoints[index]
                results_by_index[index] = EndpointResult(
                    endpoint.name,
                    endpoint.url,
                    endpoint.hard_raw,
                    endpoint.television_compatible,
                    endpoint.required_primary,
                    attempts=0,
                    error=f"worker failure: {exc!r}",
                    deadline_seconds=endpoint.endpoint_deadline_seconds,
                    path=endpoint.path,
                )
    except TimeoutError:
        for future, index in futures.items():
            if index not in results_by_index:
                endpoint = endpoints[index]
                future.cancel()
                results_by_index[index] = EndpointResult(
                    endpoint.name,
                    endpoint.url,
                    endpoint.hard_raw,
                    endpoint.television_compatible,
                    endpoint.required_primary,
                    error=f"global deadline exceeded ({args.global_deadline}s)",
                    deadline_seconds=endpoint.endpoint_deadline_seconds,
                    path=endpoint.path,
                )
    finally:
        # Do not re-enter the executor context manager: its implicit
        # shutdown(wait=True) would make a global deadline non-binding.
        executor.shutdown(wait=False, cancel_futures=True)
    results = [results_by_index[i] for i in range(len(endpoints))]
    report = render_report(results, len(expected), expected_hash)
    Path(args.report).write_text(report, encoding="utf-8", newline="\n")
    flags = health_flags(results)
    Path(args.json_path).write_text(
        json.dumps(
            {
                "schema_version": 2,
                "expected_file": str(Path(args.expected).name),
                "expected_size": len(expected),
                "expected_sha256": expected_hash,
                "elapsed_seconds": round(time.monotonic() - started, 3),
                "global_deadline_seconds": args.global_deadline,
                **flags,
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
    failures = publication_gate_failures(results)
    for failure in failures:
        print(failure, file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
