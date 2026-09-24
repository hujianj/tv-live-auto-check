# Publish guard report

Status: ok
Baseline lines: 302
Current lines: 340
Total drop ratio: -12.6%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 308, 'groups': {'央视频道': 17, '卫视频道': 14, '地方频道': 141, '影视剧场': 65, '少儿动漫': 2, '体育纪实': 16, '音乐综艺': 1, '综合娱乐': 51, '港澳台频道': 1}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 23 | 22 | -1 | 4.3% | 1 |
| 卫视频道 | 18 | 20 | 2 | -11.1% | 1 |
| 地方频道 | 126 | 160 | 34 | -27.0% | 1 |
| 影视剧场 | 63 | 65 | 2 | -3.2% | 0 |
| 少儿动漫 | 1 | 2 | 1 | -100.0% | 0 |
| 体育纪实 | 18 | 18 | 0 | 0.0% | 0 |
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
- Candidate source failures (non-blocking): mursor_yy, mursor_bililive, freetv_huya
- Candidate sources parsed empty (non-blocking): none

## Warnings

- group 央视频道 unique channels 17 < minimum 18
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya']
