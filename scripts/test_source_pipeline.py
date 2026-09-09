"""Offline regressions for data adapters, publication scope and probe retries."""
import json
import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from channel_scope import domestic_chinese_issue
from source_adapters import parse
from source_config import SourceSpec
from scan_checkpoint import ScanCheckpoint
from url_utils import normalize_stream_url, publishable_url_issue
import verify_sources as verify


def write_csv_fixture(root, filename, rows):
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with (root / filename).open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def prepare_export_fixture(root):
    now = datetime.now(timezone.utc).isoformat()
    (root / 'config').mkdir()
    config = root / 'config/sources.json'
    config.write_text(json.dumps([{
        'name': name, 'url': f'https://catalog.test/{name}', 'enabled': True,
        'rights_status': 'approved', 'terms_url': 'https://catalog.test/terms',
        'reviewed_at': '2026-09-07', 'permission_scope': 'synthetic unit test fixture only',
    } for name in ('fixture', 'backup')]), encoding='utf-8')
    summary = {'generated_utc': now, 'source_config_sha256': hashlib.sha256(config.read_bytes()).hexdigest()}
    (root / 'full-check-summary.json').write_text(json.dumps(summary), encoding='utf-8')
    return now


class SourcePipelineTests(unittest.TestCase):
    def test_domestic_chinese_and_specific_hk_channels(self):
        for name in ("CCTV-1", "CCTV-17", "CCTV-5+", "CETV-1", "\u8fbd\u5b81\u536b\u89c6", "\u6cb3\u5317\u536b\u89c6", "\u7fe1\u7fe0\u53f0", "TVB Jade", "TVBS", "RTHK31"):
            with self.subTest(name=name):
                self.assertEqual(domestic_chinese_issue(name), "")
        for name in ("BBC", "CNN", "CGTN", "CCTV-9English", "TVB Pearl", "ViuTVsix", "RTHK34", "TVB", "\u660e\u73e0\u53f0", "\u7f8e\u56fd\u4e2d\u6587\u7535\u89c6", "\u65b0\u4f20\u5a92\u516b\u9891\u9053"):
            with self.subTest(name=name):
                self.assertTrue(domestic_chinese_issue(name))

    def test_metadata_overrules_chinese_title(self):
        self.assertTrue(domestic_chinese_issue("\u4e2d\u6587\u65b0\u95fb", tvg_id="ChineseNews.us"))
        self.assertTrue(domestic_chinese_issue("\u4e2d\u6587\u65b0\u95fb", country="sg", language="zho"))
        self.assertTrue(domestic_chinese_issue("\u9999\u6e2f\u7535\u89c6", country="hk", language="eng"))
        self.assertFalse(domestic_chinese_issue("\u53f0\u89c6\u65b0\u95fb", country="tw", language="cmn"))

    def test_foreign_movie_channels_are_not_chinese_by_title_alone(self):
        for name in ('欧美大片1', '欧美大片2', '歐美大片', '日韩影院', '原声电影'):
            with self.subTest(name=name):
                self.assertTrue(domestic_chinese_issue(name))
        self.assertFalse(domestic_chinese_issue('CCTV-6电影'))

    def test_country_names_are_not_split_into_letter_pairs(self):
        for country in ("China", "CHN", "Hong Kong", "Macau", "Taiwan", "cn hk", "China;Hong Kong", "\u4e2d\u56fd"):
            with self.subTest(country=country):
                self.assertFalse(domestic_chinese_issue("\u4e2d\u6587\u65b0\u95fb", country=country))
        for country in ("United States", "Singapore", "cn;us", "China;Canada", "unknown", "chinanews"):
            with self.subTest(country=country):
                self.assertTrue(domestic_chinese_issue("\u4e2d\u6587\u65b0\u95fb", country=country))
        self.assertTrue(domestic_chinese_issue("\u4e2d\u6587\u65b0\u95fb", country="China", tvg_id="News.us"))

    def test_xml_and_json_preserve_country_and_language(self):
        documents = [
            '<channels><channel name="News" url="https://tv.test/live" country="Singapore" language="zho"/></channels>',
            json.dumps({"channels": [{"name": "News", "url": "https://tv.test/live", "country": ["cn", "us"], "language": ["zho"]}]}),
        ]
        for document in documents:
            channel = parse(document)[0]
            self.assertTrue(domestic_chinese_issue("\u4e2d\u6587\u65b0\u95fb", country=channel.country, language=channel.language))

    def test_quoted_commas_metadata_and_backups(self):
        text = '#EXTM3U\n#EXTINF:-1 tvg-id="CCTV1.cn" tvg-logo="https://img.test/w_400,h_500.png" group-title="News",CCTV-1\nhttps://a.test/live.m3u8;https://b.test/live.m3u8\n'
        channels = parse(text)
        self.assertEqual([c.name for c in channels], ["CCTV-1", "CCTV-1"])
        self.assertEqual(channels[0].tvg_id, "CCTV1.cn")
        self.assertIn("w_400,h_500", channels[0].tvg_logo)

    def test_txt_json_xml(self):
        documents = [
            ('CCTV-1,https://tv.test/live.m3u8', "txt"),
            (json.dumps({"channels": [{"name": "CCTV-1", "url": "https://tv.test/live.m3u8"}]}), "json"),
            ('<channels><channel name="CCTV-1" url="https://tv.test/live.m3u8"/></channels>', "xml"),
        ]
        for text, format in documents:
            self.assertEqual(parse(text, format)[0].name, "CCTV-1")

    def test_non_playlists_and_protected_entries(self):
        self.assertEqual(parse('#EXTM3U\n#EXT-X-TARGETDURATION:6\n#EXTINF:6,\nsegment.ts'), [])
        self.assertEqual(parse('#EXTM3U\n#EXTINF:-1,CCTV-1\n#KODIPROP:inputstream.adaptive.license_key=x\nhttps://tv.test/a.m3u8'), [])
        self.assertEqual(parse(json.dumps({"headers": {"Cookie": "x"}, "channels": [{"name": "CCTV-1", "url": "https://tv.test/a"}]})), [])
        for text in ('<html>denied</html>', '<!DOCTYPE channels [<!ENTITY x "x">]><channels/>'):
            with self.assertRaises(ValueError):
                parse(text)

    def test_permission_and_scope_before_media_check(self):
        candidates = [verify.Candidate("s", "", "CCTV-1", "https://a.test/1"),
                      verify.Candidate("s", "", "BBC", "https://a.test/2")]
        pending = SourceSpec("s", "https://catalog.test/list", True)
        approved = SourceSpec("s", "https://catalog.test/list", True, rights_status="approved")
        self.assertEqual(verify.eligible_candidates(candidates, pending)[0], [])
        kept, excluded = verify.eligible_candidates(candidates, approved)
        self.assertEqual([c.name for c in kept], ["CCTV-1"])
        self.assertEqual(sum(excluded.values()), 1)

    def test_failed_source_and_catalog_are_not_playable(self):
        spec = SourceSpec("s", "https://catalog.test/list", True, timeout_seconds=9)
        with patch.object(verify, "fetch_url", side_effect=TimeoutError("timed out")):
            status, channels = verify.fetch_source(spec)
        self.assertFalse(status.ok)
        self.assertEqual(channels, [])
        catalog = SourceSpec("s", "https://catalog.test/README.md", True, format="catalog")
        with patch.object(verify, "fetch_url", return_value=(200, "text/plain", b"https://catalog.test/list.m3u", catalog.url, False)):
            status, channels = verify.fetch_source(catalog)
        self.assertTrue(status.ok)
        self.assertEqual(status.parsed, 0)
        self.assertEqual(channels, [])
        self.assertEqual(status.discovered_links, ["https://catalog.test/list.m3u"])

    def test_query_safety_does_not_mutate_signed_inputs(self):
        base = "https://tv.test/live.m3u8"
        self.assertEqual(normalize_stream_url(base + "?id=1&id=1"), base + "?id=1")
        self.assertTrue(publishable_url_issue(base + "?id=1&id=2"))
        for key in ("token", "auth_key", "signature", "expires", "wsSecret", "x-amz-signature"):
            self.assertTrue(publishable_url_issue(base + "?" + key + "=x"))
        self.assertFalse(publishable_url_issue(base + "?design=one&channel=1"))
        self.assertTrue(publishable_url_issue(base + "|User-Agent=Player"))
        self.assertFalse(publishable_url_issue(base + "?key=txiptv"))
        self.assertTrue(publishable_url_issue(base + "?key=7ca9d5b4ce36f50a230ecd83ea7704b3"))
        self.assertTrue(publishable_url_issue(base + "?key=Kx4Jn8UsFz5Pr9BvTh2Ma6Wd"))
        self.assertTrue(publishable_url_issue(base + "?api_key=x"))
        self.assertTrue(publishable_url_issue(base + "?key=txiptv&key=other"))

    def test_guard_counts_channels_not_duplicate_backups(self):
        import guard_publish as guard
        rows = [("\u592e\u89c6\u9891\u9053", "CCTV-1", f"https://tv.test/{i}") for i in range(2000)]
        coverage = guard.channel_coverage(rows)
        self.assertEqual(coverage["total"], 1)
        self.assertTrue(guard.coverage_failures(coverage, {}))
        same_coverage = {"total": 29, "groups": {"\u592e\u89c6\u9891\u9053": 18, "\u536b\u89c6\u9891\u9053": 10, "\u5730\u65b9\u9891\u9053": 1}}
        self.assertEqual(guard.coverage_failures(same_coverage, same_coverage), [])
        self.assertTrue(guard.coverage_failures(same_coverage, {"total": 100, "groups": {}}))

    def test_catalog_and_pending_source_health_are_nonblocking(self):
        import guard_publish as guard
        specs = {
            "pending": SourceSpec("pending", "https://catalog.test/list", True),
            "docs": SourceSpec("docs", "https://catalog.test/README.md", True, format="catalog"),
        }
        health = guard.classify_source_health([
            {"name": "pending", "fetch_ok": "False", "parsed": "0"},
            {"name": "docs", "fetch_ok": "True", "parsed": "0"},
        ], specs)
        self.assertEqual(health["enabled_failed"], [])
        self.assertEqual(health["enabled_zero_parsed"], [])
        self.assertEqual(health["candidate_failed"], ["pending"])
        self.assertEqual(health["candidate_zero_parsed"], [])

    def test_observed_station_alias_and_regional_classification(self):
        from channel_identity import canonical_channel_key
        from curate_ku9 import classify, clean_name
        self.assertEqual(canonical_channel_key("BRTV\u5317\u4eac\u536b\u89c6(1080p)"), canonical_channel_key("\u5317\u4eac\u536b\u89c6"))
        self.assertEqual(clean_name("BRTV\u5317\u4eac\u536b\u89c6(1080p)"), "\u5317\u4eac\u536b\u89c6")
        self.assertEqual(classify("\u4f59\u59da\u65b0\u95fb\u7efc\u5408(576p)", "", "s"), "\u5730\u65b9\u9891\u9053")
        self.assertEqual(classify("\u798f\u5dde\u5e7f\u64ad\u7535\u89c6\u53f0\u65b0\u95fb\u7efc\u5408\u9891\u9053(FZTV-1)(1080p)", "", "s"), "\u5730\u65b9\u9891\u9053")
        approved = SourceSpec("s", "https://catalog.test/list", True, rights_status="approved")
        channel = verify.Candidate("s", "General", "DaliTV(\u5927\u7acb\u96fb\u8996\u53f0)(720p)", "https://tv.test/live", "DaliTV.tw@SD")
        kept, _excluded = verify.eligible_candidates([channel], approved)
        self.assertEqual(kept[0].group, "\u6e2f\u6fb3\u53f0\u9891\u9053")

    def test_interlaced_resolution_preserves_cctv_identity_end_to_end(self):
        from channel_identity import canonical_channel_key
        from curate_ku9 import prepare_curated_row
        spec = SourceSpec('fixture', 'https://catalog.test/list', True, rights_status='approved')
        for resolution in ('576i', '1080i', '1080p'):
            text = f'#EXTM3U\n#EXTINF:-1 tvg-id="CCTV9.cn@SD",CCTV-9 ({resolution})\nhttps://tv.test/live\n'
            candidate = verify.parse_source_candidates(text, spec.name, 'm3u')[0]
            self.assertFalse(domestic_chinese_issue(f'CCTV-9 ({resolution})'))
            kept, _excluded = verify.eligible_candidates([candidate], spec)
            self.assertEqual(len(kept), 1)
            row, reason, _detail = prepare_curated_row(kept[0].name, kept[0].url, kept[0].group, spec.name)
            self.assertEqual(reason, '')
            self.assertEqual(row[0], '\u592e\u89c6\u9891\u9053')
            self.assertEqual(canonical_channel_key(row[1]), 'CCTV-9')
        self.assertNotEqual(canonical_channel_key('CCTV-4K'), 'CCTV-4')
        self.assertTrue(domestic_chinese_issue('CCTV-9 English (576i)'))

    def test_known_cctv_descriptive_aliases_have_one_display_identity(self):
        from curate_ku9 import clean_name
        from audit_coverage import build_coverage
        names = ['CCTV-4\u4e2d\u6587\u56fd\u9645', 'CCTV-16\u5965\u6797\u5339\u514b', 'CCTV-5+\u4f53\u80b2\u8d5b\u4e8b']
        expected = ['CCTV-4', 'CCTV-16', 'CCTV-5+']
        self.assertEqual([clean_name(name) for name in names], expected)
        rows = [('\u592e\u89c6\u9891\u9053', clean_name(name), f'https://tv.test/{index}') for index, name in enumerate(names)]
        self.assertEqual(build_coverage(rows, {'required_cctv': expected})['missing_cctv'], [])
        self.assertEqual(clean_name('CCTV-4K'), 'CCTV-4K')
        self.assertEqual(clean_name('CCTV-4(RTHK33)'), 'CCTV-4(RTHK33)')

    def test_domestic_english_labels_are_normalized_before_scope_filter(self):
        spec = SourceSpec('iptv_org_cn', 'https://catalog.test/list', True, rights_status='approved')
        pairs = [('AnhuiTV.cn@SD', 'Anhui TV (1080p)', '\u5b89\u5fbd\u536b\u89c6'),
                 ('HunanTV.cn@SD', 'Hunan TV (2160p)', '\u6e56\u5357\u536b\u89c6'),
                 ('BRTVKakuChildrensChannel.cn@SD', 'BRTV Kaku Childrens Channel', '\u5361\u9177\u5c11\u513f'),
                 ('HeilongjiangTV.cn@SD', '\u9ed1\u9f99\u6c5f (1080p)', '\u9ed1\u9f99\u6c5f\u536b\u89c6')]
        for tvg_id, name, expected in pairs:
            with self.subTest(name=name):
                candidate = verify.Candidate(spec.name, 'Undefined', name, 'https://tv.test/live', tvg_id)
                kept, excluded = verify.eligible_candidates([candidate], spec)
                self.assertEqual(excluded, {})
                self.assertEqual([row.name for row in kept], [expected])
                self.assertEqual(kept[0].url, candidate.url)

    def test_domestic_alias_does_not_override_negative_metadata_or_status(self):
        from dataclasses import replace
        from channel_scope import known_domestic_name
        spec = SourceSpec('iptv_org_cn', 'https://catalog.test/list', True, rights_status='approved')
        good = verify.Candidate(spec.name, 'Undefined', 'Anhui TV', 'https://tv.test/live', 'AnhuiTV.cn@SD')
        for change in ({'country': 'us'}, {'language': 'eng'}, {'tvg_id': 'AnhuiTV.us'},
                       {'name': 'Anhui TV English'}, {'name': 'Anhui TV [Geo-blocked]'},
                       {'name': 'Anhui TV [Not 24/7]'}, {'source': 'unreviewed'}):
            with self.subTest(change=change):
                self.assertEqual(verify.eligible_candidates([replace(good, **change)], spec)[0], [])
        self.assertEqual(known_domestic_name('Xinjiang TV 2', 'XinjiangTV2.cn', spec.name), 'Xinjiang TV 2')
        self.assertEqual(known_domestic_name('Ando TV', 'AndoTV.cn', spec.name), 'Ando TV')

    def test_cctv_descriptions_merge_only_the_correct_number(self):
        from channel_identity import aliases_are_compatible, canonical_channel_key
        from curate_ku9 import clean_name
        from audit_coverage import build_coverage
        self.assertEqual(clean_name('CCTV-9\u7eaa\u5f55(1080p)'), 'CCTV-9')
        self.assertEqual(clean_name('CCTV-15\u97f3\u4e50'), 'CCTV-15')
        self.assertTrue(aliases_are_compatible(['CCTV-9', 'CCTV-9\u7eaa\u5f55']))
        self.assertNotEqual(canonical_channel_key('CCTV-9\u97f3\u4e50'), 'CCTV-9')
        self.assertNotEqual(canonical_channel_key('CCTV-4\u4e2d\u6587\u56fd\u9645\uff08\u6b27\uff09'), 'CCTV-4')
        self.assertNotEqual(canonical_channel_key('CCTV-9 English'), 'CCTV-9')
        report = build_coverage([('g', 'CCTV-9\u7eaa\u5f55', 'https://tv.test/live')],
                                {'required_cctv': ['CCTV-9', 'CCTV-1']})
        self.assertEqual(report['missing_cctv'], ['CCTV-1'])
        self.assertEqual(report['status'], 'incomplete')
        self.assertEqual(report['covered_target_channels'], 1)

    def test_coverage_targets_include_all_requested_provincial_satellites(self):
        from playlist_config import load_rules
        targets = load_rules()['coverage']
        self.assertTrue({f'CCTV-{number}' for number in range(1, 18)} <= set(targets['required_cctv']))
        for name in ('\u9ed1\u9f99\u6c5f\u536b\u89c6', '\u56db\u5ddd\u536b\u89c6', '\u6e56\u5357\u536b\u89c6', '\u8fbd\u5b81\u536b\u89c6'):
            self.assertIn(name, targets['important_satellite'])
        self.assertEqual(len(targets['important_satellite']), len(set(targets['important_satellite'])))

    def test_source_approval_needs_valid_evidence_and_supported_adapter(self):
        from source_config import load_source_specs
        valid = {'name': 'fixture', 'url': 'https://catalog.test/list', 'enabled': True,
                 'rights_status': 'approved', 'terms_url': 'https://catalog.test/terms',
                 'reviewed_at': '2026-09-07', 'permission_scope': 'synthetic test fixture'}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sources.json'
            for change in ({'terms_url': 'javascript:x'}, {'terms_url': 'https://name:password@host.test'},
                           {'reviewed_at': 'yesterday'}, {'reviewed_at': '2026-02-31'},
                           {'permission_scope': '  '}, {'format': 'hls'}):
                path.write_text(json.dumps([dict(valid, **change)]), encoding='utf-8')
                with self.subTest(change=change), self.assertRaises(ValueError):
                    load_source_specs(path)

    def test_aborted_recheck_preserves_playlists_records_failure_and_restores_checkpoint(self):
        import recheck_published as recheck
        import run_maintenance as maintenance
        now = datetime.now(timezone.utc).isoformat()
        rows = [recheck.Row(group, name, f'https://tv.test/{number}') for number, (group, name) in enumerate([
            ('\u592e\u89c6\u9891\u9053', 'CCTV-1'), ('\u536b\u89c6\u9891\u9053', '\u6e56\u5357\u536b\u89c6'),
            ('\u5730\u65b9\u9891\u9053', '\u6e56\u5357\u7ecf\u89c6'),
        ], 1)]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in recheck.TXT_FILES:
                (root / name).write_text(recheck.render_txt([row.group for row in rows], rows), encoding='utf-8')
            (root / recheck.M3U_FILE).write_text(recheck.render_m3u(rows), encoding='utf-8')
            (root / recheck.SUMMARY_FILE).write_text('{"generated_utc":"' + now + '"}', encoding='utf-8')
            (root / recheck.CANDIDATE_POOL_FILE).write_text('selection_key,group,name,url,source,origin\n', encoding='utf-8')
            write_csv_fixture(root, recheck.SOURCE_MAP_FILE, [
                {'group': row.group, 'name': row.name, 'url': row.url, 'source': 'fixture'} for row in rows])
            original = {name: (root / name).read_bytes() for name in maintenance.CHECKPOINT_FILES}
            maintenance.save_curate_checkpoint(root)

            def checker(candidate, *_args, **kwargs):
                self.assertTrue(kwargs['require_decode'])
                return verify.CheckResult(candidate, not candidate.url.endswith('/2'), 'synthetic media result', 0.1, now, 3)

            retry = {'first_pass_failed_unique_urls': 1, 'attempted_unique_urls': 1,
                     'recovered_unique_urls': 0, 'still_failed_unique_urls': 1}
            with patch.object(recheck, 'ROOT', root), patch.object(recheck, 'MAX_WORKERS', 1), \
                    patch.object(recheck, 'check_candidate_resilient', side_effect=checker), \
                    patch.object(recheck, 'retry_failed_final_urls', return_value=retry), \
                    patch.object(recheck, 'coverage_is_required', return_value=True), \
                    patch.object(recheck, 'max_failed_url_ratio', return_value=0.25):
                self.assertEqual(recheck.main(), 1)
            full_summary = json.loads((root / recheck.SUMMARY_FILE).read_text(encoding='utf-8'))
            self.assertEqual(full_summary['strict_video_checked_unique'], 3)
            self.assertEqual(full_summary['strict_progress_checked_unique'], 3)
            summary = full_summary['published_recheck']
            self.assertEqual(summary['status'], 'aborted')
            self.assertFalse(summary['outputs_rewritten'])
            self.assertEqual((summary['before_rows'], summary['after_rows'], summary['candidate_after_rows']), (3, 3, 2))
            self.assertEqual(summary['removed_rows'], 0)
            self.assertEqual(summary['post_retry_failed_unique_urls'], 1)
            for name in (*recheck.TXT_FILES, recheck.M3U_FILE, recheck.SOURCE_MAP_FILE):
                self.assertEqual((root / name).read_bytes(), original[name])
            with (root / recheck.CSV_FILE).open(encoding='utf-8', newline='') as handle:
                results = list(csv.DictReader(handle))
            self.assertEqual([item['source'] for item in results], ['fixture'] * 3)
            self.assertEqual([item['ok'] for item in results], ['True', 'False', 'True'])
            self.assertFalse((root / recheck.PENDING_STABILITY_FILE).exists())
            evidence = maintenance.collect_attempt_evidence(root)['published_recheck']
            self.assertEqual(evidence['status'], 'aborted')
            self.assertEqual(evidence['candidate_after_rows'], 2)
            maintenance.restore_curate_checkpoint(root)
            self.assertEqual({name: (root / name).read_bytes() for name in original}, original)

    def test_available_policy_reports_missing_channels_but_preserves_quality_gates(self):
        from audit_quality import build_audit, build_family_audit
        from audit_coverage import build_coverage
        from playlist_config import load_rules
        from validate_playlist import validate_text
        rows = [('央视频道', 'CCTV-1', 'https://tv.test/1')]
        result, failures, warnings = build_audit(rows)
        self.assertEqual(result['status'], 'ok')
        self.assertFalse(failures)
        self.assertTrue(warnings)
        self.assertTrue(result['missing_satellite_quality'])
        family, failures = build_family_audit(rows)
        self.assertFalse(failures)
        self.assertTrue(family['warnings'])
        coverage = build_coverage(rows, load_rules()['coverage'])
        self.assertTrue(coverage['missing_satellite'])
        self.assertFalse(coverage['fail_on_missing_satellite'])
        validate_text('央视频道,#genre#\nCCTV-1,https://tv.test/1\n')
        self.assertTrue(build_audit([])[1])
        self.assertTrue(build_audit([('央视频道', 'CNN', 'https://tv.test/2')])[1])
        with self.assertRaises(ValueError):
            validate_text('央视频道,#genre#\ntvg-logo=bad,CCTV-1,https://tv.test/1\n')

    def test_final_backup_limits_preserve_every_distinct_channel_and_require_frames(self):
        import recheck_published as recheck
        from dataclasses import replace
        rows = [recheck.Row('央视频道', 'CCTV-1', f'https://tv.test/1/{i}') for i in range(12)]
        rows += [recheck.Row('影视剧场', f'中文剧场{i}', f'https://tv.test/movie/{i}') for i in range(220)]
        results = {row.url: verify.CheckResult(verify.Candidate('fixture', row.group, row.name, row.url),
                   True, 'synthetic frames', 0.1, '2026-09-09T00:00:00Z', 3) for row in rows}
        chosen = recheck.limit_verified_backups(rows, results, {})
        self.assertEqual(len({row.name for row in chosen}), 221)
        self.assertEqual(sum(row.name == 'CCTV-1' for row in chosen), recheck.per_channel_limit('央视频道', 'CCTV-1'))
        results[rows[0].url] = replace(results[rows[0].url], decoded_frames=0)
        with self.assertRaises(ValueError):
            recheck.limit_verified_backups(rows, results, {})

    def test_recheck_partial_empty_and_refill_policies_end_to_end(self):
        import recheck_published as recheck
        from dataclasses import replace
        now = datetime.now(timezone.utc).isoformat()
        rows = [recheck.Row('央视频道', f'CCTV-{i}', f'https://tv.test/{i}') for i in (1, 2)]
        backup = recheck.PoolCandidate(recheck.row_identity(rows[1])[1],
                   replace(rows[1], url='https://tv.test/backup'), 'fixture', 'current_scan')
        for mode in ('partial', 'empty', 'refill'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                for filename in recheck.TXT_FILES:
                    (root / filename).write_text(recheck.render_txt(['央视频道'], rows), encoding='utf-8')
                (root / recheck.SUMMARY_FILE).write_text(json.dumps({'generated_utc': now}), encoding='utf-8')
                (root / recheck.CANDIDATE_POOL_FILE).touch()
                original = (root / recheck.TXT_FILES[0]).read_bytes()
                def check(cand, *_args, **kwargs):
                    self.assertTrue(kwargs['require_decode'])
                    ok = mode != 'empty' and cand.url.endswith(('/1', '/backup'))
                    return verify.CheckResult(cand, ok, 'synthetic', 0.1, now, 3 if ok else 0)
                pool = [backup] if mode == 'refill' else []
                real_refill = recheck.refill_missing_rows
                def refill(*args):
                    return real_refill(*args, checker=check)
                retry = {'first_pass_failed_unique_urls': 2 if mode == 'empty' else 1,
                         'attempted_unique_urls': 0, 'recovered_unique_urls': 0,
                         'still_failed_unique_urls': 2 if mode == 'empty' else 1}
                with patch.object(recheck, 'ROOT', root), patch.object(recheck, 'MAX_WORKERS', 1), \
                     patch.object(recheck, 'load_candidate_pool', return_value=pool), \
                     patch.object(recheck, 'check_candidate_resilient', side_effect=check), \
                     patch.object(recheck, 'refill_missing_rows', side_effect=refill) as refiller, \
                     patch.object(recheck, 'retry_failed_final_urls', return_value=retry), \
                     patch.object(recheck, 'coverage_is_required', return_value=(mode == 'refill')):
                    self.assertEqual(recheck.main(), 1 if mode == 'empty' else 0)
                self.assertEqual(refiller.call_count, 1)
                summary = json.loads((root / recheck.SUMMARY_FILE).read_text(encoding='utf-8'))['published_recheck']
                if mode == 'empty':
                    self.assertEqual(summary['abort_reason'], 'no_verified_channels')
                    self.assertEqual((root / recheck.TXT_FILES[0]).read_bytes(), original)
                else:
                    self.assertEqual(summary['after_rows'], 2 if mode == 'refill' else 1)
                    self.assertEqual(summary['frame_decoded_unique_urls'], summary['after_rows'])
                    self.assertNotIn('https://tv.test/2', (root / recheck.TXT_FILES[0]).read_text(encoding='utf-8'))

    def test_bootstrap_uses_one_budget_and_reports_failure_before_media(self):
        import bootstrap_runtime as bootstrap
        with tempfile.TemporaryDirectory() as directory:
            elapsed = [0.0]
            calls = []
            def runner(command, **kwargs):
                calls.append((command, kwargs['timeout']))
                elapsed[0] += 80
            with patch.object(bootstrap.sys, 'platform', 'linux'):
                result = bootstrap.bootstrap(Path(directory), 100, runner=runner,
                         clock=lambda: elapsed[0], which=lambda _: None)
            self.assertEqual(result['status'], 'failed')
            self.assertEqual(result['failed_step'], 'python dependencies')
            self.assertEqual(len(calls), 2)
            self.assertLess(calls[1][1], calls[0][1])
            self.assertTrue(all(command[0] == 'timeout' for command, _ in calls))
            self.assertTrue((Path(directory) / 'bootstrap-report.json').is_file())

    def test_export_includes_broad_failures_without_losing_recheck_origins(self):
        from export_outputs import export_outputs
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            now = prepare_export_fixture(root)
            rows = [{'name': f'CCTV-{number}', 'url': f'https://tv.test/{number}', 'source': 'fixture',
                     'group': '\u592e\u89c6\u9891\u9053', 'ok': 'False' if number == 3 else 'True',
                     'detail': 'media' if number != 3 else 'connection timed out', 'checked_at': now} for number in (1, 2, 3, 4)]
            write_csv_fixture(root, 'stream_check_results.csv', rows)
            write_csv_fixture(root, 'published_recheck_results.csv', [
                dict(row, source='published_recheck', ok='True' if row['name'] == 'CCTV-1' else 'False',
                     video_required='True', progress_required='True', decode_required='True', decoded_frames='3') for row in rows[:2]])
            write_csv_fixture(root, 'curated-source-map.csv', [rows[0]])
            counts = export_outputs(root, {'status': 'failed', 'started_utc': now})
            report = json.loads((root / 'output/report.json').read_text(encoding='utf-8'))
            checks = {item['name']: item for item in report['checks']}
            self.assertEqual(len(report['checks']), 4)
            self.assertEqual(report['reported_unique_urls'], 4)
            self.assertEqual(report['strict_recheck_unique_urls'], 2)
            self.assertEqual(checks['CCTV-2']['source'], 'fixture')
            self.assertFalse(checks['CCTV-2']['strict_probe_ok'])
            self.assertIsNone(checks['CCTV-3']['video_probe_ok'])
            self.assertFalse(checks['CCTV-3']['broad_probe_ok'])
            self.assertEqual(checks['CCTV-4']['status'], 'not_rechecked')
            self.assertIsNone(checks['CCTV-4']['strict_probe_ok'])
            self.assertEqual(counts['final_video_rows'], sum(item['eligible_current_result'] for item in checks.values()))

    def test_export_metadata_is_keyed_by_channel_identity_not_only_url(self):
        from export_outputs import export_outputs
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            now = prepare_export_fixture(root)
            common = {'url': 'https://tv.test/shared', 'source': 'fixture', 'ok': 'True', 'checked_at': now,
                      'video_required': 'True', 'progress_required': 'True', 'decode_required': 'True', 'decoded_frames': '3', 'group': '\u592e\u89c6\u9891\u9053'}
            rows = [dict(common, name='CCTV-1', tvg_id='CCTV1.cn'),
                    dict(common, name='\u4e2d\u6587\u65b0\u95fb', tvg_id='ChineseNews.us')]
            write_csv_fixture(root, 'stream_check_results.csv', rows)
            write_csv_fixture(root, 'published_recheck_results.csv', rows)
            self.assertEqual(export_outputs(root, {'status': 'failed', 'started_utc': now})['final_video_rows'], 1)
            report = json.loads((root / 'output/report.json').read_text(encoding='utf-8'))
            checks = {item['name']: item for item in report['checks']}
            self.assertTrue(checks['CCTV-1']['eligible_current_result'])
            self.assertFalse(checks['\u4e2d\u6587\u65b0\u95fb']['eligible_current_result'])
            self.assertIn('tvg-id="CCTV1.cn"', (root / 'output/live.m3u').read_text(encoding='utf-8'))

    def test_export_excludes_ambiguous_origins_and_channel_alias_conflicts(self):
        from export_outputs import export_outputs
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            now = prepare_export_fixture(root)
            common = {'url': 'https://tv.test/shared', 'name': 'CCTV-1', 'ok': 'True', 'checked_at': now,
                      'video_required': 'True', 'progress_required': 'True', 'decode_required': 'True', 'decoded_frames': '3', 'group': '\u592e\u89c6\u9891\u9053'}
            rows = [dict(common, source=source) for source in ('fixture', 'backup')]
            write_csv_fixture(root, 'stream_check_results.csv', rows)
            write_csv_fixture(root, 'published_recheck_results.csv', [dict(common, source='published_recheck')])
            self.assertEqual(export_outputs(root, {'status': 'failed', 'started_utc': now})['final_video_rows'], 0)
            rows = [dict(common, name=f'CCTV-{number}', source='fixture') for number in (1, 2)]
            write_csv_fixture(root, 'stream_check_results.csv', rows)
            write_csv_fixture(root, 'published_recheck_results.csv', rows)
            self.assertEqual(export_outputs(root, {'status': 'failed', 'started_utc': now})['final_video_rows'], 0)
            report = json.loads((root / 'output/report.json').read_text(encoding='utf-8'))
            self.assertEqual(report['identity_conflicts_excluded'], 1)
            self.assertFalse(any(item['eligible_current_result'] for item in report['checks']))

    def test_checkpoint_success_only_same_run_and_policy(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "check.jsonl"
            state = ScanCheckpoint(path, "run1", "policy1")
            state.record("https://a.test/1", True, True, "media ok", "now", 1.0)
            state.record("https://a.test/2", True, False, "timeout", "now", 1.0)
            resumed = ScanCheckpoint(path, "run1", "policy1")
            self.assertIsNotNone(resumed.get("https://a.test/1", True))
            self.assertIsNone(resumed.get("https://a.test/1", False))
            self.assertIsNone(resumed.get("https://a.test/2", True))
            self.assertIsNone(ScanCheckpoint(path, "run2", "policy1").get("https://a.test/1", True))

    def test_checkpoint_resumes_after_interrupted_append_but_rechecks_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'scan.jsonl'
            first = ScanCheckpoint(path, 'run1', 'policy1')
            now = datetime.now(timezone.utc).isoformat()
            for number in range(100):
                first.record(f'https://tv.test/{number}', True, number < 90, 'fixture', now, 0.01)
            with path.open('a', encoding='utf-8') as handle:
                handle.write('{"url":"interrupted')
            resumed = ScanCheckpoint(path, 'run1', 'policy1')
            self.assertEqual(sum(resumed.get(f'https://tv.test/{number}', True) is not None for number in range(100)), 90)
            resumed.record('https://tv.test/100', True, True, 'recovered', now, 0.01)
            self.assertIsNotNone(ScanCheckpoint(path, 'run1', 'policy1').get('https://tv.test/100', True))
            self.assertIsNone(ScanCheckpoint(path, 'run1', 'changed-policy').get('https://tv.test/0', True))

    def test_slow_drip_body_cannot_extend_url_budget(self):
        from types import SimpleNamespace
        clock = [0.0]
        reads = []
        def read(_limit):
            clock[0] += 0.6
            reads.append(1)
            return b'x'
        response = SimpleNamespace(read=read, read1=read)
        with patch.object(verify._PROBE_CONTEXT, 'deadline', 1.0, create=True), \
                patch.object(verify.time, 'monotonic', side_effect=lambda: clock[0]):
            with self.assertRaisesRegex(TimeoutError, 'URL total budget exceeded'):
                verify.read_bounded(response, 65536)
        self.assertEqual(len(reads), 2)

    def test_encryption_is_rejected_without_fetching_keys(self):
        manifest = verify.parse_hls_manifest('#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="skd://license"\n#EXTINF:6,\na.ts', 'https://tv.test/live')
        with patch.object(verify, "http_get_small") as fetch:
            ok, _detail = verify.check_aux_resources(manifest, 1)
        self.assertFalse(ok)
        fetch.assert_not_called()

    def test_github_fallback_ref_and_path_are_preserved(self):
        self.assertEqual(verify.github_content_url('https://raw.githubusercontent.com/o/r/refs/heads/main/folder/list.m3u'),
                         'https://api.github.com/repos/o/r/contents/folder/list.m3u?ref=main')
        self.assertEqual(verify.github_content_url('https://example.test/o/r/main/list'), '')
        spec = SourceSpec('s', 'https://raw.githubusercontent.com/o/r/main/README.md', True, format='catalog')
        with patch.object(verify, 'fetch_url', side_effect=[TimeoutError(), (200, 'text/plain', b'# README', spec.url, False)]) as fetch:
            status, candidates = verify.fetch_source(spec)
        self.assertTrue(status.ok)
        self.assertEqual(status.transport, 'github_public_contents_api')
        self.assertEqual(candidates, [])
        self.assertEqual(fetch.call_count, 2)

    def test_diagnostic_export_never_uses_unchecked_or_stale_rows(self):
        from export_outputs import recent_check, stable_evidence
        now = datetime.now(timezone.utc).isoformat()
        self.assertTrue(recent_check(now, now))
        self.assertFalse(recent_check('2020-01-01T00:00:00+00:00', now))
        self.assertFalse(recent_check('', now))
        self.assertFalse(stable_evidence({'streak_ok': 10, 'last_status': 'ok', 'last_seen': '2020-01-01'}))

    def test_failed_run_exports_only_current_evidence_and_replaces_old_diagnostics(self):
        from export_outputs import export_outputs
        now = datetime.now(timezone.utc).isoformat()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'config').mkdir()
            config = root / 'config' / 'sources.json'
            config.write_text(json.dumps([{
                'name': 'fixture', 'url': 'https://catalog.test/list', 'enabled': True,
                'rights_status': 'approved', 'terms_url': 'https://catalog.test/terms',
                'reviewed_at': '2026-09-06', 'permission_scope': 'synthetic unit test fixture only',
            }]), encoding='utf-8')
            summary = {'generated_utc': now, 'source_config_sha256': hashlib.sha256(config.read_bytes()).hexdigest()}
            (root / 'full-check-summary.json').write_text(json.dumps(summary), encoding='utf-8')
            evidence = {
                'ok': 'True', 'group': '\u592e\u89c6\u9891\u9053', 'name': 'CCTV-1', 'url': 'https://tv.test/live',
                'source': 'fixture', 'video_required': 'True', 'progress_required': 'True', 'checked_at': now,
                'decode_required': 'True', 'decoded_frames': '3',
            }
            for filename in ('stream_check_results.csv', 'published_recheck_results.csv', 'curated-source-map.csv'):
                with (root / filename).open('w', encoding='utf-8', newline='') as handle:
                    writer = csv.DictWriter(handle, fieldnames=list(evidence))
                    writer.writeheader()
                    writer.writerow(evidence)
            result = export_outputs(root, {'status': 'failed', 'started_utc': now})
            self.assertEqual(result['final_video_rows'], 1)
            report = json.loads((root / 'output/report.json').read_text(encoding='utf-8'))
            self.assertFalse(report['publication_ready'])
            self.assertFalse(report['subscription_replaced_by_export'])
            self.assertEqual(report['final_sources'], {'fixture': 1})
            self.assertFalse((root / 'live.m3u').exists())
            summary['source_config_sha256'] = 'wrong-config'
            summary['publish_guard'] = {'status': 'ok'}
            summary['published_recheck'] = {'outputs_rewritten': True}
            (root / 'full-check-summary.json').write_text(json.dumps(summary), encoding='utf-8')
            self.assertEqual(export_outputs(root, {'status': 'ok', 'started_utc': now})['final_video_rows'], 0)
            report = json.loads((root / 'output/report.json').read_text(encoding='utf-8'))
            self.assertFalse(report['publication_ready'])
            self.assertEqual((root / 'output/live.m3u').read_text(encoding='utf-8'), '#EXTM3U\n')

    def test_invalid_stability_history_is_not_deferred_until_after_network_probes(self):
        import stability
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            for bad in ([], {'version': 2, 'applied_observation_ids': [], 'urls': {'https://tv.test/a': {'last_seen': 'x' * 25}}}):
                path.write_text(json.dumps(bad), encoding='utf-8')
                self.assertEqual(stability.load_json_history(path), stability.empty_history())

    def test_maintenance_summary_distinguishes_timeout_and_publication_hold(self):
        from run_maintenance import maintenance_summary
        stage = {'label': 'strict recheck', 'returncode': 1, 'classification': 'retryable',
                 'elapsed_seconds': 40, 'timed_out': False}
        report = {'status': 'failed', 'elapsed_seconds': 100, 'failed_stage': stage,
                  'attempts': [{'attempt': 1, 'stages': [stage], 'evidence': {
                      'published_recheck': {'status': 'aborted', 'abort_reason': 'failed ratio 30% > 25%',
                          'candidate_after_rows': 18, 'post_retry_failed_unique_urls': 10,
                          'outputs_rewritten': False}}}]}
        summary = maintenance_summary(report)
        self.assertIn('failed ratio 30% > 25%', summary)
        self.assertIn('verified candidate rows=18', summary)
        self.assertIn('outputs_rewritten=False', summary)
        self.assertNotIn('| timeout |', summary)
        stage.update(timed_out=True, failure_reason='stage timeout exceeded', elapsed_seconds=1800)
        summary = maintenance_summary(report)
        self.assertIn('| timeout |', summary)
        self.assertIn('stage timeout exceeded', summary)
        self.assertIn('后续步骤', maintenance_summary({'status': 'ok'}))

    def test_maintenance_alert_reports_aborted_candidate_count(self):
        from notify_maintenance import maintenance_failure_detail
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'run.json'
            path.write_text(json.dumps({'status': 'failed',
                'failed_stage': {'label': 'recheck', 'script': 'recheck_published.py', 'returncode': 1},
                'attempts': [{'attempt': 1, 'evidence': {'published_recheck': {
                    'status': 'aborted', 'abort_reason': 'too many failed URLs',
                    'after_rows': 28, 'candidate_after_rows': 18, 'outputs_rewritten': False,
                    'post_retry_failed_unique_urls': 10}}}]}), encoding='utf-8')
            detail = maintenance_failure_detail(str(path))
            self.assertIn('verified_candidate_rows=18', detail)
            self.assertIn('too many failed URLs', detail)
            self.assertIn('subscription was not updated', detail)

    def test_invalid_publication_is_not_reported_as_cdn_lag(self):
        import check_publication_endpoints as endpoints
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = root / 'live.txt'
            report = root / 'report.md'
            machine = root / 'report.json'
            args = ['--repo', 'fixture/repo', '--expected', str(expected),
                    '--report', str(report), '--json', str(machine)]
            expected.write_text('<html>error</html>', encoding='utf-8')
            with patch.object(endpoints.cf, 'ThreadPoolExecutor') as pool:
                self.assertEqual(endpoints.main(args), 2)
            pool.assert_not_called()
            data = json.loads(machine.read_text(encoding='utf-8'))
            self.assertEqual(data['failure_scope'], 'publication')
            self.assertIsNone(data['primary_current'])
            self.assertEqual(data['endpoints_checked'], 0)
            categories = '央视频道,#genre#\n卫视频道,#genre#\n地方频道,#genre#\n'
            expected.write_text(categories, encoding='utf-8')
            with patch.object(endpoints.cf, 'ThreadPoolExecutor') as pool:
                self.assertEqual(endpoints.main(args + ['--validate-only']), 2)
            pool.assert_not_called()
            expected.write_text('央视频道,#genre#\nCCTV-1,https://tv.test/live.m3u8\n卫视频道,#genre#\n地方频道,#genre#\n', encoding='utf-8')
            with patch.object(endpoints.cf, 'ThreadPoolExecutor') as pool:
                self.assertEqual(endpoints.main(args + ['--validate-only']), 0)
            pool.assert_not_called()
            self.assertEqual(json.loads(machine.read_text(encoding='utf-8'))['status'], 'input_valid')


def run_tests():
    result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(SourcePipelineTests))
    if not result.wasSuccessful():
        raise AssertionError("source pipeline regression tests failed")


if __name__ == "__main__":
    run_tests()
