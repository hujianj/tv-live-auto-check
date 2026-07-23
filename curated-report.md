# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2740
Published channel names: 1688
Stability history URLs loaded: 4966
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 470
- Channel limit trimmed rows: 1781
- Group limit trimmed rows: 118
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7029
- unstable_or_wrong_alias: 834
- strict_quality_filter: 470
- foreign_channel: 420
- ambiguous_url_identity: 225
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 109
- 影视剧场: 9

## Groups
- 央视频道: 131
- 卫视频道: 198
- 地方频道: 820
- 影视剧场: 180
- 少儿动漫: 26
- 体育纪实: 65
- 音乐综艺: 32
- 生活休闲: 105
- 综合娱乐: 894
- 港澳台频道: 69
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 501 |
| zbds_iptv4_txt | 425 |
| bigbiggrandg_gather | 392 |
| guovin_all | 358 |
| iyouhun_zb | 335 |
| mursor_yy | 301 |
| guovin_ipv4 | 208 |
| suxuang_ipv4 | 143 |
| migu_interface | 37 |
| iptv_org_all | 10 |
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
- guovin_ipv4: 53
- epg_cn: 30
- zbds_iptv4_txt: 29
- iyouhun_zb: 6
- suxuang_ipv4: 6
- iptv_org_all: 5
- migu_interface: 2

### 卫视频道
- guovin_ipv4: 107
- zbds_iptv4_txt: 58
- guovin_all: 12
- suxuang_ipv4: 12
- iyouhun_zb: 4
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 247
- zbds_iptv4_txt: 223
- iyouhun_zb: 147
- epg_cn: 145
- suxuang_ipv4: 23
- guovin_ipv4: 11
- migu_interface: 11
- vamoschuck_m3u: 7

### 影视剧场
- mursor_yy: 39
- guovin_all: 34
- iyouhun_zb: 32
- zbds_iptv4_txt: 30
- suxuang_ipv4: 26
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 10
- guovin_all: 6
- mursor_yy: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
- mursor_yy: 4
- epg_cn: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 9
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 2
- epg_cn: 1
- iyouhun_zb: 1

### 生活休闲
- iyouhun_zb: 36
- epg_cn: 26
- guovin_all: 26
- bigbiggrandg_gather: 7
- mursor_yy: 4
- guovin_ipv4: 3
- iptv_org_all: 2
- vamoschuck_m3u: 1

### 综合娱乐
- bigbiggrandg_gather: 353
- epg_cn: 271
- iyouhun_zb: 74
- suxuang_ipv4: 69
- zbds_iptv4_txt: 50
- guovin_all: 24
- migu_interface: 21
- mursor_yy: 16

### 港澳台频道
- iyouhun_zb: 17
- epg_cn: 15
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 7
- suxuang_ipv6: 4
- guovin_ipv4: 2
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
