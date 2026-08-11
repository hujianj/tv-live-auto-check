#!/usr/bin/env python3
"""Run the complete IPTV maintenance pipeline with bounded stage retries.

This module is the single orchestration entry point used both locally and by
GitHub Actions. It records every stage in ``maintenance-run.json`` and resumes
at the failed network stage when a bounded retry is warranted. Deterministic
curation, audit, guard, and publication-contract failures are fatal and are
never hidden by an expensive full-pipeline retry.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from typing import Any

from maintenance_contract import GUARD_REJECTED_EXIT_CODE

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "maintenance.json"
REPORT_PATH = ROOT / "maintenance-run.json"

STALE_RUN_OUTPUTS: tuple[str, ...] = (
    "live-curated.txt",
    "live.txt",
    "live-verified.txt",
    "ku9-live.txt",
    "live.m3u",
    "ku9-family.txt",
    "live-family.txt",
    "family.m3u",
    "stream_check_results.csv",
    "live-all-playable.txt",
    "all-playable.m3u",
    "curated-source-map.csv",
    "curated-candidate-pool.csv",
    "alias-conflict-report.md",
    "published_recheck_results.csv",
    "source-report.md",
    "check-report.md",
    "curated-report.md",
    "published-recheck-report.md",
    "final-publish-report.md",
    "stability-report.md",
    "coverage-report.md",
    "quality-audit-report.md",
    "publish-guard-report.md",
    "publish-size-report.md",
    "publish-manifest.json",
    "full-check-summary.json",
    "sources_status.csv",
)


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
    "IPTV_PUBLISHED_REQUIRE_BROADCAST_PROGRESS": "1",
}

STEP_ENV_OVERRIDES = {
    "verify_sources.py": {"IPTV_REQUIRE_VIDEO_TRACK": "0"},
    "recheck_published.py": {"IPTV_REQUIRE_VIDEO_TRACK": "1"},
}

PROFILE_ENV = "IPTV_MAINTENANCE_PROFILE"
PIPELINE_DEADLINE_ENV = "IPTV_MAINTENANCE_DEADLINE_MONOTONIC"


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
    data["guard_confirmation_attempts"] = _positive_int(
        data.get("guard_confirmation_attempts", 1), "guard_confirmation_attempts"
    )
    confirmation_start = data.get("guard_confirmation_retry_from", "verify_sources.py")
    if not isinstance(confirmation_start, str) or not confirmation_start.strip():
        raise ValueError("guard_confirmation_retry_from must be a non-empty script name")
    data["guard_confirmation_retry_from"] = confirmation_start.strip()
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
    if data["guard_confirmation_retry_from"] not in known_scripts:
        raise ValueError("guard_confirmation_retry_from must name a maintenance stage")
    if data["guard_confirmation_retry_from"] not in retryable_set:
        raise ValueError("guard_confirmation_retry_from must be a retryable network stage")
    data["max_total_runtime_seconds"] = _positive_int(
        data.get("max_total_runtime_seconds"), "max_total_runtime_seconds"
    )
    stage_timeouts = data.get("stage_timeouts_seconds")
    if not isinstance(stage_timeouts, dict) or set(stage_timeouts) != known_scripts:
        missing = sorted(known_scripts - set(stage_timeouts or {}))
        extra = sorted(set(stage_timeouts or {}) - known_scripts)
        raise ValueError(f"stage_timeouts_seconds must cover every stage exactly: missing={missing} extra={extra}")
    data["stage_timeouts_seconds"] = {
        script: _positive_int(value, f"stage_timeouts_seconds.{script}")
        for script, value in stage_timeouts.items()
    }
    confirmation_env = data.get("conservative_retry_env")
    if not isinstance(confirmation_env, dict) or not confirmation_env:
        raise ValueError("conservative_retry_env must be a non-empty object")
    invalid_env = sorted(
        key for key, value in confirmation_env.items()
        if not isinstance(key, str)
        or not key.startswith("IPTV_")
        or key not in ENV_DEFAULTS
        or not isinstance(value, str)
        or not value.strip()
    )
    if invalid_env:
        raise ValueError(f"conservative_retry_env has invalid overrides: {invalid_env}")
    data["conservative_retry_env"] = dict(confirmation_env)
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


def cleanup_attempt_evidence() -> None:
    """Remove only this workflow's bounded failure snapshots before a run."""
    for path in ROOT.glob("maintenance-attempt-*"):
        if path.is_file():
            try:
                path.unlink()
            except OSError as exc:
                print(f"MAINTENANCE WARN: cannot remove stale evidence {path.name}: {exc!r}")


