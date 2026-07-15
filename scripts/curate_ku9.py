#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import csv, json, re
from pathlib import Path
from collections import defaultdict, Counter
from validate_playlist import validate_text
from playlist_config import get_group_order, load_home_priority, load_quality, load_rules, score_adjustments, source_priority as configured_source_priority
from stability import load_history, stability_adjustment, stability_enabled
from channel_utils import cctv_number, cctv_sort_key, chinese_count as shared_chinese_count, format_extinf

ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / "stream_check_results.csv"
RULES_PATH = ROOT / "config" / "rules.json"
CURATED_SOURCE_MAP = ROOT / "curated-source-map.csv"

G_CCTV = "\u592e\u89c6\u9891\u9053"
G_SAT = "\u536b\u89c6\u9891\u9053"
G_LOCAL = "\u5730\u65b9\u9891\u9053"
G_MOVIE = "\u5f71\u89c6\u5267\u573a"
G_KIDS = "\u5c11\u513f\u52a8\u6f2b"
G_SPORT_DOC = "\u4f53\u80b2\u7eaa\u5b9e"
G_MUSIC_SHOW = "\u97f3\u4e50\u7efc\u827a"
G_LIFE = "\u751f\u6d3b\u4f11\u95f2"
G_ENT = "\u7efc\u5408\u5a31\u4e50"
G_HK = "\u6e2f\u6fb3\u53f0\u9891\u9053"
G_OVERSEA = "\u6d77\u5916\u534e\u8bed\u9891\u9053"
GROUP_ORDER = get_group_order()


RULES = load_rules()
QUALITY = load_quality()
HOME_PRIORITY = load_home_priority()
PROVINCES = RULES['provinces']
HK_KEYS = RULES['category_keywords']['hk']
MOVIE_KEYS = RULES['category_keywords']['movie']
KIDS_KEYS = RULES['category_keywords']['kids']
SPORT_DOC_KEYS = RULES['category_keywords']['sport_doc']
MUSIC_SHOW_KEYS = RULES['category_keywords']['music_show']
LIFE_KEYS = RULES['category_keywords']['life']
GROUP_KEYS = RULES['group_keywords']
FOREIGN_LANG = re.compile(RULES['foreign_lang_regex'], re.I)
FOREIGN_NAME_TOKENS = RULES['foreign_name_tokens']
FOREIGN_CN_TOKENS = RULES['foreign_cn_tokens']
UNSTABLE_NAME_TOKENS = RULES['unstable_name_tokens']
CCTV_ALIAS_BLOCK_TOKENS = RULES['cctv_alias_block_tokens']
HK_CN_KEYS = RULES['hk_cn_keys']
HK_LATIN_PREFIXES = tuple(RULES['hk_latin_prefixes'])
TVB_PREFIXES = tuple(RULES['tvb_prefixes'])
DROP_LATIN_TOKENS = RULES['drop_latin_tokens']
SATELLITE_PRIORITY = RULES['satellite_priority']
CCTV_FOREIGN_SUFFIXES = RULES['cctv_foreign_suffixes']
STABILITY_HISTORY = load_history()
STRICT_DROP_NAME_TOKENS = [str(x) for x in QUALITY.get('strict_drop_name_tokens', [])]
STRICT_DROP_REGEX = [re.compile(str(x), re.I) for x in QUALITY.get('strict_drop_regex', [])]
CHANNEL_LIMITS = QUALITY.get('channel_limits', {})
GROUP_MAX_ROWS = {str(k): int(v) for k, v in QUALITY.get('group_max_rows', {}).items()}
CORE_CHANNEL_PATTERNS = [re.compile(str(x), re.I) for x in QUALITY.get('core_channel_patterns', [])]
QUALITY_SOURCE_BONUS = QUALITY.get('quality_source_bonus', {})
HOME_PRIORITY_ENABLED = bool(HOME_PRIORITY.get('enabled', True))
HOME_OK_URLS = {str(x).strip() for x in HOME_PRIORITY.get('home_ok_urls', []) if str(x).strip()}
HOME_FAILED_URLS = {str(x).strip() for x in HOME_PRIORITY.get('home_failed_urls', []) if str(x).strip()}
HOME_PRIORITY_BONUS = int(HOME_PRIORITY.get('bonus', -120))
HOME_PRIORITY_PENALTY = int(HOME_PRIORITY.get('penalty', 180))

