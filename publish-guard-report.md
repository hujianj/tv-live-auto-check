# Publish guard report

Status: ok
Baseline lines: 238
Current lines: 333
Total drop ratio: -39.9%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 289, 'groups': {'央视频道': 18, '卫视频道': 18, '地方频道': 135, '影视剧场': 48, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 2, '综合娱乐': 49, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 32 | 30 | -2 | 6.2% | 1 |
| 卫视频道 | 28 | 25 | -3 | 10.7% | 1 |
| 地方频道 | 153 | 158 | 5 | -3.3% | 1 |
| 影视剧场 | 2 | 48 | 46 | -2300.0% | 0 |
| 少儿动漫 | 1 | 2 | 1 | -100.0% | 0 |
| 体育纪实 | 21 | 18 | -3 | 14.3% | 0 |
| 音乐综艺 | 1 | 2 | 1 | -100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 0 | 49 | 49 | n/a | 0 |
| 港澳台频道 | 0 | 1 | 1 | n/a | 0 |
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

- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
