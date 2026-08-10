# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2625
Published channel names: 1607
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 462
- Channel limit trimmed rows: 1615
- Group limit trimmed rows: 190
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7082
- unstable_or_wrong_alias: 815
- strict_quality_filter: 462
- foreign_channel: 364
- ambiguous_url_identity: 220
- cgtn_url: 25
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 171
- 港澳台频道: 17
- 影视剧场: 2

## Groups
- 央视频道: 128
- 卫视频道: 196
- 地方频道: 727
- 影视剧场: 180
- 少儿动漫: 23
- 体育纪实: 68
- 音乐综艺: 34
- 生活休闲: 96
- 综合娱乐: 863
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 438 |
| epg_cn | 411 |
| iyouhun_zb | 384 |
| zbds_iptv4_txt | 370 |
| guovin_all | 319 |
| mursor_yy | 313 |
| guovin_ipv4 | 174 |
| suxuang_ipv4 | 172 |
| epg_tw | 11 |
| vamoschuck_m3u | 10 |
| epg_mo | 7 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| epg_hk | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 74
- guovin_ipv4: 29
- epg_cn: 23
- iptv_org_all: 1
- suxuang_ipv4: 1

### 卫视频道
- guovin_ipv4: 94
- zbds_iptv4_txt: 68
- suxuang_ipv4: 19
- guovin_all: 9
- iyouhun_zb: 5
- iptv_org_all: 1

### 地方频道
- guovin_all: 209
- iyouhun_zb: 172
- zbds_iptv4_txt: 167
- epg_cn: 129
- suxuang_ipv4: 23
- guovin_ipv4: 12
- vamoschuck_m3u: 8
- bigbiggrandg_gather: 6

### 影视剧场
- mursor_yy: 48
- suxuang_ipv4: 32
- guovin_all: 30
- iyouhun_zb: 25
- zbds_iptv4_txt: 21
- guovin_ipv4: 18
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- epg_cn: 6
- mursor_yy: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 34
- iyouhun_zb: 17
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 12
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2
- iyouhun_zb: 1

### 生活休闲
- iyouhun_zb: 37
- guovin_all: 29
- epg_cn: 14
- bigbiggrandg_gather: 8
- mursor_yy: 4
- iptv_org_all: 2
- suxuang_ipv4: 1
- vamoschuck_m3u: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- epg_cn: 227
- iyouhun_zb: 86
- suxuang_ipv4: 80
- guovin_all: 25
- mursor_yy: 19
- epg_tw: 11
- guovin_ipv4: 8

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 9
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
- free_tv_world: 1

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
