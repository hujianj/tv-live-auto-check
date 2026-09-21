# Publish guard report

Status: ok
Baseline lines: 138
Current lines: 336
Total drop ratio: -143.5%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 306, 'groups': {'央视频道': 17, '卫视频道': 13, '地方频道': 142, '影视剧场': 64, '少儿动漫': 1, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 17 | 21 | 4 | -23.5% | 1 |
| 卫视频道 | 12 | 17 | 5 | -41.7% | 1 |
| 地方频道 | 77 | 162 | 85 | -110.4% | 1 |
| 影视剧场 | 2 | 64 | 62 | -3100.0% | 0 |
| 少儿动漫 | 2 | 1 | -1 | 50.0% | 0 |
| 体育纪实 | 23 | 18 | -5 | 21.7% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 51 | 47 | -1175.0% | 0 |
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

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
