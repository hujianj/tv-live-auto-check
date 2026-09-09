# Publish guard report

Status: ok
Baseline lines: 323
Current lines: 169
Total drop ratio: 47.7%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 140, 'groups': {'央视频道': 18, '卫视频道': 13, '地方频道': 62, '影视剧场': 19, '少儿动漫': 2, '体育纪实': 20, '综合娱乐': 4, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 21 | 24 | 3 | -14.3% | 1 |
| 卫视频道 | 20 | 17 | -3 | 15.0% | 1 |
| 地方频道 | 161 | 79 | -82 | 50.9% | 1 |
| 影视剧场 | 46 | 19 | -27 | 58.7% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 22 | 4 | -22.2% | 0 |
| 音乐综艺 | 1 | 0 | -1 | 100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 50 | 4 | -46 | 92.0% | 0 |
| 港澳台频道 | 4 | 2 | -2 | 50.0% | 0 |
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

- unique channels dropped: baseline=292 current=140
- group 地方频道 unique channels dropped: baseline=140 current=62
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
