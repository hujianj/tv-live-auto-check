#!/usr/bin/env python3
"""Capture bounded, strict local playback evidence for temporary ordering hints."""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--playlist', type=Path, default=ROOT / 'ku9-live.txt')
    parser.add_argument('--output', type=Path, default=ROOT / 'config/home-priority.json')
    parser.add_argument('--core-only', action='store_true')
    parser.add_argument('--workers', type=int, default=6)
    parser.add_argument('--per-host', type=int, default=2)
    parser.add_argument('--timeout', type=int, default=12)
    parser.add_argument('--max-age-hours', type=int, default=48)
    args = parser.parse_args(argv)
    if not (1 <= args.workers <= 24 and 1 <= args.per_host <= 3
            and 1 <= args.timeout <= 30 and 1 <= args.max_age_hours <= 720):
        parser.error('workers 1..24, per-host 1..3, timeout 1..30, max-age-hours 1..720')
    os.environ['IPTV_CHECK_WORKERS_PER_HOST'] = str(args.per_host)
    from media_decode import decoder_preflight
    from probe_scheduler import iter_probe_results
    from recheck_published import parse_tv_txt
    from verify_sources import Candidate, check_candidate
    from validate_playlist import validate_text
    from url_utils import redact_text

    validation = validate_text(args.playlist.read_text(encoding='utf-8-sig'))
    if validation['rows'] < 1:
        raise ValueError('playlist validation failed; no snapshot written')
    decoder_preflight()
    _, rows = parse_tv_txt(args.playlist)
    if args.core_only:
        rows = [r for r in rows if r.group in {'央视频道', '卫视频道'}]
    unique = {row.url: row for row in rows}
    if not unique:
        raise ValueError('no candidates; previous snapshot preserved')
    generated = datetime.now(timezone.utc)
    jobs = [(Candidate('local_diagnostic', r.group, r.name, r.url),
             dict(timeout=args.timeout, require_video=True, require_decode=True,
                  require_progress=r.group in {'央视频道', '卫视频道', '地方频道'}))
            for r in unique.values()]
    quality = {}
    for cand, result in iter_probe_results(jobs, check_candidate,
                                         workers=args.workers, per_host=args.per_host):
        quality[cand.url] = {field: getattr(result, field) for field in
                            ('ok', 'checked_at', 'decoded_frames',
                             'media_realtime_ratio', 'media_measurement')}
        print(f'{len(quality)}/{len(jobs)} {cand.name}: ok={result.ok} '
              f'margin={result.media_realtime_ratio} {redact_text(result.detail)[:160]}', flush=True)
    snapshot = dict(enabled=True, max_age_hours=args.max_age_hours, bonus=0, penalty=0,
                    home_ok_urls=[], home_failed_urls=[], home_quality=quality,
                    generated_at_utc=generated.isoformat(),
                    expires_at_utc=(generated + timedelta(hours=args.max_age_hours)).isoformat(),
                    generated_from='strict local published playlist probes',
                    network_scope='current local computer; not television',
                    checked_unique_urls=len(quality))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_name(args.output.name + '.tmp')
    temporary.write_bytes((json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    temporary.replace(args.output)
    print(f'Saved {len(quality)} observations: {args.output}; failures only affect ordering.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
