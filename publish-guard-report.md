# Publish guard report

Status: ok
Baseline lines: 316
Current lines: 315
Total drop ratio: 0.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 286, 'groups': {'央视频道': 17, '卫视频道': 14, '地方频道': 135, '影视剧场': 49, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 50, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 23 | 18 | -5 | 21.7% | 1 |
| 卫视频道 | 22 | 20 | -2 | 9.1% | 1 |
| 地方频道 | 132 | 155 | 23 | -17.4% | 1 |
| 影视剧场 | 65 | 49 | -16 | 24.6% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 50 | -1 | 2.0% | 0 |
| 港澳台频道 | 2 | 2 | 0 | 0.0% | 0 |
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
