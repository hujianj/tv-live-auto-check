# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2272
Published channel names: 1585
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 432
- Channel limit trimmed rows: 675
- Group limit trimmed rows: 1760
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7161
- unstable_or_wrong_alias: 840
- strict_quality_filter: 432
- foreign_channel: 335
- ambiguous_url_identity: 149
- latin_noise_name: 85
- cgtn_url: 22
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 1624
- 影视剧场: 136

## Groups
- 央视频道: 128
- 卫视频道: 179
- 地方频道: 544
- 影视剧场: 180
- 少儿动漫: 39
- 体育纪实: 72
- 音乐综艺: 44
- 生活休闲: 111
- 综合娱乐: 900
- 港澳台频道: 75

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 438 |
| guovin_all | 414 |
| freetv_douyu | 287 |
| guovin_ipv4 | 286 |
| freetv_huya | 273 |
| epg_cn | 253 |
| suxuang_ipv4 | 135 |
| mursor_yy | 101 |
| zbds_iptv4_txt | 29 |
| vamoschuck_m3u | 27 |
| iptv_org_all | 8 |
| suxuang_ipv6 | 7 |
| guovin_ipv6 | 5 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |
| iptv_org_tw | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 69
- epg_cn: 38
- suxuang_ipv4: 16
- iptv_org_all: 4
- free_tv_world: 1

### 卫视频道
- guovin_ipv4: 131
- suxuang_ipv4: 31
- guovin_all: 9
- guovin_ipv6: 4
- bigbiggrandg_gather: 1
- iptv_org_all: 1
- suxuang_ipv6: 1
- zbds_iptv4_txt: 1

### 地方频道
- guovin_all: 296
- epg_cn: 132
- guovin_ipv4: 46
- suxuang_ipv4: 37
- vamoschuck_m3u: 18
- bigbiggrandg_gather: 6
- freetv_douyu: 4
- freetv_huya: 2

### 影视剧场
- freetv_douyu: 81
- freetv_huya: 37
- guovin_all: 17
- mursor_yy: 15
- guovin_ipv4: 12
- suxuang_ipv4: 11
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 2

### 少儿动漫
- freetv_douyu: 19
- guovin_all: 9
- freetv_huya: 8
- mursor_yy: 3

### 体育纪实
- zbds_iptv4_txt: 27
- freetv_douyu: 11
- guovin_all: 11
- guovin_ipv4: 10
- freetv_huya: 7
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 10
- freetv_douyu: 10
- freetv_huya: 10
- mursor_yy: 7
- guovin_ipv4: 4
- kimentanm_aptv: 3

### 生活休闲
- guovin_all: 50
- epg_cn: 13
- bigbiggrandg_gather: 9
- freetv_huya: 8
- freetv_douyu: 7
- suxuang_ipv4: 7
- guovin_ipv4: 6
- vamoschuck_m3u: 5

### 综合娱乐
- bigbiggrandg_gather: 391
- freetv_huya: 189
- freetv_douyu: 155
- mursor_yy: 67
- epg_cn: 61
- guovin_all: 14
- suxuang_ipv4: 12
- guovin_ipv4: 6

### 港澳台频道
- suxuang_ipv4: 21
- bigbiggrandg_gather: 16
- freetv_huya: 12
- guovin_all: 8
- epg_cn: 6
- suxuang_ipv6: 6
- guovin_ipv4: 2
- mursor_yy: 2


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
