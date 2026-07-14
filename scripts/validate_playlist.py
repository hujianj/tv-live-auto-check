#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

G_CCTV = "\u592e\u89c6\u9891\u9053"
G_SAT = "\u536b\u89c6\u9891\u9053"
G_LOCAL = "\u5730\u65b9\u9891\u9053"
G_MOVIE = "\u5f71\u89c6\u5267\u573a"
G_KIDS = "\u5c11\u513f\u52a8\u6f2b"
G_SPORT_DOC = "\u4f53\u80b2\u7eaa\u5b9e"
G_MUSIC_SHOW = "\u97f3\u4e50\u7efc\u827a"
G_LIFE = "\u751f\u6d3b\u4f11\u95f2"
G_ENT = "\u7efc\u5408\u5a31\u4e50"
G_HK = "\u6e2f\u6fb3\u53f0\u9891\u9053"
G_OVERSEA = "\u6d77\u5916\u534e\u8bed\u9891\u9053"
GROUP_ORDER = [G_CCTV, G_SAT, G_LOCAL, G_MOVIE, G_KIDS, G_SPORT_DOC, G_MUSIC_SHOW, G_LIFE, G_ENT, G_HK, G_OVERSEA]

BAD_NAME_TOKENS = ["group-title=", "tvg-logo=", "user-agent", "likeGecko", "w_400", "h_500", "#EXTINF"]
UNWANTED_OVERSEAS_TOKENS = [
    "PLUTOTV", "PLUTO", "REDBULL", "BUDAPEST", "BOGOTA", "BRASIL", "BRAZIL",
    "BULGARIA", "BULGARIAONAIR", "BANGLA", "MOVIEBANGLA", "NEWS18BANGLA",
    "NEWS21BANGLA", "BRESCIA", "BREMEN", "BODENSEE", "BANDUNG",
    "BOJONEGORO", "BARILOCHE", "ASUNCION", "LIONSGATE", "WEDOTV",
    "EBONYTV", "CITYTV", "PEACETV", "PENIEL", "STASHTV", "SUPERTV",
    "CONECTV", "CREATV", "DELTATV", "RTVBN", "RADIO", "MTV",
    "NICKELODEON", "NICKJR", "NICKTOONS", "CIN\u00c9", "CINE",
]
HK_CN_KEYS = ["\u9999\u6e2f", "\u6fb3\u95e8", "\u6fb3\u9580", "\u53f0\u6e7e", "\u53f0\u7063", "\u6e2f\u53f0", "\u51e4\u51f0", "\u9cf3\u51f0", "\u7fe1\u7fe0", "\u660e\u73e0", "\u6c11\u89c6", "\u4e2d\u89c6", "\u534e\u89c6", "\u53f0\u89c6", "\u4e1c\u68ee", "\u4e09\u7acb", "\u4e2d\u5929"]
HK_LATIN_PREFIXES = ("RTHK", "VIUTV", "TVBS", "PHOENIX")
TVB_PREFIXES = ("TVBJADE", "TVBPEARL", "TVBNEWS", "TVBFINANCE", "TVBENTERTAINMENT", "TVBCLASSIC", "TVBPLUS", "TVBSPORTS")


def chinese_count(s: str) -> int:
    return sum(1 for ch in s if "\u4e00" <= ch <= "\u9fff")


def cctv_num(name: str):
    m = re.match(r"^CCTV[-_ ]?(\d+)(\+?)", name, re.I)
    if not m:
        return None
    return int(m.group(1)), 1 if m.group(2) else 0


def is_hk_mo_tw_channel(name: str, group: str = "") -> bool:
    upper = name.upper()
    if any(k in name for k in HK_CN_KEYS):
        return True
    if chinese_count(name) > 0 and any(k in (group or "") for k in HK_CN_KEYS):
        return True
    if upper.startswith(HK_LATIN_PREFIXES) or upper.startswith(TVB_PREFIXES):
        return True
    return bool(re.search(r"(^|[^A-Z0-9])(RTHK|VIUTV|TVB|TVBS|PHOENIX)([^A-Z0-9]|$)", upper))


def has_invalid_channel_name(name: str) -> bool:
    if not name or not name.strip():
        return True
    low = name.lower()
    if "\ufffd" in name:
        return True
    if any((ord(ch) < 32 or ord(ch) == 127) for ch in name):
        return True
    if "," in name:
        return True
    if re.search(r"https?://", name, re.I):
        return True
    if name.endswith("#genre#"):
        return True
    if any(tok.lower() in low for tok in BAD_NAME_TOKENS):
        return True
    return False


def has_invalid_url(url: str) -> bool:
    if not url or not url.startswith(("http://", "https://")):
        return True
    if "\ufffd" in url:
        return True
    if any(ch.isspace() for ch in url):
        return True
    if url.rstrip() != url:
        return True
    if url.endswith(","):
        return True
    # Raw duplicate URL delimiters usually come from malformed upstream TXT rows,
    # e.g. url1;http://url2 or url1#https://url2. They break many TV players.
    if re.search(r"[;#](?=https?://)", url, re.I):
        return True
    if len(re.findall(r"https?://", url, re.I)) != 1:
        return True
    return False


def split_unquoted_last_comma(line: str) -> tuple[str, str]:
    in_quote = False
    escape = False
    split_at = -1
    for i, ch in enumerate(line):
        if escape:
            escape = False
            continue
        if ch == "\\":
            escape = True
            continue
        if ch == '"':
            in_quote = not in_quote
            continue
        if ch == "," and not in_quote:
            split_at = i
    if split_at < 0:
        return line, ""
    return line[:split_at], line[split_at + 1:].strip()


