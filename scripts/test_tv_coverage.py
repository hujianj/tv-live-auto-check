"""Availability mode and separate TV manual-review coverage regression tests."""
import hashlib
import json
from pathlib import Path
import tempfile
from unittest import mock

import tv_coverage as tv
import recheck_published as recheck
import verify_sources as verify
from playback_quality import playback_rank
from source_config import SourceSpec
from validate_playlist import validate_text, validate_m3u_text


def test_availability_keeps_every_decoded_backup_and_ignores_speed():
    rows = [recheck.Row('央视频道', 'CCTV-1', f'https://unit.test/{i}.m3u8') for i in range(12)]
    results = {r.url: verify.CheckResult(verify.Candidate('unit', r.group, r.name, r.url), True,
                       'decoded', elapsed_seconds=i + 1, decoded_frames=3,
                       media_realtime_ratio=0.01 if i % 2 else 20) for i, r in enumerate(rows)}
    with mock.patch('playback_quality.load_quality', return_value={'playback_selection': {'mode': 'availability'}}), \
         mock.patch.object(recheck, 'load_quality', return_value={'playback_selection': {'mode': 'availability'}}), \
         mock.patch.object(recheck, 'per_channel_limit', return_value=2), \
         mock.patch.object(recheck, 'url_score', return_value=(0, 0, 'unit')):
        assert set(recheck.limit_verified_backups(rows, results, {})) == set(rows)
        slow, fast = results[rows[1].url], results[rows[0].url]
        snapshot = {'enabled': True, '_active': True, '_fresh': True, 'home_quality': {rows[1].url: {'ok': False}}}
        assert playback_rank(slow, rows[1].url, (-200, 0, 'zbds'), {}, snapshot) < playback_rank(fast, rows[0].url, (0, 0, 'unit'), {})
        results[rows[0].url].decoded_frames = 0
        try:
            recheck.limit_verified_backups(rows, results, {})
        except ValueError:
            pass
        else:
            raise AssertionError('availability is not permission to accept undecoded media')


def test_core_failure_adds_all_real_candidates_but_never_to_success():
    strict = [tv.TVRow('央视频道', 'CCTV-1', 'https://unit.test/1.m3u8'),
              tv.TVRow('央视频道', 'CCTV-4欧洲', 'https://unit.test/europe.m3u8')]
    records = [dict(group='卫视频道', name='吉林卫视', url=f'https://unit.test/jilin{i}.m3u8', source='unit',
                    checked_at='2026-10-29T01:00:00Z', check_ok=False, check_detail='timeout') for i in range(8)]
    records += [dict(group='央视频道', name=n, url=u, source='unit', checked_at='', check_ok=False, check_detail='failed')
                for n, u in [('CCTV-1','https://unit.test/failed1.m3u8'),('CCTV-4','https://unit.test/4.m3u8')]]
    records += [dict(group='影视剧场', name='电影频道', url='https://unit.test/movie', source='unit', checked_at='', check_ok=False, check_detail='failed')]
    rows, report = tv.assemble(strict, records, '2026-10-29T01:00:00Z')
    assert report['verified_lines'] == 2 and report['review_lines'] == 9
    assert len([r for r in rows if r.name == '吉林卫视']) == 8
    assert all(r.url != 'https://unit.test/failed1.m3u8' for r in rows)
    assert 'CCTV-4' not in report['missing_required_channels']
    assert 'CCTV-2' in report['missing_required_channels']
    assert all(item['status'] == 'pending_tv_review' for item in report['review_rows'])
    txt, m3u = tv.render(rows, report)
    validate_text(txt, require_categories=True)
    validate_m3u_text(m3u, require_categories=True)
    assert m3u.count('x-check-status="pending_tv_review"') == 9
    assert m3u.count('x-check-status="verified"') == 2
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root/'config').mkdir()
        (root/'config/sources.json').write_text(json.dumps([dict(name='unit', url='https://unit.test/list', enabled=True,
                                                   rights_status='approved', terms_url='https://unit.test/terms', reviewed_at='2026-10-29', permission_scope='test_fixture')]), encoding='utf-8')
        strict_txt, _ = tv.render(strict, {'review_rows': []})
        for name, data in [('live-curated.txt',strict_txt), ('ku9-live.txt',txt), ('tv-coverage.m3u',m3u)]:
            (root/name).write_text(data, encoding='utf-8', newline='\n')
        (root/'tv-review-report.json').write_text(json.dumps(report), encoding='utf-8')
        counts = {k:v for k,v in report.items() if k not in {'review_rows','excluded_candidate_rows'}}
        (root/'full-check-summary.json').write_text(json.dumps({'tv_coverage':counts}), encoding='utf-8')
        assert tv.validate_tv_coverage(root)['status'] == 'ok'
        (root/'ku9-live.txt').write_text(txt.replace('CCTV-1,','CCTV-2,',1), encoding='utf-8')
        try:
            tv.validate_tv_coverage(root)
        except ValueError:
            pass
        else:
            raise AssertionError('tampered TV coverage must fail')


