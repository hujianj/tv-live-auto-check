# Publish guard report

Status: ok
Baseline lines: 204
Current lines: 272
Total drop ratio: -33.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 226, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 108, '影视剧场': 60, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 2, '综合娱乐': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 30 | 31 | 1 | -3.3% | 1 |
| 卫视频道 | 27 | 27 | 0 | 0.0% | 1 |
| 地方频道 | 117 | 130 | 13 | -11.1% | 1 |
| 影视剧场 | 2 | 60 | 58 | -2900.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 18 | -4 | 18.2% | 0 |
| 音乐综艺 | 1 | 2 | 1 | -100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 3 | 2 | -1 | 33.3% | 0 |
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
