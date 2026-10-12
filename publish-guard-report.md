# Publish guard report

Status: ok
Baseline lines: 332
Current lines: 140
Total drop ratio: 57.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 118, 'groups': {'央视频道': 16, '卫视频道': 8, '地方频道': 66, '影视剧场': 2, '少儿动漫': 2, '体育纪实': 21, '综合娱乐': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 20 | 17 | -3 | 15.0% | 1 |
| 卫视频道 | 20 | 11 | -9 | 45.0% | 1 |
| 地方频道 | 156 | 83 | -73 | 46.8% | 1 |
| 影视剧场 | 64 | 2 | -62 | 96.9% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 22 | 4 | -22.2% | 0 |
| 音乐综艺 | 1 | 0 | -1 | 100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 50 | 3 | -47 | 94.0% | 0 |
| 港澳台频道 | 1 | 0 | -1 | 100.0% | 0 |
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

- unique channels dropped: baseline=300 current=118
- group 央视频道 unique channels 16 < minimum 18
- group 卫视频道 unique channels 8 < minimum 10
- group 地方频道 unique channels dropped: baseline=135 current=66
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_douyu']
