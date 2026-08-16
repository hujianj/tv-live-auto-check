# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2306
Published channel names: 1436
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 441
- Channel limit trimmed rows: 905
- Group limit trimmed rows: 242
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6955
- unstable_or_wrong_alias: 827
- strict_quality_filter: 441
- foreign_channel: 304
- ambiguous_url_identity: 129
- cgtn_url: 22
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 242

## Groups
- 央视频道: 128
- 卫视频道: 193
- 地方频道: 710
- 影视剧场: 145
- 少儿动漫: 20
- 体育纪实: 49
- 音乐综艺: 27
- 生活休闲: 70
- 综合娱乐: 900
- 港澳台频道: 64

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 444 |
| bigbiggrandg_gather | 443 |
| epg_cn | 399 |
| guovin_all | 366 |
| mursor_yy | 273 |
| guovin_ipv4 | 180 |
| suxuang_ipv4 | 146 |
| vamoschuck_m3u | 19 |
| iptv_org_all | 9 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| iyouhun_zb | 1 |
| epg_tw | 1 |
| free_tv_world | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- zbds_iptv4_txt: 53
- guovin_ipv4: 46
- epg_cn: 22
- suxuang_ipv4: 4
- iptv_org_all: 3

### 卫视频道
- guovin_ipv4: 85
- zbds_iptv4_txt: 78
- suxuang_ipv4: 18
- guovin_all: 9
- bigbiggrandg_gather: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 254
- zbds_iptv4_txt: 252
- epg_cn: 144
- suxuang_ipv4: 24
- vamoschuck_m3u: 17
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- guovin_all: 35
- suxuang_ipv4: 32
- mursor_yy: 30
- zbds_iptv4_txt: 24
- guovin_ipv4: 18
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- epg_cn: 7
- guovin_all: 7
- mursor_yy: 4
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 30
- guovin_ipv4: 8
- guovin_all: 5
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 12
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
- guovin_ipv4: 1
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 395
- mursor_yy: 221
- epg_cn: 193
- suxuang_ipv4: 48
- guovin_all: 18
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 4

### 港澳台频道
- suxuang_ipv4: 19
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
