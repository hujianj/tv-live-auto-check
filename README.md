# TV Live Auto Check

这是给家用电视/酷9准备的 IPTV 自动维护项目：定时抓取公开上游直播源，解析频道，去重后实测真实媒体流分片，只发布通过检测的可播放线路，并按家人使用习惯整理成酷9可导入的 TXT 列表和通用 M3U 列表。

此分支正在迁移来源许可和国内中文筛选规则。代码测试通过不等于新订阅已发布；只有完整维护运行通过覆盖、质量和发布校验后，才会替换 `main` 中的订阅文件。失败运行的 `output/` 只提供本轮诊断结果，不能冒充正式长期订阅。

2026-09-07 核查：云端第 177 次主维护确认在首检阶段两次达到 1800 秒后退出，第二次重新检测全部 22849 个 URL，未执行发布和 CDN 检查。修复分支加入检测前筛选、同轮成功结果续检、整条 URL 时间预算和最终视频帧解码。120 项离线测试通过，但这不等于新订阅已发布。先前本地全流程复检保留 13 条线路，因核心频道缺失未发布；该轮发生在实际解码增强之前，不能作为解码成功证据。完整证据与未完成项见 [迁移审查记录](docs/review-2026-09-07.md)。

## 当前维护范围

- 只验证**当前执行环境的网络**。不再筛选辽宁本地频道，不要求提供电视宽带信息，也不把检测结果表述为“辽宁地区验证通过”。本地执行与 GitHub Actions 执行分别代表各自当时的网络。
- 频道范围为国内中文电视，包括明确中文的港澳台频道。央视、卫视、地方台在前，少量娱乐分类随后，港澳台中文频道靠后。国外频道、国外华语台和外语子频道均排除，不再生成海外华语分类。`TVB Pearl`、`ViuTVsix`、`RTHK34/35` 不因品牌属于港澳台而放行。
- 频道语言依据来源元数据和具体频道身份筛选，不是语音识别；中文名称本身不能证明节目全程为中文。上游明确的外国归属或非中文语言标签优先于名称。
- `config/home-priority.json` 的家庭网络额外排序已默认关闭。无需配置所在地、运营商或家庭网络检测节点。
- 原始来源记录不删除。`rights_status: pending/restricted` 仅记录、抓取静态数据或待审核候选，不进入正式媒体候选；只有有明确、带日期的许可依据且通过检测的来源可参与发布。应用/代码许可证不等于电视节目版权授权。

四个参考项目均保留独立的 `catalog` 配置：`youhunwl/TVAPP`、`qist/tvbox`、`Huameng11/yingshiTV`、`tushen6/Tomorrow`。只读取公开说明和静态候选链接，不执行 APK、JAR、spider 或私有接口。当前 `iptv-org` 的许可依据仅覆盖公开链接目录，不表示项目取得了电视节目再分发权。

来源审核与使用边界见 [来源许可记录](docs/source-permissions.md)。BurningC4 和 Free-TV 按各自 README 明确的播放器订阅说明接入；不将链接目录的使用许可解释为节目内容再分发权。

来源最新状态即时写入 `source-inventory.json`，作为 Actions 诊断 artifact 保存，不提交每日大文件。该文件包含格式、超时、启用状态、许可说明、抓取时间、解析数、策略排除原因和进入媒体检测的数量。`full-check-summary.json` 区分 `parsed_candidates`、`eligible_candidates`、`policy_excluded_candidates` 与实际检测数，不能把未检测候选计为可播放。

## 推荐订阅地址

结合这台电视此前的实际测试，酷9长期订阅优先使用电视端可正常访问的 jsDelivr 固定地址：

