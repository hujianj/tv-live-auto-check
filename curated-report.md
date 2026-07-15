# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2530
Published channel names: 1763
Stability history URLs loaded: 3667

## Quality filters and limits

- Strict quality filter dropped rows: 371
- Channel limit trimmed rows: 1218
- Group limit trimmed rows: 178
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 8024
- unstable_or_wrong_alias: 756
- strict_quality_filter: 371
- foreign_channel: 341
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 综合娱乐: 102
- 生活休闲: 64
- 海外华语频道: 12

## Groups
- 央视频道: 149
- 卫视频道: 203
- 地方频道: 524
- 影视剧场: 160
- 少儿动漫: 20
- 体育纪实: 68
- 音乐综艺: 47
- 生活休闲: 180
- 综合娱乐: 900
- 港澳台频道: 59
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 549 |
| epg_cn | 381 |
| mursor_yy | 301 |
| iyouhun_zb | 268 |
| guovin_ipv4 | 266 |
| zbds_iptv4_m3u | 183 |
| suxuang_ipv4 | 161 |
| zbds_iptv4_txt | 118 |
| guovin_ipv6 | 116 |
| migu_interface | 61 |
| epg_tw | 34 |
| vamoschuck_m3u | 26 |
| iptv_org_all | 25 |
| suxuang_ipv6 | 14 |
| epg_hk | 8 |
| epg_mo | 5 |
| kimentanm_aptv | 4 |
| fanmingming_ipv6_raw | 3 |
| yang_gather | 2 |
| epg_my | 2 |
| iptv_org_tw | 2 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 58
- zbds_iptv4_txt: 32
- epg_cn: 29
- iptv_org_all: 12
- iyouhun_zb: 7
- suxuang_ipv4: 5
- zbds_iptv4_m3u: 4
- migu_interface: 2

### 卫视频道
- guovin_ipv4: 90
- zbds_iptv4_txt: 63
- suxuang_ipv4: 13
- zbds_iptv4_m3u: 10
- iyouhun_zb: 9
- migu_interface: 8
- guovin_ipv6: 7
- bigbiggrandg_gather: 1

### 地方频道
- epg_cn: 139
- bigbiggrandg_gather: 96
- zbds_iptv4_m3u: 95
- iyouhun_zb: 61
- guovin_ipv4: 41
- suxuang_ipv4: 24
- zbds_iptv4_txt: 23
- guovin_ipv6: 17

### 影视剧场
- mursor_yy: 60
- suxuang_ipv4: 34
- iyouhun_zb: 17
- guovin_ipv4: 16
- guovin_ipv6: 14
- zbds_iptv4_m3u: 13
- migu_interface: 4
- bigbiggrandg_gather: 1

### 少儿动漫
- epg_cn: 8
- guovin_ipv6: 3
- mursor_yy: 3
- iyouhun_zb: 2
- zbds_iptv4_m3u: 2
- epg_tw: 1
- iptv_org_all: 1

### 体育纪实
- iyouhun_zb: 25
- zbds_iptv4_m3u: 25
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_ipv6: 1

### 音乐综艺
- suxuang_ipv4: 18
- bigbiggrandg_gather: 10
- mursor_yy: 8
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- guovin_ipv6: 1
- zbds_iptv4_m3u: 1

### 生活休闲
- iyouhun_zb: 49
- guovin_ipv6: 35
- epg_cn: 20
- guovin_ipv4: 19
- vamoschuck_m3u: 15
- bigbiggrandg_gather: 13
- migu_interface: 10
- suxuang_ipv4: 7

### 综合娱乐
- bigbiggrandg_gather: 413
- epg_cn: 182
- iyouhun_zb: 78
- suxuang_ipv4: 55
- guovin_ipv6: 38
- zbds_iptv4_m3u: 32
- epg_tw: 26
- guovin_ipv4: 25

### 港澳台频道
- iyouhun_zb: 18
- bigbiggrandg_gather: 15
- epg_tw: 7
- suxuang_ipv4: 5
- suxuang_ipv6: 5
- epg_hk: 3
- guovin_ipv4: 3
- free_tv_world: 1

### 海外华语频道
- mursor_yy: 216
- iptv_org_all: 3
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
