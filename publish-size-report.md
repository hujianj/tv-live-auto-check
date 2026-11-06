# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 334671
Unique payload blob bytes: 271676
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36882

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18441 | f91a447357e9b55ece5ed64b5597689daa3fad6edfe9f19f8d4ef976dad35545 | 3fbbabcf78e2aa737bb177448564ae8a1dab35f4 |
| live.txt | 18441 | f91a447357e9b55ece5ed64b5597689daa3fad6edfe9f19f8d4ef976dad35545 | 3fbbabcf78e2aa737bb177448564ae8a1dab35f4 |
| live-verified.txt | 18441 | f91a447357e9b55ece5ed64b5597689daa3fad6edfe9f19f8d4ef976dad35545 | 3fbbabcf78e2aa737bb177448564ae8a1dab35f4 |
| ku9-live.txt | 22245 | bac6c7c21c5b3d4985e66bc609f9234976713574a04afe729286cc52c5ebb143 | 2b5bf59b33f9e4692899dddbf6918d98fbbf8b97 |
| live.m3u | 35236 | cebe8f54c8b7f9bd9166c77a2740fc951d05ed0050c5b819c9b3a0748a469b67 | c13872a1d4a720d8f2dfad9b4716f07930d5cdb5 |
| ku9-family.txt | 18005 | 7e5239659943b07957714ea6638c641a521faf80c4ec3411218d5c69e5380d83 | 8ce6897439814bccbbeab05521c39526d3ee7e06 |
| live-family.txt | 18005 | 7e5239659943b07957714ea6638c641a521faf80c4ec3411218d5c69e5380d83 | 8ce6897439814bccbbeab05521c39526d3ee7e06 |
| family.m3u | 34428 | 1108fa985e309bd1bee58f128ff3b8e103a9a2a0798d8c9bb4ea39ae99ec0363 | c39a181af41cea2318fa2712b20ce358cd091776 |
| final-publish-report.md | 10909 | bd0a1f1ed903dd189b41fb23f88ab044cd51ee70613e393674c43dd334c2b361 | 1493c49f940c8577febb055da070512119c9e160 |
| coverage-report.md | 2200 | d8f65f48428b2c488748a17b03eeb4f9f5257a9bd6f6ec9716d016f8a5023201 | 937a3bd38680925e84e74ee5d7bf770cd9f10c64 |
| quality-audit-report.md | 4699 | 2fad1f180b1502f31278e44257fee2b39b1ad9da15883783ad2539e979ff552d | 3ca14c34508ad336a6e7a0c6e8c294c240842e4b |
| publish-guard-report.md | 1503 | e3d7bd6fc38170628957aeef797b514a56794daac412aaa4467da27478007f54 | fcf6ce2c8ce30d74abb812d521624b483d6e53f2 |
| published-recheck-report.md | 30633 | 2e5bb4166d26815c582d5a130253d9f291b23046739a0cb2ba050d012fb81aa0 | 481b15e36545e0c9693e91d59193dbf63857f8ab |
| source-report.md | 8108 | ac12b9fdf0b70597617db0a44a164ce4ab76dd1a7b65b51702e90e70bc085b0d | ae6d098af32fe840fcb5f62d935452f120b63615 |
| check-report.md | 8108 | ac12b9fdf0b70597617db0a44a164ce4ab76dd1a7b65b51702e90e70bc085b0d | ae6d098af32fe840fcb5f62d935452f120b63615 |
| curated-report.md | 1833 | ec3bdd3f7cc0acaaff16fb9dd14248b0fe10318af5aed178346bacd3153c66a0 | dbcf23f22fa11535074e397918b26de2f95cf29a |
| sources_status.csv | 4180 | 95d397caa1718a336135100c736e10079b8110a4e78827a6ff64c7a90eeb0126 | 35f5a0a5fd15aa3bbb4e05470386b5418b272f71 |
| tv-coverage.m3u | 49973 | f2665db760571145b7629e065827ade02aaeed64e18e860be177d7dd3a686537 | 54270683728a9eb5a94f53c4f6283c918ab2f4ed |
| tv-review-report.json | 18609 | a1d6fbbc50d988714f433301c8ea95396faaefae73e7078eb9a55108db003195 | 4e65daa6a1f96867b1467f3d307ef8dbadd0b624 |
| tv-review-report.md | 10674 | de0d7a7c9b4d2229863947202c5b88abbc99c9fa024d3f64cde13e7cd7bafd25 | edf45eb318b09606d23b5afee809d98d4c95a1e9 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
