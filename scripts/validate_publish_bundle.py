#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate the complete set of publishable IPTV playlist artifacts.

This is intentionally stricter than validating each file in isolation.  A run
must not publish when aliases, M3U/TXT output, the compact family list, source
mapping, or summary metadata disagree with one another.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from channel_identity import aliases_are_compatible, canonical_channel_key
from playlist_config import get_group_order
from validate_playlist import split_unquoted_last_comma, validate_file

ROOT = Path(__file__).resolve().parents[1]
FULL_TXT_FILES = ("live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt")
FAMILY_TXT_FILES = ("ku9-family.txt", "live-family.txt")
FULL_M3U_FILE = "live.m3u"
FAMILY_M3U_FILE = "family.m3u"
SUMMARY_FILE = "full-check-summary.json"
SOURCE_MAP_FILE = "curated-source-map.csv"
CANDIDATE_POOL_FILE = "curated-candidate-pool.csv"
ALIAS_CONFLICT_REPORT = "alias-conflict-report.md"
SOURCES_STATUS_FILE = "sources_status.csv"


@dataclass(frozen=True)
class Row:
    group: str
    name: str
    url: str


class BundleValidationError(ValueError):
    pass


def _fail(errors: list[str]) -> None:
    if errors:
        preview = "\n - ".join(errors[:80])
        extra = f"\n - ... and {len(errors) - 80} more" if len(errors) > 80 else ""
        raise BundleValidationError(f"publish bundle validation failed:\n - {preview}{extra}")


def parse_txt_document(text: str) -> tuple[list[str], list[Row]]:
    groups: list[str] = []
    rows: list[Row] = []
    errors: list[str] = []
    current_group = ""
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.endswith(",#genre#"):
            group = line[:-len(",#genre#")].strip()
            if not group:
                errors.append(f"TXT line {lineno}: empty category")
            groups.append(group)
            current_group = group
            continue
        if not current_group:
            errors.append(f"TXT line {lineno}: channel appears before first category")
        if "," not in line:
            errors.append(f"TXT line {lineno}: missing channel/URL delimiter")
            continue
        name, url = line.split(",", 1)
        rows.append(Row(current_group, name.strip(), url.strip()))
    _fail(errors)
    return groups, rows


def parse_m3u_document(text: str) -> list[Row]:
    lines = [(lineno, raw.strip()) for lineno, raw in enumerate(text.splitlines(), 1) if raw.strip()]
    errors: list[str] = []
    rows: list[Row] = []
    if not lines or lines[0][1] != "#EXTM3U":
        errors.append("M3U: missing #EXTM3U header")
        _fail(errors)
    i = 1
    while i < len(lines):
        lineno, line = lines[i]
        if not line.startswith("#EXTINF"):
            errors.append(f"M3U line {lineno}: expected #EXTINF, got {line[:120]!r}")
            i += 1
            continue
        head, display_name = split_unquoted_last_comma(line)
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', head))
        group = html.unescape((attrs.get("group-title") or "").strip())
        tvg_name = html.unescape((attrs.get("tvg-name") or "").strip())
        name = (display_name or tvg_name).strip()
        if i + 1 >= len(lines):
            errors.append(f"M3U line {lineno}: missing URL after EXTINF")
            break
        url_lineno, url = lines[i + 1]
        if url.startswith("#"):
            errors.append(f"M3U line {url_lineno}: expected URL, got {url[:120]!r}")
            i += 1
            continue
        rows.append(Row(group, name, url.strip()))
        i += 2
    _fail(errors)
    return rows


