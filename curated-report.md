# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2462
Published channel names: 1485
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 465
- Channel limit trimmed rows: 1738
- Group limit trimmed rows: 405
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6980
- unstable_or_wrong_alias: 846
- strict_quality_filter: 465
- foreign_channel: 312
- ambiguous_url_identity: 218
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 386
- 港澳台频道: 16
- 影视剧场: 3

## Groups
- 央视频道: 129
- 卫视频道: 199
- 地方频道: 734
- 影视剧场: 180
- 少儿动漫: 25
- 体育纪实: 71
- 音乐综艺: 33
- 生活休闲: 101
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 432 |
| zbds_iptv4_txt | 366 |
| iyouhun_zb | 354 |
| epg_cn | 349 |
| mursor_yy | 328 |
| guovin_all | 294 |
| guovin_ipv4 | 175 |
| suxuang_ipv4 | 133 |
| vamoschuck_m3u | 13 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 68
- guovin_ipv4: 31
- epg_cn: 25
- suxuang_ipv4: 4
- iptv_org_all: 1

### 卫视频道
- guovin_ipv4: 94
- zbds_iptv4_txt: 67
- suxuang_ipv4: 21
- guovin_all: 9
- iyouhun_zb: 7
- iptv_org_all: 1

### 地方频道
- guovin_all: 202
- iyouhun_zb: 176
- zbds_iptv4_txt: 170
- epg_cn: 137
- suxuang_ipv4: 21
- guovin_ipv4: 13
- vamoschuck_m3u: 9
- bigbiggrandg_gather: 6

### 影视剧场
- mursor_yy: 52
- guovin_all: 30
- suxuang_ipv4: 29
- iyouhun_zb: 23
- zbds_iptv4_txt: 22
- guovin_ipv4: 18
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 34
- iyouhun_zb: 20
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 38
- guovin_all: 28
- epg_cn: 18
- bigbiggrandg_gather: 8
- mursor_yy: 4
- iptv_org_all: 2
- vamoschuck_m3u: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 389
- mursor_yy: 244
- epg_cn: 152
- iyouhun_zb: 48
- suxuang_ipv4: 41
- guovin_all: 8
- guovin_ipv4: 6
- epg_tw: 3

### 港澳台频道
- iyouhun_zb: 40
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 7
- suxuang_ipv6: 3
- guovin_ipv4: 2
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
