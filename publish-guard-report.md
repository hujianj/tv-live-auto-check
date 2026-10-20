# Publish guard report

Status: ok
Baseline lines: 302
Current lines: 318
Total drop ratio: -5.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 291, 'groups': {'央视频道': 8, '卫视频道': 11, '地方频道': 136, '影视剧场': 64, '少儿动漫': 2, '体育纪实': 17, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 20 | 8 | -12 | 60.0% | 1 |
| 卫视频道 | 14 | 15 | 1 | -7.1% | 1 |
| 地方频道 | 131 | 157 | 26 | -19.8% | 1 |
| 影视剧场 | 63 | 64 | 1 | -1.6% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
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
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_huya, freetv_douyu
- Candidate sources parsed empty (non-blocking): none

## Warnings

- group 央视频道 unique channels 8 < minimum 18
- group 央视频道 unique channels dropped: baseline=17 current=8
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
