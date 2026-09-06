#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import csv
import copy
import os
import tempfile
import uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Iterable

from playlist_config import ROOT, load_priority
from url_utils import is_publishable_http_url

STATE_VERSION = 2
OBSERVATION_VERSION = 1
MAX_APPLIED_OBSERVATIONS = 32

HISTORY_FIELDS = [
    "url",
    "ok",
    "fail",
    "streak_ok",
    "streak_fail",
    "last_status",
    "adjustment",
    "last_seen",
    "last_name",
    "last_source",
    "last_error",
]


def stability_config() -> dict:
    return load_priority().get("stability", {})


def stability_enabled() -> bool:
    return bool(stability_config().get("enabled", True))


def history_path() -> Path:
    return ROOT / str(stability_config().get("history_file", "stability-state.json"))


def report_path() -> Path:
    return ROOT / str(stability_config().get("report_file", "stability-report.md"))


def now_beijing() -> str:
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()


def current_beijing_week() -> str:
    today = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8))).date()
    return (today - timedelta(days=today.weekday())).isoformat()


def load_history() -> dict:
    path = history_path()
    if not stability_enabled():
        return empty_history()
    if not path.exists():
        configured_path = ROOT / str(stability_config().get("history_file", "stability-state.json"))
        if path == configured_path:
            for legacy in (ROOT / "stability-history.tsv", ROOT / "stability-history.json"):
                if legacy.exists() and legacy != path:
                    data = load_json_history(legacy) if legacy.suffix.lower() == ".json" else load_tsv_history(legacy)
                    data["version"] = STATE_VERSION
                    data.setdefault("applied_observation_ids", [])
                    return data
        return empty_history()
    if path.suffix.lower() == ".json":
        return load_json_history(path)
    return load_tsv_history(path)


def empty_history() -> dict:
    return {"version": STATE_VERSION, "applied_observation_ids": [], "urls": {}}


