# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2235
Published channel names: 1430
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 438
- Channel limit trimmed rows: 745
- Group limit trimmed rows: 187
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7285
- unstable_or_wrong_alias: 823
- foreign_channel: 510
- strict_quality_filter: 438
- ambiguous_url_identity: 146
- cgtn_url: 15
- latin_noise_name: 2
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 187

## Groups
- 央视频道: 129
- 卫视频道: 186
- 地方频道: 622
- 影视剧场: 168
- 少儿动漫: 20
- 体育纪实: 49
- 音乐综艺: 26
- 生活休闲: 66
- 综合娱乐: 900
- 港澳台频道: 69

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 441 |
| zbds_iptv4_txt | 403 |
| epg_cn | 384 |
| guovin_all | 367 |
| mursor_yy | 295 |
| guovin_ipv4 | 198 |
| suxuang_ipv4 | 102 |
| iptv_org_all | 9 |
| vamoschuck_m3u | 8 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| epg_hk | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 50
- zbds_iptv4_txt: 43
- epg_cn: 32
- iptv_org_all: 3
- free_tv_world: 1

### 卫视频道
- guovin_ipv4: 99
- zbds_iptv4_txt: 70
- guovin_all: 9
- suxuang_ipv4: 4
- bigbiggrandg_gather: 1
- guovin_ipv6: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 258
- zbds_iptv4_txt: 191
- epg_cn: 130
- suxuang_ipv4: 17
- guovin_ipv4: 11
- vamoschuck_m3u: 7
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- zbds_iptv4_txt: 62
- mursor_yy: 35
- guovin_all: 30
- guovin_ipv4: 19
- suxuang_ipv4: 16
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- epg_cn: 7
- mursor_yy: 3
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
- epg_cn: 20
- bigbiggrandg_gather: 8
- mursor_yy: 4
- iptv_org_all: 2
- guovin_ipv4: 1
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 395
- mursor_yy: 239
- epg_cn: 184
- suxuang_ipv4: 40
- guovin_all: 19
- epg_mo: 7
- guovin_ipv4: 5
- zbds_iptv4_txt: 4

### 港澳台频道
- suxuang_ipv4: 24
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
