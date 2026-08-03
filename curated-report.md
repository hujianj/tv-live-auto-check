# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2740
Published channel names: 1684
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 452
- Channel limit trimmed rows: 1529
- Group limit trimmed rows: 211
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7067
- unstable_or_wrong_alias: 828
- strict_quality_filter: 452
- foreign_channel: 347
- ambiguous_url_identity: 284
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 191
- 港澳台频道: 13
- 影视剧场: 7

## Groups
- 央视频道: 129
- 卫视频道: 197
- 地方频道: 816
- 影视剧场: 180
- 少儿动漫: 27
- 体育纪实: 65
- 音乐综艺: 33
- 生活休闲: 93
- 综合娱乐: 890
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 434 |
| epg_cn | 424 |
| iyouhun_zb | 372 |
| guovin_all | 354 |
| zbds_iptv4_txt | 326 |
| mursor_yy | 323 |
| guovin_ipv4 | 221 |
| suxuang_ipv4 | 196 |
| migu_interface | 36 |
| epg_tw | 20 |
| iptv_org_all | 9 |
| vamoschuck_m3u | 9 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 3 |
| guovin_ipv6 | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 64
- epg_cn: 28
- suxuang_ipv4: 16
- iptv_org_all: 6
- iyouhun_zb: 6
- zbds_iptv4_txt: 6
- migu_interface: 3

### 卫视频道
- guovin_ipv4: 109
- zbds_iptv4_txt: 41
- suxuang_ipv4: 26
- guovin_all: 12
- iyouhun_zb: 6
- guovin_ipv6: 2
- iptv_org_all: 1

### 地方频道
- guovin_all: 242
- zbds_iptv4_txt: 222
- iyouhun_zb: 156
- epg_cn: 135
- suxuang_ipv4: 25
- guovin_ipv4: 12
- migu_interface: 10
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 51
- guovin_all: 33
- suxuang_ipv4: 31
- iyouhun_zb: 24
- zbds_iptv4_txt: 22
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- epg_cn: 7
- mursor_yy: 7
- epg_tw: 2
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 15
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 37
- guovin_all: 26
- epg_cn: 11
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- epg_cn: 232
- iyouhun_zb: 84
- suxuang_ipv4: 81
- guovin_all: 24
- migu_interface: 21
- mursor_yy: 20
- epg_tw: 18

### 港澳台频道
- iyouhun_zb: 40
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 8
- guovin_all: 7
- suxuang_ipv6: 3
- guovin_ipv4: 2
- mursor_yy: 1

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
