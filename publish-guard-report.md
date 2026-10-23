# Publish guard report

Status: ok
Baseline lines: 117
Current lines: 317
Total drop ratio: -170.9%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 291, 'groups': {'央视频道': 16, '卫视频道': 9, '地方频道': 132, '影视剧场': 64, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 50, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 17 | 18 | 1 | -5.9% | 1 |
| 卫视频道 | 2 | 11 | 9 | -450.0% | 1 |
| 地方频道 | 28 | 152 | 124 | -442.9% | 1 |
| 影视剧场 | 45 | 64 | 19 | -42.2% | 0 |
| 少儿动漫 | 0 | 2 | 2 | n/a | 0 |
| 体育纪实 | 21 | 18 | -3 | 14.3% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 3 | 50 | 47 | -1566.7% | 0 |
| 港澳台频道 | 0 | 1 | 1 | n/a | 0 |
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

- group 央视频道 unique channels 16 < minimum 18
- group 卫视频道 unique channels 9 < minimum 10
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
