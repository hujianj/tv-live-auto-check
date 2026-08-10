#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validated source lifecycle configuration shared by fetch and publication checks."""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE_CONFIG = ROOT / "config" / "sources.json"
SOURCE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,79}$")


@dataclass(frozen=True)
class SourceSpec:
    name: str
    url: str
    enabled: bool
    auto_recover: bool = False
    note: str = ""

    @property
    def mode(self) -> str:
        if self.enabled:
            return "enabled"
        if self.auto_recover:
            return "recovery"
        return "disabled"

    @property
    def should_probe(self) -> bool:
        return self.enabled or self.auto_recover


def load_source_specs(path: Path = SOURCE_CONFIG) -> list[SourceSpec]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        raise ValueError(f"cannot read source config {path}: {exc}") from exc
    if not isinstance(raw, list) or not raw:
        raise ValueError("source config must be a non-empty list")

    specs: list[SourceSpec] = []
    seen_names: set[str] = set()
    seen_urls: set[str] = set()
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError(f"source config entries must be objects: {item!r}")
        name = str(item.get("name") or "").strip()
        url = str(item.get("url") or "").strip()
        if not SOURCE_NAME.fullmatch(name):
            raise ValueError(f"invalid source name: {name!r}")
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"source {name!r} must use an absolute HTTP(S) URL")
        if name in seen_names:
            raise ValueError(f"duplicate source name: {name}")
        if url in seen_urls:
            raise ValueError(f"duplicate source URL: {url}")
        seen_names.add(name)
        seen_urls.add(url)
        enabled = item.get("enabled", True)
        auto_recover = item.get("auto_recover", False)
        if type(enabled) is not bool or type(auto_recover) is not bool:
            raise ValueError(f"source {name!r} enabled/auto_recover must be boolean")
        if enabled and auto_recover:
            raise ValueError(f"source {name!r} cannot be both enabled and auto_recover")
        specs.append(SourceSpec(name, url, enabled, auto_recover, str(item.get("note") or "").strip()))

    if not any(spec.enabled for spec in specs):
        raise ValueError("source config must contain at least one enabled source")
    return specs


def probe_source_specs(path: Path = SOURCE_CONFIG) -> list[SourceSpec]:
    return [spec for spec in load_source_specs(path) if spec.should_probe]


def configured_source_pairs(path: Path = SOURCE_CONFIG, *, probe: bool = False) -> list[tuple[str, str]]:
    specs = probe_source_specs(path) if probe else load_source_specs(path)
    return [(spec.name, spec.url) for spec in specs if probe or spec.enabled]
