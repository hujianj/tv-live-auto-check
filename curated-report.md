# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2498
Published channel names: 1521
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 467
- Channel limit trimmed rows: 1733
- Group limit trimmed rows: 396
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6975
- unstable_or_wrong_alias: 847
- strict_quality_filter: 467
- foreign_channel: 312
- ambiguous_url_identity: 219
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 381
- 港澳台频道: 15

## Groups
- 央视频道: 129
- 卫视频道: 198
- 地方频道: 787
- 影视剧场: 167
- 少儿动漫: 29
- 体育纪实: 68
- 音乐综艺: 33
- 生活休闲: 97
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| zbds_iptv4_txt | 387 |
| iyouhun_zb | 359 |
| epg_cn | 347 |
| mursor_yy | 333 |
| guovin_all | 287 |
| guovin_ipv4 | 185 |
| suxuang_ipv4 | 139 |
| vamoschuck_m3u | 11 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 61
- guovin_ipv4: 38
- epg_cn: 23
- suxuang_ipv4: 6
- iptv_org_all: 1

### 卫视频道
- guovin_ipv4: 96
- zbds_iptv4_txt: 65
- suxuang_ipv4: 21
- guovin_all: 9
- iyouhun_zb: 6
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 216
- guovin_all: 203
- iyouhun_zb: 181
- epg_cn: 136
- suxuang_ipv4: 23
- guovin_ipv4: 13
- vamoschuck_m3u: 10
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 56
- suxuang_ipv4: 31
- guovin_all: 28
- iyouhun_zb: 24
- guovin_ipv4: 19
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 3
- vamoschuck_m3u: 1

### 少儿动漫
- epg_cn: 8
- mursor_yy: 8
- zbds_iptv4_txt: 6
- guovin_all: 5
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 20
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 14
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- iyouhun_zb: 36
- guovin_all: 28
- epg_cn: 16
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 2

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 245
- epg_cn: 153
- iyouhun_zb: 49
- suxuang_ipv4: 40
- guovin_ipv4: 6
- guovin_all: 5
- zbds_iptv4_txt: 3

### 港澳台频道
- iyouhun_zb: 41
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
- mursor_yy: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