def chinese_count(s: str) -> int:
    return shared_chinese_count(s)


def clean_name(name: str) -> str:
    name = (name or '').strip().replace(' ', '')
    # TXT playlist uses comma as delimiter; keep channel names delimiter-safe.
    name = name.replace(',', '\uFF0C')
    # CCTV1/CCTV1??/CCTV-1 -> CCTV-1/CCTV-1??
    name = re.sub(r'^CCTV[-_ ]?(\d+)(\+?)', r'CCTV-\1\2', name, flags=re.I)
    return name[:80]



def clean_url(url: str) -> str:
    url = (url or '').strip().strip('"').strip("'").lstrip('\ufeff')
    url = re.split(r'[;#](?=https?://)', url, maxsplit=1, flags=re.I)[0]
    url = url.rstrip(',')
    return url.strip()

def has_invalid_channel_name(name: str) -> bool:
    if not name:
        return True
    # Reject mojibake/replacement characters that make Ku9 show broken names
    # and indicate upstream decoding corruption.
    if '\ufffd' in name:
        return True
    # Reject control characters; tabs/newlines can corrupt TXT row structure.
    if any((ord(ch) < 32 or ord(ch) == 127) for ch in name):
        return True
    return False


def cctv_num(name: str):
    return cctv_number(name)


def is_core_channel_name(name: str) -> bool:
    n = (name or '').strip()
    return any(rx.search(n) for rx in CORE_CHANNEL_PATTERNS)


def strict_quality_drop_reason(name: str) -> str:
    n = name or ''
    low = n.lower()
    for token in STRICT_DROP_NAME_TOKENS:
        if token and token.lower() in low:
            return f"token:{token}"
    for rx in STRICT_DROP_REGEX:
        if rx.search(n):
            return f"regex:{rx.pattern}"
    return ''


def is_hk_mo_tw_channel(name: str, group: str = '') -> bool:
    n = name.strip()
    upper = n.upper()
    g = group or ''
    # Name-level Chinese markers are reliable.
    if any(k in n for k in HK_CN_KEYS):
        return True
    # Group-level HK/MO/TW markers are only trusted for Chinese channel names.
    # Some overseas collections put unrelated pure-English channels under a
    # broad HK/TW/overseas group; do not let that bypass the home-list filter.
    if chinese_count(n) > 0 and any(k in g for k in HK_CN_KEYS):
        return True
    # Latin abbreviations must appear as a clear brand prefix, not as an
    # accidental substring such as ABTVBariloche, StaraTVBandung or TVBrasil.
    if upper.startswith(HK_LATIN_PREFIXES):
        return True
    if upper.startswith(TVB_PREFIXES):
        return True
    if re.search(r'(^|[^A-Z0-9])(RTHK|VIUTV|TVB|TVBS|PHOENIX)([^A-Z0-9]|$)', upper):
        return True
    return False


def is_unwanted_overseas_english(name: str, group: str, source: str) -> bool:
    n = name.strip()
    upper = n.upper()
    # Keep real CCTV numeric channels before applying the pure-Latin home-list
    # filter; otherwise CCTV-1/CCTV-5 are incorrectly treated as English names.
    if cctv_num(n):
        return False
    if is_hk_mo_tw_channel(n, group):
        return False
    if any(tok in upper for tok in DROP_LATIN_TOKENS):
        return True
    # Pure Latin/number names are not useful in the home-facing mainland list
    # unless they are explicitly recognized HK/MO/TW brands.
    if chinese_count(n) == 0 and re.search(r'[A-Z]{3,}', upper):
        return True
    return False


