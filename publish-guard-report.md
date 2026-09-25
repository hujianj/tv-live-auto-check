# Publish guard report

Status: ok
Baseline lines: 249
Current lines: 303
Total drop ratio: -21.7%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 281, 'groups': {'央视频道': 16, '卫视频道': 12, '地方频道': 119, '影视剧场': 63, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 19 | 21 | 2 | -10.5% | 1 |
| 卫视频道 | 16 | 16 | 0 | 0.0% | 1 |
| 地方频道 | 141 | 130 | -11 | 7.8% | 1 |
| 影视剧场 | 2 | 63 | 61 | -3050.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 48 | 51 | 3 | -6.2% | 0 |
| 港澳台频道 | 2 | 1 | -1 | 50.0% | 0 |
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

- group 央视频道 unique channels 16 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_douyu']
