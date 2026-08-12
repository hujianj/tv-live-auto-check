# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2500
Published channel names: 1530
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 466
- Channel limit trimmed rows: 1612
- Group limit trimmed rows: 392
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6921
- unstable_or_wrong_alias: 813
- strict_quality_filter: 466
- foreign_channel: 309
- ambiguous_url_identity: 223
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 372
- 港澳台频道: 15
- 影视剧场: 5

## Groups
- 央视频道: 128
- 卫视频道: 197
- 地方频道: 787
- 影视剧场: 180
- 少儿动漫: 25
- 体育纪实: 65
- 音乐综艺: 34
- 生活休闲: 94
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| zbds_iptv4_txt | 375 |
| iyouhun_zb | 347 |
| epg_cn | 337 |
| mursor_yy | 327 |
| guovin_all | 299 |
| guovin_ipv4 | 205 |
| suxuang_ipv4 | 146 |
| vamoschuck_m3u | 11 |
| iptv_org_all | 8 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| guovin_ipv6 | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 53
- zbds_iptv4_txt: 39
- epg_cn: 24
- suxuang_ipv4: 7
- iptv_org_all: 3
- guovin_ipv6: 1
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 106
- zbds_iptv4_txt: 48
- suxuang_ipv4: 27
- guovin_all: 9
- iyouhun_zb: 6
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 228
- guovin_all: 211
- iyouhun_zb: 169
- epg_cn: 130
- suxuang_ipv4: 22
- guovin_ipv4: 12
- vamoschuck_m3u: 10
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 53
- suxuang_ipv4: 31
- guovin_all: 28
- iyouhun_zb: 24
- zbds_iptv4_txt: 23
- guovin_ipv4: 15
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 17
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- iyouhun_zb: 36
- guovin_all: 28
- epg_cn: 14
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 241
- epg_cn: 152
- iyouhun_zb: 51
- suxuang_ipv4: 42
- guovin_all: 6
- guovin_ipv4: 6
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