def is_foreign_channel(name: str, group: str, source: str) -> bool:
    n = name.strip()
    lower = n.lower()
    upper = n.upper()
    if any(tok in upper for tok in FOREIGN_NAME_TOKENS):
        return True
    if any(tok in n for tok in FOREIGN_CN_TOKENS):
        return True
    # Explicit foreign-language/international news channels.
    if 'CGTN' in n.upper():
        return True
    if FOREIGN_LANG.search(n):
        return True
    # CCTV overseas English-suffixed variants, e.g. CCTV-4America/Asia/Europe.
    if cctv_num(n) and chinese_count(n) == 0 and any(x in lower for x in CCTV_FOREIGN_SUFFIXES):
        return True
    # Pure English/foreign names are removed, except numeric CCTV and HK/TW abbreviations.
    if chinese_count(n) == 0:
        if cctv_num(n):
            return False
        if is_hk_mo_tw_channel(n, group):
            return False
        return True
    return False




def is_unstable_or_wrong_alias(name: str, group: str, source: str) -> bool:
    n = name.strip()
    upper = n.upper()
    if any(tok in upper for tok in UNSTABLE_NAME_TOKENS):
        return True
    # Avoid pseudo-CCTV aliases such as CCTV-1(RTHK33) being placed in CCTV.
    if cctv_num(n) and any(tok.upper() in upper or tok in n for tok in CCTV_ALIAS_BLOCK_TOKENS):
        return True
    return False


def classify(name: str, group: str, source: str) -> str:
    if cctv_num(name):
        return G_CCTV
    if "\u536b\u89c6" in name:
        return G_SAT
    if any(k in name for k in HK_KEYS) or any(k in group for k in GROUP_KEYS['hk']):
        return G_HK
    if any(p in name for p in PROVINCES) or any(k in group for k in GROUP_KEYS['local']):
        return G_LOCAL
    # Merge former movie/entertainment and other miscellaneous channels into a few broad categories.
    if any(k in name for k in MOVIE_KEYS) or any(k in group for k in GROUP_KEYS['movie']):
        return G_MOVIE
    if any(k in name for k in KIDS_KEYS) or any(k in group for k in GROUP_KEYS['kids']):
        return G_KIDS
    if any(k in name for k in SPORT_DOC_KEYS) or any(k in group for k in GROUP_KEYS['sport_doc']):
        return G_SPORT_DOC
    if any(k in name for k in MUSIC_SHOW_KEYS) or any(k in group for k in GROUP_KEYS['music_show']):
        return G_MUSIC_SHOW
    if any(k in name for k in LIFE_KEYS):
        return G_LIFE
    if re.search(r'[A-Za-z]{4,}', group or ''):
        return G_OVERSEA if chinese_count(name) > 0 else G_ENT
    return G_ENT


def source_priority(source: str, url: str = '') -> int:
    """Lower is better. Kept as wrapper for tests and sorting code."""
    return configured_source_priority(source, url)


def home_priority_adjustment(url: str) -> int:
    if not HOME_PRIORITY_ENABLED:
        return 0
    if url in HOME_OK_URLS:
        return HOME_PRIORITY_BONUS
    if url in HOME_FAILED_URLS:
        return HOME_PRIORITY_PENALTY
    return 0


def url_score(url: str, source: str):
    s = source_priority(source, url)
    adjust = score_adjustments('curate')
    if url.startswith('http://'):
        s += adjust.get('http_url', -20)
    if 'epg.pw' in url:
        s += adjust.get('epg_pw', 20)
    if '[' in url or 'ipv6' in (source or '').lower():
        s += adjust.get('ipv6_source_or_literal', 20)
    if 'migu' in url.lower():
        s += adjust.get('migu_url', 5)
    source_bonus_tokens = [str(x).lower() for x in QUALITY_SOURCE_BONUS.get('official_domain_contains', [])]
    if source_bonus_tokens and any(x in (url or '').lower() or x in (source or '').lower() for x in source_bonus_tokens):
        s += int(QUALITY_SOURCE_BONUS.get('bonus', -8))
    if stability_enabled():
        s += stability_adjustment(url, STABILITY_HISTORY)
    s += home_priority_adjustment(url)
    return (s, len(url), source)


