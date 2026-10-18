# Publish guard report

Status: ok
Baseline lines: 320
Current lines: 259
Total drop ratio: 19.1%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 232, 'groups': {'央视频道': 15, '卫视频道': 11, '地方频道': 136, '影视剧场': 2, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 48, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 21 | 16 | -5 | 23.8% | 1 |
| 卫视频道 | 23 | 15 | -8 | 34.8% | 1 |
| 地方频道 | 137 | 156 | 19 | -13.9% | 1 |
| 影视剧场 | 64 | 2 | -62 | 96.9% | 0 |
| 少儿动漫 | 3 | 2 | -1 | 33.3% | 0 |
| 体育纪实 | 19 | 18 | -1 | 5.3% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 48 | -3 | 5.9% | 0 |
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

- unique channels dropped: baseline=295 current=232
- group 央视频道 unique channels 15 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
