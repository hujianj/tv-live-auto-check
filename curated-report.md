# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2761
Published channel names: 1664
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 475
- Channel limit trimmed rows: 1691
- Group limit trimmed rows: 191
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7037
- unstable_or_wrong_alias: 810
- strict_quality_filter: 475
- foreign_channel: 369
- ambiguous_url_identity: 272
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 186
- 港澳台频道: 5

## Groups
- 央视频道: 131
- 卫视频道: 197
- 地方频道: 826
- 影视剧场: 174
- 少儿动漫: 26
- 体育纪实: 65
- 音乐综艺: 32
- 生活休闲: 102
- 综合娱乐: 898
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 476 |
| bigbiggrandg_gather | 435 |
| iyouhun_zb | 377 |
| guovin_all | 354 |
| zbds_iptv4_txt | 352 |
| mursor_yy | 311 |
| guovin_ipv4 | 217 |
| suxuang_ipv4 | 168 |
| migu_interface | 35 |
| vamoschuck_m3u | 9 |
| iptv_org_all | 8 |
| epg_mo | 7 |
| epg_tw | 3 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| suxuang_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 54
- zbds_iptv4_txt: 31
- epg_cn: 28
- suxuang_ipv4: 8
- iptv_org_all: 5
- iyouhun_zb: 3
- migu_interface: 2

### 卫视频道
- guovin_ipv4: 111
- zbds_iptv4_txt: 42
- suxuang_ipv4: 23
- guovin_all: 12
- iyouhun_zb: 6
- guovin_ipv6: 2
- iptv_org_all: 1

### 地方频道
- guovin_all: 242
- zbds_iptv4_txt: 221
- iyouhun_zb: 161
- epg_cn: 142
- suxuang_ipv4: 23
- guovin_ipv4: 13
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 47
- guovin_all: 35
- suxuang_ipv4: 25
- iyouhun_zb: 23
- zbds_iptv4_txt: 22
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 8
- guovin_all: 7
- mursor_yy: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 2
- epg_tw: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 36
- guovin_all: 26
- epg_cn: 21
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- epg_cn: 270
- iyouhun_zb: 85
- suxuang_ipv4: 73
- guovin_all: 23
- migu_interface: 21
- mursor_yy: 15
- epg_mo: 7

### 港澳台频道
- iyouhun_zb: 44
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- guovin_all: 7
- epg_cn: 4
- guovin_ipv4: 2
- suxuang_ipv6: 2
- epg_tw: 1

### 海外华语频道
- mursor_yy: 219
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
