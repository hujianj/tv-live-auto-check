#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import concurrent.futures as cf
import csv
import json
import os
import shutil
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from pathlib import Path

from validate_playlist import validate_file, validate_text
from verify_sources import (
    Candidate,
    CheckResult,
    REQUIRE_VIDEO_TRACK,
    check_candidate,
    check_candidate_resilient,
    is_core_family_candidate,
)
from stability import build_observation, preview_observation, write_observation
from playlist_config import get_group_order, load_guard, load_quality, load_rules
from curate_ku9 import per_channel_limit
from channel_utils import format_extinf
from channel_identity import canonical_channel_key
from playlist_order import canonicalize_channel_rows
from url_utils import is_publishable_http_url
from media_decode import MIN_DECODED_FRAMES, decoder_preflight

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
PENDING_STABILITY_FILE = "stability-observation.json"
TRANSACTION_DIR = ".maintenance-staging/recheck"

MAX_WORKERS = int(os.getenv("IPTV_PUBLISHED_RECHECK_WORKERS", os.getenv("IPTV_CHECK_WORKERS", "64")))
REFILL_WORKERS = max(1, int(os.getenv("IPTV_PUBLISHED_REFILL_WORKERS", "24")))
FINAL_RETRY_WORKERS = max(1, int(os.getenv("IPTV_PUBLISHED_FINAL_RETRY_WORKERS", "16")))
FINAL_RETRY_TIMEOUT = max(1, int(os.getenv("IPTV_PUBLISHED_FINAL_RETRY_TIMEOUT", "14")))
FINAL_RETRY_ATTEMPTS = max(0, int(os.getenv("IPTV_PUBLISHED_FINAL_RETRY_ATTEMPTS", "1")))
REQUIRE_CORE_PROGRESS = os.getenv("IPTV_PUBLISHED_REQUIRE_CORE_PROGRESS", "1").strip().lower() not in {"0", "false", "no"}
REQUIRE_BROADCAST_PROGRESS = os.getenv(
    "IPTV_PUBLISHED_REQUIRE_BROADCAST_PROGRESS",
    "1" if REQUIRE_CORE_PROGRESS else "0",
).strip().lower() not in {"0", "false", "no"}
LIVE_PROGRESS_GROUPS = frozenset(
    str(group) for group in load_quality().get("live_progress_groups", []) if str(group).strip()
)
RECHECK_POLICY_VERSION = int(load_quality().get("published_recheck_policy_version", 1))
HISTORICAL_FALLBACK = load_guard().get("historical_fallback") or {}
HISTORICAL_FALLBACK_ENABLED = bool(HISTORICAL_FALLBACK.get("enabled", False))
HISTORICAL_FALLBACK_GROUPS = frozenset(
    str(group) for group in HISTORICAL_FALLBACK.get("groups", []) if str(group).strip()
)


def max_failed_url_ratio() -> float:
    return float(os.getenv("IPTV_PUBLISHED_RECHECK_MAX_FAILED_RATIO", str(load_guard().get("max_published_recheck_failed_url_ratio", 0.25))))


def require_decoded_result(result: CheckResult) -> CheckResult:
    if result.ok and result.decoded_frames < MIN_DECODED_FRAMES:
        return replace(result, ok=False, detail="final probe did not prove 3 decoded video frames")
    return result


