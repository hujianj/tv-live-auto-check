# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 2244
Published channel names: 1446
Stability history URLs loaded: 5000
Home priority URLs loaded: ok=0, failed=0, enabled=True

## Quality filters and limits

- Strict quality filter dropped rows: 443
- Channel limit trimmed rows: 689
- Group limit trimmed rows: 181
- Quality config: `config/quality.json`

### Drop counts

- unwanted_overseas_english: 7284
- unstable_or_wrong_alias: 814
- foreign_channel: 529
- strict_quality_filter: 443
- ambiguous_url_identity: 154
- cgtn_url: 15
- latin_noise_name: 2
- invalid_name_or_url: 1

### Group limit trims

- 综合娱乐: 181

## Groups
- 央视频道: 128
- 卫视频道: 168
- 地方频道: 657
- 影视剧场: 162
- 少儿动漫: 20
- 体育纪实: 49
- 音乐综艺: 28
- 生活休闲: 64
- 综合娱乐: 900
- 港澳台频道: 68

## Final published lines by source

| Source | Lines |
|---|---:|
| bigbiggrandg_gather | 443 |
| zbds_iptv4_txt | 428 |
| epg_cn | 380 |
| guovin_all | 348 |
| mursor_yy | 300 |
| guovin_ipv4 | 200 |
| suxuang_ipv4 | 101 |
| vamoschuck_m3u | 12 |
| suxuang_ipv6 | 7 |
| epg_mo | 7 |
| iptv_org_all | 6 |
| kimentanm_aptv | 3 |
| yang_gather | 2 |
| iptv_org_tw | 2 |
| epg_hk | 2 |
| free_tv_world | 1 |
| guovin_ipv6 | 1 |
| iyouhun_zb | 1 |

## Top sources per group

### 央视频道
- guovin_ipv4: 51
- epg_cn: 38
- zbds_iptv4_txt: 37
- free_tv_world: 1
- iptv_org_all: 1

### 卫视频道
- guovin_ipv4: 87
- zbds_iptv4_txt: 66
- guovin_all: 9
- suxuang_ipv4: 4
- bigbiggrandg_gather: 1
- suxuang_ipv6: 1

### 地方频道
- guovin_all: 253
- zbds_iptv4_txt: 221
- epg_cn: 130
- guovin_ipv4: 20
- suxuang_ipv4: 16
- vamoschuck_m3u: 10
- bigbiggrandg_gather: 5
- guovin_ipv6: 1

### 影视剧场
- zbds_iptv4_txt: 65
- mursor_yy: 34
- guovin_all: 22
- guovin_ipv4: 19
- suxuang_ipv4: 16
- bigbiggrandg_gather: 5
- vamoschuck_m3u: 1

### 少儿动漫
- guovin_all: 7
- epg_cn: 6
- mursor_yy: 4
- zbds_iptv4_txt: 3

### 体育纪实
- zbds_iptv4_txt: 30
- guovin_ipv4: 9
- guovin_all: 4
- epg_cn: 3
- mursor_yy: 3

### 音乐综艺
- bigbiggrandg_gather: 12
- mursor_yy: 9
- guovin_ipv4: 3
- kimentanm_aptv: 3
- zbds_iptv4_txt: 1

### 生活休闲
- guovin_all: 30
- epg_cn: 14
- bigbiggrandg_gather: 9
- mursor_yy: 4
- guovin_ipv4: 3
- iptv_org_all: 2
- suxuang_ipv4: 1
- vamoschuck_m3u: 1

### 综合娱乐
- bigbiggrandg_gather: 395
- mursor_yy: 244
- epg_cn: 181
- suxuang_ipv4: 40
- guovin_all: 16
- epg_mo: 7
- guovin_ipv4: 6
- zbds_iptv4_txt: 4

### 港澳台频道
- suxuang_ipv4: 24
- bigbiggrandg_gather: 16
- epg_cn: 8
- guovin_all: 7
- suxuang_ipv6: 6
- guovin_ipv4: 2
- mursor_yy: 2
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
