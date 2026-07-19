#!/usr/bin/env python3
"""Run the complete IPTV maintenance pipeline with bounded full-run retries.

This module is the single orchestration entry point used both locally and by
GitHub Actions.  It records every stage in ``maintenance-run.json`` and retries
the *entire* verification pipeline once when a network-dependent stage fails.
Configuration, tests, and final publication-contract failures are fatal and are
never hidden by retries.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "maintenance.json"
REPORT_PATH = ROOT / "maintenance-run.json"


@dataclass(frozen=True)
class Stage:
    label: str
    script: str
    args: tuple[str, ...] = ()


STAGES: tuple[Stage, ...] = (
    Stage("validate publication configuration", "publication_config.py", ("--validate",)),
    Stage("unit tests", "test_playlist_logic.py"),
    Stage("verify every upstream URL", "verify_sources.py"),
    Stage("curate playlist", "curate_ku9.py"),
    Stage("recheck every published URL", "recheck_published.py"),
    Stage("audit core coverage", "audit_coverage.py"),
    Stage("audit playlist quality", "audit_quality.py"),
    Stage("guard against unsafe shrinkage", "guard_publish.py"),
    Stage("audit publish size and generate manifest", "audit_publish_size.py"),
    Stage("validate complete publish bundle", "validate_publish_bundle.py", ("--strict",)),
    Stage("validate immutable public publication", "validate_publication.py"),
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
    "IPTV_PUBLISHED_FINAL_RETRY_WORKERS": "16",
    "IPTV_PUBLISHED_FINAL_RETRY_TIMEOUT": "14",
    "IPTV_PUBLISHED_FINAL_RETRY_ATTEMPTS": "1",
    "IPTV_PUBLISHED_REQUIRE_CORE_PROGRESS": "1",
}

STEP_ENV_OVERRIDES = {
    "verify_sources.py": {"IPTV_REQUIRE_VIDEO_TRACK": "0"},
    "recheck_published.py": {"IPTV_REQUIRE_VIDEO_TRACK": "1"},
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _positive_int(value: object, field: str) -> int:
    if type(value) is not int or value < 1:
        raise ValueError(f"{field} must be a positive integer")
    return value


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if data.get("schema_version") != 1:
        raise ValueError("maintenance config schema_version must be 1")
    data["max_attempts"] = _positive_int(data.get("max_attempts"), "max_attempts")
    data["retry_delay_seconds"] = _positive_int(data.get("retry_delay_seconds"), "retry_delay_seconds")
    known_scripts = {stage.script for stage in STAGES}
    retryable = data.get("retryable_scripts")
    fatal = data.get("fatal_scripts")
    if not isinstance(retryable, list) or not retryable or not all(isinstance(x, str) for x in retryable):
        raise ValueError("retryable_scripts must be a non-empty string list")
    if not isinstance(fatal, list) or not fatal or not all(isinstance(x, str) for x in fatal):
        raise ValueError("fatal_scripts must be a non-empty string list")
    retryable_set, fatal_set = set(retryable), set(fatal)
    if retryable_set & fatal_set:
        raise ValueError("maintenance scripts cannot be both retryable and fatal")
    if retryable_set | fatal_set != known_scripts:
        missing = sorted(known_scripts - (retryable_set | fatal_set))
        extra = sorted((retryable_set | fatal_set) - known_scripts)
        raise ValueError(f"maintenance stage classification mismatch: missing={missing} extra={extra}")
    for key in (
        "max_candidates_per_source",
        "max_total_candidates",
        "max_unique_urls",
        "max_source_bytes",
        "max_total_fetch_bytes",
        "max_pending_futures",
    ):
        data[key] = _positive_int(data.get(key), key)
    return data


# Compatibility/readability view used by tests and documentation.
STEPS: tuple[tuple[str, str], ...] = tuple((stage.label, stage.script) for stage in STAGES)


def stage_command(stage: Stage) -> list[str]:
    return [sys.executable, str(ROOT / "scripts" / stage.script), *stage.args]


def pipeline_commands() -> list[tuple[str, list[str]]]:
    return [(stage.label, stage_command(stage)) for stage in STAGES]


def append_step_summary(text: str) -> None:
    target = os.getenv("GITHUB_STEP_SUMMARY")
    if not target:
        return
    try:
        with Path(target).open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(text.rstrip() + "\n")
    except Exception as exc:
        print(f"MAINTENANCE WARN: cannot write GITHUB_STEP_SUMMARY: {exc!r}")


def write_report(report: dict[str, Any]) -> None:
    REPORT_PATH.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def run_attempt(attempt: int, total: int, env: dict[str, str], config: dict[str, Any]) -> dict[str, Any]:
    attempt_started = time.monotonic()
    record: dict[str, Any] = {
        "attempt": attempt,
        "started_utc": utc_now(),
        "status": "running",
        "stages": [],
    }
    for index, stage in enumerate(STAGES, 1):
        command = stage_command(stage)
        stage_started = time.monotonic()
        print(f"\n[attempt {attempt}/{total} stage {index}/{len(STAGES)}] {stage.label}", flush=True)
        stage_env = env.copy()
        stage_env.update(STEP_ENV_OVERRIDES.get(stage.script, {}))
        completed = subprocess.run(command, cwd=ROOT, env=stage_env, check=False)
        elapsed = round(time.monotonic() - stage_started, 3)
        classification = "ok" if completed.returncode == 0 else (
            "retryable" if stage.script in set(config["retryable_scripts"]) else "fatal"
        )
        stage_record = {
            "index": index,
            "label": stage.label,
            "script": stage.script,
            "args": list(stage.args),
            "returncode": completed.returncode,
            "elapsed_seconds": elapsed,
            "classification": classification,
        }
        record["stages"].append(stage_record)
        if completed.returncode != 0:
            record.update(
                {
                    "status": "failed",
                    "failure_classification": classification,
                    "failed_stage": stage_record,
                    "finished_utc": utc_now(),
                    "elapsed_seconds": round(time.monotonic() - attempt_started, 3),
                }
            )
            print(
                f"MAINTENANCE ATTEMPT FAILED: stage={stage.label} exit={completed.returncode} "
                f"classification={classification} elapsed={elapsed:.1f}s",
                file=sys.stderr,
                flush=True,
            )
            return record
        print(f"Stage OK: {stage.label} ({elapsed:.1f}s)", flush=True)
    record.update(
        {
            "status": "ok",
            "failure_classification": "none",
            "finished_utc": utc_now(),
            "elapsed_seconds": round(time.monotonic() - attempt_started, 3),
        }
    )
    return record


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="print the exact ordered stages")
    parser.add_argument("--max-attempts", type=int, default=0, help="override config; 0 uses config")
    parser.add_argument("--retry-delay", type=int, default=-1, help="override seconds; -1 uses config")
    args = parser.parse_args(argv)

    config = load_config()
    max_attempts = args.max_attempts or int(config["max_attempts"])
    retry_delay = int(config["retry_delay_seconds"]) if args.retry_delay < 0 else args.retry_delay
    if max_attempts < 1 or retry_delay < 0:
        raise SystemExit("max attempts must be >=1 and retry delay must be >=0")

    if args.dry_run:
        print(f"max_attempts={max_attempts} retry_delay_seconds={retry_delay}")
        for index, stage in enumerate(STAGES, 1):
            classification = "retryable" if stage.script in set(config["retryable_scripts"]) else "fatal"
            print(f"{index:02d}. [{classification}] {stage.label}: {' '.join(stage_command(stage))}")
        return 0

    env = os.environ.copy()
    for key, value in ENV_DEFAULTS.items():
        env.setdefault(key, value)
    # Pass resource budgets to the first-pass verifier. Environment overrides
    # remain possible for controlled local experiments, but the repository
    # configuration is the production default.
    env.setdefault("IPTV_MAX_CANDIDATES_PER_SOURCE", str(config["max_candidates_per_source"]))
    env.setdefault("IPTV_MAX_TOTAL_CANDIDATES", str(config["max_total_candidates"]))
    env.setdefault("IPTV_MAX_UNIQUE_URLS", str(config["max_unique_urls"]))
    env.setdefault("IPTV_MAX_SOURCE_BYTES", str(config["max_source_bytes"]))
    env.setdefault("IPTV_MAX_TOTAL_FETCH_BYTES", str(config["max_total_fetch_bytes"]))
    env.setdefault("IPTV_MAX_PENDING_FUTURES", str(config["max_pending_futures"]))

    report: dict[str, Any] = {
        "schema_version": 1,
        "started_utc": utc_now(),
        "status": "running",
        "max_attempts": max_attempts,
        "retry_delay_seconds": retry_delay,
        "attempts": [],
    }
    write_report(report)
    started = time.monotonic()

    for attempt in range(1, max_attempts + 1):
        attempt_record = run_attempt(attempt, max_attempts, env, config)
        report["attempts"].append(attempt_record)
        if attempt_record["status"] == "ok":
            report.update(
                {
                    "status": "ok",
                    "successful_attempt": attempt,
                    "finished_utc": utc_now(),
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                }
            )
            write_report(report)
            append_step_summary(
                f"## Maintenance pipeline\n\nStatus: **OK**  \n"
                f"Successful attempt: {attempt}/{max_attempts}  \n"
                f"Elapsed: {report['elapsed_seconds']}s\n"
            )
            print(f"\nMAINTENANCE PIPELINE OK on attempt {attempt}/{max_attempts}")
            return 0

        write_report(report)
        classification = str(attempt_record.get("failure_classification"))
        if classification != "retryable" or attempt >= max_attempts:
            break
        print(f"Retryable full-pipeline failure; waiting {retry_delay}s before complete retry.", flush=True)
        if retry_delay:
            time.sleep(retry_delay)

    last = report["attempts"][-1]
    report.update(
        {
            "status": "failed",
            "failure_classification": last.get("failure_classification", "fatal"),
            "failed_stage": last.get("failed_stage"),
            "finished_utc": utc_now(),
            "elapsed_seconds": round(time.monotonic() - started, 3),
        }
    )
    write_report(report)
    append_step_summary(
        f"## Maintenance pipeline\n\nStatus: **FAILED**  \n"
        f"Attempts: {len(report['attempts'])}/{max_attempts}  \n"
        f"Classification: {report['failure_classification']}  \n"
        f"Failed stage: {(report.get('failed_stage') or {}).get('label', 'unknown')}\n"
    )
    return int((last.get("failed_stage") or {}).get("returncode") or 1)


if __name__ == "__main__":
    raise SystemExit(main())
