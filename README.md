# TV Live Auto Check

这是给家用电视/酷9准备的 IPTV 自动维护项目：定时抓取公开上游直播源，解析频道，去重后实测真实媒体流分片，只发布通过检测的可播放线路，并按家人使用习惯整理成酷9可导入的 TXT 列表和通用 M3U 列表。

## 推荐订阅地址

结合这台电视此前的实际测试，酷9长期订阅优先使用电视端可正常访问的 jsDelivr 固定地址：

```text
https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check/ku9-live.txt
```

jsDelivr 边缘节点可能在自动更新后短时间返回上一版，但固定地址不需要在电视上反复修改。需要立即确认最新版时，使用 Raw 代理地址：

```text
https://gh-proxy.com/raw.githubusercontent.com/hujianj/tv-live-auto-check/main/ku9-live.txt
```

GitHub Pages 可作为电脑端或网络可访问设备的备用入口；此前这台电视访问 GitHub 域名曾出现“数据为空”，因此不再把它列为电视端第一选择：

```text
https://hujianj.github.io/tv-live-auto-check/ku9-live.txt
```

M3U 格式：

```text
https://hujianj.github.io/tv-live-auto-check/live.m3u
```

历史兼容别名 `live-curated.txt` / `live.txt` / `live-verified.txt` 仍会生成，内容与 `ku9-live.txt` 一致。

## 自动维护逻辑

GitHub Actions 每天北京时间 04:20 计划运行，也可以手动 `Run workflow`。GitHub 托管运行器可能延迟几十分钟启动，因此 04:20 是计划时间，不是精确执行时刻。

流程：

1. 读取 `config/sources.json` 中启用的所有上游源。
2. 抓取 TXT / M3U / M3U8 聚合列表。
3. 解析频道名、分类和播放 URL。
4. 对同一 URL 去重，避免重复检测。
5. 对所有唯一 URL 做真实媒体流检测；HLS 会继续检查子播放列表和媒体分片。
6. 只保留检测可播放的 URL。
7. 按 `config/rules.json` 和 `config/quality.json` 做家用分类、过滤和限量。
8. 生成 `live-curated.txt` / `live.txt` / `live-verified.txt` / `ku9-live.txt` / `live.m3u`。
9. 对最终发布列表再做一次全量 URL 复测；第一轮失败的所有最终 URL 会以更低并发和更长超时再试一次，确认失败后才删除并从候选池补线。
10. 更新 `stability-history.tsv`，让历史更稳定的线路在下一轮排序更靠前。
11. 运行核心频道覆盖审计、最终质量审计和防缩水发布守卫。
12. 最终写入体积审计结果，再生成不包含自哈希的 `publish-manifest.json`，对所有其余发布文件的最终大小和 SHA256 做不可变校验。
13. 完整跨文件校验和公开产物校验全部通过后才提交新版直播源。
14. 发布后检查 GitHub Raw 和电视固定使用的主 jsDelivr URL；主 jsDelivr 仍旧时即使其他代理已更新也会判定维护失败。

大体积诊断文件不会再进入 Git 历史，只作为 GitHub Actions artifact 保存 30 天：

```text
stream_check_results.csv
live-all-playable.txt
all-playable.m3u
published_recheck_results.csv
curated-source-map.csv
curated-candidate-pool.csv
alias-conflict-report.md
```

`curated-source-map.csv` 和 `curated-candidate-pool.csv` 每次都会生成，但只存放在 Actions artifact 中，不是仓库内的公开订阅文件。`full-check-summary.json` 会用 `*_generated` 和 `*_artifact_only` 字段明确区分这两种语义。

`publish-manifest.json` 是最终公开产物清单。它记录除自身以外的所有发布文件最终大小和 SHA256；清单自身不记录自己的哈希，从设计上避免 `full-check-summary.json` 过去那种“写回审计数据后自身大小和哈希立即失效”的循环依赖。另有只读、无仓库写凭据的轻量 CI，会在代码或公开产物被直接修改时运行单元测试和清单校验，不触发三万 URL 的昂贵全量检测。

## 频道分类与质量规则

电视主列表优先顺序：

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

`CCTV` 会按 `CCTV-1, CCTV-2, CCTV-3...` 排序。外语频道、纯英文频道、Not24/7、Geo-blocked、PlutoTV、RedBullTV、Discovery、NatGeo、CartoonNetwork 等不适合家用主列表的频道会被过滤。TVB / RTHK / TVBS / ViuTV / 凤凰等明确港澳台或华语频道会保留在靠后的分类中。

最终质量审计会额外检查：

- 严格过滤词是否残留；
- 核心 CCTV 是否有足够的精确线路数；
- 重点卫视是否有足够的线路数；
- 每个频道名是否超过配置的最大线路数；
- 各分类是否超过配置的最大行数；
- 仍残留的疑似英文/海外频道会进入报告供后续人工调整。

核心配置文件：

```text
config/sources.json   # 上游源列表
config/rules.json     # 分类、过滤、核心频道覆盖规则
config/quality.json   # 家用质量过滤、每频道线路数、分类总量限制、最终质量审计阈值
config/priority.json  # 源优先级、URL 偏好、稳定性评分
config/guard.json     # 防缩水阈值、发布体积阈值、核心源守卫
```

## 当前最高优先级源

优先使用：

