#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent health monitor for the unattended IPTV publication pipeline.

The main update workflow can fail silently, be suspended, or leave a stale CDN
entry. This watchdog checks the workflow history and the canonical public
playlist from a separate scheduled run, then opens/updates a dedicated issue.
It never edits playlists.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from network_safety import public_urlopen
from publication_config import endpoint_urls, load_publication_config
from validate_playlist import validate_text

MARKER = "<!-- tv-live-auto-check-watchdog -->"
ISSUE_TITLE = "\u81ea\u52a8\u76d1\u63a7\u544a\u8b66 IPTV \u81ea\u52a8\u7ef4\u62a4\u6216 Raw \u53d1\u5e03\u5f02\u5e38"
HARD_FAILURE_CONCLUSIONS = {"action_required", "failure", "startup_failure", "timed_out"}
RUN_DETAIL_FIELDS = (
    "id",
    "run_number",
    "event",
    "status",
    "conclusion",
    "created_at",
    "updated_at",
    "run_started_at",
    "head_sha",
    "html_url",
)
MAX_ISSUE_BODY_CHARS = 30_000
MAX_ISSUE_EVIDENCE_CHARS = 20_000
MAX_ISSUE_PAGES = 10


class WatchdogError(RuntimeError):
    pass


@dataclass(frozen=True)
class HealthResult:
    failures: list[str]
    warnings: list[str]
    details: dict[str, Any]


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    text = str(value).replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def age_hours(value: str | None, now: datetime) -> float | None:
    parsed = parse_time(value)
    if parsed is None:
        return None
    return max(0.0, (now - parsed).total_seconds() / 3600.0)


def compact_run(run: dict[str, Any] | None) -> dict[str, Any] | None:
    if run is None:
        return None
    return {key: run.get(key) for key in RUN_DETAIL_FIELDS if key in run}


