# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2415
Published channel names: 1495
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 472
- Channel limit trimmed rows: 1573
- Group limit trimmed rows: 394
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6998
- unstable_or_wrong_alias: 801
- strict_quality_filter: 472
- foreign_channel: 310
- ambiguous_url_identity: 181
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 376
- 港澳台频道: 13
- 影视剧场: 5

## Groups
- 央视频道: 127
- 卫视频道: 195
- 地方频道: 718
- 影视剧场: 180
- 少儿动漫: 25
- 体育纪实: 64
- 音乐综艺: 31
- 生活休闲: 85
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 435 |
| epg_cn | 343 |
| mursor_yy | 328 |
| iyouhun_zb | 307 |
| guovin_all | 307 |
| zbds_iptv4_txt | 304 |
| guovin_ipv4 | 215 |
| suxuang_ipv4 | 150 |
| iptv_org_all | 8 |
| vamoschuck_m3u | 8 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| yang_gather | 2 |
| guovin_ipv6 | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 56
- zbds_iptv4_txt: 27
- epg_cn: 26
- suxuang_ipv4: 13
- iptv_org_all: 3
- guovin_ipv6: 1
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 114
- zbds_iptv4_txt: 38
- suxuang_ipv4: 27
- guovin_all: 9
- iyouhun_zb: 6
- iptv_org_all: 1

### 地方频道
- guovin_all: 216
- zbds_iptv4_txt: 180
- iyouhun_zb: 148
- epg_cn: 129
- suxuang_ipv4: 22
- guovin_ipv4: 11
- vamoschuck_m3u: 7
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 54
- suxuang_ipv4: 30
- guovin_all: 28
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 16
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 17
- guovin_ipv4: 7
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- guovin_all: 28
- iyouhun_zb: 24
- epg_cn: 17
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 243
- epg_cn: 154
- iyouhun_zb: 45
- suxuang_ipv4: 41
- guovin_all: 9
- guovin_ipv4: 6
- zbds_iptv4_txt: 3

### 港澳台频道
- iyouhun_zb: 40
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 7
- suxuang_ipv6: 3
- guovin_ipv4: 2
- mursor_yy: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
