# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 251156
Unique payload blob bytes: 168772
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 56031

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18677 | e5ad30dc87a78ffe5eb8c75ffef46226c88650da118d676f0d8f5cdbd60bba0d | 170e65b09cd11ddb3fefc55e820bbb119ad17156 |
| live.txt | 18677 | e5ad30dc87a78ffe5eb8c75ffef46226c88650da118d676f0d8f5cdbd60bba0d | 170e65b09cd11ddb3fefc55e820bbb119ad17156 |
| live-verified.txt | 18677 | e5ad30dc87a78ffe5eb8c75ffef46226c88650da118d676f0d8f5cdbd60bba0d | 170e65b09cd11ddb3fefc55e820bbb119ad17156 |
| ku9-live.txt | 18677 | e5ad30dc87a78ffe5eb8c75ffef46226c88650da118d676f0d8f5cdbd60bba0d | 170e65b09cd11ddb3fefc55e820bbb119ad17156 |
| live.m3u | 35079 | 82570cf249d8ee0cde4ffb96c6b1c09ef37f46aca2b9a8e18f6da16d185a8a86 | 9d912add11187ac85f571e7599a92a463f43758e |
| ku9-family.txt | 18247 | c3c6f176ca0288ce1f89f8bebed01b3797962098f225aacc2e95bb496f513124 | 4199b68de4ea3ac8175389dd58c17b262a656141 |
| live-family.txt | 18247 | c3c6f176ca0288ce1f89f8bebed01b3797962098f225aacc2e95bb496f513124 | 4199b68de4ea3ac8175389dd58c17b262a656141 |
| family.m3u | 34277 | 89d81f4870fe8279abf917b2b6720ffc7890b75981ab71fd906c5bb8d0c4a231 | 8d2e04fdb8896f85b5abaf6d5a2d1aaa6ce40211 |
| final-publish-report.md | 10717 | f8d1a875e4565d37b43d71b1ba750786c649597e5f56036d7ebaeec739999b5a | ac4b3db6c5ce91a5be01e28eadec969740ddf42c |
| coverage-report.md | 2240 | 878cf4d4dbacf66a7abb94ca3ec9f45b57141f2ce5a0d6641d30d12f1f8afad7 | c3ad8a7309b12a33ad495c07e623b146a932ae5d |
| quality-audit-report.md | 4790 | b8992c94fe05842fee78247578f294409d293886631efd5ad1db98fd25049555 | 91213c5604a4414a71dc515c6d75fc9a0a3e5583 |
| publish-guard-report.md | 1528 | 489ebc30c0c0d960c5be26e065e8226160ed75fe05da0e536bdf6772904aed53 | 3a244f33583be505c4d3bd529b0d578862b3c6ec |
| published-recheck-report.md | 29132 | de78d0f2ae02c37eddc0716f11b9f729617021c3d335dd6b5a93257c4bd2f0ff | d561b9dd898bdd6a3baddc27f44fd7ee81ca5626 |
| source-report.md | 8106 | a3af6fa0b40d7d3145cf5c6cb298dec2e14ac243db0af7c41f8bc479db7aea81 | c97b03e02e4b08ed45f0b6b9b14fb7f29504143e |
| check-report.md | 8106 | a3af6fa0b40d7d3145cf5c6cb298dec2e14ac243db0af7c41f8bc479db7aea81 | c97b03e02e4b08ed45f0b6b9b14fb7f29504143e |
| curated-report.md | 1804 | 28e91b4edca25d87f281a36b439483fd28854c16ed2312e7335fe06a692d94a4 | 5af0855a14afbca8b9e4cf8f3e07fa9617e006a8 |
| sources_status.csv | 4175 | 2ff855900e2da0c4f4ac1927f486962205a85401e63c58561aaf31c21dc8959d | 409b6287fe1cb1526fc570a7093312142ac614de |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
