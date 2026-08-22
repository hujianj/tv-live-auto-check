# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2340
Published channel names: 1571
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 448
- Channel limit trimmed rows: 743
- Group limit trimmed rows: 908
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7424
- unstable_or_wrong_alias: 838
- foreign_channel: 594
- strict_quality_filter: 448
- ambiguous_url_identity: 164
- latin_noise_name: 64
- cgtn_url: 15
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 783
- 影视剧场: 125

## Groups
- 央视频道: 128
- 卫视频道: 181
- 地方频道: 680
- 影视剧场: 180
- 少儿动漫: 38
- 体育纪实: 59
- 音乐综艺: 36
- 生活休闲: 69
- 综合娱乐: 900
- 港澳台频道: 69

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 419 |
| zbds_iptv4_txt | 412 |
| freetv_douyu | 389 |
| guovin_all | 339 |
| epg_cn | 297 |
| guovin_ipv4 | 198 |
| mursor_yy | 166 |
| suxuang_ipv4 | 73 |
| vamoschuck_m3u | 18 |
| iptv_org_all | 7 |
| suxuang_ipv6 | 7 |
| guovin_ipv6 | 4 |
| kimentanm_aptv | 3 |
| free_tv_world | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| iyouhun_zb | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 55
- zbds_iptv4_txt: 38
- epg_cn: 30
- iptv_org_all: 3
- free_tv_world: 1
- suxuang_ipv4: 1

### 卫视频道
- guovin_ipv4: 101
- zbds_iptv4_txt: 63
- guovin_all: 9
- suxuang_ipv4: 3
- guovin_ipv6: 2
- bigbiggrandg_gather: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 255
- zbds_iptv4_txt: 242
- epg_cn: 125
- suxuang_ipv4: 17
- vamoschuck_m3u: 17
- guovin_ipv4: 12
- bigbiggrandg_gather: 5
- freetv_douyu: 4

### 影视剧场
- freetv_douyu: 84
- zbds_iptv4_txt: 35
- mursor_yy: 19
- guovin_all: 17
- guovin_ipv4: 10
- suxuang_ipv4: 9
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- freetv_douyu: 18
- guovin_all: 9
- epg_cn: 6
- mursor_yy: 4
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- freetv_douyu: 10
- guovin_ipv4: 8
- guovin_all: 5
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 10
- freetv_douyu: 10
- mursor_yy: 9
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 15
- bigbiggrandg_gather: 9
- freetv_douyu: 7
- mursor_yy: 4
- iptv_org_all: 2
- guovin_ipv4: 1
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 373
- freetv_douyu: 256
- mursor_yy: 124
- epg_cn: 110
- suxuang_ipv4: 19
- guovin_all: 6
- guovin_ipv4: 6
- yang_gather: 2

### 港澳台频道
- suxuang_ipv4: 23
- bigbiggrandg_gather: 16
- epg_cn: 8
- guovin_all: 8
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
