# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2567
Published channel names: 1825
Stability history URLs loaded: 3585

## Quality filters and limits

- Strict quality filter dropped rows: 318
- Channel limit trimmed rows: 1195
- Group limit trimmed rows: 111
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7822
- unstable_or_wrong_alias: 744
- foreign_channel: 320
- strict_quality_filter: 318
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 97
- 影视剧场: 9
- 综合娱乐: 5

## Groups
- 央视频道: 144
- 卫视频道: 204
- 地方频道: 539
- 影视剧场: 180
- 少儿动漫: 28
- 体育纪实: 67
- 音乐综艺: 50
- 生活休闲: 175
- 综合娱乐: 900
- 港澳台频道: 60
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 557 |
| zbds_iptv4_txt | 426 |
| epg_cn | 363 |
| mursor_yy | 333 |
| iyouhun_zb | 263 |
| guovin_ipv4 | 218 |
| guovin_ipv6 | 123 |
| suxuang_ipv4 | 98 |
| migu_interface | 58 |
| epg_tw | 33 |
| iptv_org_all | 27 |
| vamoschuck_m3u | 18 |
| epg_hk | 16 |
| suxuang_ipv6 | 15 |
| epg_mo | 5 |
| kimentanm_aptv | 4 |
| epg_my | 3 |
| iptv_org_tw | 3 |
| fanmingming_ipv6_raw | 2 |
| yang_gather | 2 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 62
- guovin_ipv4: 41
- epg_cn: 19
- iptv_org_all: 14
- migu_interface: 3
- suxuang_ipv4: 3
- iyouhun_zb: 2

### 卫视频道
- zbds_iptv4_txt: 123
- guovin_ipv4: 53
- iyouhun_zb: 9
- migu_interface: 7
- suxuang_ipv4: 6
- guovin_ipv6: 3
- bigbiggrandg_gather: 1
- iptv_org_all: 1

### 地方频道
- epg_cn: 136
- zbds_iptv4_txt: 126
- bigbiggrandg_gather: 97
- iyouhun_zb: 63
- guovin_ipv4: 43
- suxuang_ipv4: 29
- guovin_ipv6: 20
- migu_interface: 13

### 影视剧场
- mursor_yy: 82
- suxuang_ipv4: 22
- zbds_iptv4_txt: 22
- guovin_ipv6: 18
- iyouhun_zb: 17
- guovin_ipv4: 14
- migu_interface: 2
- vamoschuck_m3u: 2

### 少儿动漫
- epg_cn: 9
- mursor_yy: 8
- iyouhun_zb: 4
- guovin_ipv6: 3
- zbds_iptv4_txt: 2
- epg_tw: 1
- iptv_org_all: 1

### 体育纪实
- iyouhun_zb: 24
- zbds_iptv4_txt: 23
- guovin_ipv4: 11
- mursor_yy: 4
- epg_cn: 3
- guovin_ipv6: 1
- suxuang_ipv4: 1

### 音乐综艺
- zbds_iptv4_txt: 18
- mursor_yy: 12
- bigbiggrandg_gather: 10
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- suxuang_ipv4: 1

### 生活休闲
- iyouhun_zb: 51
- guovin_ipv6: 43
- guovin_ipv4: 21
- bigbiggrandg_gather: 14
- vamoschuck_m3u: 12
- epg_cn: 11
- migu_interface: 11
- mursor_yy: 6

### 综合娱乐
- bigbiggrandg_gather: 418
- epg_cn: 185
- iyouhun_zb: 73
- zbds_iptv4_txt: 49
- guovin_ipv6: 35
- suxuang_ipv4: 32
- guovin_ipv4: 29
- epg_tw: 25

### 港澳台频道
- iyouhun_zb: 18
- bigbiggrandg_gather: 16
- epg_tw: 7
- epg_hk: 6
- suxuang_ipv6: 5
- suxuang_ipv4: 3
- guovin_ipv4: 2
- iptv_org_tw: 1

### 海外华语频道
- mursor_yy: 214
- iptv_org_all: 4
- iptv_org_tw: 2


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
