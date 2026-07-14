#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from playlist_config import load_guard

ROOT = Path(__file__).resolve().parents[1]
GUARD = load_guard()
MIN_GROUPS = {str(group): int(minimum) for group, minimum in GUARD["min_groups"].items()}
MAX_GROUP_DROP_RATIOS = {str(group): float(ratio) for group, ratio in GUARD["max_group_drop_ratios"].items()}
CORE_SOURCES = {str(source) for source in GUARD["core_sources"]}


def guard_min_lines() -> int:
    return int(os.getenv("IPTV_GUARD_MIN_CURATED_LINES", str(GUARD.get("min_lines", 1800))))


def guard_max_total_drop_ratio() -> float:
    return float(os.getenv("IPTV_GUARD_MAX_TOTAL_DROP_RATIO", str(GUARD.get("max_total_drop_ratio", 0.20))))


def guard_max_failed_sources() -> int:
    return int(os.getenv("IPTV_GUARD_MAX_FAILED_SOURCES", str(GUARD.get("max_failed_sources", 5))))


def guard_core_failed_fail_threshold() -> int:
    return int(os.getenv("IPTV_GUARD_CORE_FAILED_FAIL_THRESHOLD", str(GUARD.get("core_failed_fail_threshold", 2))))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git_command() -> str:
    return os.getenv("GIT_CMD") or shutil.which("git") or "git"


def git_show_json(spec: str) -> dict | None:
    try:
        data = subprocess.check_output([git_command(), "show", spec], cwd=ROOT, stderr=subprocess.DEVNULL)
        return json.loads(data.decode("utf-8"))
    except Exception as e:
        warn(f"cannot read baseline from git ({e!r}); set GIT_CMD if running locally")
        return None


def read_sources_status() -> list[dict[str, str]]:
    import csv
    path = ROOT / "sources_status.csv"
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)
    print("GUARD FAIL:", msg)


def warn(msg: str) -> None:
    print("GUARD WARN:", msg)


def ratio(base: int, current: int) -> float | None:
    if base <= 0:
        return None
    return (base - current) / base


