# Publish guard report

Status: ok
Baseline lines: 282
Current lines: 216
Total drop ratio: 23.4%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 168, 'groups': {'央视频道': 17, '卫视频道': 18, '地方频道': 109, '影视剧场': 2, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 32 | 29 | -3 | 9.4% | 1 |
| 卫视频道 | 27 | 28 | 1 | -3.7% | 1 |
| 地方频道 | 132 | 133 | 1 | -0.8% | 1 |
| 影视剧场 | 65 | 2 | -63 | 96.9% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 2 | 1 | -1 | 50.0% | 0 |
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

- unique channels dropped: baseline=233 current=168
- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
