# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2414
Published channel names: 1795
Stability history URLs loaded: 3884
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 342
- Channel limit trimmed rows: 571
- Group limit trimmed rows: 92
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7830
- unstable_or_wrong_alias: 749
- strict_quality_filter: 342
- foreign_channel: 302
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 79
- 影视剧场: 13

## Groups
- 央视频道: 134
- 卫视频道: 201
- 地方频道: 480
- 影视剧场: 180
- 少儿动漫: 21
- 体育纪实: 69
- 音乐综艺: 51
- 生活休闲: 168
- 综合娱乐: 834
- 港澳台频道: 56
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 552 |
| zbds_iptv4_txt | 350 |
| mursor_yy | 338 |
| iyouhun_zb | 254 |
| epg_cn | 253 |
| guovin_ipv4 | 240 |
| suxuang_ipv4 | 157 |
| guovin_ipv6 | 115 |
| migu_interface | 56 |
| epg_tw | 26 |
| iptv_org_all | 25 |
| suxuang_ipv6 | 17 |
| vamoschuck_m3u | 17 |
| kimentanm_aptv | 4 |
| fanmingming_ipv6_raw | 4 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| epg_mo | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 51
- zbds_iptv4_txt: 43
- iptv_org_all: 14
- epg_cn: 13
- migu_interface: 5
- iyouhun_zb: 4
- suxuang_ipv4: 4

### 卫视频道
- zbds_iptv4_txt: 96
- guovin_ipv4: 74
- iyouhun_zb: 9
- suxuang_ipv4: 8
- migu_interface: 7
- guovin_ipv6: 4
- bigbiggrandg_gather: 1
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 118
- epg_cn: 105
- bigbiggrandg_gather: 95
- iyouhun_zb: 58
- guovin_ipv4: 39
- suxuang_ipv4: 23
- guovin_ipv6: 16
- suxuang_ipv6: 10

### 影视剧场
- mursor_yy: 78
- suxuang_ipv4: 31
- guovin_ipv6: 20
- iyouhun_zb: 16
- zbds_iptv4_txt: 16
- guovin_ipv4: 14
- migu_interface: 3
- bigbiggrandg_gather: 1

### 少儿动漫
- mursor_yy: 8
- epg_cn: 6
- guovin_ipv6: 2
- iyouhun_zb: 2
- zbds_iptv4_txt: 2
- iptv_org_all: 1

### 体育纪实
- zbds_iptv4_txt: 26
- iyouhun_zb: 25
- guovin_ipv4: 10
- mursor_yy: 5
- epg_cn: 3

### 音乐综艺
- suxuang_ipv4: 18
- mursor_yy: 12
- bigbiggrandg_gather: 10
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- guovin_ipv6: 1
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_ipv6: 44
- iyouhun_zb: 38
- guovin_ipv4: 20
- bigbiggrandg_gather: 13
- vamoschuck_m3u: 12
- suxuang_ipv4: 10
- epg_cn: 9
- migu_interface: 8

### 综合娱乐
- bigbiggrandg_gather: 415
- epg_cn: 117
- iyouhun_zb: 82
- suxuang_ipv4: 60
- zbds_iptv4_txt: 47
- guovin_ipv6: 28
- guovin_ipv4: 25
- migu_interface: 24

### 港澳台频道
- iyouhun_zb: 18
- bigbiggrandg_gather: 17
- epg_tw: 6
- suxuang_ipv6: 5
- guovin_ipv4: 3
- suxuang_ipv4: 3
- mursor_yy: 2
- iptv_org_tw: 1

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
