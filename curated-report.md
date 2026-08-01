# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2703
Published channel names: 1665
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 474
- Channel limit trimmed rows: 1501
- Group limit trimmed rows: 182
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7033
- unstable_or_wrong_alias: 824
- strict_quality_filter: 474
- foreign_channel: 364
- ambiguous_url_identity: 232
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 176
- 影视剧场: 3
- 港澳台频道: 3

## Groups
- 央视频道: 126
- 卫视频道: 196
- 地方频道: 767
- 影视剧场: 180
- 少儿动漫: 26
- 体育纪实: 68
- 音乐综艺: 34
- 生活休闲: 104
- 综合娱乐: 892
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 439 |
| bigbiggrandg_gather | 437 |
| iyouhun_zb | 381 |
| guovin_all | 358 |
| mursor_yy | 319 |
| zbds_iptv4_txt | 297 |
| guovin_ipv4 | 221 |
| suxuang_ipv4 | 180 |
| migu_interface | 35 |
| vamoschuck_m3u | 10 |
| iptv_org_all | 9 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| suxuang_ipv6 | 2 |
| free_tv_world | 1 |
| epg_tw | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 58
- epg_cn: 28
- zbds_iptv4_txt: 18
- suxuang_ipv4: 11
- iptv_org_all: 5
- iyouhun_zb: 5
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 112
- zbds_iptv4_txt: 38
- suxuang_ipv4: 23
- guovin_all: 12
- iyouhun_zb: 7
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 244
- zbds_iptv4_txt: 185
- iyouhun_zb: 144
- epg_cn: 135
- suxuang_ipv4: 23
- guovin_ipv4: 12
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 48
- guovin_all: 34
- suxuang_ipv4: 30
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 7
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 29
- iyouhun_zb: 19
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 3

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 41
- guovin_all: 26
- epg_cn: 17
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 395
- epg_cn: 245
- iyouhun_zb: 94
- suxuang_ipv4: 77
- guovin_all: 24
- migu_interface: 21
- mursor_yy: 19
- epg_mo: 7

### 港澳台频道
- iyouhun_zb: 44
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- guovin_all: 7
- epg_cn: 4
- guovin_ipv4: 2
- suxuang_ipv6: 2
- epg_tw: 1

### 海外华语频道
- mursor_yy: 218
- iptv_org_all: 1
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
