"""Regression tests for playback ranking, independent backups and recovery."""
from datetime import datetime, timedelta, timezone
from unittest import mock

import curate_ku9 as curate
import recheck_published as recheck
import stability
import verify_sources as verify
from playback_quality import playback_rank, prefer_independent_hosts, redundancy_summary
from source_config import SourceSpec
from probe_scheduler import iter_probe_results


def test_segment_measurement():
    transfer = dict(bytes=524288, limit=524288, content_length=1048576,
                    connect_seconds=0.1, body_seconds=0.2, status=200, encoded=False)
    measured = verify.segment_transfer_quality(transfer, 4)
    assert measured['measurement'] == 'partial_segment_estimate'
    assert measured['ratio'] == 8.0
    assert verify.segment_transfer_quality({**transfer, 'content_length': 0}, 4) is None
    assert verify.segment_transfer_quality(transfer, None) is None
    assert verify.segment_transfer_quality({**transfer, 'encoded': True}, 4) is None
    complete = verify.segment_transfer_quality({**transfer, 'bytes': 400000, 'content_length': 0}, 4)
    assert complete['measurement'] == 'complete_segment'
    manifest = verify.parse_hls_manifest('#EXTM3U\n#EXTINF:4.5,\na.ts\n#EXTINF:bad,\nb.ts\n', 'https://unit.test/live.m3u8')
    assert manifest.segment_durations == {'https://unit.test/a.ts': 4.5}


def test_quality_before_source_and_total_duration():
    cand = verify.Candidate('unit', '央视频道', 'CCTV-1', 'https://unit.test/a.m3u8')
    good = verify.CheckResult(cand, True, 'decoded', elapsed_seconds=40, decoded_frames=3, media_realtime_ratio=4)
    slow = verify.CheckResult(cand, True, 'decoded', elapsed_seconds=1, decoded_frames=3, media_realtime_ratio=0.5)
    unknown = verify.CheckResult(cand, True, 'decoded', decoded_frames=3)
    assert playback_rank(good, cand.url, (0, 20, 'other'), {}) < playback_rank(slow, cand.url, (-200, 20, 'zbds'), {})
    assert playback_rank(unknown, cand.url, (0, 20, 'other'), {}) < playback_rank(slow, cand.url, (-200, 20, 'zbds'), {})
    assert playback_rank(good, cand.url, (-200, 20, 'zbds'), {}) < playback_rank(good, cand.url, (0, 20, 'other'), {})


def test_independent_hosts_and_limit():
    rows = [recheck.Row('央视频道', 'CCTV-1', u) for u in (
        'https://same.test/a.m3u8', 'http://same.test:888/a.m3u8', 'https://other.test/a.m3u8')]
    assert prefer_independent_hosts(rows, 2) == [rows[0], rows[2]]
    results = {row.url: verify.CheckResult(verify.Candidate('unit', row.group, row.name, row.url), True, 'decoded',
                                        decoded_frames=3, media_realtime_ratio=4) for row in rows}
    with mock.patch.object(recheck, 'per_channel_limit', return_value=2), \
         mock.patch.object(recheck, 'url_score', return_value=(0, 0, 'unit')):
        selected = recheck.limit_verified_backups(rows, results, {})
    assert len(selected) == 2 and rows[2] in selected
    assert sum(row in selected for row in rows[:2]) == 1
    assert redundancy_summary(selected)['channels_with_independent_host_backups'] == 1
    results[rows[2].url].decoded_frames = 0
    try:
        recheck.limit_verified_backups(rows, results, {})
    except ValueError:
        pass
    else:
        raise AssertionError('unverified backup must be refused')


def test_history_recovery_policy_and_age():
    url = 'https://unit.test/cctv1.m3u8'
    now = datetime.now(timezone.utc)
    entry = dict(ok=3, fail=1, streak_fail=1, last_status='fail', last_name='CCTV-1',
                 last_source='unit', last_success_at=now.isoformat())
    approved = SourceSpec('unit', 'https://unit.test/list.txt', True, rights_status='approved')
    pending = SourceSpec('unit', 'https://unit.test/list.txt', True, rights_status='pending')
    with mock.patch.object(curate, 'git_show_text', return_value=''), \
         mock.patch.object(curate, 'STABILITY_HISTORY', {'urls': {url: entry}}), \
         mock.patch.object(curate, 'load_source_specs', return_value=[approved]):
        assert [row[2] for row in curate.historical_fallback_rows()] == [url]
        with mock.patch.object(curate, 'load_source_specs', return_value=[pending]):
            assert curate.historical_fallback_rows() == []
        entry['last_success_at'] = (now - timedelta(days=40)).isoformat()
        assert curate.historical_fallback_rows() == []
        entry['last_success_at'] = now.isoformat()
        entry['streak_fail'] = 3
        assert curate.historical_fallback_rows() == []
        entry['streak_fail'] = 1
        del entry['last_success_at']
        entry['last_seen'] = now.date().isoformat()
        assert [row[2] for row in curate.historical_fallback_rows()] == [url]


