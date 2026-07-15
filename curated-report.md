# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2521
Published channel names: 1753
Stability history URLs loaded: 3775
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 347
- Channel limit trimmed rows: 1207
- Group limit trimmed rows: 208
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7556
- unstable_or_wrong_alias: 740
- strict_quality_filter: 347
- foreign_channel: 300
- cgtn_url: 24
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 105
- 生活休闲: 53
- 海外华语频道: 50

## Groups
- 央视频道: 148
- 卫视频道: 197
- 地方频道: 507
- 影视剧场: 168
- 少儿动漫: 24
- 体育纪实: 68
- 音乐综艺: 48
- 生活休闲: 180
- 综合娱乐: 900
- 港澳台频道: 61
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 545 |
| epg_cn | 367 |
| mursor_yy | 320 |
| iyouhun_zb | 259 |
| guovin_ipv4 | 243 |
| zbds_iptv4_m3u | 186 |
| suxuang_ipv4 | 163 |
| zbds_iptv4_txt | 139 |
| guovin_all | 108 |
| migu_interface | 51 |
| epg_tw | 37 |
| vamoschuck_m3u | 27 |
| iptv_org_all | 25 |
| suxuang_ipv6 | 15 |
| epg_hk | 13 |
| epg_mo | 5 |
| kimentanm_aptv | 4 |
| guovin_ipv6 | 3 |
| fanmingming_ipv6_raw | 3 |
| mursor_bililive | 2 |
| yang_gather | 2 |
| epg_my | 2 |
| iptv_org_tw | 2 |

## Top sources per group

### 央视频道
- guovin_ipv4: 47
- zbds_iptv4_txt: 46
- epg_cn: 28
- iptv_org_all: 13
- zbds_iptv4_m3u: 7
- iyouhun_zb: 3
- migu_interface: 2
- suxuang_ipv4: 2

### 卫视频道
- guovin_ipv4: 75
- zbds_iptv4_txt: 73
- zbds_iptv4_m3u: 16
- iyouhun_zb: 10
- suxuang_ipv4: 9
- guovin_all: 4
- migu_interface: 4
- guovin_ipv6: 3

### 地方频道
- epg_cn: 137
- bigbiggrandg_gather: 95
- zbds_iptv4_m3u: 91
- iyouhun_zb: 56
- guovin_ipv4: 43
- suxuang_ipv4: 24
- zbds_iptv4_txt: 20
- guovin_all: 14

### 影视剧场
- mursor_yy: 74
- suxuang_ipv4: 28
- guovin_ipv4: 18
- iyouhun_zb: 18
- guovin_all: 14
- zbds_iptv4_m3u: 10
- migu_interface: 3
- vamoschuck_m3u: 2

### 少儿动漫
- epg_cn: 9
- mursor_yy: 7
- guovin_all: 3
- iyouhun_zb: 2
- epg_tw: 1
- iptv_org_all: 1
- zbds_iptv4_m3u: 1

### 体育纪实
- zbds_iptv4_m3u: 27
- iyouhun_zb: 23
- guovin_ipv4: 11
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 1

### 音乐综艺
- suxuang_ipv4: 18
- bigbiggrandg_gather: 10
- mursor_yy: 9
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- guovin_all: 1
- zbds_iptv4_m3u: 1

### 生活休闲
- iyouhun_zb: 54
- guovin_all: 33
- epg_cn: 19
- guovin_ipv4: 19
- vamoschuck_m3u: 15
- bigbiggrandg_gather: 13
- migu_interface: 9
- suxuang_ipv4: 7

### 综合娱乐
- bigbiggrandg_gather: 410
- epg_cn: 171
- iyouhun_zb: 75
- suxuang_ipv4: 70
- guovin_all: 38
- zbds_iptv4_m3u: 32
- epg_tw: 31
- guovin_ipv4: 23

### 港澳台频道
- iyouhun_zb: 16
- bigbiggrandg_gather: 15
- epg_hk: 8
- epg_tw: 5
- suxuang_ipv4: 5
- suxuang_ipv6: 5
- guovin_ipv4: 3
- mursor_yy: 2

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