def load_json_history(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return empty_history()
    urls = data.get("urls")
    if not isinstance(urls, dict):
        data["urls"] = {}
    if data.get("version") in {None, 1}:
        data["version"] = STATE_VERSION
    data.setdefault("applied_observation_ids", [])
    return data


def load_tsv_history(path: Path) -> dict:
    urls: dict[str, dict] = {}
    counter_cap = max(1, int(stability_config().get("evidence_counter_cap", 20)))
    streak_cap = max(1, int(stability_config().get("streak_cap", 10)))
    try:
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                url = (row.get("url") or "").strip()
                if not url or not is_publishable_http_url(url):
                    continue
                entry = {
                    "ok": _clamp(int(row.get("ok") or 0), 0, counter_cap),
                    "fail": _clamp(int(row.get("fail") or 0), 0, counter_cap),
                    "streak_ok": _clamp(int(row.get("streak_ok") or 0), 0, streak_cap),
                    "streak_fail": _clamp(int(row.get("streak_fail") or 0), 0, streak_cap),
                    "last_status": _text(row.get("last_status"), 8),
                    "adjustment": _clamp(
                        int(row.get("adjustment") or 0),
                        int(stability_config().get("min_adjustment", -90)),
                        int(stability_config().get("max_adjustment", 140)),
                    ),
                    "last_seen": _text(row.get("last_seen"), 20),
                    "last_name": _text(row.get("last_name"), 80),
                    "last_source": _text(row.get("last_source"), 80),
                }
                last_error = row.get("last_error") or ""
                if last_error:
                    entry["last_error"] = _text(last_error, 160)
                urls[url] = entry
    except Exception:
        return empty_history()
    return {"version": STATE_VERSION, "applied_observation_ids": [], "urls": urls}


def validate_history(history: dict) -> dict:
    if not isinstance(history, dict):
        raise ValueError("stability state must be an object")
    if history.get("version") != STATE_VERSION:
        raise ValueError(f"unsupported stability state version={history.get('version')!r}")
    applied = history.get("applied_observation_ids")
    if not isinstance(applied, list) or len(applied) > MAX_APPLIED_OBSERVATIONS:
        raise ValueError("applied_observation_ids must be a bounded list")
    if len(set(applied)) != len(applied) or any(not isinstance(item, str) or not item or len(item) > 200 for item in applied):
        raise ValueError("invalid applied observation id")
    urls = history.get("urls")
    max_entries = max(0, int(stability_config().get("max_entries", 5000)))
    if not isinstance(urls, dict) or (max_entries and len(urls) > max_entries):
        raise ValueError("stability URL state is invalid or exceeds max_entries")
    counter_cap = max(1, int(stability_config().get("evidence_counter_cap", 20)))
    streak_cap = max(1, int(stability_config().get("streak_cap", 10)))
    min_adjustment = int(stability_config().get("min_adjustment", -90))
    max_adjustment = int(stability_config().get("max_adjustment", 140))
    for url, entry in urls.items():
        if not isinstance(url, str) or len(url) > 4096 or not is_publishable_http_url(url) or not isinstance(entry, dict):
            raise ValueError(f"invalid stability URL entry: {url!r}")
        for field, cap in (("ok", counter_cap), ("fail", counter_cap), ("streak_ok", streak_cap), ("streak_fail", streak_cap)):
            value = entry.get(field, 0)
            if type(value) is not int or not 0 <= value <= cap:
                raise ValueError(f"invalid stability counter {field} for {url}")
        if entry.get("last_status", "") not in {"", "ok", "fail"}:
            raise ValueError(f"invalid last_status for {url}")
        adjustment = entry.get("adjustment", 0)
        if type(adjustment) is not int or not min_adjustment <= adjustment <= max_adjustment:
            raise ValueError(f"invalid stability adjustment for {url}")
        for field, limit in (("last_seen", 20), ("last_name", 80), ("last_source", 80), ("last_error", 160)):
            value = entry.get(field, "")
            if not isinstance(value, str) or len(value) > limit or any(ch in value for ch in "\r\n\t"):
                raise ValueError(f"invalid stability field {field} for {url}")
    return history


def _clamp(value: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, value))


def stability_adjustment(url: str, history: dict | None = None) -> int:
    """Return a sorting adjustment. Lower is better, higher means less stable."""
    if not stability_enabled():
        return 0
    cfg = stability_config()
    history = history if history is not None else load_history()
    entry = (history.get("urls") or {}).get(url)
    if not entry:
        return int(cfg.get("no_history_adjustment", 0))
    ok = int(entry.get("ok") or 0)
    fail = int(entry.get("fail") or 0)
    streak_ok = int(entry.get("streak_ok") or 0)
    streak_fail = int(entry.get("streak_fail") or 0)
    counter_cap = max(1, int(cfg.get("evidence_counter_cap", 20)))
    streak_cap = max(1, int(cfg.get("streak_cap", 10)))
    ok = min(counter_cap, ok)
    fail = min(counter_cap, fail)
    streak_ok = min(streak_cap, streak_ok)
    streak_fail = min(streak_cap, streak_fail)
    score = (
        ok * int(cfg.get("ok_bonus", -3))
        + fail * int(cfg.get("fail_penalty", 10))
        + streak_ok * int(cfg.get("streak_ok_bonus", -8))
        + streak_fail * int(cfg.get("streak_fail_penalty", 45))
    )
    return _clamp(
        score,
        int(cfg.get("min_adjustment", -90)),
        int(cfg.get("max_adjustment", 140)),
    )


def source_for(row, source_map: dict[tuple[str, str], str]) -> str:
    return source_map.get((row.name, row.url), "unknown")


def _text(value: object, limit: int = 0) -> str:
    text = str(value or "").replace("\r", " ").replace("\n", " ").replace("\t", " ").strip()
    return text[:limit] if limit > 0 else text


