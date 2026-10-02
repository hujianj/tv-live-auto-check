# Published playlist recheck report

Outputs rewritten: True
Elapsed: 329.2s
Rows before: 489
Rows after: 318
Rows removed from outputs: 171
Candidate rows failing strict recheck: 171
Rows refilled after strict recheck: 0
Net output row delta: -171
Failed unique URLs after slow retry: 171
Slow retry attempted unique URLs: 178
Slow retry recovered unique URLs: 7
Core live-progress check required: True
Broadcast live-progress check required: True
Live-progress groups: 卫视频道, 地方频道, 央视频道
Video track required: True
Video-track verified final unique URLs: 318
Refill attempted unique URLs: 0
Refill playable unique URLs: 0
Refilled rows: 0
Historical fallback candidates attempted: 0
Historical fallback rows accepted: 0
Unresolved refill rows: 171

## Group deltas

| Group | Before | After | Net delta |
|---|---:|---:|---:|
| 央视频道 | 22 | 21 | -1 |
| 卫视频道 | 27 | 21 | -6 |
| 地方频道 | 272 | 140 | -132 |
| 影视剧场 | 66 | 63 | -3 |
| 少儿动漫 | 2 | 2 | +0 |
| 体育纪实 | 28 | 18 | -10 |
| 音乐综艺 | 19 | 1 | -18 |
| 综合娱乐 | 52 | 51 | -1 |
| 港澳台频道 | 1 | 1 | +0 |

## First failed rows

