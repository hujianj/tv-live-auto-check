"""Playback-oriented ranking of verified rows (never a substitute for probing)."""
from __future__ import annotations

import math
from collections import Counter, defaultdict
from urllib.parse import urlsplit

from channel_identity import canonical_channel_key
from playlist_config import load_quality
from stability import stability_adjustment


def host_identity(url: str) -> str:
    # Different ports, schemes and query strings are not independent servers.
    return (urlsplit(url).hostname or "unknown").lower().rstrip(".")


def playback_rank(result, url: str, source_score: tuple, history: dict) -> tuple:
    cfg = load_quality().get("playback_selection", {})
    ratio = result.media_realtime_ratio
    measured = ratio is not None and math.isfinite(ratio) and ratio > 0
    if measured:
        tier = 0 if ratio >= float(cfg.get("preferred_realtime_margin", 2.0)) else (
            1 if ratio >= float(cfg.get("minimum_realtime_margin", 1.0)) else 3)
    else:
        tier = 2  # Unknown is not a speed pass, but better than a proven slow line.
    adjust = stability_adjustment(url, history)
    history_tier = 0 if adjust <= -30 else (2 if adjust >= 45 else 1)
    # Keep the user's source preference within comparable quality/history tiers.
    # Total probe duration includes intentional waits and must not rank playback.
    return tier, history_tier, source_score[0], -(ratio or 0), source_score[1:], url


def prefer_independent_hosts(sorted_rows: list, limit: int) -> list:
    selected, duplicates = [], []
    hosts = set()
    for row in sorted_rows:
        host = host_identity(row.url)
        if host not in hosts:
            selected.append(row)
            hosts.add(host)
        else:
            duplicates.append(row)
    return (selected + duplicates)[:limit]


def redundancy_summary(rows: list, results: dict | None = None) -> dict:
    grouped = defaultdict(list)
    for row in rows:
        grouped[(row.group, canonical_channel_key(row.name))].append(row)
    distribution = Counter(len({row.url for row in items}) for items in grouped.values())
    primary_hosts = Counter(host_identity(items[0].url) for items in grouped.values())
    measurements = Counter(getattr((results or {}).get(row.url), "media_measurement", "unmeasured") for row in rows)
    return {
        "channel_count": len(grouped), "line_count": len(rows),
        "channels_by_line_count": {str(k): v for k, v in sorted(distribution.items())},
        "single_line_channels": distribution.get(1, 0),
        "channels_with_independent_host_backups": sum(
            len({host_identity(row.url) for row in items}) > 1 for items in grouped.values()),
        "primary_host_counts": dict(primary_hosts.most_common()),
        "media_measurements": dict(measurements),
        "measurement_scope": "current runner network; worst sampled HLS segment margin, not TV playback guarantee",
    }
