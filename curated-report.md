# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2632
Published channel names: 1604
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 465
- Channel limit trimmed rows: 1576
- Group limit trimmed rows: 204
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7021
- unstable_or_wrong_alias: 820
- strict_quality_filter: 465
- foreign_channel: 365
- ambiguous_url_identity: 220
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 188
- 港澳台频道: 14
- 影视剧场: 2

## Groups
- 央视频道: 128
- 卫视频道: 198
- 地方频道: 729
- 影视剧场: 180
- 少儿动漫: 23
- 体育纪实: 70
- 音乐综艺: 33
- 生活休闲: 100
- 综合娱乐: 861
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 425 |
| epg_cn | 410 |
| iyouhun_zb | 396 |
| zbds_iptv4_txt | 356 |
| mursor_yy | 321 |
| guovin_all | 313 |
| guovin_ipv4 | 190 |
| suxuang_ipv4 | 173 |
| vamoschuck_m3u | 13 |
| epg_tw | 12 |
| epg_mo | 7 |
| iptv_org_all | 5 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| epg_hk | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 57
- guovin_ipv4: 37
- epg_cn: 24
- suxuang_ipv4: 6
- iptv_org_all: 3
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 96
- zbds_iptv4_txt: 66
- suxuang_ipv4: 21
- guovin_all: 9
- iyouhun_zb: 6

### 地方频道
- guovin_all: 206
- iyouhun_zb: 179
- zbds_iptv4_txt: 169
- epg_cn: 125
- suxuang_ipv4: 22
- guovin_ipv4: 14
- vamoschuck_m3u: 9
- bigbiggrandg_gather: 4

### 影视剧场
- mursor_yy: 50
- suxuang_ipv4: 31
- guovin_all: 28
- iyouhun_zb: 26
- zbds_iptv4_txt: 22
- guovin_ipv4: 17
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 7
- epg_cn: 6
- mursor_yy: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 35
- iyouhun_zb: 16
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
- iyouhun_zb: 1

### 生活休闲
- iyouhun_zb: 38
- guovin_all: 27
- epg_cn: 15
- bigbiggrandg_gather: 7
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- vamoschuck_m3u: 2

### 综合娱乐
- bigbiggrandg_gather: 387
- epg_cn: 228
- iyouhun_zb: 87
- suxuang_ipv4: 77
- guovin_all: 27
- mursor_yy: 21
- epg_tw: 12
- guovin_ipv4: 8

### 港澳台频道
- iyouhun_zb: 40
- suxuang_ipv4: 15
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
