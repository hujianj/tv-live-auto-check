# Publish guard report

Status: ok
Baseline lines: 276
Current lines: 275
Total drop ratio: 0.4%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 233, 'groups': {'央视频道': 17, '卫视频道': 18, '地方频道': 130, '影视剧场': 3, '少儿动漫': 1, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 46, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 30 | 29 | -1 | 3.3% | 1 |
| 卫视频道 | 26 | 25 | -1 | 3.8% | 1 |
| 地方频道 | 150 | 151 | 1 | -0.7% | 1 |
| 影视剧场 | 3 | 3 | 0 | 0.0% | 0 |
| 少儿动漫 | 1 | 1 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 46 | 46 | 0 | 0.0% | 0 |
| 港澳台频道 | 1 | 1 | 0 | 0.0% | 0 |
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
