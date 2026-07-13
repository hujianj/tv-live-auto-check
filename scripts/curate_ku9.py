#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import csv, json, re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / "stream_check_results.csv"

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
GROUP_ORDER = [G_CCTV, G_SAT, G_LOCAL, G_MOVIE, G_KIDS, G_SPORT_DOC, G_MUSIC_SHOW, G_LIFE, G_ENT, G_HK, G_OVERSEA]

PROVINCES = "\u5317\u4eac \u5929\u6d25 \u6cb3\u5317 \u5c71\u897f \u5185\u8499\u53e4 \u8fbd\u5b81 \u5409\u6797 \u9ed1\u9f99\u6c5f \u4e0a\u6d77 \u6c5f\u82cf \u6d59\u6c5f \u5b89\u5fbd \u798f\u5efa \u6c5f\u897f \u5c71\u4e1c \u6cb3\u5357 \u6e56\u5317 \u6e56\u5357 \u5e7f\u4e1c \u5e7f\u897f \u6d77\u5357 \u91cd\u5e86 \u56db\u5ddd \u8d35\u5dde \u4e91\u5357 \u897f\u85cf \u9655\u897f \u7518\u8083 \u9752\u6d77 \u5b81\u590f \u65b0\u7586 \u6df1\u5733 \u53a6\u95e8 \u5175\u56e2 \u82cf\u5dde \u5e7f\u5dde \u5357\u4eac \u676d\u5dde".split()
ENT_KEYS = "\u7535\u5f71 \u5f71\u9662 \u5267\u573a \u7535\u89c6\u5267 \u5f71\u89c6 \u52a8\u753b \u52a8\u6f2b \u5361\u901a \u5c11\u513f \u7efc\u827a \u97f3\u4e50 \u4f53\u80b2 \u8db3\u7403 \u7bee\u7403 \u7eaa\u5b9e \u7eaa\u5f55 \u751f\u6d3b \u7f8e\u98df \u6e38\u620f \u7535\u7ade \u8f6e\u64ad \u864e\u7259 \u6597\u9c7c \u54d4\u54e9 \u6625\u665a \u76f8\u58f0 \u5c0f\u54c1 \u65b0\u95fb \u8d22\u7ecf \u6cd5\u6cbb \u79d1\u6559 \u620f\u66f2 \u6587\u5316 \u65c5\u6e38 \u90fd\u5e02 \u516c\u5171 \u519c\u4e1a".split()
HK_KEYS = "\u9999\u6e2f \u6fb3\u95e8 \u53f0\u6e7e \u51e4\u51f0 \u7fe1\u7fe0 \u660e\u73e0 TVB ViuTV RTHK \u6c11\u89c6 \u4e2d\u89c6 \u534e\u89c6 \u53f0\u89c6 \u4e1c\u68ee \u4e09\u7acb \u4e2d\u5929 TVBS \u5bf0\u5b87".split()
MOVIE_KEYS = "\u7535\u5f71 \u5f71\u9662 \u5267\u573a \u7535\u89c6\u5267 \u5f71\u89c6 \u5267\u96c6 \u5267 \u6b66\u4fa0 \u5c04\u96d5 \u5510\u671d\u8be1\u5b9e\u5f55".split()
KIDS_KEYS = "\u5c11\u513f \u513f\u7ae5 \u52a8\u753b \u52a8\u6f2b \u5361\u901a \u5b9d\u5b9d \u5c0f\u670b\u53cb".split()
SPORT_DOC_KEYS = "\u4f53\u80b2 \u8db3\u7403 \u7bee\u7403 \u4e52\u4e53 \u7fbd\u6bdb\u7403 \u53f0\u7403 \u516b\u7403 \u5965\u6797\u5339\u514b \u7eaa\u5b9e \u7eaa\u5f55 \u63a2\u7d22 \u5730\u7406 \u7ade\u6280 \u8d5b".split()
MUSIC_SHOW_KEYS = "\u97f3\u4e50 \u6b4c \u6f14\u5531\u4f1a \u7efc\u827a \u6625\u665a \u76f8\u58f0 \u5c0f\u54c1 \u620f\u66f2 \u4eac\u5267 \u66f2\u827a".split()
LIFE_KEYS = "\u751f\u6d3b \u7f8e\u98df \u65c5\u6e38 \u6587\u5316 \u90fd\u5e02 \u516c\u5171 \u519c\u4e1a \u8d22\u7ecf \u65b0\u95fb \u6cd5\u6cbb \u79d1\u6559 \u5065\u5eb7 \u5bb6\u5ead \u6c7d\u8f66 \u623f \u8336 \u5c55 \u5b66 \u753b\u753b \u6a21\u578b \u5ba0\u7269".split()
FOREIGN_LANG = re.compile(r"\b(CGTN|CCTV\+|CCTVPLUS|DW|BBC|CNN|NHK|KBS|ARIRANG|FRANCE24|ALJAZEERA|TRT|VOA|BLOOMBERG|CNBC|FOX|ABC|NBC|CBS|PBS)\b", re.I)
# Match foreign/non-mainland channel brands in channel names even when they are
# glued to Chinese words or resolution suffixes, e.g. TVBRICSEnglish, 纪录|BBCEarth.
FOREIGN_NAME_TOKENS = [
    "CGTN", "CCTVPLUS", "CCTV+", "BBC", "CNN", "NHK", "KBS", "ARIRANG",
    "FRANCE24", "ALJAZEERA", "BLOOMBERG", "CNBC", "TVBRICS", "DW", "VOA",
    "FOX", "PBS", "TRT", "EURONEWS", "DEUTSCHE", "RUSSIA", "AFRICA",
    "ENGLISH", "FRANCAIS", "ESPANOL", "ARABIC", "RUSSIAN", "KOREA",
    "JAPAN", "THAILAND", "VIETNAM", "INDIA", "INDONESIA", "MALAYSIA",
    "SINGAPORE", "AMERICA", "EUROPE",
]
FOREIGN_CN_TOKENS = ["阿里郎", "环球电视", "朝鲜", "韩国", "日本", "俄罗斯", "非洲", "欧洲", "美洲"]
UNSTABLE_NAME_TOKENS = ["NOT24/7", "NOT 24/7", "[NOT24/7]", "\u6d4b\u8bd5", "\u505c\u64ad", "\u7ef4\u62a4", "OFFLINE"]
CCTV_ALIAS_BLOCK_TOKENS = ["RTHK", "TVB", "VIUTV", "\u6e2f\u53f0", "\u9999\u6e2f", "\u6fb3\u95e8", "\u6fb3\u9580", "\u53f0\u6e7e", "\u53f0\u7063", "\u51e4\u51f0", "\u9cf3\u51f0", "\u7fe1\u7fe0", "\u660e\u73e0"]
HK_CN_KEYS = ["\u9999\u6e2f", "\u6fb3\u95e8", "\u6fb3\u9580", "\u53f0\u6e7e", "\u53f0\u7063", "\u6e2f\u53f0", "\u51e4\u51f0", "\u9cf3\u51f0", "\u7fe1\u7fe0", "\u660e\u73e0", "\u6c11\u89c6", "\u4e2d\u89c6", "\u534e\u89c6", "\u53f0\u89c6", "\u4e1c\u68ee", "\u4e09\u7acb", "\u4e2d\u5929"]
HK_LATIN_PREFIXES = ("RTHK", "VIUTV", "TVBS", "PHOENIX")
DROP_LATIN_TOKENS = [
    "PLUTOTV", "PLUTO", "REDBULL", "BUDAPEST", "BOGOTA", "BRASIL", "BRAZIL",
    "BULGARIA", "BULGARIAONAIR", "BANGLA", "MOVIEBANGLA", "NEWS18BANGLA",
    "NEWS21BANGLA", "BRESCIA", "BREMEN", "BODENSEE", "BANDUNG",
    "BOJONEGORO", "BARILOCHE", "ASUNCION", "LIONSGATE", "WEDOTV",
    "EBONYTV", "CITYTV", "PEACETV", "PENIEL", "STASHTV", "SUPERTV",
    "CONECTV", "CREATV", "DELTATV", "RTVBN", "RADIO", "MTV",
    "NICKELODEON", "NICKJR", "NICKTOONS", "CIN?", "CINE",
]


