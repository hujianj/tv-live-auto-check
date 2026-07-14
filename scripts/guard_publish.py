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
    G_CCTV: 100,
    G_SAT: 150,
    G_LOCAL: 350,
    G_MOVIE: 100,
    G_KIDS: 20,
    G_SPORT_DOC: 50,
    G_MUSIC_SHOW: 30,
    G_LIFE: 120,
    G_ENT: 600,
    G_HK: 50,
    G_OVERSEA: 100,
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


def main() -> int:
    current = load_json(ROOT / "full-check-summary.json")
    baseline = git_show_json("HEAD:full-check-summary.json") or {}
    failures: list[str] = []
    cur_lines = int(current.get("curated_published_lines") or current.get("primary_published_lines") or 0)
    base_lines = int(baseline.get("curated_published_lines") or baseline.get("primary_published_lines") or 0)
    min_lines = int(os.getenv("IPTV_GUARD_MIN_CURATED_LINES", "1800"))
    max_drop_ratio = float(os.getenv("IPTV_GUARD_MAX_TOTAL_DROP_RATIO", "0.20"))
    if cur_lines < min_lines:
        fail(f"curated lines {cur_lines} < minimum {min_lines}", failures)
    if base_lines > 0:
        drop = (base_lines - cur_lines) / base_lines
        if drop > max_drop_ratio:
            fail(f"curated lines dropped {drop:.1%}: baseline={base_lines} current={cur_lines}", failures)
        else:
            print(f"GUARD OK total lines baseline={base_lines} current={cur_lines} drop={drop:.1%}")
    else:
        warn("no baseline full-check-summary.json found; total drop guard skipped")
    groups = current.get("curated_groups") or {}
    base_groups = baseline.get("curated_groups") or {}
    for group, minimum in MIN_GROUPS.items():
        cur = int(groups.get(group, 0))
        if cur < minimum:
            fail(f"group {group} count {cur} < minimum {minimum}", failures)
        base = int(base_groups.get(group, 0)) if base_groups else 0
        if base >= minimum:
            drop = (base - cur) / base
            if drop > 0.45:
                fail(f"group {group} dropped {drop:.1%}: baseline={base} current={cur}", failures)
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
            warn(f"one core source failed: {core_failed}")
        if len(failed_sources) > 5:
            fail(f"too many upstream fetch failures: {len(failed_sources)} {failed_sources[:10]}", failures)
        zero_parsed = [r["name"] for r in statuses if r.get("fetch_ok") == "True" and int(r.get("parsed") or 0) == 0]
        if zero_parsed:
            warn(f"fetched but parsed no supported streams: {zero_parsed}")
    if failures:
        print("Publish guard rejected this run; keeping previous published playlist unchanged.")
        return 1
    print("Publish guard OK", json.dumps({"curated_published_lines": cur_lines, "baseline_lines": base_lines}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
