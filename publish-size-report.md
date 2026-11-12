# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 347857
Unique payload blob bytes: 281031
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 39342

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19671 | 9b2461481f1afb32048f14493c5f74ce8e5cd94a52e2d62d6ef1b143a4be5c52 | 9578cfe325354671516d189ddff497b4605a5261 |
| live.txt | 19671 | 9b2461481f1afb32048f14493c5f74ce8e5cd94a52e2d62d6ef1b143a4be5c52 | 9578cfe325354671516d189ddff497b4605a5261 |
| live-verified.txt | 19671 | 9b2461481f1afb32048f14493c5f74ce8e5cd94a52e2d62d6ef1b143a4be5c52 | 9578cfe325354671516d189ddff497b4605a5261 |
| ku9-live.txt | 23352 | e0aa384c7f8f412c52e2e67f0a8d36bdee51824c97d2f7df5ba0a4560e7492fd | d45194f945adb0ce2631d08380de15624568b610 |
| live.m3u | 37730 | 2873c454df54cf34cf2713fe6da5a2e6dc412edf136a442bcba9e9a4876a70d5 | bcd091f2c8ef15ee61817ed2397bb6d86c999242 |
| ku9-family.txt | 19310 | 9fc982381d852108bc55c4e4433024bb53ef74036f93e162c87ead8d74f7c8d4 | 26e087619c89b889714a3a4f6dd9b12559421fad |
| live-family.txt | 19310 | 9fc982381d852108bc55c4e4433024bb53ef74036f93e162c87ead8d74f7c8d4 | 26e087619c89b889714a3a4f6dd9b12559421fad |
| family.m3u | 37059 | 5cdfd4440be66a46b2e4d163cbd2e17a5da1bd906ce3b4ea744acb636ef3765d | a4d65a168ff364c6a2fffad0c983c35e42ac1e60 |
| final-publish-report.md | 10887 | 53d9639bab4aa13e60d568a8b92f1bc8016ea5ef7859b351e5faa37bbf977987 | 1e8b04f53f5f80d2555fad999b93192f6cb4c426 |
| coverage-report.md | 2200 | e7399567705c085a9d2d5223861b80051ae910918b333c41de6959a393f5a9d6 | b9a536938ddb8f14e1021555b742348e2fa62fd1 |
| quality-audit-report.md | 4677 | 7afe71528ce316d69d0c04d2958e13f9473a3e327b83671900647574bd3ddfec | 8d0472d06bf9f8a80f605c00dd7dc314bf540cf6 |
| publish-guard-report.md | 1531 | df88e65052ca99fcb06b427dc2ef245b8408513854fe2d370cad96c9c2a151d6 | 4405dfe7f02f8f01214153ae874bbfd0c5dcbcad |
| published-recheck-report.md | 30209 | 3ec10eb1195949417dc5d2d42e073ba45b42b8cf798091f966618b9137cc7c45 | a50a3d99c5413663b8a7da3544e61116ef862b8b |
| source-report.md | 8174 | 0b5674180fe9fd252531cdc4bb6e6aaefd93a9dd07f2caabccb1bc80b19f7fe6 | db6c78500951a0b6ac5ae4ee66dcfce68f912e6f |
| check-report.md | 8174 | 0b5674180fe9fd252531cdc4bb6e6aaefd93a9dd07f2caabccb1bc80b19f7fe6 | db6c78500951a0b6ac5ae4ee66dcfce68f912e6f |
| curated-report.md | 1833 | c53da950a41b46c301839db67da630866e1087d9fca3e6ba4949a510a302440b | 9123ba9ce5cc4b5e8f0655eff52fa7eea034c69c |
| sources_status.csv | 4241 | 43e64fd57ea88021c6d7b6b984c91c5a66008736fd661438e54c8c31c7e99c07 | d459f8b48636373cffa2cceb255e8173dac953b7 |
| tv-coverage.m3u | 52698 | 6b1d1c4b532d535fd6f8aea9d58adc8d6c11d39c5bc1372886c8f0f5b09e30ca | 32bec275e526983d793919704f97b31ce713fb71 |
| tv-review-report.json | 17502 | 5f3bf381a2b04089ad5956a526edea1d6eab56246b960b66de6a1f2687a9e727 | 0383da056f890497b32abf7e129532b1052e5586 |
| tv-review-report.md | 9957 | 314b82a73dfb02af43f2a84255bb4b8807a4d07708e8f5509ddfcfc37d261168 | 5ce92b96d97b36ad37fa49822c1e56d5bf091600 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
