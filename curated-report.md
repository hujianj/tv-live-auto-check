# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2751
Published channel names: 1692
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 466
- Channel limit trimmed rows: 1578
- Group limit trimmed rows: 212
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7005
- unstable_or_wrong_alias: 836
- strict_quality_filter: 466
- foreign_channel: 374
- ambiguous_url_identity: 278
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 189
- 港澳台频道: 17
- 影视剧场: 6

## Groups
- 央视频道: 128
- 卫视频道: 199
- 地方频道: 806
- 影视剧场: 180
- 少儿动漫: 25
- 体育纪实: 68
- 音乐综艺: 32
- 生活休闲: 104
- 综合娱乐: 899
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 437 |
| epg_cn | 431 |
| iyouhun_zb | 374 |
| guovin_all | 355 |
| zbds_iptv4_txt | 341 |
| mursor_yy | 321 |
| guovin_ipv4 | 218 |
| suxuang_ipv4 | 184 |
| migu_interface | 35 |
| epg_tw | 19 |
| iptv_org_all | 10 |
| vamoschuck_m3u | 10 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| guovin_ipv6 | 2 |
| suxuang_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 60
- epg_cn: 23
- zbds_iptv4_txt: 23
- suxuang_ipv4: 10
- iptv_org_all: 7
- iyouhun_zb: 4
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 109
- zbds_iptv4_txt: 45
- suxuang_ipv4: 24
- guovin_all: 12
- iyouhun_zb: 6
- guovin_ipv6: 2
- iptv_org_all: 1

### 地方频道
- guovin_all: 242
- zbds_iptv4_txt: 216
- iyouhun_zb: 152
- epg_cn: 135
- suxuang_ipv4: 23
- guovin_ipv4: 13
- migu_interface: 11
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 50
- guovin_all: 34
- suxuang_ipv4: 31
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 7
- epg_cn: 6
- iyouhun_zb: 2
- epg_tw: 1
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
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 40
- guovin_all: 26
- epg_cn: 17
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 2

### 综合娱乐
- bigbiggrandg_gather: 396
- epg_cn: 236
- iyouhun_zb: 88
- suxuang_ipv4: 79
- guovin_all: 24
- migu_interface: 21
- mursor_yy: 20
- epg_tw: 18

### 港澳台频道
- iyouhun_zb: 38
- suxuang_ipv4: 15
- bigbiggrandg_gather: 13
- epg_cn: 11
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
- free_tv_world: 1

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