def chinese_count(s: str) -> int:
    return sum(1 for ch in s if '\u4e00' <= ch <= '\u9fff')


def clean_name(name: str) -> str:
    name = (name or '').strip().replace(' ', '')
    # TXT playlist uses comma as delimiter; keep channel names delimiter-safe.
    name = name.replace(',', '\uFF0C')
    # CCTV1/CCTV1??/CCTV-1 -> CCTV-1/CCTV-1??
    name = re.sub(r'^CCTV[-_ ]?(\d+)(\+?)', r'CCTV-\1\2', name, flags=re.I)
    return name[:80]


def cctv_num(name: str):
    m = re.match(r'^CCTV[-_ ]?(\d+)(\+?)', name, re.I)
    if not m:
        return None
    return (int(m.group(1)), 1 if m.group(2) else 0)


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
    if upper.startswith(("TVBJADE", "TVBPEARL", "TVBNEWS", "TVBFINANCE", "TVBENTERTAINMENT", "TVBCLASSIC", "TVBPLUS", "TVBSPORTS")):
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
    if cctv_num(n) and chinese_count(n) == 0 and any(x in lower for x in ['america', 'asia', 'europe', 'english', 'fran', 'espa', 'arab', 'russian']):
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
    if any(k in name for k in HK_KEYS) or any(k in group for k in ["\u9999\u6e2f", "\u6fb3\u95e8", "\u53f0\u6e7e", "\u6e2f\u6fb3\u53f0"]):
        return G_HK
    if any(p in name for p in PROVINCES) or any(k in group for k in ["\u5730\u65b9", "\u7701\u5185", "\u57ce\u5e02", "4K", "4K8K"]):
        return G_LOCAL
    # Merge former movie/entertainment and other miscellaneous channels into a few broad categories.
    if any(k in name for k in MOVIE_KEYS) or any(k in group for k in ["\u5f71\u89c6", "\u7535\u5f71", "\u5267\u573a"]):
        return G_MOVIE
    if any(k in name for k in KIDS_KEYS) or any(k in group for k in ["\u5c11\u513f", "\u52a8\u6f2b"]):
        return G_KIDS
    if any(k in name for k in SPORT_DOC_KEYS) or any(k in group for k in ["\u4f53\u80b2", "\u7eaa\u5b9e", "\u7eaa\u5f55"]):
        return G_SPORT_DOC
    if any(k in name for k in MUSIC_SHOW_KEYS) or any(k in group for k in ["\u97f3\u4e50", "\u7efc\u827a", "\u620f\u66f2"]):
        return G_MUSIC_SHOW
    if any(k in name for k in LIFE_KEYS):
        return G_LIFE
    if re.search(r'[A-Za-z]{4,}', group or ''):
        return G_OVERSEA if chinese_count(name) > 0 else G_ENT
    return G_ENT


