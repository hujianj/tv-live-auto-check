"""Decode bounded, already-downloaded media without granting FFmpeg network access."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import os
from pathlib import Path
import re
import shutil
import subprocess
import threading
import time

MIN_DECODED_FRAMES = 3
MAX_SAMPLE_BYTES = 4 * 1024 * 1024
MAX_INIT_BYTES = 256 * 1024
DECODE_TIMEOUT = 12.0
DECODE_WORKERS = max(1, min(8, int(os.getenv("IPTV_DECODE_WORKERS", "4"))))
_SLOTS = threading.BoundedSemaphore(DECODE_WORKERS)
_FRAME = re.compile(rb"^0,\s*-?\d+,\s*-?\d+,\s*\d+,\s*[1-9]\d*,\s*[a-f0-9]{32}$")


@dataclass(frozen=True)
class DecodeResult:
    ok: bool
    frames: int
    detail: str


@lru_cache(maxsize=1)
def decoder_executable() -> str:
    configured = os.getenv("IPTV_FFMPEG_EXE", "").strip()
    if configured:
        executable = configured
    else:
        try:
            import imageio_ffmpeg
            executable = imageio_ffmpeg.get_ffmpeg_exe()
        except (ImportError, RuntimeError):
            executable = shutil.which("ffmpeg") or ""
    if not executable or not Path(executable).is_file():
        raise RuntimeError("FFmpeg unavailable; install requirements.txt before maintenance")
    return str(Path(executable).resolve())


def decoder_preflight() -> str:
    process = subprocess.run(
        [decoder_executable(), "-version"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        timeout=5, check=True, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    return process.stdout.decode("utf-8", "replace").splitlines()[0]


def decode_video(data: bytes, *, deadline: float | None = None) -> DecodeResult:
    if not data or len(data) > MAX_SAMPLE_BYTES + MAX_INIT_BYTES:
        return DecodeResult(False, 0, "decode sample empty or exceeds byte limit")
    deadline = deadline if deadline is not None else time.monotonic() + DECODE_TIMEOUT
    remaining = deadline - time.monotonic()
    if remaining <= 0 or not _SLOTS.acquire(timeout=max(0, remaining)):
        return DecodeResult(False, 0, "decode queue exceeded URL budget")
    try:
        remaining = min(DECODE_TIMEOUT, deadline - time.monotonic())
        if remaining <= 0:
            return DecodeResult(False, 0, "decode exceeded URL budget")
        # Only pipe transport and known media demuxers are allowed. An upstream
        # playlist, nested URL or file reference cannot make the decoder fetch it.
        command = [
            decoder_executable(), "-hide_banner", "-loglevel", "error", "-nostdin",
            "-max_alloc", "67108864", "-protocol_whitelist", "pipe",
            "-format_whitelist", "mpegts,mov,flv", "-probesize", str(MAX_SAMPLE_BYTES),
            "-analyzeduration", "3000000", "-threads", "1", "-i", "pipe:0",
            "-map", "0:v:0", "-an", "-sn", "-dn", "-frames:v", str(MIN_DECODED_FRAMES),
            "-vf", "scale=64:36", "-threads", "1", "-filter_threads", "1",
            "-f", "framemd5", "pipe:1",
        ]
        process = subprocess.run(
            command, input=data, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            timeout=remaining, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        frames = sum(bool(_FRAME.fullmatch(line.strip())) for line in process.stdout.splitlines())
        ok = process.returncode == 0 and frames >= MIN_DECODED_FRAMES
        return DecodeResult(ok, frames, f"frame decode {'ok' if ok else 'failed'} frames={frames} exit={process.returncode}")
    except subprocess.TimeoutExpired:
        return DecodeResult(False, 0, "frame decode timed out")
    except (OSError, RuntimeError):
        return DecodeResult(False, 0, "frame decoder unavailable or failed to start")
    finally:
        _SLOTS.release()


if __name__ == "__main__":
    print(decoder_preflight())
