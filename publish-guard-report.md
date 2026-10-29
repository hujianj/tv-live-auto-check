# Publish guard report

Status: ok
Baseline lines: 218
Current lines: 260
Total drop ratio: -19.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 227, 'groups': {'央视频道': 16, '卫视频道': 18, '地方频道': 126, '影视剧场': 2, '少儿动漫': 1, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 46, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 23 | 20 | -3 | 13.0% | 1 |
| 卫视频道 | 25 | 25 | 0 | 0.0% | 1 |
| 地方频道 | 143 | 146 | 3 | -2.1% | 1 |
| 影视剧场 | 3 | 2 | -1 | 33.3% | 0 |
| 少儿动漫 | 1 | 1 | 0 | 0.0% | 0 |
| 体育纪实 | 21 | 18 | -3 | 14.3% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 1 | 46 | 45 | -4500.0% | 0 |
| 港澳台频道 | 0 | 1 | 1 | n/a | 0 |
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

- group 央视频道 unique channels 16 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive']
