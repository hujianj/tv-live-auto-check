# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2643
Published channel names: 1620
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 461
- Channel limit trimmed rows: 1628
- Group limit trimmed rows: 204
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7083
- unstable_or_wrong_alias: 821
- strict_quality_filter: 461
- foreign_channel: 367
- ambiguous_url_identity: 224
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 188
- 港澳台频道: 16

## Groups
- 央视频道: 128
- 卫视频道: 195
- 地方频道: 731
- 影视剧场: 180
- 少儿动漫: 25
- 体育纪实: 71
- 音乐综艺: 32
- 生活休闲: 98
- 综合娱乐: 873
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| epg_cn | 424 |
| iyouhun_zb | 386 |
| zbds_iptv4_txt | 370 |
| mursor_yy | 321 |
| guovin_all | 317 |
| guovin_ipv4 | 173 |
| suxuang_ipv4 | 171 |
| vamoschuck_m3u | 13 |
| epg_tw | 11 |
| epg_mo | 7 |
| iptv_org_all | 4 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| epg_hk | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 73
- guovin_ipv4: 29
- epg_cn: 24
- iptv_org_all: 1
- suxuang_ipv4: 1

### 卫视频道
- guovin_ipv4: 93
- zbds_iptv4_txt: 67
- suxuang_ipv4: 19
- guovin_all: 9
- iyouhun_zb: 6
- iptv_org_all: 1

### 地方频道
- guovin_all: 209
- iyouhun_zb: 170
- zbds_iptv4_txt: 168
- epg_cn: 132
- suxuang_ipv4: 23
- guovin_ipv4: 13
- vamoschuck_m3u: 9
- bigbiggrandg_gather: 6

### 影视剧场
- mursor_yy: 50
- suxuang_ipv4: 31
- guovin_all: 29
- iyouhun_zb: 25
- zbds_iptv4_txt: 22
- guovin_ipv4: 17
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 34
- iyouhun_zb: 20
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2
- iyouhun_zb: 1

### 生活休闲
- iyouhun_zb: 38
- guovin_all: 28
- epg_cn: 14
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- vamoschuck_m3u: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- epg_cn: 236
- iyouhun_zb: 85
- suxuang_ipv4: 80
- guovin_all: 25
- mursor_yy: 20
- epg_tw: 11
- guovin_ipv4: 8

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 9
- guovin_all: 7
- suxuang_ipv6: 3
- guovin_ipv4: 2
- mursor_yy: 1

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
