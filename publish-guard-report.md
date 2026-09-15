# Publish guard report

Status: ok
Baseline lines: 350
Current lines: 315
Total drop ratio: 10.0%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 287, 'groups': {'央视频道': 18, '卫视频道': 14, '地方频道': 137, '影视剧场': 46, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 50, '港澳台频道': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 33 | 21 | -12 | 36.4% | 1 |
| 卫视频道 | 25 | 18 | -7 | 28.0% | 1 |
| 地方频道 | 154 | 156 | 2 | -1.3% | 1 |
| 影视剧场 | 63 | 46 | -17 | 27.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 50 | -1 | 2.0% | 0 |
| 港澳台频道 | 3 | 3 | 0 | 0.0% | 0 |
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

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