def per_channel_limit(group: str, name: str) -> int:
    limits = CHANNEL_LIMITS
    if is_core_channel_name(name):
        return int(limits.get('core_max_urls_per_name', 6))
    if group == G_CCTV:
        return int(limits.get('cctv_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_SAT:
        return int(limits.get('satellite_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_LOCAL:
        return int(limits.get('local_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_MOVIE:
        return int(limits.get('movie_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_KIDS:
        return int(limits.get('kids_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_SPORT_DOC:
        return int(limits.get('sport_doc_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_MUSIC_SHOW:
        return int(limits.get('music_show_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_LIFE:
        return int(limits.get('life_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_HK:
        return int(limits.get('hk_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_OVERSEA:
        return int(limits.get('oversea_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    if group == G_ENT:
        return int(limits.get('entertainment_max_urls_per_name', limits.get('default_max_urls_per_name', 3)))
    return int(limits.get('default_max_urls_per_name', 3))


def apply_group_limits(pub: list[tuple[str, str, str, str]]) -> tuple[list[tuple[str, str, str, str]], dict[str, int]]:
    trimmed: dict[str, int] = {}
    limited: list[tuple[str, str, str, str]] = []
    seen_groups = list(GROUP_ORDER) + sorted({g for g, _, _, _ in pub} - set(GROUP_ORDER))
    for group in seen_groups:
        part = [x for x in pub if x[0] == group]
        if not part:
            continue
        limit = GROUP_MAX_ROWS.get(group, 0)
        if limit <= 0 or len(part) <= limit:
            limited.extend(part)
            continue
        core = [x for x in part if is_core_channel_name(x[1])]
        ordinary = [x for x in part if not is_core_channel_name(x[1])]
        keep_slots = max(0, limit - len(core))
        keep = core + ordinary[:keep_slots]
        # Never let category limits remove required CCTV/important satellite rows.
        trimmed[group] = len(part) - len(keep)
        limited.extend(keep)
    return limited, trimmed


BAD_NAME_TOKENS = RULES['bad_name_tokens']


def has_abnormal_channel_name(name: str) -> bool:
    """Reject names that can corrupt Ku9 TXT rows or indicate bad decoding."""
    n = name or ''
    low = n.lower()
    if not n.strip():
        return True
    # Unicode replacement character means the upstream name was decoded badly.
    # Do not publish it as a channel name; it is confusing on TV and shows that
    # the row is not cleanly generated.
    if '\ufffd' in n:
        return True
    if any(ch in n for ch in ['\r', '\n', '\t']):
        return True
    if any((ord(ch) < 32 or ord(ch) == 127) for ch in n):
        return True
    if ',' in n:
        return True
    if re.search(r'https?://', n, re.I):
        return True
    if n.endswith('#genre#'):
        return True
    if any(tok.lower() in low for tok in BAD_NAME_TOKENS):
        return True
    return False


def validate_final_rows(text: str) -> None:
    validate_text(text, require_categories=True)


def sort_key(item):
    group, name, url, source = item
    gi = GROUP_ORDER.index(group) if group in GROUP_ORDER else 99
    if group == G_CCTV:
        return (gi, cctv_sort_key(name), url_score(url, source))
    if group == G_SAT:
        pi = SATELLITE_PRIORITY.index(name) if name in SATELLITE_PRIORITY else 99
        return (gi, pi, name, url_score(url, source))
    return (gi, name, url_score(url, source))


def main():
    rows = []
    drop_counts = Counter()
    strict_drop_reasons = Counter()
    with IN.open(encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r.get('ok') != 'True':
                continue
            name = clean_name(r.get('name', ''))
            url = clean_url(r.get('url', '') or '')
            group = r.get('group', '') or ''
            source = r.get('source', '') or ''
            if has_invalid_channel_name(name) or not url.startswith(('http://', 'https://')):
                drop_counts['invalid_name_or_url'] += 1
                continue
            if has_abnormal_channel_name(name):
                drop_counts['abnormal_channel_name'] += 1
                continue
            if 'cgtn' in url.lower():
                drop_counts['cgtn_url'] += 1
                continue
            if is_unstable_or_wrong_alias(name, group, source):
                drop_counts['unstable_or_wrong_alias'] += 1
                continue
            strict_reason = strict_quality_drop_reason(name)
            if strict_reason:
                drop_counts['strict_quality_filter'] += 1
                strict_drop_reasons[strict_reason] += 1
                continue
            if is_unwanted_overseas_english(name, group, source):
                drop_counts['unwanted_overseas_english'] += 1
                continue
            if is_foreign_channel(name, group, source):
                drop_counts['foreign_channel'] += 1
                continue
            g = classify(name, group, source)
            if g == G_OVERSEA and chinese_count(name) == 0:
                drop_counts['oversea_latin_name'] += 1
                continue
            rows.append((g, name, url, source))

    by = defaultdict(list)
    seen = set()
    for row in rows:
        g, n, u, s = row
        if (n, u) in seen:
            continue
        seen.add((n, u))
        by[n].append(row)

    pub = []
    channel_limit_trimmed = 0
    channel_limit_stats = Counter()
    for n, arr in by.items():
        arr = sorted(arr, key=lambda x: (url_score(x[2], x[3]), sort_key(x)))
        limit = max(1, per_channel_limit(arr[0][0], n))
        if len(arr) > limit:
            channel_limit_trimmed += len(arr) - limit
            channel_limit_stats[arr[0][0]] += len(arr) - limit
        pub.extend(arr[:limit])
    pub.sort(key=sort_key)
    pub, group_limit_trimmed = apply_group_limits(pub)
    pub.sort(key=sort_key)
    with CURATED_SOURCE_MAP.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['group', 'name', 'url', 'source'])
        for g, n, u, s in pub:
            w.writerow([g, n, u, s])

    lines = []
    for g in GROUP_ORDER:
        part = [x for x in pub if x[0] == g]
        if not part:
            continue
        if lines:
            lines.append('')
        lines.append(f'{g},#genre#')
        for _, n, u, s in part:
            lines.append(f'{n},{u}')
    text = '\n'.join(lines).strip() + '\n'
    validate_final_rows(text)
    for fn in ['live-curated.txt', 'live-verified.txt', 'live.txt', 'ku9-live.txt']:
        (ROOT / fn).write_bytes(text.encode('utf-8'))

    m = ['#EXTM3U']
    for g, n, u, s in pub:
        m.append(format_extinf(n, g))
        m.append(u)
    (ROOT / 'live.m3u').write_text('\n'.join(m) + '\n', encoding='utf-8', newline='\n')

    cnt = Counter(g for g, _, _, _ in pub)
    source_cnt = Counter(src for _, _, _, src in pub)
    group_source_cnt = Counter((g, src) for g, _, _, src in pub)
    per_group_unique_names = {g: len({n for gg, n, _, _ in pub if gg == g}) for g in GROUP_ORDER}
    published_unique_names = len({n for _, n, _, _ in pub})
    summary_path = ROOT / 'full-check-summary.json'
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text(encoding='utf-8'))
        except Exception:
            summary = {}
    else:
        summary = {}
    summary.update({
        'pre_recheck_curated_lines': len(pub),
        'pre_recheck_curated_channel_names': published_unique_names,
        'pre_recheck_curated_groups': dict(cnt),
        'pre_recheck_curated_sources': dict(source_cnt),
        'pre_recheck_per_group_unique_names': per_group_unique_names,
        'stability_history_loaded': stability_enabled(),
        'stability_history_urls': len((STABILITY_HISTORY.get('urls') or {})),
        'home_priority': {
            'enabled': HOME_PRIORITY_ENABLED,
            'ok_urls': len(HOME_OK_URLS),
            'failed_urls': len(HOME_FAILED_URLS),
            'bonus': HOME_PRIORITY_BONUS,
            'penalty': HOME_PRIORITY_PENALTY,
        },
        'curated_generated': True,
        'curated_published_lines': len(pub),
        'curated_channel_names': published_unique_names,
        'curated_groups': dict(cnt),
        'curated_sources': dict(source_cnt),
        'per_group_unique_names': per_group_unique_names,
        'quality_limits_applied': {
            'config_file': 'config/quality.json',
            'channel_limit_trimmed_rows': channel_limit_trimmed,
            'channel_limit_trimmed_by_group': dict(channel_limit_stats),
            'group_limit_trimmed_counts': group_limit_trimmed,
            'strict_filter_dropped_rows': int(drop_counts.get('strict_quality_filter', 0)),
            'drop_counts': dict(drop_counts),
            'top_strict_drop_reasons': dict(strict_drop_reasons.most_common(20)),
            'group_max_rows': GROUP_MAX_ROWS,
            'channel_limits': CHANNEL_LIMITS,
        },
        'final_primary_file': 'live-curated.txt',
        'final_primary_published_lines': len(pub),
        # Keep this legacy field aligned with the final TV-facing playlist after curation.
        'primary_published_lines': len(pub),
    })
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

    report = [
        '# Pre-recheck curated Ku9 playlist report',
        '',
        'This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.',
        '',
        f'Pre-recheck candidate lines: {len(pub)}',
        f'Published channel names: {published_unique_names}',
        f'Stability history URLs loaded: {len((STABILITY_HISTORY.get("urls") or {}))}',
        f'Home priority URLs loaded: ok={len(HOME_OK_URLS)}, failed={len(HOME_FAILED_URLS)}, enabled={HOME_PRIORITY_ENABLED}',
        '',
        '## Quality filters and limits',
        '',
        f'- Strict quality filter dropped rows: {int(drop_counts.get("strict_quality_filter", 0))}',
        f'- Channel limit trimmed rows: {channel_limit_trimmed}',
        f'- Group limit trimmed rows: {sum(group_limit_trimmed.values())}',
        f'- Quality config: `config/quality.json`',
        '',
        '### Drop counts',
        '',
    ]
    for reason, amount in drop_counts.most_common():
        report.append(f'- {reason}: {amount}')
    report += ['', '### Group limit trims', '']
    if group_limit_trimmed:
        for group, amount in sorted(group_limit_trimmed.items(), key=lambda x: (-x[1], x[0])):
            report.append(f'- {group}: {amount}')
    else:
        report.append('- none')
    report += ['', '## Groups']
    for g in GROUP_ORDER:
        if cnt[g]:
            report.append(f'- {g}: {cnt[g]}')
    report += ['', '## Final published lines by source', '', '| Source | Lines |', '|---|---:|']
    for src, n in source_cnt.most_common():
        report.append(f'| {src} | {n} |')
    report += ['', '## Top sources per group', '']
    for g in GROUP_ORDER:
        top = [(src, n) for (gg, src), n in group_source_cnt.items() if gg == g]
        if not top:
            continue
        report.append(f'### {g}')
        for src, n in sorted(top, key=lambda x: (-x[1], x[0]))[:8]:
            report.append(f'- {src}: {n}')
        report.append('')
    report += ['', '## Rules', '- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...', '- Mainland CCTV/satellite/local channels first', '- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later', '- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese', '- English/foreign-language channels removed', '- English category names removed', '- Not24/7 and obvious unstable entries removed from TV-facing playlist', '- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV']
    (ROOT / 'curated-report.md').write_text('\n'.join(report) + '\n', encoding='utf-8', newline='\n')
    print('published', len(pub), 'names', published_unique_names, 'bytes', len(text.encode('utf-8')))
    for g in GROUP_ORDER:
        print(g.encode('unicode_escape').decode(), cnt[g])


if __name__ == '__main__':
    main()
