# Publish guard report

Status: ok
Baseline lines: 336
Current lines: 316
Total drop ratio: 6.0%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 291, 'groups': {'央视频道': 18, '卫视频道': 15, '地方频道': 121, '影视剧场': 65, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 21 | 23 | 2 | -9.5% | 1 |
| 卫视频道 | 17 | 22 | 5 | -29.4% | 1 |
| 地方频道 | 162 | 132 | -30 | 18.5% | 1 |
| 影视剧场 | 64 | 65 | 1 | -1.6% | 0 |
| 少儿动漫 | 1 | 2 | 1 | -100.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 51 | 0 | 0.0% | 0 |
| 港澳台频道 | 1 | 2 | 1 | -100.0% | 0 |
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
