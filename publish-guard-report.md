# Publish guard report

Status: ok
Baseline lines: 344
Current lines: 167
Total drop ratio: 51.5%
Relative baseline comparable: True
Relative guard migration: none
Coverage metric: canonical_channels
Independent channel coverage: {'total': 143, 'groups': {'央视频道': 19, '卫视频道': 15, '地方频道': 60, '影视剧场': 20, '少儿动漫': 2, '体育纪实': 20, '综合娱乐': 4, '港澳台频道': 3}}

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 26 | 24 | -2 | 7.7% | 1 |
| 卫视频道 | 23 | 19 | -4 | 17.4% | 1 |
| 地方频道 | 156 | 73 | -83 | 53.2% | 1 |
| 影视剧场 | 63 | 20 | -43 | 68.3% | 0 |
| 少儿动漫 | 2 | 2 | 0 | 0.0% | 0 |
| 体育纪实 | 18 | 22 | 4 | -22.2% | 0 |
| 音乐综艺 | 1 | 0 | -1 | 100.0% | 0 |
| 生活休闲 | 0 | 0 | 0 | n/a | 0 |
| 综合娱乐 | 51 | 4 | -47 | 92.2% | 0 |
| 港澳台频道 | 4 | 3 | -1 | 25.0% | 0 |
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

- unique channels dropped: baseline=310 current=143
- group 地方频道 unique channels dropped: baseline=137 current=60
- candidate-only sources unavailable (non-blocking): ['mursor_yy', 'mursor_bililive', 'freetv_huya']
