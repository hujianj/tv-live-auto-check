# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2278
Published channel names: 1445
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 436
- Channel limit trimmed rows: 746
- Group limit trimmed rows: 157
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7223
- unstable_or_wrong_alias: 821
- foreign_channel: 471
- strict_quality_filter: 436
- ambiguous_url_identity: 162
- cgtn_url: 15
- latin_noise_name: 2
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 157

## Groups
- 央视频道: 128
- 卫视频道: 182
- 地方频道: 683
- 影视剧场: 170
- 少儿动漫: 21
- 体育纪实: 49
- 音乐综艺: 27
- 生活休闲: 63
- 综合娱乐: 900
- 港澳台频道: 55

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 446 |
| bigbiggrandg_gather | 408 |
| guovin_all | 366 |
| epg_cn | 364 |
| mursor_yy | 322 |
| guovin_ipv4 | 211 |
| suxuang_ipv4 | 103 |
| vamoschuck_m3u | 20 |
| iptv_org_all | 9 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 4 |
| kimentanm_aptv | 3 |
| free_tv_world | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| iyouhun_zb | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 56
- zbds_iptv4_txt: 39
- epg_cn: 29
- iptv_org_all: 3
- free_tv_world: 1

### 卫视频道
- guovin_ipv4: 105
- zbds_iptv4_txt: 60
- guovin_all: 9
- suxuang_ipv4: 3
- guovin_ipv6: 2
- bigbiggrandg_gather: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 257
- zbds_iptv4_txt: 245
- epg_cn: 126
- suxuang_ipv4: 18
- vamoschuck_m3u: 18
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- zbds_iptv4_txt: 64
- mursor_yy: 35
- guovin_all: 30
- guovin_ipv4: 19
- suxuang_ipv4: 16
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- epg_cn: 7
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
- mursor_yy: 9
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 16
- bigbiggrandg_gather: 9
- mursor_yy: 4
- iptv_org_all: 2
- guovin_ipv4: 1
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 373
- mursor_yy: 265
- epg_cn: 174
- suxuang_ipv4: 44
- guovin_all: 19
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 5

### 港澳台频道
- suxuang_ipv4: 21
- epg_cn: 9
- guovin_all: 8
- suxuang_ipv6: 6
- bigbiggrandg_gather: 4
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
