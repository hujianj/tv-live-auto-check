#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validated source lifecycle configuration shared by fetch and publication checks."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import urlparse

from url_utils import publishable_url_issue

ROOT = Path(__file__).resolve().parents[1]
SOURCE_CONFIG = ROOT / "config" / "sources.json"
SOURCE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,79}$")


@dataclass(frozen=True)
class SourceSpec:
    name: str
    url: str
    enabled: bool
    auto_recover: bool = False
    note: str = ""
    format: str = "auto"
    timeout_seconds: int = 20
    update_method: str = "scheduled_fetch"
    rights_status: str = "pending"
    license: str = "unknown"
    terms_url: str = ""
    homepage: str = ""
    reviewed_at: str = ""
    permission_scope: str = "unconfirmed"
    publication_urls: tuple[str, ...] = ()
    review_record: str = ""

    @property
    def publish_allowed(self) -> bool:
        # User-requested selections do not claim an upstream/content license.
        # They require exact reviewed URLs, enforced again by source_policy.
        allowed = self.rights_status == "approved" or (
            self.rights_status == "user_requested" and bool(self.publication_urls)
        )
        return self.should_probe and allowed and self.format != "catalog"

    @property
    def mode(self) -> str:
        if self.enabled:
            return "enabled"
        if self.auto_recover:
            return "recovery"
        return "disabled"

    @property
    def should_probe(self) -> bool:
        return self.enabled or self.auto_recover


def load_source_specs(path: Path = SOURCE_CONFIG) -> list[SourceSpec]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        raise ValueError(f"cannot read source config {path}: {exc}") from exc
    if not isinstance(raw, list) or not raw:
        raise ValueError("source config must be a non-empty list")

    specs: list[SourceSpec] = []
    seen_names: set[str] = set()
    seen_urls: set[str] = set()
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError(f"source config entries must be objects: {item!r}")
        name = str(item.get("name") or "").strip()
        url = str(item.get("url") or "").strip()
        if not SOURCE_NAME.fullmatch(name):
            raise ValueError(f"invalid source name: {name!r}")
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"source {name!r} must use an absolute HTTP(S) URL")
        if name in seen_names:
            raise ValueError(f"duplicate source name: {name}")
        if url in seen_urls:
            raise ValueError(f"duplicate source URL: {url}")
        seen_names.add(name)
        seen_urls.add(url)
        enabled = item.get("enabled", True)
        auto_recover = item.get("auto_recover", False)
        if type(enabled) is not bool or type(auto_recover) is not bool:
            raise ValueError(f"source {name!r} enabled/auto_recover must be boolean")
        if enabled and auto_recover:
            raise ValueError(f"source {name!r} cannot be both enabled and auto_recover")
        format = item.get("format", "auto")
        if format not in {"auto", "m3u", "m3u8", "txt", "json", "xml", "catalog"}:
            raise ValueError(f"source {name!r} has unsupported format")
        timeout = item.get("timeout_seconds", 20)
        if type(timeout) is not int or not 1 <= timeout <= 60:
            raise ValueError(f"source {name!r} timeout_seconds must be 1..60")
        rights = item.get("rights_status", "pending")
        if rights not in {"pending", "approved", "restricted", "user_requested"}:
            raise ValueError(f"source {name!r} rights_status is invalid")
        if rights == "approved":
            terms = item.get("terms_url")
            reviewed = item.get("reviewed_at")
            scope = item.get("permission_scope")
            if not all(isinstance(value, str) and value.strip() for value in (terms, reviewed, scope)):
                raise ValueError(f"source {name!r} approval requires dated permission evidence")
            evidence_url = urlparse(terms)
            if evidence_url.scheme not in {"http", "https"} or not evidence_url.hostname or evidence_url.username or evidence_url.password:
                raise ValueError(f"source {name!r} terms_url must be an HTTP(S) evidence URL without credentials")
            try:
                date.fromisoformat(reviewed)
            except ValueError as exc:
                raise ValueError(f"source {name!r} reviewed_at must be an ISO calendar date") from exc
        publication_urls = item.get("publication_urls", [])
        if (not isinstance(publication_urls, list) or len(publication_urls) > 200
                or any(not isinstance(value, str) for value in publication_urls)
                or len(set(publication_urls)) != len(publication_urls)):
            raise ValueError(f"source {name!r} publication_urls must be at most 200 unique URL strings")
        for value in publication_urls:
            if publishable_url_issue(value) or urlparse(value).query:
                raise ValueError(f"source {name!r} publication_urls must be credential-free exact URLs without query parameters")
        review_record = item.get("review_record", "")
        if not isinstance(review_record, str):
            raise ValueError(f"source {name!r} review_record must be a string")
        if rights == "user_requested":
            # This is an explicit repository-owner decision, not fabricated
            # third-party permission. No wildcard, URL rewriting or parameter
            # removal is permitted; new URLs need a separate review.
            if not publication_urls or format not in {"auto", "m3u", "txt"}:
                raise ValueError(f"source {name!r} user_requested requires exact URLs and a data-only playlist adapter")
            if not isinstance(item.get("permission_scope"), str) or not item["permission_scope"].strip():
                raise ValueError(f"source {name!r} user_requested requires a documented scope")
            try:
                date.fromisoformat(item.get("reviewed_at", ""))
            except (TypeError, ValueError) as exc:
                raise ValueError(f"source {name!r} user_requested requires an ISO review date") from exc
            record_path = (path.resolve().parent.parent / review_record).resolve()
            docs_root = (path.resolve().parent.parent / "docs").resolve()
            if (not review_record or Path(review_record).is_absolute()
                    or not record_path.is_relative_to(docs_root)
                    or record_path.suffix != ".md" or not record_path.is_file()):
                raise ValueError(f"source {name!r} user_requested requires an existing repository docs review record")
        specs.append(SourceSpec(name, url, enabled, auto_recover, str(item.get("note") or "").strip(),
                                format, timeout, str(item.get("update_method", "scheduled_fetch")), rights,
                                str(item.get("license", "unknown")), str(item.get("terms_url", "")),
                                str(item.get("homepage", url)), str(item.get("reviewed_at", "")),
                                str(item.get("permission_scope", "unconfirmed")),
                                tuple(publication_urls), review_record))

    if not any(spec.enabled for spec in specs):
        raise ValueError("source config must contain at least one enabled source")
    return specs


def probe_source_specs(path: Path = SOURCE_CONFIG) -> list[SourceSpec]:
    return [spec for spec in load_source_specs(path) if spec.should_probe]


def configured_source_pairs(path: Path = SOURCE_CONFIG, *, probe: bool = False) -> list[tuple[str, str]]:
    specs = probe_source_specs(path) if probe else load_source_specs(path)
    return [(spec.name, spec.url) for spec in specs if probe or spec.enabled]
