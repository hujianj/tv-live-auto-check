#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path
from urllib.request import Request

from network_safety import public_urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URL = "https://hujianj.github.io/tv-live-auto-check/ku9-live.txt"
REPORT = ROOT / "local-network-report.md"
CSV_FILE = ROOT / "local-network-results.csv"
HOME_PRIORITY_FILE = ROOT / "config" / "home-priority.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the published IPTV playlist from the current local/home network."
    )
    parser.add_argument("--url", default=DEFAULT_URL, help="Remote playlist URL to fetch. Default: GitHub Pages ku9-live.txt")
    parser.add_argument("--playlist", help="Read a local playlist file instead of fetching --url")
    parser.add_argument("--core-only", action="store_true", help="Only check required CCTV and important satellite channels")
    parser.add_argument("--limit", type=int, default=0, help="Limit checked rows after filtering; useful for quick smoke tests")
    parser.add_argument("--workers", type=int, default=32, help="Concurrent URL checks")
    parser.add_argument("--timeout", type=int, default=15, help="Per-request timeout in seconds")
    parser.add_argument("--fail-on-bad", action="store_true", help="Exit with code 1 when any checked row fails")
    parser.add_argument("--fail-on-missing-channel", action="store_true", help="Exit with code 1 when any checked channel/core key has zero playable lines")
    parser.add_argument("--report", default=str(REPORT), help="Markdown report path")
    parser.add_argument("--csv", default=str(CSV_FILE), help="CSV result path")
    parser.add_argument("--write-home-priority", action="store_true", help="Write config/home-priority.json from this local-network check")
    parser.add_argument("--home-priority", default=str(HOME_PRIORITY_FILE), help="Home priority JSON path")
    parser.add_argument("--home-priority-max-urls", type=int, default=500, help="Maximum OK URLs and failed URLs to keep in home priority config")
    return parser.parse_args()


def load_playlist_text(args: argparse.Namespace) -> tuple[str, str]:
    if args.playlist:
        path = Path(args.playlist)
        return path.read_text(encoding="utf-8"), str(path)
    req = Request(args.url, headers={"User-Agent": "Mozilla/5.0 local-network-check", "Accept": "*/*"})
    with public_urlopen(req, timeout=args.timeout) as r:
        data = r.read()
        final_url = r.geturl()
    return data.decode("utf-8", "replace"), final_url


def parse_tv_txt(text: str) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    group = ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.endswith(",#genre#"):
            group = line.split(",", 1)[0].strip()
            continue
        if "," not in line:
            continue
        name, url = line.split(",", 1)
        if url.startswith(("http://", "https://")):
            rows.append((group, name, url))
    return rows


def is_core_row(group: str, name: str, required_cctv: set[str], important_satellite: set[str]) -> bool:
    from channel_utils import cctv_key

    key = cctv_key(name)
    if key and key in required_cctv:
        return True
    return name in important_satellite


def core_key_for_report(group: str, name: str) -> str:
    from channel_utils import cctv_key

    return cctv_key(name) or name


def filter_rows(rows: list[tuple[str, str, str]], args: argparse.Namespace) -> list[tuple[str, str, str]]:
    from playlist_config import load_rules

    rules = load_rules()
    coverage = rules.get("coverage", {})
    required_cctv = set(coverage.get("required_cctv", []))
    important_satellite = set(coverage.get("important_satellite", []))
    if args.core_only:
        rows = [row for row in rows if is_core_row(row[0], row[1], required_cctv, important_satellite)]
    if args.limit and args.limit > 0:
        rows = rows[: args.limit]
    return rows


def check_rows(rows: list[tuple[str, str, str]], workers: int) -> dict[str, object]:
    from verify_sources import Candidate, check_candidate_resilient

    by_url: dict[str, tuple[str, str, str]] = {}
    for row in rows:
        by_url.setdefault(row[2], row)
    results_by_url = {}
    start = time.time()
    with cf.ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futures = {
            ex.submit(check_candidate_resilient, Candidate("local_network", row[0], row[1], row[2])): url
            for url, row in by_url.items()
        }
        for i, fut in enumerate(cf.as_completed(futures), 1):
            url = futures[fut]
            results_by_url[url] = fut.result()
            if i % 50 == 0 or i == len(futures):
                ok = sum(1 for r in results_by_url.values() if r.ok)
                print(f"local_check {i}/{len(futures)} ok_urls={ok}", flush=True)
    row_results = []
    for group, name, url in rows:
        result = results_by_url[url]
        row_results.append({
            "ok": bool(result.ok),
            "group": group,
            "name": name,
            "core_key": core_key_for_report(group, name),
            "url": url,
            "detail": result.detail,
        })
    return {
        "elapsed_seconds": round(time.time() - start, 1),
        "checked_rows": len(rows),
        "checked_unique_urls": len(by_url),
        "ok_rows": sum(1 for r in row_results if r["ok"]),
        "failed_rows": sum(1 for r in row_results if not r["ok"]),
        "ok_unique_urls": sum(1 for r in results_by_url.values() if r.ok),
        "failed_unique_urls": sum(1 for r in results_by_url.values() if not r.ok),
        "rows": row_results,
        "channel_stats": channel_stats(row_results),
    }


