# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2714
Published channel names: 1693
Stability history URLs loaded: 4772
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 482
- Channel limit trimmed rows: 1743
- Group limit trimmed rows: 162
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 6757
- unstable_or_wrong_alias: 789
- strict_quality_filter: 482
- foreign_channel: 411
- ambiguous_url_identity: 230
- cgtn_url: 26
- invalid_name_or_url: 3

### Group limit trims

- 海外华语频道: 130
- 综合娱乐: 32

## Groups
- 央视频道: 133
- 卫视频道: 198
- 地方频道: 809
- 影视剧场: 169
- 少儿动漫: 27
- 体育纪实: 64
- 音乐综艺: 32
- 生活休闲: 88
- 综合娱乐: 900
- 港澳台频道: 74
- 海外华语频道: 220

## Final published lines by source

| Source | Lines |
|---|---:|
| epg_cn | 467 |
| bigbiggrandg_gather | 433 |
| zbds_iptv4_txt | 380 |
| guovin_all | 362 |
| mursor_yy | 312 |
| iyouhun_zb | 302 |
| guovin_ipv4 | 216 |
| suxuang_ipv4 | 165 |
| migu_interface | 34 |
| iptv_org_all | 11 |
| vamoschuck_m3u | 8 |
| suxuang_ipv6 | 6 |
| epg_mo | 6 |
| kimentanm_aptv | 3 |
| epg_tw | 3 |
| guovin_ipv6 | 2 |
| yang_gather | 2 |
| free_tv_world | 1 |
| iptv_org_tw | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 57
- epg_cn: 27
- zbds_iptv4_txt: 27
- suxuang_ipv4: 7
- iptv_org_all: 6
- iyouhun_zb: 5
- migu_interface: 4

### 卫视频道
- guovin_ipv4: 110
- zbds_iptv4_txt: 42
- suxuang_ipv4: 21
- guovin_all: 12
- iyouhun_zb: 8
- guovin_ipv6: 2
- iptv_org_all: 1
- migu_interface: 1

### 地方频道
- guovin_all: 249
- zbds_iptv4_txt: 223
- epg_cn: 143
- iyouhun_zb: 139
- suxuang_ipv4: 24
- guovin_ipv4: 11
- migu_interface: 7
- vamoschuck_m3u: 7

### 影视剧场
- mursor_yy: 46
- suxuang_ipv4: 31
- guovin_all: 30
- iyouhun_zb: 23
- zbds_iptv4_txt: 17
- guovin_ipv4: 14
- bigbiggrandg_gather: 5
- migu_interface: 2

### 少儿动漫
- epg_cn: 11
- guovin_all: 8
- mursor_yy: 6
- iyouhun_zb: 2

### 体育纪实
- zbds_iptv4_txt: 30
- iyouhun_zb: 16
- guovin_ipv4: 10
- epg_cn: 3
- mursor_yy: 3
- guovin_all: 2

### 音乐综艺
- mursor_yy: 13
- bigbiggrandg_gather: 10
- guovin_ipv4: 3
- kimentanm_aptv: 3
- epg_cn: 1
- iyouhun_zb: 1
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 26
- iyouhun_zb: 22
- epg_cn: 19
- bigbiggrandg_gather: 8
- mursor_yy: 5
- guovin_ipv4: 3
- iptv_org_all: 2
- migu_interface: 2

### 综合娱乐
- bigbiggrandg_gather: 392
- epg_cn: 245
- suxuang_ipv4: 73
- iyouhun_zb: 69
- zbds_iptv4_txt: 39
- guovin_all: 28
- mursor_yy: 20
- migu_interface: 18

### 港澳台频道
- epg_cn: 18
- iyouhun_zb: 17
- bigbiggrandg_gather: 13
- suxuang_ipv4: 8
- guovin_all: 7
- suxuang_ipv6: 5
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
