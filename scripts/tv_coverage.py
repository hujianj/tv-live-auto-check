#!/usr/bin/env python3
"""TV subscription: verified catalog plus real core-channel manual-review URLs.

This module never changes the verified source map or stability observations.
Failed checks remain failed; a separate report accounts for manual-review rows.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from dataclasses import dataclass
import ipaddress
import json
from pathlib import Path
from urllib.parse import urlsplit

from channel_identity import aliases_are_compatible, canonical_channel_key
from channel_utils import format_extinf
from curate_ku9 import prepare_curated_row, resolve_url_aliases, url_score
from playlist_config import get_group_order, load_rules
from playlist_order import canonicalize_channel_rows
from source_config import load_source_specs
from source_policy import publication_issue
from url_utils import redact_text, normalize_stream_url
from validate_playlist import validate_text, validate_m3u_text

ROOT = Path(__file__).resolve().parents[1]
TV_FILES = ('tv-coverage.m3u', 'tv-review-report.json', 'tv-review-report.md')


@dataclass(frozen=True)
class TVRow:
    group: str
    name: str
    url: str


def has_tv_coverage(root: Path) -> bool:
    path = root / 'full-check-summary.json'
    return path.is_file() and 'tv_coverage' in json.loads(path.read_text(encoding='utf-8'))


def review_policy_issue(url: str, details: list[str]) -> str:
    """No DNS request here: use this run's probes, reject literal private URLs.

    DNS/timeout/HTTP errors may be runner-specific and are reviewable. A probe
    discovering a private redirect, protected or encrypted stream is not.
    """
    host = (urlsplit(url).hostname or '').lower().rstrip('.')
    if host == 'localhost' or host.endswith(('.localhost', '.local', '.internal')):
        return 'non-public hostname'
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None
    if address is not None and not address.is_global:
        return 'non-public IP address'
    unsafe = ('non-public', 'resolves to non-public', 'encrypted', 'drm',
              'key or license', 'userinfo is not allowed', 'http connect tunnels')
    if any(token in detail.lower() for detail in details for token in unsafe):
        return 'probe detected excluded network/protection policy'
    return ''


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not {'name', 'url', 'source', 'ok'} <= set(reader.fieldnames):
            raise ValueError(f'invalid candidate evidence header: {path.name}')
        return list(reader)


def collect_candidates(records: list[dict], probes: list[dict], specs: dict,
                       strict_rows: list[TVRow]) -> tuple[list[dict], dict]:
    evidence = defaultdict(list)
    for record in [*records, *probes]:
        evidence[normalize_stream_url(record.get('url', ''))].append(record)
    approved, excluded = [], Counter()
    for record in records:
        source = record.get('source', '')
        issue = publication_issue(specs.get(source), record.get('url', ''))
        if issue:
            excluded['source_or_url_policy'] += 1
            continue
        row, reason, _ = prepare_curated_row(record.get('name', ''), record.get('url', ''),
                                             record.get('group', ''), source)
        if row is None:
            excluded[reason] += 1
            continue
        group, name, url, source = row
        details = [item.get('detail', '') for item in evidence[normalize_stream_url(record.get('url', ''))]]
        if review_policy_issue(url, details):
            excluded['network_or_protection_policy'] += 1
            continue
        approved.append((group, name, url, source))
    # Resolve against ALL eligible channel identities, not only core rows.
    # A URL claimed by incompatible channels is not a meaningful fallback.
    resolved, conflicts = resolve_url_aliases(approved)
    excluded['ambiguous_url_identity'] += sum(len(item['aliases']) for item in conflicts)
    strict_names = defaultdict(list)
    for row in strict_rows:
        strict_names[row.url].append(row.name)
    result = []
    for group, name, url, source in resolved:
        if strict_names[url] and not aliases_are_compatible([name, *strict_names[url]]):
            excluded['conflicts_with_verified_identity'] += 1
            continue
        observations = evidence[url]
        # Prefer a strict final probe to the earlier light check, regardless of success.
        final = [item for item in observations if 'phase' in item]
        last = (final or observations)[-1] if observations else {}
        result.append(dict(group=group, name=name, url=url, source=source,
                           checked_at=last.get('checked_at', ''),
                           check_ok=last.get('ok') == 'True',
                           check_detail=redact_text(last.get('detail', 'not checked'))[:800]))
    return result, dict(excluded)


def assemble(strict_rows: list[TVRow], candidates: list[dict], generated: str,
             excluded: dict | None = None, *, rank_review: bool = True) -> tuple[list[TVRow], dict]:
    coverage = load_rules().get('coverage', {})
    required = list(dict.fromkeys([*coverage.get('required_cctv', []),
                                   *coverage.get('important_satellite', [])]))
    required_names = {canonical_channel_key(name): name for name in required}
    verified_keys = {canonical_channel_key(row.name) for row in strict_rows}
    verified_urls = {row.url for row in strict_rows}
    review_by_key = defaultdict(list)
    for item in candidates:
        key = canonical_channel_key(item['name'])
        if key in verified_keys or item['url'] in verified_urls:
            continue
        if key not in required_names and item['group'] not in {'央视频道', '卫视频道'}:
            continue
        review_by_key[key].append(item)
    review = []
    for key, items in review_by_key.items():
        if rank_review:
            items.sort(key=lambda item: (*url_score(item['url'], item['source']), item['url']))
        name = required_names.get(key, items[0]['name'])
        group = '央视频道' if name.startswith('CCTV-') else items[0]['group']
        seen = set()
        for item in items:
            if item['url'] in seen:
                continue
            seen.add(item['url'])
            review.append({**item, 'name': name, 'group': group, 'status': 'pending_tv_review'})
    ordered_review = canonicalize_channel_rows(get_group_order(),
        [TVRow(item['group'], item['name'], item['url']) for item in review])
    review_map = {(item['name'], item['url']): item for item in review}
    review = [review_map[(row.name, row.url)] for row in ordered_review]
    rows = canonicalize_channel_rows(get_group_order(), [*strict_rows, *ordered_review])
    review_keys = set(review_by_key)
    missing = [name for name in required if canonical_channel_key(name) not in verified_keys | review_keys]
    counts = dict(schema_version=1, generated_utc=generated, subscription='ku9-live.txt',
        verified_subscription='live-curated.txt',
        channel_count=len({canonical_channel_key(row.name) for row in rows}),
        line_count=len(rows), verified_lines=len(strict_rows),
        verified_channels=len(verified_keys), review_lines=len(review),
        review_channels=len({canonical_channel_key(item['name']) for item in review}),
        missing_required_channels=missing,
        classification='verified and pending_tv_review are counted separately',
        selection='all verified URLs; all eligible real URLs only for core channels without verified URLs',
        speed_filter_enabled=False)
    report = {**counts, 'review_rows': review, 'excluded_candidate_rows': excluded or {}}
    return rows, report


def prepare(root: Path, *, rank_review: bool = True) -> tuple[list[TVRow], dict]:
    # Import lazily so the bundle validator can call this module without a cycle.
    from validate_publish_bundle import parse_txt_document
    _, parsed = parse_txt_document((root / 'live-curated.txt').read_text(encoding='utf-8'))
    strict = [TVRow(row.group, row.name, row.url) for row in parsed]
    if not strict:
        raise ValueError('verified playlist is empty; manual candidates cannot substitute for success')
    specs = {spec.name: spec for spec in load_source_specs(root / 'config/sources.json')}
    records = read_csv(root / 'stream_check_results.csv')
    probes = read_csv(root / 'published_recheck_results.csv')
    candidates, excluded = collect_candidates(records, probes, specs, strict)
    summary = json.loads((root / 'full-check-summary.json').read_text(encoding='utf-8'))
    return assemble(strict, candidates, summary.get('generated_utc', ''), excluded,
                    rank_review=rank_review)


def render(rows: list[TVRow], report: dict) -> tuple[str, str]:
    review = {item['url'] for item in report['review_rows']}
    txt, m3u, previous = [], ['#EXTM3U'], None
    for row in rows:
        if row.group != previous:
            txt.append(f'{row.group},#genre#')
            previous = row.group
        txt.append(f'{row.name},{row.url}')
        status = 'pending_tv_review' if row.url in review else 'verified'
        extinf = format_extinf(row.name, row.group).replace(' group-title=', f' x-check-status="{status}" group-title=', 1)
        m3u.extend([extinf, row.url])
    return '\n'.join(txt) + '\n', '\n'.join(m3u) + '\n'


def generate(root: Path = ROOT) -> dict:
    rows, report = prepare(root)
    txt, m3u = render(rows, report)
    validate_text(txt, require_categories=True)
    validate_m3u_text(m3u, require_categories=True)
    summary_path = root / 'full-check-summary.json'
    summary = json.loads(summary_path.read_text(encoding='utf-8'))
    summary['tv_coverage'] = {key: value for key, value in report.items()
                              if key not in {'review_rows', 'excluded_candidate_rows'}}
    (root / 'ku9-live.txt').write_text(txt, encoding='utf-8', newline='\n')
    (root / 'tv-coverage.m3u').write_text(m3u, encoding='utf-8', newline='\n')
    (root / 'tv-review-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    lines = ['# 电视完整订阅与待复核报告', '',
        f"生成时间：{report['generated_utc']}",
        f"电视订阅：{report['channel_count']} 个频道 / {report['line_count']} 条地址。",
        f"严格实测通过：{report['verified_channels']} 个频道 / {report['verified_lines']} 条地址。",
        f"待电视自行复核：{report['review_channels']} 个频道 / {report['review_lines']} 条真实候选地址。", '',
        '待复核地址不是检测成功地址，不进入稳定历史或严格清单。频道名保持不变，便于播放器聚合线路。',
        '有任意严格成功线路的频道，不补入失败线路；没有成功线路的央视/卫视保留全部合规候选。',
        '不使用当前电脑/云端的分片速率、响应耗时进行排序或淘汰。保留来源优先级及历史规则。', '',
        '## 没有合规真实候选的重点频道',
        ', '.join(report['missing_required_channels']) or '无', '', '## 待复核地址']
    for item in report['review_rows']:
        lines.append(f"- {item['name']} | {item['source']} | {item['checked_at']} | {item['check_detail']} | {item['url']}")
    (root / 'tv-review-report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    validate_tv_coverage(root, require_artifacts=True)
    return summary['tv_coverage']


def validate_tv_coverage(root: Path, require_artifacts: bool = False) -> dict:
    from validate_publish_bundle import parse_txt_document, parse_m3u_document, _validate_document_invariants
    summary = json.loads((root / 'full-check-summary.json').read_text(encoding='utf-8'))
    if 'tv_coverage' not in summary:
        return {'status': 'legacy_verified_alias'}
    if summary['tv_coverage'].get('schema_version') != 1:
        raise ValueError('unsupported TV coverage schema')
    report = json.loads((root / 'tv-review-report.json').read_text(encoding='utf-8'))
    expected_counts = {key: value for key, value in report.items()
                       if key not in {'review_rows', 'excluded_candidate_rows'}}
    if expected_counts != summary['tv_coverage']:
        raise ValueError('TV summary and review report disagree')
    _, strict = parse_txt_document((root / 'live-curated.txt').read_text(encoding='utf-8'))
    groups, rows = parse_txt_document((root / 'ku9-live.txt').read_text(encoding='utf-8'))
    errors = []
    _validate_document_invariants('TV coverage', groups, rows, errors)
    if errors:
        raise ValueError('; '.join(errors))
    if parse_m3u_document((root / 'tv-coverage.m3u').read_text(encoding='utf-8')) != rows:
        raise ValueError('TV M3U/TXT rows or order differ')
    strict_keys = {canonical_channel_key(row.name) for row in strict}
    specs = {spec.name: spec for spec in load_source_specs(root / 'config/sources.json')}
    review = []
    for item in report['review_rows']:
        if item.get('status') != 'pending_tv_review' or canonical_channel_key(item['name']) in strict_keys:
            raise ValueError('manual review must not replace a verified channel or claim success')
        issue = publication_issue(specs.get(item['source']), item['url'])
        prepared, _, _ = prepare_curated_row(item['name'], item['url'], item['group'], item['source'])
        if issue or not prepared or review_policy_issue(item['url'], [item.get('check_detail', '')]):
            raise ValueError('manual review row violates source, channel or network policy')
        if item['group'] not in {'央视频道', '卫视频道'}:
            raise ValueError('manual review is limited to CCTV and satellite channels')
        review.append(TVRow(item['group'], item['name'], item['url']))
    strict_tv = [TVRow(row.group, row.name, row.url) for row in strict]
    # Check the committed order, not a fresh ranking against mutable/absent
    # local history. Generation ranks backups once; canonicalization still
    # enforces group/channel order while retaining each channel's line order.
    rebuilt, expected = assemble(strict_tv, report['review_rows'], report['generated_utc'],
                                 report['excluded_candidate_rows'], rank_review=False)
    if expected != report or [TVRow(row.group, row.name, row.url) for row in rows] != rebuilt:
        raise ValueError('TV catalog/report counts, coverage or ordering do not reconcile')
    txt, m3u = render(rebuilt, report)
    if (root / 'ku9-live.txt').read_bytes() != txt.encode() or (root / 'tv-coverage.m3u').read_bytes() != m3u.encode():
        raise ValueError('TV canonical rendering/status attributes differ')
    if require_artifacts:
        # Candidate evidence must reconcile exactly, independently of where
        # this validation runs or whether a later observation changed ranking.
        # Output/report order has already been checked above. Never relax
        # completeness, metadata, policy, counts or duplicate detection here.
        actual_rows, actual_report = prepare(root, rank_review=False)
        row_key = lambda row: (row.group, row.name, row.url)
        review_key = lambda item: (item['group'], item['name'], item['url'])
        expected_evidence = {**report, 'review_rows': sorted(report['review_rows'], key=review_key)}
        actual_evidence = {**actual_report, 'review_rows': sorted(actual_report['review_rows'], key=review_key)}
        if (sorted(actual_rows, key=row_key) != sorted(rebuilt, key=row_key)
                or actual_evidence != expected_evidence):
            raise ValueError('TV manual-review URLs do not exactly match current candidate evidence')
    return {'status': 'ok', **summary['tv_coverage']}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(generate(args.root), ensure_ascii=False), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