def update_evidence(entry: dict, is_fail: bool, error: str = "") -> None:
    """Update bounded recent evidence without letting old counts dominate forever."""
    cfg = stability_config()
    counter_cap = max(1, int(cfg.get("evidence_counter_cap", 20)))
    streak_cap = max(1, int(cfg.get("streak_cap", 10)))
    ok = min(counter_cap, int(entry.get("ok") or 0))
    fail = min(counter_cap, int(entry.get("fail") or 0))
    if is_fail:
        entry["ok"] = max(0, ok - 1)
        entry["fail"] = min(counter_cap, fail + 1)
        entry["streak_fail"] = min(streak_cap, int(entry.get("streak_fail") or 0) + 1)
        entry["streak_ok"] = 0
        entry["last_status"] = "fail"
        entry["last_error"] = str(error or "")[:160]
    else:
        entry["ok"] = min(counter_cap, ok + 1)
        entry["fail"] = max(0, fail - 1)
        entry["streak_ok"] = min(streak_cap, int(entry.get("streak_ok") or 0) + 1)
        entry["streak_fail"] = 0
        entry["last_status"] = "ok"
        entry.pop("last_error", None)


def write_history(history: dict) -> None:
    path = history_path()
    urls = history.get("urls") or {}
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() == ".json":
        validate_history(history)
        payload = json.dumps(history, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
        fd, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, path)
        finally:
            try:
                Path(temporary).unlink()
            except FileNotFoundError:
                pass
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HISTORY_FIELDS, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for url, entry in sorted(urls.items(), key=lambda item: item[0]):
            writer.writerow({
                "url": _text(url),
                "ok": int(entry.get("ok") or 0),
                "fail": int(entry.get("fail") or 0),
                "streak_ok": int(entry.get("streak_ok") or 0),
                "streak_fail": int(entry.get("streak_fail") or 0),
                "last_status": _text(entry.get("last_status")),
                "adjustment": int(entry.get("adjustment") or 0),
                "last_seen": _text(entry.get("last_seen")),
                "last_name": _text(entry.get("last_name"), 80),
                "last_source": _text(entry.get("last_source"), 80),
                "last_error": _text(entry.get("last_error"), 160),
            })


def build_observation(
    rows: Iterable,
    failed_urls: dict[str, str],
    source_map: dict[tuple[str, str], str],
    observation_id: str,
) -> dict:
    observation_id = _text(observation_id, 200)
    if not observation_id:
        raise ValueError("stability observation id must not be empty")
    representative_by_url = {}
    for row in rows:
        representative_by_url.setdefault(row.url, row)
    entries = []
    for row in representative_by_url.values():
        failed = row.url in failed_urls
        entries.append({
            "url": row.url,
            "name": _text(row.name, 80),
            "source": _text(source_for(row, source_map), 80),
            "status": "fail" if failed else "ok",
            "error": _text(failed_urls.get(row.url, ""), 160),
        })
    return {
        "schema_version": OBSERVATION_VERSION,
        "observation_id": observation_id,
        "created_beijing": now_beijing(),
        "seen_period": current_beijing_week(),
        "entries": entries,
    }


