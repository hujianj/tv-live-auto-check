# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2745
Published channel names: 1712
Stability history URLs loaded: 4909
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 494
- Channel limit trimmed rows: 1668
- Group limit trimmed rows: 178
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7026
- unstable_or_wrong_alias: 837
- strict_quality_filter: 494
- foreign_channel: 422
- ambiguous_url_identity: 262
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 138
- 综合娱乐: 28
- 影视剧场: 12

## Groups
- 央视频道: 132
- 卫视频道: 191
- 地方频道: 827
- 影视剧场: 180
- 少儿动漫: 26
- 体育纪实: 63
- 音乐综艺: 31
- 生活休闲: 100
- 综合娱乐: 900
- 港澳台频道: 75
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 475 |
| bigbiggrandg_gather | 429 |
| iyouhun_zb | 364 |
| guovin_all | 363 |
| zbds_iptv4_txt | 354 |
| mursor_yy | 301 |
| guovin_ipv4 | 231 |
| suxuang_ipv4 | 158 |
| migu_interface | 31 |
| iptv_org_all | 9 |
| vamoschuck_m3u | 9 |
| epg_mo | 6 |
| suxuang_ipv6 | 5 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| guovin_ipv6 | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 61
- epg_cn: 31
- zbds_iptv4_txt: 18
- suxuang_ipv4: 9
- iyouhun_zb: 7
- iptv_org_all: 5
- migu_interface: 1

### 卫视频道
- guovin_ipv4: 110
- zbds_iptv4_txt: 39
- suxuang_ipv4: 17
- guovin_all: 12
- iyouhun_zb: 9
- guovin_ipv6: 2
- migu_interface: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 245
- zbds_iptv4_txt: 205
- iyouhun_zb: 164
- epg_cn: 146
- suxuang_ipv4: 23
- guovin_ipv4: 21
- migu_interface: 9
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 41
- iyouhun_zb: 35
- guovin_all: 30
- zbds_iptv4_txt: 28
- suxuang_ipv4: 26
- guovin_ipv4: 12
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 9
- guovin_all: 7
- mursor_yy: 7
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 24
- iyouhun_zb: 17
- guovin_ipv4: 10
- guovin_all: 7
- epg_cn: 3
- mursor_yy: 2

### 音乐综艺
- mursor_yy: 11
- bigbiggrandg_gather: 10
- guovin_ipv4: 4
- kimentanm_aptv: 3
- epg_cn: 1
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 31
- guovin_all: 30
- epg_cn: 23
- bigbiggrandg_gather: 7
- mursor_yy: 4
- guovin_ipv4: 3
- iptv_org_all: 2

### 综合娱乐
- bigbiggrandg_gather: 389
- epg_cn: 245
- iyouhun_zb: 78
- suxuang_ipv4: 76
- zbds_iptv4_txt: 37
- guovin_all: 25
- migu_interface: 18
- mursor_yy: 16

### 港澳台频道
- iyouhun_zb: 20
- epg_cn: 17
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 7
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
