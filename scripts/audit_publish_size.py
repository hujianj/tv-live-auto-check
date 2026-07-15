#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

from playlist_config import ROOT, load_guard

TXT_ALIAS_FILES = ["live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"]
PUBLIC_FILES = [
    *TXT_ALIAS_FILES,
    "live.m3u",
    "stability-history.tsv",
    "full-check-summary.json",
    "final-publish-report.md",
    "stability-report.md",
    "coverage-report.md",
    "publish-guard-report.md",
    "published-recheck-report.md",
    "source-report.md",
    "check-report.md",
    "curated-report.md",
    "sources_status.csv",
]
REPORT = ROOT / "publish-size-report.md"
SUMMARY = ROOT / "full-check-summary.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_files() -> set[str]:
    try:
        out = subprocess.check_output([git_command(), "ls-files"], cwd=ROOT, text=True, encoding="utf-8")
        return {line.strip().replace("\\", "/") for line in out.splitlines() if line.strip()}
    except Exception:
        return set()


def git_command() -> str:
    if os.getenv("GIT_CMD"):
        return os.environ["GIT_CMD"]
    found = shutil.which("git")
    if found:
        return found
    codex_git = Path.home() / "Documents" / "Codex" / "tools" / "bin" / "git.cmd"
    if codex_git.exists():
        return str(codex_git)
    return "git"


def blob_ids(paths: list[str]) -> dict[str, str]:
    try:
        out = subprocess.check_output([git_command(), "ls-files", "-s", *paths], cwd=ROOT, text=True, encoding="utf-8")
    except Exception:
        return {}
    ids: dict[str, str] = {}
    for line in out.splitlines():
        parts = line.split(None, 3)
        if len(parts) == 4:
            ids[parts[3].replace("\\", "/")] = parts[1]
    return ids


def main() -> int:
    guard = load_guard().get("publish_size", {})
    failures: list[str] = []
    warnings: list[str] = []
    tracked = tracked_files()
    forbidden_tracked = [p for p in guard.get("forbid_tracked_artifacts", []) if p in tracked]
    if forbidden_tracked:
        failures.append("large diagnostic artifacts are tracked: " + ", ".join(forbidden_tracked))

    files = [p for p in PUBLIC_FILES if (ROOT / p).exists()]
    sizes = {p: (ROOT / p).stat().st_size for p in files}
    hashes = {p: sha256(ROOT / p) for p in files}
    blobs = blob_ids(files)
    unique_blob_ids: dict[str, int] = {}
    for p in files:
        blob = blobs.get(p) or hashes[p]
        unique_blob_ids.setdefault(blob, sizes[p])
    unique_public_blob_bytes = sum(unique_blob_ids.values())
    working_tree_public_bytes = sum(sizes.values())

    txt_hashes = {p: hashes[p] for p in TXT_ALIAS_FILES if p in hashes}
    txt_alias_same_hash = len(set(txt_hashes.values())) == 1
    if guard.get("require_txt_alias_same_hash", True) and not txt_alias_same_hash:
        failures.append("TXT alias files differ: " + repr(txt_hashes))

    thresholds = {
        "max_primary_txt_bytes": ("ku9-live.txt", int(guard.get("max_primary_txt_bytes", 600_000))),
        "max_m3u_bytes": ("live.m3u", int(guard.get("max_m3u_bytes", 1_000_000))),
        "max_stability_history_bytes": ("stability-history.tsv", int(guard.get("max_stability_history_bytes", 1_200_000))),
    }
    for label, (filename, limit) in thresholds.items():
        size = sizes.get(filename, 0)
        if size > limit:
            failures.append(f"{filename} size {size} exceeds {label}={limit}")
    max_unique = int(guard.get("max_unique_public_blob_bytes", 2_500_000))
    if unique_public_blob_bytes > max_unique:
        failures.append(f"unique public blob bytes {unique_public_blob_bytes} exceeds max_unique_public_blob_bytes={max_unique}")

    duplicate_txt_worktree_bytes = sum(sizes.get(p, 0) for p in TXT_ALIAS_FILES) - (sizes.get("ku9-live.txt", 0) if txt_alias_same_hash else 0)
    if txt_alias_same_hash and duplicate_txt_worktree_bytes > 0:
        warnings.append(
            "TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob."
        )

    result = {
        "status": "rejected" if failures else "ok",
        "files": sizes,
        "txt_alias_same_hash": txt_alias_same_hash,
        "txt_alias_hashes": txt_hashes,
        "working_tree_public_bytes": working_tree_public_bytes,
        "unique_public_blob_bytes": unique_public_blob_bytes,
        "duplicate_txt_worktree_bytes": duplicate_txt_worktree_bytes,
        "max_unique_public_blob_bytes": max_unique,
        "forbidden_tracked_artifacts": forbidden_tracked,
        "failures": failures,
        "warnings": warnings,
    }
    if SUMMARY.exists():
        summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
        summary["publish_size"] = result
        SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# Publish size and alias safety report",
        "",
        f"Status: {result['status']}",
        f"Working-tree public bytes: {working_tree_public_bytes}",
        f"Unique public blob bytes: {unique_public_blob_bytes}",
        f"Max unique public blob bytes: {max_unique}",
        f"TXT alias same hash: {txt_alias_same_hash}",
        f"Duplicate TXT working-tree bytes: {duplicate_txt_worktree_bytes}",
        "",
        "## Public files",
        "",
        "| File | Bytes | SHA256 | Git blob |",
        "|---|---:|---|---|",
    ]
    for p in files:
        lines.append(f"| {p} | {sizes[p]} | {hashes[p]} | {blobs.get(p, 'n/a')} |")
    if failures:
        lines += ["", "## Failures", ""]
        lines += [f"- {x}" for x in failures]
    if warnings:
        lines += ["", "## Warnings", ""]
        lines += [f"- {x}" for x in warnings]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("Publish size audit", json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