def _validate_document_invariants(label: str, groups: list[str], rows: list[Row], errors: list[str]) -> None:
    expected_groups = get_group_order()
    if groups != expected_groups:
        errors.append(f"{label}: category order/coverage mismatch: actual={groups!r} expected={expected_groups!r}")
    duplicates = [row for row, count in Counter(rows).items() if count > 1]
    if duplicates:
        errors.append(f"{label}: exact duplicate rows found: {duplicates[:10]!r}")

    names_by_url: dict[str, list[str]] = defaultdict(list)
    groups_by_identity: dict[str, set[str]] = defaultdict(set)
    labels_by_identity: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        names_by_url[row.url].append(row.name)
        identity = canonical_channel_key(row.name)
        groups_by_identity[identity].add(row.group)
        labels_by_identity[identity].add(row.name)
    url_conflicts = {
        url: sorted(set(names))
        for url, names in names_by_url.items()
        if not aliases_are_compatible(names)
    }
    if url_conflicts:
        errors.append(f"{label}: URLs mapped to incompatible channel identities: {list(url_conflicts.items())[:10]!r}")
    category_conflicts = {
        identity: {"groups": sorted(groups_by_identity[identity]), "names": sorted(labels_by_identity[identity])}
        for identity in groups_by_identity
        if len(groups_by_identity[identity]) > 1
    }
    if category_conflicts:
        errors.append(f"{label}: canonical channel identities span categories: {list(category_conflicts.items())[:10]!r}")


def _ordered_subset(subset: list[Row], full: list[Row]) -> bool:
    pos = 0
    for wanted in subset:
        while pos < len(full) and full[pos] != wanted:
            pos += 1
        if pos >= len(full):
            return False
        pos += 1
    return True


def _check_equal(actual, expected, label: str, errors: list[str]) -> None:
    if actual != expected:
        errors.append(f"{label}: actual={actual!r} expected={expected!r}")


def _require_fields(mapping: dict, fields: tuple[str, ...], label: str, errors: list[str]) -> None:
    missing = [field for field in fields if field not in mapping]
    if missing:
        errors.append(f"{label}: missing required fields {missing!r}")


