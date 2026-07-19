# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2798
Published channel names: 1734
Stability history URLs loaded: 4724
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 481
- Channel limit trimmed rows: 1783
- Group limit trimmed rows: 178
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6931
- unstable_or_wrong_alias: 817
- strict_quality_filter: 481
- foreign_channel: 406
- ambiguous_url_identity: 266
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 141
- 综合娱乐: 27
- 影视剧场: 10

## Groups
- 央视频道: 132
- 卫视频道: 199
- 地方频道: 864
- 影视剧场: 180
- 少儿动漫: 28
- 体育纪实: 68
- 音乐综艺: 34
- 生活休闲: 96
- 综合娱乐: 900
- 港澳台频道: 77
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 497 |
| bigbiggrandg_gather | 423 |
| zbds_iptv4_txt | 415 |
| iyouhun_zb | 357 |
| guovin_all | 350 |
| mursor_yy | 315 |
| guovin_ipv4 | 220 |
| suxuang_ipv4 | 144 |
| migu_interface | 32 |
| iptv_org_all | 11 |
| vamoschuck_m3u | 10 |
| suxuang_ipv6 | 6 |
| epg_mo | 6 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 63
- epg_cn: 29
- zbds_iptv4_txt: 19
- suxuang_ipv4: 8
- iptv_org_all: 6
- iyouhun_zb: 6
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 110
- zbds_iptv4_txt: 45
- suxuang_ipv4: 20
- guovin_all: 12
- iyouhun_zb: 8
- guovin_ipv6: 2
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- zbds_iptv4_txt: 261
- guovin_all: 240
- iyouhun_zb: 159
- epg_cn: 145
- suxuang_ipv4: 23
- guovin_ipv4: 11
- migu_interface: 10
- vamoschuck_m3u: 9

### 影视剧场
- mursor_yy: 49
- iyouhun_zb: 36
- guovin_all: 31
- suxuang_ipv4: 26
- zbds_iptv4_txt: 19
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 11
- guovin_all: 8
- mursor_yy: 7
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 19
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 14
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2
- epg_cn: 1
- iyouhun_zb: 1

### 生活休闲
- iyouhun_zb: 33
- guovin_all: 26
- epg_cn: 20
- bigbiggrandg_gather: 8
- mursor_yy: 4
- guovin_ipv4: 3
- iptv_org_all: 2

### 综合娱乐
- bigbiggrandg_gather: 382
- epg_cn: 267
- iyouhun_zb: 76
- suxuang_ipv4: 60
- zbds_iptv4_txt: 38
- guovin_all: 24
- migu_interface: 19
- mursor_yy: 17

### 港澳台频道
- epg_cn: 21
- iyouhun_zb: 17
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 7
- suxuang_ipv6: 5
- guovin_ipv4: 2
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
