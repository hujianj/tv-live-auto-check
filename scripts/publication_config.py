#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Single source of truth for generated publication files and public endpoints."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import string
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT / "config" / "publication.json"


class PublicationConfigError(ValueError):
    pass


_ENDPOINT_FIELDS = {"repo", "branch", "owner", "name", "path"}
_FILE_LIST_KEYS = ("playlist_files", "publication_files", "purge_files")


def _validate_relative_file_name(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise PublicationConfigError(f"{field} entries must be non-empty strings")
    text = value.strip()
    # Publication inventories are intentionally flat and POSIX-shaped. They
    # are later joined to ROOT and passed to git/curl, so reject traversal,
    # absolute paths, drive prefixes, and Windows separators.
    if text.startswith(("/", "\\")) or ":" in text or "\\" in text:
        raise PublicationConfigError(f"{field} contains an unsafe path: {value!r}")
    parts = Path(text).parts
    if not parts or any(part in {"", ".", ".."} for part in parts):
        raise PublicationConfigError(f"{field} contains an unsafe path: {value!r}")
    return text


def _validate_endpoint_template(template: object, endpoint_name: str) -> str:
    if not isinstance(template, str) or not template:
        raise PublicationConfigError(f"endpoint {endpoint_name!r} template must be a non-empty string")
    parsed = urlparse(template)
    if parsed.scheme != "https" or not parsed.netloc:
        raise PublicationConfigError(f"endpoint {endpoint_name!r} template must be an HTTPS URL")
    fields: set[str] = set()
    try:
        for _literal, field_name, _format_spec, _conversion in string.Formatter().parse(template):
            if field_name:
                if any(char in field_name for char in ".[]") or field_name not in _ENDPOINT_FIELDS:
                    raise PublicationConfigError(
                        f"endpoint {endpoint_name!r} template has unsupported placeholder {field_name!r}"
                    )
                fields.add(field_name)
    except ValueError as exc:
        raise PublicationConfigError(f"endpoint {endpoint_name!r} template is malformed: {exc}") from exc
    if "path" not in fields:
        raise PublicationConfigError(f"endpoint {endpoint_name!r} template must contain {{path}}")
    return template


def load_publication_config(root: Path = ROOT) -> dict[str, Any]:
    path = root / "config" / "publication.json"
    try:
        config = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        raise PublicationConfigError(f"cannot read {path}: {exc}") from exc
    if not isinstance(config, dict):
        raise PublicationConfigError("publication config root must be an object")
    if config.get("schema_version") != 1:
        raise PublicationConfigError(f"unsupported publication schema_version={config.get('schema_version')!r}")
    for key in (*_FILE_LIST_KEYS, "endpoints"):
        if not isinstance(config.get(key), list) or not config[key]:
            raise PublicationConfigError(f"publication config {key!r} must be a non-empty list")

    inventories: dict[str, list[str]] = {}
    for key in _FILE_LIST_KEYS:
        values = [_validate_relative_file_name(item, key) for item in config[key]]
        if len(set(values)) != len(values):
            raise PublicationConfigError(f"{key} contains duplicates")
        inventories[key] = values
    publication = inventories["publication_files"]
    playlist = inventories["playlist_files"]
    purge = inventories["purge_files"]
    missing = [name for name in playlist + purge if name not in publication]
    if missing:
        raise PublicationConfigError(
            "files used by playlist/purge are not publication files: "
            + ", ".join(sorted(set(missing)))
        )

    primary = _validate_relative_file_name(config.get("primary_text_file"), "primary_text_file")
    authoritative = _validate_relative_file_name(config.get("authoritative_raw_file"), "authoritative_raw_file")
    if primary not in playlist:
        raise PublicationConfigError("primary_text_file must be in playlist_files")
    if authoritative not in playlist:
        raise PublicationConfigError("authoritative_raw_file must be in playlist_files")
    if primary == authoritative:
        raise PublicationConfigError("primary_text_file and authoritative_raw_file must be distinct aliases")

    endpoint_names: list[str] = []
    hard_raw: list[dict[str, Any]] = []
    required_primary: list[dict[str, Any]] = []
    for item in config["endpoints"]:
        if not isinstance(item, dict) or not item.get("name") or not item.get("template") or not item.get("path"):
            raise PublicationConfigError(f"invalid endpoint entry: {item!r}")
        name = item["name"]
        if not isinstance(name, str) or not name.strip():
            raise PublicationConfigError(f"endpoint name must be a non-empty string: {item!r}")
        if name in endpoint_names:
            raise PublicationConfigError(f"endpoint names must be unique: {name!r}")
        endpoint_names.append(name)
        path_value = _validate_relative_file_name(item["path"], f"endpoint {name!r} path")
        if path_value not in playlist:
            raise PublicationConfigError(f"endpoint path is not a playlist file: {item['path']!r}")
        _validate_endpoint_template(item["template"], name)
        for bool_key in ("hard_raw", "television_compatible", "required_primary"):
            if not isinstance(item.get(bool_key, False), bool):
                raise PublicationConfigError(f"endpoint {name!r} field {bool_key!r} must be boolean")
        if item.get("hard_raw", False):
            hard_raw.append(item)
        if item.get("required_primary", False):
            required_primary.append(item)
        timing_values = {
            "retries": item.get("retries"),
            "timeout_seconds": item.get("timeout_seconds"),
            "endpoint_deadline_seconds": item.get("endpoint_deadline_seconds"),
        }
        if any(type(value) is not int for value in timing_values.values()):
            raise PublicationConfigError(f"endpoint timing must use strict integers: {item!r}")
        retries = timing_values["retries"]
        timeout_seconds = timing_values["timeout_seconds"]
        deadline_seconds = timing_values["endpoint_deadline_seconds"]
        if retries < 1 or timeout_seconds < 1 or deadline_seconds < 1:
            raise PublicationConfigError(f"endpoint timing must be positive: {item!r}")

    if len(hard_raw) != 1:
        raise PublicationConfigError(
            f"publication config must have exactly one hard_raw endpoint, got {len(hard_raw)}"
        )
    if len(required_primary) != 1:
        raise PublicationConfigError(
            f"publication config must have exactly one required_primary endpoint, got {len(required_primary)}"
        )
    if hard_raw[0]["path"] != authoritative:
        raise PublicationConfigError("hard_raw endpoint must serve authoritative_raw_file")
    if required_primary[0]["path"] != primary:
        raise PublicationConfigError("required_primary endpoint must serve primary_text_file")
    if required_primary[0].get("television_compatible") is not True:
        raise PublicationConfigError("required_primary endpoint must be television_compatible=true")

    # Store normalized validated values so all callers share the same contract.
    config["playlist_files"] = playlist
    config["publication_files"] = publication
    config["purge_files"] = purge
    config["primary_text_file"] = primary
    config["authoritative_raw_file"] = authoritative
    for item in config["endpoints"]:
        item["path"] = _validate_relative_file_name(item["path"], f"endpoint {item['name']!r} path")
    return config


def publication_files(root: Path = ROOT) -> list[str]:
    return [str(x) for x in load_publication_config(root)["publication_files"]]


def playlist_files(root: Path = ROOT) -> list[str]:
    return [str(x) for x in load_publication_config(root)["playlist_files"]]


def purge_files(root: Path = ROOT) -> list[str]:
    return [str(x) for x in load_publication_config(root)["purge_files"]]


def endpoint_specs(root: Path = ROOT) -> list[dict[str, Any]]:
    return [dict(x) for x in load_publication_config(root)["endpoints"]]


def endpoint_urls(repo: str, branch: str, root: Path = ROOT) -> list[dict[str, Any]]:
    owner, name = repo.split("/", 1)
    values = {"repo": repo, "branch": branch, "owner": owner, "name": name}
    result: list[dict[str, Any]] = []
    for item in endpoint_specs(root):
        rendered = dict(item)
        rendered["url"] = str(item["template"]).format(**values, path=item["path"])
        result.append(rendered)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publication-files", action="store_true")
    parser.add_argument("--playlist-files", action="store_true")
    parser.add_argument("--purge-files", action="store_true")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args(argv)
    config = load_publication_config(ROOT)
    selected = sum(bool(x) for x in (args.publication_files, args.playlist_files, args.purge_files))
    if args.publication_files:
        print("\n".join(map(str, config["publication_files"])))
    elif args.playlist_files:
        print("\n".join(map(str, config["playlist_files"])))
    elif args.purge_files:
        print("\n".join(map(str, config["purge_files"])))
    elif args.validate or not selected:
        print(json.dumps({"status": "ok", "schema_version": config["schema_version"], "publication_files": len(config["publication_files"]), "playlist_files": len(config["playlist_files"]), "purge_files": len(config["purge_files"]), "endpoints": len(config["endpoints"])}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
