# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2734
Published channel names: 1675
Stability history URLs loaded: 4846
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 490
- Channel limit trimmed rows: 1672
- Group limit trimmed rows: 119
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6928
- unstable_or_wrong_alias: 821
- strict_quality_filter: 490
- foreign_channel: 415
- ambiguous_url_identity: 274
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 119

## Groups
- 央视频道: 134
- 卫视频道: 201
- 地方频道: 855
- 影视剧场: 171
- 少儿动漫: 27
- 体育纪实: 62
- 音乐综艺: 31
- 生活休闲: 99
- 综合娱乐: 862
- 港澳台频道: 72
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 467 |
| zbds_iptv4_txt | 423 |
| bigbiggrandg_gather | 380 |
| guovin_all | 353 |
| iyouhun_zb | 342 |
| mursor_yy | 314 |
| guovin_ipv4 | 210 |
| suxuang_ipv4 | 167 |
| migu_interface | 37 |
| iptv_org_all | 11 |
| vamoschuck_m3u | 9 |
| suxuang_ipv6 | 6 |
| epg_mo | 6 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| guovin_ipv6 | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 59
- epg_cn: 26
- zbds_iptv4_txt: 19
- suxuang_ipv4: 13
- iptv_org_all: 6
- iyouhun_zb: 6
- migu_interface: 5

### 卫视频道
- guovin_ipv4: 100
- zbds_iptv4_txt: 51
- suxuang_ipv4: 25
- guovin_all: 12
- iyouhun_zb: 8
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- zbds_iptv4_txt: 253
- guovin_all: 243
- iyouhun_zb: 158
- epg_cn: 144
- suxuang_ipv4: 23
- guovin_ipv4: 12
- migu_interface: 8
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 46
- guovin_all: 32
- suxuang_ipv4: 30
- iyouhun_zb: 22
- zbds_iptv4_txt: 19
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 10
- guovin_all: 7
- mursor_yy: 7
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
- mursor_yy: 4
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 8
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 33
- guovin_all: 26
- epg_cn: 22
- bigbiggrandg_gather: 7
- guovin_ipv4: 3
- mursor_yy: 3
- iptv_org_all: 2
- migu_interface: 2

### 综合娱乐
- bigbiggrandg_gather: 342
- epg_cn: 247
- iyouhun_zb: 79
- suxuang_ipv4: 69
- zbds_iptv4_txt: 48
- guovin_all: 24
- migu_interface: 19
- mursor_yy: 19

### 港澳台频道
- epg_cn: 18
- iyouhun_zb: 17
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 6
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
