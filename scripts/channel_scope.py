"""Shared channel-scope gate, independent of the checking network's location."""
from __future__ import annotations

import re

from channel_utils import chinese_count
from playlist_config import load_rules

POLICY_VERSION = 1
NETWORK_SCOPE = "current_execution_environment"
CHANNEL_SCOPE = "domestic_chinese"
POLICY = load_rules().get("channel_scope", {})

COUNTRY_ALIASES = {
    "china": "cn", "chn": "cn", "prc": "cn", "mainland china": "cn",
    "people's republic of china": "cn", "\u4e2d\u56fd": "cn", "\u4e2d\u570b": "cn",
    "hong kong": "hk", "hongkong": "hk", "hkg": "hk", "\u9999\u6e2f": "hk",
    "macau": "mo", "macao": "mo", "mac": "mo", "\u6fb3\u95e8": "mo", "\u6fb3\u9580": "mo",
    "taiwan": "tw", "twn": "tw", "\u53f0\u6e7e": "tw", "\u53f0\u7063": "tw",
    "united states": "us", "united states of america": "us", "usa": "us",
    "singapore": "sg", "sgp": "sg", "malaysia": "my", "mys": "my",
    "japan": "jp", "jpn": "jp", "canada": "ca", "can": "ca",
    "australia": "au", "aus": "au", "united kingdom": "gb", "uk": "gb",
}


def country_codes(value: str) -> set[str]:
    """Match whole country names/codes, never pairs of letters inside a word."""
    text = re.sub(r"\s+", " ", value.strip().casefold())
    if not text:
        return set()
    if text in COUNTRY_ALIASES:
        return {COUNTRY_ALIASES[text]}
    parts = re.split(r"[,;|/]+", text)
    if len(parts) == 1 and re.fullmatch(r"[a-z]{2}(?:\s+[a-z]{2})+", text):
        parts = text.split()
    return {COUNTRY_ALIASES.get(part.strip(), part.strip()) for part in parts if part.strip()}


def channel_countries(country: str = "", tvg_id: str = "") -> set[str]:
    countries = country_codes(country)
    suffix = re.search(r"\.([a-z]{2})(?:@[^\s]+)?$", tvg_id, re.I)
    if suffix:
        countries.add(suffix.group(1).lower())
    return countries


def known_domestic_name(name: str, tvg_id: str, source: str) -> str:
    """Translate only an exact reviewed channel ID/name pair, retaining warnings."""
    aliases = load_rules().get("domestic_channel_aliases", {})
    if source not in aliases.get("sources", []):
        return name
    entry = aliases.get("channels", {}).get(tvg_id.split("@", 1)[0])
    if not entry:
        return name
    base = re.sub(r"\s*\((?:\d{3,4}[pi]|HD|FHD|UHD|4K)\)\s*$", "", name, flags=re.I).strip()
    if base.casefold() not in {value.casefold() for value in entry["aliases"]}:
        return name
    return entry["name"]


def domestic_chinese_issue(name: str, group: str = "", source: str = "",
                           tvg_id: str = "", country: str = "", language: str = "") -> str:
    """Return a rejection reason; metadata is not proof of the spoken audio."""
    compact = re.sub(r"[\s_-]+", "", name).casefold()
    allowed_countries = set(POLICY.get("countries", ["cn", "hk", "mo", "tw"]))
    # iptv-org's channel IDs carry a country suffix. Do not infer origin from
    # a CDN hostname, server IP, or the runner's geographic location.
    countries = channel_countries(country, tvg_id)
    if countries and not countries.issubset(allowed_countries):
        return "foreign_channel_origin"
    if language:
        languages = set(re.findall(r"[a-z]+", language.lower()))
        if languages and not languages.intersection({"zh", "zho", "chi", "cmn", "yue", "nan", "hak", "chinese", "mandarin", "cantonese"}):
            return "non_chinese_language_metadata"
    rules = load_rules()
    tokens = [*POLICY.get("excluded_name_tokens", []), *rules.get("foreign_name_tokens", []),
              *rules.get("foreign_cn_tokens", []), *rules.get("drop_latin_tokens", [])]
    for token in tokens:
        if re.sub(r"[\s_-]+", "", token).casefold() in compact:
            return "foreign_or_non_chinese_channel"
    for pattern in POLICY.get("excluded_name_patterns", []):
        if re.search(pattern, name, re.I):
            return "foreign_or_non_chinese_channel"
    if source in set(POLICY.get("foreign_only_sources", [])):
        return "foreign_only_catalog"
    if any(token.casefold() in group.casefold() for token in POLICY.get("foreign_group_tokens", [])):
        return "foreign_channel_group"
    if re.fullmatch(r"(?:CCTV[-_ ]?(?:(?:[1-9]|1[0-7])\+?|[48]K)|CETV[-_ ]?[1-4])(?:HD|FHD|UHD|\((?:HD|FHD|\d+[pi])\))?", re.sub(r"\s+", "", name), re.I):
        return ""
    if chinese_count(name):
        return ""
    if any(re.fullmatch(pattern, name, re.I) for pattern in POLICY.get("chinese_latin_name_patterns", [])):
        return ""
    return "chinese_channel_identity_unconfirmed"
