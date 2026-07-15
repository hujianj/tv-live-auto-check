#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

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


def cctv_variant_base(name: str) -> str | None:
    n = (name or "").strip()
    if cctv_key(n):
        return None
    m = re.match(r"^CCTV[-_ ]?(\d+)(\+?)", n, re.I)
    if not m:
        return None
    return f"CCTV-{int(m.group(1))}{'+' if m.group(2) else ''}"


def is_latin_noise_name(name: str) -> bool:
    """Report-only heuristic for English/overseas residue in the family list."""
    n = (name or "").strip()
    upper = n.upper()
    if cctv_key(n) or re.match(r"^CCTV[-_ ]?\d+", upper):
        return False
    if re.match(r"^(TVB|TVBS|RTHK|VIUTV|PHOENIX)", upper):
        return False
    return bool(re.search(r"[A-Za-z]{5,}", n))
