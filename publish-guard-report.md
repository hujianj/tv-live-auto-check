# Publish guard report

Status: ok
Baseline lines: 274
Current lines: 268
Total drop ratio: 2.2%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 228, 'groups': {'央视频道': 16, '卫视频道': 19, '地方频道': 107, '影视剧场': 64, '少儿动漫': 1, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 28 | 22 | -6 | 21.4% | 1 |
| 卫视频道 | 28 | 27 | -1 | 3.6% | 1 |
| 地方频道 | 131 | 131 | 0 | 0.0% | 1 |
| 影视剧场 | 65 | 64 | -1 | 1.5% | 0 |
| 少儿动漫 | 2 | 1 | -1 | 50.0% | 0 |
| 体育纪实 | 15 | 18 | 3 | -20.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
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

- group 央视频道 unique channels 16 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
