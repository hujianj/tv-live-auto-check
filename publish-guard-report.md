# Publish guard report

Status: ok
Baseline lines: 169
Current lines: 317
Total drop ratio: -87.6%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 292, 'groups': {'央视频道': 19, '卫视频道': 16, '地方频道': 121, '影视剧场': 62, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 4}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 24 | 25 | 1 | -4.2% | 1 |
| 卫视频道 | 17 | 23 | 6 | -35.3% | 1 |
| 地方频道 | 79 | 131 | 52 | -65.8% | 1 |
| 影视剧场 | 19 | 62 | 43 | -226.3% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 18 | -4 | 18.2% | 0 |
| 音乐综艺 | 0 | 1 | 1 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 51 | 47 | -1175.0% | 0 |
| 港澳台频道 | 2 | 4 | 2 | -100.0% | 0 |
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
