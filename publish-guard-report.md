# Publish guard report

Status: ok
Baseline lines: 294
Current lines: 238
Total drop ratio: 19.0%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 190, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 130, '影视剧场': 2, '少儿动漫': 1, '体育纪实': 20, '音乐综艺': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 29 | 32 | 3 | -10.3% | 1 |
| 卫视频道 | 27 | 28 | 1 | -3.7% | 1 |
| 地方频道 | 167 | 153 | -14 | 8.4% | 1 |
| 影视剧场 | 3 | 2 | -1 | 33.3% | 0 |
| 少儿动漫 | 1 | 1 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 21 | 3 | -16.7% | 0 |
| 音乐综艺 | 2 | 1 | -1 | 50.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 46 | 0 | -46 | 100.0% | 0 |
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

- unique channels dropped: baseline=246 current=190
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
