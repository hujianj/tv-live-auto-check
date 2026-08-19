# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2247
Published channel names: 1427
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 454
- Channel limit trimmed rows: 734
- Group limit trimmed rows: 201
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7306
- unstable_or_wrong_alias: 834
- foreign_channel: 585
- strict_quality_filter: 454
- ambiguous_url_identity: 160
- cgtn_url: 15
- invalid_name_or_url: 3
- latin_noise_name: 2

### Group limit trims

- 综合娱乐: 201

## Groups
- 央视频道: 128
- 卫视频道: 183
- 地方频道: 672
- 影视剧场: 147
- 少儿动漫: 13
- 体育纪实: 48
- 音乐综艺: 27
- 生活休闲: 63
- 综合娱乐: 900
- 港澳台频道: 66

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 442 |
| zbds_iptv4_txt | 429 |
| guovin_all | 356 |
| epg_cn | 348 |
| mursor_yy | 289 |
| guovin_ipv4 | 183 |
| suxuang_ipv4 | 145 |
| vamoschuck_m3u | 19 |
| iptv_org_all | 8 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| epg_hk | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 70
- guovin_ipv4: 32
- epg_cn: 24
- free_tv_world: 1
- iptv_org_all: 1

### 卫视频道
- guovin_ipv4: 102
- zbds_iptv4_txt: 65
- guovin_all: 9
- suxuang_ipv4: 3
- bigbiggrandg_gather: 1
- guovin_ipv6: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 248
- zbds_iptv4_txt: 237
- epg_cn: 129
- suxuang_ipv4: 22
- vamoschuck_m3u: 17
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- suxuang_ipv4: 38
- mursor_yy: 33
- guovin_all: 29
- zbds_iptv4_txt: 22
- guovin_ipv4: 19
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 9
- mursor_yy: 3
- epg_cn: 1

### 体育纪实
- zbds_iptv4_txt: 30
- guovin_ipv4: 7
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
- mursor_yy: 3
- iptv_org_all: 2
- suxuang_ipv4: 2
- guovin_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 395
- mursor_yy: 235
- epg_cn: 169
- suxuang_ipv4: 58
- guovin_all: 18
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 4

### 港澳台频道
- suxuang_ipv4: 22
- bigbiggrandg_gather: 16
- guovin_all: 8
- epg_cn: 6
- suxuang_ipv6: 6
- mursor_yy: 3
- epg_hk: 2
- guovin_ipv4: 2


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
