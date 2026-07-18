#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from channel_utils import cctv_key, is_latin_noise_name
from channel_identity import aliases_are_compatible, canonical_channel_key
from curate_ku9 import per_channel_limit, strict_quality_drop_reason
from playlist_config import get_group_order, load_quality, load_rules
from validate_playlist import validate_file

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / "live-curated.txt"
FAMILY_PLAYLIST = ROOT / "ku9-family.txt"
SUMMARY = ROOT / "full-check-summary.json"
REPORT = ROOT / "quality-audit-report.md"


def parse_txt(path: Path = PLAYLIST) -> list[tuple[str, str, str]]:
    validate_file(path, require_categories=True)
    rows: list[tuple[str, str, str]] = []
    group = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.endswith(",#genre#"):
            group = line.split(",", 1)[0].strip()
            continue
        name, url = line.split(",", 1)
        rows.append((group, name, url))
    return rows


def core_url_audit(rows: list[tuple[str, str, str]], rules: dict, audit_cfg: dict) -> dict:
    cctv_urls: dict[str, set[str]] = defaultdict(set)
    cctv_rows: Counter[str] = Counter()
    identity_urls: dict[str, set[str]] = defaultdict(set)
    identity_rows: Counter[str] = Counter()
    for _group, name, url in rows:
        identity = canonical_channel_key(name)
        identity_urls[identity].add(url)
        identity_rows[identity] += 1
        key = cctv_key(name)
        if key:
            cctv_urls[key].add(url)
            cctv_rows[key] += 1

    required_cctv = list(rules.get("coverage", {}).get("required_cctv", []))
    important_satellite = list(rules.get("coverage", {}).get("important_satellite", []))
    min_cctv = int(audit_cfg.get("min_exact_cctv_unique_urls", audit_cfg.get("min_exact_cctv_lines", 1)))
    min_sat = int(audit_cfg.get("min_important_satellite_unique_urls", audit_cfg.get("min_important_satellite_lines", 1)))
    warn_cctv = int(audit_cfg.get("warn_exact_cctv_unique_urls_below", audit_cfg.get("warn_exact_cctv_lines_below", min_cctv)))
    warn_sat = int(audit_cfg.get("warn_important_satellite_unique_urls_below", audit_cfg.get("warn_important_satellite_lines_below", min_sat)))
    cctv_items = [
        {
            "name": name,
            "published_rows": cctv_rows.get(name, 0),
            "unique_urls": len(cctv_urls.get(name, set())),
            "count": len(cctv_urls.get(name, set())),
        }
        for name in required_cctv
    ]
    sat_items = []
    for name in important_satellite:
        key = canonical_channel_key(name)
        sat_items.append({
            "name": name,
            "published_rows": identity_rows.get(key, 0),
            "unique_urls": len(identity_urls.get(key, set())),
            "count": len(identity_urls.get(key, set())),
        })
    return {
        "min_cctv": min_cctv,
        "min_satellite": min_sat,
        "warn_cctv": warn_cctv,
        "warn_satellite": warn_sat,
        "required_cctv": cctv_items,
        "important_satellite": sat_items,
    }


