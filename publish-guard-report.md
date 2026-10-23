# Publish guard report

Status: ok
Baseline lines: 317
Current lines: 277
Total drop ratio: 12.6%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 260, 'groups': {'央视频道': 16, '卫视频道': 10, '地方频道': 120, '影视剧场': 46, '少儿动漫': 2, '体育纪实': 15, '音乐综艺': 1, '综合娱乐': 49, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 18 | 17 | -1 | 5.6% | 1 |
| 卫视频道 | 11 | 14 | 3 | -27.3% | 1 |
| 地方频道 | 152 | 132 | -20 | 13.2% | 1 |
| 影视剧场 | 64 | 46 | -18 | 28.1% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 15 | -3 | 16.7% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 50 | 49 | -1 | 2.0% | 0 |
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

- group 央视频道 unique channels 16 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya']
