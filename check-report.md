# IPTV source verification report

Generated: 2026-09-09 11:03:23
Generated UTC: 2026-09-09T11:03:23Z
Generated Beijing: 2026-09-09 19:03:23 Asia/Shanghai
Elapsed: 63.9s
Sources configured: 42 (enabled=33, recovery=2, disabled=7)
Sources probed: 35
Sources fetched OK: 31
Sources with parsed rows (before policy filters): 27
Sources with media-eligible candidates: 5
Network scope: current_execution_environment; no region or home-broadband qualification
Channel scope: domestic_chinese
Parsed candidates: 24128
Policy-excluded candidates (not media-checked): 23924
Eligible candidates before URL deduplication: 204
Unique name+URL candidates: 142
Unique stream URLs: 130
Checked unique stream URLs: 130
Checked all unique URLs: True
Playable channel names: 34
Playable unique URLs: 23
Playable name+URL lines: 35
Playable URLs found (legacy line count): 35
Pre-curated published playable lines: 35

## Source fetch status

The legacy contributed CSV flag means parsed rows, not permission approval or final publication.

| Source | Mode | Fetch | Has parsed rows | Parsed | Media eligible | Bytes | Truncated | Error |
|---|---|---:|---:|---:|---:|---:|---:|---|
| iyouhun_zb | enabled | OK | YES | 6 | 0 | 609 | False |  |
| zbds_iptv4_txt | enabled | OK | YES | 630 | 0 | 54412 | False |  |
| guovin_all | enabled | OK | YES | 1456 | 0 | 396412 | False |  |
| guovin_ipv4 | enabled | OK | YES | 398 | 0 | 106329 | False |  |
| guovin_ipv6 | enabled | OK | YES | 1215 | 0 | 330476 | False |  |
| suxuang_ipv4 | enabled | OK | YES | 1186 | 0 | 268175 | False |  |
| suxuang_ipv6 | enabled | OK | YES | 815 | 0 | 200521 | False |  |
| zbds_iptv4_m3u | enabled | OK | YES | 503 | 0 | 115632 | False |  |
| burningc4_ipv4 | enabled | OK | YES | 58 | 58 | 8021 | False |  |
| vamoschuck_m3u | enabled | OK | YES | 786 | 0 | 147124 | False |  |
| zbds_iptv6_txt | enabled | OK | YES | 2 | 0 | 268 | False |  |
| zbds_iptv6_m3u | enabled | OK | YES | 1 | 0 | 282 | False |  |
| fanmingming_ipv6_raw | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| fanmingming_ipv6_mirror | enabled | OK | YES | 69 | 0 | 25215 | False |  |
| kimentanm_aptv | enabled | OK | YES | 119 | 0 | 21944 | False |  |
| bigbiggrandg_gather | enabled | OK | YES | 1900 | 0 | 329793 | False |  |
| yang_gather | enabled | OK | YES | 127 | 0 | 27353 | False |  |
| iptv_org_all | enabled | OK | YES | 10294 | 64 | 2511985 | False |  |
| epg_cn | enabled | OK | YES | 2149 | 0 | 683907 | False |  |
| epg_hk | enabled | OK | YES | 46 | 0 | 14636 | False |  |
| epg_mo | enabled | OK | YES | 19 | 0 | 6134 | False |  |
| epg_tw | enabled | OK | YES | 65 | 0 | 23447 | False |  |
| iptv_org_tw | enabled | OK | YES | 25 | 4 | 4949 | False |  |
| epg_sg | enabled | OK | YES | 11 | 0 | 3507 | False |  |
| epg_my | enabled | OK | YES | 21 | 0 | 6723 | False |  |
| free_tv_world | enabled | OK | YES | 2036 | 21 | 550929 | False |  |
| mursor_yy | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| mursor_bililive | enabled | FAIL | NO | 0 | 0 | 0 | False | PublicURLPolicyError('DNS resolution failed for gongdian.top: [Errno -5] No address associated with hostname') |
| freetv_huya | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| freetv_douyu | recovery | FAIL | NO | 0 | 0 | 0 | False | TimeoutError('URL total budget exceeded during connection retry') |
| iptv_org_cn | enabled | OK | YES | 122 | 57 | 28662 | False |  |
| tvapp_catalog | enabled | OK | NO | 0 | 0 | 36518 | False | catalog only; child links not fetched or executed |
| qist_catalog | enabled | OK | NO | 0 | 0 | 6958 | False | catalog only; child links not fetched or executed |
| yingshitv_catalog | enabled | OK | NO | 0 | 0 | 2788 | False | catalog only; child links not fetched or executed |
| tomorrow_catalog | enabled | OK | NO | 0 | 0 | 1845 | False | catalog only; child links not fetched or executed |

## Pre-curation playable lines by source

| Source | Lines |
|---|---:|
| free_tv_world | 17 |
| iptv_org_cn | 16 |
| iptv_org_tw | 2 |

## First 80 pre-curation playable channel candidates

- 央视频道 / CCTV-1 / iptv_org_cn
- 央视频道 / CCTV-10 / iptv_org_cn
- 央视频道 / CCTV-10科教 / free_tv_world
- 央视频道 / CCTV-11 / iptv_org_cn
- 央视频道 / CCTV-11戏曲 / free_tv_world
- 央视频道 / CCTV-12 / iptv_org_cn
- 央视频道 / CCTV-12社会与法 / free_tv_world
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-13 / iptv_org_cn
- 央视频道 / CCTV-13新闻 / free_tv_world
- 央视频道 / CCTV-14 / iptv_org_cn
- 央视频道 / CCTV-14少儿 / free_tv_world
- 央视频道 / CCTV-15音乐 / free_tv_world
- 央视频道 / CCTV-17 / iptv_org_cn
- 央视频道 / CCTV-17农业农村 / free_tv_world
- 央视频道 / CCTV-1综合 / free_tv_world
- 央视频道 / CCTV-2 / iptv_org_cn
- 央视频道 / CCTV-2财经 / free_tv_world
- 央视频道 / CCTV-3 / iptv_org_cn
- 央视频道 / CCTV-3综艺 / free_tv_world
- 央视频道 / CCTV-4中文国际（亚） / free_tv_world
- 央视频道 / CCTV-4中文国际（欧） / free_tv_world
- 央视频道 / CCTV-5+ / iptv_org_cn
- 央视频道 / CCTV-6 / iptv_org_cn
- 央视频道 / CCTV-6电影 / free_tv_world
- 央视频道 / CCTV-7 / iptv_org_cn
- 央视频道 / CCTV-7国防军事 / free_tv_world
- 央视频道 / CCTV-8 / iptv_org_cn
- 央视频道 / CCTV-8电视剧 / free_tv_world
- 央视频道 / CCTV-9 / iptv_org_cn
- 央视频道 / CCTV-9纪录 / free_tv_world
- 卫视频道 / 北京卫视 / iptv_org_cn
- 地方频道 / FZTV-1News新闻综合频道 / free_tv_world
- 港澳台频道 / DaliTV(大立電視台)(720p) / iptv_org_tw
- 港澳台频道 / 唯心電視(480p) / iptv_org_tw