def build_audit(rows: list[tuple[str, str, str]]) -> tuple[dict, list[str], list[str]]:
    rules = load_rules()
    quality = load_quality()
    audit_cfg = quality.get("final_quality_audit", {})
    group_order = get_group_order()
    group_counts = Counter(group for group, _, _ in rows)
    by_identity: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    url_names: dict[str, set[str]] = defaultdict(set)
    strict_residue: list[dict] = []
    latin_noise: list[dict] = []
    for group, name, url in rows:
        by_identity[canonical_channel_key(name)].append((group, name, url))
        url_names[url].add(name)
        reason = strict_quality_drop_reason(name)
        if reason:
            strict_residue.append({"group": group, "name": name, "url": url, "reason": reason})
        if is_latin_noise_name(name):
            latin_noise.append({"group": group, "name": name, "url": url})

    core = core_url_audit(rows, rules, audit_cfg)
    missing_cctv_quality = [x for x in core["required_cctv"] if x["unique_urls"] < core["min_cctv"]]
    missing_satellite_quality = [x for x in core["important_satellite"] if x["unique_urls"] < core["min_satellite"]]
    weak_cctv = [x for x in core["required_cctv"] if core["min_cctv"] <= x["unique_urls"] < core["warn_cctv"]]
    weak_satellite = [x for x in core["important_satellite"] if core["min_satellite"] <= x["unique_urls"] < core["warn_satellite"]]

    channel_limit_violations: list[dict] = []
    identity_group_conflicts: list[dict] = []
    for identity, items in by_identity.items():
        groups = {group for group, _name, _url in items}
        names = {name for _group, name, _url in items}
        unique_urls = {url for _group, _name, url in items}
        group, name, _url = items[0]
        limit = per_channel_limit(group, name)
        if len(unique_urls) > limit:
            channel_limit_violations.append({"group": group, "name": name, "identity": identity, "published_rows": len(items), "unique_urls": len(unique_urls), "limit": limit})
        if len(groups) > 1:
            identity_group_conflicts.append({"identity": identity, "groups": sorted(groups), "names": sorted(names)})

    url_identity_conflicts = [
        {"url": url, "names": sorted(names)}
        for url, names in url_names.items()
        if not aliases_are_compatible(list(names))
    ]
    group_limit_violations: list[dict] = []
    group_max_rows = {str(k): int(v) for k, v in quality.get("group_max_rows", {}).items()}
    for group, limit in group_max_rows.items():
        count = int(group_counts.get(group, 0))
        if limit > 0 and count > limit:
            group_limit_violations.append({"group": group, "count": count, "limit": limit})

    failures: list[str] = []
    warnings: list[str] = []
    if audit_cfg.get("fail_on_strict_filter_residue", True) and strict_residue:
        failures.append(f"strict filtered channel residue remains: {len(strict_residue)} rows")
    if missing_cctv_quality:
        failures.append("core CCTV channels below independent URL minimum: " + ", ".join(f"{x['name']}={x['unique_urls']}" for x in missing_cctv_quality))
    if missing_satellite_quality:
        failures.append("important satellite channels below independent URL minimum: " + ", ".join(f"{x['name']}={x['unique_urls']}" for x in missing_satellite_quality))
    if audit_cfg.get("fail_on_channel_limit_violation", True) and channel_limit_violations:
        failures.append(f"channel unique URL limit violations: {len(channel_limit_violations)}")
    if audit_cfg.get("fail_on_group_limit_violation", True) and group_limit_violations:
        failures.append(f"group line limit violations: {len(group_limit_violations)}")
    if identity_group_conflicts:
        failures.append(f"canonical channel identities span multiple groups: {len(identity_group_conflicts)}")
    if url_identity_conflicts:
        failures.append(f"URLs assigned to incompatible channel identities: {len(url_identity_conflicts)}")
    if weak_cctv:
        warnings.append("core CCTV channels below independent URL warning target: " + ", ".join(f"{x['name']}={x['unique_urls']}" for x in weak_cctv))
    if weak_satellite:
        warnings.append("important satellite channels below independent URL warning target: " + ", ".join(f"{x['name']}={x['unique_urls']}" for x in weak_satellite))
    if latin_noise:
        warnings.append(f"latin/noise-like channel names remain for review: {len(latin_noise)}")

    result = {
        "status": "rejected" if failures else "ok",
        "rows": len(rows),
        "unique_channel_identities": len(by_identity),
        "unique_names": len({name for _, name, _ in rows}),
        "unique_urls": len({url for _, _, url in rows}),
        "groups": {group: int(group_counts.get(group, 0)) for group in group_order if group_counts.get(group, 0)},
        "min_exact_cctv_unique_urls": core["min_cctv"],
        "min_important_satellite_unique_urls": core["min_satellite"],
        "required_cctv": core["required_cctv"],
        "important_satellite": core["important_satellite"],
        "missing_cctv_quality": missing_cctv_quality,
        "missing_satellite_quality": missing_satellite_quality,
        "weak_cctv": weak_cctv,
        "weak_satellite": weak_satellite,
        "strict_filter_residue": strict_residue[:80],
        "strict_filter_residue_count": len(strict_residue),
        "latin_noise_review_count": len(latin_noise),
        "latin_noise_review_sample": latin_noise[:80],
        "channel_limit_violations": channel_limit_violations[:80],
        "channel_limit_violation_count": len(channel_limit_violations),
        "group_limit_violations": group_limit_violations,
        "identity_group_conflicts": identity_group_conflicts[:80],
        "identity_group_conflict_count": len(identity_group_conflicts),
        "url_identity_conflicts": url_identity_conflicts[:80],
        "url_identity_conflict_count": len(url_identity_conflicts),
        "failures": failures,
        "warnings": warnings,
    }
    return result, failures, warnings


