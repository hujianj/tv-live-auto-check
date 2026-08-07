# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2665
Published channel names: 1664
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 464
- Channel limit trimmed rows: 1509
- Group limit trimmed rows: 211
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7010
- unstable_or_wrong_alias: 829
- strict_quality_filter: 464
- foreign_channel: 368
- ambiguous_url_identity: 213
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 192
- 港澳台频道: 15
- 影视剧场: 4

## Groups
- 央视频道: 128
- 卫视频道: 198
- 地方频道: 736
- 影视剧场: 180
- 少儿动漫: 26
- 体育纪实: 65
- 音乐综艺: 33
- 生活休闲: 101
- 综合娱乐: 888
- 港澳台频道: 90
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 435 |
| epg_cn | 410 |
| iyouhun_zb | 379 |
| mursor_yy | 322 |
| guovin_all | 317 |
| zbds_iptv4_txt | 306 |
| guovin_ipv4 | 225 |
| suxuang_ipv4 | 179 |
| migu_interface | 40 |
| epg_tw | 19 |
| iptv_org_all | 10 |
| vamoschuck_m3u | 10 |
| epg_mo | 7 |
| kimentanm_aptv | 3 |
| suxuang_ipv6 | 2 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 53
- zbds_iptv4_txt: 26
- epg_cn: 23
- suxuang_ipv4: 10
- iptv_org_all: 7
- migu_interface: 5
- iyouhun_zb: 4

### 卫视频道
- guovin_ipv4: 118
- zbds_iptv4_txt: 42
- suxuang_ipv4: 21
- guovin_all: 9
- iyouhun_zb: 6
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 210
- zbds_iptv4_txt: 181
- iyouhun_zb: 157
- epg_cn: 128
- suxuang_ipv4: 22
- guovin_ipv4: 13
- migu_interface: 11
- vamoschuck_m3u: 8

### 影视剧场
- mursor_yy: 51
- suxuang_ipv4: 30
- guovin_all: 28
- iyouhun_zb: 25
- zbds_iptv4_txt: 22
- guovin_ipv4: 16
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- guovin_all: 8
- mursor_yy: 8
- epg_cn: 6
- iyouhun_zb: 2
- epg_tw: 1
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
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
- iyouhun_zb: 39
- guovin_all: 27
- epg_cn: 15
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 393
- epg_cn: 225
- iyouhun_zb: 90
- suxuang_ipv4: 79
- guovin_all: 26
- migu_interface: 21
- mursor_yy: 19
- epg_tw: 18

### 港澳台频道
- iyouhun_zb: 39
- suxuang_ipv4: 16
- bigbiggrandg_gather: 13
- epg_cn: 10
- guovin_all: 7
- guovin_ipv4: 2
- suxuang_ipv6: 2
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