def _validate_summary(
    summary: dict,
    full_rows: list[Row],
    family_rows: list[Row],
    sources: list[str],
    errors: list[str],
    *,
    require_extended_schema: bool = True,
) -> None:
    if not isinstance(summary, dict):
        errors.append("summary root must be a JSON object")
        return

    required_top_level = (
        "sources_total",
        "sources_fetched_ok",
        "checked_all_unique",
        "checked_candidates",
        "unique_candidates",
        "unique_name_url_candidates",
        "playable_unique_urls",
        "playable_name_url_lines",
        "playable_urls_found",
        "all_playable_lines",
        "curated_generated",
        "curated_source_map_available",
        "curated_source_map_generated",
        "curated_source_map_artifact_only",
        "curated_candidate_pool_generated",
        "curated_candidate_pool_artifact_only",
        "curated_published_lines",
        "final_primary_published_lines",
        "primary_published_lines",
        "curated_channel_names",
        "curated_groups",
        "curated_sources",
        "coverage",
        "quality_audit",
        "published_recheck",
        "stability",
        "family_playlist",
    )
    if require_extended_schema:
        required_top_level += (
            "broad_media_probe_checked",
            "broad_checked_all_unique",
            "strict_video_checked_unique",
            "strict_progress_checked_unique",
        )
    _require_fields(summary, required_top_level, "summary", errors)

    full_groups = dict(Counter(row.group for row in full_rows))
    full_sources = dict(Counter(sources))
    full_names = len({row.name for row in full_rows})
    full_urls = len({row.url for row in full_rows})

    if "broad_checked_all_unique" in summary:
        if summary.get("broad_checked_all_unique") is not True:
            errors.append("summary.broad_checked_all_unique must be true")
        if summary.get("checked_all_unique") != summary.get("broad_checked_all_unique"):
            errors.append("summary.checked_all_unique must be the legacy alias of broad_checked_all_unique")
    elif summary.get("checked_all_unique") is not True:
        errors.append("summary.checked_all_unique must be true")
    if "checked_candidates" in summary and "unique_candidates" in summary:
        _check_equal(summary["checked_candidates"], summary["unique_candidates"], "summary checked/unique candidates", errors)
    if "broad_media_probe_checked" in summary and "unique_candidates" in summary:
        _check_equal(
            summary["broad_media_probe_checked"],
            summary["unique_candidates"],
            "summary broad media probe/unique candidates",
            errors,
        )
    for field in ("strict_video_checked_unique", "strict_progress_checked_unique"):
        if field not in summary and not require_extended_schema:
            continue
        value = summary.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            errors.append(f"summary.{field} must be a non-negative integer")
    try:
        if summary["strict_progress_checked_unique"] > summary["strict_video_checked_unique"]:
            errors.append("summary.strict_progress_checked_unique exceeds strict_video_checked_unique")
    except (KeyError, TypeError):
        pass
    if "unique_name_url_candidates" in summary and "unique_candidates" in summary:
        try:
            if summary["unique_name_url_candidates"] < summary["unique_candidates"]:
                errors.append("summary.unique_name_url_candidates is smaller than unique_candidates")
        except TypeError:
            errors.append("summary unique candidate counts must be numeric")
    if summary.get("curated_generated") is not True:
        errors.append("summary.curated_generated must be true")
    for field in (
        "curated_source_map_available",
        "curated_source_map_generated",
        "curated_source_map_artifact_only",
        "curated_candidate_pool_generated",
        "curated_candidate_pool_artifact_only",
    ):
        if summary.get(field) is not True:
            errors.append(f"summary.{field} must be true")
    try:
        if summary.get("playable_unique_urls", 0) <= 0:
            errors.append("summary.playable_unique_urls must be positive")
    except TypeError:
        errors.append("summary.playable_unique_urls must be numeric")
    for left, right in (("playable_name_url_lines", "all_playable_lines"), ("playable_urls_found", "all_playable_lines")):
        if left in summary and right in summary:
            _check_equal(summary[left], summary[right], f"summary.{left}/{right}", errors)
    for field in ("curated_published_lines", "final_primary_published_lines", "primary_published_lines"):
        if field in summary:
            _check_equal(summary[field], len(full_rows), f"summary.{field}", errors)
    if "curated_channel_names" in summary:
        _check_equal(summary["curated_channel_names"], full_names, "summary.curated_channel_names", errors)
    if "curated_groups" in summary:
        _check_equal(summary["curated_groups"], full_groups, "summary.curated_groups", errors)
    if "curated_sources" in summary:
        _check_equal(summary["curated_sources"], full_sources, "summary.curated_sources", errors)

    coverage = summary.get("coverage")
    if not isinstance(coverage, dict):
        errors.append("summary.coverage must be an object")
        coverage = {}
    _require_fields(coverage, ("missing_cctv", "missing_satellite"), "summary.coverage", errors)
    if coverage.get("missing_cctv"):
        errors.append(f"summary.coverage.missing_cctv is not empty: {coverage.get('missing_cctv')!r}")
    if coverage.get("missing_satellite"):
        errors.append(f"summary.coverage.missing_satellite is not empty: {coverage.get('missing_satellite')!r}")

    quality = summary.get("quality_audit")
    if not isinstance(quality, dict):
        errors.append("summary.quality_audit must be an object")
        quality = {}
    _require_fields(
        quality,
        (
            "status",
            "rows",
            "unique_names",
            "unique_urls",
            "groups",
            "strict_filter_residue",
            "missing_cctv_quality",
            "missing_satellite_quality",
        ),
        "summary.quality_audit",
        errors,
    )
    for field, expected in (
        ("rows", len(full_rows)),
        ("unique_names", full_names),
        ("unique_urls", full_urls),
        ("groups", full_groups),
    ):
        if field in quality:
            _check_equal(quality[field], expected, f"summary.quality_audit.{field}", errors)
    if quality.get("status") != "ok":
        errors.append(f"summary.quality_audit.status is not ok: {quality.get('status')!r}")
    for field in ("strict_filter_residue", "missing_cctv_quality", "missing_satellite_quality"):
        if quality.get(field):
            errors.append(f"summary.quality_audit.{field} is not empty")

    recheck = summary.get("published_recheck")
    if not isinstance(recheck, dict):
        errors.append("summary.published_recheck must be an object")
        recheck = {}
    required_recheck_fields = (
        "core_progress_required",
        "require_video_track",
        "video_track_verified_unique_urls",
        "public_network_policy_enabled",
        "checked_unique_urls",
        "initial_checked_unique_urls",
        "initial_failed_unique_urls",
        "refill_failed_unique_urls",
        "failed_unique_urls",
        "before_rows",
        "after_rows",
        "removed_rows",
        "refill",
    )
    if require_extended_schema:
        required_recheck_fields += (
            "first_pass_failed_unique_urls",
            "slow_retry_attempted_unique_urls",
            "slow_retry_recovered_unique_urls",
            "post_retry_failed_unique_urls",
            "slow_retry",
        )
    _require_fields(recheck, required_recheck_fields, "summary.published_recheck", errors)
    if recheck.get("core_progress_required") is not True:
        errors.append("summary.published_recheck.core_progress_required must be true")
    if recheck.get("require_video_track") is not True:
        errors.append("summary.published_recheck.require_video_track must be true")
    if recheck.get("public_network_policy_enabled") is not True:
        errors.append("summary.published_recheck.public_network_policy_enabled must be true")
    if "video_track_verified_unique_urls" in recheck:
        _check_equal(
            recheck["video_track_verified_unique_urls"],
            full_urls,
            "summary.published_recheck.video_track_verified_unique_urls",
            errors,
        )
    if "after_rows" in recheck:
        _check_equal(recheck["after_rows"], len(full_rows), "summary.published_recheck.after_rows", errors)
    if "checked_unique_urls" in recheck and "strict_video_checked_unique" in summary:
        _check_equal(
            summary["strict_video_checked_unique"],
            recheck["checked_unique_urls"],
            "summary strict video/recheck checked URL counts",
            errors,
        )
    numeric_fields = (
        "checked_unique_urls",
        "initial_checked_unique_urls",
        "first_pass_failed_unique_urls",
        "slow_retry_attempted_unique_urls",
        "slow_retry_recovered_unique_urls",
        "post_retry_failed_unique_urls",
        "initial_failed_unique_urls",
        "refill_failed_unique_urls",
        "failed_unique_urls",
        "before_rows",
        "after_rows",
        "removed_rows",
    )
    for field in numeric_fields:
        if field not in recheck:
            continue
        value = recheck[field]
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            errors.append(f"summary.published_recheck.{field} must be a non-negative integer")
    try:
        if recheck["checked_unique_urls"] < recheck["initial_checked_unique_urls"]:
            errors.append("summary.published_recheck.checked_unique_urls is smaller than initial_checked_unique_urls")
        if "first_pass_failed_unique_urls" in recheck:
            if recheck["first_pass_failed_unique_urls"] > recheck["initial_checked_unique_urls"]:
                errors.append("summary.published_recheck.first_pass_failed_unique_urls exceeds initial_checked_unique_urls")
            if recheck["slow_retry_attempted_unique_urls"] > recheck["first_pass_failed_unique_urls"]:
                errors.append("summary.published_recheck slow retry attempted count exceeds first-pass failures")
            if recheck["slow_retry_recovered_unique_urls"] > recheck["slow_retry_attempted_unique_urls"]:
                errors.append("summary.published_recheck slow retry recovered count exceeds attempted count")
            if recheck["post_retry_failed_unique_urls"] != (
                recheck["first_pass_failed_unique_urls"] - recheck["slow_retry_recovered_unique_urls"]
            ):
                errors.append("summary.published_recheck post-retry failure count is inconsistent")
            if recheck["initial_failed_unique_urls"] != recheck["post_retry_failed_unique_urls"]:
                errors.append("summary.published_recheck legacy initial_failed count must equal post-retry failures")
            failed_before_refill = recheck["post_retry_failed_unique_urls"]
        else:
            failed_before_refill = recheck["initial_failed_unique_urls"]
        if recheck["failed_unique_urls"] != failed_before_refill + recheck["refill_failed_unique_urls"]:
            errors.append("summary.published_recheck failed URL counts are inconsistent")
        if recheck["removed_rows"] != recheck["before_rows"] - recheck["after_rows"]:
            errors.append("summary.published_recheck removed_rows is inconsistent")
    except (KeyError, TypeError):
        pass

    slow_retry = recheck.get("slow_retry")
    if slow_retry is None and not require_extended_schema:
        slow_retry = {}
    elif not isinstance(slow_retry, dict):
        errors.append("summary.published_recheck.slow_retry must be an object")
        slow_retry = {}
    for nested, flat in (
        ("first_pass_failed_unique_urls", "first_pass_failed_unique_urls"),
        ("attempted_unique_urls", "slow_retry_attempted_unique_urls"),
        ("recovered_unique_urls", "slow_retry_recovered_unique_urls"),
        ("still_failed_unique_urls", "post_retry_failed_unique_urls"),
    ):
        if nested in slow_retry and flat in recheck:
            _check_equal(
                slow_retry[nested],
                recheck[flat],
                f"summary.published_recheck.slow_retry.{nested}",
                errors,
            )

    refill = recheck.get("refill")
    if not isinstance(refill, dict):
        errors.append("summary.published_recheck.refill must be an object")
        refill = {}
    _require_fields(refill, ("enabled",), "summary.published_recheck.refill", errors)
    if refill.get("enabled") is not True:
        errors.append("summary.published_recheck.refill.enabled must be true")
    _require_fields(
        refill,
        ("attempted_unique_urls", "playable_unique_urls", "refilled_rows", "unresolved_rows"),
        "summary.published_recheck.refill",
        errors,
    )
    for field in ("attempted_unique_urls", "playable_unique_urls", "refilled_rows", "unresolved_rows"):
        value = refill.get(field)
        if field in refill and (not isinstance(value, int) or isinstance(value, bool) or value < 0):
            errors.append(f"summary.published_recheck.refill.{field} must be a non-negative integer")
    try:
        attempted = refill["attempted_unique_urls"]
        playable = refill["playable_unique_urls"]
        if recheck["checked_unique_urls"] != recheck["initial_checked_unique_urls"] + attempted:
            errors.append("summary.published_recheck checked/refill attempt counts are inconsistent")
        if recheck["refill_failed_unique_urls"] != attempted - playable:
            errors.append("summary.published_recheck refill failure counts are inconsistent")
        if refill["refilled_rows"] > playable:
            errors.append("summary.published_recheck.refill.refilled_rows exceeds playable_unique_urls")
    except (KeyError, TypeError):
        pass

    stability = summary.get("stability")
    if not isinstance(stability, dict):
        errors.append("summary.stability must be an object")
        stability = {}
    _require_fields(stability, ("enabled", "updated_urls", "tracked_urls_after"), "summary.stability", errors)
    if stability.get("enabled") is not True:
        errors.append("summary.stability.enabled must be true")
    if "updated_urls" in stability and "checked_unique_urls" in recheck:
        _check_equal(stability["updated_urls"], recheck["checked_unique_urls"], "summary stability/recheck URL counts", errors)
    if "tracked_urls_after" in stability and "checked_unique_urls" in recheck:
        try:
            if stability["tracked_urls_after"] < recheck["checked_unique_urls"]:
                errors.append("summary.stability.tracked_urls_after is smaller than published recheck count")
        except TypeError:
            errors.append("summary stability/recheck URL counts must be numeric")

    family = summary.get("family_playlist")
    if not isinstance(family, dict):
        errors.append("summary.family_playlist must be an object")
        family = {}
    _require_fields(family, ("enabled", "lines", "unique_names", "unique_urls", "groups"), "summary.family_playlist", errors)
    if family.get("enabled") is not True:
        errors.append("summary.family_playlist.enabled must be true")
    family_groups = dict(Counter(row.group for row in family_rows))
    for field, expected in (
        ("lines", len(family_rows)),
        ("unique_names", len({row.name for row in family_rows})),
        ("unique_urls", len({row.url for row in family_rows})),
        ("groups", family_groups),
    ):
        if field in family:
            _check_equal(family[field], expected, f"summary.family_playlist.{field}", errors)



