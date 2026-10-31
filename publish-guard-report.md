# Publish guard report

Status: ok
Baseline lines: 251
Current lines: 296
Total drop ratio: -17.9%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 248, 'groups': {'央视频道': 18, '卫视频道': 19, '地方频道': 141, '影视剧场': 4, '少儿动漫': 1, '体育纪实': 16, '音乐综艺': 2, '综合娱乐': 46, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 29 | 32 | 3 | -10.3% | 1 |
| 卫视频道 | 27 | 27 | 0 | 0.0% | 1 |
| 地方频道 | 165 | 166 | 1 | -0.6% | 1 |
| 影视剧场 | 3 | 4 | 1 | -33.3% | 0 |
| 少儿动漫 | 1 | 1 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 17 | -5 | 22.7% | 0 |
| 音乐综艺 | 2 | 2 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 2 | 46 | 44 | -2200.0% | 0 |
| 港澳台频道 | 0 | 1 | 1 | n/a | 0 |
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
