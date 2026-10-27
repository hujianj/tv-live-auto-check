# Publish guard report

Status: ok
Baseline lines: 247
Current lines: 229
Total drop ratio: 7.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 208, 'groups': {'央视频道': 18, '卫视频道': 11, '地方频道': 113, '影视剧场': 2, '少儿动漫': 1, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 45, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 21 | 21 | 0 | 0.0% | 1 |
| 卫视频道 | 15 | 15 | 0 | 0.0% | 1 |
| 地方频道 | 142 | 125 | -17 | 12.0% | 1 |
| 影视剧场 | 2 | 2 | 0 | 0.0% | 0 |
| 少儿动漫 | 1 | 1 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 46 | 45 | -1 | 2.2% | 0 |
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

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya']
