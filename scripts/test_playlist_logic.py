#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from pathlib import Path
import csv
import json
import re
import socket
import sys
import tempfile
import zlib
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_playlist import validate_m3u_text, validate_text
from verify_sources import SOURCES, Candidate, CheckResult, HLSManifest, SourceStatus, deduplicate_candidates, is_core_family_candidate, looks_bad, looks_transient_failure, order_source_statuses, parse_hls_manifest, parse_m3u, parse_txt, progress_wait_seconds, split_stream_urls, split_unquoted_last_comma
from playlist_config import get_group_order, load_guard, load_home_priority, load_priority, load_quality, source_priority
from stability import stability_adjustment
import stability as stability_module
import verify_sources as verify_module
import curate_ku9 as curate_module
import audit_quality as quality_module
import local_network_check as local_check_module
import run_maintenance as maintenance_module
from channel_utils import cctv_key as coverage_cctv_key, cctv_number, cctv_sort_key, cctv_variant_base, format_extinf, is_latin_noise_name
from channel_identity import aliases_are_compatible, canonical_channel_key
from validate_publish_bundle import BundleValidationError, Row as BundleRow, validate_publish_bundle
from publication_config import PublicationConfigError, load_publication_config
from publication_manifest import (
    FINAL_PUBLICATION_FILES,
    MANIFEST_FILE,
    ManifestValidationError,
    SIZE_AUDIT_FILES,
    SUMMARY_FILE as MANIFEST_SUMMARY_FILE,
    validate_manifest,
    write_manifest,
)
from media_probe import looks_media as media_looks_playable, probe_media
import network_safety as network_safety_module
from network_safety import PublicRedirectHandler, PublicURLPolicyError, resolve_public_addresses, validate_public_url
from url_utils import normalize_stream_url


def test_workflow_is_pinned_and_refuses_stale_publication() -> None:
    workflow = (ROOT / ".github" / "workflows" / "update.yml").read_text(encoding="utf-8")
    action_refs = [line.strip() for line in workflow.splitlines() if line.strip().startswith("uses:")]
    assert action_refs
    assert all(re.fullmatch(r"uses: [A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[0-9a-f]{40}(?: # v\d+)?", line) for line in action_refs), action_refs
    assert "stefanzweifel/git-auto-commit-action" not in workflow
    assert 'remote_sha=$(git rev-parse "origin/$TARGET_BRANCH")' in workflow
    assert 'if [ "$remote_sha" != "$SOURCE_SHA" ]; then' in workflow
    assert 'git push origin "HEAD:$TARGET_BRANCH"' in workflow
    assert "Refuse publication from a non-default branch" in workflow
    assert "github.ref_name != github.event.repository.default_branch" in workflow
    assert workflow.index("Refuse publication from a non-default branch") < workflow.index("Run complete maintenance pipeline")
    assert "IPTV_REQUIRE_VIDEO_TRACK" in (ROOT / "scripts" / "run_maintenance.py").read_text(encoding="utf-8")
    assert "IPTV_REQUIRE_VIDEO_TRACK" in (ROOT / "scripts" / "run_maintenance.py").read_text(encoding="utf-8")
    assert "issues: write" in workflow
    assert "notify_maintenance.py" in workflow
    assert workflow.count("continue-on-error: true") >= 4
    assert not workflow.rstrip().endswith(r"\n"), "workflow contains a literal trailing \\n token"
    endpoint_checker = (ROOT / "scripts" / "check_publication_endpoints.py").read_text(encoding="utf-8")
    assert "No television-compatible publication endpoint is current" in endpoint_checker
    assert "Required primary television endpoint is not current" in endpoint_checker
    assert "publication_check=" not in endpoint_checker
    assert "python scripts/run_maintenance.py" in workflow
    assert "cancel-in-progress: false" in workflow
    assert workflow.index("Run complete maintenance pipeline") < workflow.index("Commit verified playlist")
    assert "cdn_pending" in workflow
    assert "--publication-files" in workflow

    fast_workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    fast_refs = [line.strip() for line in fast_workflow.splitlines() if line.strip().startswith("uses:")]
    assert fast_refs
    assert all(re.fullmatch(r"uses: [A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[0-9a-f]{40}(?: # v\d+)?", line) for line in fast_refs), fast_refs
    assert "contents: read" in fast_workflow
    assert "persist-credentials: false" in fast_workflow
    assert "validate_publication.py" in fast_workflow


def test_publication_config_rejects_ambiguous_roles_and_unsafe_paths() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "config").mkdir()
        config = json.loads((ROOT / "config" / "publication.json").read_text(encoding="utf-8-sig"))

        def expect_rejected(mutator) -> None:
            candidate = json.loads(json.dumps(config))
            mutator(candidate)
            (root / "config" / "publication.json").write_text(
                json.dumps(candidate), encoding="utf-8", newline="\n"
            )
            try:
                load_publication_config(root)
            except PublicationConfigError:
                return
            raise AssertionError("invalid publication configuration was accepted")

        expect_rejected(lambda value: value["endpoints"].append(dict(value["endpoints"][0])))
        expect_rejected(lambda value: value["endpoints"][1].update({"required_primary": True}))
        expect_rejected(lambda value: value["endpoints"][0].update({"path": "../live-curated.txt"}))
        expect_rejected(lambda value: value["endpoints"][0].update({"template": "http://example.test/{path}"}))
        expect_rejected(lambda value: value["endpoints"][0].update({"path": value["primary_text_file"]}))
        expect_rejected(lambda value: value["endpoints"][3].update({"television_compatible": False}))


