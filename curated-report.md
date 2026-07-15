# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2626
Published channel names: 1816
Stability history URLs loaded: 3722

## Quality filters and limits

- Strict quality filter dropped rows: 371
- Channel limit trimmed rows: 1264
- Group limit trimmed rows: 101
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7846
- unstable_or_wrong_alias: 750
- strict_quality_filter: 371
- foreign_channel: 312
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 综合娱乐: 90
- 生活休闲: 11

## Groups
- 央视频道: 148
- 卫视频道: 207
- 地方频道: 625
- 影视剧场: 160
- 少儿动漫: 23
- 体育纪实: 73
- 音乐综艺: 50
- 生活休闲: 180
- 综合娱乐: 900
- 港澳台频道: 64
- 海外华语频道: 196

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 550 |
| zbds_iptv4_txt | 445 |
| epg_cn | 401 |
| iyouhun_zb | 300 |
| mursor_yy | 278 |
| guovin_ipv4 | 268 |
| suxuang_ipv4 | 138 |
| migu_interface | 55 |
| guovin_ipv6 | 52 |
| epg_tw | 42 |
| vamoschuck_m3u | 37 |
| iptv_org_all | 23 |
| epg_hk | 13 |
| epg_mo | 5 |
| kimentanm_aptv | 4 |
| fanmingming_ipv6_raw | 3 |
| suxuang_ipv6 | 3 |
| mursor_bililive | 2 |
| yang_gather | 2 |
| epg_my | 2 |
| iptv_org_tw | 2 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 56
- zbds_iptv4_txt: 39
- epg_cn: 27
- iptv_org_all: 13
- iyouhun_zb: 9
- migu_interface: 2
- suxuang_ipv4: 2

### 卫视频道
- guovin_ipv4: 91
- zbds_iptv4_txt: 72
- suxuang_ipv4: 16
- iyouhun_zb: 14
- guovin_ipv6: 6
- migu_interface: 6
- bigbiggrandg_gather: 1
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 227
- epg_cn: 139
- bigbiggrandg_gather: 97
- iyouhun_zb: 59
- guovin_ipv4: 42
- suxuang_ipv4: 30
- guovin_ipv6: 13
- migu_interface: 12

### 影视剧场
- mursor_yy: 54
- suxuang_ipv4: 25
- zbds_iptv4_txt: 21
- guovin_ipv6: 20
- iyouhun_zb: 18
- guovin_ipv4: 16
- migu_interface: 3
- vamoschuck_m3u: 2

### 少儿动漫
- epg_cn: 9
- mursor_yy: 6
- guovin_ipv6: 2
- iyouhun_zb: 2
- zbds_iptv4_txt: 2
- epg_tw: 1
- iptv_org_all: 1

### 体育纪实
- iyouhun_zb: 27
- zbds_iptv4_txt: 26
- guovin_ipv4: 11
- mursor_yy: 4
- epg_cn: 3
- guovin_ipv6: 1
- suxuang_ipv4: 1

### 音乐综艺
- zbds_iptv4_txt: 18
- bigbiggrandg_gather: 11
- mursor_yy: 11
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- suxuang_ipv4: 1

### 生活休闲
- iyouhun_zb: 70
- epg_cn: 26
- vamoschuck_m3u: 26
- guovin_ipv4: 19
- bigbiggrandg_gather: 13
- migu_interface: 10
- guovin_ipv6: 5
- iptv_org_all: 4

### 综合娱乐
- bigbiggrandg_gather: 412
- epg_cn: 197
- iyouhun_zb: 81
- suxuang_ipv4: 54
- zbds_iptv4_txt: 38
- epg_tw: 34
- guovin_ipv4: 26
- migu_interface: 22

### 港澳台频道
- iyouhun_zb: 18
- bigbiggrandg_gather: 15
- epg_hk: 7
- epg_tw: 7
- suxuang_ipv4: 7
- guovin_ipv4: 3
- suxuang_ipv6: 3
- free_tv_world: 1

### 海外华语频道
- mursor_yy: 193
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
