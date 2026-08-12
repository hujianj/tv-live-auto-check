# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2467
Published channel names: 1608
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 478
- Channel limit trimmed rows: 1682
- Group limit trimmed rows: 1347
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7035
- unstable_or_wrong_alias: 818
- strict_quality_filter: 478
- foreign_channel: 313
- ambiguous_url_identity: 178
- cgtn_url: 25
- invalid_name_or_url: 2

### Group limit trims

- 综合娱乐: 1250
- 影视剧场: 69
- 港澳台频道: 28

## Groups
- 央视频道: 128
- 卫视频道: 197
- 地方频道: 722
- 影视剧场: 180
- 少儿动漫: 32
- 体育纪实: 73
- 音乐综艺: 43
- 生活休闲: 102
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| zbds_iptv4_txt | 352 |
| freetv_huya | 336 |
| guovin_all | 293 |
| iyouhun_zb | 279 |
| epg_cn | 270 |
| mursor_yy | 191 |
| guovin_ipv4 | 176 |
| suxuang_ipv4 | 111 |
| vamoschuck_m3u | 8 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 49
- zbds_iptv4_txt: 43
- epg_cn: 23
- suxuang_ipv4: 9
- iptv_org_all: 3
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 91
- zbds_iptv4_txt: 70
- suxuang_ipv4: 21
- guovin_all: 9
- iyouhun_zb: 5
- iptv_org_all: 1

### 地方频道
- guovin_all: 217
- zbds_iptv4_txt: 182
- iyouhun_zb: 144
- epg_cn: 133
- suxuang_ipv4: 22
- guovin_ipv4: 11
- vamoschuck_m3u: 6
- bigbiggrandg_gather: 5

### 影视剧场
- freetv_huya: 50
- mursor_yy: 40
- suxuang_ipv4: 22
- zbds_iptv4_txt: 21
- iyouhun_zb: 17
- guovin_all: 15
- guovin_ipv4: 9
- bigbiggrandg_gather: 5

### 少儿动漫
- freetv_huya: 8
- guovin_all: 8
- mursor_yy: 7
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 17
- freetv_huya: 8
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 14
- bigbiggrandg_gather: 11
- freetv_huya: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- iyouhun_zb: 29
- guovin_all: 28
- epg_cn: 19
- freetv_huya: 9
- bigbiggrandg_gather: 8
- mursor_yy: 4
- iptv_org_all: 2
- suxuang_ipv4: 2

### 综合娱乐
- bigbiggrandg_gather: 394
- freetv_huya: 239
- mursor_yy: 121
- epg_cn: 78
- iyouhun_zb: 33
- suxuang_ipv4: 20
- guovin_all: 7
- guovin_ipv4: 3

### 港澳台频道
- iyouhun_zb: 31
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- freetv_huya: 10
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
