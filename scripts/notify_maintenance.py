#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create, update, and resolve one deduplicated GitHub maintenance issue."""
from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

LEGACY_MARKER = "<!-- tv-live-auto-check-maintenance-alert -->"
SCOPES = {
    "maintenance": {
        "title": "自动维护告警 IPTV 媒体检测或发布失败",
        "marker": "<!-- tv-live-auto-check-maintenance-failure -->",
    },
    "cdn": {
        "title": "自动维护告警 IPTV 主订阅 CDN 同步中",
        "marker": "<!-- tv-live-auto-check-cdn-pending -->",
    },
}
API = "https://api.github.com"
RETRYABLE_HTTP = {408, 425, 429, 500, 502, 503, 504}
MAX_FAILURE_DETAIL_CHARS = 12_000


def api_request(method: str, path: str, token: str, payload: dict | None = None, retries: int = 3):
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "tv-live-auto-check-maintenance",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json; charset=utf-8",
    }
    last_error: Exception | None = None
    for attempt in range(1, max(1, retries) + 1):
        request = Request(API + path, data=data, method=method, headers=headers)
        try:
            with urlopen(request, timeout=30) as response:
                raw = response.read(2_000_000)
            return json.loads(raw.decode("utf-8")) if raw else None
        except HTTPError as exc:
            last_error = exc
            if exc.code not in RETRYABLE_HTTP:
                break
        except Exception as exc:
            last_error = exc
        if attempt < max(1, retries):
            time.sleep(float(attempt))
    raise RuntimeError(f"GitHub API request failed after {max(1, retries)} attempts: {method} {path}: {last_error!r}")


def find_open_issue(repo: str, token: str, scope: str) -> dict | None:
    if scope not in SCOPES:
        raise ValueError(f"unsupported maintenance issue scope: {scope!r}")
    issues = api_request("GET", f"/repos/{repo}/issues?state=open&per_page=100", token) or []
    marker = str(SCOPES[scope]["marker"])
    title = str(SCOPES[scope]["title"])
    for issue in issues:
        if "pull_request" in issue:
            continue
        body = str(issue.get("body") or "")
        if issue.get("title") == title or marker in body:
            return issue
        # Migrate the original combined issue without allowing CDN recovery to
        # close a genuine media-verification failure (or vice versa).
        if LEGACY_MARKER in body:
            if scope == "cdn" and "CDN 同步中" in body:
                return issue
            if scope == "maintenance" and "维护流程失败" in body:
                return issue
    return None


def scope_for_status(status: str) -> str:
    return "maintenance" if status == "failure" else "cdn"


def run_context() -> dict[str, str]:
    server = os.getenv("GITHUB_SERVER_URL", "https://github.com")
    repo = os.getenv("GITHUB_REPOSITORY", "")
    run_id = os.getenv("GITHUB_RUN_ID", "")
    return {
        "repo": repo,
        "run_id": run_id,
        "run_number": os.getenv("GITHUB_RUN_NUMBER", ""),
        "sha": os.getenv("GITHUB_SHA", ""),
        "event": os.getenv("GITHUB_EVENT_NAME", ""),
        "ref": os.getenv("GITHUB_REF_NAME", ""),
        "run_url": f"{server}/{repo}/actions/runs/{run_id}" if repo and run_id else "",
        "time": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }


def status_label(status: str) -> str:
    return {
        "failure": "\u7ef4\u62a4\u6d41\u7a0b\u5931\u8d25",
        "cdn_pending": "\u5df2\u53d1\u5e03\uff0cCDN \u540c\u6b65\u4e2d",
    }[status]


