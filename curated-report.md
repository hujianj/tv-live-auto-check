# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 429
Published channel names: 358
Stability history URLs loaded: 0
Home priority URLs loaded: ok=0, failed=0, enabled=False

## Quality filters and limits

- Strict quality filter dropped rows: 0
- Channel limit trimmed rows: 0
- Group limit trimmed rows: 0
- Quality config: `config/quality.json`

### Drop counts

- ambiguous_url_identity: 26

### Group limit trims

- none

## Groups
- 央视频道: 24
- 卫视频道: 26
- 地方频道: 267
- 影视剧场: 24
- 少儿动漫: 2
- 体育纪实: 31
- 音乐综艺: 2
- 综合娱乐: 49
- 港澳台频道: 4

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 413 |
| iptv_org_cn | 12 |
| free_tv_world | 2 |
| iptv_org_tw | 2 |

## Top sources per group

### 央视频道
- iptv_org_cn: 11
- zbds_iptv4_txt: 11
- free_tv_world: 2

### 卫视频道
- zbds_iptv4_txt: 25
- iptv_org_cn: 1

### 地方频道
- zbds_iptv4_txt: 267

### 影视剧场
- zbds_iptv4_txt: 24

### 少儿动漫
- zbds_iptv4_txt: 2

### 体育纪实
- zbds_iptv4_txt: 31

### 音乐综艺
- zbds_iptv4_txt: 2

### 综合娱乐
- zbds_iptv4_txt: 49

### 港澳台频道
- iptv_org_tw: 2
- zbds_iptv4_txt: 2


## Rules
- CCTV sorted as CCTV-1, CCTV-2, CCTV-3...
- Mainland CCTV/satellite/local channels first
- Explicit Chinese Hong Kong/Macau/Taiwan channels moved later
- Foreign channels, including overseas Chinese stations, excluded
- English/foreign-language channels removed
- English category names removed
- Not24/7 and obvious unstable entries removed from TV-facing playlist
- Pseudo-CCTV aliases containing RTHK/TVB/ViuTV/HK/TW markers removed from CCTV
