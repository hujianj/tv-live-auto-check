# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2444
Published channel names: 1501
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 466
- Channel limit trimmed rows: 1740
- Group limit trimmed rows: 401
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6966
- unstable_or_wrong_alias: 817
- strict_quality_filter: 466
- foreign_channel: 305
- ambiguous_url_identity: 173
- cgtn_url: 22
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 385
- 港澳台频道: 16

## Groups
- 央视频道: 129
- 卫视频道: 205
- 地方频道: 732
- 影视剧场: 175
- 少儿动漫: 25
- 体育纪实: 67
- 音乐综艺: 32
- 生活休闲: 89
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 435 |
| zbds_iptv4_txt | 364 |
| epg_cn | 346 |
| mursor_yy | 338 |
| iyouhun_zb | 319 |
| guovin_all | 301 |
| guovin_ipv4 | 181 |
| suxuang_ipv4 | 136 |
| vamoschuck_m3u | 8 |
| iptv_org_all | 7 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 50
- guovin_ipv4: 49
- epg_cn: 22
- suxuang_ipv4: 5
- iptv_org_all: 2
- iyouhun_zb: 1

### 卫视频道
- zbds_iptv4_txt: 95
- guovin_ipv4: 82
- suxuang_ipv4: 14
- guovin_all: 9
- iyouhun_zb: 4
- iptv_org_all: 1

### 地方频道
- guovin_all: 216
- zbds_iptv4_txt: 175
- iyouhun_zb: 157
- epg_cn: 137
- suxuang_ipv4: 23
- guovin_ipv4: 12
- vamoschuck_m3u: 7
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 58
- suxuang_ipv4: 35
- guovin_all: 28
- iyouhun_zb: 25
- guovin_ipv4: 19
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 4
- vamoschuck_m3u: 1

### 少儿动漫
- mursor_yy: 8
- epg_cn: 5
- guovin_all: 5
- zbds_iptv4_txt: 5
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 31
- iyouhun_zb: 19
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 29
- iyouhun_zb: 25
- epg_cn: 19
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 247
- epg_cn: 152
- iyouhun_zb: 45
- suxuang_ipv4: 43
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
