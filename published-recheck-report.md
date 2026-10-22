# Published playlist recheck report

Outputs rewritten: True
Elapsed: 43.9s
Rows before: 153
Rows after: 117
Rows removed from outputs: 36
Candidate rows failing strict recheck: 36
Rows refilled after strict recheck: 0
Net output row delta: -36
Failed unique URLs after slow retry: 36
Slow retry attempted unique URLs: 38
Slow retry recovered unique URLs: 2
Core live-progress check required: True
Broadcast live-progress check required: True
Live-progress groups: 卫视频道, 地方频道, 央视频道
Video track required: True
Video-track verified final unique URLs: 117
Refill attempted unique URLs: 0
Refill playable unique URLs: 0
Refilled rows: 0
Historical fallback candidates attempted: 0
Historical fallback rows accepted: 0
Unresolved refill rows: 36

## Group deltas

| Group | Before | After | Net delta |
|---|---:|---:|---:|
| 央视频道 | 17 | 17 | +0 |
| 卫视频道 | 4 | 2 | -2 |
| 地方频道 | 36 | 28 | -8 |
| 影视剧场 | 47 | 45 | -2 |
| 体育纪实 | 27 | 21 | -6 |
| 音乐综艺 | 18 | 1 | -17 |
| 综合娱乐 | 4 | 3 | -1 |

## First failed rows

- 卫视频道 / 浙江卫视 / http://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 大湾区卫视 / http://222.128.55.152:9080/live/dwq.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s; last=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s
- 地方频道 / 文成新闻综合 / http://l.cztvcloud.com/channels/lantian/SXwencheng1/720p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江公共新闻 / https://ali-m-l.cztv.com/channels/lantian/channel007/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江国际 / https://ali-m-l.cztv.com/channels/lantian/channel010/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江少儿 / https://ali-m-l.cztv.com/channels/lantian/channel008/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江教科影视 / https://ali-m-l.cztv.com/channels/lantian/channel004/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江民生休闲 / https://ali-m-l.cztv.com/channels/lantian/channel006/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江经视 / https://ali-m-l.cztv.com/channels/lantian/channel003/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江钱江都市 / https://ali-m-l.cztv.com/channels/lantian/channel002/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 影视剧场 / 倩女幽魂人间道 / http://jsmov2.a.yximgs.com/bs3/video-hls/5250634317044855747_hlsb.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 影视剧场 / 倩女幽魂妖魔道 / http://jsmov2.a.yximgs.com/bs3/video-hls/5232901391302199073_hlsb.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 体育纪实 / 中国村庄 / http://newcntv.qcloudcdn.com/asp/hls/4000/0303000a/3/default/93fc12dbf14241c18c23da104fbade23/4000.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 体育纪实 / 人与自然 / http://newcntv.qcloudcdn.com/asp/hls/1200/0303000a/3/default/1425e1d505654cb48ba82b807b221193/1200.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 体育纪实 / 地理中国 / http://newcntv.qcloudcdn.com/asp/hls/1200/0303000a/3/default/c6baf6f74bb944aeacee1065ea72c798/1200.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 体育纪实 / 航拍中国第二季 / http://newcntv.qcloudcdn.com/asp/hls/4000/0303000a/3/default/2bdfdad540b342f592f9817cb7f3b79a/4000.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 体育纪实 / 飞碟之谜01 / https://hls.cntv.lxdns.com/asp/hls/2000/0303000a/3/default/f0a47e155d32450daa1d36a04fd7d262/2000.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 体育纪实 / 飞碟之谜02 / https://newcntv.qcloudcdn.com/asp/hls/2000/0303000a/3/default/d2454bbb542d4613a9db478dab2addfd/2000.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 音乐综艺 / 1993年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/22/BMjAyMzAxMTMyMjEwMDNfNDAzMDAxOTlfOTM1MTIzMzYwODJfMF8z_b_B647d10e431b4cc5e48e6c77347d69021.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 1994年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/22/BMjAyMzAxMTMyMjEwMDNfNDAzMDAxOTlfOTM1MTIzMzYxMjNfMF8z_b_B3dde97f36273f04403d4dc5eec611a35.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 1995年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQwNzVfMF8z_b_B811c0dec6b9a3d3074a18522c185010a.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 1996年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/22/BMjAyMzAxMTMyMjEwMDNfNDAzMDAxOTlfOTM1MTIzMzYxNTJfMF8z_b_Bd841eae10ab1c9955ef55fbedfae6c45.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2000年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/21/BMjAyMzAxMTMyMTE4MzRfNDAzMDAxOTlfOTM1MDY4ODIxMTNfMF8z_b_Bdddf4e7ef0ff6cfd477857bb40e78419.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2001年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQyMDFfMF8z_b_B70592cb7c4054e9cabb675e849bbf4bd.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2002年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/21/BMjAyMzAxMTMyMTE4MzRfNDAzMDAxOTlfOTM1MDY4ODIxNDdfMF8z_b_Ba6271d10b7e6cfae83759033a091f257.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2003年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/14/23/BMjAyMzAxMTQyMzQxNDdfNDAzMDAxOTlfOTM2MTU0MTk1NDFfMF8z_b_B182749d2cd2ea9323639254af385f24b.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2004年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/21/BMjAyMzAxMTMyMTE4MzRfNDAzMDAxOTlfOTM1MDY4ODIxOTVfMF8z_b_B86c4430b82ff5a7f4e8132f6ee558536.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2005年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQyMzhfMF8z_b_B35ad7cc86aec8fc9e5ddfb31fc7bed63.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2006年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQyNzlfMF8z_b_Bbc3703fc331dc994c50859c19aad28ff.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2007年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQzMjNfMF8z_b_B00b069c7899976459ceeaa99353dfefe.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2009年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQzOTBfMF8z_b_B29a36a85e0277f6c2a1f033ef7c10708.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2010年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQ0MjlfMF8z_b_B8818807a00eed329a69fb494f405bd43.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2013年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/13/20/BMjAyMzAxMTMyMDA5MjJfNDAzMDAxOTlfOTM0OTkwNDQ1NjNfMF8z_b_B4fea55408dca4471a68a963ae096be59.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2014年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/06/16/BMjAyMzAxMDYxNjMxMTNfNDAzMDAxOTlfOTI4OTY2ODAzNjlfMF8z_b_Bdee65c77f9e7b2120a185c919dad81d2.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 音乐综艺 / 2018年春晚 / https://alimov2.a.kwimgs.com/upic/2023/01/06/16/BMjAyMzAxMDYxNjMxMTRfNDAzMDAxOTlfOTI4OTY2ODE2MTBfMF8z_b_B11a778e34390a21de42d407e94f45b91.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 综合娱乐 / 支持作者 / https://vd2.bdstatic.com/mda-sctj0f6r4u1bpebc/1080p/cae_h264/1774706523506678171/mda-sctj0f6r4u1bpebc.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
