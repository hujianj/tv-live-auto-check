# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2762
Published channel names: 1714
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 461
- Channel limit trimmed rows: 1567
- Group limit trimmed rows: 240
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7044
- unstable_or_wrong_alias: 834
- strict_quality_filter: 461
- foreign_channel: 371
- ambiguous_url_identity: 282
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 183
- 综合娱乐: 34
- 港澳台频道: 16
- 影视剧场: 7

## Groups
- 央视频道: 128
- 卫视频道: 196
- 地方频道: 829
- 影视剧场: 180
- 少儿动漫: 25
- 体育纪实: 66
- 音乐综艺: 33
- 生活休闲: 95
- 综合娱乐: 900
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 433 |
| epg_cn | 417 |
| zbds_iptv4_txt | 401 |
| iyouhun_zb | 366 |
| guovin_all | 355 |
| mursor_yy | 318 |
| guovin_ipv4 | 217 |
| suxuang_ipv4 | 174 |
| migu_interface | 34 |
| epg_tw | 12 |
| iptv_org_all | 10 |
| vamoschuck_m3u | 9 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| suxuang_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 59
- epg_cn: 29
- zbds_iptv4_txt: 19
- suxuang_ipv4: 8
- iptv_org_all: 6
- iyouhun_zb: 6
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 111
- zbds_iptv4_txt: 45
- suxuang_ipv4: 18
- guovin_all: 12
- iyouhun_zb: 7
- guovin_ipv6: 2
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 246
- guovin_all: 237
- iyouhun_zb: 154
- epg_cn: 132
- suxuang_ipv4: 23
- guovin_ipv4: 12
- migu_interface: 11
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 50
- guovin_all: 34
- suxuang_ipv4: 31
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 28
- iyouhun_zb: 19
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 12
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 37
- guovin_all: 29
- epg_cn: 10
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 392
- epg_cn: 226
- iyouhun_zb: 77
- suxuang_ipv4: 77
- zbds_iptv4_txt: 39
- guovin_all: 26
- migu_interface: 20
- mursor_yy: 18

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 11
- epg_cn: 11
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
- free_tv_world: 1

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
