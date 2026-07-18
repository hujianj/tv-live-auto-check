# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2704
Published channel names: 1653
Stability history URLs loaded: 4048
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 492
- Channel limit trimmed rows: 1736
- Group limit trimmed rows: 131
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7018
- unstable_or_wrong_alias: 814
- strict_quality_filter: 492
- foreign_channel: 419
- ambiguous_url_identity: 262
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 131

## Groups
- 央视频道: 131
- 卫视频道: 197
- 地方频道: 863
- 影视剧场: 147
- 少儿动漫: 28
- 体育纪实: 66
- 音乐综艺: 29
- 生活休闲: 95
- 综合娱乐: 855
- 港澳台频道: 73
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 498 |
| zbds_iptv4_txt | 440 |
| bigbiggrandg_gather | 385 |
| iyouhun_zb | 354 |
| guovin_all | 342 |
| mursor_yy | 310 |
| guovin_ipv4 | 223 |
| suxuang_ipv4 | 77 |
| migu_interface | 32 |
| iptv_org_all | 11 |
| vamoschuck_m3u | 9 |
| epg_mo | 6 |
| suxuang_ipv6 | 5 |
| epg_tw | 4 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 64
- epg_cn: 29
- zbds_iptv4_txt: 20
- iyouhun_zb: 8
- iptv_org_all: 6
- suxuang_ipv4: 3
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 108
- zbds_iptv4_txt: 52
- suxuang_ipv4: 14
- guovin_all: 12
- iyouhun_zb: 7
- guovin_ipv6: 2
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- zbds_iptv4_txt: 262
- guovin_all: 239
- iyouhun_zb: 166
- epg_cn: 141
- suxuang_ipv4: 20
- guovin_ipv4: 12
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 50
- guovin_all: 28
- zbds_iptv4_txt: 24
- iyouhun_zb: 22
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2
- suxuang_ipv4: 1

### 少儿动漫
- epg_cn: 11
- guovin_all: 8
- mursor_yy: 7
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 18
- guovin_ipv4: 10
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 12
- bigbiggrandg_gather: 8
- guovin_ipv4: 3
- kimentanm_aptv: 3
- epg_cn: 1
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 33
- guovin_all: 26
- epg_cn: 20
- bigbiggrandg_gather: 7
- mursor_yy: 4
- guovin_ipv4: 3
- iptv_org_all: 2

### 综合娱乐
- bigbiggrandg_gather: 347
- epg_cn: 273
- iyouhun_zb: 80
- zbds_iptv4_txt: 50
- suxuang_ipv4: 33
- guovin_all: 20
- migu_interface: 19
- mursor_yy: 15

### 港澳台频道
- epg_cn: 20
- iyouhun_zb: 17
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 6
- suxuang_ipv6: 4
- guovin_ipv4: 2
- mursor_yy: 2

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