def record_aborted_recheck(rows: list[Row], kept_rows: list[Row], checked: int,
                           failed: int, elapsed: float, retry: dict, threshold: float) -> None:
    """Record evidence without claiming the aborted candidate list was published."""
    path = ROOT / SUMMARY_FILE
    summary = json.loads(path.read_text(encoding="utf-8"))
    summary["strict_video_checked_unique"] = checked if REQUIRE_VIDEO_TRACK else 0
    summary["strict_progress_checked_unique"] = len({row.url for row in rows if requires_live_progress(row)}) if REQUIRE_BROADCAST_PROGRESS else 0
    summary["published_recheck"] = {
        "status": "aborted", "outputs_rewritten": False,
        "abort_reason": "failed_url_ratio_exceeded",
        "policy_version": RECHECK_POLICY_VERSION,
        "require_video_track": REQUIRE_VIDEO_TRACK,
        "require_frame_decode": True,
        "candidate_frame_decoded_unique_urls": len({row.url for row in kept_rows}),
        "broadcast_progress_required": REQUIRE_BROADCAST_PROGRESS,
        "candidate_video_verified_unique_urls": len({row.url for row in kept_rows}) if REQUIRE_VIDEO_TRACK else 0,
        "checked_unique_urls": checked, "initial_checked_unique_urls": checked,
        "first_pass_failed_unique_urls": retry.get("first_pass_failed_unique_urls", failed),
        "slow_retry_attempted_unique_urls": retry.get("attempted_unique_urls", 0),
        "slow_retry_recovered_unique_urls": retry.get("recovered_unique_urls", 0),
        "post_retry_failed_unique_urls": failed, "failed_unique_urls": failed,
        "before_rows": len(rows), "after_rows": len(rows),
        "candidate_after_rows": len(kept_rows), "removed_rows": 0, "net_row_delta": 0,
        "failed_url_ratio": failed / max(1, checked), "max_failed_url_ratio": threshold,
        "elapsed_seconds": round(elapsed, 3), "slow_retry": retry,
        "refill": {"enabled": False, "refilled_rows": 0, "attempted_unique_urls": 0},
    }
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    temporary.replace(path)


def retry_failed_final_urls(
    by_url: dict[str, "Row"],
    results: dict[str, CheckResult],
    core_urls: set[str],
    progress_urls: set[str] | None = None,
    *,
    attempts: int = FINAL_RETRY_ATTEMPTS,
    workers: int = FINAL_RETRY_WORKERS,
    timeout: int = FINAL_RETRY_TIMEOUT,
    checker=check_candidate,
) -> dict[str, int]:
    """Slowly retry every failed final URL before removal/refill decisions.

    The broad 29k-URL pass remains fast. Only the much smaller final set pays
    this extra low-concurrency retry cost, reducing false removals caused by a
    transient CDN, DNS, or first-byte delay.
    """
    progress_urls = core_urls if progress_urls is None else progress_urls
    first_details = {url: result.detail for url, result in results.items() if not result.ok}
    pending = list(first_details)
    attempted: set[str] = set()
    recovered: set[str] = set()
    for attempt in range(1, attempts + 1):
        if not pending:
            break
        batch = list(pending)
        pending = []
        print(
            f"published_final_slow_retry attempt={attempt}/{attempts} urls={len(batch)} "
            f"workers={min(workers, len(batch))} timeout={timeout}",
            flush=True,
        )
        round_results: dict[str, CheckResult] = {}
        with cf.ThreadPoolExecutor(max_workers=min(workers, len(batch))) as ex:
            futs = {}
            for url in batch:
                row = by_url[url]
                core = url in core_urls
                future = ex.submit(
                    checker,
                    Candidate("published_final_slow_retry", row.group, row.name, row.url),
                    timeout=timeout,
                    core_override=core,
                    require_progress=REQUIRE_BROADCAST_PROGRESS and url in progress_urls,
                    require_video=REQUIRE_VIDEO_TRACK,
                    require_decode=True,
                )
                futs[future] = url
            for future in cf.as_completed(futs):
                url = futs[future]
                attempted.add(url)
                round_results[url] = require_decoded_result(future.result())
        for url in batch:
            retry = round_results[url]
            if retry.ok:
                recovered.add(url)
                results[url] = CheckResult(
                    results[url].cand,
                    True,
                    f"final slow retry ok attempt={attempt} first={first_details[url]}; {retry.detail}",
                    retry.elapsed_seconds,
                    retry.checked_at,
                    retry.decoded_frames,
                )
            else:
                results[url] = CheckResult(
                    results[url].cand,
                    False,
                    f"final slow retry failed attempt={attempt} first={first_details[url]}; last={retry.detail}",
                    retry.elapsed_seconds,
                    retry.checked_at,
                    retry.decoded_frames,
                )
                pending.append(url)
    return {
        "configured_attempts": attempts,
        "timeout_seconds": timeout,
        "workers": workers,
        "first_pass_failed_unique_urls": len(first_details),
        # Legacy key retained for callers that only know the old retry schema.
        "initial_failed_unique_urls": len(first_details),
        "attempted_unique_urls": len(attempted),
        "recovered_unique_urls": len(recovered),
        "still_failed_unique_urls": sum(1 for result in results.values() if not result.ok),
    }


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
    origin: str = "current_scan"


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


