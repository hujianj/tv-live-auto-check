# Publish guard report

Status: ok
Baseline lines: 333
Current lines: 282
Total drop ratio: 15.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 233, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 108, '影视剧场': 65, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 2, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 30 | 32 | 2 | -6.7% | 1 |
| 卫视频道 | 25 | 27 | 2 | -8.0% | 1 |
| 地方频道 | 158 | 132 | -26 | 16.5% | 1 |
| 影视剧场 | 48 | 65 | 17 | -35.4% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 2 | 2 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 49 | 4 | -45 | 91.8% | 0 |
| 港澳台频道 | 1 | 0 | -1 | 100.0% | 0 |
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
