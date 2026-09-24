# Publish guard report

Status: ok
Baseline lines: 340
Current lines: 249
Total drop ratio: 26.8%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 227, 'groups': {'央视频道': 17, '卫视频道': 12, '地方频道': 127, '影视剧场': 2, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 48, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 22 | 19 | -3 | 13.6% | 1 |
| 卫视频道 | 20 | 16 | -4 | 20.0% | 1 |
| 地方频道 | 160 | 141 | -19 | 11.9% | 1 |
| 影视剧场 | 65 | 2 | -63 | 96.9% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 48 | -3 | 5.9% | 0 |
| 港澳台频道 | 1 | 2 | 1 | -100.0% | 0 |
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

- unique channels dropped: baseline=308 current=227
- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