def issue_body(context: dict[str, str], status: str, message: str) -> str:
    label = status_label(status)
    scope = scope_for_status(status)
    detail = message or "\u8bf7\u67e5\u770b workflow artifact \u548c\u6b65\u9aa4\u65e5\u5fd7"
    return "\n".join([
        str(SCOPES[scope]["marker"]),
        f"# IPTV {label}",
        "",
        f"\u5f53\u524d\u72b6\u6001: **{label}**",
        "",
        "\u8fd9\u4e2a Issue \u7531\u81ea\u52a8\u7ef4\u62a4\u6d41\u7a0b\u66f4\u65b0\u3002\u5982\u679c\u4ec5 CDN \u672a\u540c\u6b65\uff0cGitHub Raw \u4ecd\u662f\u6743\u5a01\u5730\u5740\uff0c\u4e0d\u4ee3\u8868\u672c\u6b21\u68c0\u6d4b\u548c\u63d0\u4ea4\u5931\u8d25\u3002",
        "",
        f"- \u68c0\u67e5\u65f6\u95f4 (UTC): {context['time']}",
        f"- Workflow run: [{context['run_number'] or context['run_id']}]({context['run_url']})",
        f"- \u4e8b\u4ef6: `{context['event']}`",
        f"- \u5206\u652f: `{context['ref']}`",
        f"- \u63d0\u4ea4: `{context['sha']}`",
        "",
        "## \u8be6\u7ec6\u4fe1\u606f",
        "",
        detail,
        "",
        "\u6062\u590d\u540e\uff0c\u6210\u529f\u8fd0\u884c\u4f1a\u81ea\u52a8\u5173\u95ed\u6b64 Issue\u3002",
    ]) + "\n"


def status_comment(context: dict[str, str], status: str, message: str) -> str:
    label = status_label(status)
    detail = message or "\u65e0"
    return (
        f"\u72b6\u6001: **{label}**\n"
        f"\u65f6\u95f4: {context['time']} UTC\n"
        f"[Workflow run {context['run_number'] or context['run_id']}]({context['run_url']})\n"
        f"\u63d0\u4ea4: `{context['sha']}`\n"
        f"\u8be6\u7ec6:\n{detail}"
    )


def success_comment(context: dict[str, str], scope: str) -> str:
    recovered = "媒体检测与发布" if scope == "maintenance" else "主电视订阅 CDN"
    return (
        f"{recovered}已恢复: {context['time']} UTC\n"
        f"[Workflow run {context['run_number'] or context['run_id']}]({context['run_url']})\n"
        f"{recovered}恢复条件已通过自动校验，现关闭此 Issue。"
    )


