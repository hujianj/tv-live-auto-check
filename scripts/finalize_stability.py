#!/usr/bin/env python3
"""Apply one validated maintenance observation to artifact-only stability state."""
from __future__ import annotations

import json
from pathlib import Path

from playlist_config import ROOT
from stability import apply_observation, validate_observation

OBSERVATION_FILE = ROOT / "stability-observation.json"
SUMMARY_FILE = ROOT / "full-check-summary.json"


def main() -> int:
    observation = validate_observation(json.loads(OBSERVATION_FILE.read_text(encoding="utf-8")))
    summary = json.loads(SUMMARY_FILE.read_text(encoding="utf-8"))
    expected = summary.get("stability") or {}
    observation_id = observation["observation_id"]
    if expected.get("observation_id") != observation_id:
        raise ValueError("publication summary and pending stability observation disagree")
    result = apply_observation(observation)
    if result.get("observation_id") != observation_id:
        raise ValueError("finalized stability state has the wrong observation id")
    if result.get("observation_applied"):
        for field in ("tracked_urls_after", "updated_urls", "ok_updates", "fail_updates", "trimmed_urls"):
            if result.get(field) != expected.get(field):
                raise ValueError(
                    f"stability finalization changed previewed {field}: "
                    f"expected={expected.get(field)!r} actual={result.get(field)!r}"
                )
    print(
        "stability state finalized "
        f"observation_id={observation_id} applied={result.get('observation_applied')} "
        f"tracked={result.get('tracked_urls_after')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
