#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import csv, json, os, re, shutil, subprocess
from pathlib import Path
from collections import defaultdict, Counter
from validate_playlist import validate_text
from playlist_config import get_group_order, load_guard, load_home_priority, load_quality, load_rules, score_adjustments, source_priority as configured_source_priority
from stability import load_history, stability_adjustment, stability_enabled
from channel_utils import cctv_key, cctv_number, cctv_sort_key, chinese_count as shared_chinese_count, format_extinf, is_latin_noise_name
from channel_identity import aliases_are_compatible, canonical_channel_key, is_audio_only_channel
from url_utils import is_publishable_http_url, normalize_stream_url

ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / "stream_check_results.csv"
RULES_PATH = ROOT / "config" / "rules.json"
CURATED_SOURCE_MAP = ROOT / "curated-source-map.csv"
CURATED_CANDIDATE_POOL = ROOT / "curated-candidate-pool.csv"
ALIAS_CONFLICT_REPORT = ROOT / "alias-conflict-report.md"

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
GUARD = load_guard()
HOME_PRIORITY = load_home_priority()
PROVINCES = RULES['provinces']
HK_KEYS = RULES['category_keywords']['hk']
MOVIE_KEYS = RULES['category_keywords']['movie']
KIDS_KEYS = RULES['category_keywords']['kids']
SPORT_DOC_KEYS = RULES['category_keywords']['sport_doc']
MUSIC_SHOW_KEYS = RULES['category_keywords']['music_show']
LIFE_KEYS = RULES['category_keywords']['life']
GROUP_KEYS = RULES['group_keywords']
OVERSEAS_SOURCE_NAMES = {str(x) for x in RULES.get('overseas_source_names', [])}
OVERSEAS_GROUP_TOKENS = tuple(str(x).lower() for x in RULES.get('overseas_group_tokens', []))
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
HISTORICAL_FALLBACK = GUARD.get('historical_fallback') or {}
HISTORICAL_FALLBACK_ENABLED = bool(HISTORICAL_FALLBACK.get('enabled', False))
HISTORICAL_FALLBACK_GROUPS = {
    str(group) for group in HISTORICAL_FALLBACK.get('groups', []) if str(group).strip()
}
HISTORICAL_FALLBACK_MAX_CANDIDATES = max(
    0, int(HISTORICAL_FALLBACK.get('max_candidates', 0) or 0)
)

def chinese_count(s: str) -> int:
    return shared_chinese_count(s)


def clean_name(name: str) -> str:
    name = (name or '').strip().replace(' ', '')
    # TXT playlist uses comma as delimiter; keep channel names delimiter-safe.
    name = name.replace(',', '\uFF0C')
    # CCTV1/CCTV-1 -> CCTV-1, and collapse resolution aliases to the exact
    # canonical name so one channel receives one shared line quota.
    name = re.sub(r'^CCTV[-_ ]?(\d+)(\+?)', r'CCTV-\1\2', name, flags=re.I)
    exact = cctv_key(name)
    return (exact or name)[:80]


def clean_url(url: str) -> str:
    return normalize_stream_url(url)


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
    if QUALITY.get('drop_audio_only_channels', True) and is_audio_only_channel(n):
        return 'audio-only:radio'
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
    province_station_name = (
        any(p in name for p in PROVINCES)
        and not re.search(r'[，,。！？：:、；;]', name)
    )
    if (
        province_station_name
        or any(k in group for k in GROUP_KEYS['local'])
        or re.search(r'(?:\u65b0\u95fb\u7efc\u5408|\u65b0\u95fb\u9891\u9053|\u516c\u5171\u9891\u9053|\u7efc\u5408\u9891\u9053|\u516c\u5171\u53f0|\u7efc\u5408\u53f0)$', name)
    ):
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
    # An English upstream group label does not prove that a Chinese-titled
    # stream is overseas. Rotation sources commonly use generic Latin group
    # names for mainland films and shows. Only explicit overseas collections
    # plus an overseas-language group marker may select the overseas bucket.
    group_lower = (group or '').lower()
    if (
        source in OVERSEAS_SOURCE_NAMES
        and chinese_count(name) > 0
        and any(token in group_lower for token in OVERSEAS_GROUP_TOKENS)
    ):
        return G_OVERSEA
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


