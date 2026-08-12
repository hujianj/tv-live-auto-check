# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2503
Published channel names: 1521
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 477
- Channel limit trimmed rows: 1698
- Group limit trimmed rows: 408
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7000
- unstable_or_wrong_alias: 804
- strict_quality_filter: 477
- foreign_channel: 304
- ambiguous_url_identity: 217
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 393
- 港澳台频道: 15

## Groups
- 央视频道: 128
- 卫视频道: 201
- 地方频道: 798
- 影视剧场: 167
- 少儿动漫: 24
- 体育纪实: 64
- 音乐综艺: 33
- 生活休闲: 98
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 435 |
| zbds_iptv4_txt | 393 |
| iyouhun_zb | 363 |
| epg_cn | 348 |
| mursor_yy | 326 |
| guovin_all | 289 |
| guovin_ipv4 | 182 |
| suxuang_ipv4 | 140 |
| vamoschuck_m3u | 11 |
| iptv_org_all | 7 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 53
- guovin_ipv4: 45
- epg_cn: 21
- suxuang_ipv4: 5
- iptv_org_all: 3
- iyouhun_zb: 1

### 卫视频道
- guovin_ipv4: 91
- zbds_iptv4_txt: 70
- suxuang_ipv4: 23
- guovin_all: 9
- iyouhun_zb: 7
- iptv_org_all: 1

### 地方频道
- zbds_iptv4_txt: 226
- guovin_all: 204
- iyouhun_zb: 183
- epg_cn: 137
- suxuang_ipv4: 22
- guovin_ipv4: 11
- vamoschuck_m3u: 10
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 52
- suxuang_ipv4: 33
- guovin_all: 28
- iyouhun_zb: 25
- guovin_ipv4: 17
- zbds_iptv4_txt: 6
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- mursor_yy: 8
- epg_cn: 6
- guovin_all: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 17
- guovin_ipv4: 7
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 14
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- iyouhun_zb: 36
- guovin_all: 28
- epg_cn: 18
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- mursor_yy: 242
- epg_cn: 155
- iyouhun_zb: 51
- suxuang_ipv4: 41
- guovin_ipv4: 6
- guovin_all: 5
- zbds_iptv4_txt: 3

### 港澳台频道
- iyouhun_zb: 41
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
- free_tv_world: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
