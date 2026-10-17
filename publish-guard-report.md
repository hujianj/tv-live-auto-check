# Publish guard report

Status: ok
Baseline lines: 367
Current lines: 314
Total drop ratio: 14.4%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 288, 'groups': {'央视频道': 6, '卫视频道': 15, '地方频道': 132, '影视剧场': 63, '少儿动漫': 2, '体育纪实': 17, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 21 | 6 | -15 | 71.4% | 1 |
| 卫视频道 | 47 | 21 | -26 | 55.3% | 1 |
| 地方频道 | 158 | 150 | -8 | 5.1% | 1 |
| 影视剧场 | 65 | 63 | -2 | 3.1% | 0 |
| 少儿动漫 | 4 | 2 | -2 | 50.0% | 0 |
| 体育纪实 | 19 | 19 | 0 | 0.0% | 0 |
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
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_douyu
- Candidate sources parsed empty (non-blocking): none

## Warnings

- group 央视频道 unique channels 6 < minimum 18
- group 央视频道 unique channels dropped: baseline=18 current=6
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_douyu']
