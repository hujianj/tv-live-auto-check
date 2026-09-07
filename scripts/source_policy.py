#!/usr/bin/env python3
"""Explicit source permissions and candidate-only discovery records."""
from __future__ import annotations

from dataclasses import asdict
import re
from urllib.parse import urlsplit

from source_config import SourceSpec
from url_utils import publishable_url_issue


POLICY_VERSION = 1


def publication_issue(spec: SourceSpec | None, url: str) -> str:
    issue = publishable_url_issue(url)
    if issue:
        return issue
    if spec is None or not spec.publish_allowed:
        return "source permission pending or restricted"
    return ""


def discovery_links(text: str) -> list[str]:
    """Record only static public playlist/config links, without fetching children."""
    out = set()
    for url in re.findall(r"https?://[^\s<>\"'`]+", text):
        url = url.rstrip("),;]")
        if publishable_url_issue(url):
            continue
        if urlsplit(url).path.lower().endswith((".txt", ".m3u", ".m3u8", ".json", ".xml")):
            out.add(url)
    return sorted(out)[:200]


def source_record(spec: SourceSpec, status: dict | None = None) -> dict:
    record = asdict(spec)
    record.update({"publication_allowed": spec.publish_allowed,
                   "network_scope": "current checking environment only",
                   "last_check": status or {"status": "not_checked"}})
    return record
