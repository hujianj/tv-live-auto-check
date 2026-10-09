# Publish guard report

Status: ok
Baseline lines: 326
Current lines: 274
Total drop ratio: 16.0%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 253, 'groups': {'央视频道': 16, '卫视频道': 13, '地方频道': 105, '影视剧场': 63, '少儿动漫': 2, '体育纪实': 2, '音乐综艺': 1, '综合娱乐': 50, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 20 | 19 | -1 | 5.0% | 1 |
| 卫视频道 | 17 | 19 | 2 | -11.8% | 1 |
| 地方频道 | 152 | 115 | -37 | 24.3% | 1 |
| 影视剧场 | 64 | 63 | -1 | 1.6% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 4 | -14 | 77.8% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 50 | -1 | 2.0% | 0 |
| 港澳台频道 | 1 | 1 | 0 | 0.0% | 0 |
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
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
