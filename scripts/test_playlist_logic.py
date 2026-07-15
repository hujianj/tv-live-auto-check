#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from pathlib import Path
import json
import sys
import tempfile
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_playlist import validate_m3u_text, validate_text
from verify_sources import SOURCES, Candidate, is_core_family_candidate, looks_transient_failure, parse_m3u, parse_txt, split_stream_urls, split_unquoted_last_comma
from playlist_config import get_group_order, load_guard, load_priority, load_quality, source_priority
from stability import stability_adjustment
import stability as stability_module
import curate_ku9 as curate_module
import audit_quality as quality_module
import local_network_check as local_check_module
from channel_utils import cctv_key as coverage_cctv_key, cctv_number, cctv_sort_key, cctv_variant_base, format_extinf, is_latin_noise_name


def test_source_config_omits_disabled_unstable_sources() -> None:
    names = [name for name, _ in SOURCES]
    assert len(names) == len(set(names))
    assert "zbds_iptv4_txt" in names
    assert "yuechan_live" not in names
    assert "freetv_huya" not in names


def test_rules_config_contains_core_coverage() -> None:
    rules = json.loads((ROOT / "config" / "rules.json").read_text(encoding="utf-8-sig"))
    def walk_strings(obj):
        if isinstance(obj, dict):
            for value in obj.values():
                yield from walk_strings(value)
        elif isinstance(obj, list):
            for value in obj:
                yield from walk_strings(value)
        elif isinstance(obj, str):
            yield obj

    bad_strings = [s for s in walk_strings(rules) if "?" in s or "\ufffd" in s]
    assert bad_strings == []
    assert "辽宁" in rules["provinces"]
    assert "卫视" not in rules["category_keywords"]["movie"]
    assert get_group_order() == rules["group_order"]
    assert rules["bad_name_tokens"]
    assert rules["group_keywords"]["hk"] == ["香港", "澳门", "台湾", "港澳台"]
    assert "CCTV-1" in rules["coverage"]["required_cctv"]
    assert "CCTV-5+" in rules["coverage"]["required_cctv"]
    assert "辽宁卫视" in rules["coverage"]["important_satellite"]
    assert rules["coverage"].get("fail_on_missing_cctv") is True
    assert rules["coverage"].get("fail_on_missing_satellite") is True


def test_priority_and_guard_config_are_externalized() -> None:
    priority = load_priority()
    guard = load_guard()
    quality = load_quality()
    assert source_priority("zbds_iptv4_txt", "https://live.zbds.top/tv/iptv4.txt") == -200
    assert source_priority("zbds_iptv4_m3u", "https://live.zbds.top/tv/iptv4.m3u") == -150
    assert source_priority("suxuang_ipv4", "https://example.test/a.m3u8") == -30
    assert priority["score_adjustments"]["verify"]["ipv6"] > 0
    assert priority["stability"]["enabled"] is True
    assert priority["stability"]["max_entries"] <= 5000
    assert guard["min_lines"] >= 1800
    assert guard["min_groups"]["央视频道"] >= 90
    assert 0 < guard["max_published_recheck_failed_url_ratio"] <= 0.5
    assert "zbds_iptv4_txt" in guard["core_sources"]
    assert guard["publish_size"]["max_unique_public_blob_bytes"] >= 2_000_000
    assert "stream_check_results.csv" in guard["publish_size"]["forbid_tracked_artifacts"]
    assert quality["channel_limits"]["core_max_urls_per_name"] >= quality["channel_limits"]["default_max_urls_per_name"]
    assert quality["group_max_rows"]["综合娱乐"] >= guard["min_groups"]["综合娱乐"]
    assert "Geo-blocked" in quality["strict_drop_name_tokens"]


