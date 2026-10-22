# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 153
Published channel names: 151
Stability history URLs loaded: 0
Home priority URLs loaded: ok=0, failed=0, enabled=False

## Quality filters and limits

- Strict quality filter dropped rows: 0
- Channel limit trimmed rows: 0
- Group limit trimmed rows: 0
- Quality config: `config/quality.json`

### Drop counts


### Group limit trims

- none

## Groups
- 央视频道: 17
- 卫视频道: 4
- 地方频道: 36
- 影视剧场: 47
- 体育纪实: 27
- 音乐综艺: 18
- 综合娱乐: 4

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 135 |
| iptv_org_cn | 11 |
| free_tv_world | 7 |

## Top sources per group

### 央视频道
- iptv_org_cn: 11
- free_tv_world: 6

### 卫视频道
- zbds_iptv4_txt: 4

### 地方频道
- zbds_iptv4_txt: 35
- free_tv_world: 1

### 影视剧场
- zbds_iptv4_txt: 47

### 体育纪实
- zbds_iptv4_txt: 27

### 音乐综艺
- zbds_iptv4_txt: 18

### 综合娱乐
- zbds_iptv4_txt: 4


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Explicit Chinese Hong Kong/Macau/Taiwan channels moved later
- Foreign channels, including overseas Chinese stations, excluded
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
