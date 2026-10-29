# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 358345
Unique payload blob bytes: 286723
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 42658

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21329 | bba1d3e48d04836791c23979ba5e97a4a48885be13f41846fc94383a7d6fb902 | 5d714282dec1acf64699796e4cc081ea2baa14eb |
| live.txt | 21329 | bba1d3e48d04836791c23979ba5e97a4a48885be13f41846fc94383a7d6fb902 | 5d714282dec1acf64699796e4cc081ea2baa14eb |
| live-verified.txt | 21329 | bba1d3e48d04836791c23979ba5e97a4a48885be13f41846fc94383a7d6fb902 | 5d714282dec1acf64699796e4cc081ea2baa14eb |
| ku9-live.txt | 24068 | 9e1ad88188f0a7d40ccc6b0bdbbfa377627f7c78ea7dca74920aa4522640510e | 339bd441f3b368d7266d4057ca87037a518f8cce |
| live.m3u | 40197 | e49f63f12ff95d45e186a6add510535e5b0bfd1ee4d7652dda5fdba7df12595d | bb632fea2dd8900f8c55b492707e91366518fa74 |
| ku9-family.txt | 20893 | 5d46592ffbb526c20381df37100f255368c9770d360b7276e23d5455e8735cd8 | 75b6f5739546a85dbff6ac971a8243234b9ce6d2 |
| live-family.txt | 20893 | 5d46592ffbb526c20381df37100f255368c9770d360b7276e23d5455e8735cd8 | 75b6f5739546a85dbff6ac971a8243234b9ce6d2 |
| family.m3u | 39389 | 2859a133a315c465dea0fe9c282dae1c0d0a943b343ca3d235ba2ee76da0f78e | 2129e403843a8db4dca5fa9f6653e50eb3fcb52b |
| final-publish-report.md | 11092 | b93499395c1607ee6263565c72d0ac1ed05c242fd37b408f11a5c3e5ed811295 | c9181636ed64d527887a2c9b3980951e157000f3 |
| coverage-report.md | 2205 | 9ed57ab369ebab2045cfb0b5d4fbd4987c6310d1f189953269652377eb65b02c | 795b4f0a25c49aa98737ee88b2c6be464cc5d1da |
| quality-audit-report.md | 4687 | 7d383cdce0b036feff06c0f8e1273c211cb2479e5a7803a4c253f86f759c44e2 | e02ccc2f8225f422b5c81b48ca39ccc4a5680d38 |
| publish-guard-report.md | 1551 | a6943dde1a1d8a5e9c2a94cdeb5f832e2d702fc25f9a15dcb30112e06192ceaa | ad868f9f6c9c06ca88b5611348dfd70abdda2e73 |
| published-recheck-report.md | 30549 | 54d275d3cfd154f264a33c24753bf69dfca89f7ff026a6c69d8ef5b7990a109d | 64a23a04cd6f8e0904e573ac953891f2c81def90 |
| source-report.md | 8071 | 1b5dc52b90127fd45c1b8b6fd6473b1ace007ed3036bffe7f2bc3a885f26454f | 2d202a6f6ffa0be306c319bf9b3f4c39b9a37291 |
| check-report.md | 8071 | 1b5dc52b90127fd45c1b8b6fd6473b1ace007ed3036bffe7f2bc3a885f26454f | 2d202a6f6ffa0be306c319bf9b3f4c39b9a37291 |
| curated-report.md | 1895 | 7ee38c2b249b828833b38fec286a9664d2d999d8db4e1f814b31dc72d02b6338 | 59f5e45c6a3337f1469296588188d334f87147c0 |
| sources_status.csv | 4117 | 2f85ce79db33231f7ad86f376140b88f6411f8b665d317bbb2048924f4fa524b | f26ff2493f426184e0101c2c08bdb50852da97d2 |
| tv-coverage.m3u | 53899 | b80594f562f8bd58a01def1cba67bdaa8b970f25648e2ec1fecf06445a71cb37 | 943fd32394493ea544d8f6aececbe144e069f4fb |
| tv-review-report.json | 14773 | 80684473eeddcebd4944d03ab11722d5a46248a4f6c96be7f28de46009a4163c | c48e5f0a9923c149fa772cd1edb6264c118e2734 |
| tv-review-report.md | 8008 | c6c23e618a97ce46f267a59ba5b847a7e34a37973c0bec700b715d3f3c813b33 | 49f363af0c12e6c1ce1a8d604e82dfe714d0e27a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
