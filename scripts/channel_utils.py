#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import html
import re


def chinese_count(text: str) -> int:
    return sum(1 for ch in (text or "") if "\u4e00" <= ch <= "\u9fff")


def cctv_key(name: str) -> str | None:
    """Return exact core CCTV key.

    Resolution suffixes in parentheses are accepted. Variants such as CCTV-4K,
    CCTV-4FHD and CCTV-4中文国际 are deliberately not counted as the base core
    CCTV channel; this keeps coverage and quality reports honest.
    """
    m = re.match(r"^CCTV[-_ ]?(\d+)(\+?)(?:\((?:\d+p|HD|FHD|4K|高清|超清)\))?$", (name or "").strip(), re.I)
    if not m:
        return None
    return f"CCTV-{int(m.group(1))}{'+' if m.group(2) else ''}"


def cctv_number(name: str) -> tuple[int, int] | None:
    """Return broad CCTV number/plus tuple for sorting and grouping.

    This intentionally recognizes variants such as CCTV-4K or CCTV-5+体育 so
    they stay near their base CCTV channel in the TV list. Exact core coverage
    must use cctv_key() instead, otherwise variants would hide missing core
    channels.
    """
    m = re.match(r"^CCTV[-_ ]?(\d+)(\+?)", (name or "").strip(), re.I)
    if not m:
        return None
    return int(m.group(1)), 1 if m.group(2) else 0


def cctv_variant_base(name: str) -> str | None:
    n = (name or "").strip()
    if cctv_key(n):
        return None
    number = cctv_number(n)
    if not number:
        return None
    return f"CCTV-{number[0]}{'+' if number[1] else ''}"


def cctv_sort_key(name: str) -> tuple[int, int, int, str]:
    """Stable sort key for CCTV rows: exact base first, variants after it."""
    number = cctv_number(name)
    if not number:
        return 999, 9, 9, name or ""
    variant_rank = 0 if cctv_key(name) else 1
    return number[0], number[1], variant_rank, name or ""


def is_latin_noise_name(name: str) -> bool:
    """Report-only heuristic for English/overseas residue in the family list."""
    n = (name or "").strip()
    upper = n.upper()
    if cctv_key(n) or re.match(r"^CCTV[-_ ]?\d+", upper):
        return False
    if re.match(r"^(TVB|TVBS|RTHK|VIUTV|PHOENIX)", upper):
        return False
    return bool(re.search(r"[A-Za-z]{5,}", n))


def escape_m3u_attr(value: str) -> str:
    """Escape quoted M3U attribute values without changing display names."""
    text = str(value or "").replace("\r", " ").replace("\n", " ").replace("\t", " ").strip()
    return html.escape(text, quote=True)


def format_extinf(name: str, group: str) -> str:
    """Render a generated EXTINF line with safe quoted attributes."""
    return f'#EXTINF:-1 tvg-name="{escape_m3u_attr(name)}" group-title="{escape_m3u_attr(group)}",{name}'
