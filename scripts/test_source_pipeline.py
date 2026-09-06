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
            (root / 'full-check-summary.json').write_text(json.dumps(summary), encoding='utf-8')
            self.assertEqual(export_outputs(root, {'status': 'failed', 'started_utc': now})['final_video_rows'], 0)
            self.assertEqual((root / 'output/live.m3u').read_text(encoding='utf-8'), '#EXTM3U\n')

    def test_invalid_stability_history_is_not_deferred_until_after_network_probes(self):
        import stability
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            for bad in ([], {'version': 2, 'applied_observation_ids': [], 'urls': {'https://tv.test/a': {'last_seen': 'x' * 25}}}):
                path.write_text(json.dumps(bad), encoding='utf-8')
                self.assertEqual(stability.load_json_history(path), stability.empty_history())


def run_tests():
    result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(SourcePipelineTests))
    if not result.wasSuccessful():
        raise AssertionError("source pipeline regression tests failed")


if __name__ == "__main__":
    run_tests()
