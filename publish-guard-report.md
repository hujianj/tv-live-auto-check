# Publish guard report

Status: ok
Baseline lines: 228
Current lines: 333
Total drop ratio: -46.1%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 300, 'groups': {'央视频道': 18, '卫视频道': 15, '地方频道': 128, '影视剧场': 65, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 25 | 24 | -1 | 4.0% | 1 |
| 卫视频道 | 18 | 21 | 3 | -16.7% | 1 |
| 地方频道 | 87 | 147 | 60 | -69.0% | 1 |
| 影视剧场 | 63 | 65 | 2 | -3.2% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 18 | -4 | 18.2% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 7 | 51 | 44 | -628.6% | 0 |
| 港澳台频道 | 3 | 4 | 1 | -33.3% | 0 |
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
