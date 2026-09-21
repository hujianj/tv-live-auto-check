# IPTV source verification report

Generated: 2026-09-21 15:08:36
Generated UTC: 2026-09-21T15:08:36Z
Generated Beijing: 2026-09-21 23:08:36 Asia/Shanghai
Elapsed: 89.1s
Sources configured: 42 (enabled=33, recovery=2, disabled=7)
Sources probed: 35
Sources fetched OK: 31
Sources with parsed rows (before policy filters): 27
Sources with media-eligible candidates: 6
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 22733
Policy-excluded candidates (not media-checked): 21476
Eligible candidates before URL deduplication: 1257
Unique name+URL candidates: 710
Unique stream URLs: 694
Checked unique stream URLs: 694
Checked all unique URLs: True
Playable channel names: 429
Playable unique URLs: 493
Playable name+URL lines: 502
Playable URLs found (legacy line count): 502
Pre-curated published playable lines: 502

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | YES | 6 | 0 | 609 | False |  |
| zbds_iptv4_txt | enabled | OK | YES | 652 | 640 | 54860 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 519 | 510 | 119105 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10305 | 14 | 2489067 | False |  |
| epg_cn | enabled | OK | YES | 794 | 0 | 259513 | False |  |
| epg_hk | enabled | OK | YES | 18 | 0 | 5759 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 18 | 0 | 9331 | False |  |
| iptv_org_tw | enabled | OK | YES | 25 | 0 | 4747 | False |  |
| epg_sg | enabled | OK | YES | 1 | 0 | 390 | False |  |
| epg_my | enabled | OK | YES | 2 | 0 | 679 | False |  |
| free_tv_world | enabled | OK | YES | 2053 | 21 | 552188 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| freetv_douyu | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| iptv_org_cn | enabled | OK | YES | 122 | 14 | 29075 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 36517 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 486 |
| iptv_org_cn | 9 |
| free_tv_world | 7 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / iptv_org_cn
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-12 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-14 / free_tv_world
- 央视频道 / CCTV-15 / zbds_iptv4_txt
- 央视频道 / CCTV-15 / free_tv_world
- 央视频道 / CCTV-17 / free_tv_world
- 央视频道 / CCTV-2 / iptv_org_cn
- 央视频道 / CCTV-3 / zbds_iptv4_txt
- 央视频道 / CCTV-3 / iptv_org_cn
- 央视频道 / CCTV-4中文国际（亚） / free_tv_world
- 央视频道 / CCTV-4中文国际（欧） / free_tv_world
- 央视频道 / CCTV-5 / zbds_iptv4_txt
- 央视频道 / CCTV-5 / zbds_iptv4_txt
- 央视频道 / CCTV-6 / free_tv_world
- 央视频道 / CCTV-7 / iptv_org_cn
- 央视频道 / CCTV-8 / zbds_iptv4_txt
- 央视频道 / CCTV-8 / iptv_org_cn
- 央视频道 / CCTV-9 / zbds_iptv4_txt
- 央视频道 / CCTV-9 / iptv_org_cn
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 内蒙古卫视 / zbds_iptv4_txt
- 卫视频道 / 大湾区卫视 / zbds_iptv4_txt
- 卫视频道 / 安多卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / zbds_iptv4_txt
- 卫视频道 / 山西卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 江西卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 深圳卫视 / zbds_iptv4_txt
- 卫视频道 / 湖南卫视 / zbds_iptv4_txt
- 卫视频道 / 福建海峡卫视 / zbds_iptv4_txt
- 卫视频道 / 福建海峡卫视 / zbds_iptv4_txt
- 卫视频道 / 福建海峡卫视 / zbds_iptv4_txt
- 卫视频道 / 青海卫视 / zbds_iptv4_txt
- 地方频道 / FZTV-1News新闻综合频道 / free_tv_world
- 地方频道 / 万荣综合 / zbds_iptv4_txt
- 地方频道 / 三明新闻综合 / zbds_iptv4_txt
- 地方频道 / 三明新闻综合 / zbds_iptv4_txt
- 地方频道 / 上海第一财经 / zbds_iptv4_txt
- 地方频道 / 上虞文化影院 / zbds_iptv4_txt
- 地方频道 / 上虞新商都 / zbds_iptv4_txt
- 地方频道 / 上虞新闻综合 / zbds_iptv4_txt
- 地方频道 / 东丰综合 / zbds_iptv4_txt
- 地方频道 / 东莞新闻综合 / zbds_iptv4_txt
- 地方频道 / 东莞生活资讯 / zbds_iptv4_txt
- 地方频道 / 中国蓝新闻 / zbds_iptv4_txt
- 地方频道 / 乐至综合 / zbds_iptv4_txt
- 地方频道 / 九台综合 / zbds_iptv4_txt
- 地方频道 / 云南丽江冰川 / zbds_iptv4_txt
- 地方频道 / 云南丽江印象实景 / zbds_iptv4_txt
- 地方频道 / 云南丽江玉龙雪山 / zbds_iptv4_txt
- 地方频道 / 云南丽江玉龙雪山草甸 / zbds_iptv4_txt
- 地方频道 / 云南丽江蓝月谷 / zbds_iptv4_txt
- 地方频道 / 云南大理崇圣寺三塔中景 / zbds_iptv4_txt
- 地方频道 / 云南大理崇圣寺三塔远景 / zbds_iptv4_txt
- 地方频道 / 云南白沙远眺玉龙雪山 / zbds_iptv4_txt
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
