#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_playlist import validate_text
from verify_sources import parse_m3u, parse_txt, split_stream_urls, split_unquoted_last_comma


def test_split_unquoted_last_comma() -> None:
    line = (
        '#EXTINF:-1 tvg-logo="https://img.example/w_400,h_500/crop.png" '
        'group-title="zonghe",24h我爱我家喜剧'
    )
    head, tail = split_unquoted_last_comma(line)
    assert 'w_400,h_500' in head
    assert tail == "24h我爱我家喜剧"


def test_split_stream_urls() -> None:
    assert split_stream_urls("http://a/live.m3u8;http://b/live.m3u8") == [
        "http://a/live.m3u8",
        "http://b/live.m3u8",
    ]
    assert split_stream_urls("http://a/live.m3u8#https://b/live.m3u8,") == [
        "http://a/live.m3u8",
        "https://b/live.m3u8",
    ]
    assert split_stream_urls("http://a/live.m3u8?token=x;y") == [
        "http://a/live.m3u8?token=x;y",
    ]


def test_parse_m3u_name_and_split_urls() -> None:
    text = """#EXTM3U
#EXTINF:-1 tvg-logo="https://img.example/w_400,h_500/crop.png" group-title="zonghe",24h我爱我家喜剧
http://a/live.m3u8;https://b/live.m3u8
"""
    cands = parse_m3u(text, "unit")
    assert [c.name for c in cands] == ["24h我爱我家喜剧", "24h我爱我家喜剧"]
    assert [c.url for c in cands] == ["http://a/live.m3u8", "https://b/live.m3u8"]


def test_parse_txt_split_urls() -> None:
    text = """地方频道,#genre#
测试频道,http://a/live.m3u8#https://b/live.m3u8
"""
    cands = parse_txt(text, "unit")
    assert [c.url for c in cands] == ["http://a/live.m3u8", "https://b/live.m3u8"]


def test_validate_rejects_malformed_url() -> None:
    malformed = """央视频道,#genre#
CCTV-1,http://a/live.m3u8;http://b/live.m3u8
卫视频道,#genre#
辽宁卫视,http://a/ln.m3u8
地方频道,#genre#
沈阳新闻,http://a/sy.m3u8
影视剧场,#genre#
电影频道,http://a/movie.m3u8
少儿动漫,#genre#
动画频道,http://a/kids.m3u8
体育纪实,#genre#
体育频道,http://a/sport.m3u8
音乐综艺,#genre#
音乐频道,http://a/music.m3u8
生活休闲,#genre#
生活频道,http://a/life.m3u8
综合娱乐,#genre#
综合频道,http://a/ent.m3u8
港澳台频道,#genre#
凤凰中文,http://a/hk.m3u8
海外华语频道,#genre#
华语频道,http://a/oversea.m3u8
"""
    try:
        validate_text(malformed, require_categories=True)
    except ValueError as e:
        assert "invalid/suspicious url" in str(e)
    else:
        raise AssertionError("malformed URL was not rejected")


def main() -> int:
    for test in [
        test_split_unquoted_last_comma,
        test_split_stream_urls,
        test_parse_m3u_name_and_split_urls,
        test_parse_txt_split_urls,
        test_validate_rejects_malformed_url,
    ]:
        test()
        print(f"OK {test.__name__}")
    print("playlist parser/validator unit tests OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
