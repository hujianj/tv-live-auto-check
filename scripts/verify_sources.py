#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import concurrent.futures as cf
import csv
import hashlib
import zlib
import html
import ipaddress
import json
import os
import re
import sys
import threading
import time
import uuid
from collections import Counter, deque
from dataclasses import asdict, dataclass, replace
from datetime import datetime, timezone, timedelta
from pathlib import Path
from contextlib import contextmanager
from typing import Iterable
from urllib.parse import quote, unquote, urljoin, urlparse, urlsplit
from urllib.error import HTTPError, URLError
from urllib.request import Request

from channel_utils import cctv_number, format_extinf
from playlist_config import score_adjustments, source_priority as configured_source_priority
from url_utils import is_publishable_http_url, normalize_stream_url, publishable_url_issue, split_stream_urls
from network_safety import public_urlopen
from source_config import SourceSpec, configured_source_pairs, load_source_specs, probe_source_specs
from media_probe import looks_media as probe_looks_media, probe_media
from media_decode import DecodeResult, MAX_INIT_BYTES, MAX_SAMPLE_BYTES, decode_video
from source_adapters import parse as parse_source_data
from source_policy import POLICY_VERSION as SOURCE_POLICY_VERSION, discovery_links, publication_issue, source_record
from channel_scope import CHANNEL_SCOPE, NETWORK_SCOPE, POLICY_VERSION as CHANNEL_POLICY_VERSION, domestic_chinese_issue, known_domestic_name
from url_utils import redact_text
from scan_checkpoint import ScanCheckpoint

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
TIMEOUT = int(os.getenv("IPTV_CHECK_TIMEOUT", "6"))
FETCH_TIMEOUT = int(os.getenv("IPTV_FETCH_TIMEOUT", "20"))
MAX_WORKERS = int(os.getenv("IPTV_FETCH_WORKERS", "64"))
CHECK_WORKERS = int(os.getenv("IPTV_CHECK_WORKERS", "128"))
HOST_WORKERS = max(1, int(os.getenv("IPTV_CHECK_WORKERS_PER_HOST", "8")))
MAX_VALID_PER_NAME = int(os.getenv("IPTV_MAX_VALID_PER_NAME", "5"))
MAX_CANDIDATES_PER_SOURCE = int(os.getenv("IPTV_MAX_CANDIDATES_PER_SOURCE", "50000"))
MAX_TOTAL_CANDIDATES = int(os.getenv("IPTV_MAX_TOTAL_CANDIDATES", "250000"))
MAX_UNIQUE_URLS = int(os.getenv("IPTV_MAX_UNIQUE_URLS", "100000"))
MAX_SOURCE_BYTES = int(os.getenv("IPTV_MAX_SOURCE_BYTES", "30000000"))
MAX_TOTAL_FETCH_BYTES = int(os.getenv("IPTV_MAX_TOTAL_FETCH_BYTES", "180000000"))
MAX_PENDING_FUTURES = max(CHECK_WORKERS, int(os.getenv("IPTV_MAX_PENDING_FUTURES", "1024")))
HLS_SEGMENT_CHECKS = int(os.getenv("IPTV_HLS_SEGMENT_CHECKS", "2"))
HLS_VARIANT_CHECKS = int(os.getenv("IPTV_HLS_VARIANT_CHECKS", "2"))
CORE_HLS_SEGMENT_CHECKS = int(os.getenv("IPTV_CORE_HLS_SEGMENT_CHECKS", str(max(3, HLS_SEGMENT_CHECKS))))
CORE_RETRY_ATTEMPTS = int(os.getenv("IPTV_CORE_RETRY_ATTEMPTS", "1"))
CORE_RETRY_TIMEOUT = int(os.getenv("IPTV_CORE_RETRY_TIMEOUT", "14"))
HLS_PROGRESS_MIN_WAIT = float(os.getenv("IPTV_HLS_PROGRESS_MIN_WAIT", "3"))
HLS_PROGRESS_MAX_WAIT = float(os.getenv("IPTV_HLS_PROGRESS_MAX_WAIT", "14"))
HLS_PROGRESS_TARGET_MULTIPLIER = float(os.getenv("IPTV_HLS_PROGRESS_TARGET_MULTIPLIER", "1.25"))
REQUIRE_VIDEO_TRACK = os.getenv("IPTV_REQUIRE_VIDEO_TRACK", "1").strip().lower() not in {"0", "false", "no", "off"}
UA = "Player"
URL_BUDGET = max(10, int(os.getenv("IPTV_URL_BUDGET_SECONDS", "60")))
_PROBE_CONTEXT = threading.local()
SOURCE_CONFIG = ROOT / "config" / "sources.json"
TRANSIENT_OUTPUTS = [
    "stream_check_results.csv",
    "live-all-playable.txt",
    "all-playable.m3u",
    "curated-source-map.csv",
    "published_recheck_results.csv",
    "curated-candidate-pool.csv",
    "alias-conflict-report.md",
]


def load_sources(path: Path = SOURCE_CONFIG) -> list[tuple[str, str]]:
    """Load enabled upstream playlist sources from config/sources.json."""
    out = configured_source_pairs(path)
    if not out:
        raise ValueError(f"no enabled source in {path}")
    return out


SOURCES = load_sources()
SOURCE_SPECS = load_source_specs()
PROBE_SPECS = probe_source_specs()
PROBE_SOURCES = [(spec.name, spec.url) for spec in PROBE_SPECS]

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
    tvg_id: str = ""
    tvg_logo: str = ""
    country: str = ""
    language: str = ""

@dataclass
class SourceStatus:
    name: str
    url: str
    ok: bool
    bytes: int = 0
    parsed: int = 0
    truncated: bool = False
    error: str = ""
    mode: str = "enabled"
    contributed: bool = False
    checked_at: str = ""
    eligible: int = 0
    excluded: dict | None = None
    discovered_links: list[str] | None = None
    transport: str = "direct"

@dataclass
class CheckResult:
    cand: Candidate
    ok: bool
    detail: str
    elapsed_seconds: float = 0.0
    checked_at: str = ""
    decoded_frames: int = 0


