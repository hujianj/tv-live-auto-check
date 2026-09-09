# Publish guard report

Status: ok
Baseline lines: 13
Current lines: 293
Total drop ratio: -2153.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 273, 'groups': {'央视频道': 19, '卫视频道': 13, '地方频道': 123, '影视剧场': 45, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 50, '港澳台频道': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 8 | 22 | 14 | -175.0% | 1 |
| 卫视频道 | 0 | 17 | 17 | n/a | 1 |
| 地方频道 | 3 | 134 | 131 | -4366.7% | 1 |
| 影视剧场 | 0 | 45 | 45 | n/a | 0 |
| 少儿动漫 | 0 | 2 | 2 | n/a | 0 |
| 体育纪实 | 0 | 18 | 18 | n/a | 0 |
| 音乐综艺 | 0 | 1 | 1 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 0 | 50 | 50 | n/a | 0 |
| 港澳台频道 | 2 | 4 | 2 | -100.0% | 0 |
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

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
