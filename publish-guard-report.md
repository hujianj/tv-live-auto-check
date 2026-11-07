# Publish guard report

Status: ok
Baseline lines: 184
Current lines: 283
Total drop ratio: -53.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 235, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 110, '影视剧场': 65, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 2, '综合娱乐': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 31 | 32 | 1 | -3.2% | 1 |
| 卫视频道 | 27 | 26 | -1 | 3.7% | 1 |
| 地方频道 | 124 | 134 | 10 | -8.1% | 1 |
| 影视剧场 | 0 | 65 | 65 | n/a | 0 |
| 少儿动漫 | 0 | 2 | 2 | n/a | 0 |
| 体育纪实 | 1 | 18 | 17 | -1700.0% | 0 |
| 音乐综艺 | 1 | 2 | 1 | -100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 0 | 4 | 4 | n/a | 0 |
| 港澳台频道 | 0 | 0 | 0 | n/a | 0 |
| 海外华语频道 | 0 | 0 | 0 | n/a | 0 |

## Source health

- Enabled source failures: none
- Enabled sources fetched but zero parsed: none
- Enabled sources unavailable for guard purposes: none
- Recovery source failures (non-blocking): none
- Recovery sources fetched but zero parsed (non-blocking): none
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_douyu
- Candidate sources parsed empty (non-blocking): none

## Warnings

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_douyu']