def order_source_statuses(statuses: Iterable[SourceStatus], sources: list[tuple[str, str]] | None = None) -> list[SourceStatus]:
    """Return fetch results in configured source order, independent of thread completion order."""
    configured = SOURCES if sources is None else sources
    by_name = {status.name: status for status in statuses}
    expected_names = [name for name, _url in configured]
    if len(by_name) != len(expected_names) or set(by_name) != set(expected_names):
        missing = sorted(set(expected_names) - set(by_name))
        extra = sorted(set(by_name) - set(expected_names))
        raise ValueError(f"source fetch result mismatch: missing={missing!r} extra={extra!r}")
    return [by_name[name] for name in expected_names]


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


_HOST_SEMAPHORES: dict[str, threading.BoundedSemaphore] = {}
_HOST_SEMAPHORES_LOCK = threading.Lock()


def stream_host_key(url: str) -> str:
    return (urlparse(url).netloc or "unknown").lower()


@contextmanager
def host_slot(url: str):
    host = stream_host_key(url)
    with _HOST_SEMAPHORES_LOCK:
        sem = _HOST_SEMAPHORES.setdefault(host, threading.BoundedSemaphore(HOST_WORKERS))
    deadline = getattr(_PROBE_CONTEXT, "deadline", None)
    if deadline:
        if not sem.acquire(timeout=max(0, deadline - time.monotonic())):
            raise TimeoutError("per-host admission deadline exceeded")
    else:
        sem.acquire()
    try:
        yield
    finally:
        sem.release()


@contextmanager
def limited_urlopen(req: Request, timeout: int):
    url = getattr(req, "full_url", str(req))
    with host_slot(url):
        deadline = getattr(_PROBE_CONTEXT, "deadline", None)
        deadline = deadline or time.monotonic() + timeout
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("URL total budget exceeded")
        req._iptv_deadline = deadline
        timeout = min(timeout, remaining)
        with public_urlopen(req, timeout=timeout) as response:
            yield response


def read_bounded(response, max_bytes: int) -> bytes:
    read = getattr(response, "read1", response.read)
    chunks = []
    size = 0
    while size < max_bytes:
        deadline = getattr(_PROBE_CONTEXT, "deadline", None)
        if deadline and time.monotonic() >= deadline:
            raise TimeoutError("URL total budget exceeded while reading media")
        chunk = read(min(65536, max_bytes - size))
        if not chunk:
            break
        chunks.append(chunk)
        size += len(chunk)
    return b"".join(chunks)


def _bounded_gzip_decompress(data: bytes, max_bytes: int) -> bytes:
    """Strictly decompress one gzip member with an output-size ceiling."""
    decoder = zlib.decompressobj(16 + zlib.MAX_WBITS)
    output = decoder.decompress(data, max_bytes + 1)
    if len(output) > max_bytes or decoder.unconsumed_tail:
        raise ValueError("decompressed upstream playlist exceeded maximum fetch size")
    flushed = decoder.flush(max_bytes + 1 - len(output))
    output += flushed
    if len(output) > max_bytes:
        raise ValueError("decompressed upstream playlist exceeded maximum fetch size")
    if not decoder.eof:
        raise ValueError("truncated gzip upstream playlist")
    if decoder.unused_data:
        raise ValueError("unexpected trailing data after gzip upstream playlist")
    return output


def fetch_url(url: str, timeout: int = FETCH_TIMEOUT, max_bytes: int = MAX_SOURCE_BYTES, accept: str = "*/*") -> tuple[int, str, bytes, str, bool]:
    req = Request(url, headers={"User-Agent": UA, "Accept": accept, "Connection": "close", "Accept-Encoding": "gzip"})
    with limited_urlopen(req, timeout=timeout) as r:
        code = getattr(r, "status", 200)
        ctype = r.headers.get("Content-Type") or ""
        content_encoding = (r.headers.get("Content-Encoding") or "").lower()
        data = read_bounded(r, max_bytes + 1)
        final = r.geturl()
    truncated = len(data) > max_bytes
    if truncated:
        return code, ctype, data[:max_bytes], final, True
    is_gzip = (
        "gzip" in content_encoding
        or "gzip" in ctype.lower()
        or urlsplit(final).path.lower().endswith(".gz")
    )
    if is_gzip:
        data = _bounded_gzip_decompress(data, max_bytes)
    return code, ctype, data, final, False


def normalize_name(name: str) -> str:
    name = html.unescape(name or "").strip().strip('"').strip("'")
    name = re.sub(r"\s+", "", name)
    # TXT playlist uses comma as delimiter; keep channel names delimiter-safe.
    name = name.replace(",", "\uFF0C")
    if name.startswith("\u4e2d\u592e"):
        name = name.replace("\u4e2d\u592e", "CCTV", 1)
    return name[:80] or "\u672a\u547d\u540d\u9891\u9053"





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
    return parse_source_candidates(text, source, "m3u")

def parse_txt(text: str, source: str) -> list[Candidate]:
    return parse_source_candidates(text, source, "txt")


def parse_playlist(text: str, source: str) -> list[Candidate]:
    return parse_source_candidates(text, source)


def parse_source_candidates(text: str, source: str, format: str = "auto") -> list[Candidate]:
    return [Candidate(source, channel.group, normalize_name(channel.name), channel.url,
                      channel.tvg_id, channel.tvg_logo, channel.country, channel.language)
            for channel in parse_source_data(text, format)]


def eligible_candidates(candidates: list[Candidate], spec: SourceSpec) -> tuple[list[Candidate], dict[str, int]]:
    from curate_ku9 import prepare_curated_row
    from channel_scope import channel_countries

    eligible: list[Candidate] = []
    excluded: Counter = Counter()
    for candidate in candidates:
        reason = publication_issue(spec, candidate.url)
        if not reason:
            reason = domestic_chinese_issue(candidate.name, candidate.group, candidate.source,
                                            candidate.tvg_id, candidate.country, candidate.language)
            if reason in {"", "chinese_channel_identity_unconfirmed"}:
                candidate = replace(candidate, name=known_domestic_name(candidate.name, candidate.tvg_id, candidate.source))
                reason = domestic_chinese_issue(candidate.name, candidate.group, candidate.source,
                                                candidate.tvg_id, candidate.country, candidate.language)
        if not reason:
            countries = channel_countries(candidate.country, candidate.tvg_id)
            group = "\u6e2f\u6fb3\u53f0\u9891\u9053" if countries and countries.issubset({"hk", "mo", "tw"}) else candidate.group
            row, reason, _detail = prepare_curated_row(candidate.name, candidate.url, group, candidate.source)
            if row:
                group, name, url, source = row
                eligible.append(Candidate(source, group, name, url, candidate.tvg_id,
                                          candidate.tvg_logo, candidate.country, candidate.language))
                continue
        excluded[reason or "invalid_channel"] += 1
    return eligible, dict(excluded)


