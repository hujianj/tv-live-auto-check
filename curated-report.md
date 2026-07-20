# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2768
Published channel names: 1706
Stability history URLs loaded: 4804
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 490
- Channel limit trimmed rows: 1795
- Group limit trimmed rows: 159
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6940
- unstable_or_wrong_alias: 828
- strict_quality_filter: 490
- foreign_channel: 426
- ambiguous_url_identity: 253
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 132
- 综合娱乐: 27

## Groups
- 央视频道: 134
- 卫视频道: 197
- 地方频道: 862
- 影视剧场: 173
- 少儿动漫: 28
- 体育纪实: 66
- 音乐综艺: 33
- 生活休闲: 81
- 综合娱乐: 900
- 港澳台频道: 74
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 479 |
| zbds_iptv4_txt | 438 |
| bigbiggrandg_gather | 432 |
| guovin_all | 352 |
| iyouhun_zb | 320 |
| mursor_yy | 314 |
| guovin_ipv4 | 208 |
| suxuang_ipv4 | 150 |
| migu_interface | 33 |
| iptv_org_all | 10 |
| vamoschuck_m3u | 9 |
| suxuang_ipv6 | 6 |
| epg_mo | 6 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| yang_gather | 2 |
| guovin_ipv6 | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 59
- epg_cn: 31
- zbds_iptv4_txt: 21
- suxuang_ipv4: 10
- iptv_org_all: 5
- iyouhun_zb: 5
- migu_interface: 3

### 卫视频道
- guovin_ipv4: 99
- zbds_iptv4_txt: 54
- suxuang_ipv4: 19
- guovin_all: 12
- iyouhun_zb: 9
- guovin_ipv6: 1
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- zbds_iptv4_txt: 265
- guovin_all: 243
- iyouhun_zb: 152
- epg_cn: 145
- suxuang_ipv4: 23
- guovin_ipv4: 11
- migu_interface: 9
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 48
- guovin_all: 32
- zbds_iptv4_txt: 25
- suxuang_ipv4: 24
- iyouhun_zb: 22
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 10
- mursor_yy: 8
- guovin_all: 7
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 19
- guovin_ipv4: 10
- epg_cn: 3
- guovin_all: 2
- mursor_yy: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 26
- iyouhun_zb: 21
- epg_cn: 18
- bigbiggrandg_gather: 8
- guovin_ipv4: 3
- mursor_yy: 3
- iptv_org_all: 2

### 综合娱乐
- bigbiggrandg_gather: 391
- epg_cn: 252
- iyouhun_zb: 72
- suxuang_ipv4: 68
- zbds_iptv4_txt: 40
- guovin_all: 23
- mursor_yy: 19
- migu_interface: 18

### 港澳台频道
- epg_cn: 20
- iyouhun_zb: 17
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 6
- suxuang_ipv6: 5
- guovin_ipv4: 2
- epg_tw: 1

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
