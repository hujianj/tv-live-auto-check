#!/usr/bin/env python3
"""Restore validated stability state from the newest successful update artifact."""
from __future__ import annotations

import argparse
import io
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener, urlopen
import uuid
import zipfile

from network_safety import public_urlopen
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


class NoArtifactRedirect(HTTPRedirectHandler):
    """Keep the API credential on GitHub, never on signed artifact storage."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fresh_artifact_api_url(url: str) -> str:
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.netloc != "api.github.com" or parsed.fragment
            or not re.fullmatch(r"/repos/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/actions/artifacts/[0-9]+/zip", parsed.path)):
        raise ValueError("artifact download must use the GitHub artifact API")
    # Only the redirect API is cache-busted. Fixed TV subscription URLs remain
    # canonical. A cached short-lived storage Location caused repeated 401s.
    query = [(k, v) for k, v in parse_qsl(parsed.query) if k != "restore_nonce"]
    query.append(("restore_nonce", uuid.uuid4().hex))
    return urlunsplit(parsed._replace(query=urlencode(query)))


def validate_artifact_storage_url(url: str) -> str:
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower()
    if (parsed.scheme != "https" or parsed.username is not None or parsed.password is not None
            or parsed.port not in (None, 443) or parsed.fragment
            or not any(host.endswith(suffix) for suffix in (
                ".blob.core.windows.net", ".actions.githubusercontent.com", ".githubusercontent.com"))):
        raise ValueError("unexpected GitHub artifact storage destination")
    return url


def download(url: str, token: str, max_bytes: int = 5_000_000) -> bytes:
    opener = build_opener(NoArtifactRedirect())
    for attempt in range(2):
        request = Request(fresh_artifact_api_url(url), headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "tv-live-auto-check-stability-restore",
            "X-GitHub-Api-Version": "2022-11-28",
            "Cache-Control": "no-cache",
        })
        try:
            with opener.open(request, timeout=30) as response:
                payload = response.read(max_bytes + 1)
        except HTTPError as redirect:
            if redirect.code not in (301, 302, 303, 307, 308):
                raise
            try:
                location = validate_artifact_storage_url(redirect.headers.get("Location", ""))
            finally:
                redirect.close()
            # The signed storage URL authenticates itself. Sending the GitHub
            # Bearer token here both leaks it and can produce storage HTTP 401.
            storage_request = Request(location, headers={
                "User-Agent": "tv-live-auto-check-stability-restore",
            })
            try:
                with public_urlopen(storage_request, timeout=60) as response:
                    payload = response.read(max_bytes + 1)
            except HTTPError as exc:
                status = exc.code
                exc.close()
                if status in (401, 403) and attempt == 0:
                    continue  # Obtain a new signed Location, not retry the old one.
                raise RuntimeError(f"artifact storage returned HTTP {status}") from None
            except Exception as exc:
                # A transport/policy error can include the signed request URL.
                # Keep credentials out of the fallback report and Actions log.
                raise RuntimeError(f"artifact storage request failed ({type(exc).__name__})") from None
        if len(payload) > max_bytes:
            raise ValueError("stability artifact archive exceeds size limit")
        return payload
    raise RuntimeError("artifact download failed after fresh redirect retry")


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