def test_source_statuses_follow_config_order() -> None:
    configured = [("first", "https://one.test/list"), ("second", "https://two.test/list")]
    completion_order = [
        SourceStatus("second", configured[1][1], True),
        SourceStatus("first", configured[0][1], False, error="timeout"),
    ]
    ordered = order_source_statuses(completion_order, configured)
    assert [status.name for status in ordered] == ["first", "second"]


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


def test_classification_avoids_single_character_false_positives() -> None:
    rules = json.loads((ROOT / "config" / "rules.json").read_text(encoding="utf-8-sig"))
    assert "\u5267" not in rules["category_keywords"]["movie"]
    assert "\u8d5b" not in rules["category_keywords"]["sport_doc"]
    assert not {"\u623f", "\u5c55", "\u5b66"}.intersection(rules["category_keywords"]["life"])
    assert curate_module.classify("\u4eac\u5267\u9891\u9053", "", "unit") == "\u97f3\u4e50\u7efc\u827a"
    assert curate_module.classify("\u8d5b\u8f66\u9891\u9053", "", "unit") == "\u4f53\u80b2\u7eaa\u5b9e"
    assert curate_module.classify("\u623f\u4ea7\u9891\u9053", "", "unit") == "\u751f\u6d3b\u4f11\u95f2"
    assert curate_module.classify("\u661f\u5149\u5c55\u64ad", "", "unit") == "\u7efc\u5408\u5a31\u4e50"
    assert curate_module.classify("\u5b66\u800c\u601d", "", "unit") == "\u7efc\u5408\u5a31\u4e50"


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
    assert "澳門MACAU" in quality["strict_drop_name_tokens"]
    home_priority = load_home_priority()
    assert home_priority.get("enabled") is True
    assert "home_ok_urls" in home_priority
    assert "home_failed_urls" in home_priority
    family = quality.get("family_profile") or {}
    assert family.get("enabled") is True
    assert "ku9-family.txt" in family.get("txt_files", [])
    assert family.get("min_lines", 0) >= 500


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


def test_home_priority_adjustment_and_writer() -> None:
    old_enabled = curate_module.HOME_PRIORITY_ENABLED
    old_ok = set(curate_module.HOME_OK_URLS)
    old_failed = set(curate_module.HOME_FAILED_URLS)
    old_bonus = curate_module.HOME_PRIORITY_BONUS
    old_penalty = curate_module.HOME_PRIORITY_PENALTY
    try:
        curate_module.HOME_PRIORITY_ENABLED = True
        curate_module.HOME_OK_URLS.clear()
        curate_module.HOME_FAILED_URLS.clear()
        curate_module.HOME_OK_URLS.add("http://ok/live.m3u8")
        curate_module.HOME_FAILED_URLS.add("http://bad/live.m3u8")
        curate_module.HOME_PRIORITY_BONUS = -120
        curate_module.HOME_PRIORITY_PENALTY = 180
        assert curate_module.home_priority_adjustment("http://ok/live.m3u8") == -120
        assert curate_module.home_priority_adjustment("http://bad/live.m3u8") == 180
        assert curate_module.home_priority_adjustment("http://new/live.m3u8") == 0
    finally:
        curate_module.HOME_PRIORITY_ENABLED = old_enabled
        curate_module.HOME_OK_URLS.clear(); curate_module.HOME_OK_URLS.update(old_ok)
        curate_module.HOME_FAILED_URLS.clear(); curate_module.HOME_FAILED_URLS.update(old_failed)
        curate_module.HOME_PRIORITY_BONUS = old_bonus
        curate_module.HOME_PRIORITY_PENALTY = old_penalty

    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "home-priority.json"
        args = SimpleNamespace(
            home_priority=str(path),
            home_priority_max_urls=2,
            core_only=True,
            timeout=15,
        )
        result = {
            "rows": [
                {"ok": True, "url": "http://ok/1.m3u8"},
                {"ok": True, "url": "http://ok/1.m3u8"},
                {"ok": True, "url": "http://ok/2.m3u8"},
                {"ok": True, "url": "http://ok/3.m3u8"},
                {"ok": False, "url": "http://bad/1.m3u8"},
            ],
            "checked_rows": 5,
            "checked_unique_urls": 4,
            "ok_unique_urls": 3,
            "failed_unique_urls": 1,
        }
        local_check_module.write_home_priority(result, "unit", args)
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["home_ok_urls"] == ["http://ok/1.m3u8", "http://ok/2.m3u8"]
        assert data["home_failed_urls"] == ["http://bad/1.m3u8"]
        assert data["mode"] == "core-only"


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
    assert is_latin_noise_name("TVB中文") is False


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
    assert normalize_stream_url("http://a/live.m3u8#") == "http://a/live.m3u8"


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


def test_family_playlist_limits() -> None:
    from recheck_published import Row, build_family_rows, family_profile

    profile = family_profile()
    assert profile.get("enabled") is True
    rows = [
        Row("央视频道", "CCTV-1", f"http://a/cctv1-{i}.m3u8") for i in range(6)
    ] + [
        Row("综合娱乐", "娱乐频道", f"http://a/ent-{i}.m3u8") for i in range(3)
    ]
    family_rows = build_family_rows(["央视频道", "综合娱乐"], rows)
    cctv_urls = [row.url for row in family_rows if row.name == "CCTV-1"]
    ent_urls = [row.url for row in family_rows if row.name == "娱乐频道"]
    assert len(cctv_urls) == min(4, int((profile.get("group_channel_limits") or {}).get("央视频道", 4)))
    assert len(ent_urls) == 1


