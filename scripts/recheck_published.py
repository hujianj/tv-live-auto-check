#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import concurrent.futures as cf
import csv
import json
import os
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from validate_playlist import validate_file, validate_text
from verify_sources import Candidate, CheckResult, REQUIRE_VIDEO_TRACK, check_candidate_resilient, is_core_family_candidate
from stability import update_history
from playlist_config import load_guard, load_quality, load_rules
from channel_utils import format_extinf
from channel_identity import canonical_channel_key

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
TXT_FILES = ["live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"]
M3U_FILE = "live.m3u"
FAMILY_DEFAULT_TXT_FILES = ["ku9-family.txt", "live-family.txt"]
FAMILY_DEFAULT_M3U_FILE = "family.m3u"
SUMMARY_FILE = "full-check-summary.json"
REPORT_FILE = "published-recheck-report.md"
FINAL_REPORT_FILE = "final-publish-report.md"
CSV_FILE = "published_recheck_results.csv"
SOURCE_MAP_FILE = "curated-source-map.csv"
CANDIDATE_POOL_FILE = "curated-candidate-pool.csv"

MAX_WORKERS = int(os.getenv("IPTV_PUBLISHED_RECHECK_WORKERS", os.getenv("IPTV_CHECK_WORKERS", "64")))
REFILL_WORKERS = max(1, int(os.getenv("IPTV_PUBLISHED_REFILL_WORKERS", "24")))
REQUIRE_CORE_PROGRESS = os.getenv("IPTV_PUBLISHED_REQUIRE_CORE_PROGRESS", "1").strip().lower() not in {"0", "false", "no"}


def max_failed_url_ratio() -> float:
    return float(os.getenv("IPTV_PUBLISHED_RECHECK_MAX_FAILED_RATIO", str(load_guard().get("max_published_recheck_failed_url_ratio", 0.25))))


@dataclass(frozen=True)
class Row:
    group: str
    name: str
    url: str


@dataclass(frozen=True)
class PoolCandidate:
    selection_key: str
    row: Row
    source: str


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
        lines.append(format_extinf(row.name, row.group))
        lines.append(row.url)
    return "\n".join(lines) + "\n"


def family_profile() -> dict:
    return load_quality().get("family_profile") or {}


def family_enabled() -> bool:
    return bool(family_profile().get("enabled", False))


def family_txt_files() -> list[str]:
    files = family_profile().get("txt_files") or FAMILY_DEFAULT_TXT_FILES
    return [str(x) for x in files if str(x).strip()]


def family_m3u_file() -> str:
    return str(family_profile().get("m3u_file") or FAMILY_DEFAULT_M3U_FILE)


def family_limit_for_group(group: str) -> int:
    profile = family_profile()
    limits = profile.get("group_channel_limits") or {}
    return max(1, int(limits.get(group, profile.get("default_max_urls_per_name", 1))))


def build_family_rows(groups: list[str], rows: list[Row]) -> list[Row]:
    """Build a compact TV-facing family playlist while preserving curated order."""
    if not family_enabled():
        return []
    profile = family_profile()
    group_max_rows = {str(k): int(v) for k, v in (profile.get("group_max_rows") or {}).items()}
    group_counts: Counter[str] = Counter()
    name_counts: Counter[tuple[str, str]] = Counter()
    out: list[Row] = []
    for row in rows:
        group_limit = group_max_rows.get(row.group, 0)
        if group_limit > 0 and group_counts[row.group] >= group_limit:
            continue
        key = (row.group, canonical_channel_key(row.name))
        if name_counts[key] >= family_limit_for_group(row.group):
            continue
        out.append(row)
        group_counts[row.group] += 1
        name_counts[key] += 1
    return out


def write_family_outputs(groups: list[str], rows: list[Row]) -> dict:
    """Write compact family playlist aliases and return summary metadata."""
    if not family_enabled():
        return {"enabled": False}
    family_rows = build_family_rows(groups, rows)
    text = render_txt(groups, family_rows)
    validate_text(text, require_categories=True)
    txt_files = family_txt_files()
    for filename in txt_files:
        (ROOT / filename).write_text(text, encoding="utf-8", newline="\n")
    m3u_file = family_m3u_file()
    (ROOT / m3u_file).write_text(render_m3u(family_rows), encoding="utf-8", newline="\n")
    validate_file(ROOT / m3u_file)
    group_counts = Counter(row.group for row in family_rows)
    profile = family_profile()
    result = {
        "enabled": True,
        "txt_files": txt_files,
        "m3u_file": m3u_file,
        "lines": len(family_rows),
        "unique_names": len({row.name for row in family_rows}),
        "unique_urls": len({row.url for row in family_rows}),
        "groups": dict(group_counts),
        "min_lines": int(profile.get("min_lines", 0) or 0),
        "max_lines": int(profile.get("max_lines", 0) or 0),
    }
    if result["min_lines"] and result["lines"] < result["min_lines"]:
        raise ValueError(f"family playlist too small: {result['lines']} < {result['min_lines']}")
    if result["max_lines"] and result["lines"] > result["max_lines"]:
        raise ValueError(f"family playlist too large: {result['lines']} > {result['max_lines']}")
    return result


