# Published playlist recheck report

Elapsed: 111.7s
Rows before: 2527
Rows after: 2388
Removed rows: 139
Failed unique URLs: 135

## Group deltas

| Group | Before | After | Removed |
|---|---:|---:|---:|
| 央视频道 | 150 | 145 | 5 |
| 卫视频道 | 205 | 176 | 29 |
| 地方频道 | 520 | 489 | 31 |
| 影视剧场 | 147 | 134 | 13 |
| 少儿动漫 | 22 | 22 | 0 |
| 体育纪实 | 68 | 65 | 3 |
| 音乐综艺 | 50 | 49 | 1 |
| 生活休闲 | 180 | 171 | 9 |
| 综合娱乐 | 900 | 884 | 16 |
| 港澳台频道 | 65 | 65 | 0 |
| 海外华语频道 | 220 | 188 | 32 |

## First failed rows

- 央视频道 / CCTV-3 / http://112.46.85.60:8009/hls/3/index.m3u8 / <HTTPError 404: 'Not Found'>
- 央视频道 / CCTV-5+(backup) / https://stream1.freetv.fun/518f11d132212440db2e1a3b39daf7109482323163bedd6be790ac894d3f83e3.ctv / variant fail variants_checked=1 child bad 200
- 央视频道 / CCTV-9 / http://112.46.85.60:8009/hls/509/index.m3u8 / <HTTPError 404: 'Not Found'>
- 央视频道 / CCTV-15 / http://222.134.245.16:9901/tsfile/live/0015_1.m3u8?key=txiptv&playlive=1&authid=0 / <HTTPError 404: 'Not Found'> (core retry after first=TimeoutError('timed out'))
- 央视频道 / CCTV-17 / https://live.264788.xyz/channel/cctv17?streamid=f9c36f1e95b5b35eac89cc89583e7c0a&livekey=01WgOR41rriMmMkzNsd0UoaxJRwetZdxIvtVk / variant fail variants_checked=1 child bad 200
- 卫视频道 / 河北卫视 / http://63.141.230.178:82/gslb/zbdq5.m3u8?id=hewshd / segment bad 200 video/mp2t bytes=4096 checked=3
- 卫视频道 / 河北卫视 / http://38.75.136.137:98/gslb/dsdqpub/hewshd.m3u8?auth=testpub / segment bad 200 video/mp2t bytes=4096 checked=3
- 卫视频道 / 北京卫视 / http://222.134.245.16:9901/tsfile/live/0122_1.m3u8 / <HTTPError 404: 'Not Found'> (core retry after first=TimeoutError('timed out'))
- 卫视频道 / 北京卫视 / http://207.56.13.146:81/cdnlive/bjws.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=1
- 卫视频道 / 浙江卫视 / http://ali-xwl.cztv.com/live/channel01720Plxw.m3u8 / bad marker/html
- 卫视频道 / 云南卫视 / http://198.204.228.26/live/ynwshd.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=2
- 卫视频道 / 云南卫视 / http://107.150.60.122/live/ynwshd.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=2
- 卫视频道 / 云南卫视 / http://204.12.221.218:8181/3m1080p/ynws.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=2
- 卫视频道 / 云南卫视 / http://63.141.230.178:82/gslb/zbdq5.m3u8?id=ynwshd / segment bad 200 video/mp2t bytes=4096 checked=2
- 卫视频道 / 兵团卫视 / http://183.11.239.36:808/hls/7/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 内蒙古卫视 / http://222.134.245.16:9901/tsfile/live/0109_1.m3u8 / <HTTPError 404: 'Not Found'> (core retry after first=TimeoutError('timed out'))
- 卫视频道 / 农林卫视 / http://120.76.248.139/live/bfgd/4200000122.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 安徽卫视 / http://222.134.245.16:9901/tsfile/live/0130_1.m3u8 / <HTTPError 404: 'Not Found'> (core retry after first=TimeoutError('timed out'))
- 卫视频道 / 安徽卫视 / http://183.11.239.36:808/hls/40/index.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 安徽卫视 / http://63.141.230.178:82/gslb/zbdq5.m3u8?id=ahwshd / segment bad 200 video/mp2t bytes=4096 checked=3
- 卫视频道 / 山西卫视 / http://119.39.9.8:9901/tsfile/live/0118_1.m3u8 / bad marker/html
- 卫视频道 / 广西卫视 / http://222.134.245.16:9901/tsfile/live/0113_1.m3u8 / <HTTPError 404: 'Not Found'> (core retry after first=TimeoutError('timed out'))
- 卫视频道 / 延边卫视 / https://srs.iyb983.cn/video/CYS/index.m3u8 / bad marker/html
- 卫视频道 / 延边卫视 / https://srs.iyb983.cn:443/video/CYS/index.m3u8 / bad marker/html
- 卫视频道 / 新疆卫视 / http://218.84.12.186:8001/hls/main/playlist.m3u8zxinjd / <HTTPError 404: 'Not Found'>
- 卫视频道 / 新疆卫视 / http://218.84.12.186:8001/hls/main/playlist.m3u8?zxinjd / <HTTPError 404: 'Not Found'>
- 卫视频道 / 新疆卫视 / http://183.11.239.36:808/hls/65/index.m3u8 / bad marker/html
- 卫视频道 / 浙江卫视超清 / http://ali-xwl.cztv.com/live/channel01720Plxw.m3u8 / bad marker/html
- 卫视频道 / 海南卫视 / http://111.221.137.234:44330/tsfile/live/0117_1.m3u8?key=txiptv&playlive=0&authid=0 / bad marker/html
- 卫视频道 / 海南卫视 / http://120.76.248.139/live/bfgd/4200000473.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 贵州卫视 / http://182.150.23.74:808/hls/26/index.m3u8 / bad marker/html
- 卫视频道 / 黑龙江卫视 / http://198.204.228.26/live/hljwshd.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=3
- 卫视频道 / 黑龙江卫视 / http://107.150.60.122/live/hljwshd.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=3
- 卫视频道 / 黑龙江卫视 / http://204.12.221.218:8181/3m1080p/hljws.m3u8 / segment bad 200 video/mp2t bytes=4096 checked=3
- 地方频道 / 北京新闻 / https://ls.qingting.fm/live/339/64k.m3u8 / bad marker/html
- 地方频道 / 北京爱情故事，心动不打烊 / https://live.ottiptv.cc/yy/1382744423 / <HTTPError 502: 'Bad Gateway'>
- 地方频道 / 北京纪实科教 / http://120.76.248.139/live/bfgd/4200000113.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 南京十八生活 / http://nklive.nbs.cn/hls/1173a815-bfdb-4c3c-9f73-89ec37ae7716/index.m3u8 / TimeoutError('timed out')
- 地方频道 / 安徽衛視 / https://stream1.freetv.fun/05da16d9a29c25a3c7389d02cc81dafcdda207d93176603cbd560ab0075312c6.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 安徽衛視 / https://stream1.freetv.fun/98aef088ca444c3c14722ba4478c7d37c3976d8466516774ab8956b9294ac184.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 安徽衛視 / https://stream1.freetv.fun/07f34ef59982ef7598025212875253649ec5e5833979d88fbd45def3d51d4c01.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 山西衛視 / https://stream1.freetv.fun/9583a6cddbaf5f732564978bc22cecb76770106e18e003ad3ac6a9c20d3148f9.m3u8 / variant fail variants_checked=1 child bad 200
- 地方频道 / 广东珠江 / http://107.150.60.122/live/gdzja.m3u8 / <HTTPError 404: 'Not Found'>
- 地方频道 / 河北衛視 / https://stream1.freetv.fun/4ca8a4a550ab606e4a0419326b248590c5d03d2a63bd0cdc6914f681724f8fe5.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 河北衛視 / https://stream1.freetv.fun/b6129199d32bae0643d0a5e5d81e78b59a7b056a606f0e01f1994f9898dca75d.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 河北衛視 / https://stream1.freetv.fun/b1b70c0ba5ae4a14b5325b4ced18b94dd2423b228895e62c705cf91ef625219c.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=4096 checked=1
- 地方频道 / 河南衛視 / https://stream1.freetv.fun/3ba20cd120a608446b9b1fab73bdcb6ef31c97600e98c175c809f675e15f72c5.ctv / bad marker/html
- 地方频道 / 河南都市 / http://1.94.31.214/php/hntv.php?id=hnds / bad marker/html
- 地方频道 / 浙江国际 / http://ali-xwl.cztv.com/live/channel10720Plxw.m3u8 / bad marker/html
- 地方频道 / 浙江钱江 / http://ali-xwl.cztv.com/live/channel02720Plxw.m3u8 / bad marker/html
- 地方频道 / 浙江钱江都市 / http://ali-xwl.cztv.com/live/channel02720Plxw.m3u8 / bad marker/html
- 地方频道 / 海南新闻 / http://ls.qingting.fm/live/1861.m3u8 / bad marker/html
- 地方频道 / 海南衛視 / https://stream1.freetv.fun/c2050143891ad65886901531fce3a60bd082cf1d043bd0e8cdbef961ee74657e.ctv / bad marker/html
- 地方频道 / 湖南张家界水绕四门 / https://gcalic.v.myalicdn.com/gc/zjjsrsm_1/index.m3u8 / bad marker/html
- 地方频道 / 辽宁体育 / http://120.76.248.139/live/bfgd/4200000611.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁公共 / http://120.76.248.139/live/bfgd/4200000077.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁公共 / http://120.76.248.139/live/bfgd/4200000481.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁影视剧 / http://120.76.248.139/live/bfgd/4200000070.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁教育青少 / http://120.76.248.139/live/bfgd/4200000075.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁生活 / http://120.76.248.139/live/bfgd/4200000073.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁经济 / http://120.76.248.139/live/bfgd/4200000480.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁经济 / http://120.76.248.139/live/bfgd/4200000076.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 辽宁都市 / https://ls.qingting.fm/live/1099/64k.m3u8 / bad marker/html
- 地方频道 / 辽宁都市 / http://120.76.248.139/live/bfgd/4200000610.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 黑龙江少儿 / https://ls.qingting.fm/live/4972/64k.m3u8 / bad marker/html
- 影视剧场 / 【周星驰】搞笑电影 / https://live.ottiptv.cc/yy/38670875 / TimeoutError('timed out')
- 影视剧场 / 国内玄幻电影-林正英 / https://live.ottiptv.cc/yy/1354932444 / TimeoutError('timed out')
- 影视剧场 / 国内经典动作电影 / https://live.ottiptv.cc/yy/1382851522 / TimeoutError('timed out')
- 影视剧场 / 宫心计-港剧-古装 / https://live.ottiptv.cc/yy/1354933540 / bad marker/html
- 影视剧场 / 寻秦记-穿越剧经典 / https://live.ottiptv.cc/yy/1382749900 / TimeoutError('timed out')
- 影视剧场 / 射雕英雄传 / https://live.metshop.top/huya/23824164 / <HTTPError 403: 'Forbidden'>
- 影视剧场 / 斗鱼电影HD3 / http://epg.112114.xyz/douyu/122402 / TimeoutError('timed out')
- 影视剧场 / 电影搞笑喜剧 / http://live.metshop.top/huya/11342423?cdn=alicdn / RemoteDisconnected('Remote end closed connection without response')
- 影视剧场 / 精彩动作电影享不停 / https://live.ottiptv.cc/yy/1382736809 / TimeoutError('timed out')
- 影视剧场 / 绍兴文化影视 / https://t.freetv.fun/live/shao-xing-wen-hua-ying-shi-1.m3u8 / <HTTPError 404: 'Not Found'>
- 影视剧场 / 绍兴文化影视 / https://stream1.freetv.fun/shao-xing-wen-hua-ying-shi-1.m3u8 / <HTTPError 404: 'Not Found'>
- 影视剧场 / 绍兴文化影院 / http://live.shaoxing.com.cn/video/s10001-sxtv3/index.m3u8?zzhed / <HTTPError 404: 'Not Found'>
- 影视剧场 / 陪你一起看好剧 / https://live.ottiptv.cc/yy/1354932359 / bad marker/html
- 体育纪实 / 天元围棋 / http://120.76.248.139/live/bfgd/4200000633.m3u8 / URLError(TimeoutError('timed out'))
- 体育纪实 / 奎屯汉语 / http://218.84.12.186:8001/hls/main/playlist.m3u8?zxinjd / <HTTPError 404: 'Not Found'>