def _validate_candidate_pool(path: Path, full_rows: list[Row], sources: list[str], errors: list[str]) -> None:
    expected_header = ["selection_key", "group", "name", "url", "source"]
    expected_groups = set(get_group_order())
    pool_records: set[tuple[str, str, str, str]] = set()
    seen_identity_urls: set[tuple[str, str]] = set()
    names_by_url: dict[str, list[str]] = defaultdict(list)

    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != expected_header:
            errors.append(f"{CANDIDATE_POOL_FILE}: header must be {expected_header!r}, got {reader.fieldnames!r}")
        items = list(reader)

    if not items:
        errors.append(f"{CANDIDATE_POOL_FILE}: candidate pool is empty")
        return

    for lineno, item in enumerate(items, 2):
        selection_key = (item.get("selection_key") or "").strip()
        group = (item.get("group") or "").strip()
        name = (item.get("name") or "").strip()
        url = (item.get("url") or "").strip()
        source = (item.get("source") or "").strip()
        missing = [
            field
            for field, value in (
                ("selection_key", selection_key),
                ("group", group),
                ("name", name),
                ("url", url),
                ("source", source),
            )
            if not value
        ]
        if missing:
            errors.append(f"{CANDIDATE_POOL_FILE} line {lineno}: empty fields {missing!r}")
            continue
        if group not in expected_groups:
            errors.append(f"{CANDIDATE_POOL_FILE} line {lineno}: unknown group {group!r}")
        canonical = canonical_channel_key(name)
        if not canonical or selection_key != canonical:
            errors.append(
                f"{CANDIDATE_POOL_FILE} line {lineno}: selection_key {selection_key!r} "
                f"does not match canonical channel key {canonical!r}"
            )
        if not re.fullmatch(r"https?://\S+", url, flags=re.IGNORECASE):
            errors.append(f"{CANDIDATE_POOL_FILE} line {lineno}: invalid public playlist URL {url!r}")
        dedup_key = (selection_key, url)
        if dedup_key in seen_identity_urls:
            errors.append(f"{CANDIDATE_POOL_FILE} line {lineno}: duplicate selection_key/URL {dedup_key!r}")
        seen_identity_urls.add(dedup_key)
        pool_records.add((group, name, url, source))
        names_by_url[url].append(name)

    conflicts = {
        url: sorted(set(names))
        for url, names in names_by_url.items()
        if not aliases_are_compatible(names)
    }
    if conflicts:
        errors.append(
            f"{CANDIDATE_POOL_FILE}: URLs mapped to incompatible channel identities: "
            f"{list(conflicts.items())[:10]!r}"
        )

    selected_records = {(row.group, row.name, row.url, source) for row, source in zip(full_rows, sources)}
    missing_selected = sorted(selected_records - pool_records)
    if missing_selected:
        errors.append(
            f"{CANDIDATE_POOL_FILE}: final published rows are missing from the candidate pool: "
            f"{missing_selected[:10]!r}"
        )

