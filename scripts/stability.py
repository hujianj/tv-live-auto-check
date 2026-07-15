#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import csv
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Iterable

from playlist_config import ROOT, load_priority

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
    return ROOT / str(stability_config().get("history_file", "stability-history.tsv"))


def report_path() -> Path:
    return ROOT / str(stability_config().get("report_file", "stability-report.md"))


def now_beijing() -> str:
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()


def load_history() -> dict:
    path = history_path()
    if not stability_enabled():
        return {"version": 1, "urls": {}}
    if not path.exists():
        legacy = ROOT / "stability-history.json"
        if legacy.exists():
            return load_json_history(legacy)
        return {"version": 1, "urls": {}}
    if path.suffix.lower() == ".json":
        return load_json_history(path)
    return load_tsv_history(path)


def load_json_history(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"version": 1, "urls": {}}
    urls = data.get("urls")
    if not isinstance(urls, dict):
        data["urls"] = {}
    data.setdefault("version", 1)
    return data


def load_tsv_history(path: Path) -> dict:
    urls: dict[str, dict] = {}
    try:
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                url = (row.get("url") or "").strip()
                if not url:
                    continue
                entry = {
                    "ok": int(row.get("ok") or 0),
                    "fail": int(row.get("fail") or 0),
                    "streak_ok": int(row.get("streak_ok") or 0),
                    "streak_fail": int(row.get("streak_fail") or 0),
                    "last_status": row.get("last_status") or "",
                    "adjustment": int(row.get("adjustment") or 0),
                    "last_seen": row.get("last_seen") or "",
                    "last_name": row.get("last_name") or "",
                    "last_source": row.get("last_source") or "",
                }
                last_error = row.get("last_error") or ""
                if last_error:
                    entry["last_error"] = last_error
                urls[url] = entry
    except Exception:
        return {"version": 1, "urls": {}}
    return {"version": 1, "urls": urls}


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


def write_history(history: dict) -> None:
    path = history_path()
    urls = history.get("urls") or {}
    if path.suffix.lower() == ".json":
        path.write_text(json.dumps(history, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8", newline="\n")
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


def update_history(rows: Iterable, failed_urls: dict[str, str], source_map: dict[tuple[str, str], str]) -> dict:
    """Update bounded stability history from the final published recheck result."""
    cfg = stability_config()
    history = load_history()
    urls = history.setdefault("urls", {})
    rows = list(rows)
    failed = set(failed_urls)
    representative_by_url = {}
    for row in rows:
        representative_by_url.setdefault(row.url, row)
    seen_urls = set(representative_by_url)
    timestamp = now_beijing()
    before_count = len(urls)
    ok_updates = 0
    fail_updates = 0
    new_urls = 0
    status_counts: Counter[str] = Counter()

    for row in representative_by_url.values():
        entry = urls.get(row.url)
        if not isinstance(entry, dict):
            entry = {}
            urls[row.url] = entry
            new_urls += 1
        is_fail = row.url in failed
        if is_fail:
            entry["fail"] = int(entry.get("fail") or 0) + 1
            entry["streak_fail"] = int(entry.get("streak_fail") or 0) + 1
            entry["streak_ok"] = 0
            entry["last_status"] = "fail"
            entry["last_error"] = str(failed_urls.get(row.url, ""))[:160]
            fail_updates += 1
        else:
            entry["ok"] = int(entry.get("ok") or 0) + 1
            entry["streak_ok"] = int(entry.get("streak_ok") or 0) + 1
            entry["streak_fail"] = 0
            entry["last_status"] = "ok"
            entry.pop("last_error", None)
            ok_updates += 1
        entry["last_seen"] = timestamp
        entry["last_name"] = row.name[:80]
        source = source_for(row, source_map)
        if source != "unknown":
            entry["last_source"] = source[:80]
        entry["adjustment"] = stability_adjustment(row.url, history)
        status_counts[str(entry.get("last_status") or "unknown")] += 1

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
    summary = {
        "enabled": stability_enabled(),
        "history_file": str(history_path().name),
        "tracked_urls_before": before_count,
        "tracked_urls_after": len(urls),
        "max_entries": max_entries,
        "new_urls": new_urls,
        "updated_urls": len(seen_urls),
        "ok_updates": ok_updates,
        "fail_updates": fail_updates,
        "trimmed_urls": trimmed,
        "last_updated_beijing": timestamp,
        "current_adjustment_min": min(adjustments) if adjustments else 0,
        "current_adjustment_max": max(adjustments) if adjustments else 0,
    }
    history.update({
        "version": 1,
        "last_updated_beijing": timestamp,
        "summary": summary,
    })
    # Keep this committed history compact. The human-readable details are in
    # stability-report.md; the TSV is for scoring and should not bloat Git.
    write_history(history)
    write_report(history, summary)
    return summary


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
