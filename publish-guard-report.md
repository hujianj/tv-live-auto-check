# Publish guard report

Status: ok
Baseline lines: 268
Current lines: 184
Total drop ratio: 31.3%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 142, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 104, '体育纪实': 1, '音乐综艺': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 29 | 31 | 2 | -6.9% | 1 |
| 卫视频道 | 27 | 27 | 0 | 0.0% | 1 |
| 地方频道 | 137 | 124 | -13 | 9.5% | 1 |
| 影视剧场 | 64 | 0 | -64 | 100.0% | 0 |
| 少儿动漫 | 2 | 0 | -2 | 100.0% | 0 |
| 体育纪实 | 3 | 1 | -2 | 66.7% | 0 |
| 音乐综艺 | 2 | 1 | -1 | 50.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 0 | -4 | 100.0% | 0 |
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

- unique channels dropped: baseline=222 current=142
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
