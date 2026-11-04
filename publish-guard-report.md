# Publish guard report

Status: ok
Baseline lines: 216
Current lines: 248
Total drop ratio: -14.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 206, 'groups': {'央视频道': 17, '卫视频道': 18, '地方频道': 100, '影视剧场': 47, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 2, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 29 | 30 | 1 | -3.4% | 1 |
| 卫视频道 | 28 | 29 | 1 | -3.6% | 1 |
| 地方频道 | 133 | 116 | -17 | 12.8% | 1 |
| 影视剧场 | 2 | 47 | 45 | -2250.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 2 | 1 | -100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 3 | 4 | 1 | -33.3% | 0 |
| 港澳台频道 | 0 | 0 | 0 | n/a | 0 |
| 海外华语频道 | 0 | 0 | 0 | n/a | 0 |

## Source health

- Enabled source failures: none
- Enabled sources fetched but zero parsed: none
- Enabled sources unavailable for guard purposes: none
- Recovery source failures (non-blocking): none
- Recovery sources fetched but zero parsed (non-blocking): none
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_huya
- Candidate sources parsed empty (non-blocking): none

## Warnings

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya']
