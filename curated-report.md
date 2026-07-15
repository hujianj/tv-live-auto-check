# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2536
Published channel names: 1766
Stability history URLs loaded: 3474

## Quality filters and limits

- Strict quality filter dropped rows: 333
- Channel limit trimmed rows: 1301
- Group limit trimmed rows: 211
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7789
- unstable_or_wrong_alias: 747
- foreign_channel: 356
- strict_quality_filter: 333
- cgtn_url: 23
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 125
- 生活休闲: 51
- 海外华语频道: 35

## Groups
- 央视频道: 146
- 卫视频道: 205
- 地方频道: 517
- 影视剧场: 165
- 少儿动漫: 24
- 体育纪实: 66
- 音乐综艺: 46
- 生活休闲: 180
- 综合娱乐: 900
- 港澳台频道: 67
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 546 |
| zbds_iptv4_txt | 366 |
| epg_cn | 356 |
| mursor_yy | 304 |
| iyouhun_zb | 278 |
| guovin_ipv4 | 197 |
| suxuang_ipv4 | 159 |
| guovin_ipv6 | 113 |
| migu_interface | 58 |
| epg_tw | 53 |
| vamoschuck_m3u | 25 |
| iptv_org_all | 24 |
| suxuang_ipv6 | 19 |
| epg_hk | 16 |
| epg_mo | 5 |
| kimentanm_aptv | 4 |
| fanmingming_ipv6_raw | 3 |
| epg_my | 3 |
| iptv_org_tw | 3 |
| yang_gather | 2 |
| mursor_bililive | 1 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 67
- guovin_ipv4: 35
- epg_cn: 25
- iptv_org_all: 12
- migu_interface: 3
- iyouhun_zb: 2
- suxuang_ipv4: 2

### 卫视频道
- zbds_iptv4_txt: 111
- guovin_ipv4: 57
- iyouhun_zb: 10
- suxuang_ipv4: 10
- migu_interface: 8
- guovin_ipv6: 6
- bigbiggrandg_gather: 1
- iptv_org_all: 1

### 地方频道
- epg_cn: 135
- zbds_iptv4_txt: 115
- bigbiggrandg_gather: 91
- iyouhun_zb: 65
- guovin_ipv4: 36
- suxuang_ipv4: 23
- guovin_ipv6: 18
- migu_interface: 16

### 影视剧场
- mursor_yy: 64
- suxuang_ipv4: 33
- iyouhun_zb: 20
- guovin_ipv4: 16
- guovin_ipv6: 13
- zbds_iptv4_txt: 13
- migu_interface: 4
- bigbiggrandg_gather: 1

### 少儿动漫
- epg_cn: 9
- mursor_yy: 5
- iyouhun_zb: 4
- guovin_ipv6: 3
- epg_tw: 2
- iptv_org_all: 1

### 体育纪实
- zbds_iptv4_txt: 26
- iyouhun_zb: 23
- guovin_ipv4: 10
- epg_cn: 3
- mursor_yy: 3
- guovin_ipv6: 1

### 音乐综艺
- suxuang_ipv4: 18
- bigbiggrandg_gather: 10
- mursor_yy: 7
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- guovin_ipv6: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 55
- guovin_ipv6: 36
- epg_cn: 18
- guovin_ipv4: 16
- vamoschuck_m3u: 15
- bigbiggrandg_gather: 14
- migu_interface: 9
- suxuang_ipv4: 8

### 综合娱乐
- bigbiggrandg_gather: 413
- epg_cn: 166
- iyouhun_zb: 79
- suxuang_ipv4: 61
- epg_tw: 43
- guovin_ipv6: 35
- zbds_iptv4_txt: 32
- guovin_ipv4: 20

### 港澳台频道
- iyouhun_zb: 18
- bigbiggrandg_gather: 16
- epg_hk: 9
- epg_tw: 8
- suxuang_ipv6: 5
- suxuang_ipv4: 4
- guovin_ipv4: 3
- free_tv_world: 1

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