def source_priority(source: str, url: str = '') -> int:
    """Lower is better. Prefer zbds IPv4 TXT, then other zbds IPv4, then other IPv4."""
    src = (source or '').lower()
    u = (url or '').lower()
    if 'zbds_iptv4_txt' in src or 'live.zbds.top/tv/iptv4.txt' in u:
        return -200
    if 'zbds_iptv4_m3u' in src or 'live.zbds.top/tv/iptv4.m3u' in u:
        return -150
    if src.startswith('zbds_') or 'live.zbds.top' in u:
        return -80
    if 'ipv4' in src:
        return -30
    return 0


def url_score(url: str, source: str):
    s = source_priority(source, url)
    if url.startswith('http://'):
        s -= 20
    if 'epg.pw' in url:
        s += 20
    if '[' in url or 'ipv6' in (source or '').lower():
        s += 20
    if 'migu' in url.lower():
        s += 5
    return (s, len(url), source)


BAD_NAME_TOKENS = ["group-title=", "tvg-logo=", "user-agent", "likeGecko", "w_400", "h_500", "#EXTINF"]
UNWANTED_FINAL_TOKENS = DROP_LATIN_TOKENS + [
    "BUDAPEST", "BOGOTA", "BRASIL", "BRESCIA", "LIONSGATE", "WEDOTV",
    "EBONYTV", "PEACETV", "PENIEL", "STASHTV",
]


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
    if any(ord(ch) < 32 for ch in n):
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
    bad = []
    current_group = ''
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.endswith(',#genre#'):
            current_group = line.split(',', 1)[0]
            continue
        if ',' not in line:
            bad.append((lineno, 'missing comma', line[:200]))
            continue
        name, url = line.split(',', 1)
        upper_name = name.upper()
        if not name.strip() or not url.startswith(('http://', 'https://')):
            bad.append((lineno, 'bad url', line[:240]))
        if has_abnormal_channel_name(name):
            bad.append((lineno, 'abnormal/polluted name', line[:240]))
        if current_group == G_CCTV and any(tok in upper_name for tok in ['RTHK', 'TVB', 'VIUTV']):
            bad.append((lineno, 'pseudo CCTV alias', line[:240]))
        if 'NOT24/7' in upper_name or 'NOT 24/7' in upper_name:
            bad.append((lineno, 'unstable Not24/7', line[:240]))
        if not cctv_num(name) and not is_hk_mo_tw_channel(name, current_group):
            if any(tok in upper_name for tok in UNWANTED_FINAL_TOKENS):
                bad.append((lineno, 'unwanted overseas/English channel', line[:240]))
            if chinese_count(name) == 0 and re.search(r'[A-Z]{3,}', upper_name):
                bad.append((lineno, 'pure Latin overseas/English channel', line[:240]))
    if bad:
        raise SystemExit('invalid live-curated rows: ' + repr(bad[:30]))


