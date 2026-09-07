"""Real offline decoder fixtures and final-publication decoding regressions."""
import dataclasses
import subprocess
import time
import unittest
from unittest.mock import patch

import media_decode as decoder
import verify_sources as verify


def video_fixture(container: str = "mpegts") -> bytes:
    extra = ["-movflags", "empty_moov+frag_keyframe+default_base_moof"] if container == "mp4" else []
    process = subprocess.run(
        [decoder.decoder_executable(), "-hide_banner", "-loglevel", "error", "-nostdin",
         "-f", "lavfi", "-i", "testsrc2=size=160x90:rate=10", "-t", "1", "-an",
         "-c:v", "libx264", "-threads", "1", "-g", "10", "-pix_fmt", "yuv420p",
         *extra, "-f", container, "pipe:1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=True, timeout=10, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    return process.stdout


class MediaDecodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        decoder.decoder_preflight()
        cls.ts = video_fixture()
        cls.mp4 = video_fixture("mp4")

    def test_real_ts_and_fmp4_decode_frames(self):
        for container, payload in (("ts", self.ts), ("fmp4", self.mp4)):
            with self.subTest(container=container):
                result = decoder.decode_video(payload)
                self.assertTrue(result.ok, result.detail)
                self.assertEqual(result.frames, 3)

    def test_fake_track_does_not_prove_playback(self):
        payload = b'\x00\x00\x00\x18ftypisom' + b'\0' * 16 + b'moovvideavc1'
        self.assertTrue(verify.looks_media(payload, 'video/mp4', require_video=True))
        self.assertFalse(decoder.decode_video(payload).ok)
        self.assertFalse(decoder.decode_video(b'<html>denied</html>').ok)

    def test_no_url_protocol_and_bounded_timeout(self):
        self.assertFalse(decoder.decode_video(b'#EXTM3U\nhttps://example.test/private').ok)
        with patch.object(decoder.subprocess, 'run') as run:
            result = decoder.decode_video(self.ts, deadline=time.monotonic() - 1)
        self.assertFalse(result.ok)
        run.assert_not_called()

    def test_final_hls_reuses_init_and_preserves_original_url(self):
        index = self.mp4.index(b'moof') - 4
        prefix, fragment = self.mp4[:index], self.mp4[index:]
        url = 'https://catalog.test/live.m3u8'
        manifest = b'#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\n#EXTINF:1,\nsegment.m4s\n'
        def fetch(target, **_kwargs):
            data = manifest if target == url else prefix if target.endswith('init.mp4') else fragment
            return 200, 'application/octet-stream', data, target
        with patch.object(verify, 'http_get_small', side_effect=fetch) as request:
            result = verify.check_candidate(verify.Candidate('fixture', '', 'CCTV-1', url), require_decode=True)
        self.assertTrue(result.ok, result.detail)
        self.assertEqual(result.decoded_frames, 3)
        self.assertEqual(result.cand.url, url)
        self.assertEqual(sum(call.args[0].endswith('init.mp4') for call in request.call_args_list), 1)

    def test_final_gate_rejects_missing_decode_evidence(self):
        from recheck_published import require_decoded_result
        candidate = verify.Candidate('fixture', '', 'CCTV-1', 'https://tv.test/live')
        result = verify.CheckResult(candidate, True, 'track found')
        self.assertFalse(require_decoded_result(result).ok)
        self.assertTrue(require_decoded_result(dataclasses.replace(result, decoded_frames=3)).ok)

    def test_short_audio_prefix_defers_to_actual_video_decoder(self):
        url = 'https://tv.test/live.m3u8'
        manifest = '#EXTM3U\n#EXTINF:1,\nseg.ts\n'
        with patch.object(verify, 'check_media_segments', return_value=(True, 'audio/media prefix')) as segments, \
                patch.object(verify, 'decode_manifest_sample', return_value=decoder.DecodeResult(True, 3, 'decoded')):
            result = verify._check_media_manifest(verify.Candidate('fixture', '', 'CCTV-1', url),
                                                  url, manifest, url, 1, 2, False, True, True)
        self.assertTrue(result.ok)
        self.assertFalse(segments.call_args.kwargs['require_video'])

    def test_progress_failure_preserves_successful_decode_evidence(self):
        url = 'https://tv.test/live.m3u8'
        with patch.object(verify, 'check_media_segments', return_value=(True, 'media')) , \
                patch.object(verify, 'decode_manifest_sample', return_value=decoder.DecodeResult(True, 3, 'decoded')), \
                patch.object(verify, 'check_hls_progress', return_value=(False, 'manifest did not advance')):
            result = verify._check_media_manifest(verify.Candidate('fixture', '', 'CCTV-1', url),
                url, '#EXTM3U\n#EXTINF:1,\na.ts', url, 1, 2, True, True, True)
        self.assertFalse(result.ok)
        self.assertEqual(result.decoded_frames, 3)

    def test_small_decodable_sample_does_not_download_large_fallback(self):
        with patch.object(verify, 'http_get_small', return_value=(200, 'video/mp2t', self.ts, 'https://tv.test/seg.ts')) as fetch:
            result = verify.decode_public_sample('https://tv.test/seg.ts', 1)
        self.assertTrue(result.ok)
        self.assertEqual(fetch.call_count, 1)
        self.assertEqual(fetch.call_args.kwargs['max_bytes'], 512 * 1024)


def run_tests():
    return unittest.TextTestRunner(verbosity=1).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(MediaDecodeTests)).wasSuccessful()


if __name__ == '__main__':
    raise SystemExit(0 if run_tests() else 1)
