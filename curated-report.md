# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2651
Published channel names: 1632
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 466
- Channel limit trimmed rows: 1507
- Group limit trimmed rows: 203
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6990
- unstable_or_wrong_alias: 821
- strict_quality_filter: 466
- foreign_channel: 370
- ambiguous_url_identity: 231
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 187
- 港澳台频道: 16

## Groups
- 央视频道: 127
- 卫视频道: 197
- 地方频道: 775
- 影视剧场: 167
- 少儿动漫: 24
- 体育纪实: 68
- 音乐综艺: 33
- 生活休闲: 82
- 综合娱乐: 868
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 433 |
| epg_cn | 411 |
| iyouhun_zb | 350 |
| mursor_yy | 319 |
| zbds_iptv4_txt | 318 |
| guovin_all | 318 |
| guovin_ipv4 | 234 |
| suxuang_ipv4 | 176 |
| migu_interface | 41 |
| epg_tw | 15 |
| iptv_org_all | 11 |
| vamoschuck_m3u | 8 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| epg_hk | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 59
- epg_cn: 25
- zbds_iptv4_txt: 18
- suxuang_ipv4: 10
- iptv_org_all: 6
- migu_interface: 6
- iyouhun_zb: 3

### 卫视频道
- guovin_ipv4: 120
- zbds_iptv4_txt: 43
- suxuang_ipv4: 17
- guovin_all: 9
- iyouhun_zb: 6
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- zbds_iptv4_txt: 217
- guovin_all: 213
- iyouhun_zb: 152
- epg_cn: 132
- suxuang_ipv4: 24
- guovin_ipv4: 13
- migu_interface: 11
- vamoschuck_m3u: 7

### 影视剧场
- mursor_yy: 52
- suxuang_ipv4: 30
- guovin_all: 29
- iyouhun_zb: 26
- guovin_ipv4: 17
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 7
- epg_cn: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

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
- guovin_all: 27
- iyouhun_zb: 23
- epg_cn: 13
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- epg_cn: 223
- iyouhun_zb: 78
- suxuang_ipv4: 78
- guovin_all: 23
- migu_interface: 21
- mursor_yy: 18
- epg_tw: 14

### 港澳台频道
- iyouhun_zb: 40
- suxuang_ipv4: 16
- bigbiggrandg_gather: 11
- epg_cn: 9
- guovin_all: 7
- guovin_ipv4: 2
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