```text
https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/ku9-live.txt
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

GitHub Actions 每天北京时间 04:20 和 16:20 各计划运行一次，也可以手动 `Run workflow`。GitHub 托管运行器可能延迟几十分钟启动，因此这是计划时间，不是精确执行时刻。独立 watchdog 每天另外检查两次维护新鲜度、Raw、发布清单和电视主订阅端点。

手动选择非默认修复分支时，只执行验证和保存诊断 artifact，不提交播放列表、不刷新正式 CDN、不发送正式维护状态通知。定时发布只来自默认分支。

流程：

1. 读取 `config/sources.json` 中 `enabled` 源和允许自动恢复探测的 `auto_recover` 源；永久禁用源不参与本轮。
2. 抓取 TXT / M3U / M3U8 / JSON / XML 聚合列表；目录型来源只记录静态链接。HLS 媒体清单不能当作频道目录解析，HTML 错误页和 XML DTD/实体拒绝解析。
3. 解析频道名、分类和播放 URL。
4. 先执行来源许可、国内中文频道和地址安全筛选，再按频道名和实际 URL 去重。排除鉴权、临时签名、过期参数、播放请求头依赖和 DRM，不固化检测重定向产生的临时地址。
5. 对筛选范围内的所有唯一 URL 做真实媒体流检测；HLS 会继续检查子播放列表和媒体分片。每条线路请求和重试共享 60 秒预算；连接地址重试、读流和单主机排队检查剩余预算，整个阶段另有进程级时限。系统 DNS 调用仍受操作系统行为影响，不能把单请求超时当作绝对进程时限。
6. 只保留检测可播放的 URL。
7. 按 `config/rules.json` 和 `config/quality.json` 做家用分类、过滤和限量。
8. 生成 `live-curated.txt` / `live.txt` / `live-verified.txt` / `ku9-live.txt` / `live.m3u`。
9. 对最终发布列表再做一次全量 URL 复测；每个保留、慢速重试及补位地址必须实际解出至少 3 帧视频，不能只靠容器轨道声明通过。FFmpeg 仅处理安全下载的有限媒体字节，禁用网络和文件输入协议，最多 4 个解码进程、每次 12 秒，并受 URL 总预算约束。失败地址低并发重试后才删除并从候选池补线。央视、卫视、地方台还要求 HLS 直播推进；历史线路必须重新通过本轮全部检测，不会直接复用。
10. 运行核心频道覆盖审计、最终质量审计和防缩水发布守卫。
11. 最终写入体积审计结果，再生成不包含自哈希的 `publish-manifest.json`，对所有其余发布文件的最终大小和 SHA256 做不可变校验。
12. 完整跨文件校验和公开产物校验全部通过后，幂等应用本轮稳定性 observation；`stability-state.json` 只保存为 90 天 Actions artifact，不再每天提交大状态文件。下一轮仅从最近一次成功的主维护运行恢复并严格校验状态，缺失或损坏时从空状态安全启动。近期更稳定的线路会在下一轮排序更靠前；证据计数有上限并互相衰减，`last_seen` 只按北京时间周起始日更新。
13. 成功保存稳定性 artifact 且远端代码没有变化时，才提交新版直播源。
14. 发布后检查 GitHub Raw 和电视固定使用的主 jsDelivr URL；主 jsDelivr 仍旧时记录为“发布成功、CDN 同步中”并自动告警，不回滚已经通过媒体检测的 Git 提交。

最终复测摘要会分别记录实际删除行数、重新验证后补回行数和净行数变化；补线使最终行数高于本轮初始候选时，不会再用负数“删除行数”表达。

复检提前中止时，摘要明确写入 `status: aborted`、`outputs_rewritten: false` 和实际检测失败数；`candidate_after_rows` 仅表示可考虑保留的候选行数，原文件未变时 `after_rows` 不伪装成新版发布数。CSV 保留成功和失败线路的真实上游来源。诊断 `output/report.json` 的 schema 为 2，分别记录首检、严格复检、视频轨道检测及证据时效；尚未执行的检测使用 `null`，不会当作成功或 0 次失败。

防缩水守卫按标准化后的独立频道计数，不再要求 1800 条线路、90 条央视线路等旧门槛。绝对覆盖要求为 29 个频道，其中央视至少 18 个、卫视至少 10 个、地方台至少 1 个；`config/rules.json` 还会核对具体核心频道身份。同一个 CCTV-1 的大量备用线路不能冒充其他频道。相对跌幅也按独立频道比较，第一次没有同口径基线时仍执行绝对门禁。

每个指定核心频道必须有至少 1 条本轮严格检测通过的线路；备用 URL 少于 4 条或主机少于 3 个会告警，但不会因同一频道只有一条真实可播线路而拒绝整份结果。所有保留的备用线路也必须通过本轮检测。家庭精简列表不再要求凑够 700 行。节目缺失与备用不足分开报告，不制造线路凑数。

当严格播放策略首次扩展到新的广播分类时，旧规则产出的行数不能作为同口径相对基线。该次迁移仍强制执行总量和央视/卫视/地方台的绝对下限、覆盖审计、质量审计及完整发布校验，但只跳过一次相对跌幅比较；新版本成功发布后立即恢复正常相对门禁，不会永久放宽阈值。

`verify_sources.py` 和 `recheck_published.py` 两个真实网络检测阶段允许有限重试；首次网络失败后的重试从失败阶段继续，不再重新跑已经成功的前置阶段。重试会延长单请求超时并降低上游列表抓取并发，但保留足够的媒体检测与单主机并发容量，避免 2.8 万级 URL 全量检查在阶段时限内无法收尾。媒体任务使用按主机的在途准入调度，慢主机不能用排队任务占满线程池；HTTP 层仍保留第二道单主机信号量，覆盖重定向和 HLS 子资源。防缩水守卫如果第一次因网络波动或上游瞬时缩水明确拒绝，会自动从 `verify_sources.py` 重新跑一轮独立确认；确认轮仍失败才停止发布。每个阶段和整条流水线都有独立硬时限，超时会以退出码、阶段、配置时限和失败分类写入 `maintenance-run.json`，不会只留下 GitHub 的笼统超时。guard 的策略拒绝使用专用退出码；程序崩溃、确定性阶段超时或子进程无法启动会直接失败，不会被误当成网络缩水而浪费一次全量扫描。两轮证据既作为小型 artifact 保存，也内嵌到运行报告；告警 Issue 会直接列出每轮配置、最终行数、央视/卫视/地方台数量、复测删除与补回、历史候选补线及具体 guard 失败规则。分类、质量审计、防缩水、体积和清单校验仍属于确定性阶段，不能通过降低门槛重试掩盖。排队期间如果 `main` 已更新，旧运行会在昂贵检测前自动跳过；新的代码 push 会取消正在使用旧代码检测的运行，但计划和手动运行只排队、不互相取消。

上游源有三种生命周期状态：

- `enabled: true`：正常抓取和解析；还必须通过 `rights_status` 和频道筛选才能进入全量媒体检测与发布。
- `enabled: false, auto_recover: true`：进行恢复探测；只有许可合适、成功解析且通过筛选的频道，才加入本轮媒体检测和发布。
- `enabled: false, auto_recover: false`：永久禁用，不会被自动加入发布流程。

单个或多个上游不可用会记录告警，只要其余来源仍满足真实频道覆盖就可以发布。目录型 README 解析出 0 个频道是正常结果，待审核来源的失败也不会被误算为核心播放源故障。

严格维护运行生成的新版 `sources_status.csv` 会记录 `mode` 和 `contributed`，并由发布包校验器核对配置顺序、状态语义和汇总计数。旧版 7 列表头只在 `--committed-only` 迁移兼容路径接受，不能通过完整发布门禁。

其中 `contributed` / `sources_contributing` 是兼容字段，仅表示“抓取成功并解析出行”，不表示已获许可、已通过检测或最终发布。报告另列 `sources_media_eligible` 和最终来源分布，避免把待审核来源的解析数量算成可用贡献。

维护 workflow 完成后，独立的 `.github/workflows/cdn-reconcile.yml` 会只对 GitHub Raw 和电视主 jsDelivr 地址执行多轮 purge/check；它不会重复 2.8 万条媒体 URL 检测。CDN 暂时滞后与媒体检测失败使用不同告警 Issue，CDN 恢复时不会误关闭媒体检测告警。

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

严格复检使用不可变的整理阶段 checkpoint。每次重试前都会核对 SHA256 并恢复同一份输入；复检输出先在 `.maintenance-staging` 中完整生成和校验，再通过带事务日志与回滚备份的文件组提升替换工作区结果。稳定性 observation 只在覆盖、质量、防缩水、完整 bundle 和发布 manifest 全部通过后应用一次，单次运行重试不会重复累计证据。

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

`CCTV` 会按 `CCTV-1, CCTV-2, CCTV-3...` 排序。外语频道、国外频道、国外华语台、Not24/7、Geo-blocked、PlutoTV、RedBullTV 等会被过滤。TVB Jade、TVBS、RTHK31 等具体中文频道可以保留在靠后的港台分类中，不能仅凭 TVB/RTHK 品牌放行外语子频道。

最终质量审计会额外检查：

- 严格过滤词是否残留；
- 核心 CCTV 是否有足够的精确线路数；
- 重点卫视是否有足够的线路数；
- 核心频道是否缺失，以及备用线路和主机多样性是否不足（缺台阻断，备用不足告警）；
- 单一主机和前五主机占比是否过高（默认告警但不阻断，避免低价值分类集中导致长期停更）；
- 每个频道名是否超过配置的最大线路数；
- 各分类是否超过配置的最大行数；
- 违反国内中文范围的残留项会阻断发布，并记录在报告中。

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

该优先级配置保留不变，但目前 `zbds_iptv4_txt` 的聚合使用许可仍为 `pending`，不会进入正式输出。确认许可并记录依据后，它通过检测的线路才会按此优先级参与排序；失败时自动选用其他本轮通过检测的线路。不会绕过许可门禁来满足源优先级。

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
  "format": "m3u",
  "timeout_seconds": 20,
  "update_method": "scheduled_fetch",
  "rights_status": "pending",
  "license": "unknown",
  "homepage": "https://example.com/",
  "terms_url": "",
  "reviewed_at": "",
  "permission_scope": "unconfirmed",
  "note": "待核对来源与公开使用说明"
}
```

