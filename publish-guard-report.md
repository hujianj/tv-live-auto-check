# Publish guard report

Status: ok
Baseline lines: 342
Current lines: 138
Total drop ratio: 59.6%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 115, 'groups': {'央视频道': 16, '卫视频道': 8, '地方频道': 61, '影视剧场': 2, '少儿动漫': 2, '体育纪实': 21, '音乐综艺': 1, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 22 | 17 | -5 | 22.7% | 1 |
| 卫视频道 | 21 | 12 | -9 | 42.9% | 1 |
| 地方频道 | 162 | 77 | -85 | 52.5% | 1 |
| 影视剧场 | 64 | 2 | -62 | 96.9% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 23 | 5 | -27.8% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 4 | -47 | 92.2% | 0 |
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

- unique channels dropped: baseline=309 current=115
- group 央视频道 unique channels 16 < minimum 18
- group 卫视频道 unique channels 8 < minimum 10
- group 卫视频道 unique channels dropped: baseline=15 current=8
- group 地方频道 unique channels dropped: baseline=142 current=61
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive']
