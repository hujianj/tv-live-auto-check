# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 282780
Unique payload blob bytes: 187271
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65910

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21970 | 0700f02ebe98c9446b17ebda47b98bf23ffa01c92fa7e75918e08ae78ebb37dd | 91ebd4a62adaae3a3d1872aaff55b96e621c8ed2 |
| live.txt | 21970 | 0700f02ebe98c9446b17ebda47b98bf23ffa01c92fa7e75918e08ae78ebb37dd | 91ebd4a62adaae3a3d1872aaff55b96e621c8ed2 |
| live-verified.txt | 21970 | 0700f02ebe98c9446b17ebda47b98bf23ffa01c92fa7e75918e08ae78ebb37dd | 91ebd4a62adaae3a3d1872aaff55b96e621c8ed2 |
| ku9-live.txt | 21970 | 0700f02ebe98c9446b17ebda47b98bf23ffa01c92fa7e75918e08ae78ebb37dd | 91ebd4a62adaae3a3d1872aaff55b96e621c8ed2 |
| live.m3u | 42105 | 5861e64d8ccfe71a2dcf2c17614642f51caa1ee64d2d6a940aadb6c424564d8b | d2764bfad7ccf87e4f0645c92f37ef300c381c6c |
| ku9-family.txt | 21667 | 8345e023b9e5875cf922b03c30683ec6f446127b21e8a56d6aa56d9bc72cc394 | 85896e543792a6d5cd93e96d4463d4767a332f8a |
| live-family.txt | 21667 | 8345e023b9e5875cf922b03c30683ec6f446127b21e8a56d6aa56d9bc72cc394 | 85896e543792a6d5cd93e96d4463d4767a332f8a |
| family.m3u | 41554 | dbbbbb13fff86a5fed49ae3cc5907ffad58405b60935523df6fef3747d82b5ce | 8f39bdf7d9f2b7b7f28bf66acfd86cf639f56f42 |
| final-publish-report.md | 10639 | 21329250b7564fb82198272a93b5338158a941c7b039ca43a8da13d444038730 | 24aab3165c953441269db5545973d985dd0d26cc |
| coverage-report.md | 2225 | 7a73010fd3544f71b25402a46b6c56ecff50ba882925647f788c8db9fc413907 | 78481b0a1d24eaf4a0b398404e06719b2d0bd77c |
| quality-audit-report.md | 4726 | a8f7c2f14d1f7139b81f42671c8be2c3881e74efac984bfe77789f30e629c3af | 411ff462da450c87ac4a5d911d9cffec5c7c67b6 |
| publish-guard-report.md | 1562 | 65ac25495c4b0ca442541c8da84696b74fb911332c14ac75054720cbf8360ec1 | a3aaf8db95626bd360056a3d4dbdcecc9ef16388 |
| published-recheck-report.md | 26947 | abb2795d44eccd396deb6f33020c111a13829a20cd05bba2956e9bcf776babd6 | 6f7391503a01854777cd479fedbdd6e22f4c0080 |
| source-report.md | 7932 | 7bb68aaa0d148e2285a8d945cdbfb244b930a03e9263563604e07609fed4e4ad | a5030b7f7c8635e23fe30c41b9b26ef5ea2b655f |
| check-report.md | 7932 | 7bb68aaa0d148e2285a8d945cdbfb244b930a03e9263563604e07609fed4e4ad | a5030b7f7c8635e23fe30c41b9b26ef5ea2b655f |
| curated-report.md | 1806 | 8dc5bdc5c75d23df4094beec2a79ebe2de74e4189eec8ba4c211379cbc8aab37 | 3c18af9ba870cbd7604612b39d03fb80c9990504 |
| sources_status.csv | 4138 | af1076207039283c8fc585b12b81366a4b167f82e40941a8d37d67800b1f1ff4 | 8cdc72f8bfa7ff114dfeb8b1ae6c6cbeab8f5a7a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
