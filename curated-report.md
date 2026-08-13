# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2443
Published channel names: 1485
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 468
- Channel limit trimmed rows: 1659
- Group limit trimmed rows: 397
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6963
- unstable_or_wrong_alias: 820
- strict_quality_filter: 468
- foreign_channel: 348
- ambiguous_url_identity: 206
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 382
- 港澳台频道: 15

## Groups
- 央视频道: 127
- 卫视频道: 204
- 地方频道: 728
- 影视剧场: 170
- 少儿动漫: 28
- 体育纪实: 67
- 音乐综艺: 33
- 生活休闲: 96
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 435 |
| iyouhun_zb | 361 |
| epg_cn | 332 |
| mursor_yy | 328 |
| zbds_iptv4_txt | 324 |
| guovin_all | 295 |
| guovin_ipv4 | 193 |
| suxuang_ipv4 | 147 |
| vamoschuck_m3u | 13 |
| iptv_org_all | 7 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 47
- guovin_ipv4: 46
- epg_cn: 22
- suxuang_ipv4: 7
- iptv_org_all: 4
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 98
- zbds_iptv4_txt: 65
- suxuang_ipv4: 24
- guovin_all: 9
- iyouhun_zb: 7
- iptv_org_all: 1

### 地方频道
- guovin_all: 208
- iyouhun_zb: 178
- zbds_iptv4_txt: 161
- epg_cn: 130
- suxuang_ipv4: 23
- guovin_ipv4: 13
- vamoschuck_m3u: 9
- bigbiggrandg_gather: 6

### 影视剧场
- mursor_yy: 54
- suxuang_ipv4: 33
- guovin_all: 29
- iyouhun_zb: 25
- guovin_ipv4: 18
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 5
- vamoschuck_m3u: 1

### 少儿动漫
- epg_cn: 8
- mursor_yy: 7
- zbds_iptv4_txt: 6
- guovin_all: 5
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 35
- iyouhun_zb: 17
- guovin_ipv4: 7
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- iyouhun_zb: 38
- guovin_all: 28
- epg_cn: 12
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- vamoschuck_m3u: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- mursor_yy: 243
- epg_cn: 149
- iyouhun_zb: 52
- suxuang_ipv4: 43
- guovin_all: 7
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
