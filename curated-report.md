# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2411
Published channel names: 1638
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 437
- Channel limit trimmed rows: 808
- Group limit trimmed rows: 1369
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6883
- unstable_or_wrong_alias: 803
- strict_quality_filter: 437
- foreign_channel: 305
- ambiguous_url_identity: 131
- latin_noise_name: 47
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 1280
- 影视剧场: 89

## Groups
- 央视频道: 127
- 卫视频道: 196
- 地方频道: 704
- 影视剧场: 180
- 少儿动漫: 31
- 体育纪实: 65
- 音乐综艺: 51
- 生活休闲: 78
- 综合娱乐: 900
- 港澳台频道: 79

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 452 |
| bigbiggrandg_gather | 440 |
| guovin_all | 335 |
| freetv_huya | 322 |
| epg_cn | 253 |
| mursor_yy | 183 |
| guovin_ipv4 | 157 |
| suxuang_ipv4 | 113 |
| freetv_douyu | 111 |
| vamoschuck_m3u | 19 |
| iptv_org_all | 7 |
| suxuang_ipv6 | 7 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| iyouhun_zb | 1 |
| free_tv_world | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 58
- guovin_ipv4: 43
- epg_cn: 20
- suxuang_ipv4: 4
- iptv_org_all: 2

### 卫视频道
- zbds_iptv4_txt: 88
- guovin_ipv4: 78
- suxuang_ipv4: 18
- guovin_all: 9
- bigbiggrandg_gather: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 253
- zbds_iptv4_txt: 253
- epg_cn: 133
- suxuang_ipv4: 24
- vamoschuck_m3u: 18
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- freetv_douyu: 2

### 影视剧场
- freetv_huya: 44
- mursor_yy: 37
- freetv_douyu: 25
- suxuang_ipv4: 24
- guovin_all: 18
- zbds_iptv4_txt: 18
- guovin_ipv4: 8
- bigbiggrandg_gather: 5

### 少儿动漫
- freetv_huya: 9
- guovin_all: 7
- mursor_yy: 7
- freetv_douyu: 6
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 30
- freetv_douyu: 8
- guovin_ipv4: 8
- freetv_huya: 7
- guovin_all: 5
- mursor_yy: 4
- epg_cn: 3

### 音乐综艺
- mursor_yy: 14
- bigbiggrandg_gather: 12
- freetv_douyu: 10
- freetv_huya: 8
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 16
- bigbiggrandg_gather: 9
- freetv_huya: 9
- mursor_yy: 5
- freetv_douyu: 4
- iptv_org_all: 2
- suxuang_ipv4: 2

### 综合娱乐
- bigbiggrandg_gather: 392
- freetv_huya: 233
- mursor_yy: 114
- epg_cn: 71
- freetv_douyu: 56
- suxuang_ipv4: 20
- guovin_all: 5
- guovin_ipv4: 3

### 港澳台频道
- suxuang_ipv4: 21
- bigbiggrandg_gather: 16
- freetv_huya: 11
- epg_cn: 10
- guovin_all: 8
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
