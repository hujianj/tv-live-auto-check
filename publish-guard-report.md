# Publish guard report

Status: ok
Baseline lines: 12
Current lines: 13
Total drop ratio: -8.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 13, 'groups': {'央视频道': 8, '地方频道': 3, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 7 | 8 | 1 | -14.3% | 1 |
| 卫视频道 | 0 | 0 | 0 | n/a | 1 |
| 地方频道 | 3 | 3 | 0 | 0.0% | 1 |
| 影视剧场 | 0 | 0 | 0 | n/a | 0 |
| 少儿动漫 | 0 | 0 | 0 | n/a | 0 |
| 体育纪实 | 0 | 0 | 0 | n/a | 0 |
| 音乐综艺 | 0 | 0 | 0 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 0 | 0 | 0 | n/a | 0 |
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

- unique channels 13 < minimum 29
- group 央视频道 unique channels 8 < minimum 18
- group 卫视频道 unique channels 0 < minimum 10
- group 卫视频道 count 0 < minimum 1
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
