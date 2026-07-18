#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared IPTV URL parsing and publication validation.

Upstream playlists frequently concatenate backup URLs or append a second
protocol after ``#``. Keeping the parsing rules in one module prevents the
fetcher, curator, and final validator from disagreeing about what can be
published to a TV player.
"""
from __future__ import annotations

import html
import re
from urllib.parse import urlsplit


STREAM_SCHEME_RE = r"(?:https?|rtmp)://"
CONCATENATED_STREAM_RE = re.compile(rf"[;#,](?={STREAM_SCHEME_RE})", re.I)
ANY_STREAM_SCHEME_RE = re.compile(STREAM_SCHEME_RE, re.I)


def split_stream_urls(value: str) -> list[str]:
    """Split a messy upstream field into independent stream URLs.

    Delimiters are recognized only when immediately followed by another
    supported stream scheme, so semicolons inside ordinary query strings are
    preserved. Each result is still validated separately before publication.
    """
    raw = html.unescape(value or "").strip().strip('"').strip("'").lstrip("\ufeff")
    if not raw:
        return []
    out: list[str] = []
    seen: set[str] = set()
    for piece in CONCATENATED_STREAM_RE.split(raw):
        clean = piece.strip().strip('"').strip("'").lstrip("\ufeff").rstrip(",").strip()
        # An empty URL fragment (a trailing '#') is never sent to the server
        # and is a common upstream separator artifact. Remove it before the
        # strict publication validator rejects fragments in TV-facing output.
        clean = clean.rstrip("#").rstrip()
        if not clean or clean in seen:
            continue
        seen.add(clean)
        out.append(clean)
    return out


def normalize_stream_url(value: str) -> str:
    """Compatibility helper returning the first split URL, if any."""
    parts = split_stream_urls(value)
    return parts[0] if parts else ""


def publishable_url_issue(url: str) -> str:
    """Return an empty string for a TV-safe HTTP(S) URL, otherwise a reason."""
    if not url:
        return "empty"
    if url != url.strip():
        return "leading/trailing whitespace"
    if "\ufffd" in url:
        return "replacement character"
    if any(ch.isspace() or ord(ch) < 32 or ord(ch) == 127 for ch in url):
        return "whitespace/control character"
    if url.endswith(","):
        return "trailing comma"
    if CONCATENATED_STREAM_RE.search(url):
        return "concatenated stream URLs"
    if len(ANY_STREAM_SCHEME_RE.findall(url)) != 1:
        return "multiple or missing stream schemes"
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError:
        return "URL parse error"
    if parsed.scheme.lower() not in {"http", "https"}:
        return "unsupported scheme"
    if not parsed.netloc or not parsed.hostname:
        return "missing host"
    if parsed.username is not None or parsed.password is not None:
        return "userinfo is not publishable"
    if port == 0:
        return "invalid port"
    if "%" in parsed.hostname:
        return "IPv6 zone identifiers are not publishable"
    # Fragments are never sent to the HTTP server. In IPTV source lists they
    # almost always indicate a trailing separator or a concatenated backup
    # protocol (for example ``#rtmp://...``), both of which break TV players.
    if parsed.fragment:
        return "fragment is not publishable"
    if url.endswith("#"):
        return "trailing fragment marker"
    if "\\" in url:
        return "backslash in URL"
    return ""


def is_publishable_http_url(url: str) -> bool:
    return not publishable_url_issue(url)
