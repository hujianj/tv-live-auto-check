# Published playlist recheck report

Outputs rewritten: True
Elapsed: 355.6s
Rows before: 514
Rows after: 311
Rows removed from outputs: 203
Candidate rows failing strict recheck: 203
Rows refilled after strict recheck: 0
Net output row delta: -203
Failed unique URLs after slow retry: 203
Slow retry attempted unique URLs: 205
Slow retry recovered unique URLs: 2
Core live-progress check required: True
Broadcast live-progress check required: True
Live-progress groups: 卫视频道, 地方频道, 央视频道
Video track required: True
Video-track verified final unique URLs: 311
Refill attempted unique URLs: 0
Refill playable unique URLs: 0
Refilled rows: 0
Historical fallback candidates attempted: 0
Historical fallback rows accepted: 0
Unresolved refill rows: 203

## Group deltas

| Group | Before | After | Net delta |
|---|---:|---:|---:|
| 央视频道 | 49 | 20 | -29 |
| 卫视频道 | 66 | 19 | -47 |
| 地方频道 | 227 | 134 | -93 |
| 影视剧场 | 66 | 64 | -2 |
| 少儿动漫 | 2 | 2 | +0 |
| 体育纪实 | 31 | 18 | -13 |
| 音乐综艺 | 19 | 1 | -18 |
| 综合娱乐 | 52 | 51 | -1 |
| 港澳台频道 | 2 | 2 | +0 |

## First failed rows

