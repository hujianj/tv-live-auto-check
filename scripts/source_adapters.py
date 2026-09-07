#!/usr/bin/env python3
"""Bounded, data-only adapters. Never execute TVBox spiders or resolve VOD APIs."""
from __future__ import annotations

from dataclasses import dataclass
import html
import json
import re
from xml.etree import ElementTree

from url_utils import is_publishable_http_url, normalize_stream_url, split_stream_urls


@dataclass(frozen=True)
class Channel:
    name: str
    url: str
    group: str = ""
    tvg_id: str = ""
    tvg_logo: str = ""
    country: str = ""
    language: str = ""


def split_extinf(line: str) -> tuple[str, str]:
    quote = ""
    escaped = False
    for index, char in enumerate(line):
        if escaped:
            escaped = False
        elif char == "\\" and quote:
            escaped = True
        elif quote and char == quote:
            quote = ""
        elif not quote and char in "\"'":
            quote = char
        elif not quote and char == ",":
            return line[:index], line[index + 1:].strip()
    return line, ""


def attributes(text: str) -> dict[str, str]:
    return {key.lower(): html.unescape(value) for key, _quote, value in re.findall(r"([\w-]+)\s*=\s*([\"'])(.*?)\2", text)}


def _channels(name: object, urls: object, group: object = "", tvg_id: object = "", logo: object = "", country: object = "", language: object = "") -> list[Channel]:
    if not isinstance(name, str) or not name.strip():
        return []
    if isinstance(urls, str):
        urls = split_stream_urls(urls)
    if not isinstance(urls, list):
        return []
    out = []
    safe_logo = str(logo or "")
    if safe_logo and not is_publishable_http_url(safe_logo):
        safe_logo = ""
    country = ";".join(str(item) for item in country) if isinstance(country, list) else str(country or "")
    language = ";".join(str(item) for item in language) if isinstance(language, list) else str(language or "")
    for value in urls:
        if not isinstance(value, str):
            continue
        for raw_url in split_stream_urls(value):
            url = normalize_stream_url(raw_url)
            if is_publishable_http_url(url):
                out.append(Channel(name.strip(), url, str(group or ""), str(tvg_id or ""), safe_logo, country, language))
    return out


def parse_m3u(text: str) -> list[Channel]:
    # A media/master HLS manifest is one stream, never a list of TV channels.
    if re.search(r"^#EXT-X-(?:TARGETDURATION|STREAM-INF|MEDIA-SEQUENCE):", text, re.M | re.I):
        return []
    out: list[Channel] = []
    pending: tuple[str, dict[str, str]] | None = None
    blocked = False
    for raw in text.splitlines():
        line = raw.strip().lstrip("\ufeff")
        if line.startswith("#EXTINF:"):
            head, name = split_extinf(line)
            attrs = attributes(head)
            pending = (attrs.get("tvg-name") or attrs.get("title") or name, attrs)
            blocked = False
        elif line.startswith(("#KODIPROP:", "#EXTVLCOPT:")):
            # Entries requiring caller-supplied cookies, tokens or DRM are not portable public streams.
            if re.search(r"license|drm|cookie|authorization|referer|user-agent", line, re.I):
                blocked = True
        elif line and not line.startswith("#"):
            if pending and not blocked:
                name, attrs = pending
                out.extend(_channels(name, line, attrs.get("group-title"), attrs.get("tvg-id"), attrs.get("tvg-logo"), attrs.get("tvg-country"), attrs.get("tvg-language")))
            pending = None
    return out


def parse_txt(text: str) -> list[Channel]:
    group = ""
    out = []
    for raw in text.splitlines():
        line = raw.strip().lstrip("\ufeff")
        if not line or line.startswith("#"):
            continue
        if line.endswith(",#genre#"):
            group = line.split(",", 1)[0].strip()
            continue
        fields = line.split(",", 1) if "," in line else line.split(None, 1)
        if len(fields) == 2:
            out.extend(_channels(fields[0], fields[1], group))
    return out


def parse_json(text: str) -> list[Channel]:
    root = json.loads(text)
    pending = [(root, "", 0)]
    out = []
    visited = 0
    while pending:
        item, group, depth = pending.pop()
        visited += 1
        if depth > 20 or visited > 100000:
            raise ValueError("JSON playlist structure exceeds budget")
        if isinstance(item, list):
            pending.extend((child, group, depth + 1) for child in reversed(item))
        elif isinstance(item, dict):
            name = item.get("name") or item.get("title") or item.get("channel_name")
            urls = item.get("urls") or item.get("url") or item.get("stream_url") or item.get("play_url")
            category = item.get("group-title") or item.get("group") or item.get("category") or group
            if any(key.lower() in {"headers", "cookie", "drm", "license_key", "authorization", "spider"} for key in item):
                continue
            out.extend(_channels(name, urls, category, item.get("tvg-id") or item.get("tvg_id"), item.get("tvg-logo") or item.get("logo"), item.get("country"), item.get("language")))
            for key in ("channels", "groups", "items", "data", "lives"):
                if key in item:
                    pending.append((item[key], category or name or "", depth + 1))
    return out


def parse_xml(text: str) -> list[Channel]:
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)", text, re.I):
        raise ValueError("XML DTD/entities are not permitted")
    root = ElementTree.fromstring(text)
    if any(element.tag.rsplit("}", 1)[-1].lower() in {"headers", "cookie", "drm", "authorization", "license_key"} for element in root.iter()):
        raise ValueError("XML playlist requires credentials or DRM")
    out = []
    for index, item in enumerate(root.iter()):
        if index > 100000:
            raise ValueError("XML playlist structure exceeds budget")
        tag = item.tag.rsplit("}", 1)[-1].lower()
        if tag not in {"channel", "item"}:
            continue
        fields = {child.tag.rsplit("}", 1)[-1].lower(): child.text for child in item}
        out.extend(_channels(item.get("name") or fields.get("name") or fields.get("title"),
                             item.get("url") or fields.get("url") or fields.get("stream"),
                             item.get("group") or fields.get("group"), item.get("tvg-id"),
                             item.get("logo") or fields.get("logo"),
                             item.get("country") or fields.get("country"),
                             item.get("language") or fields.get("language")))
    return out


def parse(text: str, format: str = "auto") -> list[Channel]:
    start = text.lstrip("\ufeff \r\n\t")
    if re.match(r"(?is)<(?:!doctype\s+html|html|head|body)\b", start):
        raise ValueError("upstream returned HTML, not a playlist")
    if format == "auto":
        format = "m3u" if start.startswith("#EXTM3U") or "#EXTINF:" in start[:5000] else (
            "json" if start.startswith(("{", "[")) else "xml" if start.startswith("<") else "txt")
    adapters = {"m3u": parse_m3u, "m3u8": parse_m3u, "txt": parse_txt, "json": parse_json, "xml": parse_xml}
    if format not in adapters:
        raise ValueError(f"unsupported playlist format: {format}")
    return adapters[format](text)