def api_request(url: str, token: str | None, method: str = "GET", payload: dict[str, Any] | None = None, timeout: int = 30, retries: int = 3) -> Any:
    headers = {
        "User-Agent": "tv-live-auto-check-watchdog",
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    last_error: Exception | None = None
    for attempt in range(1, max(1, retries) + 1):
        request = Request(url, headers=headers, method=method, data=data)
        try:
            with urlopen(request, timeout=timeout) as response:
                raw = response.read(8_000_000)
            if not raw:
                return None
            return json.loads(raw.decode("utf-8"))
        except HTTPError as exc:
            last_error = exc
            if exc.code in {400, 401, 403, 404, 405, 409, 422}:
                break
        except Exception as exc:
            last_error = exc
        if attempt < max(1, retries):
            time.sleep(2.0 * attempt)
    raise WatchdogError(f"GitHub API request failed after {max(1, retries)} attempts {method} {url}: {last_error!r}")


def public_fetch(url: str, timeout: int = 30, max_bytes: int = 3_000_000, retries: int = 3, retry_wait: float = 2.0) -> tuple[bytes, dict[str, str]]:
    """Fetch a public endpoint with bounded transient retries.

    A single DNS reset, CDN edge timeout, or GitHub 5xx must not create a
    production alert.  HTTP 404/410 and malformed content remain permanent
    failures and are returned immediately.
    """
    last_error: Exception | None = None
    for attempt in range(1, max(1, retries) + 1):
        request = Request(
            url,
            headers={
                "User-Agent": "tv-live-auto-check-watchdog",
                "Accept": "text/plain,application/json,*/*",
                "Connection": "close",
            },
        )
        try:
            with public_urlopen(request, timeout=timeout) as response:
                data = response.read(max_bytes + 1)
                headers = {
                    "status": str(getattr(response, "status", "")),
                    "cache_control": response.headers.get("Cache-Control", ""),
                    "age": response.headers.get("Age", ""),
                    "etag": response.headers.get("ETag", ""),
                    "attempts": str(attempt),
                }
            if len(data) > max_bytes:
                raise WatchdogError(f"public endpoint exceeded {max_bytes} bytes: {url}")
            return data, headers
        except HTTPError as exc:
            last_error = exc
            if exc.code in {400, 401, 403, 404, 405, 410, 422}:
                break
        except Exception as exc:
            last_error = exc
        if attempt < max(1, retries):
            time.sleep(retry_wait * attempt)
    raise WatchdogError(f"public endpoint failed after {max(1, retries)} attempts {url}: {last_error!r}")


def inspect_runs(runs: list[dict[str, Any]], now: datetime, max_age_hours: float, max_running_minutes: float, max_consecutive_failures: int) -> tuple[list[str], list[str], dict[str, Any]]:
    completed = [run for run in runs if run.get("status") == "completed"]
    completed.sort(key=lambda run: parse_time(run.get("updated_at") or run.get("created_at")) or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    running = [run for run in runs if run.get("status") in {"queued", "in_progress"}]
    failures: list[str] = []
    warnings: list[str] = []
    latest_success = next((run for run in completed if run.get("conclusion") == "success"), None)
    latest_completed = completed[0] if completed else None
    latest_success_timestamp = (
        latest_success.get("updated_at") or latest_success.get("created_at")
        if latest_success
        else None
    )
    latest_success_age = age_hours(latest_success_timestamp, now)
    consecutive_hard_failures = 0
    recent_non_hard: list[str] = []
    for run in completed:
        conclusion = str(run.get("conclusion") or "")
        if conclusion == "success":
            break
        if conclusion in HARD_FAILURE_CONCLUSIONS:
            consecutive_hard_failures += 1
        else:
            recent_non_hard.append(f"#{run.get('run_number')}={conclusion or 'unknown'}")
    if latest_success is None:
        failures.append("update workflow has no successful completed run in the retained history")
    else:
        if latest_success_age is None:
            failures.append("latest successful update run has no parseable timestamp")
        elif latest_success_age > max_age_hours:
            failures.append(f"latest successful update run is {latest_success_age:.1f}h old (limit {max_age_hours:.1f}h)")
    if consecutive_hard_failures >= max_consecutive_failures:
        failures.append(
            f"update workflow has {consecutive_hard_failures} hard failures since the latest success "
            f"(limit {max_consecutive_failures - 1})"
        )
    if recent_non_hard:
        warnings.append(
            "non-hard completed update runs since the latest success were not counted as failures: "
            + ", ".join(recent_non_hard[:10])
        )
    running_too_long: list[str] = []
    for run in running:
        started = parse_time(run.get("run_started_at") or run.get("created_at"))
        if started is None:
            warnings.append(f"running update run {run.get('run_number')} has no parseable start time")
            continue
        minutes = max(0.0, (now - started).total_seconds() / 60.0)
        if minutes > max_running_minutes:
            running_too_long.append(f"#{run.get('run_number')} {minutes:.1f}m")
    if running_too_long:
        failures.append(f"update workflow has overlong running jobs: {', '.join(running_too_long)}")
    details = {
        "workflow_runs_seen": len(runs),
        "latest_completed": compact_run(latest_completed),
        "latest_success": compact_run(latest_success),
        # Retain the legacy field for report consumers, but give it the corrected
        # hard-failure meaning rather than counting cancelled/skipped runs.
        "consecutive_completed_failures": consecutive_hard_failures,
        "consecutive_hard_failures": consecutive_hard_failures,
        "recent_non_hard_runs": recent_non_hard,
        "running_runs": [compact_run(run) for run in running],
        "running_too_long": running_too_long,
        "latest_success_age_hours": latest_success_age,
        "limits": {
            "max_age_hours": max_age_hours,
            "max_running_minutes": max_running_minutes,
            "max_consecutive_failures": max_consecutive_failures,
        },
    }
    return failures, warnings, details


def manifest_freshness(manifest: dict[str, Any], now: datetime, max_age_hours: float) -> tuple[list[str], dict[str, Any]]:
    summary = manifest.get("source_summary") if isinstance(manifest.get("source_summary"), dict) else {}
    generated_utc = str(summary.get("generated_utc") or "")
    generated_age = age_hours(generated_utc, now)
    failures: list[str] = []
    if generated_age is None:
        failures.append("public manifest has no parseable source_summary.generated_utc")
    elif generated_age > max_age_hours:
        failures.append(
            f"public playlist generation is {generated_age:.1f}h old (limit {max_age_hours:.1f}h)"
        )
    return failures, {
        "generated_utc": generated_utc,
        "generated_age_hours": generated_age,
        "max_age_hours": max_age_hours,
    }


def inspect_publication(
    repo: str,
    branch: str,
    timeout: int,
    require_manifest: bool,
    now: datetime,
    max_age_hours: float,
) -> tuple[list[str], list[str], dict[str, Any]]:
    config = load_publication_config(ROOT)
    endpoints = endpoint_urls(repo, branch, ROOT)
    raw_spec = next(item for item in endpoints if item["name"] == "github_raw")
    primary_spec = next(item for item in endpoints if item.get("required_primary"))
    failures: list[str] = []
    warnings: list[str] = []
    result: dict[str, Any] = {"endpoints": {}}
    fetched: dict[str, bytes] = {}
    for label, spec in (("raw", raw_spec), ("primary", primary_spec)):
        try:
            data, headers = public_fetch(str(spec["url"]), timeout=timeout)
            digest = hashlib.sha256(data).hexdigest()
            validate_text(data.decode("utf-8", "strict"), require_categories=True)
            fetched[label] = data
            result["endpoints"][label] = {"url": spec["url"], "bytes": len(data), "sha256": digest, **headers}
        except Exception as exc:
            detail = f"{label} publication endpoint failed: {exc}"
            if label == "raw":
                failures.append(detail)
            else:
                # The CDN reconciler owns the television endpoint. A stale or
                # temporarily unavailable edge must not create a second
                # maintenance incident or hide the healthy Raw publication.
                warnings.append(f"{detail} (CDN scope; see the CDN reconciliation issue)")
                result["endpoints"][label] = {"url": spec["url"], "ok": False, "error": str(exc)}
    manifest_url = f"https://raw.githubusercontent.com/{repo}/{branch}/publish-manifest.json"
    try:
        manifest_data, manifest_headers = public_fetch(manifest_url, timeout=timeout, max_bytes=1_000_000)
        manifest = json.loads(manifest_data.decode("utf-8"))
        if manifest.get("schema_version") != 1:
            failures.append(f"public manifest schema_version is {manifest.get('schema_version')!r}, expected 1")
        freshness_failures, freshness_details = manifest_freshness(manifest, now, max_age_hours)
        failures.extend(freshness_failures)
        files = manifest.get("files") if isinstance(manifest.get("files"), dict) else {}
        expected_raw = files.get(config["authoritative_raw_file"], {})
        if "raw" in fetched:
            actual = hashlib.sha256(fetched["raw"]).hexdigest()
            if expected_raw.get("sha256") != actual or expected_raw.get("bytes") != len(fetched["raw"]):
                failures.append("public manifest does not match the authoritative Raw publication file")
        if "primary" in fetched:
            expected_primary = files.get(config["primary_text_file"], {})
            actual = hashlib.sha256(fetched["primary"]).hexdigest()
            if expected_primary.get("sha256") != actual or expected_primary.get("bytes") != len(fetched["primary"]):
                warnings.append("primary television endpoint is serving a valid but stale publication (CDN scope)")
            elif "raw" in fetched and fetched["raw"] != fetched["primary"]:
                warnings.append("primary television endpoint differs from authoritative Raw bytes (CDN scope)")
        result["manifest"] = {
            "url": manifest_url,
            "bytes": len(manifest_data),
            "sha256": hashlib.sha256(manifest_data).hexdigest(),
            **manifest_headers,
            **freshness_details,
        }
    except Exception as exc:
        if require_manifest:
            failures.append(f"public publication manifest failed: {exc}")
        else:
            warnings.append(f"public publication manifest unavailable: {exc}")
    return failures, warnings, result


def render_report(result: HealthResult, now: datetime) -> str:
    lines = [
        "# IPTV publication watchdog report",
        "",
        f"Checked UTC: {now.isoformat()}",
        f"Status: {'failed' if result.failures else 'ok'}",
        f"Failures: {len(result.failures)}",
        f"Warnings: {len(result.warnings)}",
        "",
        "## Failures",
        "",
    ]
    lines.extend(f"- {item}" for item in (result.failures or ["none"]))
    lines += ["", "## Warnings", ""]
    lines.extend(f"- {item}" for item in (result.warnings or ["none"]))
    return "\n".join(lines) + "\n"


def write_reports(result: HealthResult, now: datetime, markdown_path: Path, json_path: Path) -> None:
    report = render_report(result, now)
    markdown_path.write_text(report, encoding="utf-8", newline="\n")
    json_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "checked_utc": now.isoformat(),
                "status": "failed" if result.failures else "ok",
                "failures": result.failures,
                "warnings": result.warnings,
                "details": result.details,
            },
            ensure_ascii=False,
            indent=2,
            default=str,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        try:
            with Path(summary).open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(report)
        except Exception as exc:
            print(f"WATCHDOG WARN: cannot write GITHUB_STEP_SUMMARY: {exc!r}")


def render_issue_body(result: HealthResult, now: datetime) -> str:
    evidence = json.dumps(result.details, ensure_ascii=False, indent=2, default=str)
    evidence_note = ""
    if len(evidence) > MAX_ISSUE_EVIDENCE_CHARS:
        evidence = json.dumps(
            {
                "truncated": True,
                "reason": "detailed evidence exceeded the issue-body budget",
                "original_characters": len(evidence),
                "sha256": hashlib.sha256(evidence.encode("utf-8")).hexdigest(),
                "full_evidence": "download watchdog-report.json from the workflow artifact",
                "top_level_keys": sorted(str(key) for key in result.details),
            },
            ensure_ascii=False,
            indent=2,
        )
        evidence_note = "\n完整证据已保存到本次 workflow 的 `watchdog-report.json` artifact。\n"
    lines = [
        MARKER,
        "# IPTV 自动监控报警",
        "",
        f"\u68c0\u67e5\u65f6\u95f4 (UTC): {now.isoformat()}",
        "",
        "## 失败",
    ]
    lines.extend(f"- {item}" for item in (result.failures or ["\u65e0"] ))
    if result.warnings:
        lines += ["", "## 警告", *[f"- {item}" for item in result.warnings]]
    lines += ["", "## 详细证据", evidence_note, "```json", evidence, "```", ""]
    body = "\n".join(lines)
    if len(body) > MAX_ISSUE_BODY_CHARS:
        digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
        body = "\n".join(
            [
                MARKER,
                "# IPTV 自动监控报警",
                "",
                f"检查时间 (UTC): {now.isoformat()}",
                "",
                "告警正文超过安全长度，完整证据请下载本次 workflow 的 `watchdog-report.json` artifact。",
                f"原始正文字符数: {len(body)}",
                f"原始正文 SHA256: `{digest}`",
                "",
            ]
        )
    return body


def list_watchdog_issues(repo: str, token: str) -> list[dict[str, Any]]:
    """Read a bounded history so a closed watchdog issue can be reused."""
    base = f"https://api.github.com/repos/{repo}/issues"
    issues: list[dict[str, Any]] = []
    for page in range(1, MAX_ISSUE_PAGES + 1):
        batch = api_request(f"{base}?state=all&per_page=100&page={page}", token) or []
        if not isinstance(batch, list):
            raise WatchdogError(f"GitHub issues API returned a non-list page: page={page}")
        issues.extend(item for item in batch if isinstance(item, dict))
        if len(batch) < 100:
            break
    return issues


def update_issue(repo: str, token: str, result: HealthResult, now: datetime, dry_run: bool = False) -> dict[str, Any]:
    if dry_run:
        print(render_issue_body(result, now))
        return {"status": "dry-run"}
    if not token:
        raise WatchdogError("GITHUB_TOKEN is required to create/update watchdog issues")
    base = f"https://api.github.com/repos/{repo}"
    issues = list_watchdog_issues(repo, token)
    matches = [item for item in issues if "pull_request" not in item and MARKER in str(item.get("body", ""))]
    matches.sort(key=lambda item: str(item.get("updated_at") or item.get("created_at") or ""), reverse=True)
    existing = matches[0] if matches else None
    body = render_issue_body(result, now)
    if result.failures:
        payload = {"title": ISSUE_TITLE, "body": body}
        if existing:
            if existing.get("state") == "closed":
                payload["state"] = "open"
            issue = api_request(f"{base}/issues/{existing['number']}", token, method="PATCH", payload=payload)
            if existing.get("state") == "closed":
                api_request(
                    f"{base}/issues/{existing['number']}/comments",
                    token,
                    method="POST",
                    payload={"body": "Watchdog 检测到问题再次出现，已重新打开此 Issue。"},
                )
            return {"status": "updated", "number": issue.get("number")}
        issue = api_request(f"{base}/issues", token, method="POST", payload=payload)
        return {"status": "opened", "number": issue.get("number")}
    if existing and existing.get("state") == "open":
        api_request(f"{base}/issues/{existing['number']}", token, method="PATCH", payload={"state": "closed", "body": body})
        return {"status": "closed", "number": existing.get("number")}
    return {"status": "no-open-issue"}


def confirm_health(
    check_once,
    *,
    attempts: int = 2,
    delay_seconds: float = 30.0,
    sleep=time.sleep,
) -> tuple[HealthResult, datetime]:
    """Repeat a failed watchdog observation before raising an alert.

    Public endpoints and the GitHub API are outside this repository's control.
    A second independently fetched observation prevents a single edge reset or
    short Raw/CDN propagation mismatch from becoming an operator alert. The
    final result remains strict when both observations fail.
    """
    attempts = max(1, int(attempts))
    observations: list[dict[str, Any]] = []
    final_result: HealthResult | None = None
    final_now = datetime.now(timezone.utc)
    for attempt in range(1, attempts + 1):
        final_now = datetime.now(timezone.utc)
        try:
            result = check_once(final_now)
        except Exception as exc:
            result = HealthResult(
                [f"watchdog observation raised {type(exc).__name__}: {exc}"],
                [],
                {"observation_exception": repr(exc)[:1000]},
            )
        final_result = result
        observations.append({
            "attempt": attempt,
            "status": "failed" if result.failures else "ok",
            "failures": list(result.failures),
            "warnings": list(result.warnings),
        })
        if not result.failures:
            if attempt > 1:
                result = HealthResult(
                    result.failures,
                    [
                        *result.warnings,
                        f"watchdog transient failure recovered on confirmation attempt {attempt}",
                    ],
                    dict(result.details),
                )
                final_result = result
            break
        if attempt < attempts and delay_seconds > 0:
            sleep(delay_seconds)
    if final_result is None:
        final_result = HealthResult(["watchdog produced no observation"], [], {})
    details = dict(final_result.details)
    details["confirmation"] = {
        "attempts_configured": attempts,
        "observations": observations,
        "confirmed": len(observations) > 1 and not final_result.failures,
    }
    final_result = HealthResult(final_result.failures, final_result.warnings, details)
    return final_result, final_now


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=os.getenv("GITHUB_REPOSITORY", ""))
    parser.add_argument("--branch", default="main")
    parser.add_argument("--workflow", default="update.yml")
    parser.add_argument("--max-age-hours", type=float, default=36.0)
    parser.add_argument("--max-running-minutes", type=float, default=240.0)
    parser.add_argument("--max-consecutive-failures", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--confirmation-attempts", type=int, default=2)
    parser.add_argument("--confirmation-delay", type=float, default=30.0)
    parser.add_argument("--allow-missing-manifest", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", default=str(ROOT / "watchdog-report.md"))
    parser.add_argument("--json", dest="json_path", default=str(ROOT / "watchdog-report.json"))
    args = parser.parse_args(argv)
    if "/" not in args.repo:
        raise SystemExit("--repo owner/name or GITHUB_REPOSITORY is required")
    token = os.getenv("GITHUB_TOKEN", "")
    api_base = f"https://api.github.com/repos/{args.repo}"
    def check_once(now: datetime) -> HealthResult:
        runs_payload = api_request(
            f"{api_base}/actions/workflows/{args.workflow}/runs?branch={args.branch}&per_page=50",
            token,
            timeout=args.timeout,
        )
        runs = list(runs_payload.get("workflow_runs", [])) if isinstance(runs_payload, dict) else []
        run_failures, run_warnings, run_details = inspect_runs(
            runs, now, args.max_age_hours, args.max_running_minutes, args.max_consecutive_failures
        )
        pub_failures, pub_warnings, pub_details = inspect_publication(
            args.repo,
            args.branch,
            args.timeout,
            not args.allow_missing_manifest,
            now,
            args.max_age_hours,
        )
        return HealthResult(
            run_failures + pub_failures,
            run_warnings + pub_warnings,
            {"runs": run_details, "publication": pub_details},
        )

    result, now = confirm_health(
        check_once,
        attempts=max(1, args.confirmation_attempts),
        delay_seconds=max(0.0, args.confirmation_delay),
    )
    write_reports(result, now, Path(args.report), Path(args.json_path))
    print(json.dumps({"status": "fail" if result.failures else "ok", "failures": result.failures, "warnings": result.warnings, "details": result.details}, ensure_ascii=False, indent=2, default=str))
    issue_status = update_issue(args.repo, token, result, now, args.dry_run)
    print(json.dumps({"issue": issue_status}, ensure_ascii=False, sort_keys=True))
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
