# IPTV source verification report

Generated: 2026-10-29 07:57:06
Generated UTC: 2026-10-29T07:57:06Z
Generated Beijing: 2026-10-29 15:57:06 Asia/Shanghai
Elapsed: 78.3s
Sources configured: 43 (enabled=34, recovery=2, disabled=7)
Sources probed: 36
Sources fetched OK: 34
Sources with parsed rows (before policy filters): 30
Sources with media-eligible candidates: 7
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 31849
Policy-excluded candidates (not media-checked): 30769
Eligible candidates before URL deduplication: 1080
Unique name+URL candidates: 628
Unique stream URLs: 611
Checked unique stream URLs: 611
Checked all unique URLs: True
Playable channel names: 321
Playable unique URLs: 372
Playable name+URL lines: 385
Playable URLs found (legacy line count): 385
Pre-curated published playable lines: 385

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | YES | 6810 | 0 | 506352 | False |  |
| zbds_iptv4_txt | enabled | OK | YES | 538 | 526 | 45825 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 426 | 417 | 99306 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10627 | 14 | 2593969 | False |  |
| epg_cn | enabled | OK | YES | 752 | 0 | 243836 | False |  |
| epg_hk | enabled | OK | YES | 14 | 0 | 4769 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 25 | 0 | 9956 | False |  |
| iptv_org_tw | enabled | OK | YES | 31 | 0 | 5925 | False |  |
| epg_sg | enabled | OK | YES | 1 | 0 | 318 | False |  |
| epg_my | enabled | OK | YES | 5 | 0 | 1665 | False |  |
| free_tv_world | enabled | OK | YES | 2039 | 20 | 542812 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | OK | YES | 1114 | 0 | 215343 | False |  |
| freetv_douyu | recovery | OK | YES | 934 | 0 | 177391 | False |  |
| iptv_org_cn | enabled | OK | YES | 127 | 14 | 30080 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 35784 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |
| oktv_comprehensive_php | enabled | OK | YES | 188 | 31 | 42900 | False |  |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 352 |
| oktv_comprehensive_php | 16 |
| iptv_org_cn | 11 |
| free_tv_world | 6 |

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
- 央视频道 / CCTV-5 / zbds_iptv4_txt
- 央视频道 / CCTV-7 / iptv_org_cn
- 央视频道 / CCTV-8 / zbds_iptv4_txt
- 央视频道 / CCTV-8 / iptv_org_cn
- 央视频道 / CCTV-9 / free_tv_world
- 央视频道 / CCTV-9 / iptv_org_cn
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / oktv_comprehensive_php
- 卫视频道 / 东方卫视4K / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 内蒙古卫视 / zbds_iptv4_txt
- 卫视频道 / 北京卫视 / oktv_comprehensive_php
- 卫视频道 / 大湾区卫视 / zbds_iptv4_txt
- 卫视频道 / 天津卫视 / oktv_comprehensive_php
- 卫视频道 / 安多卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / oktv_comprehensive_php
- 卫视频道 / 山东卫视 / oktv_comprehensive_php
- 卫视频道 / 山西卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / oktv_comprehensive_php
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
- 地方频道 / 万荣综合 / zbds_iptv4_txt
- 地方频道 / 三明新闻综合 / zbds_iptv4_txt
- 地方频道 / 三明新闻综合 / zbds_iptv4_txt
- 地方频道 / 上海第一财经 / zbds_iptv4_txt
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
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 云霄综合 / zbds_iptv4_txt
- 地方频道 / 云霄综合 / zbds_iptv4_txt
