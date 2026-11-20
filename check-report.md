# IPTV source verification report

Generated: 2026-11-20 01:47:51
Generated UTC: 2026-11-20T01:47:51Z
Generated Beijing: 2026-11-20 09:47:51 Asia/Shanghai
Elapsed: 64.6s
Sources configured: 43 (enabled=34, recovery=2, disabled=7)
Sources probed: 36
Sources fetched OK: 32
Sources with parsed rows (before policy filters): 28
Sources with media-eligible candidates: 7
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 25692
Policy-excluded candidates (not media-checked): 24778
Eligible candidates before URL deduplication: 914
Unique name+URL candidates: 544
Unique stream URLs: 529
Checked unique stream URLs: 529
Checked all unique URLs: True
Playable channel names: 305
Playable unique URLs: 389
Playable name+URL lines: 404
Playable URLs found (legacy line count): 404
Pre-curated published playable lines: 404

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | FAIL | NO | 0 | 0 | 0 | False | URLError(TimeoutError('timed out')) |
| zbds_iptv4_txt | enabled | OK | YES | 448 | 438 | 39400 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 338 | 331 | 80857 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 267 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21971 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10853 | 18 | 2701858 | False |  |
| epg_cn | enabled | OK | YES | 2066 | 0 | 656739 | False |  |
| epg_hk | enabled | OK | YES | 53 | 0 | 17504 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 61 | 0 | 21601 | False |  |
| iptv_org_tw | enabled | OK | YES | 33 | 0 | 6268 | False |  |
| epg_sg | enabled | OK | YES | 8 | 0 | 2457 | False |  |
| epg_my | enabled | OK | YES | 22 | 0 | 7024 | False |  |
| free_tv_world | enabled | OK | YES | 2188 | 20 | 588585 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | OK | YES | 1084 | 0 | 209450 | False |  |
| freetv_douyu | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| iptv_org_cn | enabled | OK | YES | 132 | 18 | 32055 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 36055 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1779 | False | catalog only; child links not fetched or executed |
| oktv_comprehensive_php | enabled | OK | YES | 188 | 31 | 42900 | False |  |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 357 |
| oktv_comprehensive_php | 29 |
| iptv_org_cn | 11 |
| free_tv_world | 7 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / iptv_org_cn
- 央视频道 / CCTV-1 / oktv_comprehensive_php
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-10 / oktv_comprehensive_php
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-12 / iptv_org_cn
- 央视频道 / CCTV-12 / oktv_comprehensive_php
- 央视频道 / CCTV-13 / zbds_iptv4_txt
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-13 / oktv_comprehensive_php
- 央视频道 / CCTV-14 / free_tv_world
- 央视频道 / CCTV-14 / oktv_comprehensive_php
- 央视频道 / CCTV-15 / iptv_org_cn
- 央视频道 / CCTV-15 / oktv_comprehensive_php
- 央视频道 / CCTV-16 / oktv_comprehensive_php
- 央视频道 / CCTV-17 / free_tv_world
- 央视频道 / CCTV-17 / oktv_comprehensive_php
- 央视频道 / CCTV-2 / iptv_org_cn
- 央视频道 / CCTV-2 / oktv_comprehensive_php
- 央视频道 / CCTV-3 / zbds_iptv4_txt
- 央视频道 / CCTV-3 / iptv_org_cn
- 央视频道 / CCTV-3 / oktv_comprehensive_php
- 央视频道 / CCTV-4 / oktv_comprehensive_php
- 央视频道 / CCTV-4中文国际（亚） / free_tv_world
- 央视频道 / CCTV-4中文国际（欧） / free_tv_world
- 央视频道 / CCTV-4亚洲 / oktv_comprehensive_php
- 央视频道 / CCTV-5 / oktv_comprehensive_php
- 央视频道 / CCTV-6 / free_tv_world
- 央视频道 / CCTV-6 / oktv_comprehensive_php
- 央视频道 / CCTV-7 / iptv_org_cn
- 央视频道 / CCTV-7 / oktv_comprehensive_php
- 央视频道 / CCTV-8 / iptv_org_cn
- 央视频道 / CCTV-8 / oktv_comprehensive_php
- 央视频道 / CCTV-9 / free_tv_world
- 央视频道 / CCTV-9 / oktv_comprehensive_php
- 央视频道 / CCTV-9 / iptv_org_cn
- 卫视频道 / 东南卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / zbds_iptv4_txt
- 卫视频道 / 东方卫视 / oktv_comprehensive_php
- 卫视频道 / 东方卫视4K / zbds_iptv4_txt
- 卫视频道 / 内蒙古卫视 / zbds_iptv4_txt
- 卫视频道 / 北京卫视 / oktv_comprehensive_php
- 卫视频道 / 吉林卫视 / zbds_iptv4_txt
- 卫视频道 / 天津卫视 / oktv_comprehensive_php
- 卫视频道 / 安多卫视 / zbds_iptv4_txt
- 卫视频道 / 安徽卫视 / oktv_comprehensive_php
- 卫视频道 / 山东卫视 / oktv_comprehensive_php
- 卫视频道 / 山西卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / zbds_iptv4_txt
- 卫视频道 / 广东卫视 / oktv_comprehensive_php
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 延边卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 新疆卫视 / zbds_iptv4_txt
- 卫视频道 / 江苏卫视 / oktv_comprehensive_php
- 卫视频道 / 江西卫视 / zbds_iptv4_txt
- 卫视频道 / 河北卫视 / oktv_comprehensive_php
- 卫视频道 / 河南卫视 / oktv_comprehensive_php
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / oktv_comprehensive_php
- 卫视频道 / 深圳卫视 / oktv_comprehensive_php
- 卫视频道 / 湖南卫视 / zbds_iptv4_txt
- 卫视频道 / 湖南卫视 / oktv_comprehensive_php
- 地方频道 / FZTV-1News新闻综合频道 / free_tv_world
- 地方频道 / 七台河新闻综合 / zbds_iptv4_txt
- 地方频道 / 万荣综合 / zbds_iptv4_txt
- 地方频道 / 上虞文化影院 / zbds_iptv4_txt
- 地方频道 / 上虞新商都 / zbds_iptv4_txt
- 地方频道 / 上虞新闻综合 / zbds_iptv4_txt
- 地方频道 / 东莞新闻综合 / zbds_iptv4_txt
- 地方频道 / 中国蓝新闻 / zbds_iptv4_txt
- 地方频道 / 九台综合 / zbds_iptv4_txt
- 地方频道 / 云和新闻综合 / zbds_iptv4_txt
- 地方频道 / 云和新闻综合 / zbds_iptv4_txt