def sort_key(item):
    group, name, url, source = item
    gi = GROUP_ORDER.index(group) if group in GROUP_ORDER else 99
    if group == G_CCTV:
        cn = cctv_num(name)
        return (gi, cn[0] if cn else 999, cn[1] if cn else 9, name, url_score(url, source))
    if group == G_SAT:
        priority = ["\u8fbd\u5b81\u536b\u89c6", "\u6cb3\u5317\u536b\u89c6", "\u6cb3\u5357\u536b\u89c6", "\u5317\u4eac\u536b\u89c6", "\u4e1c\u65b9\u536b\u89c6", "\u6d59\u6c5f\u536b\u89c6", "\u6c5f\u82cf\u536b\u89c6", "\u6e56\u5357\u536b\u89c6", "\u5e7f\u4e1c\u536b\u89c6", "\u6df1\u5733\u536b\u89c6"]
        pi = priority.index(name) if name in priority else 99
        return (gi, pi, name, url_score(url, source))
    return (gi, name, url_score(url, source))


def main():
    rows = []
    with IN.open(encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r.get('ok') != 'True':
                continue
            name = clean_name(r.get('name', ''))
            url = (r.get('url', '') or '').strip()
            group = r.get('group', '') or ''
            source = r.get('source', '') or ''
            if not name or not url.startswith(('http://', 'https://')):
                continue
            if has_abnormal_channel_name(name):
                continue
            if 'cgtn' in url.lower():
                continue
            if is_unstable_or_wrong_alias(name, group, source):
                continue
            if is_unwanted_overseas_english(name, group, source):
                continue
            if is_foreign_channel(name, group, source):
                continue
            g = classify(name, group, source)
            if g == G_OVERSEA and chinese_count(name) == 0:
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
    for n, arr in by.items():
        pub.extend(sorted(arr, key=lambda x: url_score(x[2], x[3]))[:5])
    pub.sort(key=sort_key)

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
        m.append(f'#EXTINF:-1 tvg-name="{n}" group-title="{g}",{n}')
        m.append(u)
    (ROOT / 'live.m3u').write_text('\n'.join(m) + '\n', encoding='utf-8', newline='\n')

    cnt = Counter(g for g, _, _, _ in pub)
    source_cnt = Counter(src for _, _, _, src in pub)
    group_source_cnt = Counter((g, src) for g, _, _, src in pub)
    summary_path = ROOT / 'full-check-summary.json'
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text(encoding='utf-8'))
        except Exception:
            summary = {}
    else:
        summary = {}
    summary.update({
        'curated_generated': True,
        'curated_published_lines': len(pub),
        'curated_channel_names': len(by),
        'curated_groups': dict(cnt),
        'curated_sources': dict(source_cnt),
        'final_primary_file': 'live-curated.txt',
        'final_primary_published_lines': len(pub),
        # Keep this legacy field aligned with the final TV-facing playlist after curation.
        'primary_published_lines': len(pub),
    })
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

    report = ['# Curated Ku9 playlist report', '', f'Published lines: {len(pub)}', f'Channel names: {len(by)}', '', '## Groups']
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
    print('published', len(pub), 'names', len(by), 'bytes', len(text.encode('utf-8')))
    for g in GROUP_ORDER:
        print(g.encode('unicode_escape').decode(), cnt[g])


if __name__ == '__main__':
    main()

