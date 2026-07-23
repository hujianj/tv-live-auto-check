# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2784
Published channel names: 1714
Stability history URLs loaded: 4947
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 473
- Channel limit trimmed rows: 1796
- Group limit trimmed rows: 158
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7052
- unstable_or_wrong_alias: 837
- strict_quality_filter: 473
- foreign_channel: 422
- ambiguous_url_identity: 272
- cgtn_url: 26
- invalid_name_or_url: 2

### Group limit trims

- 海外华语频道: 128
- 综合娱乐: 30

## Groups
- 央视频道: 133
- 卫视频道: 198
- 地方频道: 865
- 影视剧场: 172
- 少儿动漫: 26
- 体育纪实: 63
- 音乐综艺: 31
- 生活休闲: 102
- 综合娱乐: 900
- 港澳台频道: 74
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 494 |
| zbds_iptv4_txt | 440 |
| bigbiggrandg_gather | 433 |
| guovin_all | 358 |
| iyouhun_zb | 332 |
| mursor_yy | 307 |
| guovin_ipv4 | 212 |
| suxuang_ipv4 | 133 |
| migu_interface | 35 |
| iptv_org_all | 10 |
| vamoschuck_m3u | 10 |
| epg_mo | 6 |
| suxuang_ipv6 | 5 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| guovin_ipv6 | 1 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 56
- zbds_iptv4_txt: 32
- epg_cn: 30
- iyouhun_zb: 6
- iptv_org_all: 5
- migu_interface: 2
- suxuang_ipv4: 2

### 卫视频道
- guovin_ipv4: 106
- zbds_iptv4_txt: 51
- suxuang_ipv4: 17
- guovin_all: 12
- iyouhun_zb: 8
- guovin_ipv6: 1
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- zbds_iptv4_txt: 255
- guovin_all: 249
- iyouhun_zb: 152
- epg_cn: 147
- suxuang_ipv4: 26
- guovin_ipv4: 11
- migu_interface: 10
- vamoschuck_m3u: 9

### 影视剧场
- mursor_yy: 46
- guovin_all: 31
- zbds_iptv4_txt: 29
- iyouhun_zb: 22
- suxuang_ipv4: 22
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 9
- guovin_all: 7
- mursor_yy: 7
- iyouhun_zb: 2
- zbds_iptv4_txt: 1

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 9
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- iyouhun_zb: 32
- guovin_all: 27
- epg_cn: 25
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2

### 综合娱乐
- bigbiggrandg_gather: 392
- epg_cn: 261
- iyouhun_zb: 76
- suxuang_ipv4: 59
- zbds_iptv4_txt: 40
- guovin_all: 23
- migu_interface: 20
- mursor_yy: 14

### 港澳台频道
- epg_cn: 19
- iyouhun_zb: 17
- bigbiggrandg_gather: 13
- guovin_all: 7
- suxuang_ipv4: 7
- suxuang_ipv6: 4
- guovin_ipv4: 3
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
