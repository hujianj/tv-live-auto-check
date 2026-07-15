#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

from validate_playlist import validate_file

ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = ROOT / "config" / "rules.json"
PLAYLIST = ROOT / "live-curated.txt"
SUMMARY = ROOT / "full-check-summary.json"
REPORT = ROOT / "coverage-report.md"


def cctv_key(name: str) -> str | None:
    """Return exact core CCTV key only.

    Resolution suffixes in parentheses are accepted, but variants such as
    CCTV-4K, CCTV-4FHD, CCTV-4中文国际 or CCTV-5+ must not be counted as the
    base CCTV-4/CCTV-5 channel. This keeps coverage reporting honest.
    """
    m = re.match(r"^CCTV[-_ ]?(\d+)(\+?)(?:\((?:\d+p|HD|FHD|4K|高清|超清)\))?$", name.strip(), re.I)
    if not m:
        return None
    return f"CCTV-{int(m.group(1))}{'+' if m.group(2) else ''}"


def cctv_variant_base(name: str) -> str | None:
    n = name.strip()
    if cctv_key(n):
        return None
    m = re.match(r"^CCTV[-_ ]?(\d+)(\+?)", n, re.I)
    if not m:
        return None
    return f"CCTV-{int(m.group(1))}{'+' if m.group(2) else ''}"


def parse_txt(path: Path) -> list[tuple[str, str, str]]:
    # Reuse the strict playlist validator before reading. This prevents a
    # malformed final TXT from producing a misleading "missing channel" report.
    validate_file(path, require_categories=True)
    rows: list[tuple[str, str, str]] = []
    group = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.endswith(",#genre#"):
            group = line.split(",", 1)[0]
            continue
        name, url = line.split(",", 1)
        rows.append((group, name, url))
    return rows


def main() -> int:
    rules = json.loads(RULES_PATH.read_text(encoding="utf-8-sig"))
    coverage = rules.get("coverage", {})
    rows = parse_txt(PLAYLIST)
    by_name: dict[str, list[str]] = defaultdict(list)
    cctv_counts: Counter[str] = Counter()
    cctv_variant_counts: Counter[str] = Counter()
    for _group, name, url in rows:
        by_name[name].append(url)
        key = cctv_key(name)
        if key:
            cctv_counts[key] += 1
        variant_key = cctv_variant_base(name)
        if variant_key:
            cctv_variant_counts[variant_key] += 1
    required_cctv = coverage.get("required_cctv", [])
    important_satellite = coverage.get("important_satellite", [])
    min_sources = int(coverage.get("min_sources_per_important_name", 1))
    cctv_rows = [{"name": name, "count": cctv_counts.get(name, 0)} for name in required_cctv]
    cctv_variant_rows = [{"name": name, "variant_count": cctv_variant_counts.get(name, 0)} for name in required_cctv if cctv_variant_counts.get(name, 0)]
    sat_rows = [{"name": name, "count": len(by_name.get(name, []))} for name in important_satellite]
    missing_cctv = [x["name"] for x in cctv_rows if x["count"] < min_sources]
    missing_satellite = [x["name"] for x in sat_rows if x["count"] < min_sources]
    fail_on_missing_cctv = bool(coverage.get("fail_on_missing_cctv", True))
    fail_on_missing_satellite = bool(coverage.get("fail_on_missing_satellite", False))
    result = {
        "min_sources_per_important_name": min_sources,
        "fail_on_missing_cctv": fail_on_missing_cctv,
        "fail_on_missing_satellite": fail_on_missing_satellite,
        "required_cctv": cctv_rows,
        "required_cctv_variants": cctv_variant_rows,
        "important_satellite": sat_rows,
        "missing_cctv": missing_cctv,
        "missing_satellite": missing_satellite,
    }
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    summary["coverage"] = result
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# Core channel coverage report",
        "",
        f"Minimum sources per important channel: {min_sources}",
        "",
        f"Fail on missing CCTV: {fail_on_missing_cctv}",
        f"Fail on missing important satellite: {fail_on_missing_satellite}",
        "",
        "## CCTV coverage",
        "",
        "| Channel | Published lines | Status |",
        "|---|---:|---|",
    ]
    for item in cctv_rows:
        status = "OK" if item["count"] >= min_sources else "MISSING"
        lines.append(f"| {item['name']} | {item['count']} | {status} |")
    lines += ["", "## Important satellite coverage", "", "| Channel | Published lines | Status |", "|---|---:|---|"]
    for item in sat_rows:
        status = "OK" if item["count"] >= min_sources else "MISSING"
        lines.append(f"| {item['name']} | {item['count']} | {status} |")
    lines += ["", "## CCTV variants not counted as exact core coverage", "", "| Core channel | Variant lines |", "|---|---:|"]
    if cctv_variant_rows:
        for item in cctv_variant_rows:
            lines.append(f"| {item['name']} | {item['variant_count']} |")
    else:
        lines.append("| none | 0 |")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("Coverage audit", json.dumps({"missing_cctv": missing_cctv, "missing_satellite": missing_satellite}, ensure_ascii=False))
    failures: list[str] = []
    if fail_on_missing_cctv and missing_cctv:
        failures.append("missing required CCTV channels: " + ", ".join(missing_cctv))
    if fail_on_missing_satellite and missing_satellite:
        failures.append("missing important satellite channels: " + ", ".join(missing_satellite))
    # Emergency override for manual debugging only; the scheduled workflow should
    # fail instead of publishing a list that dropped core family channels.
    if failures and os.getenv("IPTV_COVERAGE_ALLOW_MISSING") != "1":
        for failure in failures:
            print("COVERAGE FAIL:", failure)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
