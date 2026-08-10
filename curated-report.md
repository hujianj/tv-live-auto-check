# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2435
Published channel names: 1477
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 467
- Channel limit trimmed rows: 1609
- Group limit trimmed rows: 393
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7000
- unstable_or_wrong_alias: 819
- strict_quality_filter: 467
- foreign_channel: 367
- ambiguous_url_identity: 222
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 综合娱乐: 376
- 港澳台频道: 17

## Groups
- 央视频道: 127
- 卫视频道: 195
- 地方频道: 721
- 影视剧场: 180
- 少儿动漫: 24
- 体育纪实: 67
- 音乐综艺: 34
- 生活休闲: 97
- 综合娱乐: 900
- 港澳台频道: 90

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 434 |
| zbds_iptv4_txt | 361 |
| iyouhun_zb | 344 |
| epg_cn | 332 |
| mursor_yy | 327 |
| guovin_all | 299 |
| guovin_ipv4 | 175 |
| suxuang_ipv4 | 132 |
| vamoschuck_m3u | 13 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |
| free_tv_world | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 73
- guovin_ipv4: 29
- epg_cn: 23
- iptv_org_all: 1
- suxuang_ipv4: 1

### 卫视频道
- guovin_ipv4: 96
- zbds_iptv4_txt: 65
- suxuang_ipv4: 18
- guovin_all: 9
- iyouhun_zb: 6
- iptv_org_all: 1

### 地方频道
- guovin_all: 208
- iyouhun_zb: 169
- zbds_iptv4_txt: 163
- epg_cn: 130
- suxuang_ipv4: 23
- guovin_ipv4: 13
- vamoschuck_m3u: 9
- bigbiggrandg_gather: 5

### 影视剧场
- mursor_yy: 51
- suxuang_ipv4: 30
- guovin_all: 29
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 18
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 6
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 33
- iyouhun_zb: 17
- guovin_ipv4: 8
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2

### 生活休闲
- iyouhun_zb: 37
- guovin_all: 29
- epg_cn: 13
- bigbiggrandg_gather: 8
- mursor_yy: 5
- iptv_org_all: 2
- vamoschuck_m3u: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 392
- mursor_yy: 242
- epg_cn: 148
- iyouhun_zb: 50
- suxuang_ipv4: 43
- guovin_all: 7
- guovin_ipv4: 6
- epg_tw: 3

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 9
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