def build_family_audit(rows: list[tuple[str, str, str]]) -> tuple[dict, list[str]]:
    rules = load_rules()
    quality = load_quality()
    profile = quality.get("family_profile") or {}
    audit_cfg = quality.get("final_quality_audit", {})
    core = core_url_audit(rows, rules, audit_cfg)
    groups = Counter(group for group, _, _ in rows)
    by_identity: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for row in rows:
        by_identity[canonical_channel_key(row[1])].append(row)
    failures: list[str] = []
    min_lines = int(profile.get("min_lines", 0) or 0)
    max_lines = int(profile.get("max_lines", 0) or 0)
    if min_lines and len(rows) < min_lines:
        failures.append(f"family playlist too small: {len(rows)} < {min_lines}")
    if max_lines and len(rows) > max_lines:
        failures.append(f"family playlist too large: {len(rows)} > {max_lines}")
    missing_cctv = [x for x in core["required_cctv"] if x["unique_urls"] < core["min_cctv"]]
    missing_satellite = [x for x in core["important_satellite"] if x["unique_urls"] < core["min_satellite"]]
    if missing_cctv:
        failures.append("family CCTV below independent URL minimum: " + ", ".join(f"{x['name']}={x['unique_urls']}" for x in missing_cctv))
    if missing_satellite:
        failures.append("family satellite below independent URL minimum: " + ", ".join(f"{x['name']}={x['unique_urls']}" for x in missing_satellite))
    group_max = {str(k): int(v) for k, v in (profile.get("group_max_rows") or {}).items()}
    group_violations = [{"group": g, "count": groups[g], "limit": limit} for g, limit in group_max.items() if limit > 0 and groups[g] > limit]
    if group_violations:
        failures.append(f"family group row limit violations: {len(group_violations)}")
    per_identity_violations = []
    group_channel_limits = profile.get("group_channel_limits") or {}
    default_limit = int(profile.get("default_max_urls_per_name", 1))
    for identity, items in by_identity.items():
        group = items[0][0]
        limit = int(group_channel_limits.get(group, default_limit))
        urls = {url for _g, _n, url in items}
        if len(urls) > limit:
            per_identity_violations.append({"identity": identity, "group": group, "unique_urls": len(urls), "limit": limit})
    if per_identity_violations:
        failures.append(f"family per-channel unique URL limit violations: {len(per_identity_violations)}")
    return {
        "status": "rejected" if failures else "ok",
        "rows": len(rows),
        "unique_names": len({name for _, name, _ in rows}),
        "unique_channel_identities": len(by_identity),
        "unique_urls": len({url for _, _, url in rows}),
        "groups": dict(groups),
        "required_cctv": core["required_cctv"],
        "important_satellite": core["important_satellite"],
        "min_exact_cctv_unique_urls": core["min_cctv"],
        "min_important_satellite_unique_urls": core["min_satellite"],
        "missing_cctv_quality": missing_cctv,
        "missing_satellite_quality": missing_satellite,
        "group_limit_violations": group_violations,
        "per_identity_limit_violations": per_identity_violations[:80],
        "failures": failures,
    }, failures


