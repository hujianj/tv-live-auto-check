# Publish guard report

Status: ok
Baseline lines: 272
Current lines: 268
Total drop ratio: 1.5%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 222, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 113, '影视剧场': 64, '少儿动漫': 2, '体育纪实': 1, '音乐综艺': 2, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 31 | 29 | -2 | 6.5% | 1 |
| 卫视频道 | 27 | 27 | 0 | 0.0% | 1 |
| 地方频道 | 130 | 137 | 7 | -5.4% | 1 |
| 影视剧场 | 60 | 64 | 4 | -6.7% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 3 | -15 | 83.3% | 0 |
| 音乐综艺 | 2 | 2 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 2 | 4 | 2 | -100.0% | 0 |
| 港澳台频道 | 0 | 0 | 0 | n/a | 0 |
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
