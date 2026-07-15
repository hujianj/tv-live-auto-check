#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"

DEFAULT_GROUP_ORDER = [
    "央视频道",
    "卫视频道",
    "地方频道",
    "影视剧场",
    "少儿动漫",
    "体育纪实",
    "音乐综艺",
    "生活休闲",
    "综合娱乐",
    "港澳台频道",
    "海外华语频道",
]


@lru_cache(maxsize=None)
def load_json_config(filename: str) -> dict:
    path = CONFIG_DIR / filename
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_rules() -> dict:
    return load_json_config("rules.json")


def load_priority() -> dict:
    return load_json_config("priority.json")


def load_guard() -> dict:
    return load_json_config("guard.json")


def load_quality() -> dict:
    return load_json_config("quality.json")


def get_group_order() -> list[str]:
    rules = load_rules()
    groups = rules.get("group_order") or DEFAULT_GROUP_ORDER
    return [str(x) for x in groups]


def _contains_any(haystack: str, needles: list[str]) -> bool:
    return any(str(needle).lower() in haystack for needle in needles)


def _startswith_any(haystack: str, prefixes: list[str]) -> bool:
    return any(haystack.startswith(str(prefix).lower()) for prefix in prefixes)


def source_priority(source: str, url: str = "") -> int:
    """Lower is better. Rules are data-driven in config/priority.json."""
    src = (source or "").lower()
    u = (url or "").lower()
    for rule in load_priority().get("source_priority", []):
        matched = False
        if _contains_any(src, rule.get("source_contains_any", [])):
            matched = True
        if _startswith_any(src, rule.get("source_startswith_any", [])):
            matched = True
        if _contains_any(u, rule.get("url_contains_any", [])):
            matched = True
        if matched:
            return int(rule.get("score", 0))
    return int(load_priority().get("default_source_priority", 0))


def score_adjustments(context: str) -> dict[str, int]:
    adjustments = load_priority().get("score_adjustments", {})
    return {str(k): int(v) for k, v in (adjustments.get(context) or {}).items()}
