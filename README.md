# TV Live Auto Check

IPTV 自动维护项目：抓取公开直播源，对去重后的真实播放 URL 做媒体流检测，只发布检测到可播放分片/媒体字节的线路，并生成适合酷9/TCL 电视端导入的订阅列表。

## 推荐订阅地址

如果电视端能正常访问 GitHub Pages，优先使用这个地址；它当前最接近仓库最新版，适合自动更新后尽快生效：

```text
https://hujianj.github.io/tv-live-auto-check/ku9-live.txt
```

如果电视端访问 GitHub Pages 显示数据为空，再使用 jsDelivr 的 GCore 边缘地址作为稳定兼容地址；它通常更容易被电视端拉取，但第三方 CDN 可能短时返回上一版：

```text
https://gcore.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/ku9-live.txt
```

历史兼容地址 `live-curated.txt` / `live.txt` / `live-verified.txt` 仍会生成，但不同 jsDelivr 边缘节点可能对不同文件路径缓存不同步；电视端长期订阅优先用上面的 `ku9-live.txt`。

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
- 抓取 `config/sources.json` 中启用的所有上游公开源。
- 对所有去重后的真实流 URL 做全量检测；同一个 URL 被多个频道名引用时只检测一次，再复用检测结果。
- HLS 检测会打开播放列表，并继续检测下一级媒体分片；默认最多检测 2 个 variant、每个媒体列表最多 2 个分片。
- 生成电视端主订阅 `live-curated.txt`、同内容别名 `live.txt` / `live-verified.txt` / `ku9-live.txt`，以及 `live.m3u`。
- 全量明细 `stream_check_results.csv`、`live-all-playable.txt`、`all-playable.m3u` 不再提交到 Git 仓库，只作为 GitHub Actions artifact 保存 30 天。
- 发布前会先运行 `scripts/test_playlist_logic.py` 单元测试，再运行统一校验 `scripts/validate_playlist.py`，同时检查 TXT 和 M3U，防止异常频道名、异常 URL、错误分类或不可解析行进入正式列表。
- 正式提交前会运行 `scripts/recheck_published.py`，对最终发布列表里的每个唯一 URL 再做一次全量复测；复测失败的 URL 会从本次发布中剔除。
- 每次最终复测后会更新 `stability-history.json`，记录最终候选 URL 的成功/失败次数和连续成功/失败状态；下一轮整理时会优先排列历史更稳定的线路，降低反复波动源排在前面的概率。
- 发布前会运行 `scripts/audit_coverage.py`，生成核心央视和重点卫视频道覆盖报告；如果核心 CCTV 或重点卫视缺失，会拒绝发布，避免只看总行数而漏掉家人常看的频道。
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

分类顺序、分类关键词、港台/海外过滤词、异常频道名拦截词、卫视排序、核心频道覆盖清单集中维护在：

```text
config/rules.json
```

修改该文件后，单元测试会检查是否误写入 `????` 或乱码替换符，防止规则配置损坏后影响自动发布。

源排序和 URL 偏好集中维护在：

```text
config/priority.json
```

其中 `stability` 字段控制历史稳定性评分。历史文件 `stability-history.json` 会被限制最大条目数，避免为了稳定性评分再次制造大文件膨胀。

发布防缩水阈值、核心源清单、分类最低数量集中维护在：

```text
config/guard.json
```

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
config/sources.json
```

按同样格式新增一个对象：

```json
{
  "name": "your_source_name",
  "url": "https://example.com/your_playlist.m3u",
  "enabled": true
}
```

规则：

- `name` 建议只用英文、数字、下划线，后续报告和优先级规则都依赖这个稳定标识。
- `url` 填写 TXT / M3U / M3U8 聚合源地址。
- 临时不用的源不要删除，可把 `enabled` 改成 `false` 并写明 `note`。
- 新增后可手动运行 GitHub Actions，或等待每天自动维护。
- 如果想调整新源优先级，修改 `config/priority.json`，不要再改脚本里的排序逻辑。
- 如果这个新源是家人常看频道的重要保障源，把它加入 `config/guard.json` 的 `core_sources`。

## CDN 说明

电视长期订阅优先填写 jsDelivr `@main` 地址。优点是稳定、不容易出现电视端“获取数据为空”；缺点是维护完成后可能短时返回上一版。项目每次发布后会主动 purge jsDelivr，但第三方全球 CDN 的边缘节点刷新不能保证 100% 立刻生效。

如需立即验证最新版，优先看 GitHub Raw 或 gh-proxy Raw；电视端长期使用仍建议 jsDelivr `@main`。
