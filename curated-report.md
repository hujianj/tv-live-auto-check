# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2303
Published channel names: 1445
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 449
- Channel limit trimmed rows: 807
- Group limit trimmed rows: 213
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7483
- unstable_or_wrong_alias: 838
- foreign_channel: 592
- strict_quality_filter: 449
- ambiguous_url_identity: 160
- cgtn_url: 15
- latin_noise_name: 2
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 213

## Groups
- 央视频道: 129
- 卫视频道: 187
- 地方频道: 690
- 影视剧场: 168
- 少儿动漫: 21
- 体育纪实: 49
- 音乐综艺: 26
- 生活休闲: 66
- 综合娱乐: 900
- 港澳台频道: 67

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 451 |
| bigbiggrandg_gather | 442 |
| epg_cn | 394 |
| guovin_all | 361 |
| mursor_yy | 291 |
| guovin_ipv4 | 212 |
| suxuang_ipv4 | 96 |
| vamoschuck_m3u | 20 |
| iptv_org_all | 8 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| guovin_ipv6 | 4 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| free_tv_world | 1 |
| iyouhun_zb | 1 |
| epg_hk | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 58
- zbds_iptv4_txt: 35
- epg_cn: 31
- iptv_org_all: 3
- free_tv_world: 1
- suxuang_ipv4: 1

### 卫视频道
- guovin_ipv4: 104
- zbds_iptv4_txt: 65
- guovin_all: 9
- suxuang_ipv4: 4
- guovin_ipv6: 2
- bigbiggrandg_gather: 1
- iptv_org_all: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 252
- zbds_iptv4_txt: 249
- epg_cn: 136
- vamoschuck_m3u: 18
- suxuang_ipv4: 16
- guovin_ipv4: 11
- bigbiggrandg_gather: 5
- guovin_ipv6: 2

### 影视剧场
- zbds_iptv4_txt: 64
- mursor_yy: 34
- guovin_all: 30
- guovin_ipv4: 19
- suxuang_ipv4: 15
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 8
- epg_cn: 5
- mursor_yy: 5
- zbds_iptv4_txt: 3

### 体育纪实
- zbds_iptv4_txt: 30
- guovin_ipv4: 8
- guovin_all: 5
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 11
- mursor_yy: 8
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 19
- bigbiggrandg_gather: 9
- mursor_yy: 4
- iptv_org_all: 2
- guovin_ipv4: 1
- suxuang_ipv4: 1

### 综合娱乐
- bigbiggrandg_gather: 395
- mursor_yy: 234
- epg_cn: 193
- suxuang_ipv4: 36
- guovin_all: 19
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 4

### 港澳台频道
- suxuang_ipv4: 23
- bigbiggrandg_gather: 16
- guovin_all: 8
- epg_cn: 7
- suxuang_ipv6: 6
- mursor_yy: 3
- guovin_ipv4: 2
- epg_hk: 1


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Hong Kong/Macau/Taiwan and overseas Chinese channels moved later
- Pure English/overseas entertainment channels removed from TV-facing playlist unless explicitly HK/MO/TW/Chinese
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
