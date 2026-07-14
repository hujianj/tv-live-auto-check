# TV Live Auto Check

IPTV 自动维护项目：抓取公开直播源，对去重后的真实播放 URL 做媒体流检测，只发布检测到可播放分片/媒体字节的线路，并生成适合酷9/TCL 电视端导入的订阅列表。

## 推荐订阅地址

电视端/酷9优先使用 jsDelivr CDN 的 `@main` 地址，国内网络通常比 `github.io` 和 `raw.githubusercontent.com` 更稳定：

```text
https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/live-curated.txt
```

如果 `live-curated.txt` 在 CDN 边缘节点偶发滞后，可临时使用同内容文件：

```text
https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/live.txt
```

如果想在每次维护后尽快拿到最新版，可测试 Raw 代理地址：

```text
https://gh-proxy.com/raw.githubusercontent.com/hujianj/tv-live-auto-check/main/live-curated.txt
```

M3U 格式：

```text
https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/live.m3u
```

GitHub Pages / Raw 地址保留给电脑或人工测试；部分电视网络可能获取为空或连接失败：

```text
https://hujianj.github.io/tv-live-auto-check/live-curated.txt
https://raw.githubusercontent.com/hujianj/tv-live-auto-check/main/live-curated.txt
```

## 自动维护逻辑

- 每天北京时间 04:20 自动运行，也可在 GitHub Actions 手动 `Run workflow`。
- 抓取 `scripts/verify_sources.py` 中配置的所有上游公开源。
- 对所有去重后的真实流 URL 做全量检测；同一个 URL 被多个频道名引用时只检测一次，再复用检测结果。
- HLS 检测会打开播放列表，并继续检测下一级媒体分片；默认最多检测 2 个 variant、每个媒体列表最多 2 个分片。
- 生成电视端主订阅 `live-curated.txt`、同内容别名 `live.txt` / `live-verified.txt` / `ku9-live.txt`，以及 `live.m3u`。
- 全量明细 `stream_check_results.csv`、`live-all-playable.txt`、`all-playable.m3u` 不再提交到 Git 仓库，只作为 GitHub Actions artifact 保存 30 天。
- 发布前会运行统一校验 `scripts/validate_playlist.py`，防止异常频道名、异常 URL、错误分类或不可解析 TXT 行进入正式列表。
- 发布前会运行 `scripts/guard_publish.py`，如果本次结果比上一版明显缩水，或核心分类数量低于阈值，会拒绝发布，保留上一版可用列表。
- 发布后自动 purge jsDelivr，并检查 Raw / Pages / jsDelivr 缓存状态。jsDelivr 偶发短时滞后只记录告警，不代表仓库文件错误。

## 频道分类规则

电视主列表按家用观看习惯排序：

1. 央视频道
2. 卫视频道
3. 地方频道
4. 影视剧场
5. 少儿动漫
6. 体育纪实
7. 音乐综艺
8. 生活休闲
9. 综合娱乐
10. 港澳台频道
11. 海外华语频道

`CCTV` 会按 `CCTV-1, CCTV-2, CCTV-3...` 排序。外语频道、纯英文频道、伪 CCTV、`Not24/7`、PlutoTV/RedBull 等非家用频道会被过滤；RTHK/TVB/TVBS/ViuTV 等明确港澳台品牌会保留在港澳台分类。

## 优先源

当前最高优先级源：

```text
https://live.zbds.top/tv/iptv4.txt
```

对应源码标识：

```python
zbds_iptv4_txt
```

如果该源中某频道有可播放线路，会优先排在该频道前面；如果该源线路不可播放，则自动使用其他已检测可播放线路。

## 如何新增上游直播源

修改：

```text
scripts/verify_sources.py
```

找到：

```python
SOURCES = [
    ("zbds_iptv4_txt", "https://live.zbds.top/tv/iptv4.txt"),
    ...
]
```

按同样格式新增一行：

```python
("your_source_name", "https://example.com/your_playlist.m3u"),
```

规则：

- `your_source_name` 建议只用英文、数字、下划线。
- 第二个字段填写 TXT / M3U / M3U8 聚合源地址。
- 新增后可手动运行 GitHub Actions，或等待每天自动维护。
- 如果想调整新源优先级，修改同文件里的 `source_priority()`。

## CDN 说明

电视长期订阅优先填写 jsDelivr `@main` 地址。优点是稳定、不容易出现电视端“获取数据为空”；缺点是维护完成后可能短时返回上一版。项目每次发布后会主动 purge jsDelivr，但第三方全球 CDN 的边缘节点刷新不能保证 100% 立刻生效。

如需立即验证最新版，优先看 GitHub Raw 或 gh-proxy Raw；电视端长期使用仍建议 jsDelivr `@main`。
