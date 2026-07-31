# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2715
Published channel names: 1678
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 466
- Channel limit trimmed rows: 1399
- Group limit trimmed rows: 207
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7024
- unstable_or_wrong_alias: 828
- strict_quality_filter: 466
- foreign_channel: 355
- ambiguous_url_identity: 260
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 190
- 港澳台频道: 11
- 影视剧场: 6

## Groups
- 央视频道: 131
- 卫视频道: 199
- 地方频道: 796
- 影视剧场: 180
- 少儿动漫: 24
- 体育纪实: 65
- 音乐综艺: 35
- 生活休闲: 99
- 综合娱乐: 876
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 438 |
| iyouhun_zb | 401 |
| epg_cn | 392 |
| guovin_all | 360 |
| zbds_iptv4_txt | 340 |
| mursor_yy | 320 |
| guovin_ipv4 | 210 |
| suxuang_ipv4 | 179 |
| migu_interface | 37 |
| vamoschuck_m3u | 9 |
| iptv_org_all | 8 |
| epg_mo | 7 |
| epg_tw | 5 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| suxuang_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 54
- zbds_iptv4_txt: 33
- epg_cn: 24
- suxuang_ipv4: 8
- iptv_org_all: 5
- iyouhun_zb: 4
- migu_interface: 3

### 卫视频道
- guovin_ipv4: 106
- zbds_iptv4_txt: 50
- suxuang_ipv4: 21
- guovin_all: 12
- iyouhun_zb: 6
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 245
- zbds_iptv4_txt: 216
- iyouhun_zb: 163
- epg_cn: 112
- suxuang_ipv4: 25
- guovin_ipv4: 11
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 51
- iyouhun_zb: 38
- guovin_all: 34
- suxuang_ipv4: 31
- guovin_ipv4: 13
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 5
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
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
- guovin_all: 28
- epg_cn: 16
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 396
- epg_cn: 229
- iyouhun_zb: 88
- suxuang_ipv4: 81
- guovin_all: 24
- migu_interface: 21
- mursor_yy: 16
- epg_mo: 7

### 港澳台频道
- iyouhun_zb: 47
- bigbiggrandg_gather: 13
- suxuang_ipv4: 12
- guovin_all: 7
- epg_cn: 3
- guovin_ipv4: 3
- suxuang_ipv6: 2
- epg_tw: 1

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