- 央视频道 / CCTV-1 / http://101.66.195.137:9901/tsfile/live/0001_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-1 / http://101.66.195.192:9901/tsfile/live/0001_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-2 / http://101.66.195.192:9901/tsfile/live/0002_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-2 / http://101.66.195.137:9901/tsfile/live/0002_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-3 / http://101.66.195.192:9901/tsfile/live/0003_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-3 / http://101.66.195.137:9901/tsfile/live/0003_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-5 / http://101.66.195.137:9901/tsfile/live/0005_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-5 / http://101.66.195.192:9901/tsfile/live/0005_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-6 / http://101.66.195.137:9901/tsfile/live/0006_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-6 / http://101.66.195.192:9901/tsfile/live/0006_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-7 / http://101.66.195.137:9901/tsfile/live/0007_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-7 / http://101.66.195.192:9901/tsfile/live/0007_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-8 / http://101.66.195.192:9901/tsfile/live/0008_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-8 / http://101.66.195.137:9901/tsfile/live/0008_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-9 / http://101.66.195.192:9901/tsfile/live/0009_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-9 / http://101.66.195.137:9901/tsfile/live/0009_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-10 / http://101.66.195.137:9901/tsfile/live/0010_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-10 / http://101.66.195.192:9901/tsfile/live/0010_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-11 / http://101.66.195.192:9901/tsfile/live/0011_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-11 / http://101.66.195.137:9901/tsfile/live/0011_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-12 / http://101.66.195.137:9901/tsfile/live/0012_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-12 / http://101.66.195.192:9901/tsfile/live/0012_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-13 / http://ali-m-l.cztv.com/channels/lantian/channel21/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 央视频道 / CCTV-13 / http://101.66.195.192:9901/tsfile/live/0013_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-13 / http://101.66.195.137:9901/tsfile/live/0013_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-14 / http://101.66.195.192:9901/tsfile/live/0014_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-14 / http://101.66.195.137:9901/tsfile/live/0014_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-15 / http://101.66.195.137:9901/tsfile/live/0015_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 央视频道 / CCTV-15 / http://101.66.195.192:9901/tsfile/live/0015_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 辽宁卫视 / http://101.66.195.192:9901/tsfile/live/0121_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('per-host admission deadline exceeded') (core retry after first=TimeoutError('per-host admission deadline exceeded')); last=TimeoutError('timed out')
- 卫视频道 / 辽宁卫视 / http://101.66.195.137:9901/tsfile/live/0121_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 河北卫视 / http://101.66.195.192:9901/tsfile/live/0117_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('per-host admission deadline exceeded') (core retry after first=TimeoutError('per-host admission deadline exceeded')); last=TimeoutError('timed out')
- 卫视频道 / 河北卫视 / http://101.66.195.137:9901/tsfile/live/0117_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('per-host admission deadline exceeded') (core retry after first=TimeoutError('per-host admission deadline exceeded')); last=TimeoutError('timed out')
- 卫视频道 / 河南卫视 / http://101.66.195.192:9901/tsfile/live/0139_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 河南卫视 / http://101.66.195.137:9901/tsfile/live/0139_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 北京卫视 / http://101.66.195.192:9901/tsfile/live/0016_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 北京卫视 / http://101.66.195.137:9901/tsfile/live/0016_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 东方卫视 / http://bp-resource-dfl.bestv.cn/155/3/video.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 东方卫视 / http://bp-resource-dfl.bestv.cn/148/3/video.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 东方卫视 / http://101.66.195.192:9901/tsfile/live/0018_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 东方卫视 / http://101.66.195.137:9901/tsfile/live/0018_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 东方卫视 / https://bp-resource-dfl.bestv.cn/148/3/video.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 浙江卫视 / http://ali-vl.cztv.com/channels/lantian/channel001/360p.m3u8 / final slow retry failed attempt=1 first=URLError(TimeoutError('timed out')) (core retry after first=URLError(TimeoutError('timed out'))); last=URLError(TimeoutError('timed out'))
- 卫视频道 / 浙江卫视 / http://ali-m-l.cztv.com/channels/lantian/channel01/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 浙江卫视 / https://ali-m-l.cztv.com/channels/lantian/channel001/1080p.m3u8 / final slow retry failed attempt=1 first=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s; last=segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 10.0s
- 卫视频道 / 江苏卫视 / http://101.66.195.192:9901/tsfile/live/0017_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 江苏卫视 / http://101.66.195.137:9901/tsfile/live/0017_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 湖南卫视 / http://101.66.195.192:9901/tsfile/live/0019_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 湖南卫视 / http://101.66.195.137:9901/tsfile/live/0019_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 广东卫视 / http://101.66.195.192:9901/tsfile/live/0125_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 广东卫视 / http://101.66.195.137:9901/tsfile/live/0125_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 广东卫视 / https://txmov2.a.kwimgs.com/upic/2023/01/26/09/BMjAyMzAxMjYwOTE3NDVfNzM5MzQzNzIyXzk0NjI1OTUwNTA3XzBfMw==_b_B81ddda927d33445d544befd008e60109.mp4 / final slow retry failed attempt=1 first=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD; last=direct MP4/fMP4 cannot prove live broadcast progress; rejecting likely VOD
- 卫视频道 / 东南卫视 / http://101.66.195.192:9901/tsfile/live/0137_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 东南卫视 / http://101.66.195.137:9901/tsfile/live/0137_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 云南卫视 / http://101.66.195.192:9901/tsfile/live/0119_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('URL total budget exceeded while reading media') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 云南卫视 / http://101.66.195.137:9901/tsfile/live/0119_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 吉林卫视 / http://101.66.195.192:9901/tsfile/live/0116_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 吉林卫视 / http://101.66.195.137:9901/tsfile/live/0116_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 四川卫视 / http://101.66.195.192:9901/tsfile/live/0123_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 大湾区卫视 / http://222.128.55.152:9080/live/dwq.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s; last=variant fail variants_checked=1 segments ok checked=3 required=media; frame decode ok frames=3 exit=0; manifest did not advance after 14.0s
- 卫视频道 / 安徽卫视 / http://101.66.195.192:9901/tsfile/live/0130_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 安徽卫视 / http://101.66.195.137:9901/tsfile/live/0130_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 山东卫视 / http://101.66.195.192:9901/tsfile/live/0131_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 山东卫视 / http://101.66.195.137:9901/tsfile/live/0131_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 广西卫视 / http://101.66.195.137:9901/tsfile/live/0113_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 广西卫视 / http://101.66.195.192:9901/tsfile/live/0113_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 江西卫视 / http://101.66.195.137:9901/tsfile/live/0138_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 江西卫视 / http://101.66.195.192:9901/tsfile/live/0138_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 湖北卫视 / http://101.66.195.137:9901/tsfile/live/0132_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 湖北卫视 / http://101.66.195.192:9901/tsfile/live/0132_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 贵州卫视 / http://101.66.195.192:9901/tsfile/live/0120_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 贵州卫视 / http://101.66.195.137:9901/tsfile/live/0120_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 重庆卫视 / http://101.66.195.192:9901/tsfile/live/0142_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 重庆卫视 / http://101.66.195.137:9901/tsfile/live/0142_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 黑龙江卫视 / http://101.66.195.137:9901/tsfile/live/0143_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 卫视频道 / 黑龙江卫视 / http://101.66.195.192:9901/tsfile/live/0143_1.m3u8?key=txiptv&playlive=0&authid=0 / final slow retry failed attempt=1 first=TimeoutError('timed out') (core retry after first=TimeoutError('timed out')); last=TimeoutError('timed out')
- 地方频道 / 三明新闻综合 / http://ls.qingting.fm/live/4885.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 三明新闻综合 / https://ls.qingting.fm/live/5022100/64k.m3u8 / final slow retry failed attempt=1 first=segments ok checked=2 required=media; frame decode failed frames=0 exit=183; last=segments ok checked=2 required=media; frame decode failed frames=0 exit=183
- 地方频道 / 上海第一财经 / https://satellitepull.cnr.cn/live/wx32dycjgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
- 地方频道 / 东丰综合 / http://stream3.jlntv.cn:80/aac_dfgb/playlist.m3u8 / final slow retry failed attempt=1 first=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234; last=variant fail variants_checked=1 segments ok checked=2 required=media; frame decode failed frames=0 exit=234
