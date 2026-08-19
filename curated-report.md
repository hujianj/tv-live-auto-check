# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2310
Published channel names: 1448
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 452
- Channel limit trimmed rows: 819
- Group limit trimmed rows: 176
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7399
- unstable_or_wrong_alias: 828
- foreign_channel: 598
- strict_quality_filter: 452
- ambiguous_url_identity: 162
- cgtn_url: 15
- latin_noise_name: 2
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 176

## Groups
- 央视频道: 129
- 卫视频道: 186
- 地方频道: 696
- 影视剧场: 169
- 少儿动漫: 19
- 体育纪实: 48
- 音乐综艺: 25
- 生活休闲: 71
- 综合娱乐: 900
- 港澳台频道: 67

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 457 |
| bigbiggrandg_gather | 401 |
| epg_cn | 397 |
| guovin_all | 362 |
| mursor_yy | 313 |
| guovin_ipv4 | 214 |
| suxuang_ipv4 | 112 |
| vamoschuck_m3u | 20 |
| iptv_org_all | 8 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |
| iptv_org_tw | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 55
- zbds_iptv4_txt: 45
- epg_cn: 26
- iptv_org_all: 2
- free_tv_world: 1

### 卫视频道
- guovin_ipv4: 107
- zbds_iptv4_txt: 63
- guovin_all: 9
- suxuang_ipv4: 3
- bigbiggrandg_gather: 1
- guovin_ipv6: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 250
- zbds_iptv4_txt: 248
- epg_cn: 138
- suxuang_ipv4: 22
- vamoschuck_m3u: 18
- guovin_ipv4: 12
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- zbds_iptv4_txt: 64
- mursor_yy: 34
- guovin_all: 30
- guovin_ipv4: 19
- suxuang_ipv4: 16
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 9
- epg_cn: 6
- mursor_yy: 3
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- guovin_ipv4: 7
- guovin_all: 5
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 10
- mursor_yy: 8
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 23
- bigbiggrandg_gather: 9
- mursor_yy: 4
- guovin_ipv4: 2
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 355
- mursor_yy: 258
- epg_cn: 194
- suxuang_ipv4: 47
- guovin_all: 21
- epg_mo: 7
- guovin_ipv4: 7
- zbds_iptv4_txt: 5

### 港澳台频道
- suxuang_ipv4: 23
- bigbiggrandg_gather: 16
- guovin_all: 8
- epg_cn: 7
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
