# Publish guard report

Status: ok
Baseline lines: 308
Current lines: 302
Total drop ratio: 1.9%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 278, 'groups': {'央视频道': 18, '卫视频道': 13, '地方频道': 114, '影视剧场': 63, '少儿动漫': 1, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 22 | 23 | 1 | -4.5% | 1 |
| 卫视频道 | 18 | 18 | 0 | 0.0% | 1 |
| 地方频道 | 132 | 126 | -6 | 4.5% | 1 |
| 影视剧场 | 63 | 63 | 0 | 0.0% | 0 |
| 少儿动漫 | 2 | 1 | -1 | 50.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 51 | 0 | 0.0% | 0 |
| 港澳台频道 | 1 | 1 | 0 | 0.0% | 0 |
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
