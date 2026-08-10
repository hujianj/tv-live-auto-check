# Publish guard report

Status: ok
Baseline lines: 2552
Current lines: 1992
Total drop ratio: 21.9%
Relative baseline comparable: False
Relative guard migration: baseline predates broadcast live-progress verification

## Group deltas

| Group | Baseline | Current | Delta | Drop | Minimum |
|---|---:|---:|---:|---:|---:|
| 央视频道 | 128 | 127 | -1 | 0.8% | 90 |
| 卫视频道 | 181 | 181 | 0 | 0.0% | 120 |
| 地方频道 | 707 | 335 | -372 | 52.6% | 250 |
| 影视剧场 | 179 | 180 | 1 | -0.6% | 0 |
| 少儿动漫 | 25 | 24 | -1 | 4.0% | 0 |
| 体育纪实 | 71 | 67 | -4 | 5.6% | 0 |
| 音乐综艺 | 23 | 24 | 1 | -4.3% | 0 |
| 生活休闲 | 91 | 92 | 1 | -1.1% | 0 |
| 综合娱乐 | 847 | 881 | 34 | -4.0% | 0 |
| 港澳台频道 | 81 | 81 | 0 | 0.0% | 0 |
| 海外华语频道 | 219 | 0 | -219 | 100.0% | 0 |

## Source health

- Enabled source failures: none
- Enabled sources fetched but zero parsed: none
- Recovery source failures (non-blocking): freetv_huya, pizazz_ai_txt, pizazz_ai_m3u, gitee_dsy, freetv_douyu
- Recovery sources fetched but zero parsed (non-blocking): migu_interface

## Warnings

- relative drop guards skipped for one policy migration: baseline predates broadcast live-progress verification
- recovery sources unavailable (non-blocking): ['freetv_huya', 'pizazz_ai_txt', 'pizazz_ai_m3u', 'gitee_dsy', 'freetv_douyu']
- recovery sources fetched but parsed no supported streams (non-blocking): ['migu_interface']
