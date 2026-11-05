# Publish guard report

Status: ok
Baseline lines: 248
Current lines: 204
Total drop ratio: 17.7%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 160, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 95, '影视剧场': 2, '少儿动漫': 2, '体育纪实': 21, '音乐综艺': 1, '综合娱乐': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 30 | 30 | 0 | 0.0% | 1 |
| 卫视频道 | 29 | 27 | -2 | 6.9% | 1 |
| 地方频道 | 116 | 117 | 1 | -0.9% | 1 |
| 影视剧场 | 47 | 2 | -45 | 95.7% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 22 | 4 | -22.2% | 0 |
| 音乐综艺 | 2 | 1 | -1 | 50.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 3 | -1 | 25.0% | 0 |
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

- unique channels dropped: baseline=206 current=160
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive']
