# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2680
Published channel names: 1650
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 464
- Channel limit trimmed rows: 1577
- Group limit trimmed rows: 193
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7020
- unstable_or_wrong_alias: 811
- strict_quality_filter: 464
- foreign_channel: 370
- ambiguous_url_identity: 236
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 183
- 港澳台频道: 6
- 影视剧场: 4

## Groups
- 央视频道: 131
- 卫视频道: 200
- 地方频道: 756
- 影视剧场: 180
- 少儿动漫: 26
- 体育纪实: 64
- 音乐综艺: 34
- 生活休闲: 104
- 综合娱乐: 875
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 435 |
| epg_cn | 415 |
| iyouhun_zb | 378 |
| guovin_all | 360 |
| mursor_yy | 320 |
| zbds_iptv4_txt | 317 |
| guovin_ipv4 | 210 |
| suxuang_ipv4 | 170 |
| migu_interface | 38 |
| vamoschuck_m3u | 10 |
| iptv_org_all | 9 |
| epg_mo | 7 |
| epg_tw | 3 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 57
- zbds_iptv4_txt: 27
- epg_cn: 25
- suxuang_ipv4: 8
- iptv_org_all: 6
- iyouhun_zb: 4
- migu_interface: 4

### 卫视频道
- guovin_ipv4: 103
- zbds_iptv4_txt: 56
- suxuang_ipv4: 18
- guovin_all: 12
- iyouhun_zb: 7
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 245
- zbds_iptv4_txt: 177
- iyouhun_zb: 145
- epg_cn: 131
- suxuang_ipv4: 22
- guovin_ipv4: 12
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 50
- guovin_all: 34
- suxuang_ipv4: 31
- iyouhun_zb: 22
- zbds_iptv4_txt: 22
- guovin_ipv4: 13
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- epg_cn: 7
- mursor_yy: 7
- iyouhun_zb: 2
- epg_tw: 1
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 11
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 42
- guovin_all: 27
- epg_cn: 14
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 2

### 综合娱乐
- bigbiggrandg_gather: 393
- epg_cn: 231
- iyouhun_zb: 93
- suxuang_ipv4: 75
- guovin_all: 25
- migu_interface: 21
- mursor_yy: 19
- epg_mo: 7

### 港澳台频道
- iyouhun_zb: 46
- suxuang_ipv4: 14
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
