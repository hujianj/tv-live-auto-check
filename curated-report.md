# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2569
Published channel names: 1788
Stability history URLs loaded: 3754

## Quality filters and limits

- Strict quality filter dropped rows: 349
- Channel limit trimmed rows: 1287
- Group limit trimmed rows: 227
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7857
- unstable_or_wrong_alias: 762
- strict_quality_filter: 349
- foreign_channel: 320
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 117
- 生活休闲: 60
- 海外华语频道: 50

## Groups
- 央视频道: 148
- 卫视频道: 210
- 地方频道: 528
- 影视剧场: 172
- 少儿动漫: 26
- 体育纪实: 69
- 音乐综艺: 51
- 生活休闲: 180
- 综合娱乐: 900
- 港澳台频道: 65
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 546 |
| zbds_iptv4_txt | 370 |
| epg_cn | 364 |
| mursor_yy | 322 |
| iyouhun_zb | 265 |
| guovin_ipv4 | 217 |
| suxuang_ipv4 | 158 |
| guovin_all | 124 |
| migu_interface | 64 |
| epg_tw | 40 |
| vamoschuck_m3u | 31 |
| iptv_org_all | 25 |
| epg_hk | 15 |
| epg_mo | 5 |
| kimentanm_aptv | 4 |
| mursor_bililive | 4 |
| fanmingming_ipv6_raw | 3 |
| suxuang_ipv6 | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| epg_my | 2 |
| iptv_org_tw | 2 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 64
- guovin_ipv4: 39
- epg_cn: 25
- iptv_org_all: 13
- suxuang_ipv4: 3
- iyouhun_zb: 2
- migu_interface: 2

### 卫视频道
- zbds_iptv4_txt: 111
- guovin_ipv4: 64
- iyouhun_zb: 11
- migu_interface: 8
- suxuang_ipv4: 8
- guovin_all: 4
- guovin_ipv6: 2
- bigbiggrandg_gather: 1

### 地方频道
- epg_cn: 135
- zbds_iptv4_txt: 120
- bigbiggrandg_gather: 96
- iyouhun_zb: 67
- guovin_ipv4: 42
- suxuang_ipv4: 25
- guovin_all: 23
- migu_interface: 14

### 影视剧场
- mursor_yy: 73
- suxuang_ipv4: 30
- guovin_all: 20
- guovin_ipv4: 16
- iyouhun_zb: 14
- zbds_iptv4_txt: 13
- migu_interface: 4
- bigbiggrandg_gather: 1

### 少儿动漫
- epg_cn: 9
- mursor_yy: 8
- guovin_all: 3
- iyouhun_zb: 2
- zbds_iptv4_txt: 2
- epg_tw: 1
- iptv_org_all: 1

### 体育纪实
- zbds_iptv4_txt: 27
- iyouhun_zb: 23
- guovin_ipv4: 11
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 1

### 音乐综艺
- suxuang_ipv4: 18
- mursor_yy: 12
- bigbiggrandg_gather: 9
- guovin_ipv4: 4
- iyouhun_zb: 3
- kimentanm_aptv: 3
- guovin_all: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 50
- guovin_all: 33
- epg_cn: 19
- vamoschuck_m3u: 19
- guovin_ipv4: 15
- bigbiggrandg_gather: 13
- migu_interface: 11
- suxuang_ipv4: 9

### 综合娱乐
- bigbiggrandg_gather: 411
- epg_cn: 173
- iyouhun_zb: 75
- suxuang_ipv4: 58
- guovin_all: 39
- epg_tw: 32
- zbds_iptv4_txt: 31
- migu_interface: 25

### 港澳台频道
- iyouhun_zb: 18
- bigbiggrandg_gather: 15
- epg_hk: 9
- epg_tw: 7
- suxuang_ipv4: 7
- guovin_ipv4: 3
- suxuang_ipv6: 3
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