def fetch_source(spec: SourceSpec) -> tuple[SourceStatus, list[Candidate]]:
    name, url = spec.name, spec.url
    transport = "direct"
    try:
        try:
            payload = fetch_url(url, timeout=spec.timeout_seconds)
        except (TimeoutError, ConnectionError, URLError) as exc:
            fallback = github_content_url(url)
            if not fallback or isinstance(exc, HTTPError):
                raise
            payload = fetch_url(fallback, timeout=spec.timeout_seconds, accept="application/vnd.github.raw+json")
            transport = "github_public_contents_api"
        code, ctype, data, final, truncated = payload
        if not 200 <= code < 300:
            raise ValueError(f"upstream HTTP {code}")
        if truncated:
            raise ValueError("upstream playlist exceeded maximum fetch size; refusing partial parse")
        text = decode_bytes(data, ctype)
        if spec.format == "catalog":
            return SourceStatus(name, url, True, bytes=len(data), mode=spec.mode,
                                error="catalog only; child links not fetched or executed",
                                checked_at=datetime.now(timezone.utc).isoformat(),
                                discovered_links=discovery_links(text), transport=transport), []
        cands = parse_source_candidates(text, name, spec.format)
        if len(cands) > MAX_CANDIDATES_PER_SOURCE:
            raise ValueError(
                f"resource budget exceeded: source parsed {len(cands)} candidates "
                f"> limit {MAX_CANDIDATES_PER_SOURCE}"
            )
        eligible, excluded = eligible_candidates(cands, spec)
        warn = "" if cands else "WARN fetched but no parseable HTTP/HTTPS stream candidates"
        st = SourceStatus(
            name=name,
            url=url,
            ok=True,
            bytes=len(data),
            parsed=len(cands),
            truncated=False,
            error=warn,
            mode=spec.mode,
            contributed=bool(cands),
            checked_at=datetime.now(timezone.utc).isoformat(),
            eligible=len(eligible),
            excluded=excluded,
            transport=transport,
        )
        return st, eligible
    except Exception as e:
        message = str(e)
        return SourceStatus(
            name=name,
            url=url,
            ok=False,
            bytes=0,
            parsed=0,
            truncated="maximum fetch size" in message,
            error=redact_text(repr(e))[:240],
            mode=spec.mode,
            contributed=False,
            checked_at=datetime.now(timezone.utc).isoformat(),
        ), []


def github_content_url(url: str) -> str:
    parsed = urlsplit(url)
    if parsed.hostname != "raw.githubusercontent.com" or parsed.query:
        return ""
    parts = parsed.path.strip("/").split("/")
    if len(parts) < 4:
        return ""
    owner, repo, *rest = parts
    if rest[:2] == ["refs", "heads"]:
        rest = rest[2:]
    if len(rest) < 2:
        return ""
    ref, *path = rest
    return f"https://api.github.com/repos/{quote(owner, safe='')}/{quote(repo, safe='')}/contents/{quote(unquote('/'.join(path)), safe='/')}?ref={quote(unquote(ref), safe='')}"


def is_ipv6_url(url: str) -> bool:
    host = urlparse(url).hostname or ""
    try:
        return isinstance(ipaddress.ip_address(host), ipaddress.IPv6Address)
    except Exception:
        return ":" in host and not re.match(r"^\d+\.\d+\.\d+\.\d+$", host)


