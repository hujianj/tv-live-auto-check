# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2468
Published channel names: 1514
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 474
- Channel limit trimmed rows: 1343
- Group limit trimmed rows: 406
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7082
- unstable_or_wrong_alias: 810
- strict_quality_filter: 474
- foreign_channel: 308
- ambiguous_url_identity: 217
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 393
- 港澳台频道: 13

## Groups
- 央视频道: 128
- 卫视频道: 196
- 地方频道: 769
- 影视剧场: 166
- 少儿动漫: 24
- 体育纪实: 66
- 音乐综艺: 33
- 生活休闲: 96
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 434 |
| zbds_iptv4_txt | 384 |
| iyouhun_zb | 350 |
| epg_cn | 347 |
| mursor_yy | 327 |
| guovin_all | 277 |
| guovin_ipv4 | 178 |
| suxuang_ipv4 | 140 |
| vamoschuck_m3u | 11 |
| iptv_org_all | 10 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| guovin_ipv6 | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 53
- guovin_ipv4: 41
- epg_cn: 21
- suxuang_ipv4: 6
- iptv_org_all: 5
- iyouhun_zb: 2

### 卫视频道
- guovin_ipv4: 93
- zbds_iptv4_txt: 66
- suxuang_ipv4: 19
- guovin_all: 9
- iyouhun_zb: 7
- guovin_ipv6: 1
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 221
- guovin_all: 200
- iyouhun_zb: 166
- epg_cn: 135
- suxuang_ipv4: 22
- guovin_ipv4: 11
- vamoschuck_m3u: 9
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 54
- suxuang_ipv4: 33
- guovin_all: 27
- iyouhun_zb: 25
- guovin_ipv4: 15
- zbds_iptv4_txt: 6
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- mursor_yy: 8
- epg_cn: 6
- guovin_all: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 19
- guovin_ipv4: 7
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- iyouhun_zb: 36
- guovin_all: 24
- epg_cn: 19
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 1
- vamoschuck_m3u: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- mursor_yy: 240
- epg_cn: 155
- iyouhun_zb: 50
- suxuang_ipv4: 43
- guovin_ipv4: 6
- guovin_all: 5
- zbds_iptv4_txt: 3

### 港澳台频道
- iyouhun_zb: 43
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 4
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
