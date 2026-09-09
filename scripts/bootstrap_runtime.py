#!/usr/bin/env python3
"""Install and verify the decoder under one shared wall-clock budget."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def apt_official_source_options() -> list[str]:
    """Restrict apt to the runner's Ubuntu source when it is available.

    Hosted runner images may contain unrelated third-party repositories (for
    example the Chrome repository). A transient index mismatch in one of
    those repositories must not prevent installing the only system package
    this project needs. The option list is safe to pass to both ``update``
    and ``install``; older images without the deb822 source file use the
    traditional Ubuntu sources.list instead.
    """
    candidates = (
        Path("/etc/apt/sources.list.d/ubuntu.sources"),
        Path("/etc/apt/sources.list"),
    )
    for source in candidates:
        if source.is_file():
            return [
                "-o", f"Dir::Etc::sourcelist={source}",
                "-o", "Dir::Etc::sourceparts=-",
            ]
    # Keep compatibility with non-standard runner images. This is only used
    # when no canonical Ubuntu source file can be identified.
    return []


def bootstrap(root: Path = ROOT, budget: int = 360, *, runner=None, clock=None, which=None) -> dict:
    runner = runner or subprocess.run
    clock = clock or time.monotonic
    which = which or shutil.which
    start = clock()
    report = {
        "status": "running", "started_utc": datetime.now(timezone.utc).isoformat(),
        "budget_seconds": budget, "steps": [], "source_sha": os.getenv("GITHUB_SHA", ""),
    }
    steps = []
    if sys.platform.startswith("linux") and not which("ffmpeg"):
        apt = ["sudo", "apt-get", "-o", "Acquire::Retries=1", "-o", "Acquire::http::Timeout=20",
               "-o", "Acquire::https::Timeout=20", *apt_official_source_options()]
        steps.extend([
            ("apt update", [*apt, "update"]),
            ("install ffmpeg", [*apt, "install", "-y", "--no-install-recommends", "ffmpeg"]),
        ])
    steps.extend([
        ("python dependencies", [sys.executable, "-m", "pip", "install", "--disable-pip-version-check",
                                 "--no-input", "--retries", "1", "--timeout", "20", "-r", str(root / "requirements.txt")]),
        ("decoder preflight", [sys.executable, str(root / "scripts" / "media_decode.py")]),
    ])
    try:
        for label, command in steps:
            remaining = budget - (clock() - start)
            item = {"name": label, "status": "running", "remaining_seconds": round(max(0, remaining), 1)}
            report["steps"].append(item)
            print(f"Bootstrap: {label}; total budget remaining={remaining:.1f}s", flush=True)
            if remaining <= 0:
                raise TimeoutError("shared dependency installation budget exhausted")
            # GNU timeout terminates the process group, including apt/pip children.
            if sys.platform.startswith("linux"):
                command = ["timeout", "--signal=TERM", "--kill-after=10s", f"{remaining:.3f}s", *command]
            runner(command, cwd=root, check=True, timeout=remaining + 15)
            item["status"] = "ok"
        report["status"] = "ok"
    except (OSError, subprocess.SubprocessError, TimeoutError) as exc:
        report["status"] = "failed"
        item["status"] = "failed"
        # Do not include pip arguments/environment in persistent error output.
        report["error"] = type(exc).__name__
        report["failed_step"] = item["name"]
        print(f"Bootstrap failed: {item['name']} ({type(exc).__name__})", flush=True)
    report["elapsed_seconds"] = round(clock() - start, 3)
    (root / "bootstrap-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=int, default=360)
    args = parser.parse_args()
    if not 30 <= args.budget <= 600:
        parser.error("budget must be between 30 and 600 seconds")
    return 0 if bootstrap(budget=args.budget)["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
