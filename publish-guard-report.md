# Publish guard report

Status: ok
Baseline lines: 302
Current lines: 117
Total drop ratio: 61.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 115, 'groups': {'央视频道': 16, '卫视频道': 1, '地方频道': 28, '影视剧场': 45, '体育纪实': 21, '音乐综艺': 1, '综合娱乐': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 20 | 17 | -3 | 15.0% | 1 |
| 卫视频道 | 13 | 2 | -11 | 84.6% | 1 |
| 地方频道 | 133 | 28 | -105 | 78.9% | 1 |
| 影视剧场 | 63 | 45 | -18 | 28.6% | 0 |
| 少儿动漫 | 2 | 0 | -2 | 100.0% | 0 |
| 体育纪实 | 18 | 21 | 3 | -16.7% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 3 | -48 | 94.1% | 0 |
| 港澳台频道 | 1 | 0 | -1 | 100.0% | 0 |
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

- unique channels dropped: baseline=283 current=115
- group 央视频道 unique channels 16 < minimum 18
- group 卫视频道 unique channels 1 < minimum 10
- group 卫视频道 unique channels dropped: baseline=11 current=1
- group 地方频道 unique channels dropped: baseline=121 current=28
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