规则：

- `name` 建议只用英文、数字、下划线，后续报告、优先级和守卫都依赖这个稳定标识。
- `url` 可以是 TXT / M3U / M3U8 / JSON / XML 聚合源地址；README 等项目目录用 `format: catalog`，只收集静态候选链接。
- 新源默认 `rights_status: pending`。确认允许该使用方式后，填写真实 `terms_url`、访问日期 `reviewed_at`、许可 `license` 和使用范围 `permission_scope`，再设为 `approved`；网页可打开、仓库有代码许可证都不能自动证明每条节目的再分发授权。
- 暂时不用或长期失败的源建议保留但设为 `enabled: false`，并在 `note` 写明原因。
- 临时失败但希望自动复查的源设为 `enabled: false, auto_recover: true`；恢复后必须先解析出候选频道才会参与媒体检测，不能仅凭源地址返回 HTTP 200 就发布。
- `enabled` 与 `auto_recover` 不能同时为 `true`；永久禁用源应同时保持两者为 `false`。
- 如果新源很重要，把它加入 `config/guard.json` 的 `core_sources`。
- 如果新源需要更高优先级，修改 `config/priority.json`，不要直接改脚本排序逻辑。

## 本地验证命令

依赖 Python 3.11 或更高版本、Git 和 `requirements.txt` 固定的 FFmpeg 运行包。推荐在独立 clone 中运行，因为维护脚本会重建工作目录中的播放文件和诊断文件，但不会自行执行 `git push`。