def canonicalize_rows(groups: list[str], rows: list[Row]) -> list[Row]:
    """Return one stable category order shared by every publication format."""
    if len(groups) != len(set(groups)):
        raise ValueError("playlist category order contains duplicates")
    expected = set(groups)
    unexpected = sorted({row.group for row in rows} - expected)
    if unexpected:
        raise ValueError(f"playlist rows contain unknown categories: {unexpected!r}")
    return canonicalize_channel_rows(groups, rows)


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
    rows = canonicalize_rows(groups, rows)
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


def _transaction_root(root: Path) -> Path:
    return root / TRANSACTION_DIR


def recover_interrupted_promotion(root: Path = ROOT, *, fail_after: int | None = None) -> bool:
    """Roll back a promotion that was interrupted after its journal was written."""
    transaction_root = _transaction_root(root)
    journal_path = transaction_root / "transaction.json"
    if not journal_path.exists():
        return False
    journal = json.loads(journal_path.read_text(encoding="utf-8"))
    if journal.get("schema_version") != 1 or journal.get("state") != "promoting":
        raise ValueError("invalid recheck promotion journal")
    entries = journal.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("recheck promotion journal has no files")
    backup_root = transaction_root / "backup"
    for index, item in enumerate(entries, 1):
        if not isinstance(item, dict):
            raise ValueError("invalid recheck promotion journal entry")
        name = item.get("name")
        existed = item.get("existed")
        if not isinstance(name, str) or Path(name).name != name or type(existed) is not bool:
            raise ValueError("unsafe recheck promotion journal entry")
        destination = root / name
        backup = backup_root / name
        if existed:
            if not backup.is_file():
                raise ValueError(f"missing rollback backup for {name}")
            temporary = root / (name + ".rollback.tmp")
            shutil.copy2(backup, temporary)
            os.replace(temporary, destination)
        else:
            try:
                destination.unlink()
            except FileNotFoundError:
                pass
        if fail_after is not None and index >= fail_after:
            raise RuntimeError("injected recheck rollback failure")
    shutil.rmtree(transaction_root)
    print("Recovered an interrupted recheck output promotion.", flush=True)
    return True


def prepare_staging_root(root: Path = ROOT) -> Path:
    transaction_root = _transaction_root(root)
    if transaction_root.exists():
        shutil.rmtree(transaction_root)
    staged = transaction_root / "staged"
    staged.mkdir(parents=True)
    return staged


def promote_staged_outputs(
    staged_root: Path,
    filenames: list[str],
    root: Path = ROOT,
    *,
    fail_after: int | None = None,
) -> None:
    """Promote a validated file set, rolling every destination back on failure."""
    names = list(dict.fromkeys(filenames))
    if not names or any(Path(name).name != name for name in names):
        raise ValueError("recheck promotion accepts only non-empty basename file lists")
    missing = [name for name in names if not (staged_root / name).is_file()]
    if missing:
        raise ValueError(f"staged recheck outputs are incomplete: {missing}")
    transaction_root = _transaction_root(root)
    backup_root = transaction_root / "backup"
    backup_root.mkdir(parents=True, exist_ok=True)
    entries = []
    for name in names:
        destination = root / name
        existed = destination.is_file()
        entries.append({"name": name, "existed": existed})
        if existed:
            shutil.copy2(destination, backup_root / name)
    journal = {"schema_version": 1, "state": "promoting", "files": entries}
    journal_path = transaction_root / "transaction.json"
    temporary_journal = transaction_root / "transaction.json.tmp"
    temporary_journal.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary_journal, journal_path)
    try:
        for index, name in enumerate(names, 1):
            os.replace(staged_root / name, root / name)
            if fail_after is not None and index >= fail_after:
                raise RuntimeError("injected recheck promotion failure")
    except BaseException:
        recover_interrupted_promotion(root)
        raise
    shutil.rmtree(transaction_root)


