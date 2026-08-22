# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2301
Published channel names: 1442
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 445
- Channel limit trimmed rows: 822
- Group limit trimmed rows: 214
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7486
- unstable_or_wrong_alias: 846
- foreign_channel: 586
- strict_quality_filter: 445
- ambiguous_url_identity: 162
- cgtn_url: 15
- latin_noise_name: 2
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 214

## Groups
- 央视频道: 128
- 卫视频道: 183
- 地方频道: 692
- 影视剧场: 167
- 少儿动漫: 19
- 体育纪实: 49
- 音乐综艺: 26
- 生活休闲: 71
- 综合娱乐: 900
- 港澳台频道: 66

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 455 |
| bigbiggrandg_gather | 441 |
| epg_cn | 403 |
| guovin_all | 360 |
| mursor_yy | 284 |
| guovin_ipv4 | 203 |
| suxuang_ipv4 | 98 |
| vamoschuck_m3u | 20 |
| iptv_org_all | 10 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| epg_hk | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 53
- zbds_iptv4_txt: 39
- epg_cn: 32
- iptv_org_all: 3
- free_tv_world: 1

### 卫视频道
- guovin_ipv4: 102
- zbds_iptv4_txt: 67
- guovin_all: 9
- suxuang_ipv4: 2
- bigbiggrandg_gather: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 253
- zbds_iptv4_txt: 248
- epg_cn: 137
- vamoschuck_m3u: 18
- suxuang_ipv4: 17
- guovin_ipv4: 10
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- zbds_iptv4_txt: 64
- mursor_yy: 33
- guovin_all: 30
- guovin_ipv4: 18
- suxuang_ipv4: 16
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 7
- epg_cn: 6
- mursor_yy: 4
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 30
- guovin_ipv4: 8
- guovin_all: 5
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 11
- mursor_yy: 8
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 23
- bigbiggrandg_gather: 9
- mursor_yy: 4
- iptv_org_all: 2
- suxuang_ipv4: 2
- guovin_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 230
- epg_cn: 195
- suxuang_ipv4: 38
- guovin_all: 18
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 4

### 港澳台频道
- suxuang_ipv4: 23
- bigbiggrandg_gather: 16
- guovin_all: 8
- epg_cn: 7
- suxuang_ipv6: 6
- guovin_ipv4: 2
- mursor_yy: 2
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