```powershell
python -m pip install -r requirements.txt
python scripts\media_decode.py
python scripts\run_maintenance.py --dry-run
python scripts\run_maintenance.py
```

本地需要限制并发时可在运行前设置 `IPTV_CHECK_WORKERS=32`、`IPTV_CHECK_WORKERS_PER_HOST=4`、`IPTV_FETCH_WORKERS=8`。这是负载控制，不是所在地或电视宽带配置。

输出分为两层：

- 正式候选：仓库根目录的 `ku9-live.txt`、`live.m3u`、`ku9-family.txt`、`family.m3u`，仅在全部门禁通过后由 Actions 提交。
- 当前运行诊断：`output/live.m3u`、`output/live.txt`、`output/current-network.m3u`、`output/stable.m3u`、`output/report.json`、`output/report.md`，作为 artifact 保存 30 天。依据最新要求不生成辽宁本地专用列表。稳定列表要求本轮通过和至少 3 次有效历史成功记录，没有足够证据时为空，并在报告明确标注。

失败运行也输出诊断，`publication_ready: false` 表示不可替换长期订阅。运行开始会清理这些生成文件，导出时重新核对来源配置指纹、检测时间和当前轮次，不使用残留的成功结果。

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

## 当前网络检测

下列命令只表示执行机器当时的网络，不模拟辽宁、运营商或电视宽带，也不能保证未来始终可播：

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
- 长期地址显式包含 `@main`，避免省略分支时额外的默认分支映射缓存；它仍是固定地址，不会随提交变化。
- jsDelivr 有时会滞后，项目会等待 Git 发布传播后主动 purge，并在失败时再次 purge/复验电视实际请求的固定 URL；主 `cdn.jsdelivr.net` 固定地址是硬门禁，不能再由 gh-proxy 或其他 jsDelivr 镜像替代通过。
- 第三方 CDN 仍不保证全球每个边缘节点同时刷新，因此项目验证的是 GitHub Runner 实际命中的固定 URL 节点，并保留 Raw 代理作为即时备用。
- 这台电视访问 GitHub Pages 曾出现“数据为空”，因此 Pages 只作为电脑端备用，不再建议作为电视主地址。

