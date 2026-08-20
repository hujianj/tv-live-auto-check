# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2264
Published channel names: 1433
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 452
- Channel limit trimmed rows: 790
- Group limit trimmed rows: 187
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7334
- unstable_or_wrong_alias: 835
- foreign_channel: 591
- strict_quality_filter: 452
- ambiguous_url_identity: 162
- cgtn_url: 15
- invalid_name_or_url: 3
- latin_noise_name: 2

### Group limit trims

- 综合娱乐: 187

## Groups
- 央视频道: 128
- 卫视频道: 182
- 地方频道: 692
- 影视剧场: 145
- 少儿动漫: 16
- 体育纪实: 49
- 音乐综艺: 26
- 生活休闲: 61
- 综合娱乐: 900
- 港澳台频道: 65

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 441 |
| bigbiggrandg_gather | 440 |
| guovin_all | 360 |
| epg_cn | 350 |
| mursor_yy | 292 |
| guovin_ipv4 | 189 |
| suxuang_ipv4 | 138 |
| vamoschuck_m3u | 20 |
| iptv_org_all | 9 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 65
- guovin_ipv4: 38
- epg_cn: 22
- iptv_org_all: 2
- free_tv_world: 1

### 卫视频道
- guovin_ipv4: 101
- zbds_iptv4_txt: 65
- guovin_all: 9
- suxuang_ipv4: 3
- bigbiggrandg_gather: 1
- guovin_ipv6: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 254
- zbds_iptv4_txt: 254
- epg_cn: 130
- vamoschuck_m3u: 18
- suxuang_ipv4: 17
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- suxuang_ipv4: 37
- mursor_yy: 31
- guovin_all: 30
- zbds_iptv4_txt: 22
- guovin_ipv4: 19
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 9
- epg_cn: 4
- mursor_yy: 3

### 体育纪实
- zbds_iptv4_txt: 30
- guovin_ipv4: 8
- guovin_all: 5
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 10
- mursor_yy: 9
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 13
- bigbiggrandg_gather: 9
- mursor_yy: 3
- suxuang_ipv4: 3
- iptv_org_all: 2
- guovin_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- mursor_yy: 240
- epg_cn: 172
- suxuang_ipv4: 55
- guovin_all: 15
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 4

### 港澳台频道
- suxuang_ipv4: 23
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
