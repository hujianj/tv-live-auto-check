# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2605
Published channel names: 1611
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 468
- Channel limit trimmed rows: 1592
- Group limit trimmed rows: 206
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7004
- unstable_or_wrong_alias: 806
- strict_quality_filter: 468
- foreign_channel: 357
- ambiguous_url_identity: 189
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 185
- 港澳台频道: 14
- 影视剧场: 7

## Groups
- 央视频道: 129
- 卫视频道: 202
- 地方频道: 675
- 影视剧场: 180
- 少儿动漫: 24
- 体育纪实: 69
- 音乐综艺: 35
- 生活休闲: 103
- 综合娱乐: 878
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 435 |
| epg_cn | 418 |
| iyouhun_zb | 389 |
| mursor_yy | 323 |
| guovin_all | 312 |
| zbds_iptv4_txt | 308 |
| guovin_ipv4 | 194 |
| suxuang_ipv4 | 178 |
| vamoschuck_m3u | 12 |
| epg_tw | 12 |
| epg_mo | 7 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| epg_hk | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 45
- zbds_iptv4_txt: 45
- epg_cn: 25
- suxuang_ipv4: 8
- iptv_org_all: 4
- iyouhun_zb: 2

### 卫视频道
- guovin_ipv4: 93
- zbds_iptv4_txt: 74
- suxuang_ipv4: 20
- guovin_all: 9
- iyouhun_zb: 6

### 地方频道
- guovin_all: 208
- iyouhun_zb: 160
- epg_cn: 130
- zbds_iptv4_txt: 126
- suxuang_ipv4: 22
- guovin_ipv4: 17
- vamoschuck_m3u: 7
- bigbiggrandg_gather: 4

### 影视剧场
- mursor_yy: 53
- suxuang_ipv4: 32
- guovin_all: 27
- iyouhun_zb: 26
- zbds_iptv4_txt: 22
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 7
- mursor_yy: 7
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 34
- iyouhun_zb: 16
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2
- iyouhun_zb: 1

### 生活休闲
- iyouhun_zb: 42
- guovin_all: 27
- epg_cn: 14
- bigbiggrandg_gather: 8
- guovin_ipv4: 3
- mursor_yy: 3
- vamoschuck_m3u: 3
- iptv_org_all: 2

### 综合娱乐
- bigbiggrandg_gather: 395
- epg_cn: 231
- iyouhun_zb: 94
- suxuang_ipv4: 79
- guovin_all: 25
- mursor_yy: 21
- epg_tw: 12
- epg_mo: 7

### 港澳台频道
- iyouhun_zb: 40
- suxuang_ipv4: 16
- bigbiggrandg_gather: 12
- epg_cn: 9
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
