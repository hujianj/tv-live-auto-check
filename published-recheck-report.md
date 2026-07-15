# Published playlist recheck report

Elapsed: 126.9s
Rows before: 2569
Rows after: 2447
Removed rows: 122
Failed unique URLs: 119

## Group deltas

| Group | Before | After | Removed |
|---|---:|---:|---:|
| 央视频道 | 148 | 145 | 3 |
| 卫视频道 | 210 | 206 | 4 |
| 地方频道 | 528 | 498 | 30 |
| 影视剧场 | 172 | 155 | 17 |
| 少儿动漫 | 26 | 21 | 5 |
| 体育纪实 | 69 | 69 | 0 |
| 音乐综艺 | 51 | 50 | 1 |
| 生活休闲 | 180 | 172 | 8 |
| 综合娱乐 | 900 | 878 | 22 |
| 港澳台频道 | 65 | 65 | 0 |
| 海外华语频道 | 220 | 188 | 32 |

## First failed rows

- 央视频道 / CCTV-1 / http://112.46.85.60:8009/hls/501/index.m3u8 / <HTTPError 404: 'Not Found'>
- 央视频道 / CCTV-5 / http://124.116.183.146:9901/tsfile/live/0005_1.m3u8 / bad marker/html (core retry after first=TimeoutError('timed out'))
- 央视频道 / CCTV-5 / http://123.130.84.106:8154/tsfile/live/0005_1.m3u8 / <HTTPError 404: 'Not Found'> (core retry after first=TimeoutError('timed out'))
- 卫视频道 / 东方卫视 / http://112.46.85.60:8009/hls/31/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 吉林卫视 / http://cssbyd.imwork.net:8082/hls/41/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 海南卫视 / http://cssbyd.imwork.net:8082/hls/31/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 黑龙江卫视 / http://218.13.170.98:9901/tsfile/live/1006_1.m3u8 / bad marker/html (core retry after first=TimeoutError('timed out'))
- 地方频道 / 四川衛視 / https://stream1.freetv.fun/a9bd3a65e221b7781803b40226f113f9ce0fb6aa7ae42ac76115c6142bc18956.ctv / variant fail variants_checked=1 child bad 200
- 地方频道 / 四川衛視 / https://stream1.freetv.fun/1f0236ac4b2a4c1ee3c72d18710342dbc885bb3a42713c9889b2e647d0f9458f.ctv / bad marker/html
- 地方频道 / 固镇新闻 / http://www.guzhenm.com:7001/hls/hd-live.m3u8?%E5%85%B3%E6%B3%A8%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7[%E6%99%B4%E5%9B%AD] / <HTTPError 404: 'Not Found'>
- 地方频道 / 安徽衛視 / https://stream1.freetv.fun/4c2c313a8d2ebef4ad9b9a71d735b7b2308394f3376b5376fdbe5d77cc5e9719.ctv / TimeoutError('The read operation timed out')
- 地方频道 / 山东体育 / http://123.130.84.106:8154/tsfile/live/1006_1.m3u8?key=txiptv&playlive=1&authid=0 / TimeoutError('timed out')
- 地方频道 / 山东体育 / http://123.130.84.106:8154/tsfile/live/1006_1.m3u8 / TimeoutError('timed out')
- 地方频道 / 山东齐鲁 / http://123.130.84.106:8154/tsfile/live/1001_1.m3u8?key=txiptv&playlive=1&authid=0 / TimeoutError('timed out')
- 地方频道 / 山西衛視 / https://stream1.freetv.fun/62585ca065b0e50a8dc91b341acc3323d2f0e3da55c4c42f159731e6e13b2864.m3u8 / TimeoutError('timed out')
- 地方频道 / 广东广播 / http://ls.qingting.fm/live/1260.m3u8 / TimeoutError('timed out')
- 地方频道 / 广西新闻 / http://107.150.60.122/live/gxxw.m3u8 / bad marker/html
- 地方频道 / 广西新闻 / http://198.204.228.26/live/gxxw.m3u8 / bad marker/html
- 地方频道 / 广西新闻 / http://192.151.150.154/live/gxxw.m3u8 / bad marker/html
- 地方频道 / 广西新闻 / http://63.141.230.178:82/gslb/zbdq5.m3u8?id=gxxw / bad marker/html
- 地方频道 / 广西新闻 / http://38.75.136.137:98/gslb/dsdqpub/gxxw.m3u8?auth=testpub / bad marker/html
- 地方频道 / 欢笑剧场4K / https://live.264788.xyz/channel/huanxiaojuchang4k?streamid=3f4d4c40dbf41fd4a37dfa73878e39e1&livekey=01WgOR41rriMmMkzNsd0UoaxJRwetZdxIvtVk / variant fail variants_checked=1 no segment
- 地方频道 / 江西衛視 / https://stream1.freetv.fun/2ffc9bf43e10963bfbbf5e9cc7bd37c187bf6ebcae5087611a2adc38ef768a02.ctv / variant fail variants_checked=1 child bad 200
- 地方频道 / 河北农民 / https://ls.qingting.fm/live/1650/64k.m3u8 / URLError(TimeoutError('_ssl.c:993: The handshake operation timed out'))
- 地方频道 / 河北衛視 / https://stream1.freetv.fun/b6d7e54d6c1e48b22b610cdd9db9d9c1e209cfabadd2bc08c0a4c2717db86af4.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 河北衛視 / https://stream1.freetv.fun/b1b70c0ba5ae4a14b5325b4ced18b94dd2423b228895e62c705cf91ef625219c.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 河北衛視 / https://stream1.freetv.fun/001dee3ca98c60752fbb8ec283d79ca4e36ea48e670272f0754e21c08193992d.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 河南新闻 / http://1.94.31.214/php/hntv.php?id=hnxw / bad marker/html
- 地方频道 / 浙江Ⅰ绍兴综合(576p) / http://live.shaoxing.com.cn/video/s10001-sxtv1/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 深圳衛視 / https://stream1.freetv.fun/98f8902bd23ba7c63ca9a36ca0da0174daa74ed1cf4600d534a6a7a60791292c.m3u8 / TimeoutError('timed out')
- 地方频道 / 湖南衛視 / https://stream1.freetv.fun/c2f03cab64820fb4523ac394df4f84b0ce428b8d5b2cedde07ce375f0ad3b23a.ctv / TimeoutError('The read operation timed out')
- 地方频道 / 湖南衛視 / https://stream1.freetv.fun/9849915f8a0c20f979b1595d3d1f4825391dbe83d2151fe4135433ea45a422d5.ctv / TimeoutError('The read operation timed out')
- 地方频道 / 湖南衛視 / https://stream1.freetv.fun/e876e6dcce030ba1fed2b1eed597ccc0fc4a0a1caf19e9e18860fd84ac93a7ee.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 铜梁综合 / http://183.64.174.171:40123/ch1.m3u8?zzhongqd / <HTTPError 404: 'Not Found'>
- 地方频道 / 长子综合 / https://www.wxhcgbds.com:8081/channelTv/WXTV_1.m3u8?zshanxd / bad marker/html
- 地方频道 / 陕西新闻咨询 / http://112.46.105.20:8009/hls/18/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 陕西都市青春 / http://112.46.105.20:8009/hls/19/index.m3u8 / <HTTPError 404: 'Not Found'>
- 影视剧场 / 24h我爱我家喜剧 / https://live.ottiptv.cc/yy/1356212303 / <HTTPError 404: 'Not Found'>
- 影视剧场 / 喜剧闹翻天 / https://live.ottiptv.cc/yy/1382735548 / TimeoutError('timed out')
- 影视剧场 / 国产动作电影 / https://live.ottiptv.cc/yy/1382736858 / bad marker/html
- 影视剧场 / 国产电影-就是闹着玩的 / https://live.ottiptv.cc/yy/1354931503 / bad marker/html
- 影视剧场 / 天龙八部 / https://live.ottiptv.cc/yy/1351814644 / bad marker/html
- 影视剧场 / 憨豆先生-经典喜剧 / https://live.ottiptv.cc/yy/1354936239 / TimeoutError('timed out')
- 影视剧场 / 枪战电影 / http://cdn.jdshipin.com:8880/huya.php?id=21059579 / RemoteDisconnected('Remote end closed connection without response')
- 影视剧场 / 橙记港剧 / http://www.goodiptv.club/douyu/4549169 / <HTTPError 403: 'Forbidden'>
- 影视剧场 / 港片喜剧动作 / https://live.ottiptv.cc/yy/1355480591 / bad marker/html
- 影视剧场 / 电影百团大战 / https://live.ottiptv.cc/yy/1382736871 / TimeoutError('timed out')
- 影视剧场 / 破案港剧 / https://live.ottiptv.cc/yy/1350670730 / TimeoutError('timed out')
- 影视剧场 / 碟中谍系列电影 / https://live.ottiptv.cc/yy/1382736836 / bad marker/html
- 影视剧场 / 经典破案剧代练王者 / https://live.ottiptv.cc/yy/1353283667 / <HTTPError 404: 'Not Found'>
- 影视剧场 / 邵氏影院 / http://www.goodiptv.club/douyu/4246519 / <HTTPError 403: 'Forbidden'>
- 影视剧场 / 金玉满堂：精彩港剧 / https://live.ottiptv.cc/yy/1382736881 / bad marker/html
- 影视剧场 / 非常保镖-经典港剧 / https://live.ottiptv.cc/yy/1382736903 / TimeoutError('timed out')
- 影视剧场 / 鬼片喜剧动作港剧 / https://live.ottiptv.cc/yy/1355269576 / <HTTPError 404: 'Not Found'>
- 少儿动漫 / 福州少儿 / http://live.zohi.tv/video/s10001-fztv-4/index.m3u8 / bad marker/html
- 少儿动漫 / 福州电视台少儿频道(FZTV-少儿)(1080p) / http://live.zohi.tv/video/s10001-fztv-4/index.m3u8 / bad marker/html
- 少儿动漫 / 精彩动漫 / https://live.ottiptv.cc/yy/1420843376 / bad marker/html
- 少儿动漫 / 金鷹卡通 / https://stream1.freetv.fun/d20d03fc60ad339d49e1d54e4379efc257a119c0a7ac7ab767e40d1823d7f89c.ctv / TimeoutError('The read operation timed out')
- 少儿动漫 / 金鹰卡通 / http://183.11.239.36:808/hls/69/index.m3u8 / <HTTPError 404: 'Not Found'>
- 音乐综艺 / 音乐_AT_KroneHit / http://bitcdn-kronehit.bitmovin.com/v2/hls/master.m3u8 / variant fail variants_checked=2 no segment
- 生活休闲 / 体验另一种生活！ / https://live.ottiptv.cc/yy/1354936229 / bad marker/html
- 生活休闲 / 哈尔滨新闻综合 / http://stream.hrbtv.net/xwzh/sd/live.m3u8 / URLError(TimeoutError('timed out'))
- 生活休闲 / 嘉禾新闻综合 / https://liveplay-srs.voc.com.cn/hls/tv/184_e3af1a.m3u8 / bad marker/html
- 生活休闲 / 晉城公共 / https://stream1.freetv.fun/906138969e04bb17662c36afe229862daf7f6d4f21e727ef3f9c2e6647a82435.m3u8 / variant fail variants_checked=1 child bad 200
- 生活休闲 / 生活时尚 / https://stream1.freetv.fun/sheng-huo-shi-shang-2.ctv / TimeoutError('The read operation timed out')
- 生活休闲 / 生活時尚 / https://stream1.freetv.fun/7234712007b11f36984751e7346e2892a373748f836997863fa50f1c0892e1c1.ctv / variant fail variants_checked=1 child bad 200
- 生活休闲 / 绍兴新闻综合 / http://live.shaoxing.com.cn/video/s10001-sxtv1/index.m3u8 / <HTTPError 404: 'Not Found'>
- 生活休闲 / 绍兴电视台公共 / http://live.shaoxing.com.cn/video/s10001-sxtv2/index.m3u8?zzhed / <HTTPError 404: 'Not Found'>
- 综合娱乐 / 上虞综合 / http://l.cztvcloud.com/channels/lantian/SXzhuji3/720p.m3u8?zzhed? / bad marker/html
- 综合娱乐 / 兵器科技 / http://173.208.212.130:8181/720p/gfjs.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=2
- 综合娱乐 / 兵器科技 / http://63.141.230.178:82/gslb/zbdq5.m3u8?id=gfjs / segment bad 200 video/mp2t bytes=4096 checked=2
- 综合娱乐 / 動漫秀場 / https://stream1.freetv.fun/73a696031fc8f1fdb15ef76f1739f184c8e5d828d6d98225ce1a8a3ed4371ce5.ctv / variant fail variants_checked=1 child bad 200
- 综合娱乐 / 動漫秀場 / https://stream1.freetv.fun/01338fd08b1718f396da23e41d0f2ac8781b971adb8fb69e48b9f365f2f68470.ctv / TimeoutError('The read operation timed out')
- 综合娱乐 / 华语金曲500首 / http://ls.qingting.fm/live/3412131.m3u8 / bad marker/html
- 综合娱乐 / 发起进攻 / https://live.ottiptv.cc/bilibili/691836 / <HTTPError 404: 'Not Found'>
- 综合娱乐 / 吉首综合 / https://liveplay-srs.voc.com.cn/hls/tv/143_70175b.m3u8 / <HTTPError 404: 'Not Found'>
- 综合娱乐 / 哈哈炫動 / https://stream1.freetv.fun/eb5f5043576df8dd2010842c01a50be553e41c876df908dd14018ed306f35411.ctv / TimeoutError('The read operation timed out')
- 综合娱乐 / 哈爾濱娛樂 / https://stream1.freetv.fun/2bbb83987353f278de8023703a2c974ccdd5042777367191c1b91edaeab5eedd.m3u8 / URLError(TimeoutError('timed out'))
- 综合娱乐 / 嘉峪关综合 / http://play.kankanlive.com/live/1720583434627241.m3u8 / TimeoutError('timed out')
- 综合娱乐 / 少年包青天第一部 / https://live.ottiptv.cc/yy/1356043677 / bad marker/html
