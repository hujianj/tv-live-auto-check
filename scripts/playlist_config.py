#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from datetime import datetime, timezone
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


def _parse_utc_timestamp(value: object) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def apply_home_priority_freshness(data: dict, now: datetime | None = None) -> dict:
    """Disable one-shot home-network hints after their bounded lifetime."""
    result = dict(data)
    ok_urls = list(result.get("home_ok_urls") or [])
    failed_urls = list(result.get("home_failed_urls") or [])
    active = bool(ok_urls or failed_urls)
    now_utc = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    max_age_hours = max(1, int(result.get("max_age_hours", 14 * 24)))
    generated = _parse_utc_timestamp(result.get("generated_at_utc"))
    expires = _parse_utc_timestamp(result.get("expires_at_utc"))
    age_hours = max(0.0, (now_utc - generated).total_seconds() / 3600.0) if generated else None
    stale_reason = ""
    if active:
        if generated is None:
            stale_reason = "missing or invalid generated_at_utc"
        elif expires is not None and now_utc >= expires:
            stale_reason = "expires_at_utc reached"
        elif expires is None and age_hours is not None and age_hours >= max_age_hours:
            stale_reason = "max_age_hours reached"
    if stale_reason:
        result["home_ok_urls"] = []
        result["home_failed_urls"] = []
    result["max_age_hours"] = max_age_hours
    result["_configured"] = active
    result["_configured_ok_urls"] = len(ok_urls)
    result["_configured_failed_urls"] = len(failed_urls)
    result["_active"] = active and not bool(stale_reason)
    result["_fresh"] = not bool(stale_reason)
    result["_stale_reason"] = stale_reason
    result["_age_hours"] = round(age_hours, 3) if age_hours is not None else None
    return result


def load_home_priority() -> dict:
    path = CONFIG_DIR / "home-priority.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("home-priority.json must contain a JSON object")
    return apply_home_priority_freshness(data)


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