## 家用精简版

自动维护流程现在会同时生成完整列表和家用精简列表：

```text
完整主列表：https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/ku9-live.txt
家用精简版：https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/ku9-family.txt
家用精简版 M3U：https://cdn.jsdelivr.net/gh/hujianj/tv-live-auto-check@main/family.m3u
```

精简版从最终复测通过的列表里再筛选生成，不跳过真实播放检测；它会保留 CCTV、卫视、地方台优先顺序，并减少综合娱乐、海外等低频分类的数量，方便家人在电视上找台。

## 检测边界

- 当前检测验证 DNS/TCP/HTTP、HLS 子清单、媒体分片、容器视频轨道及广播频道的直播进度，不是用 HTTP 200 代替可播放。
- 最终检查执行有限分片的视频帧解码，不录制整场节目，不验证音频语言、节目画面身份或电视硬件兼容性。成功解出 3 帧不能证明将来持续播放或上游标注一定正确。读取超出采样上限、字节范围 HLS、动态初始化映射等暂不支持的格式会保守拒绝，不能伪造成功。
- 正式输出不固化运行中遇到的临时重定向、短期签名或令牌。加密/DRM HLS 直接拒绝，不请求密钥。普通固定 `key=txiptv` 不因参数名误删，但高熵 key、鉴权和到期参数仍需拒绝或审核。
- 失败线路保留诊断和历史记录、允许后续恢复，但不因历史成功而冒充本轮可播放备用源。GitHub 定时任务和 CDN 都可能延迟；CDN 与 Git 文件一致不代表频道已经重新检测。
- 家庭网络额外排序默认关闭，不需要用户提供所在地或电视宽带信息。
