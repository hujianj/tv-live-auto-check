#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import concurrent.futures as cf
import csv
import gzip
import html
import ipaddress
import json
import os
import re
import socket
import ssl
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from channel_utils import cctv_number, format_extinf
from playlist_config import score_adjustments, source_priority as configured_source_priority

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
TIMEOUT = int(os.getenv("IPTV_CHECK_TIMEOUT", "6"))
FETCH_TIMEOUT = int(os.getenv("IPTV_FETCH_TIMEOUT", "20"))
MAX_WORKERS = int(os.getenv("IPTV_FETCH_WORKERS", "64"))
CHECK_WORKERS = int(os.getenv("IPTV_CHECK_WORKERS", "192"))
MAX_VALID_PER_NAME = int(os.getenv("IPTV_MAX_VALID_PER_NAME", "5"))
HLS_SEGMENT_CHECKS = int(os.getenv("IPTV_HLS_SEGMENT_CHECKS", "2"))
HLS_VARIANT_CHECKS = int(os.getenv("IPTV_HLS_VARIANT_CHECKS", "2"))
CORE_HLS_SEGMENT_CHECKS = int(os.getenv("IPTV_CORE_HLS_SEGMENT_CHECKS", str(max(3, HLS_SEGMENT_CHECKS))))
CORE_RETRY_ATTEMPTS = int(os.getenv("IPTV_CORE_RETRY_ATTEMPTS", "1"))
CORE_RETRY_TIMEOUT = int(os.getenv("IPTV_CORE_RETRY_TIMEOUT", "14"))
UA = "Player"
SOURCE_CONFIG = ROOT / "config" / "sources.json"
TRANSIENT_OUTPUTS = [
    "stream_check_results.csv",
    "live-all-playable.txt",
    "all-playable.m3u",
    "curated-source-map.csv",
    "published_recheck_results.csv",
]


def load_sources(path: Path = SOURCE_CONFIG) -> list[tuple[str, str]]:
    """Load enabled upstream playlist sources from config/sources.json."""
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for item in data:
        if item.get("enabled") is False:
            continue
        name = str(item.get("name") or "").strip()
        url = str(item.get("url") or "").strip()
        if not name or not url:
            raise ValueError(f"invalid source config item: {item!r}")
        if name in seen:
            raise ValueError(f"duplicate source name in {path}: {name}")
        seen.add(name)
        out.append((name, url))
    if not out:
        raise ValueError(f"no enabled source in {path}")
    return out


SOURCES = load_sources()

BAD_MARKERS = ("nosignal", "no-signal", "no_signal", "notfound", "404", "offline")
BAD_HTML = (b"<html", b"<!doctype html", b"<head", b"<body")
MEDIA_EXTS = (".ts", ".m4s", ".mp4", ".aac", ".mp3", ".flv")


def cleanup_transient_outputs() -> None:
    """Remove ignored diagnostic files so a failed partial run cannot mislead debugging."""
    for filename in TRANSIENT_OUTPUTS:
        path = ROOT / filename
        try:
            if path.exists():
                path.unlink()
        except OSError:
            pass

@dataclass(frozen=True)
class Candidate:
    source: str
    group: str
    name: str
    url: str

@dataclass
class SourceStatus:
    name: str
    url: str
    ok: bool
    bytes: int = 0
    parsed: int = 0
    error: str = ""

@dataclass
class CheckResult:
    cand: Candidate
    ok: bool
    detail: str


def decode_bytes(data: bytes, content_type: str = "") -> str:
    # Most Chinese IPTV lists are UTF-8; fall back to gb18030 only when needed.
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace")