def test_family_playlist_uses_canonical_identity_quota() -> None:
    from recheck_published import Row, build_family_rows

    rows = [
        Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/1.m3u8"),
        Row("\u592e\u89c6\u9891\u9053", "CCTV-1(720p)", "http://a/2.m3u8"),
        Row("\u592e\u89c6\u9891\u9053", "CCTV-1\u9ad8\u6e05", "http://a/3.m3u8"),
        Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/4.m3u8"),
        Row("\u592e\u89c6\u9891\u9053", "CCTV-1\u8d85\u6e05", "http://a/5.m3u8"),
    ]
    family_rows = build_family_rows(["\u592e\u89c6\u9891\u9053"], rows)
    assert len(family_rows) == 4
    assert [row.url for row in family_rows] == [f"http://a/{i}.m3u8" for i in range(1, 5)]


def test_source_dedup_is_deterministic() -> None:
    low = Candidate("epg_cn", "\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/live.m3u8")
    preferred = Candidate("zbds_iptv4_txt", "\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/live.m3u8")
    first = deduplicate_candidates([low, preferred])
    second = deduplicate_candidates([preferred, low])
    assert first[("CCTV-1", "http://a/live.m3u8")].source == "zbds_iptv4_txt"
    assert second == first


def test_canonical_identity_collapses_resolution_and_official_aliases() -> None:
    assert canonical_channel_key("\u6e56\u5357\u536b\u89c6") == canonical_channel_key("\u6e56\u5357\u536b\u89c64K")
    assert canonical_channel_key("\u5357\u56fd\u90fd\u5e02") == canonical_channel_key("\u5357\u56fd\u90fd\u5e024K")
    assert canonical_channel_key("CCTV-16") == canonical_channel_key("CCTV-16\u8d85\u6e05")
    assert canonical_channel_key("CCTV-16") == canonical_channel_key("CCTV-16\u5965\u6797\u5339\u514b")
    assert aliases_are_compatible(["CCTV-16", "CCTV-16\u5965\u6797\u5339\u514b"])



def _psi_section(table_id: int, body: bytes) -> bytes:
    section_length = len(body) + 4
    return bytes([table_id, 0xB0 | ((section_length >> 8) & 0x0F), section_length & 0xFF]) + body + bytes(4)


def _ts_packet(pid: int, section: bytes) -> bytes:
    header = bytes([0x47, 0x40 | ((pid >> 8) & 0x1F), pid & 0xFF, 0x10])
    payload = bytes([0]) + section
    return header + payload + bytes([0xFF]) * (188 - len(header) - len(payload))


def _sample_ts(stream_type: int) -> bytes:
    pat = _psi_section(0x00, b"\x00\x01\xC1\x00\x00\x00\x01\xE0\x64")
    pmt = _psi_section(
        0x02,
        b"\x00\x01\xC1\x00\x00\xE1\x00\xF0\x00"
        + bytes([stream_type])
        + b"\xE0\x65\xF0\x00",
    )
    return _ts_packet(0, pat) + _ts_packet(100, pmt)


def test_strict_media_probe_requires_a_video_track() -> None:
    video = _sample_ts(0x1B)
    audio = _sample_ts(0x0F)
    assert probe_media(video, "video/mp2t").kind == "video"
    assert probe_media(audio, "video/mp2t").kind == "audio"
    assert media_looks_playable(video, "video/mp2t", require_video=True)
    assert not media_looks_playable(audio, "video/mp2t", require_video=True)
    assert media_looks_playable(audio, "audio/aac", require_video=False)
    init_video = b"\x00\x00\x00\x18ftypisom" + b"moovtrakmdiahdlrvideavc1"
    init_audio = b"\x00\x00\x00\x18ftypisom" + b"moovtrakmdiahdlrsounmp4a"
    assert probe_media(init_video, "video/mp4").kind == "video"
    assert probe_media(init_audio, "audio/mp4").kind == "audio"


def test_public_network_policy_blocks_private_and_redirect_targets() -> None:
    original_getaddrinfo = network_safety_module.socket.getaddrinfo
    try:
        def fake_getaddrinfo(host, port, type=socket.SOCK_STREAM):
            address = "93.184.216.34" if host == "public.test" else "127.0.0.1"
            return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (address, port))]

        network_safety_module.socket.getaddrinfo = fake_getaddrinfo
        resolve_public_addresses.cache_clear()
        assert validate_public_url("https://public.test/live.m3u8").startswith("https://")
        try:
            validate_public_url("http://private.test/live.m3u8")
        except PublicURLPolicyError as exc:
            assert "non-public" in str(exc)
        else:
            raise AssertionError("private DNS answer was accepted")
        try:
            PublicRedirectHandler().redirect_request(SimpleNamespace(full_url="https://public.test/live.m3u8"), None, 302, "Found", {}, "http://127.0.0.1/admin")
        except PublicURLPolicyError:
            pass
        else:
            raise AssertionError("private redirect target was accepted")
    finally:
        network_safety_module.socket.getaddrinfo = original_getaddrinfo
        resolve_public_addresses.cache_clear()


