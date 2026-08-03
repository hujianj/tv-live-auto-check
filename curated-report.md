# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2758
Published channel names: 1696
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 472
- Channel limit trimmed rows: 1574
- Group limit trimmed rows: 216
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7050
- unstable_or_wrong_alias: 814
- strict_quality_filter: 472
- foreign_channel: 366
- ambiguous_url_identity: 284
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 196
- 港澳台频道: 13
- 影视剧场: 7

## Groups
- 央视频道: 130
- 卫视频道: 192
- 地方频道: 816
- 影视剧场: 180
- 少儿动漫: 28
- 体育纪实: 68
- 音乐综艺: 33
- 生活休闲: 102
- 综合娱乐: 899
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 444 |
| bigbiggrandg_gather | 433 |
| iyouhun_zb | 372 |
| guovin_all | 357 |
| zbds_iptv4_txt | 340 |
| mursor_yy | 324 |
| guovin_ipv4 | 222 |
| suxuang_ipv4 | 172 |
| migu_interface | 38 |
| epg_tw | 21 |
| iptv_org_all | 9 |
| vamoschuck_m3u | 9 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| guovin_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 61
- zbds_iptv4_txt: 24
- epg_cn: 23
- suxuang_ipv4: 8
- iptv_org_all: 6
- iyouhun_zb: 4
- migu_interface: 4

### 卫视频道
- guovin_ipv4: 112
- zbds_iptv4_txt: 40
- suxuang_ipv4: 17
- guovin_all: 12
- iyouhun_zb: 7
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 245
- zbds_iptv4_txt: 219
- iyouhun_zb: 155
- epg_cn: 138
- suxuang_ipv4: 22
- guovin_ipv4: 13
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 52
- guovin_all: 33
- suxuang_ipv4: 31
- iyouhun_zb: 23
- zbds_iptv4_txt: 22
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 7
- epg_tw: 2
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 19
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 37
- guovin_all: 26
- epg_cn: 20
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 392
- epg_cn: 245
- iyouhun_zb: 85
- suxuang_ipv4: 77
- guovin_all: 24
- migu_interface: 21
- epg_tw: 19
- mursor_yy: 19

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 7
- suxuang_ipv6: 3
- guovin_ipv4: 2
- free_tv_world: 1

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
