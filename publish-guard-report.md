# Publish guard report

Status: ok
Baseline lines: 268
Current lines: 246
Total drop ratio: 8.2%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 208, 'groups': {'央视频道': 17, '卫视频道': 18, '地方频道': 93, '影视剧场': 57, '少儿动漫': 2, '体育纪实': 18, '综合娱乐': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 22 | 28 | 6 | -27.3% | 1 |
| 卫视频道 | 27 | 26 | -1 | 3.7% | 1 |
| 地方频道 | 131 | 110 | -21 | 16.0% | 1 |
| 影视剧场 | 64 | 57 | -7 | 10.9% | 0 |
| 少儿动漫 | 1 | 2 | 1 | -100.0% | 0 |
| 体育纪实 | 18 | 20 | 2 | -11.1% | 0 |
| 音乐综艺 | 1 | 0 | -1 | 100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 3 | -1 | 25.0% | 0 |
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
