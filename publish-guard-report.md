# Publish guard report

Status: ok
Baseline lines: 342
Current lines: 341
Total drop ratio: 0.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 308, 'groups': {'央视频道': 19, '卫视频道': 14, '地方频道': 137, '影视剧场': 64, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 25 | 24 | -1 | 4.0% | 1 |
| 卫视频道 | 23 | 20 | -3 | 13.0% | 1 |
| 地方频道 | 154 | 157 | 3 | -1.9% | 1 |
| 影视剧场 | 65 | 64 | -1 | 1.5% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 51 | 0 | 0.0% | 0 |
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
