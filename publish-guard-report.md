# Publish guard report

Status: ok
Baseline lines: 246
Current lines: 283
Total drop ratio: -15.0%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 239, 'groups': {'央视频道': 17, '卫视频道': 18, '地方频道': 110, '影视剧场': 66, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 9}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 28 | 28 | 0 | 0.0% | 1 |
| 卫视频道 | 26 | 27 | 1 | -3.8% | 1 |
| 地方频道 | 110 | 131 | 21 | -19.1% | 1 |
| 影视剧场 | 57 | 67 | 10 | -17.5% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 20 | 18 | -2 | 10.0% | 0 |
| 音乐综艺 | 0 | 1 | 1 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 3 | 9 | 6 | -200.0% | 0 |
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