def cleanup_stale_diagnostics() -> None:
    path = ROOT / CSV_FILE
    try:
        if path.exists():
            path.unlink()
    except OSError:
        pass


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


def write_source_map(rows: list[Row], source_map: dict[tuple[str, str], str]) -> None:
    with (ROOT / SOURCE_MAP_FILE).open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["group", "name", "url", "source"])
        for row in rows:
            writer.writerow([row.group, row.name, row.url, source_for(row, source_map)])


def write_results_csv(
    rows: list[Row],
    results: dict[str, CheckResult],
    attempted_refills: list[PoolCandidate] | None = None,
    refill_results: dict[str, CheckResult] | None = None,
) -> None:
    attempted_refills = attempted_refills or []
    refill_results = refill_results or {}
    with (ROOT / CSV_FILE).open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["phase", "ok", "group", "name", "url", "source", "detail"])
        for row in rows:
            result = results[row.url]
            writer.writerow(["published", result.ok, row.group, row.name, row.url, "published_recheck", result.detail])
        for candidate in attempted_refills:
            result = refill_results[candidate.row.url]
            writer.writerow([
                "refill",
                result.ok,
                candidate.row.group,
                candidate.row.name,
                candidate.row.url,
                candidate.source,
                result.detail,
            ])


def row_identity(row: Row) -> tuple[str, str]:
    return row.group, canonical_channel_key(row.name)


def is_core_row(row: Row) -> bool:
    return is_core_family_candidate(Candidate("published_recheck", row.group, row.name, row.url))


def load_candidate_pool(path: Path | None = None) -> list[PoolCandidate]:
    path = path or (ROOT / CANDIDATE_POOL_FILE)
    if not path.exists():
        return []
    out: list[PoolCandidate] = []
    seen: set[tuple[str, str]] = set()
    with path.open(encoding="utf-8", newline="") as f:
        for item in csv.DictReader(f):
            group = (item.get("group") or "").strip()
            name = (item.get("name") or "").strip()
            url = (item.get("url") or "").strip()
            source = (item.get("source") or "unknown").strip() or "unknown"
            selection_key = (item.get("selection_key") or canonical_channel_key(name)).strip()
            if not group or not name or not url or not selection_key:
                continue
            # A corrupt/stale pool must never refill a different channel identity.
            if selection_key != canonical_channel_key(name):
                continue
            dedup_key = (selection_key, url)
            if dedup_key in seen:
                continue
            seen.add(dedup_key)
            out.append(PoolCandidate(selection_key, Row(group, name, url), source))
    return out


def _unique_url_counts(rows: list[Row]) -> Counter[tuple[str, str]]:
    values: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in rows:
        values[row_identity(row)].add(row.url)
    return Counter({key: len(urls) for key, urls in values.items()})


def _ordered_rows(before_rows: list[Row], rows: list[Row]) -> list[Row]:
    """Keep canonical channels in original curated order after adding refills."""
    order: list[tuple[str, str]] = []
    seen_keys: set[tuple[str, str]] = set()
    for row in before_rows + rows:
        key = row_identity(row)
        if key not in seen_keys:
            seen_keys.add(key)
            order.append(key)
    by_key: dict[tuple[str, str], list[Row]] = defaultdict(list)
    seen_rows: set[tuple[str, str, str]] = set()
    for row in rows:
        exact = (row.group, row.name, row.url)
        if exact in seen_rows:
            continue
        seen_rows.add(exact)
        by_key[row_identity(row)].append(row)
    return [row for key in order for row in by_key.get(key, [])]


