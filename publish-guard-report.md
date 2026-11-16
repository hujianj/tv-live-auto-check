# Publish guard report

Status: ok
Baseline lines: 267
Current lines: 274
Total drop ratio: -2.6%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 226, 'groups': {'央视频道': 18, '卫视频道': 20, '地方频道': 113, '影视剧场': 46, '少儿动漫': 2, '体育纪实': 20, '音乐综艺': 3, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 29 | 30 | 1 | -3.4% | 1 |
| 卫视频道 | 30 | 30 | 0 | 0.0% | 1 |
| 地方频道 | 131 | 137 | 6 | -4.6% | 1 |
| 影视剧场 | 65 | 46 | -19 | 29.2% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 3 | 22 | 19 | -633.3% | 0 |
| 音乐综艺 | 3 | 3 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 4 | 0 | 0.0% | 0 |
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

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya']