def test_manual_candidates_keep_source_and_protection_boundaries():
    specs = {'unit': SourceSpec('unit','https://unit.test/list',True,rights_status='approved'),
             'pending':SourceSpec('pending','https://unit.test/other',True,rights_status='pending')}
    def row(name, url, source='unit', detail='timeout'):
        return dict(name=name, group='', url=url, source=source, ok='False', detail=detail, checked_at='')
    records = [row('吉林卫视','https://unit.test/jilin'),
               row('CCTV-1','http://192.168.1.1/live'),
               row('CCTV-2','https://unit.test/drm?a=1&a=1'),
               row('CCTV-3','https://unit.test/protected?token=secret'),
               row('CCTV-4','https://unit.test/pending','pending'),
               row('CGTN English','https://unit.test/foreign'),
               row('CCTV-7','https://unit.test/ambiguous'), row('湖南卫视','https://unit.test/ambiguous')]
    probes = [{**row('CCTV-2','https://unit.test/drm?a=1'), 'phase':'published', 'detail':'encrypted/DRM HLS excluded; no key or license requested'}]
    candidates, excluded = tv.collect_candidates(records, probes, specs, [])
    assert [item['name'] for item in candidates] == ['吉林卫视'], candidates
    assert excluded['network_or_protection_policy'] >= 2
    assert candidates[0]['check_ok'] is False


def test_publication_endpoint_checks_its_own_file_and_preflights_all():
    import check_publication_endpoints as endpoints
    config = {'authoritative_raw_file':'live-curated.txt'}
    matrix = [endpoints.Endpoint('raw','https://raw.test/live',1,hard_raw=True,path='live-curated.txt'),
              endpoints.Endpoint('tv','https://cdn.test/live',1,television_compatible=True,required_primary=True,path='ku9-live.txt')]
    raw = '央视频道,#genre#\nCCTV-1,https://unit.test/1\n'.encode()
    mixed = raw + 'CCTV-2,https://unit.test/2\n'.encode()
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root/'live-curated.txt').write_bytes(raw)
        (root/'ku9-live.txt').write_bytes(mixed)
        args=['--repo','unit/repo','--expected',str(root/'live-curated.txt'), '--report',str(root/'report.md'), '--json',str(root/'report.json'),'--retry-wait','0']
        def fetch(url, *_args):
            return (raw if 'raw.test' in url else mixed), {'status_code':200}
        with mock.patch.object(endpoints,'load_publication_config',return_value=config), \
             mock.patch.object(endpoints,'endpoint_matrix',return_value=matrix), \
             mock.patch.object(endpoints,'fetch_bytes',side_effect=fetch) as network:
            assert endpoints.main(args) == 0
            report=json.loads((root/'report.json').read_text())
            assert report['endpoints'][0]['sha256'] != report['endpoints'][1]['sha256']
            assert all(item['sha256'] == item['expected_sha256'] for item in report['endpoints'])
            assert network.call_count == 2
            (root/'ku9-live.txt').write_text('bad,not-url', encoding='utf-8')
            network.reset_mock()
            assert endpoints.main(args) == 2
            network.assert_not_called()


def run_tests():
    for test in (test_availability_keeps_every_decoded_backup_and_ignores_speed,
                 test_core_failure_adds_all_real_candidates_but_never_to_success,
                 test_manual_candidates_keep_source_and_protection_boundaries,
                 test_publication_endpoint_checks_its_own_file_and_preflights_all):
        test()
        print(f'OK {test.__name__}')

if __name__ == '__main__':
    run_tests()
