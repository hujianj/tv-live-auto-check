# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2155
Published channel names: 1352
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 450
- Channel limit trimmed rows: 736
- Group limit trimmed rows: 203
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7378
- unstable_or_wrong_alias: 823
- foreign_channel: 591
- strict_quality_filter: 450
- ambiguous_url_identity: 140
- cgtn_url: 22
- latin_noise_name: 2
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 203

## Groups
- 央视频道: 129
- 卫视频道: 175
- 地方频道: 644
- 影视剧场: 105
- 少儿动漫: 18
- 体育纪实: 27
- 音乐综艺: 26
- 生活休闲: 66
- 综合娱乐: 900
- 港澳台频道: 65

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 441 |
| epg_cn | 383 |
| guovin_all | 366 |
| mursor_yy | 293 |
| zbds_iptv4_txt | 290 |
| guovin_ipv4 | 225 |
| suxuang_ipv4 | 101 |
| vamoschuck_m3u | 20 |
| iptv_org_all | 9 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 59
- zbds_iptv4_txt: 38
- epg_cn: 28
- iptv_org_all: 3
- free_tv_world: 1

### 卫视频道
- guovin_ipv4: 115
- zbds_iptv4_txt: 43
- guovin_all: 9
- suxuang_ipv4: 4
- bigbiggrandg_gather: 1
- guovin_ipv6: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 257
- zbds_iptv4_txt: 189
- epg_cn: 136
- suxuang_ipv4: 23
- vamoschuck_m3u: 18
- guovin_ipv4: 13
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- guovin_all: 33
- mursor_yy: 32
- guovin_ipv4: 18
- suxuang_ipv4: 11
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- epg_cn: 5
- mursor_yy: 4
- zbds_iptv4_txt: 1

### 体育纪实
- guovin_ipv4: 8
- zbds_iptv4_txt: 8
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
- epg_cn: 19
- bigbiggrandg_gather: 9
- mursor_yy: 4
- iptv_org_all: 2
- guovin_ipv4: 1
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 239
- epg_cn: 186
- suxuang_ipv4: 40
- guovin_all: 16
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 5

### 港澳台频道
- suxuang_ipv4: 22
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