```text
https://live.zbds.top/tv/iptv4.txt
```

对应源标识：

```text
zbds_iptv4_txt
```

如果这个源中某个频道有可播放线路，它会优先排在该频道前面；如果不可播放，程序会自动使用其他已经检测可播放的线路。

## 如何新增上游直播源

修改：

```text
config/sources.json
```

新增一个对象：

```json
{
  "name": "your_source_name",
  "url": "https://example.com/your_playlist.m3u",
  "enabled": true,
  "note": "optional note"
}
```

规则：

- `name` 建议只用英文、数字、下划线，后续报告、优先级和守卫都依赖这个稳定标识。
- `url` 可以是 TXT / M3U / M3U8 聚合源地址。
- 暂时不用或长期失败的源建议保留但设为 `enabled: false`，并在 `note` 写明原因。
- 如果新源很重要，把它加入 `config/guard.json` 的 `core_sources`。
- 如果新源需要更高优先级，修改 `config/priority.json`，不要直接改脚本排序逻辑。

## 本地验证命令

基础验证：

```powershell
Get-ChildItem scripts\*.py | ForEach-Object { python -m py_compile $_.FullName }
python scripts\test_playlist_logic.py
python scripts\validate_playlist.py live-curated.txt live.txt live-verified.txt ku9-live.txt live.m3u ku9-family.txt live-family.txt family.m3u
python scripts\audit_coverage.py
python scripts\audit_quality.py
python scripts\guard_publish.py
python scripts\audit_publish_size.py
python scripts\validate_publication.py
```

完整流水线运行后还会生成 `curated-source-map.csv`、`curated-candidate-pool.csv` 和 `alias-conflict-report.md` 等瞬态文件，此时必须执行跨文件一致性校验：

```powershell
python scripts\validate_publish_bundle.py
python scripts\validate_publication.py
```

必须保持顺序为 `guard_publish.py` → `audit_publish_size.py` → `validate_publish_bundle.py` → `validate_publication.py`，因为前两个脚本会定稿报告和 summary，后两个校验器必须检查最终不再修改的字节。

完整跨文件校验会核对 TXT/M3U 顺序、别名文件、家庭精简版、来源映射、分类顺序和 `full-check-summary.json` 统计；普通 clone 没有 Actions 瞬态文件时，应先运行完整维护流程。


如果本地有最新的 `stream_check_results.csv`，可以重新整理当前检测结果：

```powershell
python scripts\curate_ku9.py
python scripts\recheck_published.py
python scripts\audit_coverage.py
python scripts\audit_quality.py
python scripts\validate_playlist.py live-curated.txt live.txt live-verified.txt ku9-live.txt live.m3u ku9-family.txt live-family.txt family.m3u
python scripts\guard_publish.py
python scripts\audit_publish_size.py
python scripts\validate_publish_bundle.py
python scripts\validate_publication.py
```

## 家庭网络检测

GitHub Actions 能播放，不等于你家电视网络一定能播放。为了模拟家里网络，可以在本机运行：

快速检查 CCTV 和重点卫视：

```powershell
python scripts\local_network_check.py --core-only --workers 24 --timeout 15
```

检查电视实际订阅地址的全部频道：

```powershell
python scripts\local_network_check.py --workers 32 --timeout 15
```

如果 Pages 地址在电视或本机网络不稳定，可以检查备用地址：

```powershell
python scripts\local_network_check.py --url https://gh-proxy.com/raw.githubusercontent.com/hujianj/tv-live-auto-check/main/ku9-live.txt --core-only --workers 24 --timeout 15
```

生成的结果不会提交到 Git：

```text
local-network-report.md
local-network-results.csv
```

## CDN 说明

- GitHub Raw 是发布校验的权威基准，gh-proxy 适合立即查看最新版。
- 这台电视已实测 jsDelivr 固定地址可用，因此长期订阅仍优先使用 jsDelivr。
- jsDelivr 有时会滞后，项目会主动 purge 并校验电视实际请求的固定 URL；主 `cdn.jsdelivr.net` 固定地址是硬门禁，不能再由 gh-proxy 或其他 jsDelivr 镜像替代通过。
- 第三方 CDN 仍不保证全球每个边缘节点同时刷新，因此项目验证的是 GitHub Runner 实际命中的固定 URL 节点，并保留 Raw 代理作为即时备用。
- 这台电视访问 GitHub Pages 曾出现“数据为空”，因此 Pages 只作为电脑端备用，不再建议作为电视主地址。

## 家用精简版

自动维护流程现在会同时生成完整列表和家用精简列表：

```text
完整主列表：https://hujianj.github.io/tv-live-auto-check/ku9-live.txt
家用精简版：https://hujianj.github.io/tv-live-auto-check/ku9-family.txt
家用精简版 M3U：https://hujianj.github.io/tv-live-auto-check/family.m3u
```

精简版从最终复测通过的列表里再筛选生成，不跳过真实播放检测；它会保留 CCTV、卫视、地方台优先顺序，并减少综合娱乐、海外等低频分类的数量，方便家人在电视上找台。

## 家庭网络优先级

在家里网络运行：

```powershell
python scripts\local_network_check.py --core-only --workers 24 --timeout 15 --write-home-priority
```

会更新 `config/home-priority.json`，后续自动整理会优先家里实际可播的 URL，并降权家里失败的 URL。