def validate_publish_bundle(
    root: Path = ROOT,
    *,
    require_artifacts: bool = True,
) -> dict:
    """Validate either a complete workflow bundle or only committed outputs.

    ``require_artifacts=True`` is the publication gate used inside the full
    maintenance workflow, where artifact-only provenance files must exist.
    ``False`` is intended for ordinary clones and read-only CI, where those
    large diagnostic files are deliberately absent from Git.
    """
    root = Path(root)
    errors: list[str] = []
    required = [
        *FULL_TXT_FILES,
        *FAMILY_TXT_FILES,
        FULL_M3U_FILE,
        FAMILY_M3U_FILE,
        SUMMARY_FILE,
        SOURCES_STATUS_FILE,
    ]
    if require_artifacts:
        required.extend((SOURCE_MAP_FILE, CANDIDATE_POOL_FILE, ALIAS_CONFLICT_REPORT))
    missing = [name for name in required if not (root / name).is_file()]
    if missing:
        raise BundleValidationError(f"missing publish bundle files: {missing!r}")

    for name in [*FULL_TXT_FILES, *FAMILY_TXT_FILES, FULL_M3U_FILE, FAMILY_M3U_FILE]:
        try:
            validate_file(root / name, require_categories=True)
        except Exception as exc:
            errors.append(f"{name}: standalone validation failed: {exc}")

    full_payloads = [(root / name).read_bytes() for name in FULL_TXT_FILES]
    if len(set(full_payloads)) != 1:
        errors.append(f"full TXT aliases are not byte-identical: {list(FULL_TXT_FILES)!r}")
    family_payloads = [(root / name).read_bytes() for name in FAMILY_TXT_FILES]
    if len(set(family_payloads)) != 1:
        errors.append(f"family TXT aliases are not byte-identical: {list(FAMILY_TXT_FILES)!r}")

    full_groups, full_rows = parse_txt_document(full_payloads[0].decode("utf-8"))
    family_groups, family_rows = parse_txt_document(family_payloads[0].decode("utf-8"))
    _validate_document_invariants("full playlist", full_groups, full_rows, errors)
    _validate_document_invariants("family playlist", family_groups, family_rows, errors)

    full_m3u_rows = parse_m3u_document((root / FULL_M3U_FILE).read_text(encoding="utf-8"))
    family_m3u_rows = parse_m3u_document((root / FAMILY_M3U_FILE).read_text(encoding="utf-8"))
    if full_m3u_rows != full_rows:
        errors.append("live.m3u rows/order do not exactly match full TXT playlist")
    if family_m3u_rows != family_rows:
        errors.append("family.m3u rows/order do not exactly match family TXT playlist")
    if not _ordered_subset(family_rows, full_rows):
        errors.append("family playlist is not an ordered subset of the full playlist")

    try:
        summary = json.loads((root / SUMMARY_FILE).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{SUMMARY_FILE}: invalid JSON: {exc}")
        summary = {}

    sources: list[str] = []
    if require_artifacts:
        source_rows: list[Row] = []
        with (root / SOURCE_MAP_FILE).open(encoding="utf-8", newline="") as f:
            source_reader = csv.DictReader(f)
            expected_source_header = ["group", "name", "url", "source"]
            if source_reader.fieldnames != expected_source_header:
                errors.append(
                    f"{SOURCE_MAP_FILE}: header must be {expected_source_header!r}, got {source_reader.fieldnames!r}"
                )
            for item in source_reader:
                source_rows.append(
                    Row(
                        (item.get("group") or "").strip(),
                        (item.get("name") or "").strip(),
                        (item.get("url") or "").strip(),
                    )
                )
                sources.append((item.get("source") or "").strip())
        if source_rows != full_rows:
            errors.append("curated-source-map.csv rows/order do not exactly match full playlist")
        if any(not source for source in sources):
            errors.append("curated-source-map.csv contains an empty source")
        _validate_candidate_pool(root / CANDIDATE_POOL_FILE, full_rows, sources, errors)
        if not (root / ALIAS_CONFLICT_REPORT).read_text(encoding="utf-8").strip():
            errors.append(f"{ALIAS_CONFLICT_REPORT}: report is empty")
    else:
        curated_sources = summary.get("curated_sources") if isinstance(summary, dict) else None
        if not isinstance(curated_sources, dict):
            errors.append("summary.curated_sources must be an object")
        else:
            for source, count in curated_sources.items():
                if not isinstance(source, str) or not source.strip():
                    errors.append("summary.curated_sources contains an empty source name")
                    continue
                if not isinstance(count, int) or isinstance(count, bool) or count < 0:
                    errors.append(f"summary.curated_sources[{source!r}] must be a non-negative integer")
                    continue
                sources.extend([source] * count)
            if len(sources) != len(full_rows):
                errors.append(
                    "summary.curated_sources counts do not sum to the committed full playlist row count"
                )

    with (root / SOURCES_STATUS_FILE).open(encoding="utf-8", newline="") as f:
        status_reader = csv.DictReader(f)
        expected_status_header = ["name", "url", "fetch_ok", "bytes", "parsed", "truncated", "error"]
        if status_reader.fieldnames != expected_status_header:
            errors.append(
                f"{SOURCES_STATUS_FILE}: header must be {expected_status_header!r}, got {status_reader.fieldnames!r}"
            )
        source_statuses = list(status_reader)
    status_pairs = [((item.get("name") or "").strip(), (item.get("url") or "").strip()) for item in source_statuses]
    status_names = [name for name, _url in status_pairs]
    if any(not name for name in status_names):
        errors.append(f"{SOURCES_STATUS_FILE}: contains an empty source name")
    if any(not url for _name, url in status_pairs):
        errors.append(f"{SOURCES_STATUS_FILE}: contains an empty source URL")
    if len(status_names) != len(set(status_names)):
        errors.append(f"{SOURCES_STATUS_FILE}: contains duplicate source names")
    bad_fetch_values = sorted({str(item.get("fetch_ok") or "") for item in source_statuses} - {"True", "False"})
    if bad_fetch_values:
        errors.append(f"{SOURCES_STATUS_FILE}: invalid fetch_ok values {bad_fetch_values!r}")
    bad_truncated_values = sorted({str(item.get("truncated") or "") for item in source_statuses} - {"True", "False"})
    if bad_truncated_values:
        errors.append(f"{SOURCES_STATUS_FILE}: invalid truncated values {bad_truncated_values!r}")
    for item in source_statuses:
        for field in ("bytes", "parsed"):
            try:
                value = int(item.get(field) or 0)
                if value < 0:
                    raise ValueError
            except ValueError:
                errors.append(f"{SOURCES_STATUS_FILE}: source {item.get('name')!r} has invalid {field}")
    if "sources_total" in summary:
        _check_equal(summary["sources_total"], len(source_statuses), "summary.sources_total/sources_status rows", errors)
    if "sources_fetched_ok" in summary:
        fetched_ok = sum(item.get("fetch_ok") == "True" for item in source_statuses)
        _check_equal(summary["sources_fetched_ok"], fetched_ok, "summary.sources_fetched_ok/sources_status", errors)
    config_path = root / "config" / "sources.json"
    if config_path.is_file():
        try:
            configured = json.loads(config_path.read_text(encoding="utf-8-sig"))
            enabled_pairs = [
                (str(item.get("name") or "").strip(), str(item.get("url") or "").strip())
                for item in configured
                if item.get("enabled") is not False
            ]
            if status_pairs != enabled_pairs:
                errors.append(f"{SOURCES_STATUS_FILE}: source name/URL order does not match enabled config/sources.json")
        except Exception as exc:
            errors.append(f"config/sources.json: invalid JSON: {exc}")

    _validate_summary(
        summary,
        full_rows,
        family_rows,
        sources,
        errors,
        require_extended_schema=require_artifacts,
    )
    _fail(errors)
    return {
        "status": "ok",
        "mode": "strict" if require_artifacts else "committed-only",
        "full_rows": len(full_rows),
        "full_unique_names": len({row.name for row in full_rows}),
        "full_unique_urls": len({row.url for row in full_rows}),
        "family_rows": len(family_rows),
        "groups": dict(Counter(row.group for row in full_rows)),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--strict",
        action="store_true",
        help="require artifact-only provenance files (default; publication workflow mode)",
    )
    mode.add_argument(
        "--committed-only",
        action="store_true",
        help="validate only files intentionally committed to an ordinary clone",
    )
    parser.add_argument("root", nargs="?", type=Path, default=ROOT, help="repository root")
    args = parser.parse_args(argv)
    result = validate_publish_bundle(args.root, require_artifacts=not args.committed_only)
    print("publish bundle validation OK " + json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
