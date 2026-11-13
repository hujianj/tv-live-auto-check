# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 327018
Unique payload blob bytes: 265287
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36008

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18004 | 0d1bee785dc3231cc9d93b488309715e752a4284ec5d8c84524144ac0507f5c2 | 86b02f00edb7a72b68c14657b3b52ac64136f4a8 |
| live.txt | 18004 | 0d1bee785dc3231cc9d93b488309715e752a4284ec5d8c84524144ac0507f5c2 | 86b02f00edb7a72b68c14657b3b52ac64136f4a8 |
| live-verified.txt | 18004 | 0d1bee785dc3231cc9d93b488309715e752a4284ec5d8c84524144ac0507f5c2 | 86b02f00edb7a72b68c14657b3b52ac64136f4a8 |
| ku9-live.txt | 21685 | 299fa7418bd064bdb899bbe19b087107a2a96414f663e8c6210d68ffa9b3200c | 02a428b535be758e175b7b4d6e4a7effb369e5a7 |
| live.m3u | 34668 | 1ee68a18ab9689224926175d84439141148ed54ec1bf26da77ddcc36ab32167b | 8720788754b15da91662e750f4cafd53e6e1c0b5 |
| ku9-family.txt | 17568 | 5f99961a991e00f7ab3dd8dd44f5ccefee13c4d63d6a12e3fe9d7b267fce7f19 | 3a65a37a50d2db6b4aee2557abf0fbc7ef466ebe |
| live-family.txt | 17568 | 5f99961a991e00f7ab3dd8dd44f5ccefee13c4d63d6a12e3fe9d7b267fce7f19 | 3a65a37a50d2db6b4aee2557abf0fbc7ef466ebe |
| family.m3u | 33860 | 3a191b0d3ca154491e27c322227ec804e84916905484b33c49f61b1043ff64c2 | 4d78b251ea0bb207d23007bd83f218d8da7b9189 |
| final-publish-report.md | 10871 | cac8911c5308bdfa243677e23e2387c46ac09c72f7f602292d31c053a412dd86 | ef17b56eafda810e64303a26c3abbb0fce241838 |
| coverage-report.md | 2200 | e7399567705c085a9d2d5223861b80051ae910918b333c41de6959a393f5a9d6 | b9a536938ddb8f14e1021555b742348e2fa62fd1 |
| quality-audit-report.md | 4675 | ee3d461dc1ade6e00d259f35e89a8137997574cc84fe8e26d1047be6b4984ef9 | 2126383a1f4d6872f37f5243290693a370e6a733 |
| publish-guard-report.md | 1531 | 1bf1d85b123205a4164fdfec026cc86e18258f36d309cf1b366a86f5b622622e | 9253d8618fd738dd3fca729dfbdb0daec67e953d |
| published-recheck-report.md | 29077 | cfe1bf51b95714d81602d5622dfc54d85b7a195711a6a3aaf64efa0b15bef7b0 | 18180efd1ac6b185bf4e43e81dccb3f92fe06e94 |
| source-report.md | 8155 | 5c837379c57b91ab644f5ba7b357a9eb89861f0d370548b72eed7c778698ce1e | 457cebac873f7b09869add60e64cc79197f4f3e7 |
| check-report.md | 8155 | 5c837379c57b91ab644f5ba7b357a9eb89861f0d370548b72eed7c778698ce1e | 457cebac873f7b09869add60e64cc79197f4f3e7 |
| curated-report.md | 1833 | 83994c888f8129c7c1cf5b46c98de6d15f8a0e9b1d707f79a0a13d856b01b811 | f36a8bf7bb798430d711214e73d2e86b0b2dedc9 |
| sources_status.csv | 4241 | 006cf6bb83cfcd86d8fa465564cc5c14142895d63aaa104c8d0870fde35465bb | 765fea398ba226a99c9915f74c887d9804ca0258 |
| tv-coverage.m3u | 49090 | 890ccc0fd6a4f3417238f1b07e3cffacb97d42f57ad517e99151c242e3e9ba41 | e4b54474f77c3ffcb831f90c3ae46d6ec344f07a |
| tv-review-report.json | 17687 | f516e24c2707c8279719897bac75d256ba2540127c8d597f383b592b634a008f | 631ace19b79868e357c90395cf9cf9a9b09e2305 |
| tv-review-report.md | 10142 | bef7a9467a7c6b4083a6538baa2bb8992e706b189cd3a06afbf932fe2eb3a1b3 | d8cdc8bf1cdd5d5f12a4f12026fc66622dc7c5a6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
