# IPTV source verification report

Generated: 2026-10-24 12:44:11
Generated UTC: 2026-10-24T12:44:11Z
Generated Beijing: 2026-10-24 20:44:11 Asia/Shanghai
Elapsed: 195.1s
Sources configured: 42 (enabled=33, recovery=2, disabled=7)
Sources probed: 35
Sources fetched OK: 32
Sources with parsed rows (before policy filters): 28
Sources with media-eligible candidates: 6
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 32354
Policy-excluded candidates (not media-checked): 31060
Eligible candidates before URL deduplication: 1294
Unique name+URL candidates: 744
Unique stream URLs: 728
Checked unique stream URLs: 728
Checked all unique URLs: True
Playable channel names: 419
Playable unique URLs: 490
Playable name+URL lines: 504
Playable URLs found (legacy line count): 504
Pre-curated published playable lines: 504

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | YES | 6885 | 0 | 511212 | False |  |
| zbds_iptv4_txt | enabled | OK | YES | 687 | 675 | 57983 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 522 | 513 | 119336 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10614 | 14 | 2573275 | False |  |
| epg_cn | enabled | OK | YES | 2130 | 0 | 676904 | False |  |
| epg_hk | enabled | OK | YES | 48 | 0 | 15564 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 73 | 0 | 25255 | False |  |
| iptv_org_tw | enabled | OK | YES | 30 | 0 | 5696 | False |  |
| epg_sg | enabled | OK | YES | 7 | 0 | 2192 | False |  |
| epg_my | enabled | OK | YES | 23 | 0 | 7411 | False |  |
| free_tv_world | enabled | OK | YES | 2038 | 20 | 542646 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | FAIL | NO | 0 | 0 | 0 | False | <HTTPError 504: 'Gateway Timeout'> |
| freetv_douyu | recovery | OK | YES | 952 | 0 | 180843 | False |  |
| iptv_org_cn | enabled | OK | YES | 127 | 14 | 30076 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 35785 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 486 |
| iptv_org_cn | 11 |
| free_tv_world | 7 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / iptv_org_cn
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-12 / iptv_org_cn
- 央视频道 / CCTV-13 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-14 / free_tv_world
- 央视频道 / CCTV-15 / zbds_iptv4_txt
- 央视频道 / CCTV-15 / iptv_org_cn
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
- 央视频道 / CCTV-9 / free_tv_world
- 央视频道 / CCTV-9 / iptv_org_cn
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视4K / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 内蒙古卫视 / zbds_iptv4_txt
- 卫视频道 / 大湾区卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 湖南卫视 / zbds_iptv4_txt
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
- 地方频道 / 余姚新闻综合 / zbds_iptv4_txt
- 地方频道 / 余姚综合 / zbds_iptv4_txt
- 地方频道 / 余姚综合 / zbds_iptv4_txt
- 地方频道 / 余姚综合 / zbds_iptv4_txt
- 地方频道 / 余杭未来E / zbds_iptv4_txt
- 地方频道 / 余杭未来E / zbds_iptv4_txt