def prepare_curated_row(
    raw_name: str,
    raw_url: str,
    raw_group: str,
    source: str,
) -> tuple[tuple[str, str, str, str] | None, str, str]:
    """Apply the complete current publication hygiene policy to one row.

    The same function is used for fresh upstream rows and previous-publication
    fallback candidates. This prevents a policy change from silently restoring
    a row that the current curation rules would reject.
    """
    name = clean_name(raw_name)
    url = clean_url(raw_url)
    group = raw_group or ''
    source = source or ''
    if has_invalid_channel_name(name) or not is_publishable_http_url(url):
        return None, 'invalid_name_or_url', ''
    if has_abnormal_channel_name(name):
        return None, 'abnormal_channel_name', ''
    if 'cgtn' in url.lower():
        return None, 'cgtn_url', ''
    if is_unstable_or_wrong_alias(name, group, source):
        return None, 'unstable_or_wrong_alias', ''
    strict_reason = strict_quality_drop_reason(name)
    if strict_reason:
        return None, 'strict_quality_filter', strict_reason
    if is_unwanted_overseas_english(name, group, source):
        return None, 'unwanted_overseas_english', ''
    if is_foreign_channel(name, group, source):
        return None, 'foreign_channel', ''
    if is_latin_noise_name(name):
        return None, 'latin_noise_name', ''
    curated_group = classify(name, group, source)
    if curated_group == G_OVERSEA and chinese_count(name) == 0:
        return None, 'oversea_latin_name', ''
    return (curated_group, name, url, source), '', ''


def git_show_text(spec: str) -> str:
    git = os.getenv('GIT_CMD') or shutil.which('git') or 'git'
    try:
        data = subprocess.check_output([git, 'show', spec], cwd=ROOT, stderr=subprocess.DEVNULL)
        return data.decode('utf-8')
    except Exception:
        return ''


def parse_tv_txt_rows(text: str) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    group = ''
    for raw in (text or '').splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.endswith(',#genre#'):
            group = line.split(',', 1)[0].strip()
            continue
        if not group or ',' not in line:
            continue
        name, url = line.split(',', 1)
        rows.append((group, name.strip(), url.strip()))
    return rows


