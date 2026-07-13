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

## é¢éåç±»è§å

é¢éä¼æå½åçµè§è§çä¹ æ¯èªå¨åç±»ï¼

1. å¤®è§é¢é
2. å«è§é¢é
3. å°æ¹é¢é
4. å½±è§å§åº
5. å°å¿å¨æ¼«
6. ä½è²çºªå®
7. é³ä¹ç»¼èº
8. çæ´»ä¼é²
9. ç»¼åå¨±ä¹
10. æ¸¯æ¾³å°é¢é
11. æµ·å¤åè¯­é¢é

`CCTV` ä¼æ `CCTV-1, CCTV-2, CCTV-3...` æåºï¼å¤è¯­é¢éåçº¯è±æåç±»ä¼å°½éæé¤æåç§»ï¼çµè§ä¸»åè¡¨ä¼è¿æ»¤ `Not24/7`ãä¼ª CCTVãä»¥å PlutoTV/RedBull/æµ·å¤çº¯è±æå¨±ä¹ç­éå®¶ç¨é¢éï¼RTHK/TVB/TVBS/ViuTV ç­æç¡®æ¸¯æ¾³å°åçä¿çå¨æ¸¯æ¾³å°åç±»ã

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

## CDN è¯´æ

çµè§é¿æè®¢éä¼åå¡«å jsDelivr `@main` å°åï¼ä¼ç¹æ¯ç¨³å®ãä¸å®¹æâè·åæ°æ®ä¸ºç©ºâï¼ç¼ºç¹æ¯ç»´æ¤å®æåå¯è½ç­æ¶è¿åä¸ä¸çãé¡¹ç®ä¼å¨æ¯æ¬¡åå¸åä¸»å¨ purge jsDelivrï¼ä½ jsDelivr å±äºç¬¬ä¸æ¹å¨ç CDNï¼è¾¹ç¼èç¹å·æ°ä¸è½ä¿è¯ 100% ç«å»çæã

å¦æä½ å¸æç»´æ¤å®æåç«å»æ¿å°ææ°çæ¬ï¼å¯å¨çµè§ç«¯æµè¯ `gh-proxy.com/raw.githubusercontent.com/.../live-curated.txt` ä»£çå°åï¼æ¬é¡¹ç®ä¼å¨ Actions ä¸­æ£æ¥å®æ¯å¦è½æ¿å°ææ°æä»¶ã

`github.io` / `raw.githubusercontent.com` ä¿çç»çµèæµè§å¨æäººå·¥æµè¯ï¼é¨åçµè§ç½ç»å¯è½è·åä¸ºç©ºæè¿æ¥å¤±è´¥ãjsDelivr å¶å°ç­æ¶æ»åå±æ­£å¸¸ç°è±¡ï¼å¦éç«å³éªè¯ææ°çæ¬ï¼ä¼åä½¿ç¨ gh-proxy Raw å°åã
