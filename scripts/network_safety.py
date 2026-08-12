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
from http.client import HTTPConnection, HTTPException, HTTPSConnection
import socket
import ssl
import threading
from functools import lru_cache
from urllib.parse import urljoin, urlsplit
from urllib.request import (
    HTTPHandler,
    HTTPRedirectHandler,
    HTTPSHandler,
    OpenerDirector,
    ProxyHandler,
    Request,
    build_opener,
)
from urllib.error import URLError


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


def _connect_exact_address(
    address: str,
    port: int,
    timeout: float | object,
    source_address: tuple[str, int] | None = None,
) -> socket.socket:
    """Open a socket to one already validated IP literal without DNS."""
    literal = ipaddress.ip_address(address)
    if not literal.is_global:
        raise PublicURLPolicyError(f"refusing non-public pinned address: {address}")
    family = socket.AF_INET6 if literal.version == 6 else socket.AF_INET
    target = (address, port, 0, 0) if family == socket.AF_INET6 else (address, port)
    sock = socket.socket(family, socket.SOCK_STREAM)
    try:
        if timeout is not socket._GLOBAL_DEFAULT_TIMEOUT:
            sock.settimeout(timeout)  # type: ignore[arg-type]
        if source_address:
            sock.bind(source_address)
        sock.connect(target)
        return sock
    except Exception:
        sock.close()
        raise


_LAST_GOOD_ADDRESS: dict[tuple[str, int], str] = {}
_BAD_ADDRESSES: dict[tuple[str, int], set[str]] = {}
_LAST_GOOD_ADDRESS_LOCK = threading.Lock()
MAX_ADDRESS_ATTEMPTS = 3
MAX_READ_RETRIES = 1


def _ordered_public_addresses(host: str, port: int) -> tuple[str, ...]:
    addresses = resolve_public_addresses(host, port)
    key = (_normalise_host(host), port)
    with _LAST_GOOD_ADDRESS_LOCK:
        preferred = _LAST_GOOD_ADDRESS.get(key)
        bad = set(_BAD_ADDRESSES.get(key, set()))
    healthy = tuple(address for address in addresses if address not in bad)
    degraded = tuple(address for address in addresses if address in bad)
    ordered = (*healthy, *degraded)
    if preferred in healthy:
        return (preferred, *(address for address in ordered if address != preferred))
    return ordered


def _remember_good_address(host: str, port: int, address: str) -> None:
    key = (_normalise_host(host), port)
    with _LAST_GOOD_ADDRESS_LOCK:
        _LAST_GOOD_ADDRESS[key] = address
        if key in _BAD_ADDRESSES:
            _BAD_ADDRESSES[key].discard(address)
            if not _BAD_ADDRESSES[key]:
                del _BAD_ADDRESSES[key]


def _remember_bad_address(host: str, port: int, address: str) -> None:
    key = (_normalise_host(host), port)
    with _LAST_GOOD_ADDRESS_LOCK:
        if _LAST_GOOD_ADDRESS.get(key) == address:
            del _LAST_GOOD_ADDRESS[key]
        _BAD_ADDRESSES.setdefault(key, set()).add(address)


class PublicHTTPConnection(HTTPConnection):
    """HTTP connection pinned to a policy-validated public IP."""

    def __init__(self, *args, pinned_address: str | None = None, **kwargs):
        self._pinned_address = pinned_address
        super().__init__(*args, **kwargs)

    def connect(self) -> None:
        if self._tunnel_host:
            raise PublicURLPolicyError("HTTP CONNECT tunnels are not allowed")
        address = self._pinned_address or _ordered_public_addresses(self.host, self.port)[0]
        self.sock = _connect_exact_address(
            address,
            self.port,
            self.timeout,
            self.source_address,
        )