def validate_observation(observation: dict) -> dict:
    if not isinstance(observation, dict) or observation.get("schema_version") != OBSERVATION_VERSION:
        raise ValueError("invalid stability observation schema")
    observation_id = observation.get("observation_id")
    if not isinstance(observation_id, str) or not observation_id or len(observation_id) > 200:
        raise ValueError("invalid stability observation id")
    created = observation.get("created_beijing")
    seen_period = observation.get("seen_period")
    if not isinstance(created, str) or not created or len(created) > 40:
        raise ValueError("invalid stability observation timestamp")
    if not isinstance(seen_period, str) or not seen_period or len(seen_period) > 20:
        raise ValueError("invalid stability observation period")
    entries = observation.get("entries")
    max_entries = max(1, int(stability_config().get("max_entries", 5000))) * 2
    if not isinstance(entries, list) or len(entries) > max_entries:
        raise ValueError("invalid stability observation entries")
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("stability observation entry must be an object")
        url = entry.get("url")
        if not isinstance(url, str) or len(url) > 4096 or not is_publishable_http_url(url) or url in seen:
            raise ValueError(f"invalid or duplicate observation URL: {url!r}")
        seen.add(url)
        if entry.get("status") not in {"ok", "fail"}:
            raise ValueError(f"invalid observation status for {url}")
        for field, limit in (("name", 80), ("source", 80), ("error", 160)):
            value = entry.get(field, "")
            if not isinstance(value, str) or len(value) > limit or any(ch in value for ch in "\r\n\t"):
                raise ValueError(f"invalid observation {field} for {url}")
    return observation