def test_quality_filters_and_limits_are_enforced() -> None:
    assert curate_module.strict_quality_drop_reason("纪录|Discovery")
    assert curate_module.strict_quality_drop_reason("吉林市新闻综合[Geo-blocked]")
    assert not curate_module.strict_quality_drop_reason("BRTV北京卫视(1080p)")
    assert curate_module.per_channel_limit(curate_module.G_CCTV, "CCTV-1") >= 6
    assert curate_module.per_channel_limit(curate_module.G_ENT, "普通娱乐") <= 3

    old_limits = dict(curate_module.GROUP_MAX_ROWS)
    try:
        curate_module.GROUP_MAX_ROWS[curate_module.G_SAT] = 1
        rows = [
            (curate_module.G_SAT, "辽宁卫视", "http://a/ln.m3u8", "s"),
            (curate_module.G_SAT, "河北卫视", "http://a/hb.m3u8", "s"),
            (curate_module.G_SAT, "普通卫视", "http://a/other.m3u8", "s"),
        ]
        limited, trimmed = curate_module.apply_group_limits(rows)
        names = [x[1] for x in limited]
        assert "辽宁卫视" in names
        assert "河北卫视" in names
        assert "普通卫视" not in names
        assert trimmed[curate_module.G_SAT] == 1
    finally:
        curate_module.GROUP_MAX_ROWS.clear()
        curate_module.GROUP_MAX_ROWS.update(old_limits)


def test_coverage_counts_exact_cctv_and_reports_variants() -> None:
    assert coverage_cctv_key("CCTV-4") == "CCTV-4"
    assert coverage_cctv_key("CCTV-4(1080p)") == "CCTV-4"
    assert coverage_cctv_key("CCTV-4K") is None
    assert coverage_cctv_key("CCTV-4FHD") is None
    assert cctv_number("CCTV-4K") == (4, 0)
    assert cctv_sort_key("CCTV-4") < cctv_sort_key("CCTV-4K")
    assert cctv_variant_base("CCTV-4K") == "CCTV-4"
    assert coverage_cctv_key("CCTV-5+") == "CCTV-5+"
    assert cctv_variant_base("CCTV-5+体育") == "CCTV-5+"
    assert is_latin_noise_name("DiscoveryAsia") is True
    assert is_latin_noise_name("BRTV北京卫视") is False
    assert is_latin_noise_name("TVB翡翠台") is False


def test_format_extinf_escapes_quoted_attributes() -> None:
    line = format_extinf('示例"频道', "综合娱乐")
    assert 'tvg-name="示例&quot;频道"' in line
    m3u = f"""#EXTM3U
{line}
http://a/live.m3u8
"""
    result = validate_m3u_text(m3u, require_categories=False)
    assert result["rows"] == 1


def test_quality_audit_detects_core_and_strict_residue() -> None:
    rows = [
        ("央视频道", "CCTV-1", "http://a/cctv1.m3u8"),
        ("央视频道", "CCTV-1", "http://b/cctv1.m3u8"),
        ("央视频道", "CCTV-1", "http://c/cctv1.m3u8"),
        ("卫视频道", "辽宁卫视", "http://a/ln.m3u8"),
        ("卫视频道", "辽宁卫视", "http://b/ln.m3u8"),
        ("卫视频道", "辽宁卫视", "http://c/ln.m3u8"),
        ("综合娱乐", "纪录|Discovery", "http://a/discovery.m3u8"),
    ]
    result, failures, warnings = quality_module.build_audit(rows)
    assert result["strict_filter_residue_count"] == 1
    assert any("strict filtered" in x for x in failures)
    assert result["missing_cctv_quality"]
    assert warnings


