#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Channel identity, quota, and family-list hygiene helpers."""
from __future__ import annotations

import re

from channel_utils import cctv_key


_RESOLUTION_SUFFIX = re.compile(
    r"(?:\((?:\d{3,4}p|HD|FHD|UHD|4K|\u9ad8\u6e05|\u8d85\u6e05|\u6807\u6e05|\u84dd\u5149)\)|"
    r"[-_ ]?(?:\d{3,4}p|HD|FHD|UHD|4K|\u9ad8\u6e05|\u8d85\u6e05|\u6807\u6e05|\u84dd\u5149))$",
    re.I,
)
_CCTV_NUMBERED_ALIAS_SUFFIX = re.compile(
    r"^(CCTV[-_ ]?\d+\+?)(?:\u5965\u6797\u5339\u514b|\u4f53\u80b2\u8d5b\u4e8b|\u4e2d\u6587\u56fd\u9645)$",
    re.I,
)
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


def canonical_channel_key(name: str) -> str:
    """Return the key used for line quotas, coverage, and refill accounting."""
    text = re.sub(r"\s+", "", (name or "").strip())
    alias_match = _CCTV_NUMBERED_ALIAS_SUFFIX.match(text)
    if alias_match:
        text = alias_match.group(1)
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
