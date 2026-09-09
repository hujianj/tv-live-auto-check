# Published playlist recheck report

Outputs rewritten: True
Elapsed: 44.3s
Rows before: 10
Rows after: 12
Rows removed from outputs: 1
Candidate rows failing strict recheck: 1
Rows refilled after strict recheck: 3
Net output row delta: +2
Failed unique URLs after slow retry: 1
Slow retry attempted unique URLs: 1
Slow retry recovered unique URLs: 0
Core live-progress check required: True
Broadcast live-progress check required: True
Live-progress groups: 卫视频道, 地方频道, 央视频道
Video track required: True
Video-track verified final unique URLs: 12
Refill attempted unique URLs: 3
Refill playable unique URLs: 3
Refilled rows: 3
Historical fallback candidates attempted: 3
Historical fallback rows accepted: 3
Unresolved refill rows: 1

## Group deltas

| Group | Before | After | Net delta |
|---|---:|---:|---:|
| 央视频道 | 6 | 7 | +1 |
| 卫视频道 | 1 | 0 | -1 |
| 地方频道 | 1 | 3 | +2 |
| 港澳台频道 | 2 | 2 | +0 |

## First failed rows

- 卫视频道 / 北京卫视 / http://go.bkpcp.top/mg/bjws / final slow retry failed attempt=1 first=PublicURLPolicyError('host resolves to non-public address(es): jxcbn.ws01-cdn.gitv.tv -> 127.0.0.1'); last=PublicURLPolicyError('host resolves to non-public address(es): jxcbn.ws01-cdn.gitv.tv -> 127.0.0.1')
