# IPTV source verification report

Generated: 2026-10-29 00:01:54
Generated UTC: 2026-10-29T00:01:54Z
Generated Beijing: 2026-10-29 08:01:54 Asia/Shanghai
Elapsed: 80.3s
Sources configured: 43 (enabled=34, recovery=2, disabled=7)
Sources probed: 36
Sources fetched OK: 32
Sources with parsed rows (before policy filters): 28
Sources with media-eligible candidates: 7
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 29397
Policy-excluded candidates (not media-checked): 28642
Eligible candidates before URL deduplication: 755
Unique name+URL candidates: 453
Unique stream URLs: 439
Checked unique stream URLs: 439
Checked all unique URLs: True
Playable channel names: 228
Playable unique URLs: 288
Playable name+URL lines: 300
Playable URLs found (legacy line count): 300
Pre-curated published playable lines: 300

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | YES | 6820 | 0 | 507678 | False |  |
| zbds_iptv4_txt | enabled | OK | YES | 358 | 348 | 31499 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 277 | 270 | 64233 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10644 | 14 | 2579164 | False |  |
| epg_cn | enabled | OK | YES | 655 | 0 | 213741 | False |  |
| epg_hk | enabled | OK | YES | 13 | 0 | 4437 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 22 | 0 | 9001 | False |  |
| iptv_org_tw | enabled | OK | YES | 31 | 0 | 5925 | False |  |
| epg_sg | enabled | OK | YES | 1 | 0 | 318 | False |  |
| epg_my | enabled | OK | YES | 4 | 0 | 1330 | False |  |
| free_tv_world | enabled | OK | YES | 2039 | 20 | 542812 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| freetv_douyu | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| iptv_org_cn | enabled | OK | YES | 127 | 14 | 30080 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 35784 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |
| oktv_comprehensive_php | enabled | OK | YES | 188 | 31 | 42900 | False |  |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 261 |
| oktv_comprehensive_php | 21 |
| iptv_org_cn | 11 |
| free_tv_world | 7 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / iptv_org_cn
- 央视频道 / CCTV-1 / oktv_comprehensive_php
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-12 / iptv_org_cn
- 央视频道 / CCTV-13 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-14 / free_tv_world
- 央视频道 / CCTV-14 / oktv_comprehensive_php
- 央视频道 / CCTV-15 / iptv_org_cn
- 央视频道 / CCTV-15 / oktv_comprehensive_php
- 央视频道 / CCTV-16 / oktv_comprehensive_php
- 央视频道 / CCTV-17 / free_tv_world
- 央视频道 / CCTV-17 / oktv_comprehensive_php
- 央视频道 / CCTV-2 / iptv_org_cn
- 央视频道 / CCTV-2 / oktv_comprehensive_php
- 央视频道 / CCTV-3 / iptv_org_cn
- 央视频道 / CCTV-3 / oktv_comprehensive_php
- 央视频道 / CCTV-4 / oktv_comprehensive_php
- 央视频道 / CCTV-4中文国际（亚） / free_tv_world
- 央视频道 / CCTV-4中文国际（欧） / free_tv_world
- 央视频道 / CCTV-4亚洲 / oktv_comprehensive_php
- 央视频道 / CCTV-6 / free_tv_world
- 央视频道 / CCTV-6 / oktv_comprehensive_php
- 央视频道 / CCTV-7 / iptv_org_cn
- 央视频道 / CCTV-8 / iptv_org_cn
- 央视频道 / CCTV-8 / oktv_comprehensive_php
- 央视频道 / CCTV-9 / free_tv_world
- 央视频道 / CCTV-9 / iptv_org_cn
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / oktv_comprehensive_php
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 内蒙古卫视 / zbds_iptv4_txt
- 卫视频道 / 北京卫视 / oktv_comprehensive_php
- 卫视频道 / 大湾区卫视 / zbds_iptv4_txt
- 卫视频道 / 天津卫视 / oktv_comprehensive_php
- 卫视频道 / 安多卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / oktv_comprehensive_php
- 卫视频道 / 山东卫视 / oktv_comprehensive_php
- 卫视频道 / 山西卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / oktv_comprehensive_php
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 江苏卫视 / oktv_comprehensive_php
- 卫视频道 / 江西卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / oktv_comprehensive_php
- 卫视频道 / 深圳卫视 / oktv_comprehensive_php
- 卫视频道 / 湖南卫视 / zbds_iptv4_txt
- 卫视频道 / 湖南卫视 / oktv_comprehensive_php
- 地方频道 / FZTV-1News新闻综合频道 / free_tv_world
- 地方频道 / 三明新闻综合 / zbds_iptv4_txt
- 地方频道 / 三明新闻综合 / zbds_iptv4_txt
- 地方频道 / 上海第一财经 / zbds_iptv4_txt
- 地方频道 / 上虞新闻综合 / zbds_iptv4_txt
- 地方频道 / 东莞新闻综合 / zbds_iptv4_txt
- 地方频道 / 中国蓝新闻 / zbds_iptv4_txt
- 地方频道 / 乐至综合 / zbds_iptv4_txt
- 地方频道 / 云和新闻综合 / zbds_iptv4_txt
- 地方频道 / 云和新闻综合 / zbds_iptv4_txt
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 井研综合 / zbds_iptv4_txt
- 地方频道 / 亳州农村 / zbds_iptv4_txt
- 地方频道 / 亳州农村 / zbds_iptv4_txt
- 地方频道 / 余姚姚江文化 / zbds_iptv4_txt
- 地方频道 / 余姚姚江文化 / zbds_iptv4_txt
- 地方频道 / 余姚新闻综合 / zbds_iptv4_txt
- 地方频道 / 余姚新闻综合 / zbds_iptv4_txt
- 地方频道 / 余姚综合 / zbds_iptv4_txt
- 地方频道 / 余姚综合 / zbds_iptv4_txt
