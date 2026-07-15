# Published playlist recheck report

Elapsed: 106.0s
Rows before: 2530
Rows after: 2410
Removed rows: 120
Failed unique URLs: 118

## Group deltas

| Group | Before | After | Removed |
|---|---:|---:|---:|
| 央视频道 | 149 | 145 | 4 |
| 卫视频道 | 203 | 187 | 16 |
| 地方频道 | 524 | 507 | 17 |
| 影视剧场 | 160 | 130 | 30 |
| 少儿动漫 | 20 | 19 | 1 |
| 体育纪实 | 68 | 67 | 1 |
| 音乐综艺 | 47 | 47 | 0 |
| 生活休闲 | 180 | 171 | 9 |
| 综合娱乐 | 900 | 884 | 16 |
| 港澳台频道 | 59 | 59 | 0 |
| 海外华语频道 | 220 | 194 | 26 |

## First failed rows

- 央视频道 / CCTV-1 / http://38.75.136.137:98/gslb/dsdqbv/cctv1hd.m3u8?auth=test20251009 / bad marker/html
- 央视频道 / CCTV-4FHD / https://stream1.freetv.fun/5ecad9013e2ea27f67c57feed0633c32297275f5be83a25917869edbbcbba0b0.m3u8 / <HTTPError 404: 'Not Found'>
- 央视频道 / CCTV-14 / http://61.136.172.236:9901/tsfile/live/0014_1.m3u8?key=txiptv&playlive=1&authid=0 / TimeoutError('timed out')
- 央视频道 / CCTV-16 / http://gmxw.7766.org:808/hls/169/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 河北卫视 / http://173.208.212.130:8181/720p/hews.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=1
- 卫视频道 / 河北卫视 / http://204.12.221.218:8181/3m1080p/hews.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=1
- 卫视频道 / 广东卫视 / http://204.12.221.218:8181/3m1080p/gdws.m3u8 / bad marker/html
- 卫视频道 / 广东卫视 / http://63.141.230.178:82/gslb/zbdq5.m3u8?id=gdwshd / bad marker/html
- 卫视频道 / 内蒙古卫视 / http://182.150.23.74:808/hls/37/index.m3u8 / URLError(TimeoutError('timed out'))
- 卫视频道 / 大湾区卫视 / http://gmxw.7766.org:808/hls/132/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 宁夏卫视 / http://cssbyd.imwork.net:8082/hls/45/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 山西卫视 / http://119.39.9.8:9901/tsfile/live/0118_1.m3u8 / bad marker/html
- 卫视频道 / 山西卫视 / https://live.264788.xyz/channel/shanxiweishi?streamid=69e002ac7467d661ff7ad0671ed43f16&livekey=01WgOR41rriMmMkzNsd0UoaxJRwetZdxIvtVk / variant fail variants_checked=1 child bad 200
- 卫视频道 / 广东卫视4K / https://live.264788.xyz/channel/guangdongweishi4k?streamid=33aeafbb59f2bcb1877c3a8229c0135b&livekey=01WgOR41rriMmMkzNsd0UoaxJRwetZdxIvtVk / variant fail variants_checked=1 child bad 200
- 卫视频道 / 延边卫视 / http://gmxw.7766.org:808/hls/15/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 江西卫视 / http://61.136.172.236:9901/tsfile/live/0138_1.m3u8?key=txiptv&playlive=1&authid=0 / bad marker/html
- 卫视频道 / 江西卫视 / http://61.136.172.236:9901/tsfile/live/0138_1.m3u8 / bad marker/html
- 卫视频道 / 湖北卫视 / http://198.204.228.26/live/hbwshd.m3u8 / bad marker/html
- 卫视频道 / 湖北卫视 / http://107.150.60.122/live/hbwshd.m3u8 / bad marker/html
- 卫视频道 / 甘肃卫视 / http://218.13.170.98:9901/tsfile/live/0141_1.m3u8 / TimeoutError('timed out')
- 地方频道 / 合肥新闻 / http://112.27.235.94:8000/hls/18/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 天津衛視 / https://stream1.freetv.fun/a700de96dc13188f1532d89bbb699c4232e8c8c62418eaca13e737017ea8eec7.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 山西衛視 / https://stream1.freetv.fun/7134b52d41c5da0ebefe4234424eb6e81cb40844c3c32dec3bb8ec46c333c129.ctv / variant fail variants_checked=1 child bad 200
- 地方频道 / 山西衛視 / https://stream1.freetv.fun/2f538e8c3c3dc60b99799fb3331f5f05b5a9c3c574544b4178a57a7de78f6884.m3u8 / variant fail variants_checked=1 child bad 200
- 地方频道 / 广东体育 / http://183.11.239.36:808/hls/2/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 广东珠江 / http://183.11.239.36:808/hls/83/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 广东珠江 / http://gmxw.7766.org:808/hls/83/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 欢笑剧场4K / https://live.264788.xyz/channel/huanxiaojuchang4k?streamid=3f4d4c40dbf41fd4a37dfa73878e39e1&livekey=01WgOR41rriMmMkzNsd0UoaxJRwetZdxIvtVk / variant fail variants_checked=1 child bad 200
- 地方频道 / 津南一套 / http://play.jinnantv.top/live/JNTV1.m3u8?ztianjd / TimeoutError('timed out')
- 地方频道 / 浙江少兒頻道 / https://stream1.freetv.fun/d148043df6b2f6d9464b41a73a6da05d758d0ad15a0d1d8a38a95b817d0a34e3.ctv / TimeoutError('timed out')
- 地方频道 / 浙江民生休闲 / http://ali-vl.cztv.com/channels/lantian/channel006/360p.m3u8 / TimeoutError('timed out')
- 地方频道 / 湖北衛視 / https://stream1.freetv.fun/37aa38a997eb8e568186fad85670c3a3a6684361c2b038c5cd0d0835216f299b.m3u8 / variant fail variants_checked=1 child bad 200
- 地方频道 / 湖北衛視 / https://stream1.freetv.fun/622bdb14c81d58a5d35bce8ec1e1d77b9bc0a6986148e1d0eff2bffd552c9b88.m3u8 / variant fail variants_checked=1 child bad 200
- 地方频道 / 湖北衛視 / https://stream1.freetv.fun/2393ff19f0698372b15cdb49722ac208125de613259d1235631a2f33850641ca.m3u8 / variant fail variants_checked=1 child bad 200
- 地方频道 / 湖南經視 / https://stream1.freetv.fun/083dd83573e39b2be5781d200c5bf2e046f39104e90d3bbca658d5a40d53d5f0.m3u8 / variant fail variants_checked=1 child bad 200
- 地方频道 / 福建新闻 / http://satellitepull.cnr.cn/live/wx32fjxwgb/playlist.m3u8 / bad marker/html
- 地方频道 / 西藏衛視 / https://stream1.freetv.fun/dd47ba03fe77064ea4e0978637231bce94e7554c9f8f6a020195311829752aed.m3u8 / <HTTPError 404: 'Not Found'>
- 影视剧场 / 刘德华电影 / http://cdn.jdshipin.com:8880/huya.php?id=11342424 / <HTTPError 403: 'Forbidden'>
- 影视剧场 / 古装剧 / https://live.ottiptv.cc/yy/1356158015 / TimeoutError('The read operation timed out')
- 影视剧场 / 国产电影-就是闹着玩的 / https://live.ottiptv.cc/yy/1354931503 / bad marker/html
- 影视剧场 / 国内高分悬疑剧-风筝 / https://live.ottiptv.cc/yy/1354931585 / bad marker/html
- 影视剧场 / 寻秦记-穿越剧经典 / https://live.ottiptv.cc/yy/1382851591 / TimeoutError('timed out')
- 影视剧场 / 岳云鹏宋小宝也来演电影了？ / https://live.ottiptv.cc/yy/1354926612 / TimeoutError('timed out')
- 影视剧场 / 成龙电影 / http://cdn.jdshipin.com:8880/huya.php?id=11342386 / <HTTPError 403: 'Forbidden'>
- 影视剧场 / 末日电影合集 / https://live.ottiptv.cc/yy/1354889019 / bad marker/html
- 影视剧场 / 末日系列-外国电影合集 / https://live.ottiptv.cc/yy/1354889019 / bad marker/html
- 影视剧场 / 电影梁家辉 / http://live.metshop.top/huya/11342429?cdn=alicdn / RemoteDisconnected('Remote end closed connection without response')
- 影视剧场 / 电影百团大战 / https://live.ottiptv.cc/yy/1382736871 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 电影黑豹 / https://live.ottiptv.cc/yy/1382736816 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 电视剧-流金岁月 / https://live.ottiptv.cc/yy/1382749906 / TimeoutError('The read operation timed out')
- 影视剧场 / 碟中谍系列电影 / https://live.ottiptv.cc/yy/1382736836 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 科幻电影 / https://live.ottiptv.cc/yy/1354930209 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 笑傲江湖-电视剧 / https://live.ottiptv.cc/yy/1354936128 / TimeoutError('The read operation timed out')
- 影视剧场 / 粟裕大将-影视 / https://live.ottiptv.cc/yy/1354926542 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 精彩动作电影享不停 / https://live.ottiptv.cc/yy/1382736809 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 经典电影港片枪战 / https://live.ottiptv.cc/yy/1355076627 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 经典破案剧代练王者 / https://live.ottiptv.cc/yy/1353283667 / TimeoutError('The read operation timed out')
- 影视剧场 / 缺宅男女-精彩港剧 / https://live.ottiptv.cc/yy/1382745088 / TimeoutError('The read operation timed out')
- 影视剧场 / 老妖私影院 / https://live.ottiptv.cc/yy/1354952229 / TimeoutError('The read operation timed out')
- 影视剧场 / 许光汉主演喜剧大片 / https://live.ottiptv.cc/yy/1382736825 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 赌神港片喜剧 / https://live.ottiptv.cc/yy/1355112116 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 超精彩！系列动作电影 / https://live.ottiptv.cc/yy/1382745096 / bad marker/html
- 影视剧场 / 辉煌或疯狂-韩剧 / https://live.ottiptv.cc/yy/1382749902 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 这部剧你居然没看过？ / https://live.ottiptv.cc/yy/1354932355 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 金庸武侠天龙八部 / https://live.ottiptv.cc/yy/1352300646 / TimeoutError('The read operation timed out')
- 影视剧场 / 金牌喜剧班 / https://live.ottiptv.cc/yy/1354889009 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 金玉满堂：精彩港剧 / https://live.ottiptv.cc/yy/1382736881 / TimeoutError('The read operation timed out')
- 少儿动漫 / 卡酷少儿 / http://218.13.170.98:9901/tsfile/live/1021_1.m3u8 / TimeoutError('timed out')
- 体育纪实 / 金鹰纪实 / https://t.freetv.fun/live/jin-ying-ji-shi-2.m3u8 / variant fail variants_checked=1 child bad 200
- 生活休闲 / papi酱主演，北漂生活中的爱情与梦想 / https://live.ottiptv.cc/yy/1382745124 / bad marker/html
- 生活休闲 / 体验另一种生活！ / https://live.ottiptv.cc/yy/1354936229 / TimeoutError('The read operation timed out')
- 生活休闲 / 固镇新闻 / http://www.guzhenm.com:7001/hls/hd-live.m3u8 / <HTTPError 404: 'Not Found'>
- 生活休闲 / 海宁新闻综合 / https://p2hs.vzan.com/slowlive/317913155078575177/live.m3u8 / bad marker/html
- 生活休闲 / 海宁新闻综合 / http://p2hs.vzan.com/slowlive/317913155078575177/live.m3u8 / bad marker/html
- 生活休闲 / 海宁新闻综合 / https://p2hs.vzan.com/slowlive/317913155078575177/live.m3u8?zbid=293304&tpid=1708007815 / bad marker/html
- 生活休闲 / 生活時尚 / https://stream1.freetv.fun/af577cd69d640274bdefa24125bfba424d35044c1235f7a429a7e85a00fc41e4.ctv / variant fail variants_checked=1 no segment
- 生活休闲 / 绍兴新闻 / http://live.shaoxing.com.cn/video/s10001-sxtv1/index.m3u8?zzhed? / <HTTPError 404: 'Not Found'>
- 生活休闲 / 绍兴新闻综合 / http://live.shaoxing.com.cn/video/s10001-sxtv1/index.m3u8?zzhed / <HTTPError 404: 'Not Found'>
- 综合娱乐 / HK港鬼片(🚀) / http://epg.112114.eu.org/douyu/8009547 / TimeoutError('timed out')
- 综合娱乐 / ▶️毒液：致命守护者 / https://www.goodiptv.club/yy/1382745095 / bad marker/html
