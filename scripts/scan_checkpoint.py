"""Append-only probe evidence, reusable only inside the same maintenance run."""
from __future__ import annotations

import json
from pathlib import Path
import time


class ScanCheckpoint:
    def __init__(self, path: Path, run_id: str, fingerprint: str, max_age: int = 7200):
        self.path = path
        self.max_age = max_age
        self.results: dict[str, dict] = {}
        header = {"schema_version": 1, "run_id": run_id, "fingerprint": fingerprint}
        valid = False
        if path.is_file() and path.stat().st_size <= 80_000_000:
            with path.open(encoding="utf-8") as handle:
                try:
                    valid = json.loads(handle.readline()) == header
                except ValueError:
                    pass
                if valid:
                    for line in handle:
                        try:
                            item = json.loads(line)
                            if isinstance(item, dict) and isinstance(item.get("url"), str):
                                self.results[item["url"]] = item
                        except ValueError:
                            # A process timeout may interrupt the final append.
                            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        if not valid:
            path.write_text(json.dumps(header) + "\n", encoding="utf-8")

    def get(self, url: str, core: bool) -> dict | None:
        item = self.results.get(url)
        if not item or item.get("ok") is not True or item.get("core") != core:
            return None
        timestamp = item.get("timestamp")
        if not isinstance(timestamp, (int, float)) or not 0 <= time.time() - timestamp <= self.max_age:
            return None
        return item

    def record(self, url: str, core: bool, ok: bool, detail: str,
               checked_at: str, elapsed_seconds: float) -> None:
        item = {"url": url, "core": core, "ok": ok, "detail": detail,
                "checked_at": checked_at, "elapsed_seconds": elapsed_seconds, "timestamp": time.time()}
        # Leading newline isolates a partial final record from a killed process.
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write("\n" + json.dumps(item, ensure_ascii=True) + "\n")
            handle.flush()
        self.results[url] = item