def write_outputs(groups: list[str], rows: list[Row]) -> list[Row]:
    canonical_rows = canonicalize_rows(groups, rows)
    text = render_txt(groups, canonical_rows)
    validate_text(text, require_categories=True)
    for filename in TXT_FILES:
        (ROOT / filename).write_text(text, encoding="utf-8", newline="\n")
    (ROOT / M3U_FILE).write_text(render_m3u(canonical_rows), encoding="utf-8", newline="\n")
    validate_file(ROOT / M3U_FILE)
    return canonical_rows


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
    *,
    source_map: dict[tuple[str, str], str] | None = None,
) -> None:
    attempted_refills = attempted_refills or []
    refill_results = refill_results or {}
    source_map = source_map if source_map is not None else load_source_map()
    with (ROOT / CSV_FILE).open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["phase", "ok", "group", "name", "url", "source", "origin", "detail", "video_required", "progress_required", "checked_at", "elapsed_seconds", "decode_required", "decoded_frames"])
        for row in rows:
            result = results[row.url]
            writer.writerow(["published", result.ok, row.group, row.name, row.url, source_for(row, source_map), "current_publication", result.detail,
                             REQUIRE_VIDEO_TRACK, REQUIRE_BROADCAST_PROGRESS and requires_live_progress(row), result.checked_at, result.elapsed_seconds, True, result.decoded_frames])
        for candidate in attempted_refills:
            result = refill_results[candidate.row.url]
            writer.writerow([
                "refill",
                result.ok,
                candidate.row.group,
                candidate.row.name,
                candidate.row.url,
                candidate.source,
                candidate.origin,
                result.detail,
                REQUIRE_VIDEO_TRACK,
                REQUIRE_BROADCAST_PROGRESS and requires_live_progress(candidate.row),
                result.checked_at,
                result.elapsed_seconds,
                True,
                result.decoded_frames,
            ])


def row_identity(row: Row) -> tuple[str, str]:
    return row.group, canonical_channel_key(row.name)


def is_core_row(row: Row) -> bool:
    return is_core_family_candidate(Candidate("published_recheck", row.group, row.name, row.url))


def requires_live_progress(row: Row) -> bool:
    return is_core_row(row) or row.group in LIVE_PROGRESS_GROUPS