def write_outputs(result: dict, family_result: dict | None = None) -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8")) if SUMMARY.exists() else {}
    summary["quality_audit"] = result
    if family_result is not None:
        summary["family_quality_audit"] = family_result
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# Final playlist quality audit",
        "",
        f"Status: {result['status']}",
        f"Rows: {result['rows']}",
        f"Unique channel names: {result['unique_names']}",
        f"Unique canonical channel identities: {result['unique_channel_identities']}",
        f"Unique URLs: {result['unique_urls']}",
        f"Strict filter residue count: {result['strict_filter_residue_count']}",
        f"Latin/noise-like review count: {result['latin_noise_review_count']}",
        f"Channel unique URL limit violations: {result['channel_limit_violation_count']}",
        f"URL identity conflicts: {result['url_identity_conflict_count']}",
        "",
        "## Core CCTV quality",
        "",
        f"Minimum exact CCTV independent URLs: {result['min_exact_cctv_unique_urls']}",
        "",
        "| Channel | Published rows | Unique URLs | Status |",
        "|---|---:|---:|---|",
    ]
    for item in result["required_cctv"]:
        status = "OK" if item["unique_urls"] >= result["min_exact_cctv_unique_urls"] else "LOW"
        lines.append(f"| {item['name']} | {item['published_rows']} | {item['unique_urls']} | {status} |")
    lines += [
        "",
        "## Important satellite quality",
        "",
        f"Minimum important satellite independent URLs: {result['min_important_satellite_unique_urls']}",
        "",
        "| Channel | Published rows | Unique URLs | Status |",
        "|---|---:|---:|---|",
    ]
    for item in result["important_satellite"]:
        status = "OK" if item["unique_urls"] >= result["min_important_satellite_unique_urls"] else "LOW"
        lines.append(f"| {item['name']} | {item['published_rows']} | {item['unique_urls']} | {status} |")
    if family_result is not None:
        lines += ["", "## Family playlist audit", "", f"Status: {family_result['status']}", f"Rows: {family_result['rows']}", f"Unique URLs: {family_result['unique_urls']}"]
        if family_result["failures"]:
            lines += [f"- {x}" for x in family_result["failures"]]
    if result["group_limit_violations"]:
        lines += ["", "## Group limit violations", ""]
        for item in result["group_limit_violations"]:
            lines.append(f"- {item['group']}: {item['count']} > {item['limit']}")
    if result["strict_filter_residue"]:
        lines += ["", "## Strict filter residue sample", ""]
        for item in result["strict_filter_residue"][:30]:
            lines.append(f"- {item['group']} / {item['name']} / {item['reason']}")
    if result["url_identity_conflicts"]:
        lines += ["", "## URL identity conflict sample", ""]
        for item in result["url_identity_conflicts"][:30]:
            lines.append(f"- {item['url']} :: {' / '.join(item['names'])}")
    if result["failures"]:
        lines += ["", "## Failures", ""] + [f"- {x}" for x in result["failures"]]
    if result["warnings"]:
        lines += ["", "## Warnings", ""] + [f"- {x}" for x in result["warnings"]]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    result, failures, _warnings = build_audit(parse_txt())
    family_result = None
    family_failures: list[str] = []
    profile = load_quality().get("family_profile") or {}
    if profile.get("enabled"):
        if not FAMILY_PLAYLIST.exists():
            family_failures.append("family playlist is enabled but ku9-family.txt is missing")
            family_result = {"status": "rejected", "rows": 0, "unique_urls": 0, "failures": family_failures}
        else:
            family_result, family_failures = build_family_audit(parse_txt(FAMILY_PLAYLIST))
    write_outputs(result, family_result)
    all_failures = failures + family_failures
    print("Quality audit", json.dumps({"status": "rejected" if all_failures else "ok", "failures": all_failures, "warnings": result["warnings"]}, ensure_ascii=False))
    return 1 if all_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
