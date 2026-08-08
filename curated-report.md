# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2713
Published channel names: 1672
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 465
- Channel limit trimmed rows: 1464
- Group limit trimmed rows: 204
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7063
- unstable_or_wrong_alias: 821
- strict_quality_filter: 465
- foreign_channel: 372
- ambiguous_url_identity: 247
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 181
- 港澳台频道: 16
- 影视剧场: 7

## Groups
- 央视频道: 128
- 卫视频道: 197
- 地方频道: 780
- 影视剧场: 180
- 少儿动漫: 24
- 体育纪实: 68
- 音乐综艺: 32
- 生活休闲: 103
- 综合娱乐: 891
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 436 |
| epg_cn | 426 |
| iyouhun_zb | 377 |
| zbds_iptv4_txt | 350 |
| mursor_yy | 326 |
| guovin_all | 312 |
| guovin_ipv4 | 217 |
| suxuang_ipv4 | 185 |
| migu_interface | 37 |
| epg_tw | 12 |
| iptv_org_all | 9 |
| vamoschuck_m3u | 9 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| suxuang_ipv6 | 2 |
| epg_hk | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 50
- zbds_iptv4_txt: 32
- epg_cn: 24
- suxuang_ipv4: 10
- iptv_org_all: 7
- migu_interface: 3
- iyouhun_zb: 2

### 卫视频道
- guovin_ipv4: 115
- zbds_iptv4_txt: 41
- suxuang_ipv4: 24
- guovin_all: 9
- iyouhun_zb: 7
- migu_interface: 1

### 地方频道
- zbds_iptv4_txt: 220
- guovin_all: 209
- iyouhun_zb: 157
- epg_cn: 135
- suxuang_ipv4: 22
- guovin_ipv4: 13
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 54
- suxuang_ipv4: 32
- guovin_all: 26
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
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
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 41
- guovin_all: 27
- epg_cn: 16
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 395
- epg_cn: 233
- iyouhun_zb: 85
- suxuang_ipv4: 80
- guovin_all: 24
- migu_interface: 21
- mursor_yy: 21
- epg_tw: 12

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 9
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
