# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2527
Published channel names: 1774
Stability history URLs loaded: 3986
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 376
- Channel limit trimmed rows: 1066
- Group limit trimmed rows: 155
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 8049
- unstable_or_wrong_alias: 753
- strict_quality_filter: 376
- foreign_channel: 319
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 59
- 生活休闲: 57
- 海外华语频道: 39

## Groups
- 央视频道: 150
- 卫视频道: 205
- 地方频道: 520
- 影视剧场: 147
- 少儿动漫: 22
- 体育纪实: 68
- 音乐综艺: 50
- 生活休闲: 180
- 综合娱乐: 900
- 港澳台频道: 65
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 544 |
| epg_cn | 379 |
| mursor_yy | 320 |
| zbds_iptv4_txt | 304 |
| iyouhun_zb | 281 |
| guovin_ipv4 | 267 |
| guovin_ipv6 | 125 |
| suxuang_ipv4 | 112 |
| epg_tw | 45 |
| migu_interface | 43 |
| vamoschuck_m3u | 30 |
| iptv_org_all | 28 |
| suxuang_ipv6 | 17 |
| epg_hk | 13 |
| epg_mo | 5 |
| epg_my | 4 |
| kimentanm_aptv | 3 |
| fanmingming_ipv6_raw | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| mursor_bililive | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 56
- zbds_iptv4_txt: 37
- epg_cn: 27
- iptv_org_all: 16
- iyouhun_zb: 6
- suxuang_ipv4: 5
- migu_interface: 3

### 卫视频道
- guovin_ipv4: 88
- zbds_iptv4_txt: 76
- iyouhun_zb: 13
- suxuang_ipv4: 11
- guovin_ipv6: 7
- migu_interface: 7
- bigbiggrandg_gather: 1
- iptv_org_all: 1

### 地方频道
- epg_cn: 135
- zbds_iptv4_txt: 115
- bigbiggrandg_gather: 89
- iyouhun_zb: 64
- guovin_ipv4: 43
- suxuang_ipv4: 31
- guovin_ipv6: 21
- suxuang_ipv6: 9

### 影视剧场
- mursor_yy: 67
- iyouhun_zb: 20
- guovin_ipv4: 16
- guovin_ipv6: 14
- zbds_iptv4_txt: 14
- suxuang_ipv4: 10
- vamoschuck_m3u: 3
- migu_interface: 2

### 少儿动漫
- epg_cn: 9
- mursor_yy: 5
- guovin_ipv6: 3
- iyouhun_zb: 2
- epg_tw: 1
- iptv_org_all: 1
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 26
- iyouhun_zb: 24
- guovin_ipv4: 11
- epg_cn: 3
- mursor_yy: 2
- guovin_ipv6: 1
- suxuang_ipv4: 1

### 音乐综艺
- suxuang_ipv4: 18
- mursor_yy: 11
- bigbiggrandg_gather: 10
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- guovin_ipv6: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 47
- guovin_ipv6: 39
- guovin_ipv4: 20
- epg_cn: 17
- vamoschuck_m3u: 16
- bigbiggrandg_gather: 13
- suxuang_ipv4: 9
- mursor_yy: 8

### 综合娱乐
- bigbiggrandg_gather: 414
- epg_cn: 188
- iyouhun_zb: 85
- guovin_ipv6: 39
- epg_tw: 36
- zbds_iptv4_txt: 33
- guovin_ipv4: 26
- suxuang_ipv4: 23

### 港澳台频道
- iyouhun_zb: 18
- bigbiggrandg_gather: 16
- epg_hk: 8
- epg_tw: 8
- suxuang_ipv4: 4
- suxuang_ipv6: 4
- guovin_ipv4: 3
- mursor_yy: 2

### 海外华语频道
- mursor_yy: 217
- iptv_org_all: 2
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
