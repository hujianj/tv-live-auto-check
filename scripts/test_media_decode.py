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
        for payload in (self.ts, self.mp4):
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


def run_tests():
    return unittest.TextTestRunner(verbosity=1).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(MediaDecodeTests)).wasSuccessful()


if __name__ == '__main__':
    raise SystemExit(0 if run_tests() else 1)
