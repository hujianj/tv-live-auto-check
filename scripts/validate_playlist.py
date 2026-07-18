#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import html
import re
import sys
from collections import Counter
from pathlib import Path

from playlist_config import get_group_order, load_quality, load_rules
from channel_utils import cctv_number, chinese_count as shared_chinese_count
from channel_identity import is_audio_only_channel
from url_utils import publishable_url_issue

RULES = load_rules()
QUALITY = load_quality()
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
GROUP_ORDER = get_group_order()

BAD_NAME_TOKENS = RULES["bad_name_tokens"]
UNWANTED_OVERSEAS_TOKENS = RULES["drop_latin_tokens"]
HK_CN_KEYS = RULES["hk_cn_keys"]
HK_LATIN_PREFIXES = tuple(RULES["hk_latin_prefixes"])
TVB_PREFIXES = tuple(RULES["tvb_prefixes"])
CCTV_ALIAS_BLOCK_TOKENS = [str(x).upper() for x in RULES["cctv_alias_block_tokens"]]
UNSTABLE_NAME_TOKENS = [str(x).upper() for x in RULES["unstable_name_tokens"]]
OBSOLETE_CATEGORIES = RULES["obsolete_categories"]
STRICT_DROP_NAME_TOKENS = [str(x) for x in QUALITY.get("strict_drop_name_tokens", [])]
STRICT_DROP_REGEX = [re.compile(str(x), re.I) for x in QUALITY.get("strict_drop_regex", [])]


def chinese_count(s: str) -> int:
    return shared_chinese_count(s)


def cctv_num(name: str):
    return cctv_number(name)


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
    return bool(publishable_url_issue(url))


def strict_quality_drop_reason(name: str) -> str:
    if QUALITY.get("drop_audio_only_channels", True) and is_audio_only_channel(name):
        return "audio-only:radio"
    low = (name or "").lower()
    for token in STRICT_DROP_NAME_TOKENS:
        if token and token.lower() in low:
            return f"token:{token}"
    for rx in STRICT_DROP_REGEX:
        if rx.search(name or ""):
            return f"regex:{rx.pattern}"
    return ""


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
    if group == G_CCTV and any(tok in upper_name for tok in CCTV_ALIAS_BLOCK_TOKENS):
        bad.append((lineno, "pseudo CCTV alias", line[:240]))
    if any(tok in upper_name for tok in UNSTABLE_NAME_TOKENS):
        bad.append((lineno, "unstable Not24/7", line[:240]))
    strict_reason = strict_quality_drop_reason(name)
    if strict_reason:
        bad.append((lineno, f"strict quality filtered channel ({strict_reason})", line[:240]))
    if not cctv_num(name) and not is_hk_mo_tw_channel(name, group):
        if any(tok in upper_name for tok in UNWANTED_OVERSEAS_TOKENS):
            bad.append((lineno, "unwanted overseas/English channel", line[:240]))
        if chinese_count(name) == 0 and re.search(r"[A-Z]{3,}", upper_name):
            bad.append((lineno, "pure Latin overseas/English channel", line[:240]))


def validate_categories(groups: list[str], bad: list[tuple[int, str, str]]) -> None:
    missing = [g for g in GROUP_ORDER if g not in groups]
    for g in missing:
        bad.append((0, "missing category", f"{g},#genre#"))
    for old in OBSOLETE_CATEGORIES:
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
            group = html.unescape((attrs.get("group-title") or "").strip())
            tvg_name = html.unescape((attrs.get("tvg-name") or "").strip())
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
