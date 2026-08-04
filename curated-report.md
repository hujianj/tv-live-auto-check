# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2636
Published channel names: 1641
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 484
- Channel limit trimmed rows: 1427
- Group limit trimmed rows: 208
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7078
- unstable_or_wrong_alias: 816
- strict_quality_filter: 484
- foreign_channel: 360
- ambiguous_url_identity: 227
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 190
- 港澳台频道: 13
- 影视剧场: 5

## Groups
- 央视频道: 126
- 卫视频道: 197
- 地方频道: 750
- 影视剧场: 180
- 少儿动漫: 27
- 体育纪实: 65
- 音乐综艺: 33
- 生活休闲: 81
- 综合娱乐: 867
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 434 |
| epg_cn | 388 |
| iyouhun_zb | 351 |
| guovin_all | 347 |
| zbds_iptv4_txt | 331 |
| mursor_yy | 323 |
| guovin_ipv4 | 198 |
| suxuang_ipv4 | 176 |
| migu_interface | 35 |
| epg_tw | 21 |
| iptv_org_all | 8 |
| vamoschuck_m3u | 8 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| guovin_ipv6 | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 54
- zbds_iptv4_txt: 33
- epg_cn: 22
- suxuang_ipv4: 6
- iptv_org_all: 5
- iyouhun_zb: 4
- migu_interface: 2

### 卫视频道
- guovin_ipv4: 94
- zbds_iptv4_txt: 61
- suxuang_ipv4: 19
- guovin_all: 12
- iyouhun_zb: 7
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 232
- zbds_iptv4_txt: 181
- iyouhun_zb: 149
- epg_cn: 129
- suxuang_ipv4: 24
- guovin_ipv4: 13
- migu_interface: 9
- vamoschuck_m3u: 7

### 影视剧场
- mursor_yy: 50
- guovin_all: 34
- suxuang_ipv4: 31
- iyouhun_zb: 23
- zbds_iptv4_txt: 22
- guovin_ipv4: 12
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- mursor_yy: 8
- guovin_all: 7
- epg_cn: 6
- epg_tw: 2
- iyouhun_zb: 2
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 28
- iyouhun_zb: 17
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 3

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 26
- iyouhun_zb: 24
- epg_cn: 12
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- epg_cn: 208
- iyouhun_zb: 83
- suxuang_ipv4: 80
- guovin_all: 26
- migu_interface: 21
- mursor_yy: 20
- epg_tw: 19

### 港澳台频道
- iyouhun_zb: 41
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- epg_cn: 8
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
