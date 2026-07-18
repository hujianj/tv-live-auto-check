#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from channel_utils import cctv_key, cctv_variant_base
from channel_identity import canonical_channel_key
from validate_playlist import validate_file

ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = ROOT / "config" / "rules.json"
PLAYLIST = ROOT / "live-curated.txt"
SUMMARY = ROOT / "full-check-summary.json"
REPORT = ROOT / "coverage-report.md"


def parse_txt(path: Path) -> list[tuple[str, str, str]]:
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


def build_coverage(rows: list[tuple[str, str, str]], coverage: dict) -> dict:
    by_key_urls: dict[str, set[str]] = defaultdict(set)
    by_key_rows: Counter[str] = Counter()
    cctv_urls: dict[str, set[str]] = defaultdict(set)
    cctv_rows: Counter[str] = Counter()
    cctv_variant_urls: dict[str, set[str]] = defaultdict(set)
    cctv_variant_rows: Counter[str] = Counter()
    for _group, name, url in rows:
        identity = canonical_channel_key(name)
        by_key_urls[identity].add(url)
        by_key_rows[identity] += 1
        key = cctv_key(name)
        if key:
            cctv_urls[key].add(url)
            cctv_rows[key] += 1
        variant_key = cctv_variant_base(name)
        if variant_key and not key:
            cctv_variant_urls[variant_key].add(url)
            cctv_variant_rows[variant_key] += 1

    required_cctv = coverage.get("required_cctv", [])
    important_satellite = coverage.get("important_satellite", [])
    min_urls = int(coverage.get("min_unique_urls_per_important_name", coverage.get("min_sources_per_important_name", 1)))
    cctv_items = [
        {
            "name": name,
            "published_rows": cctv_rows.get(name, 0),
            "unique_urls": len(cctv_urls.get(name, set())),
            "count": len(cctv_urls.get(name, set())),
        }
        for name in required_cctv
    ]
    variant_items = [
        {
            "name": name,
            "published_rows": cctv_variant_rows.get(name, 0),
            "unique_urls": len(cctv_variant_urls.get(name, set())),
            "variant_count": len(cctv_variant_urls.get(name, set())),
        }
        for name in required_cctv
        if cctv_variant_urls.get(name)
    ]
    sat_items = []
    for name in important_satellite:
        key = canonical_channel_key(name)
        sat_items.append({
            "name": name,
            "published_rows": by_key_rows.get(key, 0),
            "unique_urls": len(by_key_urls.get(key, set())),
            "count": len(by_key_urls.get(key, set())),
        })
    missing_cctv = [x["name"] for x in cctv_items if x["unique_urls"] < min_urls]
    missing_satellite = [x["name"] for x in sat_items if x["unique_urls"] < min_urls]
    return {
        "minimum_unique_urls_per_important_channel": min_urls,
        "min_sources_per_important_name": min_urls,
        "fail_on_missing_cctv": bool(coverage.get("fail_on_missing_cctv", True)),
        "fail_on_missing_satellite": bool(coverage.get("fail_on_missing_satellite", False)),
        "required_cctv": cctv_items,
        "required_cctv_variants": variant_items,
        "important_satellite": sat_items,
        "missing_cctv": missing_cctv,
        "missing_satellite": missing_satellite,
    }


def main() -> int:
    rules = json.loads(RULES_PATH.read_text(encoding="utf-8-sig"))
    result = build_coverage(parse_txt(PLAYLIST), rules.get("coverage", {}))
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    summary["coverage"] = result
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    min_urls = result["minimum_unique_urls_per_important_channel"]
    lines = [
        "# Core channel coverage report",
        "",
        f"Minimum independent URLs per important channel: {min_urls}",
        "",
        f"Fail on missing CCTV: {result['fail_on_missing_cctv']}",
        f"Fail on missing important satellite: {result['fail_on_missing_satellite']}",
        "",
        "## CCTV coverage",
        "",
        "| Channel | Published rows | Unique URLs | Status |",
        "|---|---:|---:|---|",
    ]
    for item in result["required_cctv"]:
        status = "OK" if item["unique_urls"] >= min_urls else "MISSING"
        lines.append(f"| {item['name']} | {item['published_rows']} | {item['unique_urls']} | {status} |")
    lines += ["", "## Important satellite coverage", "", "| Channel | Published rows | Unique URLs | Status |", "|---|---:|---:|---|"]
    for item in result["important_satellite"]:
        status = "OK" if item["unique_urls"] >= min_urls else "MISSING"
        lines.append(f"| {item['name']} | {item['published_rows']} | {item['unique_urls']} | {status} |")
    lines += ["", "## CCTV variants not counted as exact core coverage", "", "| Core channel | Variant rows | Variant unique URLs |", "|---|---:|---:|"]
    if result["required_cctv_variants"]:
        for item in result["required_cctv_variants"]:
            lines.append(f"| {item['name']} | {item['published_rows']} | {item['unique_urls']} |")
    else:
        lines.append("| none | 0 | 0 |")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    failures: list[str] = []
    if result["fail_on_missing_cctv"] and result["missing_cctv"]:
        failures.append("missing CCTV independent URLs: " + ", ".join(result["missing_cctv"]))
    if result["fail_on_missing_satellite"] and result["missing_satellite"]:
        failures.append("missing satellite independent URLs: " + ", ".join(result["missing_satellite"]))
    print(json.dumps(result, ensure_ascii=False))
    if failures:
        print("Coverage audit failed: " + "; ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
