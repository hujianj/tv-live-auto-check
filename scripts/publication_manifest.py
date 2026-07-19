#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build and verify a non-self-referential manifest for published outputs.

The manifest deliberately does not hash itself.  All other files that form the
public release are finalized before this manifest is written, so a validator can
prove the exact bytes that are about to be committed without circular hashes.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from publication_config import load_publication_config

_PUBLICATION_CONFIG = load_publication_config()
MANIFEST_SCHEMA_VERSION = 1
MANIFEST_FILE = "publish-manifest.json"
SUMMARY_FILE = "full-check-summary.json"
SIZE_REPORT_FILE = "publish-size-report.md"

TXT_ALIAS_FILES = [
    name for name in _PUBLICATION_CONFIG["playlist_files"]
    if name.endswith(".txt") and name not in {"ku9-family.txt", "live-family.txt"}
]
FAMILY_TXT_ALIAS_FILES = [name for name in _PUBLICATION_CONFIG["playlist_files"] if name in {"ku9-family.txt", "live-family.txt"}]
FAMILY_FILES = [*FAMILY_TXT_ALIAS_FILES, "family.m3u"]

# The generated publication inventory is centralized in config/publication.json.
# The size report and manifest intentionally cover the same immutable files.
SIZE_AUDIT_FILES = [
    name for name in _PUBLICATION_CONFIG["publication_files"]
    if name not in {SUMMARY_FILE, SIZE_REPORT_FILE}
]
FINAL_PUBLICATION_FILES = [*SIZE_AUDIT_FILES, SUMMARY_FILE, SIZE_REPORT_FILE]


class ManifestValidationError(ValueError):
    pass


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _summary_metadata(root: Path) -> dict[str, object]:
    path = root / SUMMARY_FILE
    try:
        summary = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ManifestValidationError(f"cannot read {SUMMARY_FILE}: {exc}") from exc
    return {
        "generated_utc": summary.get("generated_utc", ""),
        "generated_beijing": summary.get("generated_beijing", ""),
        "final_primary_published_lines": summary.get("final_primary_published_lines"),
    }


def build_manifest(root: Path) -> dict[str, object]:
    missing = [name for name in FINAL_PUBLICATION_FILES if not (root / name).is_file()]
    if missing:
        raise ManifestValidationError("missing final publication files: " + ", ".join(missing))
    files = {
        name: {
            "bytes": (root / name).stat().st_size,
            "sha256": sha256_file(root / name),
        }
        for name in FINAL_PUBLICATION_FILES
    }
    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "scope": "all final publication files except this non-self-hashing manifest",
        "manifest_file": MANIFEST_FILE,
        "manifest_self_hash_excluded": True,
        "source_summary": _summary_metadata(root),
        "file_count": len(files),
        "files": files,
    }


def write_manifest(root: Path) -> dict[str, object]:
    manifest = build_manifest(root)
    (root / MANIFEST_FILE).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def validate_manifest(root: Path) -> dict[str, object]:
    path = root / MANIFEST_FILE
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ManifestValidationError(f"cannot read {MANIFEST_FILE}: {exc}") from exc

    failures: list[str] = []
    if manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION:
        failures.append(f"unsupported schema_version={manifest.get('schema_version')!r}")
    if manifest.get("manifest_file") != MANIFEST_FILE:
        failures.append("manifest_file does not name the canonical manifest")
    if manifest.get("manifest_self_hash_excluded") is not True:
        failures.append("manifest must explicitly exclude its own hash")

    files = manifest.get("files")
    if not isinstance(files, dict):
        failures.append("files must be an object")
        files = {}
    expected_names = set(FINAL_PUBLICATION_FILES)
    actual_names = set(files)
    missing = sorted(expected_names - actual_names)
    extra = sorted(actual_names - expected_names)
    if missing:
        failures.append("manifest missing files: " + ", ".join(missing))
    if extra:
        failures.append("manifest has unexpected files: " + ", ".join(extra))
    if manifest.get("file_count") != len(expected_names):
        failures.append(
            f"file_count={manifest.get('file_count')!r} expected={len(expected_names)}"
        )

    for name in FINAL_PUBLICATION_FILES:
        item = files.get(name)
        if not isinstance(item, dict):
            continue
        file_path = root / name
        if not file_path.is_file():
            failures.append(f"missing file on disk: {name}")
            continue
        actual_size = file_path.stat().st_size
        actual_hash = sha256_file(file_path)
        if item.get("bytes") != actual_size:
            failures.append(
                f"size mismatch for {name}: manifest={item.get('bytes')!r} actual={actual_size}"
            )
        if item.get("sha256") != actual_hash:
            failures.append(
                f"sha256 mismatch for {name}: manifest={item.get('sha256')!r} actual={actual_hash}"
            )

    if failures:
        raise ManifestValidationError("invalid publication manifest: " + "; ".join(failures))
    return {
        "status": "ok",
        "file_count": len(expected_names),
        "manifest_bytes": path.stat().st_size,
        "manifest_sha256": sha256_file(path),
    }
