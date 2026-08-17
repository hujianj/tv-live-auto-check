# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2254
Published channel names: 1428
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 434
- Channel limit trimmed rows: 800
- Group limit trimmed rows: 194
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6973
- unstable_or_wrong_alias: 839
- strict_quality_filter: 434
- foreign_channel: 317
- ambiguous_url_identity: 125
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 194

## Groups
- 央视频道: 127
- 卫视频道: 193
- 地方频道: 670
- 影视剧场: 150
- 少儿动漫: 14
- 体育纪实: 47
- 音乐综艺: 27
- 生活休闲: 63
- 综合娱乐: 900
- 港澳台频道: 63

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 441 |
| zbds_iptv4_txt | 419 |
| guovin_all | 369 |
| epg_cn | 347 |
| mursor_yy | 288 |
| guovin_ipv4 | 174 |
| suxuang_ipv4 | 161 |
| vamoschuck_m3u | 21 |
| iptv_org_all | 8 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| iyouhun_zb | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 65
- guovin_ipv4: 38
- epg_cn: 19
- suxuang_ipv4: 4
- iptv_org_all: 1

### 卫视频道
- guovin_ipv4: 85
- zbds_iptv4_txt: 73
- suxuang_ipv4: 22
- guovin_all: 9
- bigbiggrandg_gather: 1
- guovin_ipv6: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 253
- zbds_iptv4_txt: 221
- epg_cn: 134
- suxuang_ipv4: 22
- vamoschuck_m3u: 19
- guovin_ipv4: 12
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- suxuang_ipv4: 35
- guovin_all: 34
- mursor_yy: 33
- zbds_iptv4_txt: 23
- guovin_ipv4: 19
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 7
- mursor_yy: 4
- zbds_iptv4_txt: 3

### 体育纪实
- zbds_iptv4_txt: 28
- guovin_ipv4: 8
- guovin_all: 5
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 11
- mursor_yy: 9
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 17
- bigbiggrandg_gather: 9
- mursor_yy: 3
- iptv_org_all: 2
- guovin_ipv4: 1
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 233
- epg_cn: 168
- suxuang_ipv4: 57
- guovin_all: 23
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 5

### 港澳台频道
- suxuang_ipv4: 20
- bigbiggrandg_gather: 16
- guovin_all: 8
- epg_cn: 6
- suxuang_ipv6: 6
- mursor_yy: 3
- guovin_ipv4: 2
- epg_hk: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
