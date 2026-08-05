# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2642
Published channel names: 1637
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 468
- Channel limit trimmed rows: 1404
- Group limit trimmed rows: 204
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7088
- unstable_or_wrong_alias: 813
- strict_quality_filter: 468
- foreign_channel: 370
- ambiguous_url_identity: 258
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 186
- 港澳台频道: 14
- 影视剧场: 4

## Groups
- 央视频道: 129
- 卫视频道: 191
- 地方频道: 775
- 影视剧场: 180
- 少儿动漫: 26
- 体育纪实: 63
- 音乐综艺: 34
- 生活休闲: 83
- 综合娱乐: 851
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 434 |
| epg_cn | 410 |
| zbds_iptv4_txt | 356 |
| iyouhun_zb | 342 |
| guovin_all | 329 |
| mursor_yy | 317 |
| guovin_ipv4 | 203 |
| suxuang_ipv4 | 177 |
| migu_interface | 35 |
| iptv_org_all | 9 |
| vamoschuck_m3u | 8 |
| epg_tw | 6 |
| epg_mo | 6 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 54
- zbds_iptv4_txt: 33
- epg_cn: 24
- iptv_org_all: 6
- suxuang_ipv4: 5
- iyouhun_zb: 4
- migu_interface: 3

### 卫视频道
- guovin_ipv4: 99
- zbds_iptv4_txt: 52
- suxuang_ipv4: 20
- guovin_all: 10
- iyouhun_zb: 7
- guovin_ipv6: 2
- iptv_org_all: 1

### 地方频道
- guovin_all: 223
- zbds_iptv4_txt: 215
- iyouhun_zb: 152
- epg_cn: 127
- suxuang_ipv4: 23
- guovin_ipv4: 13
- migu_interface: 9
- vamoschuck_m3u: 7

### 影视剧场
- mursor_yy: 49
- guovin_all: 34
- suxuang_ipv4: 31
- iyouhun_zb: 23
- zbds_iptv4_txt: 22
- guovin_ipv4: 12
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- mursor_yy: 8
- epg_cn: 7
- guovin_all: 7
- iyouhun_zb: 2
- epg_tw: 1
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 29
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
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 28
- guovin_all: 24
- epg_cn: 12
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- epg_cn: 228
- suxuang_ipv4: 80
- iyouhun_zb: 71
- guovin_all: 22
- migu_interface: 21
- mursor_yy: 16
- guovin_ipv4: 7

### 港澳台频道
- iyouhun_zb: 38
- suxuang_ipv4: 17
- bigbiggrandg_gather: 12
- epg_cn: 9
- guovin_all: 7
- guovin_ipv4: 2
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
