#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from audit_coverage import cctv_key
from curate_ku9 import per_channel_limit, strict_quality_drop_reason
from playlist_config import get_group_order, load_quality, load_rules
from validate_playlist import validate_file

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / "live-curated.txt"
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


def is_latin_noise_name(name: str) -> bool:
    """Heuristic for report-only English/overseas residue.

    Do not fail on this alone because valid names such as BRTV北京卫视, IPTV4K or
    TVB are acceptable. Strict fail tokens live in config/quality.json.
    """
    n = name.strip()
    upper = n.upper()
    if re.match(r"^CCTV[-_ ]?\d+", upper):
        return False
    if re.match(r"^(TVB|TVBS|RTHK|VIUTV|PHOENIX)", upper):
        return False
    return bool(re.search(r"[A-Za-z]{5,}", n))


def build_audit(rows: list[tuple[str, str, str]]) -> tuple[dict, list[str], list[str]]:
    rules = load_rules()
    quality = load_quality()
    audit_cfg = quality.get("final_quality_audit", {})
    group_order = get_group_order()
    group_counts = Counter(group for group, _, _ in rows)
    by_name: dict[str, list[tuple[str, str]]] = defaultdict(list)
    strict_residue: list[dict] = []
    latin_noise: list[dict] = []
    for group, name, url in rows:
        by_name[name].append((group, url))
        reason = strict_quality_drop_reason(name)
        if reason:
            strict_residue.append({"group": group, "name": name, "url": url, "reason": reason})
        if is_latin_noise_name(name):
            latin_noise.append({"group": group, "name": name, "url": url})

    cctv_counts: Counter[str] = Counter()
    for _group, name, _url in rows:
        key = cctv_key(name)
        if key:
            cctv_counts[key] += 1

    required_cctv = list(rules.get("coverage", {}).get("required_cctv", []))
    important_satellite = list(rules.get("coverage", {}).get("important_satellite", []))
    min_cctv = int(audit_cfg.get("min_exact_cctv_lines", 1))
    min_sat = int(audit_cfg.get("min_important_satellite_lines", 1))
    warn_cctv = int(audit_cfg.get("warn_exact_cctv_lines_below", min_cctv))
    warn_sat = int(audit_cfg.get("warn_important_satellite_lines_below", min_sat))

    exact_cctv_rows = [{"name": name, "count": cctv_counts.get(name, 0)} for name in required_cctv]
    satellite_rows = [{"name": name, "count": len(by_name.get(name, []))} for name in important_satellite]
    missing_cctv_quality = [x for x in exact_cctv_rows if x["count"] < min_cctv]
    missing_satellite_quality = [x for x in satellite_rows if x["count"] < min_sat]
    weak_cctv = [x for x in exact_cctv_rows if min_cctv <= x["count"] < warn_cctv]
    weak_satellite = [x for x in satellite_rows if min_sat <= x["count"] < warn_sat]

    channel_limit_violations: list[dict] = []
    for name, items in by_name.items():
        group = items[0][0]
        limit = per_channel_limit(group, name)
        if len(items) > limit:
            channel_limit_violations.append({"group": group, "name": name, "count": len(items), "limit": limit})

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
        failures.append("core CCTV channels below quality minimum: " + ", ".join(f"{x['name']}={x['count']}" for x in missing_cctv_quality))
    if missing_satellite_quality:
        failures.append("important satellite channels below quality minimum: " + ", ".join(f"{x['name']}={x['count']}" for x in missing_satellite_quality))
    if audit_cfg.get("fail_on_channel_limit_violation", True) and channel_limit_violations:
        failures.append(f"channel line limit violations: {len(channel_limit_violations)}")
    if audit_cfg.get("fail_on_group_limit_violation", True) and group_limit_violations:
        failures.append(f"group line limit violations: {len(group_limit_violations)}")
    if weak_cctv:
        warnings.append("core CCTV channels below warning target: " + ", ".join(f"{x['name']}={x['count']}" for x in weak_cctv))
    if weak_satellite:
        warnings.append("important satellite channels below warning target: " + ", ".join(f"{x['name']}={x['count']}" for x in weak_satellite))
    if latin_noise:
        warnings.append(f"latin/noise-like channel names remain for review: {len(latin_noise)}")

    result = {
        "status": "rejected" if failures else "ok",
        "rows": len(rows),
        "unique_names": len(by_name),
        "unique_urls": len({url for _, _, url in rows}),
        "groups": {group: int(group_counts.get(group, 0)) for group in group_order if group_counts.get(group, 0)},
        "min_exact_cctv_lines": min_cctv,
        "min_important_satellite_lines": min_sat,
        "required_cctv": exact_cctv_rows,
        "important_satellite": satellite_rows,
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
        "failures": failures,
        "warnings": warnings,
    }
    return result, failures, warnings


def write_outputs(result: dict) -> None:
    if SUMMARY.exists():
        summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    else:
        summary = {}
    summary["quality_audit"] = result
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# Final playlist quality audit",
        "",
        f"Status: {result['status']}",
        f"Rows: {result['rows']}",
        f"Unique channel names: {result['unique_names']}",
        f"Unique URLs: {result['unique_urls']}",
        f"Strict filter residue count: {result['strict_filter_residue_count']}",
        f"Latin/noise-like review count: {result['latin_noise_review_count']}",
        f"Channel limit violations: {result['channel_limit_violation_count']}",
        "",
        "## Core CCTV quality",
        "",
        f"Minimum exact CCTV lines: {result['min_exact_cctv_lines']}",
        "",
        "| Channel | Exact published lines | Status |",
        "|---|---:|---|",
    ]
    for item in result["required_cctv"]:
        status = "OK" if item["count"] >= result["min_exact_cctv_lines"] else "LOW"
        lines.append(f"| {item['name']} | {item['count']} | {status} |")
    lines += [
        "",
        "## Important satellite quality",
        "",
        f"Minimum important satellite lines: {result['min_important_satellite_lines']}",
        "",
        "| Channel | Published lines | Status |",
        "|---|---:|---|",
    ]
    for item in result["important_satellite"]:
        status = "OK" if item["count"] >= result["min_important_satellite_lines"] else "LOW"
        lines.append(f"| {item['name']} | {item['count']} | {status} |")
    if result["group_limit_violations"]:
        lines += ["", "## Group limit violations", ""]
        for item in result["group_limit_violations"]:
            lines.append(f"- {item['group']}: {item['count']} > {item['limit']}")
    if result["strict_filter_residue"]:
        lines += ["", "## Strict filter residue sample", ""]
        for item in result["strict_filter_residue"][:30]:
            lines.append(f"- {item['group']} / {item['name']} / {item['reason']}")
    if result["latin_noise_review_sample"]:
        lines += ["", "## Latin/noise-like review sample", ""]
        for item in result["latin_noise_review_sample"][:30]:
            lines.append(f"- {item['group']} / {item['name']}")
    if result["failures"]:
        lines += ["", "## Failures", ""]
        lines += [f"- {x}" for x in result["failures"]]
    if result["warnings"]:
        lines += ["", "## Warnings", ""]
        lines += [f"- {x}" for x in result["warnings"]]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    result, failures, _warnings = build_audit(parse_txt())
    write_outputs(result)
    print("Quality audit", json.dumps({"status": result["status"], "failures": failures, "warnings": result["warnings"]}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
