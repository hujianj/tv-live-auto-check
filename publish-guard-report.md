# Publish guard report

Status: ok
Baseline lines: 293
Current lines: 286
Total drop ratio: 2.4%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 237, 'groups': {'央视频道': 17, '卫视频道': 19, '地方频道': 114, '影视剧场': 65, '少儿动漫': 2, '体育纪实': 16, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 36 | 28 | -8 | 22.2% | 1 |
| 卫视频道 | 30 | 30 | 0 | 0.0% | 1 |
| 地方频道 | 138 | 139 | 1 | -0.7% | 1 |
| 影视剧场 | 64 | 65 | 1 | -1.6% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 0 | -1 | 100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 4 | 0 | 0.0% | 0 |
| 港澳台频道 | 0 | 0 | 0 | n/a | 0 |
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
