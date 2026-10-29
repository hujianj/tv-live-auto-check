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


def local_quality_rank(data: dict | None, url: str, cfg: dict) -> tuple:
    """Fresh local measurements guide ordering only; never waive cloud checks."""
    if not data or not data.get('enabled') or not data.get('_active') or not data.get('_fresh'):
        return 2, 0.0
    quality = data.get('home_quality') or {}
    if not isinstance(quality, dict):
        return 2, 0.0
    evidence = quality.get(url)
    if not isinstance(evidence, dict):
        return 2, 0.0
    if evidence.get('ok') is False:
        return 4, 0.0
    ratio = evidence.get('media_realtime_ratio')
    frames = evidence.get('decoded_frames', 0)
    if (evidence.get('ok') is not True or not isinstance(frames, int) or frames < 3
            or evidence.get('media_measurement') not in {'complete_segment', 'partial_segment_estimate'}
            or not isinstance(ratio, (int, float)) or isinstance(ratio, bool)
            or not math.isfinite(ratio) or ratio <= 0):
        return 2, 0.0
    tier = 0 if ratio >= float(cfg.get('preferred_realtime_margin', 2.0)) else (
        1 if ratio >= float(cfg.get('minimum_realtime_margin', 1.0)) else 3)
    return tier, -ratio


def playback_rank(result, url: str, source_score: tuple, history: dict,
                  local_quality: dict | None = None) -> tuple:
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
    local_tier, local_speed = local_quality_rank(local_quality, url, cfg)
    return local_tier, tier, history_tier, source_score[0], local_speed, -(ratio or 0), source_score[1:], url


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