def cleanup_stale_run_outputs() -> None:
    """Prevent a failed run from uploading diagnostics generated by an older run."""
    for name in STALE_RUN_OUTPUTS:
        path = ROOT / name
        if not path.is_file():
            continue
        try:
            path.unlink()
        except OSError as exc:
            raise RuntimeError(f"cannot remove stale run output {name}: {exc}") from exc


def snapshot_attempt_evidence(attempt: int, not_before_epoch: float = 0.0) -> None:
    """Preserve small decision reports when a pass fails before artifacts upload."""
    names = (
        "full-check-summary.json",
        "publish-guard-report.md",
        "published-recheck-report.md",
        "sources_status.csv",
    )
    for name in names:
        source = ROOT / name
        if not source.is_file():
            continue
        target = ROOT / f"maintenance-attempt-{attempt}-{name}"
        try:
            if not_before_epoch and source.stat().st_mtime + 0.001 < not_before_epoch:
                continue
            shutil.copyfile(source, target)
        except OSError as exc:
            print(f"MAINTENANCE WARN: cannot snapshot {name}: {exc!r}")


def collect_attempt_evidence(root: Path = ROOT, not_before_epoch: float = 0.0) -> dict[str, Any]:
    """Return bounded, self-contained failure evidence for alerts and audits."""
    path = root / "full-check-summary.json"
    try:
        if not_before_epoch and path.stat().st_mtime + 0.001 < not_before_epoch:
            return {}
        summary = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return {}
    guard = summary.get("publish_guard") if isinstance(summary.get("publish_guard"), dict) else {}
    recheck = summary.get("published_recheck") if isinstance(summary.get("published_recheck"), dict) else {}
    refill = recheck.get("refill") if isinstance(recheck.get("refill"), dict) else {}
    historical = (
        recheck.get("historical_fallback")
        if isinstance(recheck.get("historical_fallback"), dict)
        else {}
    )
    curated_groups = summary.get("curated_groups")
    if not isinstance(curated_groups, dict):
        curated_groups = {}
    failures = guard.get("failures") if isinstance(guard.get("failures"), list) else []
    warnings = guard.get("warnings") if isinstance(guard.get("warnings"), list) else []
    unavailable = guard.get("unavailable_sources") if isinstance(guard.get("unavailable_sources"), list) else []
    return {
        "generated_utc": str(summary.get("generated_utc") or ""),
        "unique_candidates": int(summary.get("unique_candidates") or 0),
        "playable_unique_urls": int(summary.get("playable_unique_urls") or 0),
        "curated_published_lines": int(summary.get("curated_published_lines") or 0),
        "curated_groups": {str(key): int(value or 0) for key, value in curated_groups.items()},
        "guard": {
            "status": str(guard.get("status") or "not_run"),
            "failures": [str(item) for item in failures[:20]],
            "warnings": [str(item) for item in warnings[:20]],
            "unavailable_sources": [str(item) for item in unavailable[:20]],
        },
        "published_recheck": {
            "before_rows": int(recheck.get("before_rows") or 0),
            "after_rows": int(recheck.get("after_rows") or 0),
            "removed_rows": int(recheck.get("removed_rows") or 0),
            "refilled_rows": int(refill.get("refilled_rows") or 0),
            "net_row_delta": int(recheck.get("net_row_delta") or 0),
            "post_retry_failed_unique_urls": int(recheck.get("post_retry_failed_unique_urls") or 0),
            "historical_fallback": {
                "candidates_available": int(historical.get("candidates_available") or 0),
                "attempted_unique_urls": int(historical.get("attempted_unique_urls") or 0),
                "playable_unique_urls": int(historical.get("playable_unique_urls") or 0),
                "refilled_rows": int(historical.get("refilled_rows") or 0),
            },
        },
    }


