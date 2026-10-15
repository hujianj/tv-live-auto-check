# Publish guard report

Status: ok
Baseline lines: 315
Current lines: 337
Total drop ratio: -7.0%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 303, 'groups': {'央视频道': 18, '卫视频道': 23, '地方频道': 123, '影视剧场': 65, '少儿动漫': 3, '体育纪实': 17, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 20 | 21 | 1 | -5.0% | 1 |
| 卫视频道 | 21 | 40 | 19 | -90.5% | 1 |
| 地方频道 | 135 | 134 | -1 | 0.7% | 1 |
| 影视剧场 | 64 | 65 | 1 | -1.6% | 0 |
| 少儿动漫 | 2 | 4 | 2 | -100.0% | 0 |
| 体育纪实 | 19 | 19 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 51 | 0 | 0.0% | 0 |
| 港澳台频道 | 2 | 2 | 0 | 0.0% | 0 |
| 海外华语频道 | 0 | 0 | 0 | n/a | 0 |

## Source health

- Enabled source failures: none
- Enabled sources fetched but zero parsed: none
- Enabled sources unavailable for guard purposes: none
- Recovery source failures (non-blocking): none
- Recovery sources fetched but zero parsed (non-blocking): none
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_douyu
- Candidate sources parsed empty (non-blocking): none

## Warnings

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_douyu']
