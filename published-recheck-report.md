# Published playlist recheck report

Outputs rewritten: True
Elapsed: 246.6s
Rows before: 408
Rows after: 299
Rows removed from outputs: 109
Candidate rows failing strict recheck: 109
Rows refilled after strict recheck: 0
Net output row delta: -109
Failed unique URLs after slow retry: 109
Slow retry attempted unique URLs: 114
Slow retry recovered unique URLs: 5
Core live-progress check required: True
Broadcast live-progress check required: True
Live-progress groups: 卫视频道, 地方频道, 央视频道
Video track required: True
Video-track verified final unique URLs: 299
Refill attempted unique URLs: 0
Refill playable unique URLs: 0
Refilled rows: 0
Historical fallback candidates attempted: 0
Historical fallback rows accepted: 0
Unresolved refill rows: 109

## Group deltas

| Group | Before | After | Net delta |
|---|---:|---:|---:|
| 央视频道 | 21 | 21 | +0 |
| 卫视频道 | 23 | 17 | -6 |
| 地方频道 | 200 | 128 | -72 |
| 影视剧场 | 65 | 63 | -2 |
| 少儿动漫 | 2 | 2 | +0 |
| 体育纪实 | 25 | 15 | -10 |
| 音乐综艺 | 19 | 1 | -18 |
| 综合娱乐 | 52 | 51 | -1 |
| 港澳台频道 | 1 | 1 | +0 |

## First failed rows