def maintenance_failure_detail(path: str) -> str:
    """Return a compact failed-stage summary suitable for the alert issue."""
    try:
        report = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return ""
    if report.get("status") != "failed":
        return ""
    stage = report.get("failed_stage") or {}
    attempts = report.get("attempts") if isinstance(report.get("attempts"), list) else []
    if not stage and attempts:
        stage = attempts[-1].get("failed_stage") or {}
    if not stage:
        return ""
    label = str(stage.get("label") or stage.get("script") or "unknown")
    script = str(stage.get("script") or "unknown")
    code = int(stage.get("returncode") or 1)
    classification = str(stage.get("classification") or report.get("failure_classification") or "unknown")
    elapsed = float(stage.get("elapsed_seconds") or 0.0)
    timeout = stage.get("timeout_seconds")
    timeout_text = "none" if timeout is None else f"{float(timeout):.1f}s"
    reason = str(stage.get("failure_reason") or "none")
    lines = [(
        f"failed_stage={label} ({script}), exit={code}, classification={classification}, "
        f"stage_elapsed={elapsed:.1f}s, stage_timeout={timeout_text}, reason={reason}, "
        f"pipeline_attempts={len(attempts)}"
    )]
    for attempt in attempts:
        evidence = attempt.get("evidence") if isinstance(attempt.get("evidence"), dict) else {}
        if not evidence:
            continue
        guard = evidence.get("guard") if isinstance(evidence.get("guard"), dict) else {}
        recheck = (
            evidence.get("published_recheck")
            if isinstance(evidence.get("published_recheck"), dict)
            else {}
        )
        historical = (
            recheck.get("historical_fallback")
            if isinstance(recheck.get("historical_fallback"), dict)
            else {}
        )
        groups = evidence.get("curated_groups") if isinstance(evidence.get("curated_groups"), dict) else {}
        failures = guard.get("failures") if isinstance(guard.get("failures"), list) else []
        unavailable = guard.get("unavailable_sources") if isinstance(guard.get("unavailable_sources"), list) else []
        lines.append(
            "- attempt={attempt_no}, profile={profile}, lines={lines_count}, "
            "core_groups=CCTV:{cctv}/satellite:{satellite}/local:{local}, "
            "recheck={before}->{after} removed={removed} refilled={refilled}, "
            "historical=available:{available}/attempted:{attempted}/accepted:{accepted}, "
            "unavailable_sources={unavailable}, guard_failures={failures}".format(
                attempt_no=attempt.get("attempt", "?"),
                profile=attempt.get("profile", "unknown"),
                lines_count=evidence.get("curated_published_lines", 0),
                cctv=groups.get("\u592e\u89c6\u9891\u9053", 0),
                satellite=groups.get("\u536b\u89c6\u9891\u9053", 0),
                local=groups.get("\u5730\u65b9\u9891\u9053", 0),
                before=recheck.get("before_rows", 0),
                after=recheck.get("after_rows", 0),
                removed=recheck.get("removed_rows", 0),
                refilled=recheck.get("refilled_rows", 0),
                available=historical.get("candidates_available", 0),
                attempted=historical.get("attempted_unique_urls", 0),
                accepted=historical.get("refilled_rows", 0),
                unavailable=",".join(str(item) for item in unavailable) or "none",
                failures=" | ".join(str(item) for item in failures) or "none",
            )
        )
    detail = "\n".join(lines)
    if len(detail) > MAX_FAILURE_DETAIL_CHARS:
        detail = detail[: MAX_FAILURE_DETAIL_CHARS - 80].rstrip() + "\n[diagnostic detail truncated; see artifact]"
    return detail


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("status", choices=["failure", "cdn_pending", "success"])
    parser.add_argument("--message", default="")
    parser.add_argument("--report", default="maintenance-run.json")
    parser.add_argument("--scope", choices=["all", "maintenance", "cdn"], default="all")
    args = parser.parse_args(argv)
    token = os.getenv("GITHUB_TOKEN", "")
    context = run_context()
    repo = context["repo"]
    if args.status == "failure":
        report_detail = maintenance_failure_detail(args.report)
        if report_detail:
            args.message = f"{args.message.rstrip()} {report_detail}".strip()
    if not token or not repo:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPOSITORY are required")
    if args.status in {"failure", "cdn_pending"}:
        scope = scope_for_status(args.status)
        issue = find_open_issue(repo, token, scope)
        body = issue_body(context, args.status, args.message)
        if issue is None:
            created = api_request(
                "POST",
                f"/repos/{repo}/issues",
                token,
                {"title": str(SCOPES[scope]["title"]), "body": body},
            )
            print(f"created maintenance issue #{created.get('number')}")
        else:
            number = int(issue["number"])
            api_request(
                "PATCH",
                f"/repos/{repo}/issues/{number}",
                token,
                {"title": str(SCOPES[scope]["title"]), "body": body},
            )
            api_request("POST", f"/repos/{repo}/issues/{number}/comments", token, {"body": status_comment(context, args.status, args.message)})
            print(f"updated maintenance issue #{number}")
        return 0
    scopes = ("maintenance", "cdn") if args.scope == "all" else (args.scope,)
    closed = 0
    for scope in scopes:
        issue = find_open_issue(repo, token, scope)
        if issue is None:
            print(f"no open {scope} issue to close")
            continue
        number = int(issue["number"])
        api_request("POST", f"/repos/{repo}/issues/{number}/comments", token, {"body": success_comment(context, scope)})
        api_request("PATCH", f"/repos/{repo}/issues/{number}", token, {"state": "closed", "state_reason": "completed"})
        print(f"closed {scope} issue #{number}")
        closed += 1
    print(f"closed scoped maintenance issues: {closed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
