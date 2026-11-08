# Publish guard report

Status: ok
Baseline lines: 285
Current lines: 276
Total drop ratio: 3.2%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 230, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 105, '影视剧场': 65, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 2, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 30 | 31 | 1 | -3.3% | 1 |
| 卫视频道 | 27 | 28 | 1 | -3.7% | 1 |
| 地方频道 | 137 | 127 | -10 | 7.3% | 1 |
| 影视剧场 | 65 | 65 | 0 | 0.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 17 | -1 | 5.6% | 0 |
| 音乐综艺 | 2 | 2 | 0 | 0.0% | 0 |
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
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive
- Candidate sources parsed empty (non-blocking): none

## Warnings

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive']
