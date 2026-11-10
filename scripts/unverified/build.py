#!/usr/bin/env python3
"""Collect Chinese TV candidates without ever requesting a media URL.

Only upstream playlist documents are fetched. Source permissions, safe URL
syntax and the existing Chinese/channel-category policy still apply. The
separate output must never be counted as verified media or stability evidence.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import ipaddress
import json
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from channel_identity import canonical_channel_key, is_audio_only_channel
from channel_scope import channel_countries, domestic_chinese_issue, known_domestic_name
from channel_utils import cctv_number, cctv_sort_key, escape_m3u_attr, format_extinf
from curate_ku9 import clean_name, classify, G_CCTV, G_SAT, G_HK, G_OVERSEA, CCTV_ALIAS_BLOCK_TOKENS
from network_safety import public_urlopen
from playlist_config import get_group_order, load_rules, source_priority
from source_adapters import attributes, parse, split_extinf
from source_config import load_source_specs
from source_policy import publication_issue
from url_utils import publishable_url_issue, redact_text
from validate_playlist import has_invalid_channel_name
from verify_sources import decode_bytes, fetch_url, github_content_url, MAX_CANDIDATES_PER_SOURCE

TXT = 'chinese-unverified.txt'
M3U = 'chinese-unverified.m3u'
REPORT = 'chinese-unverified-report.json'
FILES = (TXT, M3U, REPORT)
MAX_OUTPUT_BYTES = 15_000_000
GROUPS = [group for group in get_group_order() if group != G_OVERSEA]


def source_fingerprint(spec):
    return hashlib.sha256(json.dumps(asdict(spec), sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def static_url_issue(url):
    """Reject local hosts and known webpage links without network access."""
    issue = publishable_url_issue(url)
    if issue:
        return issue
    host = (urlsplit(url).hostname or '').lower().rstrip('.')
    if any(host == domain or host.endswith('.' + domain)
           for domain in ('youtube.com', 'youtu.be', 'youtube-nocookie.com')):
        return 'webpage_not_direct_stream'
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        if ('.' not in host or host.endswith(('.localhost', '.local', '.lan', '.internal'))
                or re.fullmatch(r'[0-9.]+', host)):
            return 'non-public or ambiguous literal host'
        return ''
    return '' if address.is_global else 'non-public literal address'


def fetch_document(spec):
    """Bounded upstream-document fetch. No recursive resolution or media probe."""
    for attempt in range(2):
        try:
            transport = 'direct'
            try:
                payload = fetch_url(spec.url, timeout=spec.timeout_seconds)
            except (TimeoutError, ConnectionError, URLError) as exc:
                fallback = github_content_url(spec.url)
                if not fallback or isinstance(exc, HTTPError):
                    raise
                payload = fetch_url(fallback, timeout=spec.timeout_seconds,
                                    accept='application/vnd.github.raw+json')
                transport = 'github_public_contents_api'
            code, content_type, data, _final, truncated = payload
            if not 200 <= code < 300 or truncated:
                raise ValueError(f'upstream status={code}; truncated={truncated}')
            channels = parse(decode_bytes(data, content_type), spec.format)
            if not channels or len(channels) > MAX_CANDIDATES_PER_SOURCE:
                raise ValueError(f'empty or oversized parsed upstream: {len(channels)}')
            return channels, {'state': 'fetched', 'parsed': len(channels), 'transport': transport}
        except Exception as exc:
            error = redact_text(f'{type(exc).__name__}: {exc}')[:240]
            if attempt == 0 and not isinstance(exc, (ValueError, HTTPError)):
                continue
            return [], {'state': 'fetch_failed', 'error': error, 'parsed': 0}


def normalize(channel, spec):
    reason = publication_issue(spec, channel.url) or static_url_issue(channel.url)
    if reason:
        return None, reason
    # Some catalogs incorrectly label CGTN English streams as CCTV-4. This is
    # a language-identity rule, not a playback/availability test.
    if 'cgtn' in channel.url.lower():
        return None, 'foreign_cgtn_stream'
    # Availability annotations are not a reason to discard a manual-test row.
    # Remove only explicit annotation wrappers, retaining the actual station.
    name = re.sub(r'\s*[\[(](?:not\s*24/7|offline|geo[- ]blocked)[\])]\s*', '', channel.name, flags=re.I)
    name = known_domestic_name(name, channel.tvg_id, spec.name)
    name = clean_name(name)
    reason = domestic_chinese_issue(name, channel.group, spec.name, channel.tvg_id,
                                   channel.country, channel.language)
    if reason:
        return None, reason
    if has_invalid_channel_name(name):
        return None, 'invalid_channel_name'
    if is_audio_only_channel(name):
        return None, 'radio_not_television'
    if cctv_number(name) and any(token.upper() in name.upper() for token in CCTV_ALIAS_BLOCK_TOKENS):
        return None, 'pseudo_cctv_alias'
    countries = channel_countries(channel.country, channel.tvg_id)
    raw_group = G_HK if countries and countries.issubset({'hk', 'mo', 'tw'}) else channel.group
    group = classify(name, raw_group, spec.name)
    if group not in GROUPS:
        return None, 'excluded_group'
    return {'name': name, 'url': channel.url, 'group': group,
            'tvg_id': channel.tvg_id, 'tvg_logo': channel.tvg_logo,
            'country': channel.country, 'language': channel.language,
            'sources': [spec.name]}, ''


def read_previous(root):
    """Read provenance only from our prior hash-matched unverified snapshot."""
    if not (root / REPORT).is_file():
        return [], {}
    report = json.loads((root / REPORT).read_text(encoding='utf-8'))
    if report.get('playback_verified') is not False or report.get('schema_version') != 1:
        raise ValueError('invalid prior unverified report')
    for filename in (TXT, M3U):
        data = (root / filename).read_bytes()
        if hashlib.sha256(data).hexdigest() != report['files'][filename]['sha256']:
            raise ValueError(f'previous snapshot hash mismatch: {filename}')
    previous = []
    lines = (root / M3U).read_text(encoding='utf-8').splitlines()
    for index, line in enumerate(lines):
        if line.startswith('#EXTINF:'):
            attrs = attributes(split_extinf(line)[0])
            channels = parse('#EXTM3U\n' + line + '\n' + lines[index + 1] + '\n', 'm3u')
            if len(channels) != 1 or attrs.get('x-check-status') != 'unverified':
                raise ValueError('invalid previous candidate row')
            previous.append((channels[0], attrs.get('x-sources', '').split(',')))
    return previous, report


def ordered_rows(rows):
    """Merge station aliases and exact URLs; retain every distinct address."""
    stations = defaultdict(list)
    for row in rows:
        stations[canonical_channel_key(row['name'])].append(row)
    result = []
    for candidates in stations.values():
        candidates.sort(key=lambda r: (source_priority(r['sources'][0], r['url']),
                                       len(r['name']), r['name'], r['url']))
        representative = candidates[0]
        by_url = {}
        for candidate in candidates:
            row = dict(candidate, name=representative['name'], group=representative['group'])
            if row['url'] in by_url:
                old = by_url[row['url']]
                old['sources'] = sorted(set(old['sources'] + row['sources']))
            else:
                by_url[row['url']] = row
        result.extend(by_url.values())
    satellites = load_rules().get('satellite_priority', [])
    def key(row):
        name, group = row['name'], row['group']
        station = cctv_sort_key(name) if group == G_CCTV else (
            satellites.index(name) if group == G_SAT and name in satellites else 999, 0, 0, name)
        rank = min(source_priority(source, row['url']) for source in row['sources'])
        return GROUPS.index(group), station, rank, row['url']
    return sorted(result, key=key)


def render(rows):
    txt, m3u = [], ['#EXTM3U']
    last_group = None
    for row in rows:
        if row['group'] != last_group:
            txt.append(row['group'] + ',#genre#')
            last_group = row['group']
        txt.append(row['name'] + ',' + row['url'])
        metadata = {'tvg-id': row['tvg_id'], 'tvg-logo': row['tvg_logo'],
                    'tvg-country': row['country'], 'tvg-language': row['language'],
                    'x-check-status': 'unverified', 'x-sources': ','.join(sorted(row['sources']))}
        prefix = ' '.join(f'{key}="{escape_m3u_attr(value)}"' for key, value in metadata.items() if value)
        m3u.append(format_extinf(row['name'], row['group']).replace('#EXTINF:-1 ', f'#EXTINF:-1 {prefix} ', 1))
        m3u.append(row['url'])
    payloads = {TXT: ('\n'.join(txt) + '\n').encode('utf-8'),
                M3U: ('\n'.join(m3u) + '\n').encode('utf-8')}
    validate_documents(payloads, rows)
    return payloads


def validate_documents(payloads, expected=None):
    documents = []
    for filename, format in ((TXT, 'txt'), (M3U, 'm3u')):
        data = payloads[filename]
        if not data or len(data) > MAX_OUTPUT_BYTES:
            raise ValueError(f'empty/oversized output: {filename}')
        channels = parse(data.decode('utf-8'), format)
        if not channels:
            raise ValueError(f'no channels in {filename}')
        for channel in channels:
            if has_invalid_channel_name(channel.name) or static_url_issue(channel.url):
                raise ValueError(f'invalid output row in {filename}')
            if channel.group not in GROUPS or domestic_chinese_issue(channel.name, channel.group):
                raise ValueError(f'invalid output scope in {filename}')
        documents.append([(c.group, c.name, c.url) for c in channels])
    if documents[0] != documents[1] or (expected is not None and documents[0] != [
            (r['group'], r['name'], r['url']) for r in expected]):
        raise ValueError('TXT/M3U round-trip lost, changed or reordered rows')
    if len(documents[0]) != len(set(documents[0])):
        raise ValueError('duplicate output rows')
    return documents[0]


def semantic_report(report):
    return {key: value for key, value in report.items() if key != 'snapshot_generated_utc'}


def atomic_snapshot(root, payloads):
    """Validate all bytes before replacement; restore the prior bundle on error."""
    backups = {name: (root / name).read_bytes() if (root / name).exists() else None for name in payloads}
    staged = []
    try:
        for name, data in payloads.items():
            path = root / (name + '.tmp')
            path.write_bytes(data)
            staged.append(path)
        for name in payloads:
            (root / (name + '.tmp')).replace(root / name)
    except Exception:
        for name, data in backups.items():
            if data is None:
                (root / name).unlink(missing_ok=True)
            else:
                (root / name).write_bytes(data)
        raise
    finally:
        for path in staged:
            path.unlink(missing_ok=True)


def build(root=ROOT, specs=None, fetcher=fetch_document):
    root = Path(root)
    specs = load_source_specs(root / 'config/sources.json') if specs is None else specs
    previous, previous_report = read_previous(root)
    rows, statuses = [], {}
    active = [spec for spec in specs if spec.publish_allowed]
    # Only ten or so source documents, with conservative bounded concurrency.
    with ThreadPoolExecutor(max_workers=4) as executor:
        fetched = executor.map(fetcher, active)
        for spec, (channels, status) in zip(active, fetched):
            excluded = Counter()
            selected = []
            for channel in channels:
                row, reason = normalize(channel, spec)
                if row:
                    selected.append(row)
                else:
                    excluded[reason] += 1
            # A broken/empty upstream must not erase its last captured entries.
            # This snapshot remains UNVERIFIED, irrespective of its age.
            if not selected:
                old_status = previous_report.get('sources', {}).get(spec.name, {})
                if old_status.get('config_sha256') == source_fingerprint(spec):
                    for channel, sources in previous:
                        if spec.name in sources:
                            row, _ = normalize(channel, spec)
                            if row:
                                selected.append(row)
                status['retained_previous_rows'] = len(selected)
            status.update(config_sha256=source_fingerprint(spec), selected=len(selected), excluded=dict(excluded))
            statuses[spec.name] = status
            rows.extend(selected)
            print(f"{spec.name}: {status['state']}; parsed={status['parsed']}; selected={len(selected)}; retained={status.get('retained_previous_rows', 0)}", flush=True)
    for spec in specs:
        if spec.name not in statuses:
            statuses[spec.name] = {'state': 'not_enabled_for_publication', 'rights_status': spec.rights_status,
                                   'config_sha256': source_fingerprint(spec)}
    if not rows:
        raise ValueError('no Chinese candidates; prior subscription left untouched')
    rows = ordered_rows(rows)
    payloads = render(rows)
    report = {'schema_version': 1, 'playback_verified': False, 'media_requests': 0,
              'snapshot_generated_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'configured publication-allowed domestic Chinese TV candidates; includes retained upstream snapshots',
              'channels': len({canonical_channel_key(r['name']) for r in rows}), 'addresses': len(rows),
              'unique_urls': len({r['url'] for r in rows}),
              'groups': {g: {'channels': len({r['name'] for r in rows if r['group'] == g}),
                             'addresses': sum(r['group'] == g for r in rows)} for g in GROUPS if any(r['group'] == g for r in rows)},
              'files': {name: {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()} for name, data in payloads.items()},
              'sources': dict(sorted(statuses.items()))}
    evidence = root / 'output/unverified'
    evidence.mkdir(parents=True, exist_ok=True)
    (evidence / 'run-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if semantic_report(report) == semantic_report(previous_report):
        print('No subscription or source-state change; no new snapshot commit required.', flush=True)
        return report
    payloads[REPORT] = (json.dumps(report, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    atomic_snapshot(root, payloads)
    print(f"UNVERIFIED snapshot: {report['channels']} channels, {report['addresses']} addresses; media requests=0", flush=True)
    return report


def check_endpoint(root, repo, branch):
    if not re.fullmatch(r'[\w.-]+/[\w.-]+', repo) or not re.fullmatch(r'[\w.-]+', branch):
        raise ValueError('invalid repository/branch')
    expected = {name: (root / name).read_bytes() for name in (TXT, M3U)}
    validate_documents(expected)
    results = []
    for name in (TXT, M3U):
        url = f'https://gh-proxy.com/raw.githubusercontent.com/{repo}/{branch}/{name}'
        result = {'url': url, 'current': False}
        for attempt in range(4):
            try:
                with public_urlopen(Request(url, headers={'User-Agent': 'Player'}), timeout=25) as response:
                    host = (urlsplit(response.geturl()).hostname or '').lower()
                    if host == 'github.com' or host.endswith(('.github.com', '.githubusercontent.com', '.github.io')):
                        raise ValueError('subscription redirects to GitHub host')
                    data = response.read(MAX_OUTPUT_BYTES + 1)
                    result.update(status=response.status, final_host=host, bytes=len(data),
                                  sha256=hashlib.sha256(data).hexdigest(), age=response.headers.get('Age', ''))
                result['current'] = data == expected[name]
                if result['current']:
                    break
                result['error'] = 'endpoint bytes do not match published snapshot'
            except Exception as exc:
                result['error'] = redact_text(f'{type(exc).__name__}: {exc}')[:240]
            if attempt < 3:
                time.sleep(10)
        if result['current']:
            result.pop('error', None)
        results.append(result)
        print(json.dumps(result, ensure_ascii=False), flush=True)
    folder = root / 'output/unverified'
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'endpoint-report.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    if not all(result['current'] for result in results):
        raise ValueError('fixed non-GitHub subscription endpoint not current; inspect endpoint report')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check-endpoint', action='store_true')
    parser.add_argument('--repo', default='hujianj/tv-live-auto-check')
    parser.add_argument('--branch', default='main')
    args = parser.parse_args()
    if args.check_endpoint:
        check_endpoint(args.root, args.repo, args.branch)
    else:
        build(args.root)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'Unverified subscription failed: {redact_text(exc)}', file=sys.stderr)
        raise SystemExit(1)