def run_attempt(
    attempt: int,
    total: int,
    env: dict[str, str],
    config: dict[str, Any],
    start_index: int = 0,
) -> dict[str, Any]:
    attempt_started = time.monotonic()
    record: dict[str, Any] = {
        "attempt": attempt,
        "started_utc": utc_now(),
        "status": "running",
        "profile": env.get(PROFILE_ENV, "standard"),
        "start_stage_index": start_index + 1,
        "start_stage": STAGES[start_index].label,
        "stages": [],
    }
    for index in range(start_index, len(STAGES)):
        stage = STAGES[index]
        display_index = index + 1
        command = stage_command(stage)
        stage_started = time.monotonic()
        print(f"\n[attempt {attempt}/{total} stage {display_index}/{len(STAGES)}] {stage.label}", flush=True)
        stage_env = env.copy()
        stage_env.update(STEP_ENV_OVERRIDES.get(stage.script, {}))
        configured_timeout = int((config.get("stage_timeouts_seconds") or {}).get(stage.script, 0) or 0)
        deadline_text = env.get(PIPELINE_DEADLINE_ENV, "")
        remaining_runtime = float("inf")
        if deadline_text:
            remaining_runtime = float(deadline_text) - time.monotonic()
        if remaining_runtime <= 0:
            returncode = 124
            timed_out = True
            launch_failed = False
            timeout_reason = "pipeline runtime budget exhausted before stage"
            effective_timeout = 0.0
        else:
            effective_timeout = min(
                float(configured_timeout) if configured_timeout > 0 else remaining_runtime,
                remaining_runtime,
            )
            try:
                completed = subprocess.run(
                    command,
                    cwd=ROOT,
                    env=stage_env,
                    check=False,
                    timeout=None if effective_timeout == float("inf") else effective_timeout,
                )
                returncode = completed.returncode
                timed_out = False
                launch_failed = False
                timeout_reason = ""
            except subprocess.TimeoutExpired:
                returncode = 124
                timed_out = True
                launch_failed = False
                timeout_reason = (
                    "pipeline runtime budget exhausted during stage"
                    if remaining_runtime <= configured_timeout
                    else "stage timeout exceeded"
                )
            except OSError as exc:
                returncode = 127
                timed_out = False
                launch_failed = True
                timeout_reason = f"process launch failed: {exc!r}"
        elapsed = round(time.monotonic() - stage_started, 3)
        classification = "ok" if returncode == 0 else (
            "fatal" if timed_out and "pipeline runtime budget" in timeout_reason
            else "fatal" if launch_failed
            else "retryable" if stage.script in set(config["retryable_scripts"])
            else "fatal" if timed_out
            else "confirmable" if (
                stage.script == "guard_publish.py"
                and returncode == GUARD_REJECTED_EXIT_CODE
                and int(config.get("guard_confirmation_attempts", 1)) > 1
            )
            else "fatal"
        )
        stage_record = {
            "index": display_index,
            "label": stage.label,
            "script": stage.script,
            "args": list(stage.args),
            "returncode": returncode,
            "elapsed_seconds": elapsed,
            "classification": classification,
            "timeout_seconds": None if effective_timeout == float("inf") else round(effective_timeout, 3),
            "timed_out": timed_out,
            "launch_failed": launch_failed,
        }
        if timeout_reason:
            stage_record["failure_reason"] = timeout_reason
        record["stages"].append(stage_record)
        if returncode != 0:
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
                f"MAINTENANCE ATTEMPT FAILED: stage={stage.label} exit={returncode} "
                f"classification={classification} elapsed={elapsed:.1f}s"
                + (f" reason={timeout_reason}" if timeout_reason else ""),
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
        print(
            f"max_attempts_per_retryable_stage={max_attempts} "
            f"guard_confirmation_attempts={config.get('guard_confirmation_attempts', 1)} "
            f"retry_delay_seconds={retry_delay} "
            f"max_total_runtime_seconds={config['max_total_runtime_seconds']}"
        )
        for index, stage in enumerate(STAGES, 1):
            classification = (
                "retryable" if stage.script in set(config["retryable_scripts"])
                else "confirmable" if stage.script == "guard_publish.py" and int(config.get("guard_confirmation_attempts", 1)) > 1
                else "fatal"
            )
            print(
                f"{index:02d}. [{classification}] timeout={config['stage_timeouts_seconds'][stage.script]}s "
                f"{stage.label}: {' '.join(stage_command(stage))}"
            )
        print(
            "conservative_retry_profile="
            + json.dumps(config["conservative_retry_env"], ensure_ascii=False, sort_keys=True)
        )
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
    retryable_scripts = set(config["retryable_scripts"])
    guard_confirmation_attempts = int(config.get("guard_confirmation_attempts", 1))
    max_pipeline_passes = (
        1
        + len(retryable_scripts) * (max_attempts - 1)
        + max(0, guard_confirmation_attempts - 1)
    )

    pipeline_started_epoch = time.time()
    started = time.monotonic()
    pipeline_deadline = started + int(config["max_total_runtime_seconds"])
    env[PIPELINE_DEADLINE_ENV] = str(pipeline_deadline)
    report: dict[str, Any] = {
        "schema_version": 3,
        "retry_strategy": "resume_failed_network_stage_and_confirm_guard_conservatively",
        "started_utc": utc_now(),
        "status": "running",
        "max_attempts": max_attempts,
        "max_attempts_per_retryable_stage": max_attempts,
        "max_pipeline_passes": max_pipeline_passes,
        "retry_delay_seconds": retry_delay,
        "guard_confirmation_attempts": guard_confirmation_attempts,
        "guard_confirmation_retry_from": config["guard_confirmation_retry_from"],
        "conservative_retry_profile": config["conservative_retry_env"],
        "max_total_runtime_seconds": config["max_total_runtime_seconds"],
        "stage_timeouts_seconds": config["stage_timeouts_seconds"],
        "attempts": [],
    }
    cleanup_attempt_evidence()
    cleanup_stale_run_outputs()
    write_report(report)
    start_index = 0
    stage_failure_counts: dict[str, int] = {}
    attempt = 1
    active_profile = "standard"

    while attempt <= max_pipeline_passes:
        attempt_env = env.copy()
        if active_profile != "standard":
            attempt_env.update(config["conservative_retry_env"])
            attempt_env[PROFILE_ENV] = active_profile
        else:
            attempt_env[PROFILE_ENV] = "standard"
        attempt_record = run_attempt(attempt, max_pipeline_passes, attempt_env, config, start_index)
        report["attempts"].append(attempt_record)
        if attempt_record["status"] == "ok":
            report.update(
                {
                    "status": "ok",
                    "successful_attempt": attempt,
                    "retry_failures_by_script": stage_failure_counts,
                    "finished_utc": utc_now(),
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                }
            )
            write_report(report)
            append_step_summary(
                f"## Maintenance pipeline\n\nStatus: **OK**  \n"
                f"Successful pass: {attempt}/{max_pipeline_passes}  \n"
                f"Elapsed: {report['elapsed_seconds']}s\n"
            )
            print(f"\nMAINTENANCE PIPELINE OK on pass {attempt}/{max_pipeline_passes}")
            return 0

        classification = str(attempt_record.get("failure_classification"))
        failed_stage = attempt_record.get("failed_stage") or {}
        failed_script = str(failed_stage.get("script") or "unknown")
        stage_failure_counts[failed_script] = stage_failure_counts.get(failed_script, 0) + 1
        attempt_record["failed_stage_attempt"] = stage_failure_counts[failed_script]
        evidence = collect_attempt_evidence(not_before_epoch=pipeline_started_epoch)
        if evidence:
            attempt_record["evidence"] = evidence
        report["retry_failures_by_script"] = stage_failure_counts
        write_report(report)
        snapshot_attempt_evidence(attempt, not_before_epoch=pipeline_started_epoch)
        if classification == "confirmable":
            confirmation_count = stage_failure_counts[failed_script]
            if confirmation_count < guard_confirmation_attempts:
                start_index = next(
                    index for index, item in enumerate(STAGES)
                    if item.script == config["guard_confirmation_retry_from"]
                )
                print(
                    f"Guard rejected this pass; starting confirmation pass at stage "
                    f"{start_index + 1}/{len(STAGES)} ({STAGES[start_index].label}) "
                    "with the conservative network profile.",
                    flush=True,
                )
                active_profile = "guard_confirmation_conservative"
                if retry_delay:
                    time.sleep(retry_delay)
                attempt += 1
                continue
        if classification != "retryable" or stage_failure_counts[failed_script] >= max_attempts:
            break
        start_index = max(0, int(failed_stage.get("index") or 1) - 1)
        active_profile = "network_retry_conservative"
        print(
            f"Retryable network-stage failure; waiting {retry_delay}s before resuming at "
            f"stage {start_index + 1}/{len(STAGES)} ({STAGES[start_index].label}).",
            flush=True,
        )
        if retry_delay:
            time.sleep(retry_delay)
        attempt += 1

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
        f"Pipeline passes: {len(report['attempts'])}/{max_pipeline_passes}  \n"
        f"Classification: {report['failure_classification']}  \n"
        f"Failed stage: {(report.get('failed_stage') or {}).get('label', 'unknown')}\n"
    )
    return int((last.get("failed_stage") or {}).get("returncode") or 1)


if __name__ == "__main__":
    raise SystemExit(main())
