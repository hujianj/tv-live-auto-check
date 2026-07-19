#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate committed public playlists and their final byte manifest."""
from __future__ import annotations

import json
from pathlib import Path

from publication_manifest import (
    FAMILY_FILES,
    MANIFEST_FILE,
    TXT_ALIAS_FILES,
    validate_manifest,
)
from validate_playlist import validate_file

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST_FILES = [*TXT_ALIAS_FILES, "live.m3u", *FAMILY_FILES]


def validate_publication(root: Path = ROOT) -> dict[str, object]:
    playlists = {name: validate_file(root / name) for name in PLAYLIST_FILES}
    manifest = validate_manifest(root)
    return {"status": "ok", "playlists": playlists, "manifest": manifest}


def main() -> int:
    result = validate_publication(ROOT)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    print(f"final public publication validation OK ({MANIFEST_FILE})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
