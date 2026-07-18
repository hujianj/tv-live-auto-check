#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Public-network URL policy used by all unattended IPTV HTTP probes.

Upstream playlists and redirect targets are untrusted input.  The verifier must
never follow a playlist URL or a stream URL into loopback, private, link-local,
reserved, multicast, or otherwise non-public address space.  DNS is resolved
before every initial request and redirect; the resolved result is cached only
for the lifetime of one process so a large run does not repeatedly resolve the
same CDN host.
"""
from __future__ import annotations

import ipaddress
import socket
import ssl
from functools import lru_cache
from urllib.parse import urljoin, urlsplit
from urllib.request import (
    HTTPRedirectHandler,
    HTTPSHandler,
    OpenerDirector,
    ProxyHandler,
    Request,
    build_opener,
)


class PublicURLPolicyError(ValueError):
    """Raised when a URL is not safe for an unattended public fetch."""


def _is_public_address(value: str) -> bool:
    try:
        address = ipaddress.ip_address(value)
    except ValueError:
        return False
    return address.is_global


def _normalise_host(host: str) -> str:
    return (host or "").strip().rstrip(".").lower()


@lru_cache(maxsize=8192)
def resolve_public_addresses(host: str, port: int) -> tuple[str, ...]:
    """Resolve *host* and reject a result containing any non-public address.

    Rejecting mixed public/private answers is deliberate: accepting the public
    subset would still permit DNS load-balancing or rebinding to route a later
    connection into a private network.  The cache is process-local and is not
    persisted between maintenance runs.
    """
    host = _normalise_host(host)
    if not host:
        raise PublicURLPolicyError("missing host")
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        literal = None
    if literal is not None:
        if not literal.is_global:
            raise PublicURLPolicyError(f"non-public IP address: {host}")
        return (str(literal),)

    try:
        infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    except OSError as exc:
        raise PublicURLPolicyError(f"DNS resolution failed for {host}: {exc}") from exc
    addresses: list[str] = []
    for _family, _socktype, _proto, _canonname, sockaddr in infos:
        address = str(sockaddr[0])
        if address not in addresses:
            addresses.append(address)
    if not addresses:
        raise PublicURLPolicyError(f"DNS returned no addresses for {host}")
    private = [address for address in addresses if not _is_public_address(address)]
    if private:
        raise PublicURLPolicyError(
            f"host resolves to non-public address(es): {host} -> {','.join(private)}"
        )
    return tuple(addresses)


def validate_public_url(url: str) -> str:
    """Validate an absolute HTTP(S) URL and its current DNS result."""
    if not isinstance(url, str) or not url:
        raise PublicURLPolicyError("empty URL")
    if any(ch.isspace() or ord(ch) < 32 or ord(ch) == 127 for ch in url):
        raise PublicURLPolicyError("whitespace/control character")
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError as exc:
        raise PublicURLPolicyError(f"URL parse error: {exc}") from exc
    if parsed.scheme.lower() not in {"http", "https"}:
        raise PublicURLPolicyError("unsupported scheme")
    if not parsed.hostname or not parsed.netloc:
        raise PublicURLPolicyError("missing host")
    if parsed.username is not None or parsed.password is not None:
        raise PublicURLPolicyError("userinfo is not allowed")
    host = _normalise_host(parsed.hostname)
    resolve_public_addresses(host, port or (443 if parsed.scheme.lower() == "https" else 80))
    return url


class PublicRedirectHandler(HTTPRedirectHandler):
    """Validate every HTTP redirect before urllib follows it."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[override]
        target = urljoin(req.full_url, newurl)
        validate_public_url(target)
        return super().redirect_request(req, fp, code, msg, headers, target)


def build_public_opener() -> OpenerDirector:
    """Build a redirect-validating opener without ambient proxy settings."""
    return build_opener(
        ProxyHandler({}),
        PublicRedirectHandler(),
        HTTPSHandler(context=ssl.create_default_context()),
    )


_PUBLIC_OPENER = build_public_opener()


def public_urlopen(request: Request, timeout: float):
    """Open a Request after validating the initial URL and all redirects."""
    validate_public_url(request.full_url)
    return _PUBLIC_OPENER.open(request, timeout=timeout)