- 央视频道 / CCTV-13 / http://ali-m-l.cztv.com/channels/lantian/channel21/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / http://ali-vl.cztv.com/channels/lantian/channel001/360p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 浙江卫视 / http://ali-m-l.cztv.com/channels/lantian/channel01/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / http://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / https://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 广东卫视 / https://txmov2.a.kwimgs.com/upic/2023/01/26/09/BMjAyMzAxMjYwOTE3NDVfNzM5MzQzNzIyXzk0NjI1OTUwNTA3XzBfMw==_b_B81ddda927d33445d544befd008e60109.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 卫视频道 / 大湾区卫视 / http://222.128.55.152:9080/live/dwq.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s; last=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s
- 地方频道 / 三明新闻综合 / http://ls.qingting.fm/live/4885.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 三明新闻综合 / https://ls.qingting.fm/live/5022100/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 上海第一财经 / https://satellitepull.cnr.cn/live/wx32dycjgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 东丰综合 / http://stream3.jlntv.cn:80/aac_dfgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 中国蓝新闻 / http://ali-m-l.cztv.com/channels/lantian/channel009/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 云和新闻综合 / http://l.cztvcloud.com/channels/lantian/SXyunhe1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 余姚姚江文化 / http://l.cztvcloud.com/channels/lantian/SXyuyao3/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 12.5s
- 地方频道 / 余姚姚江文化 / https://l.cztvcloud.com/channels/lantian/SXyuyao3/720p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('_ssl.c:993: The handshake operation timed out')); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 12.5s
- 地方频道 / 余姚新闻综合 / http://l.cztvcloud.com/channels/lantian/SXyuyao1/720p.m3u8?cWlkPSZzPTg3OWMwYmMyZDMzYTFhZGY3NDQxMjgyYTg1MmUzNTY0JmVzPTE3MDY2Nzc4NzMmdXVpZD0yMjdiY2MzNGNiNGY0MThlYjRiY2IxYzcwNmZjODNkMS02NzQ3NDY2NyZ2PTImYXM9MCZjZG5leF9pZD10eF9waG9uZV9saXZl / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 余姚综合 / http://l.cztvcloud.com/channels/lantian/SXyuyao1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 余姚综合 / https://l.cztvcloud.com/channels/lantian/SXyuyao1/720p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('_ssl.c:993: The handshake operation timed out')); last=URLError(TimeoutError('_ssl.c:993: The handshake operation timed out'))
- 地方频道 / 余杭未来E / http://l.cztvcloud.com/channels/lantian/SXyuhang3/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 余杭未来E / http://l.cztvcloud.com/channels/lantian/SXyuhang3/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 余杭综合 / http://l.cztvcloud.com/channels/lantian/SXyuhang1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 余杭综合 / http://l.cztvcloud.com/channels/lantian/SXyuhang1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 六安公共 / http://ls.qingting.fm/live/1794199.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 六安新闻综合 / http://ls.qingting.fm/live/267.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 兰溪新闻综合 / http://l.cztvcloud.com/channels/lantian/SXlanxi1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 北京新闻 / https://satellitepull.cnr.cn/live/wxbjxwgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 双辽综合 / http://stream3.jlntv.cn:80/aac_slgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 可克达拉综合 / http://file.loulannews.cn/nmip-media/channellive/channel103824/playlist.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s
- 地方频道 / 吉林乡村 / https://satellitepull.cnr.cn/live/wxjlxcgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 大宁综合 / http://live.daningtv.com/aac_dngb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 山东生活 / http://ls.qingting.fm/live/60260.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 嵊州新闻综合 / http://l.cztvcloud.com/channels/lantian/SXshengzhou1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 嵊泗综合 / http://l.cztvcloud.com/channels/lantian/SXshengsi1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 平湖新闻综合 / http://l.cztvcloud.com/channels/lantian/SXpinghu1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 平湖民生休闲 / http://l.cztvcloud.com/channels/lantian/SXpinghu2/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 平湖民生休闲 / http://l.cztvcloud.com/channels/lantian/SXpinghu2/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 12.5s
- 地方频道 / 庆元新闻综合 / http://l.cztvcloud.com/channels/lantian/SXqingyuan1/720p.m3u8?fbl= / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 庆元综合 / http://l.cztvcloud.com/channels/lantian/SXqingyuan1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 庆元综合 / http://l.cztvcloud.com/channels/lantian/SXqingyuan1/720p.m3u8?zzhed? / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 开化国家公园 / http://l.cztvcloud.com/channels/lantian/SXkaihua2/720p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 开化国家公园 / http://l.cztvcloud.com/channels/lantian/SXkaihua2/720p.m3u8zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 开化国家公园 / http://l.cztvcloud.com/channels/lantian/SXkaihua2/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 开化新闻综合 / http://l.cztvcloud.com/channels/lantian/SXkaihua1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 文成新闻综合 / http://l.cztvcloud.com/channels/lantian/SXwencheng1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 文成综合 / http://l.cztvcloud.com/channels/lantian/SXwencheng1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 文成综合 / http://l.cztvcloud.com/channels/lantian/SXwencheng1/720p.m3u8?zzhed? / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 新昌新闻综合 / https://l.cztvcloud.com/channels/lantian/SXxinchang1/720p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('_ssl.c:993: The handshake operation timed out')); last=URLError(TimeoutError('_ssl.c:993: The handshake operation timed out'))
- 地方频道 / 新闻综合 / https://m3u8channel.yunxya.com/nmip-media/channellive/channel100028/playlist.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s
- 地方频道 / 普陀电视台 / http://l.cztvcloud.com/channels/lantian/SXputuo1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded while reading media'); last=TimeoutError('timed out')
- 地方频道 / 普陀电视台 / https://l.cztvcloud.com/channels/lantian/SXputuo1/720p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('_ssl.c:993: The handshake operation timed out')); last=URLError(TimeoutError('_ssl.c:993: The handshake operation timed out'))
- 地方频道 / 松阳综合 / http://l.cztvcloud.com/channels/lantian/SXsongyang1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded while reading media'); last=TimeoutError('timed out')
- 地方频道 / 松阳综合 / http://l.cztvcloud.com/channels/lantian/SXsongyang1/720p.m3u8?zzhed? / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 柳河综合 / http://stream3.jlntv.cn:80/aac_lhgb/sd/live.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 桦甸综合 / http://stream9.jlntv.cn:80/aac_huadiangb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 梅河口综合 / http://stream3.jlntv.cn:80/aac_mhkgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 武义新闻综合 / http://l.cztvcloud.com/channels/lantian/SXwuyi1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 武义新闻综合 / http://l.cztvcloud.com/channels/lantian/SXwuyi1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 武汉一台新闻综合 / https://ls.qingting.fm/live/20198/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 永嘉新闻综合 / http://l.cztvcloud.com/channels/lantian/SXyongjia1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 河北农民 / http://ls.qingting.fm/live/1650.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 河北农民 / https://ls.qingting.fm/live/1650/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 河北都市 / https://radio.pull.hebtv.com/live/hebnczx.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 洞头综合 / http://l.cztvcloud.com/channels/lantian/SXdongtou1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 洞头综合 / http://l.cztvcloud.com/channels/lantian/SXdongtou1/720p.m3u8?zzhed? / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 浙江休闲台 / http://ali-m-l.cztv.com/channels/lantian/channel006/720p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江公共新闻 / http://ali-m-l.cztv.com/channels/lantian/channel07/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江公共新闻 / http://ali-m-l.cztv.com/channels/lantian/channel007/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江国际 / http://ali-vl.cztv.com/channels/lantian/channel010/360p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')); last=URLError(TimeoutError('timed out'))
- 地方频道 / 浙江国际 / http://ali-m-l.cztv.com/channels/lantian/channel010/720p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江国际 / http://ali-m-l.cztv.com/channels/lantian/channel010/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江国际 / https://ali-m-l.cztv.com/channels/lantian/channel010/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江少儿 / http://ali-vl.cztv.com/channels/lantian/channel008/360p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')); last=URLError(TimeoutError('timed out'))
- 地方频道 / 浙江少儿 / http://ali-m-l.cztv.com/channels/lantian/channel008/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江少儿 / https://ali-m-l.cztv.com/channels/lantian/channel008/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江教科 / http://ali-m-l.cztv.com/channels/lantian/channel004/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江教科影视 / http://ali-vl.cztv.com/channels/lantian/channel004/360p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')); last=URLError(TimeoutError('timed out'))
- 地方频道 / 浙江教科影视 / http://ali-m-l.cztv.com/channels/lantian/channel04/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江教科影视 / https://ali-m-l.cztv.com/channels/lantian/channel004/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江教育 / http://ali-m-l.cztv.com/channels/lantian/channel04/720p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江数码时代 / http://ali-m-l.cztv.com/channels/lantian/channel12/720p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
