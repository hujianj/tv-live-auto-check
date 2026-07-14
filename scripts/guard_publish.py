#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
G_CCTV = "\u592e\u89c6\u9891\u9053"
G_SAT = "\u536b\u89c6\u9891\u9053"
G_LOCAL = "\u5730\u65b9\u9891\u9053"
G_MOVIE = "\u5f71\u89c6\u5267\u573a"
G_KIDS = "\u5c11\u513f\u52a8\u6f2b"
G_SPORT_DOC = "\u4f53\u80b2\u7eaa\u5b9e"
G_MUSIC_SHOW = "\u97f3\u4e50\u7efc\u827a"
G_LIFE = "\u751f\u6d3b\u4f11\u95f2"
G_ENT = "\u7efc\u5408\u5a31\u4e50"
G_HK = "\u6e2f\u6fb3\u53f0\u9891\u9053"
G_OVERSEA = "\u6d77\u5916\u534e\u8bed\u9891\u9053"
MIN_GROUPS = {
    # Static minimums are catastrophic-failure floors, not quality targets.
    # A stricter relative-drop guard below compares against the previous run.
    # Keep this below normal variance so a valid but slightly smaller run can
    # still publish fixes such as URL-format cleanup.
    G_CCTV: 90,
    G_SAT: 120,
    G_LOCAL: 250,
    G_MOVIE: 90,
    G_KIDS: 20,
    G_SPORT_DOC: 40,
    G_MUSIC_SHOW: 25,
    G_LIFE: 100,
    G_ENT: 500,
    G_HK: 40,
    G_OVERSEA: 80,
}
MAX_GROUP_DROP_RATIOS = {
    # Mainland core groups should be relatively stable.
    G_CCTV: 0.45,
    G_SAT: 0.45,
    G_LOCAL: 0.45,
    # Entertainment and HK/overseas buckets are intentionally allowed to vary
    # more because the final published recheck removes transient streams there
    # aggressively. Static minimums above still catch catastrophic collapse.
    G_MOVIE: 0.60,
    G_KIDS: 0.60,
    G_SPORT_DOC: 0.60,
    G_MUSIC_SHOW: 0.60,
    G_LIFE: 0.60,
    G_ENT: 0.60,
    G_HK: 0.65,
    G_OVERSEA: 0.75,
}
CORE_SOURCES = {"zbds_iptv4_txt", "epg_cn", "iyouhun_zb", "guovin_ipv4", "suxuang_ipv4", "bigbiggrandg_gather"}


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
        "min_lines": int(os.getenv("IPTV_GUARD_MIN_CURATED_LINES", "1800")),
        "max_total_drop_ratio": float(os.getenv("IPTV_GUARD_MAX_TOTAL_DROP_RATIO", "0.20")),
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
    min_lines = int(os.getenv("IPTV_GUARD_MIN_CURATED_LINES", "1800"))
    max_drop_ratio = float(os.getenv("IPTV_GUARD_MAX_TOTAL_DROP_RATIO", "0.20"))
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
        if len(core_failed) >= 2:
            fail(f"multiple core sources failed: {core_failed}", failures)
        elif core_failed:
            add_warn(f"one core source failed: {core_failed}")
        if len(failed_sources) > 5:
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
