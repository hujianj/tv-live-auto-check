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
from stability import update_history
from playlist_config import load_guard

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
TXT_FILES = ["live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"]
M3U_FILE = "live.m3u"
SUMMARY_FILE = "full-check-summary.json"
REPORT_FILE = "published-recheck-report.md"
FINAL_REPORT_FILE = "final-publish-report.md"
CSV_FILE = "published_recheck_results.csv"
SOURCE_MAP_FILE = "curated-source-map.csv"

MAX_WORKERS = int(os.getenv("IPTV_PUBLISHED_RECHECK_WORKERS", os.getenv("IPTV_CHECK_WORKERS", "64")))


def max_failed_url_ratio() -> float:
    return float(os.getenv("IPTV_PUBLISHED_RECHECK_MAX_FAILED_RATIO", str(load_guard().get("max_published_recheck_failed_url_ratio", 0.25))))


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


def load_source_map() -> dict[tuple[str, str], str]:
    path = ROOT / SOURCE_MAP_FILE
    if not path.exists():
        return {}
    out: dict[tuple[str, str], str] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            name = row.get("name") or ""
            url = row.get("url") or ""
            source = row.get("source") or ""
            if name and url and source:
                out.setdefault((name, url), source)
    return out


def source_for(row: Row, source_map: dict[tuple[str, str], str]) -> str:
    return source_map.get((row.name, row.url), "unknown")


def update_summary(before_rows: list[Row], after_rows: list[Row], checked_urls: int, failed_urls: dict[str, str], elapsed: float, source_map: dict[tuple[str, str], str], stability_summary: dict) -> None:
    path = ROOT / SUMMARY_FILE
    summary = json.loads(path.read_text(encoding="utf-8"))
    cnt = Counter(row.group for row in after_rows)
    source_cnt = Counter(source_for(row, source_map) for row in after_rows)
    group_source_cnt = Counter(f"{row.group}|{source_for(row, source_map)}" for row in after_rows)
    summary.update({
        "curated_published_lines": len(after_rows),
        "curated_channel_names": len({row.name for row in after_rows}),
        "curated_groups": dict(cnt),
        "curated_sources": dict(source_cnt),
        "curated_group_sources": dict(group_source_cnt),
        "final_primary_published_lines": len(after_rows),
        "primary_published_lines": len(after_rows),
        "final_publish_report_file": FINAL_REPORT_FILE,
        "curated_source_map_available": bool(source_map),
        "stability": stability_summary,
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


def write_final_report(groups: list[str], rows: list[Row], failed_urls: dict[str, str], elapsed: float, source_map: dict[tuple[str, str], str], stability_summary: dict) -> None:
    group_counts = Counter(row.group for row in rows)
    source_counts = Counter(source_for(row, source_map) for row in rows)
    group_source_counts = Counter((row.group, source_for(row, source_map)) for row in rows)
    try:
        summary = json.loads((ROOT / SUMMARY_FILE).read_text(encoding="utf-8"))
    except Exception:
        summary = {}
    quality = summary.get("quality_limits_applied") or {}
    lines = [
        "# Final TV-facing playlist report",
        "",
        "This report describes the final playlist after curation and after the second full published-URL recheck.",
        "",
        f"Rows: {len(rows)}",
        f"Unique channel names: {len({row.name for row in rows})}",
        f"Unique URLs: {len({row.url for row in rows})}",
        f"Failed unique URLs removed during final recheck: {len(failed_urls)}",
        f"Final recheck elapsed: {elapsed:.1f}s",
        f"Source map available: {bool(source_map)}",
        f"Stability tracked URLs after update: {stability_summary.get('tracked_urls_after')}",
        f"Stability OK/fail updates: {stability_summary.get('ok_updates')}/{stability_summary.get('fail_updates')}",
        f"Strict quality filter dropped rows before recheck: {quality.get('strict_filter_dropped_rows', 0)}",
        f"Channel limit trimmed rows before recheck: {quality.get('channel_limit_trimmed_rows', 0)}",
        f"Group limit trimmed rows before recheck: {sum((quality.get('group_limit_trimmed_counts') or {}).values())}",
        "",
        "## Groups",
        "",
        "| Group | Rows |",
        "|---|---:|",
    ]
    for group in groups:
        if group_counts[group]:
            lines.append(f"| {group} | {group_counts[group]} |")
    lines += ["", "## Final published lines by source", "", "| Source | Rows |", "|---|---:|"]
    for source, count in source_counts.most_common():
        lines.append(f"| {source} | {count} |")
    lines += ["", "## Top sources per group", ""]
    for group in groups:
        top = [(source, count) for (g, source), count in group_source_counts.items() if g == group]
        if not top:
            continue
        lines.append(f"### {group}")
        for source, count in sorted(top, key=lambda item: (-item[1], item[0]))[:8]:
            lines.append(f"- {source}: {count}")
        lines.append("")
    lines += ["## First 80 final published rows", ""]
    for row in rows[:80]:
        lines.append(f"- {row.group} / {row.name} / {source_for(row, source_map)} / {row.url}")
    (ROOT / FINAL_REPORT_FILE).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    start = time.time()
    for filename in TXT_FILES:
        validate_file(ROOT / filename)
    groups, rows = parse_tv_txt(ROOT / "live-curated.txt")
    source_map = load_source_map()
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
    elapsed = time.time() - start
    failed_ratio = len(failed_urls) / max(1, len(by_url))
    threshold = max_failed_url_ratio()
    if failed_ratio > threshold:
        write_report(rows, kept_rows, failed_urls, elapsed)
        abort_lines = [
            "# Final TV-facing playlist report",
            "",
            "ABORTED: final published-URL recheck failed too many URLs, so playlist files were not rewritten.",
            "",
            f"Rows before: {len(rows)}",
            f"Candidate rows after failed URL removal: {len(kept_rows)}",
            f"Failed unique URLs: {len(failed_urls)}",
            f"Checked unique URLs: {len(by_url)}",
            f"Failed URL ratio: {failed_ratio:.1%}",
            f"Maximum allowed failed URL ratio: {threshold:.1%}",
            f"Elapsed: {elapsed:.1f}s",
        ]
        (ROOT / FINAL_REPORT_FILE).write_text("\n".join(abort_lines) + "\n", encoding="utf-8", newline="\n")
        print(
            "Published recheck aborted: "
            f"failed_url_ratio={failed_ratio:.1%} threshold={threshold:.1%}; "
            "not rewriting playlist outputs"
        )
        return 1
    write_outputs(groups, kept_rows)
    stability_summary = update_history(rows, failed_urls, source_map)
    update_summary(rows, kept_rows, len(by_url), failed_urls, elapsed, source_map, stability_summary)
    write_report(rows, kept_rows, failed_urls, elapsed)
    write_final_report(groups, kept_rows, failed_urls, elapsed, source_map, stability_summary)
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
