# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2501
Published channel names: 1533
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 473
- Channel limit trimmed rows: 1656
- Group limit trimmed rows: 417
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7060
- unstable_or_wrong_alias: 819
- strict_quality_filter: 473
- foreign_channel: 312
- ambiguous_url_identity: 223
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 398
- 港澳台频道: 15
- 影视剧场: 4

## Groups
- 央视频道: 130
- 卫视频道: 199
- 地方频道: 780
- 影视剧场: 180
- 少儿动漫: 23
- 体育纪实: 68
- 音乐综艺: 33
- 生活休闲: 98
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| zbds_iptv4_txt | 383 |
| epg_cn | 349 |
| iyouhun_zb | 346 |
| mursor_yy | 321 |
| guovin_all | 292 |
| guovin_ipv4 | 201 |
| suxuang_ipv4 | 146 |
| vamoschuck_m3u | 11 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| guovin_ipv6 | 1 |
| iptv_org_tw | 1 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 52
- zbds_iptv4_txt: 40
- epg_cn: 25
- suxuang_ipv4: 8
- iptv_org_all: 3
- guovin_ipv6: 1
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 102
- zbds_iptv4_txt: 55
- suxuang_ipv4: 27
- guovin_all: 9
- iyouhun_zb: 5
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 227
- guovin_all: 204
- iyouhun_zb: 167
- epg_cn: 133
- suxuang_ipv4: 22
- guovin_ipv4: 12
- vamoschuck_m3u: 10
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 51
- suxuang_ipv4: 31
- guovin_all: 29
- iyouhun_zb: 24
- zbds_iptv4_txt: 23
- guovin_ipv4: 16
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- epg_cn: 6
- mursor_yy: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

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
- iyouhun_zb: 37
- guovin_all: 28
- epg_cn: 17
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 240
- epg_cn: 157
- iyouhun_zb: 49
- suxuang_ipv4: 42
- guovin_ipv4: 6
- guovin_all: 5
- zbds_iptv4_txt: 4

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