def channel_stats(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    stats: dict[str, dict[str, object]] = {}
    for row in rows:
        key = str(row.get("core_key") or row.get("name") or "")
        item = stats.setdefault(key, {"channel": key, "rows": 0, "ok": 0, "failed": 0})
        item["rows"] = int(item["rows"]) + 1
        if row.get("ok"):
            item["ok"] = int(item["ok"]) + 1
        else:
            item["failed"] = int(item["failed"]) + 1
    return sorted(stats.values(), key=lambda item: (int(item["ok"]) == 0, str(item["channel"])))


def unique_urls_by_status(rows: list[dict[str, object]], ok: bool, limit: int) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for row in rows:
        if bool(row.get("ok")) != ok:
            continue
        url = str(row.get("url") or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        out.append(url)
        if limit > 0 and len(out) >= limit:
            break
    return out


def write_home_priority(result: dict[str, object], source: str, args: argparse.Namespace) -> Path:
    rows = list(result["rows"])  # type: ignore[index]
    limit = max(1, int(args.home_priority_max_urls))
    ok_urls = unique_urls_by_status(rows, True, limit)
    failed_urls = unique_urls_by_status(rows, False, limit)
    path = Path(args.home_priority)
    existing: dict[str, object] = {}
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8-sig"))
        except Exception:
            existing = {}
    data = {
        "description": "Optional local/home network priority hints. Generated by scripts/local_network_check.py --write-home-priority from the actual home network.",
        "enabled": bool(existing.get("enabled", True)),
        "bonus": int(existing.get("bonus", -120)),
        "penalty": int(existing.get("penalty", 180)),
        "max_urls": limit,
        "home_ok_urls": ok_urls,
        "home_failed_urls": failed_urls,
        "generated_from": source,
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "mode": "core-only" if args.core_only else "full/selected",
        "timeout_seconds": args.timeout,
        "checked_rows": result.get("checked_rows"),
        "checked_unique_urls": result.get("checked_unique_urls"),
        "ok_unique_urls": result.get("ok_unique_urls"),
        "failed_unique_urls": result.get("failed_unique_urls"),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return path


def write_outputs(result: dict[str, object], source: str, args: argparse.Namespace) -> None:
    rows = list(result["rows"])  # type: ignore[index]
    stats = list(result.get("channel_stats") or [])
    group_counts = Counter(str(r["group"]) for r in rows)
    failed = [r for r in rows if not r["ok"]]
    zero_ok_channels = [item for item in stats if int(item.get("ok") or 0) == 0]
    report_path = Path(args.report)
    csv_path = Path(args.csv)
    lines = [
        "# Local/home network IPTV check report",
        "",
        f"Source: {source}",
        f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Mode: {'core-only' if args.core_only else 'full/selected'}",
        f"Rows checked: {result['checked_rows']}",
        f"Unique URLs checked: {result['checked_unique_urls']}",
        f"OK rows: {result['ok_rows']}",
        f"Failed rows: {result['failed_rows']}",
        f"OK unique URLs: {result['ok_unique_urls']}",
        f"Failed unique URLs: {result['failed_unique_urls']}",
        f"Channels/core keys checked: {len(stats)}",
        f"Channels/core keys with zero playable lines: {len(zero_ok_channels)}",
        f"Elapsed seconds: {result['elapsed_seconds']}",
        "",
        "## Checked groups",
        "",
    ]
    for group, count in group_counts.most_common():
        lines.append(f"- {group}: {count}")
    lines += [
        "",
        "## Channel/core-key availability",
        "",
        "| Channel/core key | OK rows | Failed rows | Total rows | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for item in stats:
        ok = int(item.get("ok") or 0)
        failed_count = int(item.get("failed") or 0)
        total = int(item.get("rows") or 0)
        status = "OK" if ok > 0 else "ZERO"
        lines.append(f"| {item.get('channel')} | {ok} | {failed_count} | {total} | {status} |")
    if failed:
        detail_counts = Counter(str(r["detail"]) for r in failed)
        lines += ["", "## Failure details", ""]
        for detail, count in detail_counts.most_common(20):
            lines.append(f"- {count}: {detail}")
        lines += ["", "## First failed rows", ""]
        for row in failed[:80]:
            lines.append(f"- {row['group']} / {row['name']} / {row['detail']} / {row['url']}")
    if zero_ok_channels:
        lines += [
            "",
            "## Recommended next actions",
            "",
            "These channel/core keys had zero playable lines from this network. Re-run once with a larger timeout before changing the published list; if they remain zero, add or prioritize home-network-playable backup URLs for these channels.",
            "",
        ]
        for item in zero_ok_channels:
            lines.append(f"- {item.get('channel')}: 0/{item.get('rows')} playable")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ok", "group", "name", "core_key", "url", "detail"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({k: result[k] for k in result if k != "rows"}, ensure_ascii=False, sort_keys=True))
    print(f"Wrote {report_path} and {csv_path}")


def main() -> int:
    args = parse_args()
    os.environ["IPTV_CHECK_TIMEOUT"] = str(args.timeout)
    sys.path.insert(0, str(ROOT / "scripts"))
    text, source = load_playlist_text(args)
    rows = filter_rows(parse_tv_txt(text), args)
    if not rows:
        raise SystemExit("no rows to check; playlist may be empty or unsupported")
    result = check_rows(rows, args.workers)
    write_outputs(result, source, args)
    if args.write_home_priority:
        path = write_home_priority(result, source, args)
        print(f"Wrote home priority config {path}")
    zero_ok_channels = [item for item in result.get("channel_stats", []) if int(item.get("ok") or 0) == 0]
    if args.fail_on_missing_channel and zero_ok_channels:
        return 1
    if args.fail_on_bad and int(result["failed_rows"]) > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
