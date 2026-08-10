# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2667
Published channel names: 1639
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 466
- Channel limit trimmed rows: 1631
- Group limit trimmed rows: 206
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6952
- unstable_or_wrong_alias: 804
- strict_quality_filter: 466
- foreign_channel: 364
- ambiguous_url_identity: 231
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 190
- 港澳台频道: 16

## Groups
- 央视频道: 126
- 卫视频道: 193
- 地方频道: 786
- 影视剧场: 180
- 少儿动漫: 24
- 体育纪实: 65
- 音乐综艺: 35
- 生活休闲: 92
- 综合娱乐: 856
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 437 |
| bigbiggrandg_gather | 436 |
| epg_cn | 407 |
| iyouhun_zb | 374 |
| mursor_yy | 318 |
| guovin_all | 313 |
| guovin_ipv4 | 171 |
| suxuang_ipv4 | 170 |
| vamoschuck_m3u | 11 |
| epg_tw | 10 |
| epg_mo | 7 |
| iptv_org_all | 3 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| epg_hk | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 68
- guovin_ipv4: 35
- epg_cn: 21
- iptv_org_all: 1
- suxuang_ipv4: 1

### 卫视频道
- guovin_ipv4: 86
- zbds_iptv4_txt: 74
- suxuang_ipv4: 19
- guovin_all: 9
- iyouhun_zb: 5

### 地方频道
- zbds_iptv4_txt: 233
- guovin_all: 211
- iyouhun_zb: 165
- epg_cn: 126
- suxuang_ipv4: 23
- guovin_ipv4: 12
- vamoschuck_m3u: 10
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 50
- suxuang_ipv4: 32
- guovin_all: 29
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 17
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- mursor_yy: 7
- epg_cn: 6
- guovin_all: 5
- zbds_iptv4_txt: 4
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 17
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2
- iyouhun_zb: 1

### 生活休闲
- iyouhun_zb: 36
- guovin_all: 27
- epg_cn: 14
- bigbiggrandg_gather: 8
- mursor_yy: 4
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- epg_cn: 228
- iyouhun_zb: 85
- suxuang_ipv4: 78
- guovin_all: 23
- mursor_yy: 17
- epg_tw: 10
- guovin_ipv4: 8

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 9
- guovin_all: 7
- suxuang_ipv6: 3
- guovin_ipv4: 2
- mursor_yy: 1

### 海外华语频道
- mursor_yy: 219
- iptv_org_tw: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