def http_get_small(url: str, max_bytes: int = 65536, timeout: int = TIMEOUT) -> tuple[int, str, bytes, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*", "Connection": "close"})
    with limited_urlopen(req, timeout=timeout) as r:
        code = getattr(r, "status", 200)
        ctype = (r.headers.get("Content-Type") or "").lower()
        data = read_bounded(r, max_bytes)
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
    if any(x in data[:256].lower() for x in BAD_HTML):
        return True
    # A valid HLS manifest can legitimately contain tokens such as "404",
    # "offline", or "nosignal" inside signed paths and channel identifiers.
    # Media validation of its advertised segments is the authoritative check.
    if "#extm3u" in sample:
        return False
    for marker in BAD_MARKERS:
        if re.search(rf"(?<![a-z0-9]){re.escape(marker)}(?![a-z0-9])", sample):
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


@dataclass
class HLSManifest:
    variants: list[str]
    segments: list[str]
    keys: list[str]
    maps: list[str]
    media_sequence: int | None
    target_duration: float | None
    endlist: bool
    encrypted: bool = False


def _quoted_uri(line: str) -> str:
    match = re.search(r'URI="([^"]+)"', line, re.I)
    return html.unescape(match.group(1).strip()) if match else ""


def parse_hls_manifest(text: str, base: str) -> HLSManifest:
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    variants: list[str] = []
    segments: list[str] = []
    keys: list[str] = []
    maps: list[str] = []
    media_sequence: int | None = None
    target_duration: float | None = None
    endlist = any(line.upper() == "#EXT-X-ENDLIST" for line in lines)
    encrypted = any(line.upper().startswith(("#EXT-X-KEY:", "#EXT-X-SESSION-KEY:"))
                    and "METHOD=NONE" not in line.upper() for line in lines)
    for i, line in enumerate(lines):
        upper = line.upper()
        if upper.startswith("#EXT-X-MEDIA-SEQUENCE:"):
            try:
                media_sequence = int(line.split(":", 1)[1].strip())
            except (ValueError, IndexError):
                pass
        elif upper.startswith("#EXT-X-TARGETDURATION:"):
            try:
                target_duration = float(line.split(":", 1)[1].strip())
            except (ValueError, IndexError):
                pass
        elif upper.startswith("#EXT-X-KEY:") and "METHOD=NONE" not in upper:
            uri = _quoted_uri(line)
            if uri:
                keys.append(urljoin(base, uri))
        elif upper.startswith("#EXT-X-MAP:"):
            uri = _quoted_uri(line)
            if uri:
                maps.append(urljoin(base, uri))
        elif upper.startswith("#EXT-X-STREAM-INF"):
            for nxt in lines[i + 1:]:
                if not nxt.startswith("#"):
                    variants.append(urljoin(base, nxt))
                    break
        elif upper.startswith("#EXTINF"):
            for nxt in lines[i + 1:]:
                if not nxt.startswith("#"):
                    segments.append(urljoin(base, nxt))
                    break
    if not segments:
        for line in lines:
            low = line.lower()
            if not line.startswith("#") and any(ext in low for ext in MEDIA_EXTS):
                segments.append(urljoin(base, line))
    return HLSManifest(
        unique_keep_order(variants),
        unique_keep_order(segments),
        unique_keep_order(keys),
        unique_keep_order(maps),
        media_sequence,
        target_duration,
        endlist,
        encrypted,
    )


def parse_m3u8_items(text: str, base: str) -> tuple[list[str], list[str]]:
    """Compatibility wrapper used by tests and older diagnostics."""
    manifest = parse_hls_manifest(text, base)
    return manifest.variants, manifest.segments


def looks_media(data: bytes, ctype: str, require_video: bool = False) -> bool:
    return probe_looks_media(data, ctype, require_video=require_video)


def media_detail(data: bytes, ctype: str) -> str:
    probe = probe_media(data, ctype)
    return f"{probe.kind}/{probe.container}: {probe.reason}"


def load_hls_initialization(manifest: HLSManifest, timeout: int, require_video: bool = False) -> tuple[bool, str, bytes]:
    if manifest.encrypted or manifest.keys:
        return False, "encrypted/DRM HLS excluded; no key or license requested", b""
    if len(manifest.maps) > 1:
        return False, "changing HLS initialization maps not supported", b""
    prefix = b""
    for map_url in manifest.maps:
        # The initialization segment contains the track table for CMAF/fMP4.
        # It is the authoritative place to reject audio-only HLS streams.
        code, ctype, data, _final = http_get_small(map_url, max_bytes=MAX_INIT_BYTES, timeout=timeout)
        if code >= 400 or not looks_media(data, ctype, require_video=require_video):
            return False, f"map bad {code} {ctype} bytes={len(data)} {media_detail(data, ctype)}", b""
        prefix = data
    return True, f"keys=0 maps={len(manifest.maps)}", prefix


def check_aux_resources(manifest: HLSManifest, timeout: int, require_video: bool = False) -> tuple[bool, str]:
    ok, detail, _prefix = load_hls_initialization(manifest, timeout, require_video)
    return ok, detail


def check_media_segments(segments: list[str], limit: int = HLS_SEGMENT_CHECKS, timeout: int = TIMEOUT, require_video: bool | None = None, init_data: bytes = b"") -> tuple[bool, str]:
    if not segments:
        return False, "no segment"
    if require_video is None:
        require_video = REQUIRE_VIDEO_TRACK
    checked = 0
    # Probe the newest advertised segments. The head of a long/event playlist
    # may be expired or cached and does not prove the current live edge works.
    # Strict final publication probes download a larger sample so PAT/PMT or
    # container track metadata is available, not just a TS sync byte.
    sample_bytes = 32768 if require_video else 4096
    for seg in segments[-max(1, limit):]:
        code, ctype, data, _final = http_get_small(seg, max_bytes=sample_bytes, timeout=timeout)
        checked += 1
        if code >= 400 or not data or looks_bad(data) or not looks_media(init_data + data, ctype, require_video=require_video):
            return False, f"segment bad {code} {ctype} bytes={len(data)} checked={checked} {media_detail(data, ctype)}"
    mode = "video" if require_video else "media"
    return True, f"segments ok checked={checked} required={mode}"


def decode_manifest_sample(manifest: HLSManifest, timeout: int, prefix: bytes = b"") -> DecodeResult:
    if manifest.encrypted or manifest.keys or not manifest.segments:
        return DecodeResult(False, 0, "missing or encrypted media for decode")
    if manifest.maps and not prefix:
        return DecodeResult(False, 0, "missing HLS initialization for decode")
    return decode_public_sample(manifest.segments[-1], timeout, prefix)


def decode_public_sample(url: str, timeout: int, prefix: bytes = b"") -> DecodeResult:
    for sample_size in (512 * 1024, MAX_SAMPLE_BYTES):
        code, _ctype, data, _final = http_get_small(url, max_bytes=sample_size, timeout=timeout)
        if code >= 400 or not data or looks_bad(data):
            return DecodeResult(False, 0, "invalid media sample for decode")
        result = decode_video(prefix + data, deadline=getattr(_PROBE_CONTEXT, "deadline", None))
        if result.ok or len(data) < sample_size:
            return result
    return result


def progress_wait_seconds(target_duration: float | None) -> float:
    """Wait long enough for one live segment without unbounded runner delay."""
    target = target_duration if target_duration and target_duration > 0 else 4.0
    return min(HLS_PROGRESS_MAX_WAIT, max(HLS_PROGRESS_MIN_WAIT, target * HLS_PROGRESS_TARGET_MULTIPLIER))


def check_hls_progress(playlist_url: str, initial: HLSManifest, timeout: int, require_video: bool | None = None, require_decode: bool = False) -> tuple[bool, str]:
    if require_video is None:
        require_video = REQUIRE_VIDEO_TRACK
    if initial.endlist:
        return False, "VOD/endlist manifest is not a live channel"
    if not initial.segments:
        return False, "no initial segment for progress check"
    wait_seconds = progress_wait_seconds(initial.target_duration)
    time.sleep(wait_seconds)
    code, ctype, data, final = http_get_small(playlist_url, timeout=timeout)
    if code >= 400 or looks_bad(data):
        return False, f"progress manifest bad {code}"
    later = parse_hls_manifest(data.decode("utf-8", "ignore"), final)
    if later.endlist:
        return False, "live manifest ended during progress check"
    sequence_advanced = (
        initial.media_sequence is not None
        and later.media_sequence is not None
        and later.media_sequence > initial.media_sequence
    )
    segment_advanced = bool(later.segments and later.segments[-1] != initial.segments[-1])
    if not (sequence_advanced or segment_advanced):
        return False, f"manifest did not advance after {wait_seconds:.1f}s"
    if not later.segments:
        return False, f"manifest advanced after {wait_seconds:.1f}s but has no media segment"
    # A changing manifest URL/sequence alone is not proof that the live edge is
    # usable. Probe the newly advertised edge segment again; this rejects stale
    # manifests that advance while their latest media objects are already 404,
    # empty, HTML error pages, or audio-only payloads.
    aux_ok, aux_detail, prefix = load_hls_initialization(later, timeout, require_video and not require_decode)
    if not aux_ok:
        return False, f"new edge initialization failed: {aux_detail}"
    edge_ok, edge_detail = check_media_segments(later.segments, limit=1, timeout=timeout, require_video=require_video and not require_decode, init_data=prefix)
    if not edge_ok:
        return False, f"manifest advanced after {wait_seconds:.1f}s; new edge failed: {edge_detail}"
    if require_decode:
        decoded = decode_manifest_sample(later, timeout, prefix)
        if not decoded.ok:
            return False, f"new live edge failed: {decoded.detail}"
    return True, f"manifest advanced after {wait_seconds:.1f}s; new edge ok"


def parse_next_from_m3u8(text: str, base: str) -> tuple[str | None, str | None]:
    manifest = parse_hls_manifest(text, base)
    if manifest.variants:
        return "playlist", manifest.variants[0]
    if manifest.segments:
        return "segment", manifest.segments[0]
    return None, None


def _check_media_manifest(cand: Candidate, playlist_url: str, text: str, final: str, timeout: int, segment_limit: int, require_progress: bool, require_video: bool, require_decode: bool = False) -> CheckResult:
    manifest = parse_hls_manifest(text, final)
    aux_ok, aux_detail, prefix = load_hls_initialization(manifest, timeout, require_video=require_video and not require_decode)
    if not aux_ok:
        return CheckResult(cand, False, aux_detail)
    if require_decode and (manifest.endlist or "#EXT-X-BYTERANGE:" in text.upper()):
        return CheckResult(cand, False, "VOD/endlist or unsupported byte-range media playlist")
    # Short TS samples can contain only audio before the first video packet.
    # Final checks prove video through decoding instead of this weaker heuristic.
    segments_ok, segment_detail = check_media_segments(manifest.segments, limit=segment_limit, timeout=timeout, require_video=require_video and not require_decode, init_data=prefix)
    if not segments_ok:
        return CheckResult(cand, False, segment_detail)
    decoded = decode_manifest_sample(manifest, timeout, prefix) if require_decode else DecodeResult(True, 0, "frame decode not requested")
    if not decoded.ok:
        return CheckResult(cand, False, f"{segment_detail}; {decoded.detail}", decoded_frames=decoded.frames)
    if require_progress:
        progress_ok, progress_detail = check_hls_progress(final, manifest, timeout, require_video=require_video, require_decode=require_decode)
        if not progress_ok:
            return CheckResult(cand, False, f"{segment_detail}; {decoded.detail}; {progress_detail}", decoded_frames=decoded.frames)
        return CheckResult(cand, True, f"{segment_detail}; {aux_detail}; {progress_detail}; {decoded.detail}", decoded_frames=decoded.frames)
    return CheckResult(cand, True, f"{segment_detail}; {aux_detail}; {decoded.detail}", decoded_frames=decoded.frames)


def check_candidate(cand: Candidate, timeout: int = TIMEOUT, core_override: bool | None = None, require_progress: bool = False, require_video: bool | None = None, require_decode: bool = False) -> CheckResult:
    start = time.monotonic()
    previous = getattr(_PROBE_CONTEXT, "deadline", None)
    _PROBE_CONTEXT.deadline = previous or start + URL_BUDGET
    try:
        result = _check_candidate(cand, timeout, core_override, require_progress, require_video, require_decode)
    finally:
        _PROBE_CONTEXT.deadline = previous
    result.elapsed_seconds = round(time.monotonic() - start, 3)
    result.checked_at = datetime.now(timezone.utc).isoformat()
    return result


def _check_candidate(cand: Candidate, timeout: int = TIMEOUT, core_override: bool | None = None, require_progress: bool = False, require_video: bool | None = None, require_decode: bool = False) -> CheckResult:
    url = cand.url.strip()
    issue = publishable_url_issue(url)
    if issue:
        return CheckResult(cand, False, f"invalid URL: {issue}")
    is_core = is_core_family_candidate(cand) if core_override is None else core_override
    if require_video is None:
        require_video = REQUIRE_VIDEO_TRACK
    segment_limit = CORE_HLS_SEGMENT_CHECKS if is_core else HLS_SEGMENT_CHECKS
    try:
        code, ctype, data, final = http_get_small(url, timeout=timeout)
        if code >= 400:
            return CheckResult(cand, False, f"http {code}")
        if looks_bad(data):
            return CheckResult(cand, False, "bad marker/html")
        text = data.decode("utf-8", "ignore")
        if "#EXTM3U" in text or "mpegurl" in ctype or url.lower().endswith((".m3u8", ".m3u")):
            manifest = parse_hls_manifest(text, final)
            if manifest.encrypted:
                return CheckResult(cand, False, "encrypted/DRM master playlist excluded")
            if manifest.variants:
                checked_variants = 0
                last_detail = ""
                for child in manifest.variants[:max(1, HLS_VARIANT_CHECKS)]:
                    checked_variants += 1
                    code2, ctype2, data2, final2 = http_get_small(child, timeout=timeout)
                    if code2 >= 400 or looks_bad(data2):
                        last_detail = f"child bad {code2}"
                        continue
                    result = _check_media_manifest(
                        cand,
                        child,
                        data2.decode("utf-8", "ignore"),
                        final2,
                        timeout,
                        segment_limit,
                        require_progress,
                        require_video,
                        require_decode,
                    )
                    last_detail = result.detail
                    if result.ok:
                        return replace(result, detail=f"variant ok variants_checked={checked_variants} {result.detail}")
                return CheckResult(cand, False, f"variant fail variants_checked={checked_variants} {last_detail}")
            return _check_media_manifest(cand, url, text, final, timeout, segment_limit, require_progress, require_video, require_decode)
        direct_probe = probe_media(data, ctype)
        if (require_progress or require_decode) and direct_probe.container in {"mp4/fmp4", "fmp4"}:
            return CheckResult(
                cand,
                False,
                "direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD",
            )
        decoded = DecodeResult(True, 0, "frame decode not requested")
        if require_decode and direct_probe.kind == "video":
            decoded = decode_public_sample(url, timeout)
        return CheckResult(
            cand,
            decoded.ok and (direct_probe.kind == "video" if require_video or require_decode else direct_probe.kind in {"video", "audio"}),
            f"direct {ctype} bytes={len(data)} {media_detail(data, ctype)} "
            f"required={'video' if require_video else 'media'} progress={'required' if require_progress else 'not-required'}; {decoded.detail}",
            decoded_frames=decoded.frames,
        )
    except Exception as exc:
        return CheckResult(cand, False, redact_text(repr(exc))[:160])


def check_candidate_resilient(cand: Candidate, core_override: bool | None = None, require_progress: bool = False, require_video: bool | None = None, require_decode: bool = False) -> CheckResult:
    start = time.monotonic()
    previous_deadline = getattr(_PROBE_CONTEXT, "deadline", None)
    _PROBE_CONTEXT.deadline = previous_deadline or start + URL_BUDGET
    try:
        result = _check_candidate_resilient(cand, core_override, require_progress, require_video, require_decode)
    except Exception as exc:
        result = CheckResult(cand, False, redact_text(repr(exc))[:240])
    finally:
        _PROBE_CONTEXT.deadline = previous_deadline
    result.elapsed_seconds = round(time.monotonic() - start, 3)
    result.checked_at = datetime.now(timezone.utc).isoformat()
    return result


def _check_candidate_resilient(cand: Candidate, core_override: bool | None = None, require_progress: bool = False, require_video: bool | None = None, require_decode: bool = False) -> CheckResult:
    """Check a URL, with a slow retry for core family channels on transient failures."""
    is_core = is_core_family_candidate(cand) if core_override is None else core_override
    first = check_candidate(cand, timeout=TIMEOUT, core_override=is_core, require_progress=require_progress, require_video=require_video, require_decode=require_decode)
    if first.ok or CORE_RETRY_ATTEMPTS <= 0:
        return first
    if not is_core or not looks_transient_failure(first.detail):
        return first
    last = first
    for attempt in range(1, CORE_RETRY_ATTEMPTS + 1):
        retry = check_candidate(
            cand,
            timeout=max(TIMEOUT, CORE_RETRY_TIMEOUT),
            core_override=is_core,
            require_progress=require_progress,
            require_video=require_video,
            require_decode=require_decode,
        )
        if retry.ok:
            return replace(retry, detail=f"core retry ok attempt={attempt} first={first.detail}; {retry.detail}")
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


def deduplicate_candidates(candidates: Iterable[Candidate]) -> dict[tuple[str, str], Candidate]:
    """Normalize and deterministically retain the best source per name+URL."""
    dedup: dict[tuple[str, str], Candidate] = {}
    for raw in candidates:
        name = normalize_name(raw.name)
        url = normalize_stream_url(raw.url)
        if not name or len(url) > 1000 or not is_publishable_http_url(url):
            continue
        candidate = Candidate(raw.source, raw.group or infer_group(name), name, url,
                              raw.tvg_id, raw.tvg_logo, raw.country, raw.language)
        key = (name, url)
        current = dedup.get(key)
        if current is None or prefer_score(candidate) < prefer_score(current):
            dedup[key] = candidate
    return dedup


def interleave_candidates_by_host(candidates: Iterable[Candidate]) -> list[Candidate]:
    """Round-robin initial hosts while preserving priority within each host.

    Host semaphores are acquired inside worker threads. Without host-fair
    submission, a priority-sorted burst from one host can occupy the whole
    executor with threads waiting on the same semaphore while unrelated hosts
    sit in the queue.
    """
    buckets: dict[str, deque[Candidate]] = {}
    for candidate in candidates:
        buckets.setdefault(stream_host_key(candidate.url), deque()).append(candidate)
    active = deque(buckets)
    ordered: list[Candidate] = []
    while active:
        host = active.popleft()
        bucket = buckets[host]
        ordered.append(bucket.popleft())
        if bucket:
            active.append(host)
    return ordered



def iter_bounded_check_results(candidates: list[Candidate], core_by_url: dict[str, bool]) -> Iterable[CheckResult]:
    """Probe all candidates with bounded futures and host-aware admission.

    The HTTP layer still enforces the per-host semaphore for redirects and HLS
    child resources. Admission control here prevents queued tasks for one slow
    host from occupying every executor thread while unrelated hosts wait.
    """
    buckets: dict[str, deque[Candidate]] = {}
    for candidate in candidates:
        buckets.setdefault(stream_host_key(candidate.url), deque()).append(candidate)
    ready_hosts = deque(buckets)
    ready_set = set(ready_hosts)
    inflight_by_host: dict[str, int] = {host: 0 for host in buckets}
    pending: dict[cf.Future[CheckResult], tuple[Candidate, str]] = {}

    def mark_ready(host: str) -> None:
        if buckets[host] and inflight_by_host[host] < HOST_WORKERS and host not in ready_set:
            ready_hosts.append(host)
            ready_set.add(host)

    def submit_ready(executor: cf.ThreadPoolExecutor) -> None:
        while ready_hosts and len(pending) < MAX_PENDING_FUTURES:
            host = ready_hosts.popleft()
            ready_set.remove(host)
            if not buckets[host] or inflight_by_host[host] >= HOST_WORKERS:
                continue
            cand = buckets[host].popleft()
            future = executor.submit(check_candidate_resilient, cand, core_by_url[cand.url], False)
            pending[future] = (cand, host)
            inflight_by_host[host] += 1
            mark_ready(host)

    with cf.ThreadPoolExecutor(max_workers=CHECK_WORKERS) as executor:
        submit_ready(executor)
        while pending:
            done, _ = cf.wait(pending, return_when=cf.FIRST_COMPLETED)
            for future in done:
                _candidate, host = pending.pop(future)
                inflight_by_host[host] -= 1
                mark_ready(host)
                yield future.result()
            submit_ready(executor)

def main() -> None:
    cleanup_transient_outputs()
    start = time.time()
    print(
        f"Fetching {len(PROBE_SPECS)} sources "
        f"(enabled={sum(1 for spec in SOURCE_SPECS if spec.enabled)}, "
        f"recovery={sum(1 for spec in SOURCE_SPECS if spec.auto_recover)}, "
        f"disabled={sum(1 for spec in SOURCE_SPECS if not spec.should_probe)})...",
        flush=True,
    )
    statuses: list[SourceStatus] = []
    all_cands: list[Candidate] = []

    def write_inventory() -> None:
        by_name = {status.name: status for status in statuses}
        inventory = {
            "schema_version": 1, "network_scope": NETWORK_SCOPE,
            "channel_scope": CHANNEL_SCOPE,
            "sources": [source_record(spec, asdict(by_name[spec.name]) if spec.name in by_name else
                                      {"status": "pending_fetch" if spec.should_probe else "disabled"})
                        for spec in SOURCE_SPECS],
        }
        path = ROOT / "source-inventory.json"
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(path)

    write_inventory()
    with cf.ThreadPoolExecutor(max_workers=min(MAX_WORKERS, len(PROBE_SPECS))) as ex:
        futs = [ex.submit(fetch_source, spec) for spec in PROBE_SPECS]
        for fut in cf.as_completed(futs):
            st, cands = fut.result()
            statuses.append(st)
            if st.contributed:
                all_cands.extend(cands)
            write_inventory()
            print(
                f"source {'OK' if st.ok else 'FAIL'} {st.name} mode={st.mode} "
                f"parsed={st.parsed} eligible={st.eligible} excluded={st.excluded or {}} bytes={st.bytes} {st.error}",
                flush=True,
            )

    statuses = order_source_statuses(statuses, PROBE_SOURCES)
    total_fetch_bytes = sum(status.bytes for status in statuses)
    budget_failures = [status for status in statuses if status.truncated or "resource budget exceeded" in status.error]
    if budget_failures:
        names = ", ".join(status.name for status in budget_failures)
        print(f"WARN rejected oversized upstream sources without blocking other sources: {names}", flush=True)
    if total_fetch_bytes > MAX_TOTAL_FETCH_BYTES:
        raise RuntimeError(
            f"total upstream fetch bytes {total_fetch_bytes} exceed budget {MAX_TOTAL_FETCH_BYTES}"
        )
    parsed_candidates = sum(status.parsed for status in statuses)
    if parsed_candidates > MAX_TOTAL_CANDIDATES:
        raise RuntimeError(
            f"parsed candidate count {parsed_candidates} exceeds budget {MAX_TOTAL_CANDIDATES}"
        )

    # Deduplicate before expensive checking.
    # Full-check rule: every distinct stream URL is probed against a real media
    # playlist/segment. The same URL can appear under multiple channel names in
    # upstream lists; checking it once and reusing the result is equivalent for
    # playback validity and avoids thousands of duplicate network probes.
    # Fetch completion order is nondeterministic. Deterministically retain the
    # configured best source so reports and downstream priority stay stable.
    dedup = deduplicate_candidates(all_cands)

    url_to_candidates: dict[str, list[Candidate]] = {}
    for c in dedup.values():
        url_to_candidates.setdefault(c.url, []).append(c)
    to_check: list[Candidate] = []
    core_by_url: dict[str, bool] = {}
    for url, arr in url_to_candidates.items():
        # Pick the best representative only for logging/source priority. Core
        # depth/retry is URL-level: if any alias is CCTV/satellite, a misleading
        # ordinary alias must not downgrade verification for the shared URL.
        to_check.append(sorted(arr, key=lambda c: (prefer_score(c), c.name))[0])
        core_by_url[url] = any(is_core_family_candidate(alias) for alias in arr)
    to_check.sort(key=lambda c: (prefer_score(c), c.name, c.url))
    to_check = interleave_candidates_by_host(to_check)
    if len(to_check) > MAX_UNIQUE_URLS:
        raise RuntimeError(
            f"unique stream URL count {len(to_check)} exceeds budget {MAX_UNIQUE_URLS}"
        )
    print(
        f"Parsed candidates={parsed_candidates}, eligible={len(all_cands)}, unique_name_url={len(dedup)}, "
        f"unique_urls={len(url_to_candidates)}, checking_all_unique_urls={len(to_check)}, "
        f"workers={CHECK_WORKERS}, per_host={HOST_WORKERS}, timeout={TIMEOUT}s",
        flush=True,
    )

    fingerprint = hashlib.sha256()
    for filename in ("config/sources.json", "config/rules.json", "config/quality.json", "scripts/verify_sources.py",
                     "scripts/media_probe.py", "scripts/url_utils.py", "scripts/network_safety.py", "scripts/channel_scope.py"):
        fingerprint.update((ROOT / filename).read_bytes())
    fingerprint.update(str((REQUIRE_VIDEO_TRACK, HLS_SEGMENT_CHECKS, CORE_HLS_SEGMENT_CHECKS, HLS_VARIANT_CHECKS)).encode())
    checkpoint = ScanCheckpoint(ROOT / ".maintenance-staging" / "scan-results.jsonl",
                                os.getenv("IPTV_SCAN_RUN_ID") or uuid.uuid4().hex, fingerprint.hexdigest())
    checked_by_url: dict[str, CheckResult] = {}
    for candidate in to_check:
        saved = checkpoint.get(candidate.url, core_by_url[candidate.url])
        if saved:
            checked_by_url[candidate.url] = CheckResult(candidate, True, saved["detail"], saved["elapsed_seconds"], saved["checked_at"])
    reused = len(checked_by_url)
    pending_candidates = [candidate for candidate in to_check if candidate.url not in checked_by_url]
    print(f"Current-run successful checkpoints reused={reused}; fresh probes={len(pending_candidates)}", flush=True)
    ok_count = reused
    for i, result in enumerate(iter_bounded_check_results(pending_candidates, core_by_url), reused + 1):
        checked_by_url[result.cand.url] = result
        checkpoint.record(result.cand.url, core_by_url[result.cand.url], result.ok, result.detail,
                          result.checked_at, result.elapsed_seconds)
        if result.ok:
            ok_count += 1
        if i % 100 == 0 or i == len(to_check):
            print(f"checked_url {i}/{len(to_check)}, ok_urls={ok_count}", flush=True)

    results: list[CheckResult] = []
    for url, arr in url_to_candidates.items():
        r = checked_by_url[url]
        for c in arr:
            results.append(CheckResult(c, r.ok, r.detail, r.elapsed_seconds, r.checked_at))

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
        "source_config_sha256": hashlib.sha256(SOURCE_CONFIG.read_bytes()).hexdigest(),
        "sources_configured_total": len(SOURCE_SPECS),
        "sources_enabled_total": sum(1 for spec in SOURCE_SPECS if spec.enabled),
        "sources_recovery_total": sum(1 for spec in SOURCE_SPECS if spec.auto_recover),
        "sources_disabled_total": sum(1 for spec in SOURCE_SPECS if not spec.should_probe),
        "sources_total": len(PROBE_SPECS),
        "sources_fetched_ok": sum(1 for s in statuses if s.ok),
        "sources_contributing": sum(1 for s in statuses if s.contributed),
        "sources_contributing_semantics": "legacy: fetched and parsed rows before permission/scope filtering; not media-eligible or finally published sources",
        "upstream_fetch_bytes": total_fetch_bytes,
        "resource_budgets": {
            "max_candidates_per_source": MAX_CANDIDATES_PER_SOURCE,
            "max_total_candidates": MAX_TOTAL_CANDIDATES,
            "max_unique_urls": MAX_UNIQUE_URLS,
            "max_source_bytes": MAX_SOURCE_BYTES,
            "max_total_fetch_bytes": MAX_TOTAL_FETCH_BYTES,
            "max_pending_futures": MAX_PENDING_FUTURES,
        },
        "probe_scheduling": {
            "strategy": "host_aware_bounded_futures",
            "initial_host_count": len({stream_host_key(candidate.url) for candidate in to_check}),
            "workers": CHECK_WORKERS,
            "workers_per_host": HOST_WORKERS,
        },
        "parsed_candidates": parsed_candidates,
        "eligible_candidates": len(all_cands),
        "policy_excluded_candidates": parsed_candidates - len(all_cands),
        "policy_exclusions": dict(sum((Counter(status.excluded or {}) for status in statuses), Counter())),
        "source_policy_version": SOURCE_POLICY_VERSION,
        "channel_policy_version": CHANNEL_POLICY_VERSION,
        "channel_scope": CHANNEL_SCOPE,
        "network_scope": NETWORK_SCOPE,
        "language_validation": "channel identity and upstream metadata; not speech recognition",
        "sources_media_eligible": sum(status.eligible > 0 for status in statuses),
        "same_run_successful_probes_reused": reused,
        "url_budget_seconds": URL_BUDGET,
        "unique_candidates": len(url_to_candidates),
        "unique_name_url_candidates": len(dedup),
        # The first pass checks every distinct URL for real media bytes. It
        # intentionally does not require a video track for every upstream
        # candidate because that would make the 29k-URL pass much slower and
        # would reject audio-only streams before curation. Keep the broad and
        # strict meanings separate so reports cannot overclaim what was proved.
        "checked_candidates": len(to_check),
        "broad_media_probe_checked": len(to_check),
        "broad_checked_all_unique": len(to_check) == len(url_to_candidates),
        "strict_video_checked_unique": 0,
        "strict_progress_checked_unique": 0,
        # Legacy field retained for consumers that only know the old schema;
        # it now explicitly aliases the broad first-pass claim.
        "checked_all_unique": len(to_check) == len(url_to_candidates),
        "first_pass_validation": {
            "require_video_track": REQUIRE_VIDEO_TRACK,
            "public_network_policy_enabled": True,
            "hls_segment_checks": HLS_SEGMENT_CHECKS,
            "core_hls_segment_checks": CORE_HLS_SEGMENT_CHECKS,
        },
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
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["name", "url", "mode", "contributed", "fetch_ok", "bytes", "parsed", "truncated", "error"])
        for st in statuses:
            w.writerow([st.name, st.url, st.mode, st.contributed, st.ok, st.bytes, st.parsed, st.truncated, st.error])

    with (ROOT / "stream_check_results.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["ok", "group", "name", "url", "source", "detail", "elapsed_seconds", "checked_at", "tvg_id", "tvg_logo", "country", "language"])
        for r in sorted(results, key=lambda x: (not x.ok, x.cand.group, x.cand.name)):
            w.writerow([r.ok, r.cand.group, r.cand.name, r.cand.url, r.cand.source, redact_text(r.detail),
                        r.elapsed_seconds, r.checked_at, r.cand.tvg_id, r.cand.tvg_logo, r.cand.country, r.cand.language])

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
        f"Sources configured: {len(SOURCE_SPECS)} (enabled={sum(1 for spec in SOURCE_SPECS if spec.enabled)}, recovery={sum(1 for spec in SOURCE_SPECS if spec.auto_recover)}, disabled={sum(1 for spec in SOURCE_SPECS if not spec.should_probe)})",
        f"Sources probed: {len(PROBE_SPECS)}",
        f"Sources fetched OK: {sum(1 for s in statuses if s.ok)}",
        f"Sources with parsed rows (before policy filters): {sum(1 for s in statuses if s.contributed)}",
        f"Sources with media-eligible candidates: {sum(status.eligible > 0 for status in statuses)}",
        f"Network scope: {NETWORK_SCOPE}; no region or home-broadband qualification",
        f"Channel scope: {CHANNEL_SCOPE}",
        f"Parsed candidates: {parsed_candidates}",
        f"Policy-excluded candidates (not media-checked): {parsed_candidates - len(all_cands)}",
        f"Eligible candidates before URL deduplication: {len(all_cands)}",
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
        "The legacy contributed CSV flag means parsed rows, not permission approval or final publication.",
        "",
        "| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for st in statuses:
        report.append(f"| {st.name} | {st.mode} | {'OK' if st.ok else 'FAIL'} | {'YES' if st.contributed else 'NO'} | {st.parsed} | {st.eligible} | {st.bytes} | {st.truncated} | {st.error.replace('|','/')} |")
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
