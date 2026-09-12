# Publish guard report

Status: ok
Baseline lines: 167
Current lines: 199
Total drop ratio: -19.2%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 175, 'groups': {'央视频道': 18, '卫视频道': 12, '地方频道': 71, '影视剧场': 42, '少儿动漫': 2, '体育纪实': 20, '音乐综艺': 1, '综合娱乐': 6, '港澳台频道': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 24 | 21 | -3 | 12.5% | 1 |
| 卫视频道 | 19 | 16 | -3 | 15.8% | 1 |
| 地方频道 | 73 | 86 | 13 | -17.8% | 1 |
| 影视剧场 | 20 | 42 | 22 | -110.0% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 22 | 22 | 0 | 0.0% | 0 |
| 音乐综艺 | 0 | 1 | 1 | n/a | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 4 | 6 | 2 | -50.0% | 0 |
| 港澳台频道 | 3 | 3 | 0 | 0.0% | 0 |
| 海外华语频道 | 0 | 0 | 0 | n/a | 0 |

## Source health

- Enabled source failures: none
- Enabled sources fetched but zero parsed: none
- Enabled sources unavailable for guard purposes: none
- Recovery source failures (non-blocking): none
- Recovery sources fetched but zero parsed (non-blocking): none
- Candidate source failures (non-blocking): epg_cn, mursor_yy, mursor_bililive, freetv_huya, freetv_douyu
- Candidate sources parsed empty (non-blocking): none

## Warnings

- candidate-only sources unavailable (non-blocking): ['epg_cn', 'mursor_yy', 'mursor_bililive', 'freetv_huya', 'freetv_douyu']
