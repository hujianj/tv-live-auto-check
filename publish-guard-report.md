# Publish guard report

Status: ok
Baseline lines: 213
Current lines: 293
Total drop ratio: -37.6%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 259, 'groups': {'央视频道': 17, '卫视频道': 15, '地方频道': 135, '影视剧场': 21, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 48, '港澳台频道': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 24 | 23 | -1 | 4.2% | 1 |
| 卫视频道 | 16 | 21 | 5 | -31.2% | 1 |
| 地方频道 | 75 | 155 | 80 | -106.7% | 1 |
| 影视剧场 | 63 | 21 | -42 | 66.7% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 18 | -4 | 18.2% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 7 | 48 | 41 | -585.7% | 0 |
| 港澳台频道 | 3 | 4 | 1 | -33.3% | 0 |
| 海外华语频道 | 0 | 0 | 0 | n/a | 0 |

## Source health

- Enabled source failures: none
- Enabled sources fetched but zero parsed: none
- Enabled sources unavailable for guard purposes: none
- Recovery source failures (non-blocking): none
- Recovery sources fetched but zero parsed (non-blocking): none
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_huya
- Candidate sources parsed empty (non-blocking): none

## Warnings

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya']
