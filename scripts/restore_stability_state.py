#!/usr/bin/env python3
"""Restore validated stability state from the newest successful update artifact."""
from __future__ import annotations

import argparse
import io
import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import zipfile

from playlist_config import ROOT
from stability import history_path, load_history, validate_history, write_history

API = "https://api.github.com"
ARTIFACT_NAME = "stability-state"
WORKFLOW_FILE = "update.yml"


def api_json(path: str, token: str) -> dict:
    request = Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "tv-live-auto-check-stability-restore",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def download(url: str, token: str, max_bytes: int = 5_000_000) -> bytes:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "tv-live-auto-check-stability-restore",
        },
    )
    with urlopen(request, timeout=60) as response:
        payload = response.read(max_bytes + 1)
    if len(payload) > max_bytes:
        raise ValueError("stability artifact archive exceeds size limit")
    return payload


def successful_run_ids(repo: str, branch: str, token: str) -> list[int]:
    query = urlencode({"branch": branch, "status": "success", "per_page": 20})
    data = api_json(f"/repos/{repo}/actions/workflows/{WORKFLOW_FILE}/runs?{query}", token)
    runs = data.get("workflow_runs") or []
    return [int(run["id"]) for run in runs if run.get("head_branch") == branch]


def artifact_for_run(repo: str, run_id: int, token: str) -> dict | None:
    query = urlencode({"name": ARTIFACT_NAME, "per_page": 10})
    data = api_json(f"/repos/{repo}/actions/runs/{run_id}/artifacts?{query}", token)
    artifacts = [item for item in data.get("artifacts") or [] if item.get("name") == ARTIFACT_NAME and not item.get("expired")]
    return max(artifacts, key=lambda item: int(item.get("id") or 0)) if artifacts else None


def history_from_zip(payload: bytes) -> dict:
    expected = history_path().name
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        safe_names = [name for name in archive.namelist() if not name.endswith("/")]
        matches = [name for name in safe_names if Path(name).name == expected]
        if len(matches) != 1 or len(safe_names) != 1:
            raise ValueError(f"stability artifact must contain exactly {expected}")
        info = archive.getinfo(matches[0])
        if info.file_size > 4_000_000:
            raise ValueError("stability state exceeds uncompressed size limit")
        data = json.loads(archive.read(info).decode("utf-8"))
    return validate_history(data)


def restore(repo: str, branch: str, token: str) -> dict:
    failures: list[str] = []
    if repo and token:
        try:
            for run_id in successful_run_ids(repo, branch, token):
                artifact = artifact_for_run(repo, run_id, token)
                if not artifact:
                    continue
                try:
                    history = history_from_zip(download(str(artifact["archive_download_url"]), token))
                    write_history(history)
                    return {"status": "restored", "run_id": run_id, "artifact_id": artifact.get("id"), "urls": len(history["urls"])}
                except Exception as exc:
                    failures.append(f"run {run_id}: {exc}")
        except Exception as exc:
            failures.append(f"artifact lookup: {exc}")

    # First deployment migrates the checked-in legacy TSV. Later missing or
    # damaged artifacts degrade to a fresh state instead of blocking TV updates.
    history = validate_history(load_history())
    write_history(history)
    return {
        "status": "fallback",
        "urls": len(history["urls"]),
        "reason": failures[:5] or ["no successful stability artifact available"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=os.getenv("GITHUB_REPOSITORY", ""))
    parser.add_argument("--branch", default=os.getenv("GITHUB_REF_NAME", "main"))
    args = parser.parse_args(argv)
    result = restore(args.repo.strip(), args.branch.strip(), os.getenv("GITHUB_TOKEN", "").strip())
    print("stability restore " + json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
