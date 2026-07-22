# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2670
Published channel names: 1662
Stability history URLs loaded: 4874
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 490
- Channel limit trimmed rows: 1624
- Group limit trimmed rows: 131
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6958
- unstable_or_wrong_alias: 821
- strict_quality_filter: 490
- foreign_channel: 422
- ambiguous_url_identity: 214
- cgtn_url: 25
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 131

## Groups
- 央视频道: 132
- 卫视频道: 187
- 地方频道: 805
- 影视剧场: 154
- 少儿动漫: 27
- 体育纪实: 65
- 音乐综艺: 28
- 生活休闲: 93
- 综合娱乐: 883
- 港澳台频道: 76
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 486 |
| bigbiggrandg_gather | 388 |
| guovin_all | 361 |
| zbds_iptv4_txt | 323 |
| iyouhun_zb | 322 |
| mursor_yy | 305 |
| guovin_ipv4 | 230 |
| suxuang_ipv4 | 170 |
| migu_interface | 36 |
| iptv_org_all | 12 |
| vamoschuck_m3u | 8 |
| epg_tw | 7 |
| suxuang_ipv6 | 6 |
| epg_mo | 6 |
| guovin_ipv6 | 3 |
| kimentanm_aptv | 3 |
| epg_hk | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 60
- epg_cn: 30
- zbds_iptv4_txt: 12
- suxuang_ipv4: 11
- iptv_org_all: 7
- iyouhun_zb: 7
- migu_interface: 5

### 卫视频道
- guovin_ipv4: 118
- suxuang_ipv4: 24
- zbds_iptv4_txt: 18
- guovin_all: 12
- iyouhun_zb: 9
- guovin_ipv6: 3
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 249
- zbds_iptv4_txt: 208
- iyouhun_zb: 149
- epg_cn: 142
- suxuang_ipv4: 25
- guovin_ipv4: 12
- migu_interface: 7
- vamoschuck_m3u: 7

### 影视剧场
- mursor_yy: 46
- guovin_all: 31
- suxuang_ipv4: 30
- iyouhun_zb: 21
- guovin_ipv4: 15
- bigbiggrandg_gather: 5
- zbds_iptv4_txt: 3
- migu_interface: 2

### 少儿动漫
- epg_cn: 11
- guovin_all: 7
- mursor_yy: 6
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 19
- guovin_ipv4: 10
- mursor_yy: 3
- guovin_all: 2
- epg_cn: 1

### 音乐综艺
- bigbiggrandg_gather: 10
- mursor_yy: 9
- guovin_ipv4: 3
- kimentanm_aptv: 3
- epg_cn: 1
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 27
- epg_cn: 26
- iyouhun_zb: 20
- bigbiggrandg_gather: 7
- mursor_yy: 4
- guovin_ipv4: 3
- iptv_org_all: 2
- migu_interface: 2

### 综合娱乐
- bigbiggrandg_gather: 348
- epg_cn: 256
- iyouhun_zb: 76
- suxuang_ipv4: 72
- zbds_iptv4_txt: 49
- guovin_all: 26
- migu_interface: 19
- mursor_yy: 17

### 港澳台频道
- epg_cn: 19
- iyouhun_zb: 18
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 6
- suxuang_ipv6: 5
- epg_tw: 2
- guovin_ipv4: 2

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
