# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2778
Published channel names: 1720
Stability history URLs loaded: 4827
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 494
- Channel limit trimmed rows: 1707
- Group limit trimmed rows: 165
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6988
- unstable_or_wrong_alias: 822
- strict_quality_filter: 494
- foreign_channel: 421
- ambiguous_url_identity: 270
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 151
- 综合娱乐: 14

## Groups
- 央视频道: 131
- 卫视频道: 198
- 地方频道: 864
- 影视剧场: 172
- 少儿动漫: 25
- 体育纪实: 64
- 音乐综艺: 35
- 生活休闲: 96
- 综合娱乐: 900
- 港澳台频道: 73
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 452 |
| zbds_iptv4_txt | 436 |
| bigbiggrandg_gather | 431 |
| guovin_all | 354 |
| iyouhun_zb | 343 |
| mursor_yy | 310 |
| guovin_ipv4 | 213 |
| suxuang_ipv4 | 143 |
| migu_interface | 35 |
| epg_tw | 18 |
| iptv_org_all | 12 |
| vamoschuck_m3u | 10 |
| suxuang_ipv6 | 6 |
| epg_mo | 6 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 57
- zbds_iptv4_txt: 30
- epg_cn: 26
- iptv_org_all: 7
- iyouhun_zb: 6
- migu_interface: 3
- suxuang_ipv4: 2

### 卫视频道
- guovin_ipv4: 106
- zbds_iptv4_txt: 48
- suxuang_ipv4: 19
- guovin_all: 12
- iyouhun_zb: 8
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- zbds_iptv4_txt: 257
- guovin_all: 245
- iyouhun_zb: 159
- epg_cn: 142
- suxuang_ipv4: 24
- guovin_ipv4: 11
- migu_interface: 11
- vamoschuck_m3u: 9

### 影视剧场
- mursor_yy: 45
- guovin_all: 31
- suxuang_ipv4: 28
- iyouhun_zb: 23
- zbds_iptv4_txt: 23
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 9
- guovin_all: 8
- mursor_yy: 6
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- epg_cn: 1
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 33
- guovin_all: 26
- epg_cn: 19
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2

### 综合娱乐
- bigbiggrandg_gather: 389
- epg_cn: 235
- iyouhun_zb: 77
- suxuang_ipv4: 63
- zbds_iptv4_txt: 46
- guovin_all: 23
- migu_interface: 18
- epg_tw: 17

### 港澳台频道
- iyouhun_zb: 18
- epg_cn: 17
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 7
- suxuang_ipv6: 5
- guovin_ipv4: 2
- epg_tw: 1

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
