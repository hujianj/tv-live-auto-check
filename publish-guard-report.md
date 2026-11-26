# Publish guard report

Status: ok
Baseline lines: 273
Current lines: 278
Total drop ratio: -1.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 236, 'groups': {'央视频道': 17, '卫视频道': 19, '地方频道': 106, '影视剧场': 66, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 9}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 29 | 28 | -1 | 3.4% | 1 |
| 卫视频道 | 26 | 28 | 2 | -7.7% | 1 |
| 地方频道 | 124 | 125 | 1 | -0.8% | 1 |
| 影视剧场 | 64 | 67 | 3 | -4.7% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 19 | 18 | -1 | 5.3% | 0 |
| 音乐综艺 | 0 | 1 | 1 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 9 | 9 | 0 | 0.0% | 0 |
| 港澳台频道 | 0 | 0 | 0 | n/a | 0 |
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
