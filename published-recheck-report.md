# Published playlist recheck report

Elapsed: 299.3s
Rows before: 2704
Rows after: 2543
Removed rows: 161
Failed unique URLs in initial final recheck: 207
Core live-progress check required: True
Video track required: True
Video-track verified final unique URLs: 2543
Refill attempted unique URLs: 49
Refill playable unique URLs: 46
Refilled rows: 46
Unresolved refill rows: 161

## Group deltas

| Group | Before | After | Removed |
|---|---:|---:|---:|
| 央视频道 | 131 | 128 | 3 |
| 卫视频道 | 197 | 180 | 17 |
| 地方频道 | 863 | 827 | 36 |
| 影视剧场 | 147 | 137 | 10 |
| 少儿动漫 | 28 | 27 | 1 |
| 体育纪实 | 66 | 66 | 0 |
| 音乐综艺 | 29 | 20 | 9 |
| 生活休闲 | 95 | 90 | 5 |
| 综合娱乐 | 855 | 807 | 48 |
| 港澳台频道 | 73 | 63 | 10 |
| 海外华语频道 | 220 | 198 | 22 |

## First failed rows

- 央视频道 / CCTV-1 / http://183.11.239.36:808/hls/19/index.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 央视频道 / CCTV-4K / https://stream1.freetv.fun/be485615e65d6f8fb8940553193e872e3b71f9f42cc10a4254745dad055d4e7f.m3u8 / <HTTPError 403: 'Forbidden'>
- 央视频道 / CCTV-5(h265) / https://stream1.freetv.fun/40710de671d35439e7b352aad3066e07cdaeb78312280215f469628adb873a16.ctv / bad marker/html
- 央视频道 / CCTV-8 / http://183.11.239.36:808/hls/96/index.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 央视频道 / CCTV-8 / http://207.56.13.146:81/cdnlive/cctv8.m3u8 / <HTTPError 404: 'Not Found'>
- 央视频道 / CCTV-9(576i) / https://xykt-fix.github.io/Y77.m3u8 / variant fail variants_checked=1 segments ok checked=3 required=video; manifest did not advance after 3.0s
- 央视频道 / CCTV-13 / http://ali-m-l.cztv.com/channels/lantian/channel21/1080p.m3u8 / segments ok checked=3 required=video; manifest did not advance after 10.0s
- 央视频道 / CCTV-13 / http://drive.mxmy.net:8888/udp/239.3.1.124:8128 / direct application/octet-stream bytes=65536 unknown/mpeg-ts: TS packets found but PAT/PMT video track not observed required=video
- 卫视频道 / 浙江卫视 / http://ali-m-l.cztv.com/channels/lantian/channel01/1080p.m3u8 / segments ok checked=3 required=video; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / http://ali-m-l.cztv.com:80/channels/lantian/channel001/1080p.m3u8 / segments ok checked=3 required=video; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / https://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8 / segments ok checked=3 required=video; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / http://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8 / segments ok checked=3 required=video; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / https://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8? / segments ok checked=3 required=video; manifest did not advance after 10.0s
- 卫视频道 / 深圳卫视 / http://198.204.228.26/live/szwshd.m3u8 / segments ok checked=3 required=video; manifest did not advance after 14.0s
- 卫视频道 / 内蒙古卫视 / http://183.11.239.36:808/hls/60/index.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 大湾区卫视 / http://222.128.55.152:9080/live/dwq.m3u8 / variant fail variants_checked=1 segments ok checked=3 required=video; manifest did not advance after 14.0s
- 卫视频道 / 大湾区卫视 / http://183.11.239.36:808/hls/132/index.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 大湾区卫视 / https://stream1.freetv.fun/9e44565ab6186689007a295d8b94b2a970fafde637068b0e3837e5f84689a8f3.m3u8 / variant fail variants_checked=1 segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 天津卫视 / http://204.12.221.218:8181/3m1080p/tjws.m3u8 / segments ok checked=3 required=video; manifest did not advance after 13.8s
- 卫视频道 / 宁夏卫视 / http://183.11.239.36:808/hls/106/index.m3u8 / TimeoutError('timed out') (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 安多卫视 / https://stream1.freetv.fun/52d0df257c5c3cec42f2ae19268dbbc261256ff391b27bd83553bea941d0c186.m3u8 / variant fail variants_checked=1 segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 山东卫视 / http://drive.mxmy.net:8888/udp/239.3.1.209:8052 / direct application/octet-stream bytes=65536 unknown/mpeg-ts: TS packets found but PAT/PMT video track not observed required=video
- 卫视频道 / 延边卫视 / https://stream1.freetv.fun/yan-bian-wei-shi-16.m3u8 / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 延边卫视 / https://stream1.freetv.fun/yan-bian-wei-shi-15.m3u8 / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 新疆卫视 / http://183.11.239.36:808/hls/65/index.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 星空卫视 / https://stream1.freetv.fun/xing-kong-wei-shi-4.ctv / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 星空卫视 / https://stream1.freetv.fun/xing-kong-wei-shi-12.m3u8 / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 星空卫视 / https://stream1.freetv.fun/xing-kong-wei-shi-10.m3u8 / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 星空卫视 / https://stream1.freetv.fun/xing-kong-wei-shi-11.m3u8 / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 江西卫视 / http://183.11.239.36:808/hls/44/index.m3u8 / TimeoutError('timed out') (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 海南卫视 / http://183.11.239.36:808/hls/124/index.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 澳亚卫视 / https://stream1.freetv.fun/ao-ya-wei-shi-1.ctv / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 甘肃卫视 / http://183.11.239.36:808/hls/119/index.m3u8 / URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out')))
- 卫视频道 / 陕西卫视 / http://198.204.228.26/live/snwshd.m3u8 / <HTTPError 404: 'Not Found'>
- 卫视频道 / 香港卫视 / https://stream1.freetv.fun/5335c88a9a7d8b74173b491f480d4f94e8d3bd596af54478106aa2399e6c7917.ctv / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 香港卫视 / https://stream1.freetv.fun/c751876ae5ceaa0d82b5cf2badc152342aa92a4b45bf504d12ee45966b2fc644.ctv / segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 香港卫视 / https://stream1.freetv.fun/5335c88a9a7d8b74173b491f480d4f94e8d3bd596af54478106aa2399e6c7917.m3u8 / variant fail variants_checked=1 segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 香港卫视 / https://stream1.freetv.fun/ae7eaf28d8610cdc1651ef6a1f7dbb24b49c5a87627d0d881330afaea37a1616.m3u8 / variant fail variants_checked=1 segments ok checked=3 required=video; VOD/endlist manifest is not a live channel
- 卫视频道 / 黑龙江卫视 / http://drive.mxmy.net:8888/udp/239.3.1.133:8016 / direct application/octet-stream bytes=65536 unknown/mpeg-ts: TS packets found but PAT/PMT video track not observed required=video
- 地方频道 / 三明新闻综合 / http://ls.qingting.fm/live/4885.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 上海动感101 / http://ls.qingting.fm/live/274.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 东丰综合 / http://stream3.jlntv.cn:80/aac_dfgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 仁寿综合 / https://play.scrstv.com.cn/DT/live.m3u8?auth_key=60001724663204-0-0-c1cc4ded9841ac34f63cdbd3aec647ef / segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 六安公共 / http://ls.qingting.fm/live/1794199.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 六安新闻综合 / http://ls.qingting.fm/live/267.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 北京新闻 / https://satellitepull.cnr.cn/live/wxbjxwgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 北京衛視 / https://stream1.freetv.fun/5a20fa5ec6a4bf5ba25f3efd6f4521e86065d5cb07ac8cb90b1c4edac73a3265.m3u8 / TimeoutError('timed out')
- 地方频道 / 双辽综合 / http://stream3.jlntv.cn:80/aac_slgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 吉林乡村 / https://satellitepull.cnr.cn/live/wxjlxcgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 四川衛視 / https://stream1.freetv.fun/c1b56c701705c237fe6019d936786b891cd3aacc240d31ae59cfafb1b076289b.ctv / TimeoutError('The read operation timed out')
- 地方频道 / 四川衛視 / https://stream1.freetv.fun/135a6af8a6c568de2ce54c9d47a3e464c4b2afbaeec67584c573c01c276ae4ab.ctv / TimeoutError('The read operation timed out')
- 地方频道 / 天津衛視 / https://stream1.freetv.fun/f222f3958ea857ac01bdceb54d347d2a059b9ac3114ed39c837280bdad93b9ab.ctv / TimeoutError('The read operation timed out')
- 地方频道 / 山东体育 / http://live.xmcdn.com/live/805/64.m3u8 / segment bad 200 audio/x-aac bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 山东体育 / http://satellitepull.cnr.cn/live/wxsdtyxxgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 山东体育 / https://satellitepull.cnr.cn/live/wxsdtyxxgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 山东生活 / http://ls.qingting.fm/live/60260.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 山东生活 / http://live.xmcdn.com/live/802/64.m3u8 / segment bad 200 audio/x-aac bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 广东新闻 / http://satellitepull.cnr.cn/live/wxgdxwgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 广东民生 / http://183.11.239.36:808/hls/18/index.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 广东民生 / https://t.freetv.fun/live/yan-dong-min-sheng-6.m3u8 / URLError(TimeoutError('timed out'))
- 地方频道 / 新沂新闻 / http://live.xysrmt.cn/xwzh/sd/live.m3u8?zjiangsd / URLError(OSError(101, 'Network is unreachable'))
- 地方频道 / 新沂生活 / http://live.xysrmt.cn/shpd/sd/live.m3u8 / URLError(OSError(101, 'Network is unreachable'))
- 地方频道 / 杭州综合 / http://live.xmcdn.com/live/1845/64.m3u8 / segment bad 200 audio/x-aac bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 柳河综合 / http://stream3.jlntv.cn:80/aac_lhgb/sd/live.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 桦甸综合 / http://stream9.jlntv.cn:80/aac_huadiangb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 梅河口综合 / http://stream3.jlntv.cn:80/aac_mhkgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 河北农民 / http://ls.qingting.fm/live/1650.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 河北都市 / https://radio.pull.hebtv.com/live/hebnczx.m3u8 / segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 浙江动听 / http://ls.qingting.fm/live/4866.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 浙江音乐调频•动听968 / https://satellitepull.cnr.cn/live/wxzj968/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 海南新闻 / http://ls.qingting.fm/live/1861.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 深圳飞扬971 / https://satellitepull.cnr.cn/live/wxszfy971/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 深圳飞扬音乐台 / http://ls.qingting.fm/live/1271.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 渭源新闻 / http://play.kankanlive.com/live/1720408280309109.m3u8 / TimeoutError('timed out')
- 地方频道 / 甘肃经济 / https://satellitepull.cnr.cn/live/wxgshhzs/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 白银综合 / http://play.kankanlive.com/live/1720408089419110.m3u8 / TimeoutError('timed out')
- 地方频道 / 磐石综合 / http://stream3.jlntv.cn:80/aac_psgb/sd/live.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
- 地方频道 / 福建新闻 / http://satellitepull.cnr.cn/live/wx32fjxwgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 福建经济 / http://satellitepull.cnr.cn/live/wx32fjdnjjgb/playlist.m3u8 / variant fail variants_checked=1 segment bad 200 video/mp2t bytes=32768 checked=1 audio/mpeg-ts: PAT/PMT advertises audio but no video
- 地方频道 / 第一财经 / http://ls.qingting.fm/live/276.m3u8 / segment bad 200 application/octet-stream bytes=32768 checked=1 audio/mpeg-audio: MPEG audio frame observed
