# Publish guard report

Status: ok
Baseline lines: 199
Current lines: 341
Total drop ratio: -71.4%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 307, 'groups': {'央视频道': 18, '卫视频道': 15, '地方频道': 141, '影视剧场': 61, '少儿动漫': 2, '体育纪实': 15, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 21 | 24 | 3 | -14.3% | 1 |
| 卫视频道 | 16 | 21 | 5 | -31.2% | 1 |
| 地方频道 | 86 | 161 | 75 | -87.2% | 1 |
| 影视剧场 | 42 | 61 | 19 | -45.2% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 17 | -5 | 22.7% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 6 | 51 | 45 | -750.0% | 0 |
| 港澳台频道 | 3 | 3 | 0 | 0.0% | 0 |
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
