#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create, update, and resolve one deduplicated GitHub maintenance issue."""
from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime, timezone
from urllib.error import HTTPError
from urllib.request import Request, urlopen

TITLE = "\u81ea\u52a8\u7ef4\u62a4\u544a\u8b66 IPTV \u76f4\u64ad\u6e90\u7ef4\u62a4\u6d41\u7a0b\u5931\u8d25"
MARKER = "<!-- tv-live-auto-check-maintenance-alert -->"
API = "https://api.github.com"
RETRYABLE_HTTP = {408, 425, 429, 500, 502, 503, 504}


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


def find_open_issue(repo: str, token: str) -> dict | None:
    issues = api_request("GET", f"/repos/{repo}/issues?state=open&per_page=100", token) or []
    for issue in issues:
        if "pull_request" in issue:
            continue
        if issue.get("title") == TITLE or MARKER in str(issue.get("body") or ""):
            return issue
    return None


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
    detail = message or "\u8bf7\u67e5\u770b workflow artifact \u548c\u6b65\u9aa4\u65e5\u5fd7"
    return "\n".join([
        MARKER,
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
        f"- \u8be6\u7ec6\u4fe1\u606f: {detail}",
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
        f"\u8be6\u7ec6: {detail}"
    )


def success_comment(context: dict[str, str]) -> str:
    return (
        f"\u81ea\u52a8\u7ef4\u62a4\u5df2\u6062\u590d: {context['time']} UTC\n"
        f"[Workflow run {context['run_number'] or context['run_id']}]({context['run_url']})\n"
        "GitHub Raw \u548c\u4e3b\u7535\u89c6\u8ba2\u9605\u7aef\u70b9\u5747\u5df2\u901a\u8fc7\u68c0\u67e5?\u73b0\u5173\u95ed\u6b64 Issue\u3002"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("status", choices=["failure", "cdn_pending", "success"])
    parser.add_argument("--message", default="")
    args = parser.parse_args(argv)
    token = os.getenv("GITHUB_TOKEN", "")
    context = run_context()
    repo = context["repo"]
    if not token or not repo:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPOSITORY are required")
    issue = find_open_issue(repo, token)
    if args.status in {"failure", "cdn_pending"}:
        body = issue_body(context, args.status, args.message)
        if issue is None:
            created = api_request("POST", f"/repos/{repo}/issues", token, {"title": TITLE, "body": body})
            print(f"created maintenance issue #{created.get('number')}")
        else:
            number = int(issue["number"])
            api_request("PATCH", f"/repos/{repo}/issues/{number}", token, {"title": TITLE, "body": body})
            api_request("POST", f"/repos/{repo}/issues/{number}/comments", token, {"body": status_comment(context, args.status, args.message)})
            print(f"updated maintenance issue #{number}")
        return 0
    if issue is None:
        print("no open maintenance issue to close")
        return 0
    number = int(issue["number"])
    api_request("POST", f"/repos/{repo}/issues/{number}/comments", token, {"body": success_comment(context)})
    api_request("PATCH", f"/repos/{repo}/issues/{number}", token, {"state": "closed", "state_reason": "completed"})
    print(f"closed maintenance issue #{number}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