def test_fetch_url_handles_gzip_final_url() -> None:
    payload = b"channel,http://example.test/live.m3u8\n"
    compressed = zlib.compressobj(wbits=16 + zlib.MAX_WBITS)
    blob = compressed.compress(payload) + compressed.flush()
    original = verify_module.limited_urlopen

    class Response:
        status = 200
        headers = {"Content-Type": "application/gzip", "Content-Encoding": "gzip"}

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self, limit):
            return blob[:limit]

        def geturl(self):
            return "https://public.test/list.m3u.gz"

    try:
        verify_module.limited_urlopen = lambda _request, timeout: Response()
        code, ctype, data, final, truncated = verify_module.fetch_url("https://public.test/list.m3u.gz")
        assert code == 200
        assert ctype == "application/gzip"
        assert data == payload
        assert final.endswith(".gz")
        assert truncated is False
    finally:
        verify_module.limited_urlopen = original


def test_strict_bounded_gzip_decompression() -> None:
    payload = ("\u9891\u9053,http://example.test/live.m3u8\n" * 100).encode("utf-8")
    compressed = zlib.compressobj(wbits=16 + zlib.MAX_WBITS)
    blob = compressed.compress(payload) + compressed.flush()
    assert verify_module._bounded_gzip_decompress(blob, len(payload)) == payload
    for bad, limit, expected in [
        (blob[:-3], len(payload), "truncated gzip"),
        (blob, len(payload) - 1, "exceeded maximum"),
        (blob + b"junk", len(payload), "trailing data"),
    ]:
        try:
            verify_module._bounded_gzip_decompress(bad, limit)
        except ValueError as exc:
            assert expected in str(exc), str(exc)
        else:
            raise AssertionError(f"gzip case should fail: {expected}")


def test_hls_error_words_inside_valid_urls_are_not_false_negatives() -> None:
    text = "#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:404\n#EXTINF:4,\nsegment-offline-404.ts?token=nosignal\n"
    manifest = parse_hls_manifest(text, "https://unit.test/live/index.m3u8")
    assert manifest.media_sequence == 404
    assert manifest.segments == ["https://unit.test/live/segment-offline-404.ts?token=nosignal"]
    assert not looks_bad(text.encode("utf-8"))
    assert looks_bad(b"404 Not Found")


def test_hls_progress_rechecks_new_live_edge_segment() -> None:
    initial = HLSManifest([], ["http://unit.test/s1.ts"], [], [], 1, 1.0, False)
    later_manifest = b"#EXTM3U\n#EXT-X-TARGETDURATION:1\n#EXT-X-MEDIA-SEQUENCE:2\n#EXTINF:1,\ns2.ts\n"
    original_get = verify_module.http_get_small
    original_sleep = verify_module.time.sleep
    try:
        calls = []

        def failing_edge(url, max_bytes=4096, timeout=1):
            calls.append(url)
            if url.endswith("playlist.m3u8"):
                return 200, "application/vnd.apple.mpegurl", later_manifest, url
            return 404, "text/html", b"not found", url

        verify_module.http_get_small = failing_edge
        verify_module.time.sleep = lambda _seconds: None
        ok, detail = verify_module.check_hls_progress("http://unit.test/playlist.m3u8", initial, 1, require_video=False)
        assert not ok, detail
        assert "new edge failed" in detail
        assert calls == ["http://unit.test/playlist.m3u8", "http://unit.test/s2.ts"]

        calls.clear()
        media = _sample_ts(0x1B)

        def working_edge(url, max_bytes=4096, timeout=1):
            calls.append(url)
            if url.endswith("playlist.m3u8"):
                return 200, "application/vnd.apple.mpegurl", later_manifest, url
            return 200, "video/mp2t", media, url

        verify_module.http_get_small = working_edge
        ok, detail = verify_module.check_hls_progress("http://unit.test/playlist.m3u8", initial, 1, require_video=False)
        assert ok, detail
        assert "new edge ok" in detail
        assert calls == ["http://unit.test/playlist.m3u8", "http://unit.test/s2.ts"]
    finally:
        verify_module.http_get_small = original_get
        verify_module.time.sleep = original_sleep


def test_progress_wait_respects_target_duration() -> None:
    assert progress_wait_seconds(None) >= verify_module.HLS_PROGRESS_MIN_WAIT
    assert progress_wait_seconds(10.0) >= 10.0
    assert progress_wait_seconds(999.0) == verify_module.HLS_PROGRESS_MAX_WAIT


def test_media_segment_probe_uses_live_edge() -> None:
    called = []
    original = verify_module.http_get_small
    try:
        def fake(url, max_bytes=4096, timeout=1):
            called.append(url)
            return 200, "video/mp2t", _sample_ts(0x1B), url

        verify_module.http_get_small = fake
        ok, _detail = verify_module.check_media_segments(["s1", "s2", "s3", "s4"], limit=2, timeout=1, require_video=False)
        assert ok
        assert called == ["s3", "s4"]
    finally:
        verify_module.http_get_small = original


