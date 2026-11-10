"""Offline tests: candidate export must not depend on media availability."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build
from source_adapters import Channel
from source_config import SourceSpec


class UnverifiedTests(unittest.TestCase):
    def setUp(self):
        self.spec = SourceSpec('zbds_iptv4_txt', 'https://catalog.test/list', True,
                               rights_status='approved')

    def test_unreachable_and_not247_retained_without_media_requests(self):
        document = '央视频道,#genre#\nCCTV-1 [Not 24/7],https://unreachable.test/offline.m3u8\n'
        with tempfile.TemporaryDirectory() as folder, patch.object(
                build, 'fetch_url', return_value=(200, 'text/plain', document.encode(), self.spec.url, False)) as fetch, patch(
                'verify_sources.probe_media', side_effect=AssertionError('media probe called')), patch(
                'verify_sources.decode_video', side_effect=AssertionError('decoder called')):
            report = build.build(Path(folder), [self.spec])
            self.assertEqual(report['addresses'], 1)
            self.assertEqual(report['media_requests'], 0)
            self.assertFalse(report['playback_verified'])
            self.assertEqual(fetch.call_count, 1)
            self.assertEqual(fetch.call_args.args, (self.spec.url,))
            self.assertIn('CCTV-1,https://unreachable.test/offline.m3u8', (Path(folder) / build.TXT).read_text(encoding='utf-8'))

    def test_all_backups_dedup_sort_and_existing_groups(self):
        channels = [Channel('CCTV-10', 'https://tv.test/10'), Channel('CCTV-2', 'https://tv.test/2'),
                    Channel('吉林卫视', 'https://tv.test/jl'), Channel('国产动漫', 'https://tv.test/kids'),
                    Channel('翡翠台', 'https://tv.test/hk', country='hk', language='yue')]
        channels += [Channel('CCTV1高清', f'https://tv.test/1/{i}') for i in range(15)]
        channels += [Channel('CCTV-1', 'https://tv.test/1/0')]
        rows = build.ordered_rows([build.normalize(channel, self.spec)[0] for channel in channels])
        self.assertEqual(len([r for r in rows if r['name'] == 'CCTV-1']), 15)
        self.assertEqual([r['name'] for r in rows][15:17], ['CCTV-2', 'CCTV-10'])
        self.assertEqual(list(dict.fromkeys(r['group'] for r in rows)), ['央视频道', '卫视频道', '少儿动漫', '港澳台频道'])
        build.render(rows)

    def test_chinese_scope_and_sensitive_urls_still_filtered(self):
        rejected = [Channel('BBC', 'https://tv.test/bbc'), Channel('明珠台', 'https://tv.test/pearl'),
                    Channel('中文新闻', 'https://tv.test/news', country='us'),
                    Channel('中文新闻', 'https://tv.test/news', language='eng'),
                    Channel('CCTV-1', 'https://tv.test/live?token=secret'),
                    Channel('CCTV-1', 'http://192.168.1.1/live'),
                    Channel('group-title=污染', 'https://tv.test/live')]
        for channel in rejected:
            with self.subTest(channel=channel):
                self.assertIsNone(build.normalize(channel, self.spec)[0])
        pending = SourceSpec('pending', 'https://catalog.test/pending', True)
        self.assertIsNone(build.normalize(Channel('CCTV-1', 'https://tv.test/1'), pending)[0])

    def test_partial_failure_preserves_prior_source_snapshot(self):
        other = SourceSpec('backup', 'https://catalog.test/backup', True, rights_status='approved')
        def initial(spec):
            name = 'CCTV-1' if spec == self.spec else '吉林卫视'
            return [Channel(name, f'https://tv.test/{spec.name}')], {'state': 'fetched', 'parsed': 1}
        def later(spec):
            if spec == self.spec:
                return [], {'state': 'fetch_failed', 'parsed': 0, 'error': 'timeout'}
            return initial(spec)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            build.build(root, [self.spec, other], initial)
            before = (root / build.TXT).read_bytes()
            report = build.build(root, [self.spec, other], later)
            self.assertEqual(before, (root / build.TXT).read_bytes())
            self.assertEqual(report['sources'][self.spec.name]['retained_previous_rows'], 1)
            self.assertFalse(report['playback_verified'])

    def test_known_webpages_rejected_but_dynamic_streams_retained(self):
        for url in ('https://www.youtube.com/watch?v=abc',
                    'https://m.youtube.com/@channel/live',
                    'https://youtu.be/abc', 'https://www.youtube-nocookie.com/embed/abc'):
            with self.subTest(url=url):
                self.assertEqual(build.normalize(Channel('中文新闻', url), self.spec),
                                 (None, 'webpage_not_direct_stream'))
        self.assertIsNotNone(build.normalize(
            Channel('CCTV-1', 'https://tv.test/live.php?id=1'), self.spec)[0])

    def test_mislabeled_cgtn_english_stream_rejected(self):
        channel = Channel('CCTV-4中文国际（美）',
                          'https://global.cgtn.cicc.media.caton.cloud/master/cgtn-america.m3u8')
        self.assertEqual(build.normalize(channel, self.spec), (None, 'foreign_cgtn_stream'))
        self.assertIsNotNone(build.normalize(
            Channel('CCTV-4中文国际（亚）', 'https://tv.test/cctv4.m3u8'), self.spec)[0])

    def test_removed_or_permission_changed_source_not_restored(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            build.build(root, [self.spec], lambda s: ([Channel('CCTV-1', 'https://tv.test/1')], {'state': 'fetched', 'parsed': 1}))
            other = SourceSpec('backup', 'https://catalog.test/backup', True, rights_status='approved')
            report = build.build(root, [other], lambda s: ([Channel('吉林卫视', 'https://tv.test/jl')], {'state': 'fetched', 'parsed': 1}))
            self.assertEqual(report['addresses'], 1)
            self.assertNotIn('CCTV', (root / build.TXT).read_text(encoding='utf-8'))

    def test_empty_failure_leaves_output_untouched(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with self.assertRaises(ValueError):
                build.build(root, [self.spec], lambda s: ([], {'state': 'fetch_failed', 'parsed': 0}))
            self.assertFalse((root / build.TXT).exists())

    def test_unchanged_run_does_not_rewrite_snapshot(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            fetcher = lambda s: ([Channel('CCTV-1', 'https://tv.test/1')], {'state': 'fetched', 'parsed': 1})
            build.build(root, [self.spec], fetcher)
            before = {name: (root / name).read_bytes() for name in build.FILES}
            build.build(root, [self.spec], fetcher)
            self.assertEqual(before, {name: (root / name).read_bytes() for name in build.FILES})

    def test_publish_rollback_restores_previous_bundle(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in build.FILES:
                (root / name).write_bytes(b'old')
            original = Path.replace
            def fail_second(path, destination):
                if str(path).endswith(build.M3U + '.tmp'):
                    raise OSError('synthetic replacement failure')
                return original(path, destination)
            with patch.object(Path, 'replace', fail_second), self.assertRaises(OSError):
                build.atomic_snapshot(root, {name: b'new' for name in build.FILES})
            self.assertEqual([b'old'] * 3, [(root / name).read_bytes() for name in build.FILES])

    def test_user_selected_exact_url_scope_unchanged(self):
        spec = SourceSpec('selection', 'https://catalog.test/list', True, rights_status='user_requested',
                          publication_urls=('https://tv.test/1',))
        self.assertIsNotNone(build.normalize(Channel('CCTV-1', 'https://tv.test/1'), spec)[0])
        self.assertIsNone(build.normalize(Channel('CCTV-2', 'https://tv.test/2'), spec)[0])


if __name__ == '__main__':
    unittest.main()
