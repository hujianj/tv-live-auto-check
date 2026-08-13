# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2527
Published channel names: 1531
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 470
- Channel limit trimmed rows: 1760
- Group limit trimmed rows: 432
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6984
- unstable_or_wrong_alias: 819
- strict_quality_filter: 470
- foreign_channel: 309
- ambiguous_url_identity: 223
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 408
- 港澳台频道: 16
- 影视剧场: 8

## Groups
- 央视频道: 128
- 卫视频道: 209
- 地方频道: 795
- 影视剧场: 180
- 少儿动漫: 26
- 体育纪实: 66
- 音乐综艺: 33
- 生活休闲: 100
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 440 |
| bigbiggrandg_gather | 436 |
| epg_cn | 352 |
| iyouhun_zb | 349 |
| mursor_yy | 325 |
| guovin_all | 292 |
| guovin_ipv4 | 168 |
| suxuang_ipv4 | 134 |
| vamoschuck_m3u | 12 |
| iptv_org_all | 6 |
| epg_tw | 4 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 58
- guovin_ipv4: 43
- epg_cn: 20
- suxuang_ipv4: 4
- iptv_org_all: 3

### 卫视频道
- zbds_iptv4_txt: 95
- guovin_ipv4: 81
- suxuang_ipv4: 19
- guovin_all: 9
- iyouhun_zb: 4
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 222
- guovin_all: 210
- iyouhun_zb: 174
- epg_cn: 140
- suxuang_ipv4: 20
- guovin_ipv4: 13
- vamoschuck_m3u: 11
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 55
- suxuang_ipv4: 32
- guovin_all: 26
- iyouhun_zb: 24
- zbds_iptv4_txt: 24
- guovin_ipv4: 13
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- mursor_yy: 8
- epg_cn: 6
- guovin_all: 5
- zbds_iptv4_txt: 5
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 20
- guovin_ipv4: 7
- epg_cn: 3
- mursor_yy: 3
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
- epg_cn: 20
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 239
- epg_cn: 155
- iyouhun_zb: 48
- suxuang_ipv4: 43
- guovin_ipv4: 6
- guovin_all: 5
- epg_tw: 4

### 港澳台频道
- iyouhun_zb: 41
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
- free_tv_world: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
