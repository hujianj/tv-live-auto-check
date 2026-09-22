# Publish guard report

Status: ok
Baseline lines: 315
Current lines: 300
Total drop ratio: 4.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 285, 'groups': {'央视频道': 17, '卫视频道': 15, '地方频道': 125, '影视剧场': 62, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 48, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 18 | 22 | 4 | -22.2% | 1 |
| 卫视频道 | 20 | 20 | 0 | 0.0% | 1 |
| 地方频道 | 155 | 128 | -27 | 17.4% | 1 |
| 影视剧场 | 49 | 62 | 13 | -26.5% | 0 |
| 少儿动漫 | 2 | 0 | -2 | 100.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 50 | 48 | -2 | 4.0% | 0 |
| 港澳台频道 | 2 | 1 | -1 | 50.0% | 0 |
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
