#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Channel identity, quota, and family-list hygiene helpers."""
from __future__ import annotations

import re

from channel_utils import cctv_key


_RESOLUTION_SUFFIX = re.compile(
    r"(?:\((?:\d{3,4}[pi]|HD|FHD|UHD|4K|\u9ad8\u6e05|\u8d85\u6e05|\u6807\u6e05|\u84dd\u5149)\)|"
    r"[-_ ]?(?:\d{3,4}[pi]|HD|FHD|UHD|4K|\u9ad8\u6e05|\u8d85\u6e05|\u6807\u6e05|\u84dd\u5149))$",
    re.I,
)
_CCTV_DESCRIPTIONS = {
    "1": {"\u7efc\u5408"}, "2": {"\u8d22\u7ecf"}, "3": {"\u7efc\u827a"},
    "4": {"\u4e2d\u6587\u56fd\u9645"}, "5": {"\u4f53\u80b2"},
    "5+": {"\u4f53\u80b2\u8d5b\u4e8b"}, "6": {"\u7535\u5f71"},
    "7": {"\u56fd\u9632\u519b\u4e8b", "\u519b\u4e8b\u519c\u4e1a"},
    "8": {"\u7535\u89c6\u5267"}, "9": {"\u7eaa\u5f55"}, "10": {"\u79d1\u6559"},
    "11": {"\u620f\u66f2"}, "12": {"\u793e\u4f1a\u4e0e\u6cd5"},
    "13": {"\u65b0\u95fb"}, "14": {"\u5c11\u513f"}, "15": {"\u97f3\u4e50"},
    "16": {"\u5965\u6797\u5339\u514b"}, "17": {"\u519c\u4e1a\u519c\u6751"},
}
_CHANNEL_SUFFIX = re.compile(
    r"(?:\u9ad8\u6e05\u9891\u9053|\u8d85\u6e05\u9891\u9053|\u6807\u6e05\u9891\u9053|\u9891\u9053)$",
    re.I,
)
_AUDIO_TOKEN_RE = re.compile(
    r"(?:\u5e7f\u64ad|\u7535\u53f0|\u4e4b\u58f0|"
    r"(?:^|[^A-Za-z])(?:FM|AM)[-_ ]?\d{2,4}(?:[.\-]\d+)?(?:[^A-Za-z]|$))",
    re.I,
)
_BROADCAST_TV_ORG_RE = re.compile(
    r"(?:\u5e7f\u64ad\u7535\u89c6\u53f0|\u5e7f\u64ad\u7535\u89c6|\u5e7f\u7535\u7f51\u7edc)",
    re.I,
)
_STATION_ALIASES = {
    "brtv\u5317\u4eac\u536b\u89c6": "\u5317\u4eac\u536b\u89c6",
    "btv\u5317\u4eac\u536b\u89c6": "\u5317\u4eac\u536b\u89c6",
}


def normalize_station_alias(name: str) -> str:
    compact = re.sub(r"\s+", "", name.strip())
    return _STATION_ALIASES.get(_RESOLUTION_SUFFIX.sub("", compact).casefold(), name)


def canonical_channel_key(name: str) -> str:
    """Return the key used for line quotas, coverage, and refill accounting."""
    text = re.sub(r"\s+", "", normalize_station_alias(name or "").strip())
    text = _RESOLUTION_SUFFIX.sub("", text)
    alias_match = re.fullmatch(r"CCTV[-_ ]?(\d+\+?)(.+)", text, re.I)
    if alias_match and alias_match.group(2) in _CCTV_DESCRIPTIONS.get(alias_match.group(1), set()):
        text = "CCTV-" + alias_match.group(1)
    exact_cctv = cctv_key(text)
    if exact_cctv:
        return exact_cctv
    text = _RESOLUTION_SUFFIX.sub("", text)
    exact_cctv = cctv_key(text)
    if exact_cctv:
        return exact_cctv
    # Upstream aliases often prepend CCTV to non-numbered paid specialty
    # channels. Treat these as the same identity, but never rewrite CCTV-1..17.
    if re.match(r"^CCTV[\u4e00-\u9fff]", text, re.I):
        text = re.sub(r"^CCTV", "", text, flags=re.I)
    text = _CHANNEL_SUFFIX.sub("", text)
    return text.casefold()


def is_audio_only_channel(name: str) -> bool:
    """True for radio/audio services that should not appear in a TV playlist.

    A station name containing ``broadcast television station`` describes the
    TV organisation rather than an audio service, so that phrase is removed
    before applying radio markers.
    """
    text = (name or "").strip()
    text = _BROADCAST_TV_ORG_RE.sub("", text)
    return bool(_AUDIO_TOKEN_RE.search(text))


def aliases_are_compatible(names: list[str]) -> bool:
    """Whether several labels are safe aliases for one URL.

    Conservative by design: unknown different names are treated as an identity
    conflict and excluded rather than publishing a playable stream under the
    wrong channel name.
    """
    keys = {canonical_channel_key(name) for name in names if name.strip()}
    return len(keys) <= 1
