"""Export current-run diagnostics without replacing the guarded TV subscription."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from channel_scope import CHANNEL_SCOPE, NETWORK_SCOPE, domestic_chinese_issue
from channel_utils import escape_m3u_attr
from channel_utils import cctv_number
from curate_ku9 import prepare_curated_row, resolve_url_aliases, sort_key
from source_config import load_source_specs
from source_policy import publication_issue
from stability import empty_history, validate_history
from url_utils import is_publishable_http_url, redact_text


def read_json(path: Path, default: dict) -> dict:
    if not path.is_file():
        return default
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} must contain an object")
    return data


def read_csv(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def recent_check(value: str, not_before: str) -> bool:
    try:
        checked = datetime.fromisoformat(value.replace("Z", "+00:00"))
        start = datetime.fromisoformat(not_before.replace("Z", "+00:00"))
        return checked.tzinfo is not None and start <= checked <= datetime.now(timezone.utc) and (datetime.now(timezone.utc) - checked).total_seconds() <= 7200
    except (ValueError, TypeError):
        return False


def stable_evidence(entry: dict) -> bool:
    try:
        last_seen = datetime.fromisoformat(str(entry.get("last_seen", "")))
        last_seen = last_seen.replace(tzinfo=timezone.utc) if last_seen.tzinfo is None else last_seen.astimezone(timezone.utc)
        fresh = 0 <= (datetime.now(timezone.utc) - last_seen).total_seconds() <= 30 * 86400
        return fresh and entry.get("last_status") == "ok" and int(entry.get("streak_ok", 0)) >= 3
    except (ValueError, TypeError):
        return False


def export_outputs(root: Path, maintenance: dict | None = None) -> dict:
    summary = read_json(root / "full-check-summary.json", {})
    maintenance = maintenance or read_json(root / "maintenance-run.json", {})
    specs = {spec.name: spec for spec in load_source_specs(root / "config" / "sources.json")}
    inventory = read_json(root / "source-inventory.json", {"sources": []})
    metadata = {item["url"]: item for item in read_csv(root / "stream_check_results.csv") if item.get("ok") == "True"}
    origins = {(item["name"], item["url"]): item["source"] for item in read_csv(root / "curated-source-map.csv")}
    rows, checks = [], []
    config_matches = summary.get("source_config_sha256") == hashlib.sha256((root / "config" / "sources.json").read_bytes()).hexdigest()
    for item in read_csv(root / "published_recheck_results.csv"):
        url = item.get("url", "")
        name = item.get("name", "")
        evidence = metadata.get(url, {})
        source = origins.get((name, url), evidence.get("source", item.get("source", "")))
        checked_now = (config_matches
                       and recent_check(item.get("checked_at", ""), summary.get("generated_utc", ""))
                       and recent_check(item.get("checked_at", ""), maintenance.get("started_utc", "")))
        issue = publication_issue(specs.get(source), url)
        if not checked_now:
            issue = issue or "no matching current-run check evidence"
        issue = issue or domestic_chinese_issue(name, item.get("group", ""), source, evidence.get("tvg_id", ""), evidence.get("country", ""), evidence.get("language", ""))
        needs_progress = bool(cctv_number(name) or item.get("group") in {"\u592e\u89c6\u9891\u9053", "\u536b\u89c6\u9891\u9053", "\u5730\u65b9\u9891\u9053"})
        if needs_progress and item.get("progress_required") != "True":
            issue = issue or "live progress was not checked"
        row, reason, _detail = prepare_curated_row(name, url, item.get("group", ""), source)
        playable = checked_now and item.get("ok") == "True" and item.get("video_required") == "True" and not issue and row is not None
        checks.append({"name": name, "source": source, "url": url if is_publishable_http_url(url) else "[excluded]",
                       "video_probe_ok": item.get("ok") == "True", "eligible_current_result": playable,
                       "checked_at": item.get("checked_at", ""), "elapsed_seconds": item.get("elapsed_seconds", ""),
                       "reason": issue or reason or redact_text(item.get("detail", ""))})
        if playable:
            rows.append(row)
    rows, conflicts = resolve_url_aliases(rows)
    rows.sort(key=sort_key)
    history_status = "not_available"
    history = empty_history()
    try:
        history = validate_history(read_json(root / "stability-state.json", history))
        history_status = "validated" if history["urls"] else "empty"
    except (ValueError, TypeError):
        history_status = "invalid_ignored"
    stable = [row for row in rows if stable_evidence(history["urls"].get(row[2], {}))]

    def render(values) -> str:
        lines = ["#EXTM3U"]
        for group, name, url, _source in values:
            entry = metadata.get(url, {})
            logo = entry.get("tvg_logo", "")
            logo = logo if is_publishable_http_url(logo) else ""
            attrs = {"tvg-id": entry.get("tvg_id", ""), "tvg-name": name, "tvg-logo": logo, "group-title": group}
            lines.append('#EXTINF:-1 ' + ' '.join(f'{key}="{escape_m3u_attr(value)}"' for key, value in attrs.items()) + ',' + name)
            lines.append(url)
        return "\n".join(lines) + "\n"

    report = {"schema_version": 1, "network_scope": NETWORK_SCOPE, "channel_scope": CHANNEL_SCOPE,
              "maintenance_status": maintenance.get("status", "not_run"),
              "subscription_replaced_by_export": False,
              "publication_ready": maintenance.get("status") == "ok" and summary.get("publish_guard", {}).get("status") == "ok",
              "playlist_role": "diagnostic_only_until_publication_gates_pass",
              "generated_utc": summary.get("generated_utc", ""),
              "counts": {"parsed": summary.get("parsed_candidates", 0), "eligible": summary.get("eligible_candidates", 0),
                         "checked_unique": summary.get("checked_candidates", 0), "final_video_rows": len(rows), "stable_rows": len(stable)},
              "final_sources": dict(Counter(row[3] for row in rows)),
              "groups_by_source": {group: dict(Counter(row[3] for row in rows if row[0] == group)) for group in dict.fromkeys(row[0] for row in rows)},
              "groups": dict(Counter(row[0] for row in rows)), "checks": checks, "sources": inventory.get("sources", []),
              "identity_conflicts_excluded": len(conflicts), "history_status": history_status,
              "stable_rule": "current video check passed and at least 3 prior consecutive successful observations within 30 days; not a long-term guarantee",
              "failed_stage": maintenance.get("failed_stage"),
              "language_validation": "upstream metadata and channel identity, not audio transcription"}
    output = root / "output"
    output.mkdir(exist_ok=True)
    files = {"live.m3u": render(rows), "current-network.m3u": render(rows), "stable.m3u": render(stable),
             "report.json": json.dumps(report, ensure_ascii=False, indent=2) + "\n"}
    lines = ["# Current-network IPTV verification", "", f"Maintenance: {report['maintenance_status']}",
             "Scope: domestic Chinese channels, current execution environment only.",
             "These exports do not replace the guarded public subscription.",
             f"Counts: {report['counts']}", f"History: {history_status}. Stable list may be empty during warm-up.", "",
             "| Channel | Current video check | Source |", "|---|---|---|"]
    lines.extend(f"| {item['name'].replace('|', '/')} | {'PASS' if item['eligible_current_result'] else 'FAIL/EXCLUDED'} | {item['source']} |" for item in checks)
    files["report.md"] = "\n".join(lines) + "\n"
    for name, payload in files.items():
        temporary = output / (name + ".tmp")
        temporary.write_text(payload, encoding="utf-8", newline="\n")
        temporary.replace(output / name)
    return report["counts"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    print(json.dumps(export_outputs(parser.parse_args().root), ensure_ascii=False))
