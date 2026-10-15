# Publish guard report

Status: ok
Baseline lines: 311
Current lines: 315
Total drop ratio: -1.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 292, 'groups': {'央视频道': 17, '卫视频道': 14, '地方频道': 124, '影视剧场': 64, '少儿动漫': 2, '体育纪实': 17, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 20 | 20 | 0 | 0.0% | 1 |
| 卫视频道 | 19 | 21 | 2 | -10.5% | 1 |
| 地方频道 | 134 | 135 | 1 | -0.7% | 1 |
| 影视剧场 | 64 | 64 | 0 | 0.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 19 | 1 | -5.6% | 0 |
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
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive
- Candidate sources parsed empty (non-blocking): none

## Warnings

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive']
