# TV Live Auto Check

IPTV 自动维护项目：抓取公开直播源，对去重后的真实播放 URL 做媒体流检测，只发布检测到可播放分片/媒体字节的线路，并生成适合酷9/电视端导入的订阅列表。

## 推荐订阅地址

电视端/酷9优先使用 jsDelivr CDN 地址，国内网络通常比 `github.io` 和 `raw.githubusercontent.com` 更稳定：

```text
https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/live-curated.txt
```

如果你想在每次维护后尽快拿到“最新版本”，可测试 Raw 代理地址：

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

## 全量可播清单

`live-curated.txt` 是电视端友好的主订阅。完整检测明细和全量可播文件不再每天提交到仓库，避免 Git 历史持续膨胀；每次 Actions 成功后会作为 artifact 保存 30 天：

```text
stream_check_results.csv
live-all-playable.txt
all-playable.m3u
```

需要排查时，到 GitHub Actions 对应运行记录里下载 `full-iptv-check-<run_id>` artifact。

## 自动维护逻辑

- 每天北京时间 04:20 自动运行。
- 可在 GitHub Actions 手动点击 `Run workflow` 立即运行。
- 抓取 `scripts/verify_sources.py` 中配置的所有上游源。
- 对所有去重后的真实流 URL 做播放检测，不做抽样预筛；同一个 URL 被多个频道名引用时只探测一次，再复用检测结果，减少重复耗时。
- 真实检测逻辑会打开 HLS/媒体播放列表，并继续探测下一级媒体分片/媒体字节；HLS 默认检测最多 2 个 variant、每个媒体列表最多 2 个分片，以减少单分片假阳性。
- 生成：
  - `live-curated.txt`：电视端主订阅。
  - `live.m3u`：M3U 主订阅。
  - `stream_check_results.csv`：所有 URL 检测明细，作为 Actions artifact 保存，不再每日提交。
  - `live-all-playable.txt` / `all-playable.m3u`：全量可播清单，作为 Actions artifact 保存，不再每日提交。
  - `full-check-summary.json`：全量检测与最终发布摘要。
- Actions 会硬校验：`checked_candidates == unique_candidates`，这里的 `unique_candidates` 指去重后的真实流 URL 数，确保不是抽查。
- 本地 smoke test 通过后才提交发布，避免坏列表先进入仓库。
- 自动 purge jsDelivr；GitHub Raw / GitHub Pages / jsDelivr 缓存状态会被检查，CDN 边缘缓存短时滞后只记录告警，不阻断主发布。

## 频道分类规则

频道会按当前电视观看习惯自动分类：

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

`CCTV` 会按 `CCTV-1, CCTV-2, CCTV-3...` 排序；外语频道和纯英文分类会尽量排除或后移；电视主列表会过滤 `Not24/7` 和含 RTHK/TVB/ViuTV/港澳台标识的伪 CCTV 别名。

## 优先源

当前最高优先级源是：

```text
https://live.zbds.top/tv/iptv4.txt
```

对应源码标识：

```python
zbds_iptv4_txt
```

如果该源中某频道有可播放线路，会优先排在该频道前面；如果该源线路不可播，则自动使用其他已检测可播放线路。

## 如何新增上游直播源

只需要修改：

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
- 新增后可手动运行 GitHub Actions，或等每天自动维护。
- 如果想调整新源优先级，修改同文件里的 `source_priority()`。

## CDN 说明

电视长期订阅优先填写 jsDelivr `@main` 地址，优点是稳定、不容易“获取数据为空”；缺点是维护完成后可能短时返回上一版。项目会在每次发布后主动 purge jsDelivr，但 jsDelivr 属于第三方全球 CDN，边缘节点刷新不能保证 100% 立刻生效。

如果你希望维护完成后立刻拿到最新版本，可在电视端测试 `gh-proxy.com/raw.githubusercontent.com/.../live-curated.txt` 代理地址；本项目会在 Actions 中检查它是否能拿到最新文件。

`github.io` / `raw.githubusercontent.com` 保留给电脑浏览器或人工测试，部分电视网络可能获取为空或连接失败。
