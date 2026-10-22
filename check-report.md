# IPTV source verification report

Generated: 2026-10-22 23:24:27
Generated UTC: 2026-10-22T23:24:27Z
Generated Beijing: 2026-10-23 07:24:27 Asia/Shanghai
Elapsed: 80.2s
Sources configured: 42 (enabled=33, recovery=2, disabled=7)
Sources probed: 35
Sources fetched OK: 31
Sources with parsed rows (before policy filters): 27
Sources with media-eligible candidates: 6
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 30734
Policy-excluded candidates (not media-checked): 30283
Eligible candidates before URL deduplication: 451
Unique name+URL candidates: 254
Unique stream URLs: 254
Checked unique stream URLs: 254
Checked all unique URLs: True
Playable channel names: 151
Playable unique URLs: 153
Playable name+URL lines: 153
Playable URLs found (legacy line count): 153
Pre-curated published playable lines: 153

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | YES | 6882 | 0 | 509922 | False |  |
| zbds_iptv4_txt | enabled | OK | YES | 184 | 174 | 15052 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1188 | 0 | 268591 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 178 | 171 | 40090 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 123 | 0 | 26227 | False |  |
| iptv_org_all | enabled | OK | YES | 10641 | 14 | 2579692 | False |  |
| epg_cn | enabled | OK | YES | 2300 | 0 | 731915 | False |  |
| epg_hk | enabled | OK | YES | 52 | 0 | 16797 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 78 | 0 | 26846 | False |  |
| iptv_org_tw | enabled | OK | YES | 30 | 0 | 5696 | False |  |
| epg_sg | enabled | OK | YES | 9 | 0 | 2769 | False |  |
| epg_my | enabled | OK | YES | 25 | 0 | 8044 | False |  |
| free_tv_world | enabled | OK | YES | 2010 | 20 | 537738 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| freetv_douyu | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| iptv_org_cn | enabled | OK | YES | 127 | 14 | 30076 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 35785 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| zbds_iptv4_txt | 135 |
| iptv_org_cn | 11 |
| free_tv_world | 7 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / iptv_org_cn
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-12 / iptv_org_cn
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-14 / free_tv_world
- 央视频道 / CCTV-15 / iptv_org_cn
- 央视频道 / CCTV-17 / free_tv_world
- 央视频道 / CCTV-2 / iptv_org_cn
- 央视频道 / CCTV-3 / iptv_org_cn
- 央视频道 / CCTV-4中文国际（亚） / free_tv_world
- 央视频道 / CCTV-4中文国际（欧） / free_tv_world
- 央视频道 / CCTV-6 / free_tv_world
- 央视频道 / CCTV-7 / iptv_org_cn
- 央视频道 / CCTV-8 / iptv_org_cn
- 央视频道 / CCTV-9 / free_tv_world
- 央视频道 / CCTV-9 / iptv_org_cn
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 人间卫视 / zbds_iptv4_txt
- 卫视频道 / 大湾区卫视 / zbds_iptv4_txt
- 卫视频道 / 浙江卫视 / zbds_iptv4_txt
- 地方频道 / FZTV-1News新闻综合频道 / free_tv_world
- 地方频道 / 东莞新闻综合 / zbds_iptv4_txt
- 地方频道 / 乐至综合 / zbds_iptv4_txt
- 地方频道 / 云和新闻综合 / zbds_iptv4_txt
- 地方频道 / 兵团五师双河影 / zbds_iptv4_txt
- 地方频道 / 哈尔滨娱乐 / zbds_iptv4_txt
- 地方频道 / 哈尔滨新闻综合 / zbds_iptv4_txt
- 地方频道 / 哈尔滨生活 / zbds_iptv4_txt
- 地方频道 / 哈尔滨都市咨询 / zbds_iptv4_txt
- 地方频道 / 山东教育 / zbds_iptv4_txt
- 地方频道 / 广安公共 / zbds_iptv4_txt
- 地方频道 / 广州竞赛 / zbds_iptv4_txt
- 地方频道 / 文成新闻综合 / zbds_iptv4_txt
- 地方频道 / 汉源综合 / zbds_iptv4_txt
- 地方频道 / 江夏新闻综合 / zbds_iptv4_txt
- 地方频道 / 浙江公共新闻 / zbds_iptv4_txt
- 地方频道 / 浙江国际 / zbds_iptv4_txt
- 地方频道 / 浙江少儿 / zbds_iptv4_txt
- 地方频道 / 浙江教科影视 / zbds_iptv4_txt
- 地方频道 / 浙江民生休闲 / zbds_iptv4_txt
- 地方频道 / 浙江经视 / zbds_iptv4_txt
- 地方频道 / 浙江钱江都市 / zbds_iptv4_txt
- 地方频道 / 苏州4K / zbds_iptv4_txt
- 地方频道 / 苏州文化生活 / zbds_iptv4_txt
- 地方频道 / 苏州新闻综合 / zbds_iptv4_txt
- 地方频道 / 苏州生活资讯 / zbds_iptv4_txt
- 地方频道 / 苏州社会经济 / zbds_iptv4_txt
- 地方频道 / 荥经综合 / zbds_iptv4_txt
- 地方频道 / 萧山综合 / zbds_iptv4_txt
- 地方频道 / 象山新闻综合 / zbds_iptv4_txt
- 地方频道 / 金川乡村 / zbds_iptv4_txt
- 地方频道 / 金川新闻综合 / zbds_iptv4_txt
- 地方频道 / 雅安新闻综合 / zbds_iptv4_txt
- 地方频道 / 青川综合 / zbds_iptv4_txt
- 地方频道 / 青田电视台 / zbds_iptv4_txt
- 地方频道 / 龙泉新闻综合 / zbds_iptv4_txt
- 音乐综艺 / 1993年春晚 / zbds_iptv4_txt
- 音乐综艺 / 1994年春晚 / zbds_iptv4_txt
- 音乐综艺 / 1995年春晚 / zbds_iptv4_txt
- 音乐综艺 / 1996年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2000年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2001年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2002年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2003年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2004年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2005年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2006年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2007年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2009年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2010年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2013年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2014年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2018年春晚 / zbds_iptv4_txt
- 音乐综艺 / 2024年春晚 / zbds_iptv4_txt
- 体育纪实 / 东丰 / zbds_iptv4_txt
- 体育纪实 / 中国村庄 / zbds_iptv4_txt
- 体育纪实 / 之江纪录 / zbds_iptv4_txt
- 体育纪实 / 九台 / zbds_iptv4_txt
- 体育纪实 / 人与自然 / zbds_iptv4_txt
