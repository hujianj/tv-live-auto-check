# IPTV source verification report

Generated: 2026-10-14 23:18:43
Generated UTC: 2026-10-14T23:18:43Z
Generated Beijing: 2026-10-15 07:18:43 Asia/Shanghai
Elapsed: 218.1s
Sources configured: 42 (enabled=33, recovery=2, disabled=7)
Sources probed: 35
Sources fetched OK: 31
Sources with parsed rows (before policy filters): 26
Sources with media-eligible candidates: 6
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 24901
Policy-excluded candidates (not media-checked): 23566
Eligible candidates before URL deduplication: 1335
Unique name+URL candidates: 780
Unique stream URLs: 764
Checked unique stream URLs: 764
Checked all unique URLs: True
Playable channel names: 419
Playable unique URLs: 524
Playable name+URL lines: 535
Playable URLs found (legacy line count): 535
Pre-curated published playable lines: 535

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | NO | 0 | 0 | 37 | False | WARN fetched but no parseable HTTP/HTTPS stream candidates |
| zbds_iptv4_txt | enabled | OK | YES | 725 | 713 | 61946 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 525 | 516 | 119448 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10548 | 14 | 2552322 | False |  |
| epg_cn | enabled | OK | YES | 2381 | 0 | 758131 | False |  |
| epg_hk | enabled | OK | YES | 94 | 0 | 29941 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 161 | 0 | 52362 | False |  |
| iptv_org_tw | enabled | OK | YES | 26 | 0 | 4978 | False |  |
| epg_sg | enabled | OK | YES | 17 | 0 | 5177 | False |  |
| epg_my | enabled | OK | YES | 45 | 0 | 14394 | False |  |
| free_tv_world | enabled | OK | YES | 2036 | 20 | 547970 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| freetv_douyu | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| iptv_org_cn | enabled | OK | YES | 125 | 14 | 29674 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 35785 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 520 |
| iptv_org_cn | 8 |
| free_tv_world | 7 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / zbds_iptv4_txt
- 央视频道 / CCTV-1 / zbds_iptv4_txt
- 央视频道 / CCTV-1 / zbds_iptv4_txt
- 央视频道 / CCTV-10 / zbds_iptv4_txt
- 央视频道 / CCTV-10 / zbds_iptv4_txt
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-11 / zbds_iptv4_txt
- 央视频道 / CCTV-11 / zbds_iptv4_txt
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-12 / zbds_iptv4_txt
- 央视频道 / CCTV-12 / zbds_iptv4_txt
- 央视频道 / CCTV-12 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-14 / zbds_iptv4_txt
- 央视频道 / CCTV-14 / zbds_iptv4_txt
- 央视频道 / CCTV-14 / free_tv_world
- 央视频道 / CCTV-15 / zbds_iptv4_txt
- 央视频道 / CCTV-15 / zbds_iptv4_txt
- 央视频道 / CCTV-15 / zbds_iptv4_txt
- 央视频道 / CCTV-15 / free_tv_world
- 央视频道 / CCTV-17 / free_tv_world
- 央视频道 / CCTV-2 / zbds_iptv4_txt
- 央视频道 / CCTV-2 / zbds_iptv4_txt
- 央视频道 / CCTV-2 / iptv_org_cn
- 央视频道 / CCTV-3 / zbds_iptv4_txt
- 央视频道 / CCTV-3 / zbds_iptv4_txt
- 央视频道 / CCTV-3 / iptv_org_cn
- 央视频道 / CCTV-4中文国际（亚） / free_tv_world
- 央视频道 / CCTV-4中文国际（欧） / free_tv_world
- 央视频道 / CCTV-5 / zbds_iptv4_txt
- 央视频道 / CCTV-5 / zbds_iptv4_txt
- 央视频道 / CCTV-5 / zbds_iptv4_txt
- 央视频道 / CCTV-6 / zbds_iptv4_txt
- 央视频道 / CCTV-6 / zbds_iptv4_txt
- 央视频道 / CCTV-6 / free_tv_world
- 央视频道 / CCTV-7 / zbds_iptv4_txt
- 央视频道 / CCTV-7 / zbds_iptv4_txt
- 央视频道 / CCTV-7 / iptv_org_cn
- 央视频道 / CCTV-8 / zbds_iptv4_txt
- 央视频道 / CCTV-8 / zbds_iptv4_txt
- 央视频道 / CCTV-8 / zbds_iptv4_txt
- 央视频道 / CCTV-8 / iptv_org_cn
- 央视频道 / CCTV-9 / zbds_iptv4_txt
- 央视频道 / CCTV-9 / zbds_iptv4_txt
- 央视频道 / CCTV-9 / zbds_iptv4_txt
- 央视频道 / CCTV-9 / iptv_org_cn
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视4K / zbds_iptv4_txt
- 卫视频道 / 云南卫视 / zbds_iptv4_txt
- 卫视频道 / 云南卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 内蒙古卫视 / zbds_iptv4_txt
- 卫视频道 / 北京卫视 / zbds_iptv4_txt
- 卫视频道 / 北京卫视 / zbds_iptv4_txt
- 卫视频道 / 吉林卫视 / zbds_iptv4_txt
- 卫视频道 / 吉林卫视 / zbds_iptv4_txt
- 卫视频道 / 四川卫视 / zbds_iptv4_txt
- 卫视频道 / 大湾区卫视 / zbds_iptv4_txt
- 卫视频道 / 安多卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / zbds_iptv4_txt
- 卫视频道 / 山东卫视 / zbds_iptv4_txt
- 卫视频道 / 山东卫视 / zbds_iptv4_txt
- 卫视频道 / 山西卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 广西卫视 / zbds_iptv4_txt
- 卫视频道 / 广西卫视 / zbds_iptv4_txt
