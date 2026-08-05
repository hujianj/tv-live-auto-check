# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2648
Published channel names: 1629
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 464
- Channel limit trimmed rows: 1478
- Group limit trimmed rows: 208
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7034
- unstable_or_wrong_alias: 831
- strict_quality_filter: 464
- foreign_channel: 375
- ambiguous_url_identity: 251
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 186
- 港澳台频道: 16
- 影视剧场: 6

## Groups
- 央视频道: 134
- 卫视频道: 198
- 地方频道: 715
- 影视剧场: 180
- 少儿动漫: 24
- 体育纪实: 71
- 音乐综艺: 33
- 生活休闲: 98
- 综合娱乐: 885
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| epg_cn | 426 |
| iyouhun_zb | 363 |
| guovin_all | 336 |
| mursor_yy | 322 |
| zbds_iptv4_txt | 296 |
| guovin_ipv4 | 210 |
| suxuang_ipv4 | 172 |
| migu_interface | 35 |
| epg_tw | 17 |
| iptv_org_all | 10 |
| vamoschuck_m3u | 10 |
| epg_mo | 6 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| suxuang_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 57
- zbds_iptv4_txt: 31
- epg_cn: 28
- iptv_org_all: 7
- suxuang_ipv4: 5
- iyouhun_zb: 4
- migu_interface: 2

### 卫视频道
- guovin_ipv4: 103
- zbds_iptv4_txt: 53
- suxuang_ipv4: 23
- guovin_all: 12
- iyouhun_zb: 4
- guovin_ipv6: 2
- iptv_org_all: 1

### 地方频道
- guovin_all: 224
- iyouhun_zb: 154
- zbds_iptv4_txt: 154
- epg_cn: 128
- suxuang_ipv4: 20
- guovin_ipv4: 14
- migu_interface: 9
- vamoschuck_m3u: 6

### 影视剧场
- mursor_yy: 51
- guovin_all: 34
- suxuang_ipv4: 31
- iyouhun_zb: 23
- zbds_iptv4_txt: 22
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- mursor_yy: 8
- epg_cn: 6
- guovin_all: 6
- iyouhun_zb: 2
- epg_tw: 1
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 19
- guovin_ipv4: 10
- guovin_all: 4
- mursor_yy: 4
- epg_cn: 3

### 音乐综艺
- mursor_yy: 14
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 38
- guovin_all: 24
- epg_cn: 16
- bigbiggrandg_gather: 8
- mursor_yy: 4
- guovin_ipv4: 3
- iptv_org_all: 2
- vamoschuck_m3u: 2

### 综合娱乐
- bigbiggrandg_gather: 394
- epg_cn: 234
- iyouhun_zb: 80
- suxuang_ipv4: 77
- guovin_all: 25
- migu_interface: 22
- mursor_yy: 20
- epg_tw: 16

### 港澳台频道
- iyouhun_zb: 38
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- epg_cn: 11
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
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
