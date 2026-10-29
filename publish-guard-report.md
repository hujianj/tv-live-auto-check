# Publish guard report

Status: ok
Baseline lines: 275
Current lines: 218
Total drop ratio: 20.7%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 182, 'groups': {'央视频道': 16, '卫视频道': 18, '地方频道': 123, '影视剧场': 3, '少儿动漫': 1, '体育纪实': 19, '音乐综艺': 1, '综合娱乐': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 29 | 23 | -6 | 20.7% | 1 |
| 卫视频道 | 25 | 25 | 0 | 0.0% | 1 |
| 地方频道 | 151 | 143 | -8 | 5.3% | 1 |
| 影视剧场 | 3 | 3 | 0 | 0.0% | 0 |
| 少儿动漫 | 1 | 1 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 21 | 3 | -16.7% | 0 |
| 音乐综艺 | 1 | 1 | 0 | 0.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 46 | 1 | -45 | 97.8% | 0 |
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

- unique channels dropped: baseline=233 current=182
- group 央视频道 unique channels 16 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
