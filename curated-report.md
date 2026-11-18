# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 429
Published channel names: 343
Stability history URLs loaded: 475
Home priority URLs loaded: ok=0, failed=0, enabled=False

## Quality filters and limits

- Strict quality filter dropped rows: 0
- Channel limit trimmed rows: 0
- Group limit trimmed rows: 0
- Quality config: `config/quality.json`

### Drop counts

- ambiguous_url_identity: 28

### Group limit trims

- none

## Groups
- 央视频道: 33
- 卫视频道: 34
- 地方频道: 250
- 影视剧场: 62
- 少儿动漫: 2
- 体育纪实: 24
- 音乐综艺: 19
- 综合娱乐: 5

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 393 |
| oktv_comprehensive_php | 19 |
| iptv_org_cn | 11 |
| free_tv_world | 6 |

## Top sources per group

### 央视频道
- iptv_org_cn: 11
- oktv_comprehensive_php: 9
- zbds_iptv4_txt: 7
- free_tv_world: 6

### 卫视频道
- zbds_iptv4_txt: 24
- oktv_comprehensive_php: 10

### 地方频道
- zbds_iptv4_txt: 250

### 影视剧场
- zbds_iptv4_txt: 62

### 少儿动漫
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 24

### 音乐综艺
- zbds_iptv4_txt: 19

### 综合娱乐
- zbds_iptv4_txt: 5


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Explicit Chinese Hong Kong/Macau/Taiwan channels moved later
- Foreign channels, including overseas Chinese stations, excluded
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
