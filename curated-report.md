# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2599
Published channel names: 1634
Stability history URLs loaded: 4986
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 464
- Channel limit trimmed rows: 1324
- Group limit trimmed rows: 191
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6855
- unstable_or_wrong_alias: 810
- strict_quality_filter: 464
- foreign_channel: 324
- ambiguous_url_identity: 215
- cgtn_url: 25
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 182
- 港澳台频道: 9

## Groups
- 央视频道: 125
- 卫视频道: 184
- 地方频道: 719
- 影视剧场: 167
- 少儿动漫: 21
- 体育纪实: 68
- 音乐综艺: 33
- 生活休闲: 103
- 综合娱乐: 869
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| iyouhun_zb | 395 |
| guovin_all | 360 |
| epg_cn | 353 |
| mursor_yy | 318 |
| zbds_iptv4_txt | 257 |
| guovin_ipv4 | 230 |
| suxuang_ipv4 | 160 |
| migu_interface | 34 |
| epg_tw | 16 |
| iptv_org_all | 9 |
| vamoschuck_m3u | 9 |
| epg_mo | 7 |
| epg_hk | 4 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 2 |
| epg_my | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 62
- epg_cn: 28
- zbds_iptv4_txt: 20
- iyouhun_zb: 6
- iptv_org_all: 5
- suxuang_ipv4: 3
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 116
- zbds_iptv4_txt: 32
- guovin_all: 12
- suxuang_ipv4: 12
- iyouhun_zb: 8
- guovin_ipv6: 3
- migu_interface: 1

### 地方频道
- guovin_all: 247
- zbds_iptv4_txt: 167
- iyouhun_zb: 153
- epg_cn: 94
- suxuang_ipv4: 24
- guovin_ipv4: 11
- migu_interface: 10
- vamoschuck_m3u: 7

### 影视剧场
- mursor_yy: 52
- guovin_all: 33
- suxuang_ipv4: 31
- iyouhun_zb: 24
- guovin_ipv4: 15
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 4
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 7
- epg_cn: 4
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 19
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 14
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 38
- guovin_all: 27
- epg_cn: 18
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 394
- epg_cn: 203
- iyouhun_zb: 98
- suxuang_ipv4: 76
- guovin_all: 24
- migu_interface: 20
- mursor_yy: 17
- epg_tw: 15

### 港澳台频道
- iyouhun_zb: 46
- bigbiggrandg_gather: 13
- suxuang_ipv4: 13
- guovin_all: 7
- epg_cn: 3
- guovin_ipv4: 3
- suxuang_ipv6: 2
- epg_tw: 1

### 海外华语频道
- mursor_yy: 217
- iptv_org_all: 2
- iptv_org_tw: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