def write_observation(path: Path, observation: dict) -> None:
    validate_observation(observation)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(observation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def _apply_observation(history: dict, observation: dict) -> tuple[dict, dict]:
    """Apply one observation in memory; repeated observation IDs are a no-op."""
    validate_history(history)
    validate_observation(observation)
    cfg = stability_config()
    urls = history.setdefault("urls", {})
    observation_id = observation["observation_id"]
    applied_ids = history.setdefault("applied_observation_ids", [])
    duplicate = observation_id in applied_ids
    seen_urls = {entry["url"] for entry in observation["entries"]}
    timestamp = observation["created_beijing"]
    seen_period = observation["seen_period"]
    before_count = len(urls)
    ok_updates = 0
    fail_updates = 0
    new_urls = 0

    if not duplicate:
        for observed in observation["entries"]:
            url = observed["url"]
            entry = urls.get(url)
            if not isinstance(entry, dict):
                entry = {}
                urls[url] = entry
                new_urls += 1
            is_fail = observed["status"] == "fail"
            update_evidence(entry, is_fail, observed.get("error", ""))
            if is_fail:
                fail_updates += 1
            else:
                ok_updates += 1
            entry["last_seen"] = seen_period
            entry["last_name"] = observed.get("name", "")
            source = observed.get("source", "")
            if source and source != "unknown":
                entry["last_source"] = source
            entry["adjustment"] = stability_adjustment(url, history)

    max_entries = int(cfg.get("max_entries", 5000))
    trimmed = 0
    if max_entries > 0 and len(urls) > max_entries:
        def keep_key(item: tuple[str, dict]) -> tuple[int, int, int, str]:
            url, entry = item
            current = 1 if url in seen_urls else 0
            ok = int(entry.get("ok") or 0)
            fail = int(entry.get("fail") or 0)
            last_seen = str(entry.get("last_seen") or "")
            # Keep current candidates first, then proven stable URLs, then newest.
            return (current, ok - fail, ok + fail, last_seen)

        kept = dict(sorted(urls.items(), key=keep_key, reverse=True)[:max_entries])
        trimmed = len(urls) - len(kept)
        history["urls"] = kept
        urls = kept

    adjustments = [stability_adjustment(url, history) for url in seen_urls if url in urls]
    if not duplicate:
        applied_ids.append(observation_id)
        history["applied_observation_ids"] = applied_ids[-MAX_APPLIED_OBSERVATIONS:]

    summary = {
        "enabled": stability_enabled(),
        "history_file": str(history_path().name),
        "state_artifact_only": True,
        "state_update_mode": "applied",
        "observation_id": observation_id,
        "observation_applied": not duplicate,
        "tracked_urls_before": before_count,
        "tracked_urls_after": len(urls),
        "max_entries": max_entries,
        "evidence_counter_cap": max(1, int(cfg.get("evidence_counter_cap", 20))),
        "streak_cap": max(1, int(cfg.get("streak_cap", 10))),
        "last_seen_granularity": "beijing_week_start",
        "new_urls": new_urls,
        "updated_urls": 0 if duplicate else len(seen_urls),
        "ok_updates": ok_updates,
        "fail_updates": fail_updates,
        "trimmed_urls": trimmed,
        "last_updated_beijing": timestamp,
        "current_adjustment_min": min(adjustments) if adjustments else 0,
        "current_adjustment_max": max(adjustments) if adjustments else 0,
    }
    history.update({
        "version": STATE_VERSION,
        "last_updated_beijing": history.get("last_updated_beijing", timestamp) if duplicate else timestamp,
        "summary": summary,
    })
    validate_history(history)
    return history, summary


def preview_observation(observation: dict, history: dict | None = None) -> dict:
    baseline = history if history is not None else load_history()
    working_history = copy.deepcopy(baseline)
    _, summary = _apply_observation(working_history, observation)
    summary["observation_applied"] = False
    summary["observation_pending"] = observation["observation_id"] not in baseline.get("applied_observation_ids", [])
    summary["state_update_mode"] = "deferred_until_maintenance_success"
    return summary


def apply_observation(observation: dict) -> dict:
    history, summary = _apply_observation(load_history(), observation)
    write_history(history)
    write_report(history, summary)
    return summary


def update_history(rows: Iterable, failed_urls: dict[str, str], source_map: dict[tuple[str, str], str]) -> dict:
    """Compatibility helper for direct callers; production uses pending observations."""
    observation = build_observation(rows, failed_urls, source_map, f"direct:{uuid.uuid4().hex}")
    return apply_observation(observation)


def write_report(history: dict, summary: dict) -> None:
    urls = history.get("urls") or {}
    ranked = sorted(urls.items(), key=lambda item: stability_adjustment(item[0], history))
    worst = sorted(urls.items(), key=lambda item: stability_adjustment(item[0], history), reverse=True)
    lines = [
        "# Stream stability report",
        "",
        f"Enabled: {summary.get('enabled')}",
        f"Tracked URLs before: {summary.get('tracked_urls_before')}",
        f"Tracked URLs after: {summary.get('tracked_urls_after')}",
        f"Updated URLs this run: {summary.get('updated_urls')}",
        f"OK updates this run: {summary.get('ok_updates')}",
        f"Fail updates this run: {summary.get('fail_updates')}",
        f"Trimmed URLs: {summary.get('trimmed_urls')}",
        f"Last updated Beijing: {summary.get('last_updated_beijing')}",
        "",
        "## Most stable tracked URLs",
        "",
        "| Adjustment | OK | Fail | Streak OK | Streak Fail | Channel | Source | URL |",
        "|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for url, entry in ranked[:30]:
        lines.append(
            f"| {stability_adjustment(url, history)} | {int(entry.get('ok') or 0)} | {int(entry.get('fail') or 0)} | "
            f"{int(entry.get('streak_ok') or 0)} | {int(entry.get('streak_fail') or 0)} | "
            f"{str(entry.get('last_name') or '').replace('|', '/')} | {str(entry.get('last_source') or '').replace('|', '/')} | {url.replace('|', '/')} |"
        )
    lines += [
        "",
        "## Least stable tracked URLs",
        "",
        "| Adjustment | OK | Fail | Streak OK | Streak Fail | Channel | Source | Error | URL |",
        "|---:|---:|---:|---:|---:|---|---|---|---|",
    ]
    for url, entry in worst[:30]:
        lines.append(
            f"| {stability_adjustment(url, history)} | {int(entry.get('ok') or 0)} | {int(entry.get('fail') or 0)} | "
            f"{int(entry.get('streak_ok') or 0)} | {int(entry.get('streak_fail') or 0)} | "
            f"{str(entry.get('last_name') or '').replace('|', '/')} | {str(entry.get('last_source') or '').replace('|', '/')} | "
            f"{str(entry.get('last_error') or '').replace('|', '/')} | {url.replace('|', '/')} |"
        )
    report_path().write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
