# Pre-recheck curated Ku9 playlist report

This report is generated immediately after curation and before the final published URL recheck. See `final-publish-report.md` for the TV-facing result after recheck.

Pre-recheck candidate lines: 370
Published channel names: 311
Stability history URLs loaded: 414
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
- 央视频道: 26
- 卫视频道: 29
- 地方频道: 189
- 影视剧场: 67
- 少儿动漫: 3
- 体育纪实: 31
- 音乐综艺: 20
- 综合娱乐: 5

## Final published lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 340 |
| oktv_comprehensive_php | 14 |
| iptv_org_cn | 11 |
| free_tv_world | 5 |

## Top sources per group

### 央视频道
- iptv_org_cn: 11
- zbds_iptv4_txt: 6
- free_tv_world: 5
- oktv_comprehensive_php: 4

### 卫视频道
- zbds_iptv4_txt: 19
- oktv_comprehensive_php: 10

### 地方频道
- zbds_iptv4_txt: 189

### 影视剧场
- zbds_iptv4_txt: 67

### 少儿动漫
- zbds_iptv4_txt: 3

### 体育纪实
- zbds_iptv4_txt: 31

### 音乐综艺
- zbds_iptv4_txt: 20

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