def refill_missing_rows(
    before_rows: list[Row],
    kept_rows: list[Row],
    failed_urls: dict[str, str],
    pool: list[PoolCandidate],
    checker=check_candidate_resilient,
) -> tuple[list[Row], dict[str, CheckResult], dict, list[PoolCandidate], list[PoolCandidate]]:
    """Restore post-recheck line redundancy from the already curated candidate pool.

    The pre-recheck unique-URL count per canonical channel is the target. Only
    candidates that survived the first full verification and curation hygiene
    are eligible; every replacement is checked again before publication.
    """
    targets = _unique_url_counts(before_rows)
    current = _unique_url_counts(kept_rows)
    deficits = {key: max(0, target - current.get(key, 0)) for key, target in targets.items()}
    deficits = {key: count for key, count in deficits.items() if count > 0}
    if not deficits or not pool:
        return kept_rows, {}, {
            "enabled": bool(pool),
            "channels_with_deficit": len(deficits),
            "target_rows": sum(deficits.values()),
            "attempted_unique_urls": 0,
            "playable_unique_urls": 0,
            "refilled_rows": 0,
            "unresolved_rows": sum(deficits.values()),
        }, [], []

    candidates_by_key: dict[tuple[str, str], list[PoolCandidate]] = defaultdict(list)
    existing_urls = {row.url for row in kept_rows}
    for candidate in pool:
        key = (candidate.row.group, candidate.selection_key)
        if key not in deficits or candidate.row.url in existing_urls or candidate.row.url in failed_urls:
            continue
        candidates_by_key[key].append(candidate)

    positions: Counter[tuple[str, str]] = Counter()
    accepted: list[PoolCandidate] = []
    attempted: list[PoolCandidate] = []
    results: dict[str, CheckResult] = {}
    remaining = dict(deficits)

    while any(count > 0 for count in remaining.values()):
        batch: list[tuple[tuple[str, str], PoolCandidate]] = []
        reserved_urls = set(existing_urls)
        for key in deficits:
            need = remaining.get(key, 0)
            arr = candidates_by_key.get(key, [])
            while need > 0 and positions[key] < len(arr):
                candidate = arr[positions[key]]
                positions[key] += 1
                if candidate.row.url in reserved_urls or candidate.row.url in results:
                    continue
                reserved_urls.add(candidate.row.url)
                batch.append((key, candidate))
                need -= 1
        if not batch:
            break

        round_results: dict[str, CheckResult] = {}
        with cf.ThreadPoolExecutor(max_workers=min(REFILL_WORKERS, len(batch))) as ex:
            futs = {}
            for key, candidate in batch:
                core = is_core_row(candidate.row)
                fut = ex.submit(
                    checker,
                    Candidate(candidate.source, candidate.row.group, candidate.row.name, candidate.row.url),
                    core,
                    REQUIRE_CORE_PROGRESS and core,
                )
                futs[fut] = (key, candidate)
            for fut in cf.as_completed(futs):
                _key, candidate = futs[fut]
                round_results[candidate.row.url] = fut.result()

        # Apply in candidate-pool order, not thread completion order.
        for key, candidate in batch:
            attempted.append(candidate)
            result = round_results[candidate.row.url]
            results[candidate.row.url] = result
            if result.ok and remaining.get(key, 0) > 0 and candidate.row.url not in existing_urls:
                accepted.append(candidate)
                existing_urls.add(candidate.row.url)
                remaining[key] -= 1

    final_rows = _ordered_rows(before_rows, kept_rows + [candidate.row for candidate in accepted])
    summary = {
        "enabled": True,
        "channels_with_deficit": len(deficits),
        "target_rows": sum(deficits.values()),
        "attempted_unique_urls": len(results),
        "playable_unique_urls": sum(1 for result in results.values() if result.ok),
        "refilled_rows": len(accepted),
        "unresolved_rows": sum(remaining.values()),
    }
    return final_rows, results, summary, attempted, accepted


