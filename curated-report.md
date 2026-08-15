# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2578
Published channel names: 1668
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 464
- Channel limit trimmed rows: 1774
- Group limit trimmed rows: 1516
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6841
- unstable_or_wrong_alias: 832
- strict_quality_filter: 464
- foreign_channel: 310
- ambiguous_url_identity: 225
- latin_noise_name: 38
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 1380
- 影视剧场: 113
- 港澳台频道: 22
- 少儿动漫: 1

## Groups
- 央视频道: 128
- 卫视频道: 201
- 地方频道: 797
- 影视剧场: 180
- 少儿动漫: 40
- 体育纪实: 79
- 音乐综艺: 51
- 生活休闲: 112
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 433 |
| zbds_iptv4_txt | 392 |
| iyouhun_zb | 319 |
| freetv_huya | 297 |
| guovin_all | 278 |
| epg_cn | 265 |
| mursor_yy | 182 |
| guovin_ipv4 | 178 |
| suxuang_ipv4 | 110 |
| freetv_douyu | 99 |
| vamoschuck_m3u | 11 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| iptv_org_tw | 1 |
| free_tv_world | 1 |
| suxuang_ipv6 | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 54
- zbds_iptv4_txt: 40
- epg_cn: 20
- suxuang_ipv4: 10
- iptv_org_all: 3
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 87
- zbds_iptv4_txt: 81
- suxuang_ipv4: 20
- guovin_all: 9
- iyouhun_zb: 3
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 228
- guovin_all: 207
- iyouhun_zb: 173
- epg_cn: 137
- suxuang_ipv4: 22
- guovin_ipv4: 11
- vamoschuck_m3u: 10
- bigbiggrandg_gather: 5

### 影视剧场
- freetv_huya: 36
- mursor_yy: 36
- freetv_douyu: 31
- suxuang_ipv4: 24
- iyouhun_zb: 17
- guovin_all: 16
- guovin_ipv4: 10
- bigbiggrandg_gather: 5

### 少儿动漫
- freetv_huya: 9
- epg_cn: 8
- mursor_yy: 8
- zbds_iptv4_txt: 5
- freetv_douyu: 4
- guovin_all: 4
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 20
- guovin_ipv4: 8
- freetv_douyu: 7
- freetv_huya: 4
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- freetv_huya: 10
- freetv_douyu: 8
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 36
- guovin_all: 29
- epg_cn: 20
- freetv_huya: 9
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 2

### 综合娱乐
- bigbiggrandg_gather: 391
- freetv_huya: 218
- mursor_yy: 113
- epg_cn: 69
- freetv_douyu: 46
- iyouhun_zb: 32
- suxuang_ipv4: 19
- guovin_all: 4

### 港澳台频道
- iyouhun_zb: 35
- bigbiggrandg_gather: 13
- suxuang_ipv4: 13
- freetv_huya: 9
- epg_cn: 8
- guovin_all: 7
- guovin_ipv4: 2
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