def test_final_recheck_refills_failed_channel_urls() -> None:
    import recheck_published as recheck

    before = [
        recheck.Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/1.m3u8"),
        recheck.Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/2.m3u8"),
        recheck.Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/3.m3u8"),
    ]
    kept = before[:1]
    pool = [
        recheck.PoolCandidate("CCTV-1", recheck.Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/4.m3u8"), "zbds_iptv4_txt"),
        recheck.PoolCandidate("CCTV-1", recheck.Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/5.m3u8"), "epg_cn"),
        recheck.PoolCandidate("CCTV-1", recheck.Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://a/6.m3u8"), "guovin_ipv4"),
    ]
    calls = []

    def fake_checker(cand, core_override, require_progress):
        calls.append((cand.url, core_override, require_progress))
        ok = not cand.url.endswith("5.m3u8")
        return CheckResult(cand, ok, "ok" if ok else "failed")

    final_rows, results, summary, attempted, accepted = recheck.refill_missing_rows(
        before,
        kept,
        {"http://a/2.m3u8": "failed", "http://a/3.m3u8": "failed"},
        pool,
        checker=fake_checker,
    )
    assert [row.url for row in final_rows] == ["http://a/1.m3u8", "http://a/4.m3u8", "http://a/6.m3u8"]
    assert len(results) == 3
    assert len(attempted) == 3
    assert [item.row.url for item in accepted] == ["http://a/4.m3u8", "http://a/6.m3u8"]
    assert summary["refilled_rows"] == 2
    assert summary["unresolved_rows"] == 0
    assert all(core and progress for _url, core, progress in calls)


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


def _render_test_txt(groups, rows) -> str:
    lines = []
    for group in groups:
        part = [row for row in rows if row.group == group]
        if not part:
            continue
        if lines:
            lines.append("")
        lines.append(f"{group},#genre#")
        lines.extend(f"{row.name},{row.url}" for row in part)
    return "\n".join(lines) + "\n"


def _render_test_m3u(rows) -> str:
    lines = ["#EXTM3U"]
    for row in rows:
        lines.extend([format_extinf(row.name, row.group), row.url])
    return "\n".join(lines) + "\n"


def _write_test_publish_bundle(root: Path, full_rows=None, family_rows=None, group_order=None) -> tuple[list[BundleRow], list[BundleRow]]:
    groups = list(group_order or get_group_order())
    canonical_groups = get_group_order()
    if full_rows is None:
        full_rows = [
            BundleRow(group, "CCTV-1" if i == 0 else f"\u5bb6\u5ead\u9891\u9053{i}", f"http://unit.test/{i}.m3u8")
            for i, group in enumerate(canonical_groups)
        ]
    if family_rows is None:
        family_rows = list(full_rows)
    full_text = _render_test_txt(groups, full_rows)
    family_text = _render_test_txt(groups, family_rows)
    for name in ("live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"):
        (root / name).write_text(full_text, encoding="utf-8", newline="\n")
    for name in ("ku9-family.txt", "live-family.txt"):
        (root / name).write_text(family_text, encoding="utf-8", newline="\n")
    (root / "live.m3u").write_text(_render_test_m3u(full_rows), encoding="utf-8", newline="\n")
    (root / "family.m3u").write_text(_render_test_m3u(family_rows), encoding="utf-8", newline="\n")
    with (root / "curated-source-map.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["group", "name", "url", "source"])
        for row in full_rows:
            writer.writerow([row.group, row.name, row.url, "unit"])
    with (root / "curated-candidate-pool.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["selection_key", "group", "name", "url", "source"])
        for row in full_rows:
            writer.writerow([canonical_channel_key(row.name), row.group, row.name, row.url, "unit"])
    (root / "alias-conflict-report.md").write_text("# test\n", encoding="utf-8")
    (root / "sources_status.csv").write_text(
        "name,url,fetch_ok,bytes,parsed,truncated,error\nunit,https://unit.test/source,True,100,1,False,\n",
        encoding="utf-8",
        newline="\n",
    )
    (root / "config").mkdir(exist_ok=True)
    (root / "config" / "sources.json").write_text(
        json.dumps([{"name": "unit", "url": "https://unit.test/source", "enabled": True}], indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    full_groups = dict(__import__("collections").Counter(row.group for row in full_rows))
    family_groups = dict(__import__("collections").Counter(row.group for row in family_rows))
    checked = len({row.url for row in full_rows})
    summary = {
        "sources_total": 1,
        "sources_fetched_ok": 1,
        "checked_all_unique": True,
        "broad_media_probe_checked": checked,
        "broad_checked_all_unique": True,
        "strict_video_checked_unique": checked,
        "strict_progress_checked_unique": checked,
        "checked_candidates": checked,
        "unique_candidates": checked,
        "unique_name_url_candidates": len(full_rows),
        "playable_unique_urls": checked,
        "playable_name_url_lines": len(full_rows),
        "playable_urls_found": len(full_rows),
        "all_playable_lines": len(full_rows),
        "curated_generated": True,
        "curated_source_map_available": True,
        "curated_source_map_generated": True,
        "curated_source_map_artifact_only": True,
        "curated_candidate_pool_generated": True,
        "curated_candidate_pool_artifact_only": True,
        "curated_published_lines": len(full_rows),
        "final_primary_published_lines": len(full_rows),
        "primary_published_lines": len(full_rows),
        "curated_channel_names": len({row.name for row in full_rows}),
        "curated_groups": full_groups,
        "curated_sources": {"unit": len(full_rows)},
        "coverage": {"missing_cctv": [], "missing_satellite": []},
        "quality_audit": {
            "status": "ok",
            "rows": len(full_rows),
            "unique_names": len({row.name for row in full_rows}),
            "unique_urls": checked,
            "groups": full_groups,
            "strict_filter_residue": [],
            "missing_cctv_quality": [],
            "missing_satellite_quality": [],
        },
        "published_recheck": {
            "core_progress_required": True,
            "require_video_track": True,
            "video_track_verified_unique_urls": checked,
            "public_network_policy_enabled": True,
            "checked_unique_urls": checked,
            "initial_checked_unique_urls": checked,
            "first_pass_failed_unique_urls": 0,
            "slow_retry_attempted_unique_urls": 0,
            "slow_retry_recovered_unique_urls": 0,
            "post_retry_failed_unique_urls": 0,
            "initial_failed_unique_urls": 0,
            "refill_failed_unique_urls": 0,
            "failed_unique_urls": 0,
            "before_rows": len(full_rows),
            "after_rows": len(full_rows),
            "removed_rows": 0,
            "slow_retry": {
                "first_pass_failed_unique_urls": 0,
                "initial_failed_unique_urls": 0,
                "attempted_unique_urls": 0,
                "recovered_unique_urls": 0,
                "still_failed_unique_urls": 0,
            },
            "refill": {
                "enabled": True,
                "attempted_unique_urls": 0,
                "playable_unique_urls": 0,
                "refilled_rows": 0,
                "unresolved_rows": 0,
            },
        },
        "stability": {"enabled": True, "updated_urls": checked, "tracked_urls_after": checked},
        "family_playlist": {
            "enabled": True,
            "lines": len(family_rows),
            "unique_names": len({row.name for row in family_rows}),
            "unique_urls": len({row.url for row in family_rows}),
            "groups": family_groups,
        },
    }
    (root / "full-check-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return list(full_rows), list(family_rows)


def _assert_bundle_failure(root: Path, expected: str) -> None:
    try:
        validate_publish_bundle(root)
    except BundleValidationError as exc:
        assert expected in str(exc), str(exc)
    else:
        raise AssertionError(f"bundle unexpectedly passed; expected {expected!r}")


def test_publish_bundle_validator_enforces_cross_file_invariants() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        result = validate_publish_bundle(root)
        assert result["status"] == "ok"
        assert result["full_rows"] == len(get_group_order())

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        order = get_group_order()
        _write_test_publish_bundle(root, group_order=[order[1], order[0], *order[2:]])
        _assert_bundle_failure(root, "category order/coverage mismatch")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        for name in ("live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"):
            text = (root / name).read_text(encoding="utf-8")
            first = text.splitlines()[0]
            (root / name).write_text(first + "\n" + text, encoding="utf-8")
        _assert_bundle_failure(root, "category order/coverage mismatch")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        for name in ("live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"):
            text = (root / name).read_text(encoding="utf-8")
            (root / name).write_text("\u6c61\u67d3\u9891\u9053,http://unit.test/pre.m3u8\n" + text, encoding="utf-8")
        _assert_bundle_failure(root, "before first category")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        rows, _ = _write_test_publish_bundle(root)
        first_line = f"{rows[0].name},{rows[0].url}"
        for name in ("live-curated.txt", "live.txt", "live-verified.txt", "ku9-live.txt"):
            text = (root / name).read_text(encoding="utf-8")
            (root / name).write_text(text.replace(first_line, first_line + "\n" + first_line, 1), encoding="utf-8")
        _assert_bundle_failure(root, "exact duplicate rows")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        groups = get_group_order()
        rows = [
            BundleRow(group, "CCTV-1" if i == 0 else f"\u5bb6\u5ead\u9891\u9053{i}", "http://unit.test/shared.m3u8" if i < 2 else f"http://unit.test/{i}.m3u8")
            for i, group in enumerate(groups)
        ]
        _write_test_publish_bundle(root, full_rows=rows)
        _assert_bundle_failure(root, "incompatible channel identities")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        groups = get_group_order()
        rows = [
            BundleRow(group, "CCTV-1" if i == 0 else ("CCTV-1(4K)" if i == 1 else f"\u5bb6\u5ead\u9891\u9053{i}"), f"http://unit.test/{i}.m3u8")
            for i, group in enumerate(groups)
        ]
        _write_test_publish_bundle(root, full_rows=rows)
        _assert_bundle_failure(root, "canonical channel identities span categories")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        m3u = (root / "live.m3u").read_text(encoding="utf-8").replace("http://unit.test/0.m3u8", "http://unit.test/changed.m3u8", 1)
        (root / "live.m3u").write_text(m3u, encoding="utf-8")
        _assert_bundle_failure(root, "live.m3u rows/order")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        rows, _ = _write_test_publish_bundle(root)
        family = [BundleRow(rows[0].group, rows[0].name, "http://unit.test/not-in-full.m3u8"), *rows[1:]]
        _write_test_publish_bundle(root, full_rows=rows, family_rows=family)
        _assert_bundle_failure(root, "not an ordered subset")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        (root / "sources_status.csv").write_text(
            "name,url,fetch_ok,bytes,parsed,truncated,error\n", encoding="utf-8", newline="\n"
        )
        _assert_bundle_failure(root, "summary.sources_total/sources_status rows")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        summary_path = root / "full-check-summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        summary["curated_published_lines"] += 1
        summary_path.write_text(json.dumps(summary, ensure_ascii=False), encoding="utf-8")
        _assert_bundle_failure(root, "summary.curated_published_lines")


    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        summary_path = root / "full-check-summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        # checked_unique_urls includes failed refill attempts, so it may be
        # greater than the final published unique URL count.
        summary["published_recheck"]["checked_unique_urls"] += 2
        summary["strict_video_checked_unique"] += 2
        summary["published_recheck"]["refill_failed_unique_urls"] += 2
        summary["published_recheck"]["failed_unique_urls"] += 2
        summary["published_recheck"]["refill"]["attempted_unique_urls"] += 2
        summary["stability"]["updated_urls"] += 2
        summary["stability"]["tracked_urls_after"] += 2
        summary_path.write_text(json.dumps(summary, ensure_ascii=False), encoding="utf-8", newline="\n")
        assert validate_publish_bundle(root)["status"] == "ok"

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        status_path = root / "sources_status.csv"
        status_path.write_text(
            status_path.read_text(encoding="utf-8").replace("https://unit.test/source", "https://unit.test/changed", 1),
            encoding="utf-8",
            newline="\n",
        )
        _assert_bundle_failure(root, "source name/URL order does not match")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        status_path = root / "sources_status.csv"
        status_path.write_text(
            status_path.read_text(encoding="utf-8").replace(",False,\n", ",maybe,\n", 1),
            encoding="utf-8",
            newline="\n",
        )
        _assert_bundle_failure(root, "invalid truncated values")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        source_map_path = root / "curated-source-map.csv"
        source_map_path.write_text(
            source_map_path.read_text(encoding="utf-8").replace("group,name,url,source", "name,group,url,source", 1),
            encoding="utf-8",
            newline="\n",
        )
        _assert_bundle_failure(root, "header must be")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        pool_path = root / "curated-candidate-pool.csv"
        pool_path.write_text(
            pool_path.read_text(encoding="utf-8").replace("selection_key,group,name,url,source", "group,selection_key,name,url,source", 1),
            encoding="utf-8",
            newline="\n",
        )
        _assert_bundle_failure(root, "header must be")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        pool_path = root / "curated-candidate-pool.csv"
        lines = pool_path.read_text(encoding="utf-8").splitlines()
        parts = lines[1].split(",", 1)
        lines[1] = "wrong-key," + parts[1]
        pool_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        _assert_bundle_failure(root, "does not match canonical channel key")

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _write_test_publish_bundle(root)
        pool_path = root / "curated-candidate-pool.csv"
        lines = pool_path.read_text(encoding="utf-8").splitlines()
        pool_path.write_text("\n".join([lines[0], *lines[2:]]) + "\n", encoding="utf-8", newline="\n")
        _assert_bundle_failure(root, "final published rows are missing from the candidate pool")

    for field_path in (
        ("curated_channel_names",),
        ("quality_audit", "rows"),
        ("published_recheck", "video_track_verified_unique_urls"),
        ("family_playlist", "groups"),
    ):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            _write_test_publish_bundle(root)
            summary_path = root / "full-check-summary.json"
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            target = summary
            for part in field_path[:-1]:
                target = target[part]
            del target[field_path[-1]]
            summary_path.write_text(json.dumps(summary, ensure_ascii=False), encoding="utf-8", newline="\n")
            _assert_bundle_failure(root, "missing required fields")




def test_publish_size_hashes_current_worktree_not_stale_index() -> None:
    source = (ROOT / "scripts" / "audit_publish_size.py").read_text(encoding="utf-8")
    assert '"hash-object", "--"' in source
    assert '"ls-files", "-s"' not in source


def test_publication_checker_uses_exact_canonical_url_and_requires_primary() -> None:
    from check_publication_endpoints import EndpointResult, build_request, endpoint_matrix, publication_gate_failures

    url = "https://cdn.jsdelivr.net/gh/example/repo/ku9-live.txt"
    request = build_request(url)
    assert request.full_url == url
    assert "publication_check=" not in request.full_url
    headers = {key.lower(): value for key, value in request.header_items()}
    assert "cache-control" not in headers
    assert "pragma" not in headers

    endpoints = endpoint_matrix("example/repo", "main")
    primary = [item for item in endpoints if item.required_primary]
    assert [item.name for item in primary] == ["jsdelivr_primary"]
    results = [
        EndpointResult("github_raw", "https://raw.test/list", True, False, False, ok=True),
        EndpointResult("ghproxy_raw", "https://proxy.test/list", False, True, False, ok=True),
        EndpointResult("jsdelivr_cdn", url, False, True, True, ok=False, error="stale hash"),
    ]
    failures = publication_gate_failures(results)
    assert any("Required primary television endpoint" in item for item in failures)
    results[-1].ok = True
    assert publication_gate_failures(results) == []


def test_publication_manifest_covers_final_summary_without_self_hash() -> None:
    assert MANIFEST_SUMMARY_FILE not in SIZE_AUDIT_FILES
    assert MANIFEST_FILE not in FINAL_PUBLICATION_FILES
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        for name in FINAL_PUBLICATION_FILES:
            path = root / name
            if name == MANIFEST_SUMMARY_FILE:
                path.write_text(
                    json.dumps({"generated_utc": "2026-07-18T00:00:00Z", "final_primary_published_lines": 1}) + "\n",
                    encoding="utf-8",
                    newline="\n",
                )
            else:
                path.write_text(f"fixture for {name}\n", encoding="utf-8", newline="\n")
        manifest = write_manifest(root)
        assert manifest["manifest_self_hash_excluded"] is True
        assert MANIFEST_SUMMARY_FILE in manifest["files"]
        assert validate_manifest(root)["status"] == "ok"
        (root / MANIFEST_SUMMARY_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
        try:
            validate_manifest(root)
        except ManifestValidationError as exc:
            assert "full-check-summary.json" in str(exc)
        else:
            raise AssertionError("mutating a finalized summary must invalidate the publication manifest")


def test_final_recheck_slow_retry_recovers_non_core_failure() -> None:
    import recheck_published as recheck

    url = "http://example.test/live.m3u8"
    row = recheck.Row("????", "????", url)
    original = CheckResult(Candidate("fixture", row.group, row.name, row.url), False, "TimeoutError")
    results = {url: original}
    calls: list[dict] = []

    def checker(candidate, **kwargs):
        calls.append(kwargs)
        return CheckResult(candidate, True, "video/h264")

    summary = recheck.retry_failed_final_urls(
        {url: row},
        results,
        set(),
        attempts=1,
        workers=1,
        timeout=17,
        checker=checker,
    )
    assert summary["attempted_unique_urls"] == 1
    assert summary["recovered_unique_urls"] == 1
    assert summary["still_failed_unique_urls"] == 0
    assert results[url].ok is True
    assert calls == [{"timeout": 17, "core_override": False, "require_progress": False, "require_video": True}]


def test_generated_csv_writers_force_lf_line_endings() -> None:
    for relative in [
        "scripts/verify_sources.py",
        "scripts/curate_ku9.py",
        "scripts/recheck_published.py",
        "scripts/local_network_check.py",
        "scripts/stability.py",
    ]:
        source = (ROOT / relative).read_text(encoding="utf-8")
        for line in source.splitlines():
            if "csv.writer(" in line or "csv.DictWriter(" in line:
                assert 'lineterminator="\\n"' in line, (relative, line)


def test_local_maintenance_wrapper_is_fail_fast_and_complete() -> None:
    commands = maintenance_module.pipeline_commands()
    labels = [label for label, _command in commands]
    scripts = [Path(command[1]).name for _label, command in commands]
    assert labels[-4:] == [
        "guard against unsafe shrinkage",
        "audit publish size and generate manifest",
        "validate complete publish bundle",
        "validate immutable public publication",
    ]
    assert scripts == [stage.script for stage in maintenance_module.STAGES]
    assert commands[0][1][-1] == "--validate"
    assert commands[-2][1][-1] == "--strict"
    assert scripts.index("guard_publish.py") < scripts.index("audit_publish_size.py")
    assert scripts.index("audit_publish_size.py") < scripts.index("validate_publish_bundle.py")
    assert scripts.index("validate_publish_bundle.py") < scripts.index("validate_publication.py")
    assert maintenance_module.STEP_ENV_OVERRIDES["verify_sources.py"]["IPTV_REQUIRE_VIDEO_TRACK"] == "0"
    assert maintenance_module.STEP_ENV_OVERRIDES["recheck_published.py"]["IPTV_REQUIRE_VIDEO_TRACK"] == "1"
    assert maintenance_module.main(["--dry-run"]) == 0


def test_recheck_source_map_helper() -> None:
    from recheck_published import Row, source_for

    row = Row("央视频道", "CCTV-1", "http://example.test/live.m3u8")
    assert source_for(row, {("CCTV-1", "http://example.test/live.m3u8"): "zbds_iptv4_txt"}) == "zbds_iptv4_txt"
    assert source_for(row, {}) == "unknown"


def test_recheck_summary_records_video_policy() -> None:
    import recheck_published as recheck

    original_root = recheck.ROOT
    try:
        with tempfile.TemporaryDirectory() as td:
            recheck.ROOT = Path(td)
            (recheck.ROOT / recheck.SUMMARY_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
            rows = [recheck.Row("\u592e\u89c6\u9891\u9053", "CCTV-1", "http://unit.test/live.m3u8")]
            recheck.update_summary(rows, rows, 1, {}, {}, 0.1, {}, {}, {}, {}, {"first_pass_failed_unique_urls": 0, "attempted_unique_urls": 0, "recovered_unique_urls": 0, "still_failed_unique_urls": 0}, 1)
            summary = json.loads((recheck.ROOT / recheck.SUMMARY_FILE).read_text(encoding="utf-8"))
            assert summary["published_recheck"]["require_video_track"] is True
            assert summary["published_recheck"]["video_track_verified_unique_urls"] == 1
    finally:
        recheck.ROOT = original_root


def main() -> int:
    for test in [
        test_workflow_is_pinned_and_refuses_stale_publication,
        test_publication_config_rejects_ambiguous_roles_and_unsafe_paths,
        test_source_statuses_follow_config_order,
        test_source_config_omits_disabled_unstable_sources,
        test_rules_config_contains_core_coverage,
        test_classification_avoids_single_character_false_positives,
        test_priority_and_guard_config_are_externalized,
        test_quality_filters_and_limits_are_enforced,
        test_home_priority_adjustment_and_writer,
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
        test_family_playlist_limits,
        test_family_playlist_uses_canonical_identity_quota,
        test_source_dedup_is_deterministic,
        test_canonical_identity_collapses_resolution_and_official_aliases,
        test_strict_media_probe_requires_a_video_track,
        test_public_network_policy_blocks_private_and_redirect_targets,
        test_fetch_url_handles_gzip_final_url,
        test_strict_bounded_gzip_decompression,
        test_hls_error_words_inside_valid_urls_are_not_false_negatives,
        test_hls_progress_rechecks_new_live_edge_segment,
        test_progress_wait_respects_target_duration,
        test_media_segment_probe_uses_live_edge,
        test_final_recheck_refills_failed_channel_urls,
        test_core_retry_classification,
        test_validate_rejects_malformed_url,
        test_validate_m3u_accepts_generated_shape,
        test_validate_m3u_rejects_polluted_url,
        test_validate_rejects_strict_quality_filtered_channel,
        test_publish_bundle_validator_enforces_cross_file_invariants,
        test_publish_size_hashes_current_worktree_not_stale_index,
        test_publication_checker_uses_exact_canonical_url_and_requires_primary,
        test_publication_manifest_covers_final_summary_without_self_hash,
        test_final_recheck_slow_retry_recovers_non_core_failure,
        test_generated_csv_writers_force_lf_line_endings,
        test_local_maintenance_wrapper_is_fail_fast_and_complete,
        test_recheck_source_map_helper,
        test_recheck_summary_records_video_policy,
    ]:
        test()
        print(f"OK {test.__name__}")
    print("playlist parser/validator unit tests OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