def write_guard_outputs(current: dict, baseline: dict, failures: list[str], warnings: list[str], statuses: list[dict[str, str]]) -> None:
    groups = current.get("curated_groups") or {}
    base_groups = baseline.get("curated_groups") or {}
    cur_lines = int(current.get("curated_published_lines") or current.get("primary_published_lines") or 0)
    base_lines = int(baseline.get("curated_published_lines") or baseline.get("primary_published_lines") or 0)
    group_deltas: dict[str, dict[str, int | float | None]] = {}
    for group in MIN_GROUPS:
        cur = int(groups.get(group, 0))
        base = int(base_groups.get(group, 0)) if base_groups else 0
        group_deltas[group] = {
            "baseline": base,
            "current": cur,
            "delta": cur - base,
            "drop_ratio": ratio(base, cur),
        }
    failed_sources = [r["name"] for r in statuses if r.get("fetch_ok") != "True"]
    zero_parsed = [r["name"] for r in statuses if r.get("fetch_ok") == "True" and int(r.get("parsed") or 0) == 0]
    guard = {
        "status": "rejected" if failures else "ok",
        "baseline_lines": base_lines,
        "current_lines": cur_lines,
        "total_drop_ratio": ratio(base_lines, cur_lines),
        "min_lines": guard_min_lines(),
        "max_total_drop_ratio": guard_max_total_drop_ratio(),
        "max_failed_sources": guard_max_failed_sources(),
        "core_failed_fail_threshold": guard_core_failed_fail_threshold(),
        "core_sources": sorted(CORE_SOURCES),
        "group_deltas": group_deltas,
        "failed_sources": failed_sources,
        "zero_parsed_sources": zero_parsed,
        "failures": failures,
        "warnings": warnings,
    }
    current["publish_guard"] = guard
    (ROOT / "full-check-summary.json").write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# Publish guard report",
        "",
        f"Status: {guard['status']}",
        f"Baseline lines: {base_lines}",
        f"Current lines: {cur_lines}",
        f"Total drop ratio: {guard['total_drop_ratio']:.1%}" if guard["total_drop_ratio"] is not None else "Total drop ratio: n/a",
        "",
        "## Group deltas",
        "",
        "| Group | Baseline | Current | Delta | Drop | Minimum |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for group, minimum in MIN_GROUPS.items():
        item = group_deltas[group]
        drop = item["drop_ratio"]
        drop_text = f"{drop:.1%}" if drop is not None else "n/a"
        lines.append(f"| {group} | {item['baseline']} | {item['current']} | {item['delta']} | {drop_text} | {minimum} |")
    lines += ["", "## Source health", "", f"- Failed sources: {', '.join(failed_sources) if failed_sources else 'none'}", f"- Fetched but zero parsed: {', '.join(zero_parsed) if zero_parsed else 'none'}"]
    if failures:
        lines += ["", "## Failures", ""]
        lines += [f"- {x}" for x in failures]
    if warnings:
        lines += ["", "## Warnings", ""]
        lines += [f"- {x}" for x in warnings]
    (ROOT / "publish-guard-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    current = load_json(ROOT / "full-check-summary.json")
    baseline = git_show_json("HEAD:full-check-summary.json") or {}
    failures: list[str] = []
    warnings: list[str] = []
    cur_lines = int(current.get("curated_published_lines") or current.get("primary_published_lines") or 0)
    base_lines = int(baseline.get("curated_published_lines") or baseline.get("primary_published_lines") or 0)
    min_lines = guard_min_lines()
    max_drop_ratio = guard_max_total_drop_ratio()
    def add_warn(msg: str) -> None:
        warnings.append(msg)
        warn(msg)

    if cur_lines < min_lines:
        fail(f"curated lines {cur_lines} < minimum {min_lines}", failures)
    if base_lines > 0:
        drop = (base_lines - cur_lines) / base_lines
        if drop > max_drop_ratio:
            fail(f"curated lines dropped {drop:.1%}: baseline={base_lines} current={cur_lines}", failures)
        else:
            print(f"GUARD OK total lines baseline={base_lines} current={cur_lines} drop={drop:.1%}")
    else:
        add_warn("no baseline full-check-summary.json found; total drop guard skipped")
    groups = current.get("curated_groups") or {}
    base_groups = baseline.get("curated_groups") or {}
    for group, minimum in MIN_GROUPS.items():
        cur = int(groups.get(group, 0))
        if cur < minimum:
            fail(f"group {group} count {cur} < minimum {minimum}", failures)
        base = int(base_groups.get(group, 0)) if base_groups else 0
        if base >= minimum:
            drop = (base - cur) / base
            max_group_drop = MAX_GROUP_DROP_RATIOS.get(group, 0.45)
            if drop > max_group_drop:
                fail(f"group {group} dropped {drop:.1%}: baseline={base} current={cur} max={max_group_drop:.0%}", failures)
    if current.get("checked_all_unique") is not True:
        fail("checked_all_unique is not true", failures)
    if int(current.get("checked_candidates") or -1) != int(current.get("unique_candidates") or -2):
        fail("checked_candidates != unique_candidates", failures)
    statuses = read_sources_status()
    if statuses:
        failed_sources = [r["name"] for r in statuses if r.get("fetch_ok") != "True"]
        core_failed = sorted(CORE_SOURCES.intersection(failed_sources))
        if len(core_failed) >= guard_core_failed_fail_threshold():
            fail(f"multiple core sources failed: {core_failed}", failures)
        elif core_failed:
            add_warn(f"one core source failed: {core_failed}")
        if len(failed_sources) > guard_max_failed_sources():
            fail(f"too many upstream fetch failures: {len(failed_sources)} {failed_sources[:10]}", failures)
        zero_parsed = [r["name"] for r in statuses if r.get("fetch_ok") == "True" and int(r.get("parsed") or 0) == 0]
        if zero_parsed:
            add_warn(f"fetched but parsed no supported streams: {zero_parsed}")
    write_guard_outputs(current, baseline, failures, warnings, statuses)
    if failures:
        print("Publish guard rejected this run; keeping previous published playlist unchanged.")
        return 1
    print("Publish guard OK", json.dumps({"curated_published_lines": cur_lines, "baseline_lines": base_lines}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
