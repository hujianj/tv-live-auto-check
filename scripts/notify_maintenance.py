#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create, update, and resolve one deduplicated GitHub maintenance issue."""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from urllib.parse import quote
from urllib.request import Request, urlopen

TITLE = "[自动维护告警] IPTV 直播源维护流程失败"
MARKER = "<!-- tv-live-auto-check-maintenance-alert -->"
API = "https://api.github.com"


def api_request(method: str, path: str, token: str, payload: dict | None = None):
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = Request(
        API + path,
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "tv-live-auto-check-maintenance",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    with urlopen(req, timeout=30) as response:
        raw = response.read()
    return json.loads(raw.decode("utf-8")) if raw else None


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


def failure_body(context: dict[str, str], message: str) -> str:
    return "\n".join(
        [
            MARKER,
            "# IPTV 自动维护需要处理",
            "",
            "自动聚合、真实播放验证、发布或 CDN 健康检查未完整通过。",
            "提交前失败不会覆盖线上订阅；如果仅发布后的 CDN 检查失败，GitHub Raw 可能已经更新，而电视兼容 CDN 入口可能仍在返回旧缓存。",
            "",
            f"- 最新失败时间（UTC）：{context['time']}",
            f"- Workflow run：[{context['run_number'] or context['run_id']}]({context['run_url']})",
            f"- 事件：`{context['event']}`",
            f"- 分支：`{context['ref']}`",
            f"- 源提交：`{context['sha']}`",
            f"- 摘要：{message or '请打开失败 run 查看具体步骤和 artifact。'}",
            "",
            "下一次完整维护成功后，此 issue 会自动关闭。",
        ]
    ) + "\n"


def failure_comment(context: dict[str, str], message: str) -> str:
    return (
        f"再次失败：{context['time']} UTC；"
        f"[run {context['run_number'] or context['run_id']}]({context['run_url']})；"
        f"`{context['sha']}`；{message or '请查看失败步骤。'}"
    )


def success_comment(context: dict[str, str]) -> str:
    return (
        f"已恢复：{context['time']} UTC 的完整维护与发布检查通过，"
        f"[run {context['run_number'] or context['run_id']}]({context['run_url']})。自动关闭告警。"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("status", choices=["failure", "success"])
    parser.add_argument("--message", default="")
    args = parser.parse_args(argv)
    token = os.getenv("GITHUB_TOKEN", "")
    context = run_context()
    repo = context["repo"]
    if not token or not repo:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPOSITORY are required")
    issue = find_open_issue(repo, token)
    if args.status == "failure":
        body = failure_body(context, args.message)
        if issue is None:
            created = api_request("POST", f"/repos/{repo}/issues", token, {"title": TITLE, "body": body})
            print(f"created maintenance issue #{created.get('number')}")
        else:
            number = int(issue["number"])
            api_request("PATCH", f"/repos/{repo}/issues/{number}", token, {"body": body})
            api_request("POST", f"/repos/{repo}/issues/{number}/comments", token, {"body": failure_comment(context, args.message)})
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