def test_local_network_parser_and_core_filter() -> None:
    text = """央视频道,#genre#
CCTV-1,http://a/cctv1.m3u8
CCTV-4K,http://a/cctv4k.m3u8
卫视频道,#genre#
辽宁卫视,http://a/ln.m3u8
综合娱乐,#genre#
综合频道,http://a/ent.m3u8
"""
    rows = local_check_module.parse_tv_txt(text)
    args = SimpleNamespace(core_only=True, limit=0)
    filtered = local_check_module.filter_rows(rows, args)
    assert ("央视频道", "CCTV-1", "http://a/cctv1.m3u8") in filtered
    assert ("卫视频道", "辽宁卫视", "http://a/ln.m3u8") in filtered
    assert not any(name == "CCTV-4K" for _group, name, _url in filtered)
    assert not any(name == "综合频道" for _group, name, _url in filtered)
    fake_results = [
        {"ok": True, "group": "央视频道", "name": "CCTV-1", "core_key": "CCTV-1", "url": "http://a", "detail": "ok"},
        {"ok": False, "group": "央视频道", "name": "CCTV-1", "core_key": "CCTV-1", "url": "http://b", "detail": "timeout"},
        {"ok": False, "group": "央视频道", "name": "CCTV-17", "core_key": "CCTV-17", "url": "http://c", "detail": "timeout"},
    ]
    stats = local_check_module.channel_stats(fake_results)
    by_channel = {item["channel"]: item for item in stats}
    assert by_channel["CCTV-1"]["ok"] == 1
    assert by_channel["CCTV-17"]["ok"] == 0


def test_stability_adjustment_prefers_proven_urls() -> None:
    history = {
        "urls": {
            "http://stable.example/live.m3u8": {"ok": 5, "fail": 0, "streak_ok": 5, "streak_fail": 0},
            "http://flaky.example/live.m3u8": {"ok": 1, "fail": 3, "streak_ok": 0, "streak_fail": 2},
        }
    }
    assert stability_adjustment("http://stable.example/live.m3u8", history) < 0
    assert stability_adjustment("http://flaky.example/live.m3u8", history) > 0
    assert stability_adjustment("http://stable.example/live.m3u8", history) < stability_adjustment("http://flaky.example/live.m3u8", history)
    assert stability_adjustment("http://new.example/live.m3u8", history) == 0


def test_stability_update_counts_unique_urls() -> None:
    old_history_path = stability_module.history_path
    old_report_path = stability_module.report_path
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        stability_module.history_path = lambda: tmp_path / "history.tsv"  # type: ignore[assignment]
        stability_module.report_path = lambda: tmp_path / "report.md"  # type: ignore[assignment]
        try:
            rows = [
                SimpleNamespace(group="央视频道", name="CCTV-1", url="http://a/live.m3u8"),
                SimpleNamespace(group="卫视频道", name="辽宁卫视", url="http://a/live.m3u8"),
                SimpleNamespace(group="卫视频道", name="河北卫视", url="http://b/live.m3u8"),
            ]
            summary = stability_module.update_history(rows, {"http://b/live.m3u8": "timeout"}, {})
            assert summary["updated_urls"] == 2
            assert summary["ok_updates"] == 1
            assert summary["fail_updates"] == 1
            history = stability_module.load_history()
            assert history["urls"]["http://a/live.m3u8"]["ok"] == 1
            assert history["urls"]["http://b/live.m3u8"]["fail"] == 1
        finally:
            stability_module.history_path = old_history_path  # type: ignore[assignment]
            stability_module.report_path = old_report_path  # type: ignore[assignment]


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


def test_core_retry_classification() -> None:
    assert is_core_family_candidate(Candidate("unit", "央视频道", "CCTV-1", "http://a/live.m3u8"))
    assert is_core_family_candidate(Candidate("unit", "卫视频道", "辽宁卫视", "http://a/live.m3u8"))
    assert not is_core_family_candidate(Candidate("unit", "综合娱乐", "电影频道", "http://a/live.m3u8"))
    assert looks_transient_failure("TimeoutError('timed out')")
    assert looks_transient_failure("RemoteDisconnected('Remote end closed connection without response')")
    assert not looks_transient_failure("<HTTPError 404: 'Not Found'>")
    assert not looks_transient_failure("bad marker/html")


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


