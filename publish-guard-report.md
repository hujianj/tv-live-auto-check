# Publish guard report

Status: ok
Baseline lines: 140
Current lines: 331
Total drop ratio: -136.4%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 300, 'groups': {'央视频道': 17, '卫视频道': 14, '地方频道': 131, '影视剧场': 66, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 17 | 20 | 3 | -17.6% | 1 |
| 卫视频道 | 11 | 20 | 9 | -81.8% | 1 |
| 地方频道 | 83 | 151 | 68 | -81.9% | 1 |
| 影视剧场 | 2 | 66 | 64 | -3200.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 18 | -4 | 18.2% | 0 |
| 音乐综艺 | 0 | 1 | 1 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 3 | 51 | 48 | -1600.0% | 0 |
| 港澳台频道 | 0 | 2 | 2 | n/a | 0 |
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

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
