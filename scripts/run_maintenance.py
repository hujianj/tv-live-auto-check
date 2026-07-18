#!/usr/bin/env python3
"""Run the complete maintenance pipeline locally with reliable fail-fast semantics.

PowerShell does not treat a non-zero exit code from an external program as an
exception merely because ``$ErrorActionPreference = 'Stop'``.  This wrapper
mirrors the GitHub Actions order and stops immediately when any stage fails, so
a rejected guard cannot be mistaken for a successful local publication.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]

STEPS: tuple[tuple[str, str], ...] = (
    ("unit tests", "test_playlist_logic.py"),
    ("verify every upstream URL", "verify_sources.py"),
    ("curate playlist", "curate_ku9.py"),
    ("recheck every published URL", "recheck_published.py"),
    ("audit core coverage", "audit_coverage.py"),
    ("audit playlist quality", "audit_quality.py"),
    ("validate complete publish bundle", "validate_publish_bundle.py"),
    ("guard against unsafe shrinkage", "guard_publish.py"),
    ("audit publish size", "audit_publish_size.py"),
)

ENV_DEFAULTS = {
    "IPTV_CHECK_WORKERS": "192",
    "IPTV_CHECK_WORKERS_PER_HOST": "8",
    "IPTV_CHECK_TIMEOUT": "6",
    "IPTV_FETCH_WORKERS": "64",
    "IPTV_FETCH_TIMEOUT": "20",
    "IPTV_HLS_VARIANT_CHECKS": "2",
    "IPTV_HLS_SEGMENT_CHECKS": "2",
    "IPTV_CORE_HLS_SEGMENT_CHECKS": "3",
    "IPTV_CORE_RETRY_ATTEMPTS": "1",
    "IPTV_CORE_RETRY_TIMEOUT": "14",
    "IPTV_HLS_PROGRESS_MIN_WAIT": "3",
    "IPTV_HLS_PROGRESS_MAX_WAIT": "14",
    "IPTV_PUBLISHED_RECHECK_WORKERS": "64",
    "IPTV_PUBLISHED_REFILL_WORKERS": "24",
    "IPTV_PUBLISHED_REQUIRE_CORE_PROGRESS": "1",
}


STEP_ENV_OVERRIDES = {
    # Mirror update.yml exactly: the broad first pass accepts proven audio/video
    # media, while every URL that reaches the published list must prove video.
    "verify_sources.py": {"IPTV_REQUIRE_VIDEO_TRACK": "0"},
    "recheck_published.py": {"IPTV_REQUIRE_VIDEO_TRACK": "1"},
}


def pipeline_commands() -> list[tuple[str, list[str]]]:
    return [
        (label, [sys.executable, str(ROOT / "scripts" / script)])
        for label, script in STEPS
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the exact ordered stages without executing network checks",
    )
    args = parser.parse_args(argv)

    commands = pipeline_commands()
    if args.dry_run:
        for index, (label, command) in enumerate(commands, 1):
            print(f"{index:02d}. {label}: {' '.join(command)}")
        return 0

    env = os.environ.copy()
    for key, value in ENV_DEFAULTS.items():
        env.setdefault(key, value)

    started = time.monotonic()
    for index, (label, command) in enumerate(commands, 1):
        stage_started = time.monotonic()
        print(f"\n[{index}/{len(commands)}] {label}", flush=True)
        stage_env = env.copy()
        stage_env.update(STEP_ENV_OVERRIDES.get(Path(command[-1]).name, {}))
        completed = subprocess.run(command, cwd=ROOT, env=stage_env, check=False)
        elapsed = time.monotonic() - stage_started
        if completed.returncode != 0:
            print(
                f"PIPELINE FAILED at stage {index} ({label}); "
                f"exit={completed.returncode}; elapsed={elapsed:.1f}s",
                file=sys.stderr,
                flush=True,
            )
            return completed.returncode or 1
        print(f"Stage OK: {label} ({elapsed:.1f}s)", flush=True)

    print(f"\nPIPELINE OK in {time.monotonic() - started:.1f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