def test_validate_m3u_accepts_generated_shape() -> None:
    m3u = """#EXTM3U
#EXTINF:-1 tvg-name="CCTV-1" group-title="央视频道",CCTV-1
http://a/cctv1.m3u8
#EXTINF:-1 tvg-name="辽宁卫视" group-title="卫视频道",辽宁卫视
http://a/ln.m3u8
#EXTINF:-1 tvg-name="沈阳新闻" group-title="地方频道",沈阳新闻
http://a/sy.m3u8
#EXTINF:-1 tvg-name="电影频道" group-title="影视剧场",电影频道
http://a/movie.m3u8
#EXTINF:-1 tvg-name="动画频道" group-title="少儿动漫",动画频道
http://a/kids.m3u8
#EXTINF:-1 tvg-name="体育频道" group-title="体育纪实",体育频道
http://a/sport.m3u8
#EXTINF:-1 tvg-name="音乐频道" group-title="音乐综艺",音乐频道
http://a/music.m3u8
#EXTINF:-1 tvg-name="生活频道" group-title="生活休闲",生活频道
http://a/life.m3u8
#EXTINF:-1 tvg-name="综合频道" group-title="综合娱乐",综合频道
http://a/ent.m3u8
#EXTINF:-1 tvg-name="凤凰中文" group-title="港澳台频道",凤凰中文
http://a/hk.m3u8
#EXTINF:-1 tvg-name="华语频道" group-title="海外华语频道",华语频道
http://a/oversea.m3u8
"""
    result = validate_m3u_text(m3u, require_categories=True)
    assert result["format"] == "m3u"
    assert result["rows"] == 11


def test_validate_m3u_rejects_polluted_url() -> None:
    m3u = """#EXTM3U
#EXTINF:-1 tvg-name="CCTV-1" group-title="央视频道",CCTV-1
http://a/cctv1.m3u8;http://b/cctv1.m3u8
"""
    try:
        validate_m3u_text(m3u, require_categories=False)
    except ValueError as e:
        assert "invalid/suspicious url" in str(e)
    else:
        raise AssertionError("malformed M3U URL was not rejected")


def test_validate_rejects_strict_quality_filtered_channel() -> None:
    txt = """综合娱乐,#genre#
纪录|Discovery,http://a/discovery.m3u8
"""
    try:
        validate_text(txt, require_categories=False)
    except ValueError as e:
        assert "strict quality filtered channel" in str(e)
    else:
        raise AssertionError("strict quality filtered channel was not rejected")


def test_recheck_source_map_helper() -> None:
    from recheck_published import Row, source_for

    row = Row("央视频道", "CCTV-1", "http://example.test/live.m3u8")
    assert source_for(row, {("CCTV-1", "http://example.test/live.m3u8"): "zbds_iptv4_txt"}) == "zbds_iptv4_txt"
    assert source_for(row, {}) == "unknown"


def main() -> int:
    for test in [
        test_source_config_omits_disabled_unstable_sources,
        test_rules_config_contains_core_coverage,
        test_priority_and_guard_config_are_externalized,
        test_quality_filters_and_limits_are_enforced,
        test_coverage_counts_exact_cctv_and_reports_variants,
        test_format_extinf_escapes_quoted_attributes,
        test_quality_audit_detects_core_and_strict_residue,
        test_local_network_parser_and_core_filter,
        test_stability_adjustment_prefers_proven_urls,
        test_stability_update_counts_unique_urls,
        test_split_unquoted_last_comma,
        test_split_stream_urls,
        test_parse_m3u_name_and_split_urls,
        test_parse_txt_split_urls,
        test_core_retry_classification,
        test_validate_rejects_malformed_url,
        test_validate_m3u_accepts_generated_shape,
        test_validate_m3u_rejects_polluted_url,
        test_validate_rejects_strict_quality_filtered_channel,
        test_recheck_source_map_helper,
    ]:
        test()
        print(f"OK {test.__name__}")
    print("playlist parser/validator unit tests OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
