# 来源使用依据

核对日期：2026-09-09。以下是项目运营范围内的来源审核记录，不表示获得电视节目的再分发权。项目只整理链接供家庭播放器调用，不转播、代理、录制或重新许可视频内容。

## 已接入检测

| 来源 | 依据 | 本项目使用范围 |
|---|---|---|
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | [Unlicense](https://github.com/iptv-org/iptv/blob/master/LICENSE) 及 README 的公开链接目录说明 | 选择国内中文公开流链接；不取得节目的再分发权 |
| [BurningC4/Chinese-IPTV](https://github.com/BurningC4/Chinese-IPTV) | [README](https://github.com/BurningC4/Chinese-IPTV/blob/master/README.md) 明确说明 IPTV 播放器可使用 `TV-IPV4.m3u` 和 `guide.xml` | 按作者明确的播放器用法调用公开列表，选择无需鉴权的链接供家庭订阅；保留出处 |
| [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | [README](https://github.com/Free-TV/IPTV/blob/master/README.md) 写明 `To use it point your IPTV player to ...playlist.m3u8`；同时要求只收录官方免费频道 | 按作者明确的播放器用法调用公开列表；只选符合国内中文规则且实测通过的链接 |
| [vbskycn/iptv / live.zbds.top](https://live.zbds.top/) | 2026-09-09 首页明确提供电视播放器订阅，并写明“引用本项目内容到其他仓库...务必要遵守开源协议，必须注明来源”；GitHub `LICENSE` 为 GPL-3.0 | 按明确的引用说明整合公开链接目录，保留署名及许可证，不转播媒体；IPv4 TXT 优先，IPv6 仍需在当前环境实测 |

后两个项目的 GitHub `license` API 返回 404，因此不把它们描述为 MIT、GPL 或允许任意再分发的代码仓库。这里的使用依据是作者明确邀请播放器调用，范围仅限个人订阅链接，不复制上游完整文档、图片或媒体。发现具体频道要求登录、签名、付费、DRM、访问控制绕过，或收到权利限制说明时，不能继续发布该线路。

核对记录：

- BurningC4 README blob：`dac601c3aaef1505d3c0b44b845a1b6ff75161b0`，SHA256 `b395ced3d21cf71fd9d3a479f033d38e8fd3c362b09678f141ad575834ad27b9`。
- Free-TV README blob：`2c4640904cb55e3c35238b6851be18e0898ebabe`，SHA256 `426028fe06af5f8c3f5ec3a532d4f462c9fe5fc9c846b943555cab9541e74079`。
- vbskycn LICENSE blob：`94a9ed024d3859793618152ea559a168bbcbb5e2`；[原文](https://github.com/vbskycn/iptv/blob/master/LICENSE)与[本地副本](GPL-3.0.txt)。首页快照 SHA256 `82ef8862b42ef34a23283898675d6c66f803968d03a58a2d439d9136bc29c329`。

vbskycn 首页同时写有技术研究、非商业说明，以及不保证第三方媒体合法性、稳定性的声明。此次允许的是该页明确列出的公开链接目录引用，不将 GPL 或作者声明解释为电视节目版权授权；有付费、访问控制、DRM 或具体权利争议的地址仍排除。派生的链接选集按 GPL-3.0 提供，所有筛选修改和配置在本仓库公开；视频内容不适用该许可证。

频道英文显示名不是外语音轨证据。`config/rules.json.domestic_channel_aliases` 记录已核对的频道 ID、原名和中文名；只对指定目录来源和精确 ID/原名组合生效。依据为 [iptv-org 频道目录](https://iptv-org.github.io/api/channels.json) 中的别名及电视台网站，2026-09-09 快照 SHA256 `138123701d5c082130305b2081e5dece66187f43771c950416766749c86a873c`。不将所有 `.cn` 条目直接认定为中文，显式外语元数据、限制标记和未知频道仍拒绝。

## 保留但不进入长期订阅

| 来源 | 实际说明或检测情况 | 处理 |
|---|---|---|
| suxuang/myIPTV | README 要求仅学习研究，禁止商业用途，并于 24 小时内删除 | `restricted`，保留原记录 |
| Kimentanm/aptv | README 明确“仅用于产品测试使用，禁止传播” | `restricted`，保留原记录 |
| fanmingming/live | 代码 GPL 不等于流授权；README 对流列表规定测试研究用途 | 继续待审核 |
| Guovin/iptv-api | 软件许可证存在，但 README 明确要求目标站点授权，不授权未获许可的节目源 | 代码可研究；默认列表继续待审核 |
| vamoschuck/TV | README 为空，license API 404 | 继续待审核 |
| BigBigGrandG/IPTV-URL | 标注个人自用源，未找到允许本项目长期聚合的明确说明 | 继续待审核 |
| YanG-1989/m3u | README 限学习交流用途，代码中给出的 hosts 等操作不执行 | 继续待审核 |
| epg.pw | 2026-09-09 已能获取 [Terms](https://epg.pw/terms.html)：仅个人使用，禁止公开发布或再传输站点服务的部分内容 | 保留记录，不能据此批准公开仓库再发布 |

四个参考项目仍作为独立静态目录记录：`youhunwl/TVAPP`、`qist/tvbox`、`Huameng11/yingshiTV`、`tushen6/Tomorrow`。不执行 APK、JAR、spider，也不追踪需要登录或破解的接口。

新增来源修改 `config/sources.json`。先填写 `rights_status: pending`，记录可核验的 `terms_url`、ISO 日期 `reviewed_at` 和具体 `permission_scope`。有明确依据后才改为 `approved`；这只允许进入检测，不直接赋予“可播放”状态。