def validate_channel_semantics(group: str, name: str, url: str, lineno: int, line: str, bad: list[tuple[int, str, str]]) -> None:
    upper_name = name.upper()
    if has_invalid_channel_name(name):
        bad.append((lineno, "invalid/polluted channel name", line[:240]))
    if has_invalid_url(url):
        bad.append((lineno, "invalid/suspicious url", line[:240]))
    if group == G_CCTV and any(tok in upper_name for tok in ["RTHK", "TVB", "VIUTV"]):
        bad.append((lineno, "pseudo CCTV alias", line[:240]))
    if "NOT24/7" in upper_name or "NOT 24/7" in upper_name:
        bad.append((lineno, "unstable Not24/7", line[:240]))
    if not cctv_num(name) and not is_hk_mo_tw_channel(name, group):
        if any(tok in upper_name for tok in UNWANTED_OVERSEAS_TOKENS):
            bad.append((lineno, "unwanted overseas/English channel", line[:240]))
        if chinese_count(name) == 0 and re.search(r"[A-Z]{3,}", upper_name):
            bad.append((lineno, "pure Latin overseas/English channel", line[:240]))


def validate_categories(groups: list[str], bad: list[tuple[int, str, str]]) -> None:
    missing = [g for g in GROUP_ORDER if g not in groups]
    for g in missing:
        bad.append((0, "missing category", f"{g},#genre#"))
    for old in ["\u5f71\u89c6\u5a31\u4e50", "\u5176\u4ed6\u9891\u9053"]:
        if old in groups:
            bad.append((0, "obsolete category", f"{old},#genre#"))


def validate_text(text: str, require_categories: bool = True) -> dict:
    bad: list[tuple[int, str, str]] = []
    groups: list[str] = []
    rows: list[tuple[str, str, str]] = []
    current_group = ""
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.endswith(",#genre#"):
            current_group = line.split(",", 1)[0].strip()
            groups.append(current_group)
            if current_group not in GROUP_ORDER:
                bad.append((lineno, "unexpected category", line[:240]))
            continue
        if "," not in line:
            bad.append((lineno, "missing comma", line[:240]))
            continue
        name, url = line.split(",", 1)
        rows.append((current_group, name, url))
        validate_channel_semantics(current_group, name, url, lineno, line, bad)
    if require_categories:
        validate_categories(groups, bad)
    if bad:
        raise ValueError("invalid playlist rows: " + repr(bad[:40]))
    group_counts = Counter(g for g, _, _ in rows)
    return {
        "groups": dict(group_counts),
        "rows": len(rows),
        "unique_names": len({n for _, n, _ in rows}),
        "unique_urls": len({u for _, _, u in rows}),
    }


def validate_m3u_text(text: str, require_categories: bool = True) -> dict:
    bad: list[tuple[int, str, str]] = []
    groups: list[str] = []
    rows: list[tuple[str, str, str]] = []
    lines = [(lineno, raw.strip()) for lineno, raw in enumerate(text.splitlines(), 1) if raw.strip()]
    if not lines or lines[0][1] != "#EXTM3U":
        bad.append((1, "missing #EXTM3U header", (lines[0][1] if lines else "")[:240]))
    i = 1
    while i < len(lines):
        lineno, line = lines[i]
        if line.startswith("#EXTINF"):
            head, display_name = split_unquoted_last_comma(line)
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', head))
            group = (attrs.get("group-title") or "").strip()
            tvg_name = (attrs.get("tvg-name") or "").strip()
            name = display_name or tvg_name
            if group:
                groups.append(group)
                if group not in GROUP_ORDER:
                    bad.append((lineno, "unexpected category", line[:240]))
            else:
                bad.append((lineno, "missing group-title", line[:240]))
            if not name:
                bad.append((lineno, "missing channel name", line[:240]))
            if tvg_name and display_name and tvg_name != display_name:
                # Mismatched names confuse diagnostics and make future TXT/M3U
                # parity checks harder. Keep both fields aligned in generated M3U.
                bad.append((lineno, "tvg-name/display-name mismatch", line[:240]))
            if i + 1 >= len(lines):
                bad.append((lineno, "missing URL after EXTINF", line[:240]))
                break
            url_lineno, url = lines[i + 1]
            if url.startswith("#"):
                bad.append((url_lineno, "missing URL after EXTINF", url[:240]))
                i += 1
                continue
            rows.append((group, name, url))
            validate_channel_semantics(group, name, url, url_lineno, f"{name},{url}", bad)
            i += 2
            continue
        if line.startswith("#"):
            i += 1
            continue
        bad.append((lineno, "orphan URL without EXTINF", line[:240]))
        i += 1
    if require_categories:
        validate_categories(groups, bad)
    if bad:
        raise ValueError("invalid m3u rows: " + repr(bad[:40]))
    group_counts = Counter(g for g, _, _ in rows)
    return {
        "format": "m3u",
        "groups": dict(group_counts),
        "rows": len(rows),
        "unique_names": len({n for _, n, _ in rows}),
        "unique_urls": len({u for _, _, u in rows}),
    }


def validate_file(path: Path, require_categories: bool = True) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".m3u", ".m3u8"} or text.lstrip().startswith("#EXTM3U"):
        return validate_m3u_text(text, require_categories=require_categories)
    return validate_text(text, require_categories=require_categories)


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: validate_playlist.py <playlist.txt> [more.txt...]", file=sys.stderr)
        return 2
    for arg in argv:
        path = Path(arg)
        result = validate_file(path)
        print(f"validate OK {path} " + json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
