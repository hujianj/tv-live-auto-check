# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 10
Published channel names: 10
Stability history URLs loaded: 4874
Home priority URLs loaded: ok=0, failed=0, enabled=False

## Quality filters and limits

- Strict quality filter dropped rows: 0
- Channel limit trimmed rows: 0
- Group limit trimmed rows: 0
- Quality config: `config/quality.json`

### Drop counts

- ambiguous_url_identity: 24

### Group limit trims

- none

## Groups
- 央视频道: 6
- 卫视频道: 1
- 地方频道: 1
- 港澳台频道: 2

## Final published lines by source

| Source | Lines |
|---|---:|
| free_tv_world | 5 |
| iptv_org_cn | 3 |
| iptv_org_tw | 2 |

## Top sources per group

### 央视频道
- free_tv_world: 4
- iptv_org_cn: 2

### 卫视频道
- iptv_org_cn: 1

### 地方频道
- free_tv_world: 1

### 港澳台频道
- iptv_org_tw: 2


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Explicit Chinese Hong Kong/Macau/Taiwan channels moved later
- Foreign channels, including overseas Chinese stations, excluded
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
