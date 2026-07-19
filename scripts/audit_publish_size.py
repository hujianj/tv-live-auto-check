#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

from playlist_config import ROOT, load_guard
from publication_manifest import (
    FAMILY_TXT_ALIAS_FILES,
    MANIFEST_FILE,
    SIZE_AUDIT_FILES,
    SIZE_REPORT_FILE,
    SUMMARY_FILE,
    TXT_ALIAS_FILES,
    sha256_file,
    validate_manifest,
    write_manifest,
)

REPORT = ROOT / SIZE_REPORT_FILE
SUMMARY = ROOT / SUMMARY_FILE


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
    """Return prospective Git blob IDs for the current working-tree bytes.

    ``git ls-files -s`` reports the index/HEAD blob and is stale while a new
    playlist is being audited before ``git add``.  ``git hash-object`` hashes
    the files that would actually be committed, so identical aliases are
    deduplicated correctly and changed files are not attributed to old blobs.
    """
    try:
        out = subprocess.check_output(
            [git_command(), "hash-object", "--", *paths],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
        )
    except Exception:
        return {}
    values = [line.strip() for line in out.splitlines() if line.strip()]
    if len(values) != len(paths):
        return {}
    return {path.replace("\\", "/"): value for path, value in zip(paths, values)}


def main() -> int:
    guard = load_guard().get("publish_size", {})
    failures: list[str] = []
    warnings: list[str] = []
    tracked = tracked_files()
    forbidden_tracked = [p for p in guard.get("forbid_tracked_artifacts", []) if p in tracked]
    if forbidden_tracked:
        failures.append("large diagnostic artifacts are tracked: " + ", ".join(forbidden_tracked))

    # Self-referential control files are finalized later and covered by the
    # non-self-hashing publication manifest instead of their own hash map.
    files = [p for p in SIZE_AUDIT_FILES if (ROOT / p).exists()]
    sizes = {p: (ROOT / p).stat().st_size for p in files}
    hashes = {p: sha256_file(ROOT / p) for p in files}
    blobs = blob_ids(files)
    unique_blob_ids: dict[str, int] = {}
    for p in files:
        blob = blobs.get(p) or hashes[p]
        unique_blob_ids.setdefault(blob, sizes[p])
    unique_payload_blob_bytes = sum(unique_blob_ids.values())
    working_tree_payload_bytes = sum(sizes.values())

    txt_hashes = {p: hashes[p] for p in TXT_ALIAS_FILES if p in hashes}
    txt_alias_same_hash = len(set(txt_hashes.values())) == 1
    if guard.get("require_txt_alias_same_hash", True) and not txt_alias_same_hash:
        failures.append("TXT alias files differ: " + repr(txt_hashes))
    family_txt_hashes = {p: hashes[p] for p in FAMILY_TXT_ALIAS_FILES if p in hashes}
    family_txt_alias_same_hash = len(set(family_txt_hashes.values())) <= 1
    if not family_txt_alias_same_hash:
        failures.append("family TXT alias files differ: " + repr(family_txt_hashes))

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
    if unique_payload_blob_bytes > max_unique:
        failures.append(f"unique payload blob bytes {unique_payload_blob_bytes} exceeds max_unique_public_blob_bytes={max_unique}")

    duplicate_txt_worktree_bytes = sum(sizes.get(p, 0) for p in TXT_ALIAS_FILES) - (sizes.get("ku9-live.txt", 0) if txt_alias_same_hash else 0)
    if txt_alias_same_hash and duplicate_txt_worktree_bytes > 0:
        warnings.append(
            "TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob."
        )

    result = {
        "status": "rejected" if failures else "ok",
        "measurement_scope": "publication payload files; self-referential control files are verified by publish-manifest.json",
        "excluded_control_files": [SUMMARY_FILE, SIZE_REPORT_FILE, MANIFEST_FILE],
        "manifest_file": MANIFEST_FILE,
        "files": sizes,
        "txt_alias_same_hash": txt_alias_same_hash,
        "family_txt_alias_same_hash": family_txt_alias_same_hash,
        "txt_alias_hashes": txt_hashes,
        "family_txt_alias_hashes": family_txt_hashes,
        "working_tree_payload_bytes": working_tree_payload_bytes,
        "unique_payload_blob_bytes": unique_payload_blob_bytes,
        "duplicate_txt_worktree_bytes": duplicate_txt_worktree_bytes,
        "max_unique_payload_blob_bytes": max_unique,
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
        "Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately",
        f"Working-tree payload bytes: {working_tree_payload_bytes}",
        f"Unique payload blob bytes: {unique_payload_blob_bytes}",
        f"Max unique payload blob bytes: {max_unique}",
        f"TXT alias same hash: {txt_alias_same_hash}",
        f"Family TXT alias same hash: {family_txt_alias_same_hash}",
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
    if failures:
        print("Publish size audit", json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 1

    # This is the last generation write. Any later mutation to a release file
    # is detected by validate_publication.py before commit.
    write_manifest(ROOT)
    manifest_result = validate_manifest(ROOT)
    print(
        "publication manifest OK: "
        f"files={manifest_result['file_count']} bytes={manifest_result['manifest_bytes']}"
    )
    print("Publish size audit", json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
