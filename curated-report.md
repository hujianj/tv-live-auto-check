# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2775
Published channel names: 1697
Stability history URLs loaded: 4757
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 494
- Channel limit trimmed rows: 1802
- Group limit trimmed rows: 165
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6924
- unstable_or_wrong_alias: 798
- strict_quality_filter: 494
- foreign_channel: 410
- ambiguous_url_identity: 274
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 126
- 综合娱乐: 39

## Groups
- 央视频道: 131
- 卫视频道: 199
- 地方频道: 871
- 影视剧场: 161
- 少儿动漫: 25
- 体育纪实: 67
- 音乐综艺: 31
- 生活休闲: 93
- 综合娱乐: 900
- 港澳台频道: 77
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 490 |
| bigbiggrandg_gather | 433 |
| zbds_iptv4_txt | 421 |
| guovin_all | 351 |
| iyouhun_zb | 337 |
| mursor_yy | 294 |
| guovin_ipv4 | 220 |
| suxuang_ipv4 | 153 |
| migu_interface | 32 |
| iptv_org_all | 10 |
| vamoschuck_m3u | 10 |
| suxuang_ipv6 | 6 |
| epg_mo | 6 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 61
- epg_cn: 30
- zbds_iptv4_txt: 19
- suxuang_ipv4: 8
- iptv_org_all: 6
- iyouhun_zb: 6
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 110
- zbds_iptv4_txt: 44
- suxuang_ipv4: 20
- guovin_all: 12
- iyouhun_zb: 8
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- zbds_iptv4_txt: 265
- guovin_all: 239
- iyouhun_zb: 161
- epg_cn: 146
- suxuang_ipv4: 24
- guovin_ipv4: 11
- migu_interface: 10
- vamoschuck_m3u: 9

### 影视剧场
- mursor_yy: 37
- guovin_all: 33
- suxuang_ipv4: 27
- iyouhun_zb: 21
- zbds_iptv4_txt: 21
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 9
- guovin_all: 8
- mursor_yy: 6
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 19
- guovin_ipv4: 10
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 12
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- epg_cn: 1
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 33
- guovin_all: 26
- epg_cn: 21
- bigbiggrandg_gather: 8
- guovin_ipv4: 3
- iptv_org_all: 1
- mursor_yy: 1

### 综合娱乐
- bigbiggrandg_gather: 392
- epg_cn: 260
- iyouhun_zb: 69
- suxuang_ipv4: 66
- zbds_iptv4_txt: 40
- guovin_all: 24
- migu_interface: 18
- mursor_yy: 15

### 港澳台频道
- epg_cn: 20
- iyouhun_zb: 17
- bigbiggrandg_gather: 13
- suxuang_ipv4: 8
- guovin_all: 7
- suxuang_ipv6: 5
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
