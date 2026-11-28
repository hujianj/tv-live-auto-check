# Publish guard report

Status: ok
Baseline lines: 277
Current lines: 268
Total drop ratio: 3.2%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 229, 'groups': {'央视频道': 17, '卫视频道': 19, '地方频道': 101, '影视剧场': 64, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 9}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 28 | 28 | 0 | 0.0% | 1 |
| 卫视频道 | 28 | 26 | -2 | 7.1% | 1 |
| 地方频道 | 128 | 119 | -9 | 7.0% | 1 |
| 影视剧场 | 65 | 65 | 0 | 0.0% | 0 |
| 少儿动漫 | 1 | 2 | 1 | -100.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 0 | 1 | 1 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 9 | 9 | 0 | 0.0% | 0 |
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
