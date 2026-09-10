# Publish guard report

Status: ok
Baseline lines: 317
Current lines: 213
Total drop ratio: 32.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 192, 'groups': {'央视频道': 18, '卫视频道': 12, '地方频道': 66, '影视剧场': 63, '少儿动漫': 2, '体育纪实': 20, '音乐综艺': 1, '综合娱乐': 7, '港澳台频道': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 25 | 24 | -1 | 4.0% | 1 |
| 卫视频道 | 23 | 16 | -7 | 30.4% | 1 |
| 地方频道 | 131 | 75 | -56 | 42.7% | 1 |
| 影视剧场 | 62 | 63 | 1 | -1.6% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 22 | 4 | -22.2% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 7 | -44 | 86.3% | 0 |
| 港澳台频道 | 4 | 3 | -1 | 25.0% | 0 |
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

- unique channels dropped: baseline=292 current=192
- group 地方频道 unique channels dropped: baseline=121 current=66
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
