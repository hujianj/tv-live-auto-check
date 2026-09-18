# Publish guard report

Status: ok
Baseline lines: 345
Current lines: 316
Total drop ratio: 8.4%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 285, 'groups': {'央视频道': 17, '卫视频道': 13, '地方频道': 137, '影视剧场': 48, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 50, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 24 | 19 | -5 | 20.8% | 1 |
| 卫视频道 | 19 | 19 | 0 | 0.0% | 1 |
| 地方频道 | 163 | 158 | -5 | 3.1% | 1 |
| 影视剧场 | 64 | 48 | -16 | 25.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 50 | -1 | 2.0% | 0 |
| 港澳台频道 | 3 | 1 | -2 | 66.7% | 0 |
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

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_douyu']
