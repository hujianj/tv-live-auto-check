# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2531
Published channel names: 1804
Stability history URLs loaded: 3814
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 343
- Channel limit trimmed rows: 806
- Group limit trimmed rows: 178
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7726
- unstable_or_wrong_alias: 766
- strict_quality_filter: 343
- foreign_channel: 294
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 81
- 综合娱乐: 50
- 生活休闲: 47

## Groups
- 央视频道: 143
- 卫视频道: 208
- 地方频道: 505
- 影视剧场: 176
- 少儿动漫: 20
- 体育纪实: 68
- 音乐综艺: 49
- 生活休闲: 180
- 综合娱乐: 900
- 港澳台频道: 62
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 551 |
| zbds_iptv4_txt | 376 |
| mursor_yy | 330 |
| epg_cn | 303 |
| iyouhun_zb | 284 |
| guovin_ipv4 | 209 |
| suxuang_ipv4 | 178 |
| guovin_all | 112 |
| migu_interface | 66 |
| epg_tw | 35 |
| vamoschuck_m3u | 29 |
| iptv_org_all | 26 |
| epg_hk | 11 |
| epg_mo | 4 |
| fanmingming_ipv6_raw | 3 |
| kimentanm_aptv | 3 |
| mursor_bililive | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| guovin_ipv6 | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 65
- guovin_ipv4: 37
- epg_cn: 21
- iptv_org_all: 13
- migu_interface: 3
- iyouhun_zb: 2
- suxuang_ipv4: 2

### 卫视频道
- zbds_iptv4_txt: 122
- guovin_ipv4: 55
- iyouhun_zb: 10
- suxuang_ipv4: 8
- migu_interface: 7
- guovin_all: 3
- bigbiggrandg_gather: 1
- guovin_ipv6: 1

### 地方频道
- epg_cn: 124
- zbds_iptv4_txt: 117
- bigbiggrandg_gather: 97
- iyouhun_zb: 62
- guovin_ipv4: 41
- suxuang_ipv4: 27
- guovin_all: 16
- migu_interface: 14

### 影视剧场
- mursor_yy: 80
- suxuang_ipv4: 33
- iyouhun_zb: 17
- guovin_all: 16
- guovin_ipv4: 14
- zbds_iptv4_txt: 9
- migu_interface: 4
- vamoschuck_m3u: 2

### 少儿动漫
- epg_cn: 7
- mursor_yy: 7
- guovin_all: 2
- iyouhun_zb: 2
- epg_tw: 1
- iptv_org_all: 1

### 体育纪实
- zbds_iptv4_txt: 27
- iyouhun_zb: 25
- guovin_ipv4: 11
- mursor_yy: 4
- guovin_all: 1

### 音乐综艺
- suxuang_ipv4: 18
- mursor_yy: 11
- bigbiggrandg_gather: 9
- guovin_ipv4: 4
- kimentanm_aptv: 3
- iyouhun_zb: 2
- guovin_all: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 61
- guovin_all: 33
- guovin_ipv4: 19
- vamoschuck_m3u: 15
- bigbiggrandg_gather: 13
- suxuang_ipv4: 11
- migu_interface: 10
- epg_cn: 8

### 综合娱乐
- bigbiggrandg_gather: 415
- epg_cn: 143
- iyouhun_zb: 86
- suxuang_ipv4: 73
- guovin_all: 40
- zbds_iptv4_txt: 34
- migu_interface: 28
- epg_tw: 27

### 港澳台频道
- iyouhun_zb: 17
- bigbiggrandg_gather: 15
- epg_hk: 7
- epg_tw: 7
- suxuang_ipv4: 6
- guovin_ipv4: 3
- suxuang_ipv6: 3
- mursor_yy: 2

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
