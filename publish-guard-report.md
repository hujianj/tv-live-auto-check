# Publish guard report

Status: ok
Baseline lines: 2042
Current lines: 12
Total drop ratio: 99.4%
Relative baseline comparable: False
Relative guard migration: source permission policy migrated 0->1 with domestic Chinese scope; absolute core coverage still required
Coverage metric: canonical_channels
Independent channel coverage: {'total': 12, 'groups': {'央视频道': 7, '地方频道': 3, '港澳台频道': 2}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 128 | 7 | -121 | 94.5% | 1 |
| 卫视频道 | 189 | 0 | -189 | 100.0% | 1 |
| 地方频道 | 395 | 3 | -392 | 99.2% | 1 |
| 影视剧场 | 167 | 0 | -167 | 100.0% | 0 |
| 少儿动漫 | 24 | 0 | -24 | 100.0% | 0 |
| 体育纪实 | 63 | 0 | -63 | 100.0% | 0 |
| 音乐综艺 | 23 | 0 | -23 | 100.0% | 0 |
| 生活休闲 | 93 | 0 | -93 | 100.0% | 0 |
| 综合娱乐 | 880 | 0 | -880 | 100.0% | 0 |
| 港澳台频道 | 80 | 2 | -78 | 97.5% | 0 |
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

- no comparable independent-channel baseline; absolute coverage remains enforced
- unique channels 12 < minimum 29
- group 央视频道 unique channels 7 < minimum 18
- group 卫视频道 unique channels 0 < minimum 10
- group 卫视频道 count 0 < minimum 1
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