def update_summary(before_rows: list[Row], after_rows: list[Row], checked_urls: int, initial_failed_urls: dict[str, str], all_failed_urls: dict[str, str], elapsed: float, source_map: dict[tuple[str, str], str], stability_summary: dict, family_summary: dict, refill_summary: dict) -> None:
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
        "curated_source_map_generated": True,
        "curated_source_map_artifact_only": True,
        "curated_candidate_pool_generated": True,
        "curated_candidate_pool_artifact_only": True,
        "family_playlist": family_summary,
        "stability": stability_summary,
        "published_recheck": {
            "enabled": True,
            "checked_unique_urls": checked_urls,
            "initial_checked_unique_urls": len({row.url for row in before_rows}),
            "before_rows": len(before_rows),
            "after_rows": len(after_rows),
            "removed_rows": len(before_rows) - len(after_rows),
            "initial_failed_unique_urls": len(initial_failed_urls),
            "refill_failed_unique_urls": len(all_failed_urls) - len(initial_failed_urls),
            "failed_unique_urls": len(all_failed_urls),
            "core_progress_required": REQUIRE_CORE_PROGRESS,
            "require_video_track": REQUIRE_VIDEO_TRACK,
            "video_track_verified_unique_urls": len({row.url for row in after_rows}),
            "audio_only_rejected_unique_urls": sum(
                1 for detail in all_failed_urls.values() if "audio/" in detail.lower() or " audio " in detail.lower()
            ),
            "unknown_track_rejected_unique_urls": sum(
                1 for detail in all_failed_urls.values() if "unknown/" in detail.lower() or "not observed" in detail.lower()
            ),
            "public_network_policy_enabled": True,
            "refill": refill_summary,
            "elapsed_seconds": round(elapsed, 1),
        },
    })
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_report(before_rows: list[Row], after_rows: list[Row], failed_urls: dict[str, str], elapsed: float, refill_summary: dict | None = None) -> None:
    before_counts = Counter(row.group for row in before_rows)
    after_counts = Counter(row.group for row in after_rows)
    failed_rows = [row for row in before_rows if row.url in failed_urls]
    refill_summary = refill_summary or {}
    lines = [
        "# Published playlist recheck report",
        "",
        f"Elapsed: {elapsed:.1f}s",
        f"Rows before: {len(before_rows)}",
        f"Rows after: {len(after_rows)}",
        f"Removed rows: {len(before_rows) - len(after_rows)}",
        f"Failed unique URLs in initial final recheck: {len(failed_urls)}",
        f"Core live-progress check required: {REQUIRE_CORE_PROGRESS}",
        f"Video track required: {REQUIRE_VIDEO_TRACK}",
        f"Video-track verified final unique URLs: {len({row.url for row in after_rows})}",
        f"Refill attempted unique URLs: {refill_summary.get('attempted_unique_urls', 0)}",
        f"Refill playable unique URLs: {refill_summary.get('playable_unique_urls', 0)}",
        f"Refilled rows: {refill_summary.get('refilled_rows', 0)}",
        f"Unresolved refill rows: {refill_summary.get('unresolved_rows', 0)}",
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


def write_final_report(groups: list[str], rows: list[Row], failed_urls: dict[str, str], elapsed: float, source_map: dict[tuple[str, str], str], stability_summary: dict, family_summary: dict, refill_summary: dict) -> None:
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
        f"Failed unique URLs in initial final recheck: {len(failed_urls)}",
        f"Refilled rows from checked candidate pool: {refill_summary.get('refilled_rows', 0)}",
        f"Unresolved refill rows: {refill_summary.get('unresolved_rows', 0)}",
        f"Core live-progress check required: {REQUIRE_CORE_PROGRESS}",
        f"Final recheck elapsed: {elapsed:.1f}s",
        f"Source map available: {bool(source_map)}",
        f"Stability tracked URLs after update: {stability_summary.get('tracked_urls_after')}",
        f"Stability OK/fail updates: {stability_summary.get('ok_updates')}/{stability_summary.get('fail_updates')}",
        f"Strict quality filter dropped rows before recheck: {quality.get('strict_filter_dropped_rows', 0)}",
        f"Channel limit trimmed rows before recheck: {quality.get('channel_limit_trimmed_rows', 0)}",
        f"Group limit trimmed rows before recheck: {sum((quality.get('group_limit_trimmed_counts') or {}).values())}",
        f"Family compact playlist: {family_summary.get('lines', 0)} rows / {family_summary.get('unique_names', 0)} names / {family_summary.get('unique_urls', 0)} URLs",
        "",
        "## Groups",
        "",
        "| Group | Rows |",
        "|---|---:|",
    ]
    for group in groups:
        if group_counts[group]:
            lines.append(f"| {group} | {group_counts[group]} |")
    if family_summary.get("enabled"):
        lines += ["", "## Family compact playlist", ""]
        lines.append(f"- TXT files: {', '.join(family_summary.get('txt_files') or [])}")
        lines.append(f"- M3U file: {family_summary.get('m3u_file')}")
        lines.append(f"- Rows: {family_summary.get('lines')}")
        lines.append(f"- Unique names: {family_summary.get('unique_names')}")
        lines.append(f"- Unique URLs: {family_summary.get('unique_urls')}")
        lines.append("")
        lines.append("| Group | Rows |")
        lines.append("|---|---:|")
        for group in groups:
            count = (family_summary.get("groups") or {}).get(group, 0)
            if count:
                lines.append(f"| {group} | {count} |")
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
    cleanup_stale_diagnostics()
    start = time.time()
    for filename in TXT_FILES:
        validate_file(ROOT / filename)
    groups, rows = parse_tv_txt(ROOT / "live-curated.txt")
    source_map = load_source_map()
    pool_path = ROOT / CANDIDATE_POOL_FILE
    if not pool_path.exists():
        raise ValueError(f"missing required refill candidate pool: {pool_path.name}")
    candidate_pool = load_candidate_pool(pool_path)

    by_url: dict[str, Row] = {}
    for row in rows:
        by_url.setdefault(row.url, row)
    core_urls = {url for url, row in by_url.items() if is_core_row(row)}
    print(
        f"Published recheck: rows={len(rows)} unique_urls={len(by_url)} "
        f"core_urls={len(core_urls)} core_progress={REQUIRE_CORE_PROGRESS} "
        f"pool={len(candidate_pool)} workers={MAX_WORKERS}",
        flush=True,
    )

    results: dict[str, CheckResult] = {}
    with cf.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {}
        for url, row in by_url.items():
            core = url in core_urls
            fut = ex.submit(
                check_candidate_resilient,
                Candidate("published_recheck", row.group, row.name, row.url),
                core,
                REQUIRE_CORE_PROGRESS and core,
            )
            futs[fut] = url
        for i, fut in enumerate(cf.as_completed(futs), 1):
            url = futs[fut]
            results[url] = fut.result()
            if i % 100 == 0 or i == len(futs):
                ok_count = sum(1 for result in results.values() if result.ok)
                print(f"published_recheck {i}/{len(futs)} ok_urls={ok_count}", flush=True)

    failed_urls = {url: result.detail for url, result in results.items() if not result.ok}
    kept_rows = [row for row in rows if row.url not in failed_urls]
    failed_ratio = len(failed_urls) / max(1, len(by_url))
    threshold = max_failed_url_ratio()
    if failed_ratio > threshold:
        elapsed = time.time() - start
        refill_summary = {
            "enabled": False,
            "skipped_reason": "initial_failed_ratio_exceeded",
            "attempted_unique_urls": 0,
            "playable_unique_urls": 0,
            "refilled_rows": 0,
            "unresolved_rows": len(rows) - len(kept_rows),
        }
        write_results_csv(rows, results)
        write_report(rows, kept_rows, failed_urls, elapsed, refill_summary)
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

    final_rows, refill_results, refill_summary, attempted_refills, accepted_refills = refill_missing_rows(
        rows,
        kept_rows,
        failed_urls,
        candidate_pool,
    )
    for candidate in accepted_refills:
        source_map[(candidate.row.name, candidate.row.url)] = candidate.source

    elapsed = time.time() - start
    write_outputs(groups, final_rows)
    write_source_map(final_rows, source_map)
    family_summary = write_family_outputs(groups, final_rows)

    refill_failed_urls = {
        url: result.detail for url, result in refill_results.items() if not result.ok
    }
    all_failed_urls = dict(failed_urls)
    all_failed_urls.update(refill_failed_urls)
    stability_rows = rows + [candidate.row for candidate in attempted_refills]
    stability_summary = update_history(stability_rows, all_failed_urls, source_map)
    checked_urls = len(by_url) + len(refill_results)

    update_summary(
        rows,
        final_rows,
        checked_urls,
        failed_urls,
        all_failed_urls,
        elapsed,
        source_map,
        stability_summary,
        family_summary,
        refill_summary,
    )
    write_report(rows, final_rows, failed_urls, elapsed, refill_summary)
    write_final_report(
        groups,
        final_rows,
        failed_urls,
        elapsed,
        source_map,
        stability_summary,
        family_summary,
        refill_summary,
    )
    write_results_csv(rows, results, attempted_refills, refill_results)
    print(
        "Published recheck done: "
        f"before={len(rows)} after={len(final_rows)} failed_urls={len(failed_urls)} "
        f"refill_attempts={len(refill_results)} refilled={refill_summary.get('refilled_rows', 0)} "
        f"unresolved={refill_summary.get('unresolved_rows', 0)} elapsed={elapsed:.1f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