def fetch_url(url: str, timeout: int = FETCH_TIMEOUT, max_bytes: int = 12_000_000) -> tuple[int, str, bytes, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Connection": "close"})
    with urlopen(req, timeout=timeout, context=ssl.create_default_context()) as r:
        code = getattr(r, "status", 200)
        ctype = r.headers.get("Content-Type") or ""
        data = r.read(max_bytes)
        final = r.geturl()
    if url.endswith(".gz") or "gzip" in (ctype.lower()):
        try:
            data = gzip.decompress(data)
        except Exception:
            pass
    return code, ctype, data, final


def normalize_name(name: str) -> str:
    name = html.unescape(name or "").strip().strip('"').strip("'")
    name = re.sub(r"\s+", "", name)
    # TXT playlist uses comma as delimiter; keep channel names delimiter-safe.
    name = name.replace(",", "\uFF0C")
    if name.startswith("\u4e2d\u592e"):
        name = name.replace("\u4e2d\u592e", "CCTV", 1)
    return name[:80] or "\u672a\u547d\u540d\u9891\u9053"




def split_stream_urls(url: str) -> list[str]:
    """Return clean candidate URLs from one messy upstream URL field.

    Some public TXT/M3U rows concatenate backup URLs in a single field, for
    example ``url1;http://url2`` or ``url1#https://url2``. Ku9 treats the whole
    field as one URL and fails. Do not merely keep the first URL here: split the
    field into independently checked candidates so a good backup URL is not
    lost. Delimiters are only recognized when immediately followed by another
    HTTP(S) URL, so normal query-string semicolons/fragments are preserved.
    """
    raw = html.unescape(url or "").strip().strip('"').strip("'").lstrip("\ufeff")
    if not raw:
        return []
    parts: list[str] = []
    for piece in re.split(r"[;#](?=https?://)", raw, flags=re.I):
        parts.extend(re.split(r",(?=https?://)", piece, flags=re.I))
    out: list[str] = []
    seen: set[str] = set()
    for piece in parts:
        clean = piece.strip().strip('"').strip("'").lstrip("\ufeff").rstrip(",").strip()
        if not clean or clean in seen:
            continue
        seen.add(clean)
        out.append(clean)
    return out


def normalize_stream_url(url: str) -> str:
    """Compatibility helper: return the first clean URL from a field."""
    urls = split_stream_urls(url)
    return urls[0] if urls else ""

def infer_group(name: str, group: str = "") -> str:
    G_CCTV = "\u592e\u89c6\u9891\u9053"
    G_SAT = "\u536b\u89c6\u9891\u9053"
    G_HK = "\u6d77\u5916\u53ca\u6e2f\u53f0"
    G_LOOP = "\u8f6e\u64ad\u9891\u9053"
    G_OTHER = "\u5176\u4ed6\u9891\u9053"
    g = (group or "").strip()
    n = name.upper()
    if "CCTV" in n or name.startswith("\u592e\u89c6") or name.startswith("\u4e2d\u592e") or "CGTN" in n:
        return G_CCTV
    if "\u536b\u89c6" in name:
        return G_SAT
    if any(x in g for x in ("\u9999\u6e2f", "\u6fb3\u95e8", "\u53f0\u6e7e", "\u6d77\u5916", "\u65e5\u672c", "\u65b0\u52a0\u5761", "\u9a6c\u6765\u897f\u4e9a")):
        return G_HK
    if any(x in g.lower() for x in ("movie", "sport", "news", "kids")):
        return G_HK
    if any(x in g for x in ("\u864e\u7259", "\u6597\u9c7c", "\u8f6e\u64ad", "\u54d4\u54e9")):
        return G_LOOP
    return g or G_OTHER

def split_unquoted_last_comma(line: str) -> tuple[str, str]:
    """Split an EXTINF line at the last comma that is not inside quotes.

    IPTV lists often place URLs, HTTP headers, logo paths, or UA strings in
    quoted attributes, and those values may contain commas. Splitting at the
    first comma corrupts the channel name and can produce invalid TXT rows such
    as ``w_400,h_500,...,real-name,url``. The channel display name is the tail
    after the final unquoted comma.
    """
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


def parse_m3u(text: str, source: str) -> list[Candidate]:
    out: list[Candidate] = []
    last_name = ""
    last_group = ""
    for raw in text.splitlines():
        line = raw.strip().lstrip("﻿")
        if not line:
            continue
        if line.startswith("#EXTINF"):
            head, tail = split_unquoted_last_comma(line)
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', head))
            # Prefer explicit tvg-name/title only when present. Otherwise use
            # the final unquoted comma tail, which is the M3U display name.
            last_name = normalize_name(attrs.get("tvg-name") or attrs.get("title") or tail or "")
            last_group = html.unescape(attrs.get("group-title") or "")
        elif line.startswith("#"):
            continue
        elif re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", line):
            for url in split_stream_urls(line):
                if url.startswith(("http://", "https://", "rtmp://")):
                    name = normalize_name(last_name or urlparse(url).path.rsplit("/", 1)[-1])
                    group = infer_group(name, last_group)
                    out.append(Candidate(source, group, name, url))
            last_name = ""
            last_group = ""
    return out

def parse_txt(text: str, source: str) -> list[Candidate]:
    out: list[Candidate] = []
    group = ""
    for raw in text.splitlines():
        line = raw.strip().lstrip("\ufeff")
        if not line or line.startswith("#"):
            continue
        if line.endswith(",#genre#"):
            group = line.split(",", 1)[0].strip()
            continue
        if "," in line:
            name, url = line.split(",", 1)
        elif " " in line:
            name, url = line.split(None, 1)
        else:
            continue
        name = normalize_name(name)
        for clean_url in split_stream_urls(url):
            if clean_url.startswith(("http://", "https://", "rtmp://")):
                out.append(Candidate(source, infer_group(name, group), name, clean_url))
    return out


def parse_playlist(text: str, source: str) -> list[Candidate]:
    if "#EXTM3U" in text[:2000] or "#EXTINF" in text[:5000]:
        return parse_m3u(text, source)
    return parse_txt(text, source)


def fetch_source(item: tuple[str, str]) -> tuple[SourceStatus, list[Candidate]]:
    name, url = item
    try:
        code, ctype, data, final = fetch_url(url)
        text = decode_bytes(data, ctype)
        cands = parse_playlist(text, name)
        warn = "" if cands else "WARN fetched but no supported HTTP/HTTPS/RTMP stream candidates"
        st = SourceStatus(name, url, True, len(data), len(cands), warn)
        return st, cands
    except Exception as e:
        return SourceStatus(name, url, False, 0, 0, repr(e)[:240]), []


def is_ipv6_url(url: str) -> bool:
    host = urlparse(url).hostname or ""
    try:
        return isinstance(ipaddress.ip_address(host), ipaddress.IPv6Address)
    except Exception:
        return ":" in host and not re.match(r"^\d+\.\d+\.\d+\.\d+$", host)


def http_get_small(url: str, max_bytes: int = 65536, timeout: int = TIMEOUT) -> tuple[int, str, bytes, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Connection": "close"})
    with urlopen(req, timeout=timeout, context=ssl.create_default_context()) as r:
        code = getattr(r, "status", 200)
        ctype = (r.headers.get("Content-Type") or "").lower()
        data = r.read(max_bytes)
        final = r.geturl()
    return code, ctype, data, final


def is_core_family_candidate(cand: Candidate) -> bool:
    name = cand.name or ""
    group = cand.group or ""
    return bool(cctv_number(name) or "卫视" in name or "央视频道" in group or "卫视频道" in group)


def looks_transient_failure(detail: str) -> bool:
    low = (detail or "").lower()
    transient = (
        "timed out",
        "timeouterror",
        "connectionreset",
        "connection reset",
        "remote end closed",
        "remotedisconnected",
        "incompleteread",
        "temporarily unavailable",
        "temporary failure",
        "ssl",
        "eof occurred",
    )
    permanent = (
        "http 404",
        "http 410",
        "not found",
        "forbidden",
        "bad marker/html",
        "unsupported scheme",
    )
    if any(x in low for x in permanent):
        return False
    return any(x in low for x in transient)


def looks_bad(data: bytes, text: str = "") -> bool:
    sample = (text or data[:4096].decode("utf-8", "ignore")).lower()
    if any(m in sample for m in BAD_MARKERS):
        return True
    if any(x in data[:256].lower() for x in BAD_HTML):
        return True
    return False


def unique_keep_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def parse_m3u8_items(text: str, base: str) -> tuple[list[str], list[str]]:
    """Return child playlists and media segments from an HLS playlist.

    A previous version only tested the first child/segment. This parser returns
    multiple candidates so the checker can verify more than one real media
    fragment and reduce false positives from one lucky/stale segment.
    """
    if any(m in text.lower() for m in BAD_MARKERS):
        return [], []
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    variants: list[str] = []
    segments: list[str] = []
    for i, line in enumerate(lines):
        if line.startswith("#EXT-X-STREAM-INF"):
            for nxt in lines[i + 1:]:
                if not nxt.startswith("#"):
                    variants.append(urljoin(base, nxt))
                    break
    for i, line in enumerate(lines):
        if line.startswith("#EXTINF"):
            for nxt in lines[i + 1:]:
                if not nxt.startswith("#"):
                    segments.append(urljoin(base, nxt))
                    break
    if not segments:
        for line in lines:
            low = line.lower()
            if not line.startswith("#") and any(ext in low for ext in MEDIA_EXTS):
                segments.append(urljoin(base, line))
    return unique_keep_order(variants), unique_keep_order(segments)


def check_media_segments(segments: list[str], limit: int = HLS_SEGMENT_CHECKS, timeout: int = TIMEOUT) -> tuple[bool, str]:
    if not segments:
        return False, "no segment"
    checked = 0
    for seg in segments[:max(1, limit)]:
        c, ct, d, f = http_get_small(seg, max_bytes=4096, timeout=timeout)
        checked += 1
        if c >= 400 or not looks_media(d, ct):
            return False, f"segment bad {c} {ct} bytes={len(d)} checked={checked}"
    return True, f"segments ok checked={checked}"


def parse_next_from_m3u8(text: str, base: str) -> tuple[str | None, str | None]:
    # Compatibility helper for older report wording; new code uses parse_m3u8_items().
    variants, segments = parse_m3u8_items(text, base)
    if variants:
        return "playlist", variants[0]
    if segments:
        return "segment", segments[0]
    return None, None


def looks_media(data: bytes, ctype: str) -> bool:
    if looks_bad(data):
        return False
    if len(data) < 188:
        return False
    if data[:1] == b"G" or data[:1] == b"\x47":
        return True
    if data[:4] in (b"\x00\x00\x00\x18", b"\x00\x00\x00 ") or b"ftyp" in data[:32]:
        return True
    if any(x in ctype for x in ("video", "audio", "octet-stream", "mp2t")):
        return True
    return False


def check_candidate(cand: Candidate, timeout: int = TIMEOUT) -> CheckResult:
    url = cand.url.strip()
    if not url.startswith(("http://", "https://")):
        return CheckResult(cand, False, "unsupported scheme")
    segment_limit = CORE_HLS_SEGMENT_CHECKS if is_core_family_candidate(cand) else HLS_SEGMENT_CHECKS
    # For home Ku9 on common networks, IPv6-only URLs often fail; still test, but mark fail on network error.
    try:
        code, ctype, data, final = http_get_small(url, timeout=timeout)
        if code >= 400:
            return CheckResult(cand, False, f"http {code}")
        if looks_bad(data):
            return CheckResult(cand, False, "bad marker/html")
        text = data.decode("utf-8", "ignore")
        if "#EXTM3U" in text or "mpegurl" in ctype or url.lower().endswith((".m3u8", ".m3u")):
            variants, segments = parse_m3u8_items(text, final)
            if variants:
                checked_variants = 0
                last_detail = ""
                for child in variants[:max(1, HLS_VARIANT_CHECKS)]:
                    checked_variants += 1
                    c2, ct2, d2, f2 = http_get_small(child, timeout=timeout)
                    if c2 >= 400 or looks_bad(d2):
                        last_detail = f"child bad {c2}"
                        continue
                    t2 = d2.decode("utf-8", "ignore")
                    _v2, child_segments = parse_m3u8_items(t2, f2)
                    ok, detail = check_media_segments(child_segments, limit=segment_limit, timeout=timeout)
                    last_detail = detail
                    if ok:
                        return CheckResult(cand, True, f"variant ok variants_checked={checked_variants} {detail}")
                return CheckResult(cand, False, f"variant fail variants_checked={checked_variants} {last_detail}")
            ok, detail = check_media_segments(segments, limit=segment_limit, timeout=timeout)
            return CheckResult(cand, ok, detail)
        else:
            return CheckResult(cand, looks_media(data, ctype), f"direct {ctype} bytes={len(data)}")
    except Exception as e:
        return CheckResult(cand, False, repr(e)[:160])


def check_candidate_resilient(cand: Candidate) -> CheckResult:
    """Check a URL, with a slow retry for core family channels on transient failures."""
    first = check_candidate(cand, timeout=TIMEOUT)
    if first.ok or CORE_RETRY_ATTEMPTS <= 0:
        return first
    if not is_core_family_candidate(cand) or not looks_transient_failure(first.detail):
        return first
    last = first
    for attempt in range(1, CORE_RETRY_ATTEMPTS + 1):
        retry = check_candidate(cand, timeout=max(TIMEOUT, CORE_RETRY_TIMEOUT))
        if retry.ok:
            return CheckResult(cand, True, f"core retry ok attempt={attempt} first={first.detail}; {retry.detail}")
        last = retry
        if not looks_transient_failure(retry.detail):
            break
    return CheckResult(cand, False, f"{last.detail} (core retry after first={first.detail})")


def source_priority(source: str, url: str = "") -> int:
    """Lower is better. Kept as wrapper for tests and report code."""
    return configured_source_priority(source, url)


def prefer_score(c: Candidate) -> tuple[int, int, int, str]:
    u = c.url.lower()
    score = source_priority(c.source, c.url)
    adjust = score_adjustments("verify")
    # Ku9/TV boxes usually handle plain HTTP IPv4 IPTV better than IPv6/foreign CDN streams.
    if u.startswith("http://"):
        score += adjust.get("http_url", -20)
    if "epg.pw" in u:
        score += adjust.get("epg_pw", 15)
    if is_ipv6_url(c.url):
        score += adjust.get("ipv6", 30)
    return (score, len(c.url), len(c.source), c.source)


def main() -> None:
    cleanup_transient_outputs()
    start = time.time()
    print(f"Fetching {len(SOURCES)} sources...", flush=True)
    statuses: list[SourceStatus] = []
    all_cands: list[Candidate] = []
    with cf.ThreadPoolExecutor(max_workers=min(MAX_WORKERS, len(SOURCES))) as ex:
        futs = [ex.submit(fetch_source, item) for item in SOURCES]
        for fut in cf.as_completed(futs):
            st, cands = fut.result()
            statuses.append(st)
            all_cands.extend(cands)
            print(f"source {'OK' if st.ok else 'FAIL'} {st.name}: parsed={st.parsed} bytes={st.bytes} {st.error}", flush=True)

    # Deduplicate before expensive checking.
    # Full-check rule: every distinct stream URL is probed against a real media
    # playlist/segment. The same URL can appear under multiple channel names in
    # upstream lists; checking it once and reusing the result is equivalent for
    # playback validity and avoids thousands of duplicate network probes.
    dedup: dict[tuple[str, str], Candidate] = {}
    for c in all_cands:
        name = normalize_name(c.name)
        url = normalize_stream_url(c.url)
        if not name or len(url) > 1000:
            continue
        dedup.setdefault((name, url), Candidate(c.source, infer_group(name, c.group), name, url))

    url_to_candidates: dict[str, list[Candidate]] = {}
    for c in dedup.values():
        url_to_candidates.setdefault(c.url, []).append(c)
    to_check: list[Candidate] = []
    for url, arr in url_to_candidates.items():
        # Pick the best representative only for logging/source priority. The
        # check itself depends solely on URL; after probing, the result is copied
        # back to every channel-name alias that used this URL.
        to_check.append(sorted(arr, key=lambda c: (prefer_score(c), c.name))[0])
    to_check.sort(key=lambda c: (prefer_score(c), c.name, c.url))
    print(
        f"Parsed candidates={len(all_cands)}, unique_name_url={len(dedup)}, "
        f"unique_urls={len(url_to_candidates)}, checking_all_unique_urls={len(to_check)}, "
        f"workers={CHECK_WORKERS}, timeout={TIMEOUT}s",
        flush=True,
    )

    checked_by_url: dict[str, CheckResult] = {}
    with cf.ThreadPoolExecutor(max_workers=CHECK_WORKERS) as ex:
        futs = [ex.submit(check_candidate_resilient, c) for c in to_check]
        ok_count = 0
        for i, fut in enumerate(cf.as_completed(futs), 1):
            r = fut.result()
            checked_by_url[r.cand.url] = r
            if r.ok:
                ok_count += 1
            if i % 100 == 0 or i == len(futs):
                print(f"checked_url {i}/{len(futs)}, ok_urls={ok_count}", flush=True)

    results: list[CheckResult] = []
    for url, arr in url_to_candidates.items():
        r = checked_by_url[url]
        for c in arr:
            results.append(CheckResult(c, r.ok, r.detail))

    valid_by_name: dict[str, list[Candidate]] = {}
    for r in results:
        if r.ok:
            valid_by_name.setdefault(r.cand.name, []).append(r.cand)
    all_valid: list[Candidate] = []
    for name, arr in valid_by_name.items():
        arr = sorted(arr, key=prefer_score)
        all_valid.extend(arr)

    valid: list[Candidate] = []
    for name, arr in valid_by_name.items():
        arr = sorted(arr, key=prefer_score)
        valid.extend(arr[:MAX_VALID_PER_NAME])

    group_order = ["\u592e\u89c6\u9891\u9053", "\u536b\u89c6\u9891\u9053", "\u5730\u65b9\u9891\u9053", "\u6d77\u5916\u53ca\u6e2f\u53f0", "\u8f6e\u64ad\u9891\u9053", "\u5176\u4ed6\u9891\u9053"]
    valid.sort(key=lambda c: (group_order.index(c.group) if c.group in group_order else 99, c.name, prefer_score(c)))
    all_valid.sort(key=lambda c: (group_order.index(c.group) if c.group in group_order else 99, c.name, prefer_score(c)))

    def render_txt(cands: list[Candidate]) -> str:
        txt_lines: list[str] = []
        for group in group_order + sorted(set(c.group for c in cands) - set(group_order)):
            rows = [c for c in cands if c.group == group]
            if not rows:
                continue
            if txt_lines:
                txt_lines.append("")
            txt_lines.append(f"{group},#genre#")
            for c in rows:
                txt_lines.append(f"{c.name},{c.url}")
        return "\n".join(txt_lines).strip() + "\n"

    live_txt = render_txt(valid)
    live_all_txt = render_txt(all_valid)
    (ROOT / "live.txt").write_bytes(live_txt.encode("utf-8"))
    (ROOT / "ku9-live.txt").write_bytes(live_txt.encode("utf-8"))
    (ROOT / "live-all-playable.txt").write_bytes(live_all_txt.encode("utf-8"))

    m3u = ["#EXTM3U"]
    for c in valid:
        m3u.append(format_extinf(c.name, c.group))
        m3u.append(c.url)
    (ROOT / "live.m3u").write_text("\n".join(m3u) + "\n", encoding="utf-8", newline="\n")

    all_m3u = ["#EXTM3U"]
    for c in all_valid:
        all_m3u.append(format_extinf(c.name, c.group))
        all_m3u.append(c.url)
    (ROOT / "all-playable.m3u").write_text("\n".join(all_m3u) + "\n", encoding="utf-8", newline="\n")

    generated_utc = datetime.now(timezone.utc).replace(microsecond=0)
    generated_beijing = generated_utc.astimezone(timezone(timedelta(hours=8)))
    summary = {
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "generated_utc": generated_utc.isoformat().replace("+00:00", "Z"),
        "generated_beijing": generated_beijing.strftime("%Y-%m-%d %H:%M:%S Asia/Shanghai"),
        "sources_total": len(SOURCES),
        "sources_fetched_ok": sum(1 for s in statuses if s.ok),
        "parsed_candidates": len(all_cands),
        "unique_candidates": len(url_to_candidates),
        "unique_name_url_candidates": len(dedup),
        "checked_candidates": len(to_check),
        "checked_all_unique": len(to_check) == len(url_to_candidates),
        "playable_channel_names": len(valid_by_name),
        "playable_unique_urls": ok_count,
        "playable_name_url_lines": len(all_valid),
        # Legacy name retained for compatibility; this is line count, not unique URL count.
        "playable_urls_found": len(all_valid),
        "all_playable_lines": len(all_valid),
        "pre_curated_published_lines": len(valid),
        "primary_published_lines": len(valid),
    }
    (ROOT / "full-check-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    with (ROOT / "sources_status.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "url", "fetch_ok", "bytes", "parsed", "error"])
        for st in statuses:
            w.writerow([st.name, st.url, st.ok, st.bytes, st.parsed, st.error])

    with (ROOT / "stream_check_results.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ok", "group", "name", "url", "source", "detail"])
        for r in sorted(results, key=lambda x: (not x.ok, x.cand.group, x.cand.name)):
            w.writerow([r.ok, r.cand.group, r.cand.name, r.cand.url, r.cand.source, r.detail])

    ok_sources: dict[str, int] = {}
    for c in valid:
        ok_sources[c.source] = ok_sources.get(c.source, 0) + 1
    report = [
        "# IPTV source verification report",
        "",
        f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Generated UTC: {generated_utc.isoformat().replace('+00:00', 'Z')}",
        f"Generated Beijing: {generated_beijing.strftime('%Y-%m-%d %H:%M:%S Asia/Shanghai')}",
        f"Elapsed: {time.time()-start:.1f}s",
        f"Sources total: {len(SOURCES)}",
        f"Sources fetched OK: {sum(1 for s in statuses if s.ok)}",
        f"Parsed candidates: {len(all_cands)}",
        f"Unique name+URL candidates: {len(dedup)}",
        f"Unique stream URLs: {len(url_to_candidates)}",
        f"Checked unique stream URLs: {len(to_check)}",
        f"Checked all unique URLs: {len(to_check) == len(url_to_candidates)}",
        f"Playable channel names: {len(valid_by_name)}",
        f"Playable unique URLs: {ok_count}",
        f"Playable name+URL lines: {len(all_valid)}",
        f"Playable URLs found (legacy line count): {len(all_valid)}",
        f"Pre-curated published playable lines: {len(valid)}",
        "",
        "## Source fetch status",
        "",
        "| Source | Fetch | Parsed | Bytes | Error |",
        "|---|---:|---:|---:|---|",
    ]
    for st in statuses:
        report.append(f"| {st.name} | {'OK' if st.ok else 'FAIL'} | {st.parsed} | {st.bytes} | {st.error.replace('|','/')} |")
    report += ["", "## Pre-curation playable lines by source", "", "| Source | Lines |", "|---|---:|"]
    for src, n in sorted(ok_sources.items(), key=lambda x: (-x[1], x[0])):
        report.append(f"| {src} | {n} |")
    report += ["", "## First 80 pre-curation playable channel candidates", ""]
    for c in valid[:80]:
        report.append(f"- {c.group} / {c.name} / {c.source}")
    (ROOT / "source-report.md").write_text("\n".join(report) + "\n", encoding="utf-8", newline="\n")
    (ROOT / "check-report.md").write_text("\n".join(report) + "\n", encoding="utf-8", newline="\n")

    print(f"DONE valid_names={len(valid_by_name)} valid_lines={len(valid)}", flush=True)
    print(f"Wrote live.txt bytes={(ROOT/'live.txt').stat().st_size}", flush=True)

if __name__ == "__main__":
    main()
