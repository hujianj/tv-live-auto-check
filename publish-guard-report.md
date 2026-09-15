# Publish guard report

Status: ok
Baseline lines: 315
Current lines: 228
Total drop ratio: 27.6%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 200, 'groups': {'央视频道': 19, '卫视频道': 14, '地方频道': 71, '影视剧场': 63, '少儿动漫': 2, '体育纪实': 20, '音乐综艺': 1, '综合娱乐': 7, '港澳台频道': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 21 | 25 | 4 | -19.0% | 1 |
| 卫视频道 | 18 | 18 | 0 | 0.0% | 1 |
| 地方频道 | 156 | 87 | -69 | 44.2% | 1 |
| 影视剧场 | 46 | 63 | 17 | -37.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 22 | 4 | -22.2% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 50 | 7 | -43 | 86.0% | 0 |
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

- unique channels dropped: baseline=287 current=200
- group 地方频道 unique channels dropped: baseline=137 current=71
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