def load_candidate_pool(path: Path | None = None) -> list[PoolCandidate]:
    path = path or (ROOT / CANDIDATE_POOL_FILE)
    if not path.exists():
        return []
    out: list[PoolCandidate] = []
    seen: set[tuple[str, str]] = set()
    expected_groups = set(get_group_order())
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        expected_header = ["selection_key", "group", "name", "url", "source", "origin"]
        if reader.fieldnames != expected_header:
            raise ValueError(
                f"{path.name}: header must be {expected_header!r}, got {reader.fieldnames!r}"
            )
        for lineno, item in enumerate(reader, 2):
            group = (item.get("group") or "").strip()
            name = (item.get("name") or "").strip()
            url = (item.get("url") or "").strip()
            source = (item.get("source") or "").strip()
            origin = (item.get("origin") or "").strip()
            selection_key = (item.get("selection_key") or "").strip()
            if not all((group, name, url, source, origin, selection_key)):
                raise ValueError(f"{path.name} line {lineno}: candidate pool contains an empty field")
            if group not in expected_groups:
                raise ValueError(f"{path.name} line {lineno}: unknown group {group!r}")
            if not is_publishable_http_url(url):
                raise ValueError(f"{path.name} line {lineno}: invalid public URL {url!r}")
            if selection_key != canonical_channel_key(name):
                raise ValueError(
                    f"{path.name} line {lineno}: selection key does not match channel name"
                )
            if origin not in {"current_scan", "previous_publication"}:
                raise ValueError(f"{path.name} line {lineno}: invalid origin {origin!r}")
            dedup_key = (selection_key, url)
            if dedup_key in seen:
                raise ValueError(f"{path.name} line {lineno}: duplicate selection key/URL")
            seen.add(dedup_key)
            out.append(PoolCandidate(selection_key, Row(group, name, url), source, origin))
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
    historical_candidates = [
        candidate for candidate in pool
        if HISTORICAL_FALLBACK_ENABLED
        and candidate.origin == "previous_publication"
        and candidate.row.group in HISTORICAL_FALLBACK_GROUPS
    ]
    historical_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)
    historical_representatives: dict[tuple[str, str], Row] = {}
    for candidate in historical_candidates:
        key = row_identity(candidate.row)
        historical_by_key[key].add(candidate.row.url)
        historical_representatives.setdefault(key, candidate.row)
    historical_target_rows = 0
    for key, urls in historical_by_key.items():
        representative = historical_representatives[key]
        limit = per_channel_limit(representative.group, representative.name)
        previous_target = targets.get(key, 0)
        # Historical candidates are only the previous URLs absent from the
        # entire current candidate pool. Add that missing redundancy to the
        # current target instead of comparing the two counts independently.
        target = min(max(1, limit), previous_target + len(urls))
        if target > previous_target:
            targets[key] = target
            historical_target_rows += target - previous_target
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
            "historical_candidates_available": len(historical_candidates),
            "historical_target_rows": historical_target_rows,
            "historical_attempted_unique_urls": 0,
            "historical_playable_unique_urls": 0,
            "historical_refilled_rows": 0,
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
                    core_override=core,
                    require_progress=REQUIRE_BROADCAST_PROGRESS and requires_live_progress(candidate.row),
                    require_video=REQUIRE_VIDEO_TRACK,
                    require_decode=True,
                )
                futs[fut] = (key, candidate)
            for fut in cf.as_completed(futs):
                _key, candidate = futs[fut]
                round_results[candidate.row.url] = require_decoded_result(fut.result())

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
    historical_attempted = [candidate for candidate in attempted if candidate.origin == "previous_publication"]
    historical_accepted = [candidate for candidate in accepted if candidate.origin == "previous_publication"]
    historical_playable = sum(
        1 for candidate in historical_attempted
        if results.get(candidate.row.url) is not None and results[candidate.row.url].ok
    )
    summary = {
        "enabled": True,
        "channels_with_deficit": len(deficits),
        "target_rows": sum(deficits.values()),
        "attempted_unique_urls": len(results),
        "playable_unique_urls": sum(1 for result in results.values() if result.ok),
        "refilled_rows": len(accepted),
        "unresolved_rows": sum(remaining.values()),
        "historical_candidates_available": len(historical_candidates),
        "historical_target_rows": historical_target_rows,
        "historical_attempted_unique_urls": len(historical_attempted),
        "historical_playable_unique_urls": historical_playable,
        "historical_refilled_rows": len(historical_accepted),
    }
    return final_rows, results, summary, attempted, accepted


