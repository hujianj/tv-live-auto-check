# IPTV source verification report

Generated: 2026-10-16 13:17:47
Generated UTC: 2026-10-16T13:17:47Z
Generated Beijing: 2026-10-16 21:17:47 Asia/Shanghai
Elapsed: 95.0s
Sources configured: 42 (enabled=33, recovery=2, disabled=7)
Sources probed: 35
Sources fetched OK: 32
Sources with parsed rows (before policy filters): 28
Sources with media-eligible candidates: 6
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 25598
Policy-excluded candidates (not media-checked): 24322
Eligible candidates before URL deduplication: 1276
Unique name+URL candidates: 722
Unique stream URLs: 706
Checked unique stream URLs: 706
Checked all unique URLs: True
Playable channel names: 394
Playable unique URLs: 434
Playable name+URL lines: 443
Playable URLs found (legacy line count): 443
Pre-curated published playable lines: 443

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | YES | 6 | 0 | 609 | False |  |
| zbds_iptv4_txt | enabled | OK | YES | 665 | 653 | 55796 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 526 | 517 | 119310 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10623 | 14 | 2573780 | False |  |
| epg_cn | enabled | OK | YES | 2293 | 0 | 731485 | False |  |
| epg_hk | enabled | OK | YES | 53 | 0 | 17139 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 82 | 0 | 28158 | False |  |
| iptv_org_tw | enabled | OK | YES | 27 | 0 | 5173 | False |  |
| epg_sg | enabled | OK | YES | 8 | 0 | 2456 | False |  |
| epg_my | enabled | OK | YES | 20 | 0 | 6374 | False |  |
| free_tv_world | enabled | OK | YES | 2009 | 20 | 537525 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| freetv_douyu | recovery | OK | YES | 943 | 0 | 179219 | False |  |
| iptv_org_cn | enabled | OK | YES | 125 | 14 | 29674 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 35785 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 428 |
| iptv_org_cn | 8 |
| free_tv_world | 7 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / zbds_iptv4_txt
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-12 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-14 / free_tv_world
- 央视频道 / CCTV-15 / zbds_iptv4_txt
- 央视频道 / CCTV-15 / free_tv_world
- 央视频道 / CCTV-16 / zbds_iptv4_txt
- 央视频道 / CCTV-17 / free_tv_world
- 央视频道 / CCTV-2 / iptv_org_cn
- 央视频道 / CCTV-3 / iptv_org_cn
- 央视频道 / CCTV-4中文国际（亚） / free_tv_world
- 央视频道 / CCTV-4中文国际（欧） / free_tv_world
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
- 地方频道 / 上海新闻综合 / zbds_iptv4_txt
- 地方频道 / 上海第一财经 / zbds_iptv4_txt
- 地方频道 / 上海第一财经 / zbds_iptv4_txt
- 地方频道 / 上海都市 / zbds_iptv4_txt
- 地方频道 / 上虞新商都 / zbds_iptv4_txt
- 地方频道 / 东丰综合 / zbds_iptv4_txt
- 地方频道 / 东莞新闻综合 / zbds_iptv4_txt
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
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 井研综合 / zbds_iptv4_txt
- 地方频道 / 亳州农村 / zbds_iptv4_txt
- 地方频道 / 亳州农村 / zbds_iptv4_txt
- 地方频道 / 余杭综合 / zbds_iptv4_txt
- 地方频道 / 六安公共 / zbds_iptv4_txt
- 地方频道 / 六安新闻综合 / zbds_iptv4_txt
- 地方频道 / 兵团五师双河影 / zbds_iptv4_txt
- 地方频道 / 兵团五师双河新闻综合 / zbds_iptv4_txt
