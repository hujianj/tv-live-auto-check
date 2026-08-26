# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2315
Published channel names: 1557
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 431
- Channel limit trimmed rows: 607
- Group limit trimmed rows: 573
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7174
- unstable_or_wrong_alias: 842
- strict_quality_filter: 431
- foreign_channel: 422
- ambiguous_url_identity: 150
- latin_noise_name: 65
- cgtn_url: 15

### Group limit trims

- 综合娱乐: 487
- 影视剧场: 86

## Groups
- 央视频道: 129
- 卫视频道: 165
- 地方频道: 687
- 影视剧场: 180
- 少儿动漫: 31
- 体育纪实: 57
- 音乐综艺: 28
- 生活休闲: 72
- 综合娱乐: 900
- 港澳台频道: 66

## Final published lines by source

| Source | Lines |
|---|---:|
| freetv_douyu | 470 |
| bigbiggrandg_gather | 440 |
| zbds_iptv4_txt | 424 |
| epg_cn | 336 |
| guovin_all | 324 |
| guovin_ipv4 | 191 |
| suxuang_ipv4 | 87 |
| vamoschuck_m3u | 19 |
| suxuang_ipv6 | 7 |
| iptv_org_all | 5 |
| kimentanm_aptv | 3 |
| free_tv_world | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| guovin_ipv6 | 1 |
| iyouhun_zb | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 51
- epg_cn: 37
- zbds_iptv4_txt: 37
- iptv_org_all: 2
- free_tv_world: 1
- suxuang_ipv4: 1

### 卫视频道
- guovin_ipv4: 88
- zbds_iptv4_txt: 62
- guovin_all: 9
- suxuang_ipv4: 4
- bigbiggrandg_gather: 1
- suxuang_ipv6: 1

### 地方频道
- zbds_iptv4_txt: 250
- guovin_all: 246
- epg_cn: 130
- guovin_ipv4: 18
- suxuang_ipv4: 16
- vamoschuck_m3u: 16
- bigbiggrandg_gather: 5
- freetv_douyu: 4

### 影视剧场
- freetv_douyu: 97
- zbds_iptv4_txt: 43
- suxuang_ipv4: 12
- guovin_all: 11
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- freetv_douyu: 17
- guovin_all: 8
- epg_cn: 4
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 26
- freetv_douyu: 11
- guovin_ipv4: 9
- guovin_all: 8
- epg_cn: 3

### 音乐综艺
- bigbiggrandg_gather: 11
- freetv_douyu: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 31
- epg_cn: 17
- bigbiggrandg_gather: 9
- freetv_douyu: 7
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 2
- vamoschuck_m3u: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- freetv_douyu: 324
- epg_cn: 137
- suxuang_ipv4: 28
- guovin_ipv4: 6
- guovin_all: 4
- zbds_iptv4_txt: 3
- yang_gather: 2

### 港澳台频道
- suxuang_ipv4: 24
- bigbiggrandg_gather: 16
- epg_cn: 8
- guovin_all: 7
- suxuang_ipv6: 6
- guovin_ipv4: 2
- epg_hk: 1
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