def update_summary(
    before_rows: list[Row],
    after_rows: list[Row],
    checked_urls: int,
    initial_failed_urls: dict[str, str],
    all_failed_urls: dict[str, str],
    elapsed: float,
    source_map: dict[tuple[str, str], str],
    stability_summary: dict,
    family_summary: dict,
    refill_summary: dict,
    retry_summary: dict[str, int],
    strict_progress_checked_unique: int,
) -> None:
    path = ROOT / SUMMARY_FILE
    summary = json.loads(path.read_text(encoding="utf-8"))
    cnt = Counter(row.group for row in after_rows)
    source_cnt = Counter(source_for(row, source_map) for row in after_rows)
    group_source_cnt = Counter(f"{row.group}|{source_for(row, source_map)}" for row in after_rows)
    removed_rows = sum(1 for row in before_rows if row.url in initial_failed_urls)
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
        "strict_video_checked_unique": checked_urls,
        "strict_progress_checked_unique": strict_progress_checked_unique,
        "family_playlist": family_summary,
        "stability": stability_summary,
        "published_recheck": {
            "enabled": True,
            "status": "ok",
            "outputs_rewritten": True,
            "candidate_after_rows": len(after_rows),
            "policy_version": RECHECK_POLICY_VERSION,
            "checked_unique_urls": checked_urls,
            "initial_checked_unique_urls": len({row.url for row in before_rows}),
            "before_rows": len(before_rows),
            "after_rows": len(after_rows),
            "removed_rows": removed_rows,
            "net_row_delta": len(after_rows) - len(before_rows),
            # Keep each phase distinct. The old initial_failed field was
            # accidentally populated after the slow retry, which made the
            # report impossible to interpret.
            "first_pass_failed_unique_urls": retry_summary.get("first_pass_failed_unique_urls", len(initial_failed_urls)),
            "slow_retry_attempted_unique_urls": retry_summary.get("attempted_unique_urls", 0),
            "slow_retry_recovered_unique_urls": retry_summary.get("recovered_unique_urls", 0),
            "post_retry_failed_unique_urls": retry_summary.get("still_failed_unique_urls", len(initial_failed_urls)),
            # Legacy alias: preserve compatibility, but define it as the
            # post-retry remainder rather than the first-pass failure count.
            "initial_failed_unique_urls": retry_summary.get("still_failed_unique_urls", len(initial_failed_urls)),
            "refill_failed_unique_urls": len(all_failed_urls) - len(initial_failed_urls),
            "failed_unique_urls": len(all_failed_urls),
            "core_progress_required": REQUIRE_CORE_PROGRESS,
            "broadcast_progress_required": REQUIRE_BROADCAST_PROGRESS,
            "progress_required_groups": sorted(LIVE_PROGRESS_GROUPS),
            "require_video_track": REQUIRE_VIDEO_TRACK,
            "require_frame_decode": True,
            "minimum_decoded_frames": MIN_DECODED_FRAMES,
            "frame_decoded_unique_urls": len({row.url for row in after_rows}),
            "video_track_verified_unique_urls": len({row.url for row in after_rows}),
            "audio_only_rejected_unique_urls": sum(
                1 for detail in all_failed_urls.values() if "audio/" in detail.lower() or " audio " in detail.lower()
            ),
            "unknown_track_rejected_unique_urls": sum(
                1 for detail in all_failed_urls.values() if "unknown/" in detail.lower() or "not observed" in detail.lower()
            ),
            "public_network_policy_enabled": True,
            "refill": refill_summary,
            "historical_fallback": {
                "enabled": HISTORICAL_FALLBACK_ENABLED,
                "groups": sorted(HISTORICAL_FALLBACK_GROUPS),
                "candidates_available": refill_summary.get("historical_candidates_available", 0),
                "target_rows": refill_summary.get("historical_target_rows", 0),
                "attempted_unique_urls": refill_summary.get("historical_attempted_unique_urls", 0),
                "playable_unique_urls": refill_summary.get("historical_playable_unique_urls", 0),
                "refilled_rows": refill_summary.get("historical_refilled_rows", 0),
            },
            "slow_retry": retry_summary,
            "elapsed_seconds": round(elapsed, 1),
        },
    })
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_report(before_rows: list[Row], after_rows: list[Row], failed_urls: dict[str, str], elapsed: float, refill_summary: dict | None = None, *, outputs_rewritten: bool = True) -> None:
    before_counts = Counter(row.group for row in before_rows)
    after_counts = Counter(row.group for row in after_rows)
    failed_rows = [row for row in before_rows if row.url in failed_urls]
    refill_summary = refill_summary or {}
    result_label = "Rows after" if outputs_rewritten else "Candidate rows after (not promoted)"
    lines = [
        "# Published playlist recheck report",
        "",
        f"Outputs rewritten: {outputs_rewritten}",
        f"Elapsed: {elapsed:.1f}s",
        f"Rows before: {len(before_rows)}",
        f"{result_label}: {len(after_rows)}",
        f"Rows removed from outputs: {len(failed_rows) if outputs_rewritten else 0}",
        f"Candidate rows failing strict recheck: {len(failed_rows)}",
        f"Rows refilled after strict recheck: {refill_summary.get('refilled_rows', 0)}",
        f"Net output row delta: {len(after_rows) - len(before_rows) if outputs_rewritten else 0:+d}",
        f"Failed unique URLs after slow retry: {len(failed_urls)}",
        f"Slow retry attempted unique URLs: {refill_summary.get('initial_retry', {}).get('attempted_unique_urls', 0)}",
        f"Slow retry recovered unique URLs: {refill_summary.get('initial_retry', {}).get('recovered_unique_urls', 0)}",
        f"Core live-progress check required: {REQUIRE_CORE_PROGRESS}",
        f"Broadcast live-progress check required: {REQUIRE_BROADCAST_PROGRESS}",
        f"Live-progress groups: {', '.join(sorted(LIVE_PROGRESS_GROUPS))}",
        f"Video track required: {REQUIRE_VIDEO_TRACK}",
        f"Video-track verified final unique URLs: {len({row.url for row in after_rows})}",
        f"Refill attempted unique URLs: {refill_summary.get('attempted_unique_urls', 0)}",
        f"Refill playable unique URLs: {refill_summary.get('playable_unique_urls', 0)}",
        f"Refilled rows: {refill_summary.get('refilled_rows', 0)}",
        f"Historical fallback candidates attempted: {refill_summary.get('historical_attempted_unique_urls', 0)}",
        f"Historical fallback rows accepted: {refill_summary.get('historical_refilled_rows', 0)}",
        f"Unresolved refill rows: {refill_summary.get('unresolved_rows', 0)}",
        "",
        "## Group deltas",
        "",
        "| Group | Before | After | Net delta |",
        "|---|---:|---:|---:|",
    ]
    for group in before_counts:
        lines.append(f"| {group} | {before_counts[group]} | {after_counts[group]} | {after_counts[group] - before_counts[group]:+d} |")
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
        f"Failed unique URLs after slow retry: {len(failed_urls)}",
        f"Slow retry attempted unique URLs: {refill_summary.get('initial_retry', {}).get('attempted_unique_urls', 0)}",
        f"Slow retry recovered unique URLs: {refill_summary.get('initial_retry', {}).get('recovered_unique_urls', 0)}",
        f"Refilled rows from checked candidate pool: {refill_summary.get('refilled_rows', 0)}",
        f"Unresolved refill rows: {refill_summary.get('unresolved_rows', 0)}",
        f"Core live-progress check required: {REQUIRE_CORE_PROGRESS}",
        f"Broadcast live-progress check required: {REQUIRE_BROADCAST_PROGRESS}",
        f"Live-progress groups: {', '.join(sorted(LIVE_PROGRESS_GROUPS))}",
        f"Final recheck elapsed: {elapsed:.1f}s",
        f"Source map available: {bool(source_map)}",
        f"Stability tracked URLs after pending observation: {stability_summary.get('tracked_urls_after')}",
        f"Pending stability OK/fail updates: {stability_summary.get('ok_updates')}/{stability_summary.get('fail_updates')}",
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
    global ROOT
    print(f"Frame decoder preflight: {decoder_preflight()}", flush=True)
    repository_root = ROOT
    recover_interrupted_promotion(repository_root)
    cleanup_stale_diagnostics()
    start = time.time()
    for filename in TXT_FILES:
        validate_file(ROOT / filename)
    _curated_groups, rows = parse_tv_txt(ROOT / "live-curated.txt")
    # Use the configured order, including categories that were empty before
    # historical refill. A recovered category must be publishable even when
    # curation emitted no header for it in this run.
    groups = get_group_order()
    source_map = load_source_map()
    pool_path = ROOT / CANDIDATE_POOL_FILE
    if not pool_path.exists():
        raise ValueError(f"missing required refill candidate pool: {pool_path.name}")
    candidate_pool = load_candidate_pool(pool_path)

    by_url: dict[str, Row] = {}
    for row in rows:
        by_url.setdefault(row.url, row)
    core_urls = {url for url, row in by_url.items() if is_core_row(row)}
    progress_urls = {url for url, row in by_url.items() if requires_live_progress(row)}
    print(
        f"Published recheck: rows={len(rows)} unique_urls={len(by_url)} "
        f"core_urls={len(core_urls)} progress_urls={len(progress_urls)} "
        f"broadcast_progress={REQUIRE_BROADCAST_PROGRESS} "
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
                REQUIRE_BROADCAST_PROGRESS and url in progress_urls,
                require_decode=True,
            )
            futs[fut] = url
        for i, fut in enumerate(cf.as_completed(futs), 1):
            url = futs[fut]
            results[url] = require_decoded_result(fut.result())
            if i % 100 == 0 or i == len(futs):
                ok_count = sum(1 for result in results.values() if result.ok)
                print(f"published_recheck {i}/{len(futs)} ok_urls={ok_count}", flush=True)

    retry_summary = retry_failed_final_urls(by_url, results, core_urls, progress_urls)
    write_results_csv(rows, results, [], {}, source_map=source_map)
    print("Published final slow retry", json.dumps(retry_summary, ensure_ascii=False, sort_keys=True), flush=True)
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
            "initial_retry": retry_summary,
        }
        write_results_csv(rows, results, source_map=source_map)
        write_report(rows, kept_rows, failed_urls, elapsed, refill_summary, outputs_rewritten=False)
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
        record_aborted_recheck(rows, kept_rows, len(by_url), len(failed_urls), elapsed, retry_summary, threshold)
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
    refill_summary["initial_retry"] = retry_summary
    for candidate in accepted_refills:
        source_map[(candidate.row.name, candidate.row.url)] = candidate.source
    write_results_csv(rows, results, attempted_refills, refill_results, source_map=source_map)

    elapsed = time.time() - start

    refill_failed_urls = {
        url: result.detail for url, result in refill_results.items() if not result.ok
    }
    all_failed_urls = dict(failed_urls)
    all_failed_urls.update(refill_failed_urls)
    stability_rows = rows + [candidate.row for candidate in attempted_refills]
    summary_before_recheck = json.loads((repository_root / SUMMARY_FILE).read_text(encoding="utf-8"))
    observation_id = os.getenv("IPTV_STABILITY_OBSERVATION_ID", "").strip()
    if not observation_id:
        observation_id = "manual:" + ":".join((
            str(summary_before_recheck.get("generated_utc") or "unknown"),
            str(summary_before_recheck.get("source_config_sha256") or "unknown"),
        ))
    observation = build_observation(stability_rows, all_failed_urls, source_map, observation_id)
    stability_summary = preview_observation(observation)
    checked_url_set = set(by_url) | set(refill_results)
    checked_urls = len(checked_url_set)

    strict_progress_urls: set[str] = set()
    if REQUIRE_BROADCAST_PROGRESS:
        strict_progress_urls.update(url for url in by_url if url in progress_urls)
        strict_progress_urls.update(
            result.cand.url
            for result in refill_results.values()
            if requires_live_progress(Row(result.cand.group, result.cand.name, result.cand.url))
        )
    strict_progress_checked_unique = len(strict_progress_urls)
    staged_root = prepare_staging_root(repository_root)
    shutil.copy2(repository_root / SUMMARY_FILE, staged_root / SUMMARY_FILE)
    ROOT = staged_root
    try:
        final_rows = write_outputs(groups, final_rows)
        write_source_map(final_rows, source_map)
        family_summary = write_family_outputs(groups, final_rows)
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
            retry_summary,
            strict_progress_checked_unique,
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
        write_results_csv(rows, results, attempted_refills, refill_results, source_map=source_map)
        write_observation(ROOT / PENDING_STABILITY_FILE, observation)
        for filename in [*TXT_FILES, M3U_FILE, *family_txt_files(), family_m3u_file()]:
            validate_file(ROOT / filename, require_categories=True)
        staged_summary = json.loads((ROOT / SUMMARY_FILE).read_text(encoding="utf-8"))
        if (staged_summary.get("stability") or {}).get("observation_id") != observation_id:
            raise ValueError("staged summary does not reference the pending stability observation")
    finally:
        ROOT = repository_root
    promoted_files = [
        *TXT_FILES,
        M3U_FILE,
        *family_txt_files(),
        family_m3u_file(),
        SOURCE_MAP_FILE,
        CSV_FILE,
        SUMMARY_FILE,
        REPORT_FILE,
        FINAL_REPORT_FILE,
        PENDING_STABILITY_FILE,
    ]
    promote_staged_outputs(staged_root, promoted_files, repository_root)
    print(
        "Published recheck done: "
        f"before={len(rows)} after={len(final_rows)} failed_urls={len(failed_urls)} "
        f"refill_attempts={len(refill_results)} refilled={refill_summary.get('refilled_rows', 0)} "
        f"unresolved={refill_summary.get('unresolved_rows', 0)} elapsed={elapsed:.1f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