class PublicHTTPSConnection(HTTPSConnection):
    """HTTPS connection pinned to a public IP while retaining hostname SNI."""

    def __init__(self, *args, pinned_address: str | None = None, **kwargs):
        self._pinned_address = pinned_address
        super().__init__(*args, **kwargs)

    def connect(self) -> None:
        if self._tunnel_host:
            raise PublicURLPolicyError("HTTP CONNECT tunnels are not allowed")
        server_hostname = _normalise_host(self.host)
        address = self._pinned_address or _ordered_public_addresses(server_hostname, self.port)[0]
        raw_socket = _connect_exact_address(
            address,
            self.port,
            self.timeout,
            self.source_address,
        )
        try:
            self.sock = self._context.wrap_socket(raw_socket, server_hostname=server_hostname)
        except Exception:
            raw_socket.close()
            raise


class _PublicAddressRetryHandler:
    """Retry idempotent requests across a bounded set of validated edge IPs."""

    def _open_pinned(self, connection_class, req, **connection_kwargs):
        parsed = urlsplit(req.full_url)
        host = _normalise_host(parsed.hostname or "")
        port = parsed.port or (443 if parsed.scheme.lower() == "https" else 80)
        addresses = _ordered_public_addresses(host, port)
        if req.get_method().upper() not in {"GET", "HEAD"}:
            addresses = addresses[:1]
        else:
            addresses = addresses[:MAX_ADDRESS_ATTEMPTS]
        last_error: BaseException | None = None
        for address in addresses:
            def connection_factory(target_host, **kwargs):
                return connection_class(
                    target_host,
                    pinned_address=address,
                    **kwargs,
                )

            try:
                response = self.do_open(connection_factory, req, **connection_kwargs)
            except (URLError, OSError, HTTPException) as exc:
                last_error = exc
                _remember_bad_address(host, port, address)
                continue
            try:
                response._public_host = host
                response._public_port = port
                response._public_pinned_address = address
            except AttributeError:
                # urllib returns a mutable HTTPResponse; keep the handler
                # friendly to lightweight test/dry-run response objects.
                pass
            _remember_good_address(host, port, address)
            return response
        if last_error is not None:
            raise last_error
        raise PublicURLPolicyError(f"DNS returned no usable public address for {host}")


class PublicHTTPHandler(_PublicAddressRetryHandler, HTTPHandler):
    def http_open(self, req):  # type: ignore[override]
        return self._open_pinned(PublicHTTPConnection, req)


class PublicHTTPSHandler(_PublicAddressRetryHandler, HTTPSHandler):
    def https_open(self, req):  # type: ignore[override]
        return self._open_pinned(
            PublicHTTPSConnection,
            req,
            context=self._context,
        )


def build_public_opener() -> OpenerDirector:
    """Build a redirect-validating, DNS-pinned opener without proxies."""
    return build_opener(
        ProxyHandler({}),
        PublicRedirectHandler(),
        PublicHTTPHandler(),
        PublicHTTPSHandler(context=ssl.create_default_context()),
    )


_PUBLIC_OPENER = build_public_opener()


class _RetryingPublicResponse:
    """Retry one failed idempotent body read on another validated edge IP."""

    def __init__(self, response, request: Request, timeout: float):
        self._response = response
        self._request = request
        self._timeout = timeout
        self._remaining_retries = MAX_READ_RETRIES

    def __getattr__(self, name):
        return getattr(self._response, name)

    def read(self, *args, **kwargs):
        while True:
            try:
                return self._response.read(*args, **kwargs)
            except (URLError, OSError, HTTPException):
                if self._remaining_retries <= 0:
                    raise
                self._remaining_retries -= 1
                host = getattr(self._response, "_public_host", "")
                port = int(getattr(self._response, "_public_port", 0) or 0)
                address = getattr(self._response, "_public_pinned_address", "")
                if host and port and address:
                    _remember_bad_address(host, port, address)
                self._response.close()
                self._response = _PUBLIC_OPENER.open(self._request, timeout=self._timeout)

    def close(self) -> None:
        self._response.close()

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.close()
        return False


def public_urlopen(request: Request, timeout: float):
    """Open a Request after validating the initial URL and all redirects."""
    validate_public_url(request.full_url)
    response = _PUBLIC_OPENER.open(request, timeout=timeout)
    if request.get_method().upper() in {"GET", "HEAD"} and MAX_READ_RETRIES > 0:
        return _RetryingPublicResponse(response, request, timeout)
    return response
