# Publish guard report

Status: ok
Baseline lines: 296
Current lines: 251
Total drop ratio: 15.2%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 205, 'groups': {'央视频道': 17, '卫视频道': 19, '地方频道': 141, '影视剧场': 3, '少儿动漫': 1, '体育纪实': 20, '音乐综艺': 2, '综合娱乐': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 31 | 29 | -2 | 6.5% | 1 |
| 卫视频道 | 27 | 27 | 0 | 0.0% | 1 |
| 地方频道 | 167 | 165 | -2 | 1.2% | 1 |
| 影视剧场 | 3 | 3 | 0 | 0.0% | 0 |
| 少儿动漫 | 1 | 1 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 22 | 4 | -22.2% | 0 |
| 音乐综艺 | 2 | 2 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 46 | 2 | -44 | 95.7% | 0 |
| 港澳台频道 | 1 | 0 | -1 | 100.0% | 0 |
| 海外华语频道 | 0 | 0 | 0 | n/a | 0 |

## Source health

- Enabled source failures: none
- Enabled sources fetched but zero parsed: none
- Enabled sources unavailable for guard purposes: none
- Recovery source failures (non-blocking): none
- Recovery sources fetched but zero parsed (non-blocking): none
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_huya, freetv_douyu
- Candidate sources parsed empty (non-blocking): none

## Warnings

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