- 卫视频道 / 东方卫视 / http://bp-resource-dfl.bestv.cn/155/3/video.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 东方卫视 / http://bp-resource-dfl.bestv.cn/148/3/video.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 东方卫视 / https://bp-resource-dfl.bestv.cn/148/3/video.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 浙江卫视 / http://ali-vl.cztv.com/channels/lantian/channel001/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 广东卫视 / https://txmov2.a.kwimgs.com/upic/2023/01/26/09/BMjAyMzAxMjYwOTE3NDVfNzM5MzQzNzIyXzk0NjI1OTUwNTA3XzBfMw==_b_B81ddda927d33445d544befd008e60109.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 卫视频道 / 大湾区卫视 / http://222.128.55.152:9080/live/dwq.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s; last=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s
- 地方频道 / 三明新闻综合 / http://ls.qingting.fm/live/4885.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 三明新闻综合 / https://ls.qingting.fm/live/5022100/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 上海第一财经 / https://satellitepull.cnr.cn/live/wx32dycjgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 东丰综合 / http://stream3.jlntv.cn:80/aac_dfgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 任丘综合 / https://jwcdnqx.hebyun.com.cn/live/rqtv1/1500k/tzwj_video.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 余姚姚江文化 / http://l.cztvcloud.com/channels/lantian/SXyuyao3/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 12.5s
- 地方频道 / 余姚新闻综合 / http://l.cztvcloud.com/channels/lantian/SXyuyao1/720p.m3u8?cWlkPSZzPTg3OWMwYmMyZDMzYTFhZGY3NDQxMjgyYTg1MmUzNTY0JmVzPTE3MDY2Nzc4NzMmdXVpZD0yMjdiY2MzNGNiNGY0MThlYjRiY2IxYzcwNmZjODNkMS02NzQ3NDY2NyZ2PTImYXM9MCZjZG5leF9pZD10eF9waG9uZV9saXZl / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 余杭未来E / http://l.cztvcloud.com/channels/lantian/SXyuhang3/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('URL total budget exceeded while reading media')
- 地方频道 / 六安公共 / http://ls.qingting.fm/live/1794199.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 六安新闻综合 / http://ls.qingting.fm/live/267.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 北京新闻 / https://satellitepull.cnr.cn/live/wxbjxwgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 双辽综合 / http://stream3.jlntv.cn:80/aac_slgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 可克达拉综合 / http://file.loulannews.cn/nmip-media/channellive/channel103824/playlist.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s
- 地方频道 / 吉林乡村 / https://satellitepull.cnr.cn/live/wxjlxcgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 大宁综合 / http://live.daningtv.com/aac_dngb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 山东生活 / http://ls.qingting.fm/live/60260.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 开化国家公园 / http://l.cztvcloud.com/channels/lantian/SXkaihua2/720p.m3u8zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 开化国家公园 / http://l.cztvcloud.com/channels/lantian/SXkaihua2/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 开化新闻综合 / http://l.cztvcloud.com/channels/lantian/SXkaihua1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 文成综合 / http://l.cztvcloud.com/channels/lantian/SXwencheng1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 文成综合 / http://l.cztvcloud.com/channels/lantian/SXwencheng1/720p.m3u8?zzhed? / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('URL total budget exceeded')
- 地方频道 / 新闻综合 / https://m3u8channel.yunxya.com/nmip-media/channellive/channel100028/playlist.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s
- 地方频道 / 柳河综合 / http://stream3.jlntv.cn:80/aac_lhgb/sd/live.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 桦甸综合 / http://stream9.jlntv.cn:80/aac_huadiangb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 梅河口综合 / http://stream3.jlntv.cn:80/aac_mhkgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 武义新闻综合 / http://l.cztvcloud.com/channels/lantian/SXwuyi1/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 武汉一台新闻综合 / https://ls.qingting.fm/live/20198/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 武进生活 / http://live.wjyanghu.com/live/CH2.m3u8 / final slow retry failed attempt=1 first=TimeoutError('The read operation timed out'); last=<HTTPError 502: 'Bad Gateway'>
- 地方频道 / 永嘉新闻综合 / http://l.cztvcloud.com/channels/lantian/SXyongjia1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 汾西综合 / https://qmmqvzoz.live.sxmty.com/live/hls/f24f8a390c084386a564074c9260100c/be3fdf07606145739ab2c4b80fe0136a.m3u8?zshanxd / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')); last=URLError(TimeoutError('timed out'))
- 地方频道 / 河北农民 / http://ls.qingting.fm/live/1650.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 河北农民 / https://ls.qingting.fm/live/1650/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 河北都市 / https://radio.pull.hebtv.com/live/hebnczx.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 浙江国际 / http://ali-vl.cztv.com/channels/lantian/channel010/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江少儿 / http://ali-vl.cztv.com/channels/lantian/channel008/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江教科影视 / http://ali-vl.cztv.com/channels/lantian/channel004/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江新闻 / http://ali-vl.cztv.com/channels/lantian/channel007/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江民生休闲 / http://ali-vl.cztv.com/channels/lantian/channel006/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江生活 / http://ls.qingting.fm/live/1099.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 浙江留学 / http://ali-vl.cztv.com/channels/lantian/channel009/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 浙江经济生活 / http://ali-vl.cztv.com/channels/lantian/channel003/360p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 地方频道 / 海南新闻 / http://ls.qingting.fm/live/1861.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 灌阳新闻综合 / https://ls.qingting.fm/live/5043/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 甘肃经济 / https://satellitepull.cnr.cn/live/wxgshhzs/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 甘肃都市 / https://satellitepull.cnr.cn/live/wxgsdstb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 磐石综合 / http://stream3.jlntv.cn:80/aac_psgb/sd/live.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 福建新闻 / http://satellitepull.cnr.cn/live/wx32fjxwgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 福建经济 / http://satellitepull.cnr.cn/live/wx32fjdnjjgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 第一财经 / http://satellitepull.cnr.cn/live/wx32dycjgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 缙云新闻综合 / http://l.cztvcloud.com/channels/lantian/SXjinyun1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 营山电视台 / http://file.ysxtv.cn/cms/videos/nmip-media/channellive/channel4/playlist.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 7.5s
- 地方频道 / 萧山生活 / http://l.cztvcloud.com/channels/lantian/SXxiaoshan2/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 萧山生活 / http://l.cztvcloud.com/channels/lantian/SXxiaoshan2/720p.m3u8?zzhed? / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 衡水公共 / http://ls.qingting.fm/live/2810.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 衡阳新闻综合 / https://liveplay-srs.voc.com.cn/hls/tv/183_554704.m3u8 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded'); last=TimeoutError('URL total budget exceeded')
- 地方频道 / 诸暨新闻综合 / http://l.cztvcloud.com/channels/lantian/SXzhuji3/720p.m3u8?zzhed / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded while reading media'); last=TimeoutError('timed out')
- 地方频道 / 象山新闻综合 / http://l.cztvcloud.com/channels/lantian/SXxiangshan1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('URL total budget exceeded while reading media')
- 地方频道 / 辽宁都市 / https://ls.qingting.fm/live/1099/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 通化县综合 / http://stream3.jlntv.cn:80/aac_thxgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 邯郸新闻 / https://jwcdnqx.hebyun.com.cn/live/hdxwzh/1500k/tzwj_video.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 13.8s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 13.8s
- 地方频道 / 邯郸科技教育 / https://jwcdnqx.hebyun.com.cn/live/hdkj/1500k/tzwj_video.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 12.5s; last=segments ok checked=2 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 12.5s
- 地方频道 / 都市剧场 / https://satellitepull.cnr.cn/live/wxcqxwgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 铜陵新闻综合 / https://ls.qingting.fm/live/21303/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 镇江新闻综合 / http://cm-wshls.homecdn.com/live/2aa50.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')); last=URLError(TimeoutError('timed out'))
- 地方频道 / 陕西公共 / http://ls.qingting.fm/live/1222.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 青田电视台 / http://l.cztvcloud.com/channels/lantian/SXqingtian1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 地方频道 / 靖宇综合 / http://stream9.jlntv.cn:80/aac_jygb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 靖江新闻综合 / http://ls.qingting.fm/live/23797.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 黑龙江少儿 / https://ls.qingting.fm/live/4972/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 黑龙江新闻 / https://ls.qingting.fm/live/4974/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 龙井综合 / http://stream9.jlntv.cn:80/aac_longjinggb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 龙泉新闻综合 / http://l.cztvcloud.com/channels/lantian/SXlongquan1/720p.m3u8 / final slow retry failed attempt=1 first=TimeoutError('timed out'); last=TimeoutError('timed out')
- 影视剧场 / 倩女幽魂人间道 / http://jsmov2.a.yximgs.com/bs3/video-hls/5250634317044855747_hlsb.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
- 影视剧场 / 倩女幽魂妖魔道 / http://jsmov2.a.yximgs.com/bs3/video-hls/5232901391302199073_hlsb.m3u8 / final slow retry failed attempt=1 first=VOD/endlist or unsupported byte-range media playlist; last=VOD/endlist or unsupported byte-range media playlist
