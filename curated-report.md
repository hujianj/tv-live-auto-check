# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2478
Published channel names: 1631
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 466
- Channel limit trimmed rows: 1810
- Group limit trimmed rows: 2121
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7022
- unstable_or_wrong_alias: 822
- strict_quality_filter: 466
- foreign_channel: 318
- ambiguous_url_identity: 174
- latin_noise_name: 86
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 1885
- 影视剧场: 191
- 港澳台频道: 28
- 少儿动漫: 17

## Groups
- 央视频道: 128
- 卫视频道: 207
- 地方频道: 679
- 影视剧场: 180
- 少儿动漫: 40
- 体育纪实: 88
- 音乐综艺: 53
- 生活休闲: 113
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 433 |
| zbds_iptv4_txt | 311 |
| guovin_all | 285 |
| iyouhun_zb | 272 |
| epg_cn | 257 |
| freetv_huya | 252 |
| freetv_douyu | 250 |
| guovin_ipv4 | 156 |
| mursor_yy | 140 |
| suxuang_ipv4 | 101 |
| vamoschuck_m3u | 10 |
| iptv_org_all | 4 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 70
- guovin_ipv4: 36
- epg_cn: 19
- suxuang_ipv4: 2
- iptv_org_all: 1

### 卫视频道
- zbds_iptv4_txt: 86
- guovin_ipv4: 85
- suxuang_ipv4: 22
- guovin_all: 9
- iyouhun_zb: 4
- iptv_org_all: 1

### 地方频道
- guovin_all: 218
- iyouhun_zb: 155
- epg_cn: 138
- zbds_iptv4_txt: 109
- suxuang_ipv4: 29
- guovin_ipv4: 12
- bigbiggrandg_gather: 6
- vamoschuck_m3u: 6

### 影视剧场
- freetv_douyu: 66
- freetv_huya: 33
- mursor_yy: 29
- suxuang_ipv4: 16
- guovin_all: 10
- iyouhun_zb: 8
- guovin_ipv4: 7
- bigbiggrandg_gather: 5

### 少儿动漫
- freetv_douyu: 12
- mursor_yy: 7
- epg_cn: 6
- freetv_huya: 6
- guovin_all: 4
- zbds_iptv4_txt: 3
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 34
- iyouhun_zb: 20
- freetv_douyu: 11
- guovin_ipv4: 8
- freetv_huya: 6
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- freetv_douyu: 10
- freetv_huya: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- guovin_all: 28
- iyouhun_zb: 26
- epg_cn: 23
- bigbiggrandg_gather: 8
- freetv_huya: 8
- freetv_douyu: 7
- mursor_yy: 5
- suxuang_ipv4: 4

### 综合娱乐
- bigbiggrandg_gather: 391
- freetv_huya: 176
- freetv_douyu: 140
- mursor_yy: 79
- epg_cn: 60
- iyouhun_zb: 26
- suxuang_ipv4: 13
- guovin_all: 7

### 港澳台频道
- iyouhun_zb: 31
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- freetv_huya: 11
- epg_cn: 8
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
