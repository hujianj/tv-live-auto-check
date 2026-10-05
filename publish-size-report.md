# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 284840
Unique payload blob bytes: 188684
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 66252

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22084 | 4db97e560f3bf1386fdee27694710bf8f6100433d8cb7c581a4193ec72f543c7 | 9654e878cdedbaea4ef00577f18b6cfc95c751b2 |
| live.txt | 22084 | 4db97e560f3bf1386fdee27694710bf8f6100433d8cb7c581a4193ec72f543c7 | 9654e878cdedbaea4ef00577f18b6cfc95c751b2 |
| live-verified.txt | 22084 | 4db97e560f3bf1386fdee27694710bf8f6100433d8cb7c581a4193ec72f543c7 | 9654e878cdedbaea4ef00577f18b6cfc95c751b2 |
| ku9-live.txt | 22084 | 4db97e560f3bf1386fdee27694710bf8f6100433d8cb7c581a4193ec72f543c7 | 9654e878cdedbaea4ef00577f18b6cfc95c751b2 |
| live.m3u | 42308 | 29f005f9ffb3509075e98b5ce4d32864b402ca4b3ce88317a674fcd04b730519 | 71038d90729e99d7298afa5e3621273427b367eb |
| ku9-family.txt | 21812 | e4050a29bebc17276240cc4e524bb3f5dfb39fb5ec423f4a4ede934f694eef47 | dcdac0a5c0326fc54a83d6d58a4b7ca3ed6bcb5f |
| live-family.txt | 21812 | e4050a29bebc17276240cc4e524bb3f5dfb39fb5ec423f4a4ede934f694eef47 | dcdac0a5c0326fc54a83d6d58a4b7ca3ed6bcb5f |
| family.m3u | 41788 | 61085449e5d2382d9c42034f9c533cb7d07f1a107f563f6108e68f96a61652fe | 94b461113498685dd90e6766ee56c8eed6fe3214 |
| final-publish-report.md | 10709 | cbd00510c95a8e99d4bc80cf113384ba276c97a05c6198b09c844cb5fa8692be | c8eb738d5cf925bb41cddc9c1494debff44cdcd9 |
| coverage-report.md | 2230 | e4ba9f7c20c07fbbdcc767d3672c62c3fb173d64ee92d9ce01d82f5babe4a2e1 | c13ce745c01dc2483ecee73bc053965a2ac677d7 |
| quality-audit-report.md | 4719 | 38cd28f08050d5a5f21f748287713d8c339ef7d0dba0351a9d12d5d36e62fa11 | ff681432e612ea674b11d695e73168804a73c17c |
| publish-guard-report.md | 1555 | 64de0787dcfcc537a564b5a8ba7cdeea56a4800b41d1985038d0d88117c03c3a | 7e5854ed48319ef33858c8f2e821fc38439ba6c1 |
| published-recheck-report.md | 27445 | d6029de66d164b0533e69150a79671b8ac68fbc3e0dfb5575971e6142f2e5f8e | 374e43205fc5b58e896d13536c069388967ed346 |
| source-report.md | 8092 | 862ace2458182577f03c68f76ac2643cc6a5cc1e585f5ae034167180489507f9 | c6dc1fd886026922c588d419de5a5cd0fd933ab0 |
| check-report.md | 8092 | 862ace2458182577f03c68f76ac2643cc6a5cc1e585f5ae034167180489507f9 | c6dc1fd886026922c588d419de5a5cd0fd933ab0 |
| curated-report.md | 1804 | e3084d3f6a0cb8315c7a8376ce4273983c38b0b14a07d7674c6aedb82403d52e | 099be43aaed7589801c1148f1a40a7945346a56f |
| sources_status.csv | 4138 | 4452e1387974f96f9e181954a041a893423dcd1c6c463c9dff1019ad9a2d75ae | 9a22acec77db64ec28ea3b2c9d7fec13586d927d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