def historical_fallback_rows() -> list[tuple[str, str, str, str]]:
    """Load last publication rows as candidates, never as trusted output.

    These rows are appended only to the candidate pool. recheck_published.py
    must prove current video bytes and live progress before any row can return
    to the television playlist.
    """
    if not HISTORICAL_FALLBACK_ENABLED or not HISTORICAL_FALLBACK_GROUPS:
        return []
    history_urls = STABILITY_HISTORY.get('urls') or {}
    prepared: list[tuple[str, str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    for old_group, old_name, old_url in parse_tv_txt_rows(git_show_text('HEAD:live-curated.txt')):
        entry = history_urls.get(clean_url(old_url)) or {}
        source = str(entry.get('last_source') or 'previous_publication')
        row, _reason, _strict_reason = prepare_curated_row(old_name, old_url, old_group, source)
        if row is None or row[0] not in HISTORICAL_FALLBACK_GROUPS:
            continue
        key = (selection_key(row[1]), row[2])
        if key in seen:
            continue
        seen.add(key)
        prepared.append(row)
    prepared.sort(key=sort_key)
    if HISTORICAL_FALLBACK_MAX_CANDIDATES > 0:
        prepared = prepared[:HISTORICAL_FALLBACK_MAX_CANDIDATES]
    return prepared


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


def candidate_pool_sort_key(item: tuple[str, str, str, str, str, str]):
    key, group, _name, url, source, origin = item
    return (
        GROUP_ORDER.index(group) if group in GROUP_ORDER else 99,
        key,
        0 if origin == 'current_scan' else 1,
        url_score(url, source),
    )


def alias_choice_score(row: tuple[str, str, str, str]):
    group, name, url, source = row
    exact = cctv_key(name)
    group_rank = GROUP_ORDER.index(group) if group in GROUP_ORDER else 99
    return (
        0 if exact == name else 1,
        0 if is_core_channel_name(name) else 1,
        group_rank,
        len(name),
        url_score(url, source),
        name,
    )


def resolve_url_aliases(rows: list[tuple[str, str, str, str]]) -> tuple[list[tuple[str, str, str, str]], list[dict]]:
    """Enforce one unambiguous channel identity per published URL."""
    by_url: dict[str, list[tuple[str, str, str, str]]] = defaultdict(list)
    for row in rows:
        by_url[row[2]].append(row)
    resolved: list[tuple[str, str, str, str]] = []
    conflicts: list[dict] = []
    for url, aliases in by_url.items():
        # First choose the best source for an identical name+URL pair.
        by_name: dict[str, tuple[str, str, str, str]] = {}
        for row in aliases:
            current = by_name.get(row[1])
            if current is None or alias_choice_score(row) < alias_choice_score(current):
                by_name[row[1]] = row
        unique_aliases = list(by_name.values())
        names = [row[1] for row in unique_aliases]
        if aliases_are_compatible(names):
            resolved.append(min(unique_aliases, key=alias_choice_score))
            continue
        conflicts.append({
            'url': url,
            'aliases': [
                {'group': group, 'name': name, 'source': source}
                for group, name, _url, source in sorted(unique_aliases, key=alias_choice_score)
            ],
        })
    return resolved, conflicts


def write_alias_conflict_report(conflicts: list[dict], input_rows: int, resolved_rows: int) -> None:
    lines = [
        '# URL/channel identity conflict report',
        '',
        'A playable URL is excluded when upstream lists assign it to multiple incompatible channel identities.',
        'This is intentionally conservative: media availability alone cannot prove the video content is the named channel.',
        '',
        f'Input eligible rows: {input_rows}',
        f'Resolved unambiguous URL rows: {resolved_rows}',
        f'Conflicting URLs excluded: {len(conflicts)}',
        f'Alias rows excluded by conflicts: {sum(len(item["aliases"]) for item in conflicts)}',
        '',
        '## Conflicts',
        '',
    ]
    if not conflicts:
        lines.append('- none')
    for item in conflicts[:300]:
        labels = '; '.join(f"{alias['group']} / {alias['name']} / {alias['source']}" for alias in item['aliases'])
        lines.append(f"- {item['url']} :: {labels}")
    ALIAS_CONFLICT_REPORT.write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')


def selection_key(name: str) -> str:
    return canonical_channel_key(name)


def main():
    rows = []
    drop_counts = Counter()
    strict_drop_reasons = Counter()
    with IN.open(encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r.get('ok') != 'True':
                continue
            row, reason, strict_reason = prepare_curated_row(
                r.get('name', ''),
                r.get('url', '') or '',
                r.get('group', '') or '',
                r.get('source', '') or '',
            )
            if row is None:
                drop_counts[reason] += 1
                if strict_reason:
                    strict_drop_reasons[strict_reason] += 1
                continue
            rows.append(row)

    resolved_rows, alias_conflicts = resolve_url_aliases(rows)
    write_alias_conflict_report(alias_conflicts, len(rows), len(resolved_rows))
    if alias_conflicts:
        drop_counts['ambiguous_url_identity'] += sum(len(item['aliases']) for item in alias_conflicts)

    by = defaultdict(list)
    for row in resolved_rows:
        by[selection_key(row[1])].append(row)

    # Normalize all URLs of one canonical channel to a single display name and
    # group. This prevents resolution aliases from receiving separate quotas.
    candidate_pool: list[tuple[str, str, str, str, str, str]] = []
    normalized_by_key: dict[str, list[tuple[str, str, str, str]]] = {}
    for key, arr in by.items():
        representative = min(arr, key=alias_choice_score)
        normalized = [
            (representative[0], representative[1], url, source)
            for _group, _name, url, source in arr
        ]
        normalized = sorted(normalized, key=lambda x: (url_score(x[2], x[3]), sort_key(x)))
        normalized_by_key[key] = normalized
        candidate_pool.extend((key, group, name, url, source, 'current_scan') for group, name, url, source in normalized)

    # The last published protected-channel rows are recovery candidates only.
    # Exclude every URL already present in the current pool, including URLs
    # currently mapped to a different identity, so historical data cannot
    # override fresh alias-conflict evidence.
    historical_rows = historical_fallback_rows()
    current_urls = {url for _key, _group, _name, url, _source, _origin in candidate_pool}
    current_key_urls = {(key, url) for key, _group, _name, url, _source, _origin in candidate_pool}
    historical_added = 0
    for group, name, url, source in historical_rows:
        key = selection_key(name)
        if url in current_urls or (key, url) in current_key_urls:
            continue
        if key in normalized_by_key:
            representative = normalized_by_key[key][0]
            group, name = representative[0], representative[1]
        candidate_pool.append((key, group, name, url, source, 'previous_publication'))
        current_urls.add(url)
        current_key_urls.add((key, url))
        historical_added += 1

    with CURATED_CANDIDATE_POOL.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(['selection_key', 'group', 'name', 'url', 'source', 'origin'])
        for key, group, name, url, source, origin in sorted(
            candidate_pool,
            key=candidate_pool_sort_key,
        ):
            w.writerow([key, group, name, url, source, origin])

    pub = []
    channel_limit_trimmed = 0
    channel_limit_stats = Counter()
    for key, arr in normalized_by_key.items():
        name = arr[0][1]
        limit = max(1, per_channel_limit(arr[0][0], name))
        if len(arr) > limit:
            channel_limit_trimmed += len(arr) - limit
            channel_limit_stats[arr[0][0]] += len(arr) - limit
        pub.extend(arr[:limit])
    pub.sort(key=sort_key)
    pub, group_limit_trimmed = apply_group_limits(pub)
    pub.sort(key=sort_key)
    with CURATED_SOURCE_MAP.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, lineterminator="\n")
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
            'configured': bool(HOME_PRIORITY.get('_configured', False)),
            'active': bool(HOME_PRIORITY.get('_active', False)),
            'fresh': bool(HOME_PRIORITY.get('_fresh', True)),
            'stale_reason': str(HOME_PRIORITY.get('_stale_reason', '')),
            'age_hours': HOME_PRIORITY.get('_age_hours'),
            'max_age_hours': int(HOME_PRIORITY.get('max_age_hours', 14 * 24)),
            'generated_at_utc': str(HOME_PRIORITY.get('generated_at_utc', '')),
            'expires_at_utc': str(HOME_PRIORITY.get('expires_at_utc', '')),
            'configured_ok_urls': int(HOME_PRIORITY.get('_configured_ok_urls', 0)),
            'configured_failed_urls': int(HOME_PRIORITY.get('_configured_failed_urls', 0)),
            'ok_urls': len(HOME_OK_URLS),
            'failed_urls': len(HOME_FAILED_URLS),
            'bonus': HOME_PRIORITY_BONUS,
            'penalty': HOME_PRIORITY_PENALTY,
        },
        'curated_generated': True,
        'curated_source_map_available': bool(pub),
        'curated_source_map_generated': True,
        'curated_source_map_artifact_only': True,
        'curated_candidate_pool_generated': True,
        'curated_candidate_pool_artifact_only': True,
        'historical_fallback_candidates': {
            'enabled': HISTORICAL_FALLBACK_ENABLED,
            'groups': sorted(HISTORICAL_FALLBACK_GROUPS),
            'previous_rows_eligible': len(historical_rows),
            'added_to_candidate_pool': historical_added,
            'requires_current_media_recheck': True,
        },
        'curated_published_lines': len(pub),
        'curated_channel_names': published_unique_names,
        'curated_groups': dict(cnt),
        'curated_sources': dict(source_cnt),
        'per_group_unique_names': per_group_unique_names,
        'alias_resolution': {
            'conflicting_urls_excluded': len(alias_conflicts),
            'conflicting_alias_rows_excluded': sum(len(item['aliases']) for item in alias_conflicts),
            'report_file': ALIAS_CONFLICT_REPORT.name,
            'candidate_pool_file': CURATED_CANDIDATE_POOL.name,
        },
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