def test_success_timestamp_survives_failure():
    url = 'https://unit.test/cctv1.m3u8'
    rows = [recheck.Row('央视频道', 'CCTV-1', url)]
    observation = stability.build_observation(rows, {}, {}, 'quality-test:ok')
    history, _ = stability._apply_observation(stability.empty_history(), observation)
    stamp = history['urls'][url]['last_success_at']
    failure = stability.build_observation(rows, {url: 'timeout'}, {}, 'quality-test:fail')
    history, _ = stability._apply_observation(history, failure)
    assert history['urls'][url]['last_success_at'] == stamp
    assert history['urls'][url]['last_status'] == 'fail'


def test_retry_does_not_restore_aggressive_media_concurrency():
    # The retry profile used to silently undo the reduced media-probe caps.
    # A network failure must not cause a larger burst against the same server.
    from run_maintenance import ENV_DEFAULTS, load_config
    retry = load_config()['conservative_retry_env']
    for key in ('IPTV_PUBLISHED_RECHECK_WORKERS', 'IPTV_PUBLISHED_WORKERS_PER_HOST',
                'IPTV_PUBLISHED_REFILL_WORKERS', 'IPTV_PUBLISHED_FINAL_RETRY_WORKERS'):
        assert 0 < int(retry[key]) <= int(ENV_DEFAULTS[key]), key


def test_retry_preserves_all_media_evidence():
    row = recheck.Row('央视频道', 'CCTV-9', 'https://unit.test/a.m3u8')
    original = verify.Candidate('unit', row.group, row.name, row.url)
    for success in (True, False):
        result = verify.CheckResult(original, False, 'first timeout')
        retried = verify.CheckResult(original, success, 'retry media', 5, '2026-10-29T00:00:00Z',
                                     9, 4.5, 524288, 0.4, 'complete_segment')
        results = {row.url: result}
        recheck.retry_failed_final_urls({row.url: row}, results, {row.url},
            attempts=1, checker=lambda *_args, **_kwargs: retried)
        actual = results[row.url]
        assert actual.cand is original and actual.ok is success
        for field in ('elapsed_seconds', 'checked_at', 'decoded_frames', 'media_realtime_ratio',
                      'media_sample_bytes', 'media_transfer_seconds', 'media_measurement'):
            assert getattr(actual, field) == getattr(retried, field), field
    # A retry may have measured media but fail the decode gate; never accept it.
    retried.ok, retried.decoded_frames = True, 0
    results = {row.url: verify.CheckResult(original, False, 'first timeout')}
    recheck.retry_failed_final_urls({row.url: row}, results, {row.url},
        attempts=1, checker=lambda *_args, **_kwargs: retried)
    assert not results[row.url].ok


def test_host_scheduler_limits_fairness_and_complete_coverage():
    from collections import Counter
    import threading
    import time
    from urllib.parse import urlsplit
    active, peaks, started = Counter(), Counter(), []
    lock = threading.Lock()
    # Alternate schemes/ports of one host still consume a single host quota.
    candidates = [verify.Candidate('unit', '地方频道', f'台{i}',
                  f'{"https" if i % 2 else "http"}://same.test:{8000+i}/a.m3u8') for i in range(8)]
    candidates += [verify.Candidate('unit', '地方频道', f'其他{i}', f'https://other{i}.test/a.m3u8') for i in range(4)]

    def checker(cand, **kwargs):
        assert kwargs == {'require_decode': True}
        host = urlsplit(cand.url).hostname
        with lock:
            active[host] += 1
            active['total'] += 1
            peaks[host] = max(peaks[host], active[host])
            peaks['total'] = max(peaks['total'], active['total'])
            started.append(cand.url)
        time.sleep(0.01)
        with lock:
            active[host] -= 1
            active['total'] -= 1
        return verify.CheckResult(cand, True, 'decoded', decoded_frames=3)

    results = list(iter_probe_results([(c, {'require_decode': True}) for c in candidates],
                   checker, workers=4, per_host=2))
    assert peaks['same.test'] <= 2 and peaks['total'] <= 4
    assert any('other' in url for url in started[:4]), 'slow host must not monopolize admission'
    assert Counter(c.url for c, _ in results) == Counter(c.url for c in candidates)
    assert len(results) == len(candidates) and all(r.ok for _, r in results)
    assert list(iter_probe_results([], checker, workers=0, per_host=0)) == []


def test_host_scheduler_isolates_probe_exception():
    candidates = [verify.Candidate('unit', '地方频道', str(i), f'https://unit.test/{i}') for i in range(3)]
    def checker(cand):
        if cand.name == '1':
            raise RuntimeError('probe broke')
        return verify.CheckResult(cand, True, 'decoded', decoded_frames=3)
    results = dict((cand.name, result) for cand, result in iter_probe_results(
                   [(cand, {}) for cand in candidates], checker, workers=2, per_host=1))
    assert len(results) == 3 and results['0'].ok and results['2'].ok
    assert not results['1'].ok and 'probe exception' in results['1'].detail


def run_tests():
    for test in (test_segment_measurement, test_quality_before_source_and_total_duration,
                 test_independent_hosts_and_limit, test_history_recovery_policy_and_age,
                 test_success_timestamp_survives_failure,
                 test_retry_does_not_restore_aggressive_media_concurrency,
                 test_retry_preserves_all_media_evidence,
                 test_host_scheduler_limits_fairness_and_complete_coverage,
                 test_host_scheduler_isolates_probe_exception):
        test()
        print(f'OK {test.__name__}')


if __name__ == '__main__':
    run_tests()
