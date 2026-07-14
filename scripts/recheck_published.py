#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import concurrent.futures as cf
import csv
import json
import os
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from validate_playlist import validate_file, validate_text
from verify_sources import Candidate, CheckResult, check_candidate

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
TXT_FILES = ["live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"]
M3U_FILE = "live.m3u"
SUMMARY_FILE = "full-check-summary.json"
REPORT_FILE = "published-recheck-report.md"
CSV_FILE = "published_recheck_results.csv"

MAX_WORKERS = int(os.getenv("IPTV_PUBLISHED_RECHECK_WORKERS", os.getenv("IPTV_CHECK_WORKERS", "128")))


@dataclass(frozen=True)
class Row:
    group: str
    name: str
    url: str


def parse_tv_txt(path: Path) -> tuple[list[str], list[Row]]:
    groups: list[str] = []
    rows: list[Row] = []
    current_group = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.endswith(",#genre#"):
            current_group = line.split(",", 1)[0].strip()
            groups.append(current_group)
            continue
        name, url = line.split(",", 1)
        rows.append(Row(current_group, name, url))
    return groups, rows


def render_txt(groups: list[str], rows: list[Row]) -> str:
    by_group: dict[str, list[Row]] = {}
    for row in rows:
        by_group.setdefault(row.group, []).append(row)
    lines: list[str] = []
    for group in groups:
        part = by_group.get(group, [])
        if not part:
            continue
        if lines:
            lines.append("")
        lines.append(f"{group},#genre#")
        for row in part:
            lines.append(f"{row.name},{row.url}")
    return "\n".join(lines).strip() + "\n"


def render_m3u(rows: list[Row]) -> str:
    lines = ["#EXTM3U"]
    for row in rows:
        lines.append(f'#EXTINF:-1 tvg-name="{row.name}" group-title="{row.group}",{row.name}')
        lines.append(row.url)
    return "\n".join(lines) + "\n"


def write_outputs(groups: list[str], rows: list[Row]) -> None:
    text = render_txt(groups, rows)
    validate_text(text, require_categories=True)
    for filename in TXT_FILES:
        (ROOT / filename).write_text(text, encoding="utf-8", newline="\n")
    (ROOT / M3U_FILE).write_text(render_m3u(rows), encoding="utf-8", newline="\n")
    validate_file(ROOT / M3U_FILE)


def update_summary(before_rows: list[Row], after_rows: list[Row], checked_urls: int, failed_urls: dict[str, str], elapsed: float) -> None:
    path = ROOT / SUMMARY_FILE
    summary = json.loads(path.read_text(encoding="utf-8"))
    cnt = Counter(row.group for row in after_rows)
    summary.update({
        "curated_published_lines": len(after_rows),
        "curated_channel_names": len({row.name for row in after_rows}),
        "curated_groups": dict(cnt),
        "final_primary_published_lines": len(after_rows),
        "primary_published_lines": len(after_rows),
        "published_recheck": {
            "enabled": True,
            "checked_unique_urls": checked_urls,
            "before_rows": len(before_rows),
            "after_rows": len(after_rows),
            "removed_rows": len(before_rows) - len(after_rows),
            "failed_unique_urls": len(failed_urls),
            "elapsed_seconds": round(elapsed, 1),
        },
    })
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_report(before_rows: list[Row], after_rows: list[Row], failed_urls: dict[str, str], elapsed: float) -> None:
    before_counts = Counter(row.group for row in before_rows)
    after_counts = Counter(row.group for row in after_rows)
    failed_rows = [row for row in before_rows if row.url in failed_urls]
    lines = [
        "# Published playlist recheck report",
        "",
        f"Elapsed: {elapsed:.1f}s",
        f"Rows before: {len(before_rows)}",
        f"Rows after: {len(after_rows)}",
        f"Removed rows: {len(before_rows) - len(after_rows)}",
        f"Failed unique URLs: {len(failed_urls)}",
        "",
        "## Group deltas",
        "",
        "| Group | Before | After | Removed |",
        "|---|---:|---:|---:|",
    ]
    for group in before_counts:
        lines.append(f"| {group} | {before_counts[group]} | {after_counts[group]} | {before_counts[group] - after_counts[group]} |")
    if failed_rows:
        lines += ["", "## First failed rows", ""]
        for row in failed_rows[:80]:
            lines.append(f"- {row.group} / {row.name} / {row.url} / {failed_urls.get(row.url, '')}")
    (ROOT / REPORT_FILE).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    start = time.time()
    for filename in TXT_FILES:
        validate_file(ROOT / filename)
    groups, rows = parse_tv_txt(ROOT / "live-curated.txt")
    by_url: dict[str, Row] = {}
    for row in rows:
        by_url.setdefault(row.url, row)
    print(f"Published recheck: rows={len(rows)} unique_urls={len(by_url)} workers={MAX_WORKERS}", flush=True)
    results: dict[str, CheckResult] = {}
    with cf.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {
            ex.submit(check_candidate, Candidate("published_recheck", row.group, row.name, row.url)): url
            for url, row in by_url.items()
        }
        for i, fut in enumerate(cf.as_completed(futs), 1):
            url = futs[fut]
            results[url] = fut.result()
            if i % 100 == 0 or i == len(futs):
                ok_count = sum(1 for r in results.values() if r.ok)
                print(f"published_recheck {i}/{len(futs)} ok_urls={ok_count}", flush=True)
    failed_urls = {url: r.detail for url, r in results.items() if not r.ok}
    kept_rows = [row for row in rows if row.url not in failed_urls]
    write_outputs(groups, kept_rows)
    elapsed = time.time() - start
    update_summary(rows, kept_rows, len(by_url), failed_urls, elapsed)
    write_report(rows, kept_rows, failed_urls, elapsed)
    with (ROOT / CSV_FILE).open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ok", "group", "name", "url", "detail"])
        for row in rows:
            r = results[row.url]
            w.writerow([r.ok, row.group, row.name, row.url, r.detail])
    print(f"Published recheck done: before={len(rows)} after={len(kept_rows)} failed_urls={len(failed_urls)} elapsed={elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
