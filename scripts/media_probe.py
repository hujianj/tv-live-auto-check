#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small dependency-free media-track probes for IPTV validation.

This is intentionally a conservative probe, not a full demuxer.  It identifies
video tracks in the container bytes that a live HLS/TCP probe already downloads:
MPEG-TS PAT/PMT, fMP4/MP4 initialization metadata, and FLV video tags.  An
unknown payload is not treated as video when strict publication verification is
enabled; this prevents AAC/MP3-only streams and HTML/error payloads from being
published as television channels.
"""
from __future__ import annotations

from dataclasses import dataclass


VIDEO_STREAM_TYPES = {
    0x01,  # MPEG-1 video
    0x02,  # MPEG-2 video
    0x10,  # MPEG-4 visual
    0x1B,  # H.264/AVC
    0x20,  # MVC
    0x24,  # H.265/HEVC
    0x42,  # AVS/AVS+
    0xD1,  # AVS2 in common Chinese IPTV lists
    0xD2,  # AVS3 in some private encoders
}
AUDIO_STREAM_TYPES = {
    0x03, 0x04, 0x0F, 0x11, 0x81, 0x87, 0x8A,
}
VIDEO_SAMPLE_ENTRIES = (b"avc1", b"avc3", b"hev1", b"hvc1", b"av01", b"vp09", b"mp4v")


@dataclass(frozen=True)
class MediaProbe:
    kind: str  # video, audio, unknown
    container: str
    reason: str


def _iter_ts_packets(data: bytes):
    """Yield (payload_unit_start, pid, payload) for aligned MPEG-TS packets."""
    if len(data) < 188 * 2:
        return
    start = -1
    for candidate in range(min(188, len(data))):
        if data[candidate] != 0x47:
            continue
        if candidate + 188 < len(data) and data[candidate + 188] != 0x47:
            continue
        start = candidate
        break
    if start < 0:
        return
    pos = start
    while pos + 188 <= len(data) and data[pos] == 0x47:
        packet = data[pos:pos + 188]
        pusi = bool(packet[1] & 0x40)
        pid = ((packet[1] & 0x1F) << 8) | packet[2]
        adaptation_control = (packet[3] >> 4) & 0x03
        payload_offset = 4
        if adaptation_control in (2, 3):
            adaptation_length = packet[4]
            payload_offset = 5 + adaptation_length
        if adaptation_control in (1, 3) and payload_offset <= 188:
            yield pusi, pid, packet[payload_offset:]
        pos += 188


def _section_assembler():
    buffers: dict[int, bytearray] = {}

    def feed(pid: int, payload: bytes, pusi: bool) -> list[bytes]:
        if not payload:
            return []
        buf = buffers.setdefault(pid, bytearray())
        if pusi:
            pointer = payload[0]
            payload = payload[1:]
            if pointer > len(payload):
                buffers[pid] = bytearray()
                buf = buffers[pid]
                return []
            # Bytes before the pointer finish a section started in the previous
            # packet; bytes after it start one or more new sections.
            if pointer and buf:
                buf.extend(payload[:pointer])
            payload = payload[pointer:]
        buf.extend(payload)
        sections: list[bytes] = []
        while len(buf) >= 3:
            if buf[0] == 0xFF:
                buf.clear()
                break
            section_length = ((buf[1] & 0x0F) << 8) | buf[2]
            total = 3 + section_length
            if total < 8 or total > 4096:
                buf.clear()
                break
            if len(buf) < total:
                break
            sections.append(bytes(buf[:total]))
            del buf[:total]
        return sections

    return feed


def _parse_pat(section: bytes) -> set[int]:
    if len(section) < 12 or section[0] != 0x00:
        return set()
    end = len(section) - 4
    out: set[int] = set()
    pos = 8
    while pos + 4 <= end:
        program = (section[pos] << 8) | section[pos + 1]
        pid = ((section[pos + 2] & 0x1F) << 8) | section[pos + 3]
        if program:
            out.add(pid)
        pos += 4
    return out


def _parse_pmt(section: bytes) -> tuple[bool, bool]:
    if len(section) < 16 or section[0] != 0x02:
        return False, False
    program_info_length = ((section[10] & 0x0F) << 8) | section[11]
    pos = 12 + program_info_length
    end = len(section) - 4
    has_video = False
    has_audio = False
    while pos + 5 <= end:
        stream_type = section[pos]
        es_info_length = ((section[pos + 3] & 0x0F) << 8) | section[pos + 4]
        if stream_type in VIDEO_STREAM_TYPES:
            has_video = True
        if stream_type in AUDIO_STREAM_TYPES:
            has_audio = True
        pos += 5 + es_info_length
    return has_video, has_audio


def probe_mpeg_ts(data: bytes) -> MediaProbe | None:
    if len(data) < 188 * 2:
        return None
    feed = _section_assembler()
    pmt_pids: set[int] = set()
    has_video = False
    has_audio = False
    saw_packet = False
    for pusi, pid, payload in _iter_ts_packets(data):
        saw_packet = True
        for section in feed(pid, payload, pusi):
            if pid == 0:
                pmt_pids.update(_parse_pat(section))
            elif pid in pmt_pids:
                video, audio = _parse_pmt(section)
                has_video = has_video or video
                has_audio = has_audio or audio
    if not saw_packet:
        return None
    if has_video:
        return MediaProbe("video", "mpeg-ts", "PAT/PMT advertises video elementary stream")
    if has_audio:
        return MediaProbe("audio", "mpeg-ts", "PAT/PMT advertises audio but no video")
    return MediaProbe("unknown", "mpeg-ts", "TS packets found but PAT/PMT video track not observed")


def probe_flv(data: bytes) -> MediaProbe | None:
    if not data.startswith(b"FLV") or len(data) < 13:
        return None
    # Header is 9 bytes, then PreviousTagSize0. Each tag header is 11 bytes;
    # inspect available tags without requiring the whole stream.
    pos = 9
    if pos + 4 > len(data):
        return MediaProbe("unknown", "flv", "truncated FLV header")
    pos += 4
    has_audio = False
    while pos + 11 <= len(data):
        tag_type = data[pos] & 0x1F
        size = int.from_bytes(data[pos + 1:pos + 4], "big")
        if tag_type == 9:
            return MediaProbe("video", "flv", "FLV video tag observed")
        if tag_type == 8:
            has_audio = True
        pos += 11 + size + 4
    if has_audio:
        return MediaProbe("audio", "flv", "FLV audio tags observed but no video tag")
    return MediaProbe("unknown", "flv", "FLV header found but no media tag observed")


def probe_mp4(data: bytes) -> MediaProbe | None:
    if len(data) < 8 or b"ftyp" not in data[:96] and b"moov" not in data[:4096]:
        return None
    if any(entry in data[:256 * 1024] for entry in VIDEO_SAMPLE_ENTRIES) or b"vide" in data[:256 * 1024]:
        return MediaProbe("video", "mp4/fmp4", "MP4 video handler/sample entry observed")
    if b"soun" in data[:256 * 1024] or any(entry in data[:256 * 1024] for entry in (b"mp4a", b"ac-3", b"ec-3", b"Opus")):
        return MediaProbe("audio", "mp4/fmp4", "MP4 audio handler/sample entry observed")
    return MediaProbe("unknown", "mp4/fmp4", "MP4 container found but no track type observed")


def probe_media(data: bytes, content_type: str = "") -> MediaProbe:
    if not data:
        return MediaProbe("unknown", "", "empty payload")
    lower = data[:4096].lower()
    if any(marker in lower for marker in (b"<html", b"<!doctype html", b"<head", b"<body")):
        return MediaProbe("unknown", "html", "HTML/error payload")
    for probe in (probe_mpeg_ts(data), probe_flv(data), probe_mp4(data)):
        if probe is not None:
            return probe
    ctype = (content_type or "").lower()
    if data.startswith(b"ID3") or (len(data) >= 2 and data[0] == 0xFF and data[1] & 0xF0 == 0xF0):
        return MediaProbe("audio", "mpeg-audio", "MPEG audio frame observed")
    if "audio/" in ctype or any(token in ctype for token in ("aac", "mpeg", "mp3")):
        return MediaProbe("audio", "audio", "audio content type")
    if data[:4] == b"moof":
        return MediaProbe("unknown", "fmp4", "fragmented MP4 media without initialization track")
    if data[:4] in (b"RIFF", b"OggS") or data[:3] == b"FLAC":
        return MediaProbe("audio", "audio", "audio container signature")
    return MediaProbe("unknown", "", "no proven media container/track")


def looks_media(data: bytes, content_type: str = "", require_video: bool = False) -> bool:
    probe = probe_media(data, content_type)
    return probe.kind == "video" if require_video else probe.kind in {"video", "audio"}
