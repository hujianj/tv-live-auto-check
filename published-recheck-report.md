# Published playlist recheck report

Elapsed: 142.6s
Rows before: 2521
Rows after: 2366
Removed rows: 155
Failed unique URLs: 150

## Group deltas

| Group | Before | After | Removed |
|---|---:|---:|---:|
| 央视频道 | 148 | 145 | 3 |
| 卫视频道 | 197 | 193 | 4 |
| 地方频道 | 507 | 496 | 11 |
| 影视剧场 | 168 | 145 | 23 |
| 少儿动漫 | 24 | 24 | 0 |
| 体育纪实 | 68 | 65 | 3 |
| 音乐综艺 | 48 | 46 | 2 |
| 生活休闲 | 180 | 171 | 9 |
| 综合娱乐 | 900 | 875 | 25 |
| 港澳台频道 | 61 | 61 | 0 |
| 海外华语频道 | 220 | 145 | 75 |

## First failed rows

- 央视频道 / CCTV-4中文國際歐洲 / https://stream1.freetv.fun/5ee007c8e8f5be19c14a8ae3bb945ee49b458b43c0017da6cf2c0eb2ba3cd358.ctv / variant fail variants_checked=1 no segment
- 央视频道 / CCTV-4中文國際歐洲 / https://stream1.freetv.fun/358675f37907cd68af9be4cf1984d5ddd672246ab766c711dd3db3aa2ca53c6d.ctv / variant fail variants_checked=1 child bad 200
- 央视频道 / CCTV-9(576i) / https://xykt-fix.github.io/Y77.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 内蒙古卫视 / https://live.264788.xyz/channel/neimengguweishi?streamid=3e7340acf8869ac1c7dad1bb836dcd35&livekey=01WgOR41rriMmMkzNsd0UoaxJRwetZdxIvtVk / variant fail variants_checked=1 child bad 200
- 卫视频道 / 宁夏卫视 / http://cssbyd.imwork.net:8082/hls/45/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 新疆卫视 / http://183.11.239.36:808/hls/65/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 新疆卫视 / http://218.84.12.186:8001/hls/main/playlist.m3u8?zxinjd / <HTTPError 404: 'Not Found'>
- 地方频道 / 广东体育 / http://63.141.230.178:82/gslb/zbdq5.m3u8?id=gdty / <HTTPError 404: 'Not Found'>
- 地方频道 / 河北衛視 / https://stream1.freetv.fun/7768a9c340a28aa351a4d6653dbe72ebfc36dda0d6b5d45b794f1ed3ab703b9c.ctv / variant fail variants_checked=1 no segment
- 地方频道 / 河南衛視 / https://stream1.freetv.fun/7a878f83f6441d8d47365bad187dfb48b806d599d24d6051d900d19058ef1956.ctv / variant fail variants_checked=1 child bad 200
- 地方频道 / 河南衛視 / https://stream1.freetv.fun/7d4da877f9b53be50b1b2a7c010781ae8cf8b7b1bf38bd24e83bce1971d8146b.ctv / variant fail variants_checked=1 no segment
- 地方频道 / 浙江Ⅰ绍兴影视(720p) / http://live.shaoxing.com.cn/video/s10001-sxtv3/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 浙江少兒頻道 / https://stream1.freetv.fun/d148043df6b2f6d9464b41a73a6da05d758d0ad15a0d1d8a38a95b817d0a34e3.ctv / TimeoutError('timed out')
- 地方频道 / 湖北衛視 / https://stream1.freetv.fun/ce0638a2de7de4108196450241cb4f0ddd1bc6cadd1a68b019d72e751586e2ec.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 陕西交通广播 / https://satellitepull.cnr.cn/live/wxsxxjtgb/playlist.m3u8 / bad marker/html
- 地方频道 / 陕西新闻咨询 / http://112.46.105.20:8009/hls/18/index.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 鬼吹灯之云南虫谷 / https://live.ottiptv.cc/huya/11352898 / TimeoutError('The read operation timed out')
- 地方频道 / 黑龙江少儿 / https://ls.qingting.fm/live/4972/64k.m3u8 / bad marker/html
- 影视剧场 / 1930年代经典电影 / https://live.ottiptv.cc/yy/1356363815 / TimeoutError('The read operation timed out')
- 影视剧场 / 24h我爱我家喜剧 / https://live.ottiptv.cc/yy/1356212303 / TimeoutError('The read operation timed out')
- 影视剧场 / 24小时循环播电视剧 / https://live.ottiptv.cc/yy/53320802 / TimeoutError('The read operation timed out')
- 影视剧场 / 8090.电影一哥 / https://live.ottiptv.cc/yy/29197808 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 83射雕英雄传 / https://live.ottiptv.cc/yy/1354210357 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / CHC电影 / http://183.237.95.108:9901/tsfile/live/1008_1.m3u8?key=txiptv&playlive=0&authid=0 / URLError(TimeoutError('timed out'))
- 影视剧场 / 【周星驰】搞笑电影 / https://live.ottiptv.cc/yy/38670875 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 史诗级科幻电影-阿凡达 / https://live.ottiptv.cc/yy/1382735577 / TimeoutError('timed out')
- 影视剧场 / 名不虚传-韩剧 / https://live.ottiptv.cc/yy/1382749904 / TimeoutError('timed out')
- 影视剧场 / 恐怖电影 / https://live.ottiptv.cc/yy/24066336 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 悬疑武侠电影—九门 / https://live.ottiptv.cc/yy/1382828768 / TimeoutError('The read operation timed out')
- 影视剧场 / 情满四合院-高分电视剧 / https://live.ottiptv.cc/yy/1382735541 / TimeoutError('The read operation timed out')
- 影视剧场 / 憨豆先生-经典喜剧 / https://live.ottiptv.cc/yy/1354936239 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 斗破苍穹~24h玄幻剧 / https://live.ottiptv.cc/yy/1356051105 / TimeoutError('The read operation timed out')
- 影视剧场 / 末日电影合集 / https://live.ottiptv.cc/yy/1354889019 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 末日系列-外国电影合集 / https://live.ottiptv.cc/yy/1354889019 / <HTTPError 502: 'Bad Gateway'>
- 影视剧场 / 狄仁杰电影 / http://cdn.jdshipin.com:8880/huya.php?id=30080229 / <HTTPError 403: 'Forbidden'>
- 影视剧场 / 珍珠港-电影 / https://live.ottiptv.cc/yy/1354936234 / TimeoutError('timed out')
- 影视剧场 / 电影_蘑菇影厅 / https://live.metshop.top/huya/11601981 / RemoteDisconnected('Remote end closed connection without response')
- 影视剧场 / 电影搞笑喜剧 / http://live.metshop.top/huya/11342423?cdn=alicdn / RemoteDisconnected('Remote end closed connection without response')
- 影视剧场 / 电影梁家辉 / http://live.metshop.top/huya/11342429?cdn=alicdn / RemoteDisconnected('Remote end closed connection without response')
- 影视剧场 / 电视剧-流金岁月 / https://live.ottiptv.cc/yy/1382749906 / TimeoutError('timed out')
- 影视剧场 / 绍兴文化影视 / http://live.shaoxing.com.cn/video/s10001-sxtv3/index.m3u8 / <HTTPError 404: 'Not Found'>
- 体育纪实 / 奎屯汉语 / http://218.84.12.186:8001/hls/main/playlist.m3u8?zxinjd / <HTTPError 404: 'Not Found'>
- 体育纪实 / 睛彩竞技 / http://drive.mxmy.net:8888/udp/239.3.1.125:8001 / TimeoutError('timed out')
- 体育纪实 / 磐石 / http://stream5.jlntv.cn/ps/sd/live.m3u8?zjild / bad marker/html
- 音乐综艺 / 《东北小品》 / https://live.ottiptv.cc/yy/29600150 / TimeoutError('timed out')
- 音乐综艺 / 贾玲春晚小品 / https://live.ottiptv.cc/yy/1382736720 / TimeoutError('timed out')
- 生活休闲 / 哈尔滨生活 / http://stream.hrbtv.net/shpd/sd/live.m3u8?zheild / URLError(TimeoutError('timed out'))
- 生活休闲 / 学生兵 / https://live.ottiptv.cc/yy/1354658003 / TimeoutError('The read operation timed out')
- 生活休闲 / 旺苍新闻综合 / http://live.spccmc.com:90/live/spxwzh.m3u8?%E5%85%B3%E6%B3%A8%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7[%E6%99%B4%E5%9B%AD] / <HTTPError 404: 'Not Found'>
- 生活休闲 / 松潘新闻综合 / http://live.spccmc.com:90/live/spxwzh.m3u8?%E5%85%B3%E6%B3%A8%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7[%E6%99%B4%E5%9B%AD] / <HTTPError 404: 'Not Found'>
- 生活休闲 / 灌阳新闻综合 / https://ls.qingting.fm/live/5043/64k.m3u8 / URLError(TimeoutError('_ssl.c:993: The handshake operation timed out'))
- 生活休闲 / 生活時尚 / https://stream1.freetv.fun/5e1548ecb7837ffba0767d48a1872d9892a7978a9e2cb268d2ed2f8ddb601799.ctv / TimeoutError('The read operation timed out')
- 生活休闲 / 生活時尚 / https://stream1.freetv.fun/af577cd69d640274bdefa24125bfba424d35044c1235f7a429a7e85a00fc41e4.ctv / variant fail variants_checked=1 child bad 200
- 生活休闲 / 生活時尚 / https://stream1.freetv.fun/7234712007b11f36984751e7346e2892a373748f836997863fa50f1c0892e1c1.ctv / variant fail variants_checked=1 child bad 200
- 生活休闲 / 紹興文化影視 / https://stream1.freetv.fun/e46895f728cf01af107df98927c3bd0664dc452a60f2d117abef3ab9b0b6768f.m3u8 / <HTTPError 404: 'Not Found'>
- 综合娱乐 / CCTV电视塔东 / https://gcalic.v.myalicdn.com/gc/ztd_1/index.m3u8 / URLError(TimeoutError('_ssl.c:993: The handshake operation timed out'))
- 综合娱乐 / 七龙珠 / https://live.ottiptv.cc/huya/11601966 / <HTTPError 502: 'Bad Gateway'>
- 综合娱乐 / 三国演义 / https://live.ottiptv.cc/huya/11602081 / TimeoutError('The read operation timed out')
- 综合娱乐 / 与凤行 / https://live.ottiptv.cc/huya/26355866 / <HTTPError 502: 'Bad Gateway'>
- 综合娱乐 / 中华小当家 / https://live.ottiptv.cc/huya/11342413 / TimeoutError('The read operation timed out')
- 综合娱乐 / 乌龙闯情关 / https://live.ottiptv.cc/huya/26355767 / TimeoutError('The read operation timed out')
- 综合娱乐 / 哆啦A梦 / https://live.ottiptv.cc/huya/11601963 / <HTTPError 403: 'Forbidden'>
- 综合娱乐 / 城步电视台 / https://liveplay-srs.voc.com.cn/hls/tv/169_b4d7a4.m3u8 / <HTTPError 404: 'Not Found'>
- 综合娱乐 / 士兵突击 / https://live.ottiptv.cc/huya/11342430 / <HTTPError 502: 'Bad Gateway'>
- 综合娱乐 / 大秦赋 / https://live.ottiptv.cc/huya/23903130 / <HTTPError 502: 'Bad Gateway'>
- 综合娱乐 / 天龙八部 / https://live.ottiptv.cc/yy/1351814644 / <HTTPError 502: 'Bad Gateway'>
- 综合娱乐 / 寧夏衛視 / https://stream1.freetv.fun/f2f8306c7cc39bd605d852b4dabd77f41f16f2a9046d0d30e2dd471bc7aafe2d.ctv / bad marker/html
- 综合娱乐 / 山東衛視 / https://stream1.freetv.fun/3b97ca6daa3a8451a385b7db783b1c5622e979ec500532a2ff7145e99e78fab5.m3u8 / variant fail variants_checked=1 child bad 200
- 综合娱乐 / 廣東少兒 / https://stream1.freetv.fun/9f3e33c6a37116c66b6d9630d2811d1cd233a02c2aedd96130ceb94323d70411.ctv / <HTTPError 503: 'Service Unavailable'>
- 综合娱乐 / 新三国 / https://live.ottiptv.cc/huya/11352944 / <HTTPError 403: 'Forbidden'>
- 综合娱乐 / 東方影視 / https://stream1.freetv.fun/24b2b7048074d6989b0b0bdbb6cf188930ea474e17a5a04641c5313791b6791a.ctv / variant fail variants_checked=1 child bad 200
- 综合娱乐 / 永昌电视台 / https://play.kankanlive.com/live/1652755738635915.m3u8 / <HTTPError 404: 'Not Found'>
- 综合娱乐 / 永昌综合 / https://play.kankanlive.com/live/1652755738635915.m3u8 / <HTTPError 404: 'Not Found'>
- 综合娱乐 / 江蘇衛視 / https://stream1.freetv.fun/0135da5c7044214df0a494aafde08fc2fa5787c20c391fc76bdce2321417d4a1.m3u8 / TimeoutError('timed out')
- 综合娱乐 / 海峽衛視 / https://stream1.freetv.fun/6617cf82ead80b552e5a8e7a9cfe5f09410e7e954dc1ee1abdb48e5dd2c2b4d4.ctv / bad marker/html
- 综合娱乐 / 笑傲江湖 / https://live.ottiptv.cc/huya/26355790 / <HTTPError 403: 'Forbidden'>
- 综合娱乐 / 第一財經 / https://stream1.freetv.fun/533f951c259e0a0db9189aab022c535bca241b30dbf0d18aca82012de4e8c080.ctv / variant fail variants_checked=1 no segment
- 综合娱乐 / 舟山新聞綜合 / https://stream1.freetv.fun/1c41768e993a54617b9a22c65c9d4dcaea80759097ee0a859f1e8590955ddad7.m3u8 / variant fail variants_checked=1 child bad 200
- 综合娱乐 / 萧山综合 / http://l.cztvcloud.com/channels/lantian/SXxiaoshan1/720p.m3u8 / bad marker/html
- 综合娱乐 / 萧山综合 / http://l.cztvcloud.com/channels/lantian/SXxiaoshan1/720p.m3u8? / bad marker/html
