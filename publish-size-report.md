# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 271527
Unique payload blob bytes: 181379
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 61848

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20616 | 8f646e654d272c24044be0bfaf4c9ac1d23ead88c7488997f18692cb58462fe4 | b562d3685b1c0562931e7c6f79c763d1dfd1c02e |
| live.txt | 20616 | 8f646e654d272c24044be0bfaf4c9ac1d23ead88c7488997f18692cb58462fe4 | b562d3685b1c0562931e7c6f79c763d1dfd1c02e |
| live-verified.txt | 20616 | 8f646e654d272c24044be0bfaf4c9ac1d23ead88c7488997f18692cb58462fe4 | b562d3685b1c0562931e7c6f79c763d1dfd1c02e |
| ku9-live.txt | 20616 | 8f646e654d272c24044be0bfaf4c9ac1d23ead88c7488997f18692cb58462fe4 | b562d3685b1c0562931e7c6f79c763d1dfd1c02e |
| live.m3u | 39396 | 3e8af79dbae7f7eeaaa25b6a673cdade4eb3450d55f10f0c0eb6af00bd5ec7a9 | c573f81cce9b24d188dfd3dcc4c5bfee923b2e88 |
| ku9-family.txt | 20193 | b907e16ddcad91d3746614cea1f94b7fa9fd74019234fb5e0bf61522f902664d | 19068aefa1f3ba4682ac286fa20ac82996efa566 |
| live-family.txt | 20193 | b907e16ddcad91d3746614cea1f94b7fa9fd74019234fb5e0bf61522f902664d | 19068aefa1f3ba4682ac286fa20ac82996efa566 |
| family.m3u | 38601 | 12c1a4da4e6156afc8d8a4ed70d4af793e98c5d1a695406c07e84148030a7b35 | 4b252d8bc8d1dfc58a6dd7fa2cac319ed0a7ea2a |
| final-publish-report.md | 10857 | faf9f536cf5c6078bac9f1056dc4f9687397a8db858361b35c03d42534fbcff8 | 90ef57bba606308bf9068b93cfc6579c2d5f6862 |
| coverage-report.md | 2250 | 87a845e5139353158771c6a8ec41e1d86d3c71ab9916c877b7d9e44e10ff1159 | 67348d3991047e82cddd2012bfc7583b02d7a1c9 |
| quality-audit-report.md | 4750 | e30eaec936c33e3b3a6b947521e456e98308af7dff1e08554034351b74ff9a64 | 96c03b26c1b737dc67f2ecf3ff9a6d2c1da5a6bd |
| publish-guard-report.md | 1617 | f9a93389ff2b258dc1550ad635edb7911ac5fe8dfafd397b7aba9617400e8ce4 | a1e6b2d40395a9aafc978902281acd1fc6fa2148 |
| published-recheck-report.md | 29042 | 7c6461664ceee2650626101dcbc0069141ff2473f1524a08b539a6c343f0a977 | 35ae55e02280639b16023ea330d0290355bc6524 |
| source-report.md | 8107 | 2339725d739c0acf75d9eb81903e04e0d97a16668981381a4ff87593af553f1a | 50dfab4f64d50b97eb3bd478b75e216b0783033a |
| check-report.md | 8107 | 2339725d739c0acf75d9eb81903e04e0d97a16668981381a4ff87593af553f1a | 50dfab4f64d50b97eb3bd478b75e216b0783033a |
| curated-report.md | 1806 | 16c32731b8bf264ab23b3a3a58490ff9c58d70d0c1417634869dacd3f82537dd | cef43b8ef6f3d5c0811f275d12afeae0d32e5135 |
| sources_status.csv | 4144 | 7e405d51952aa17899baeaeb1c016f48ba8f15405f9edcdcce4de1561b4096a3 | b417a4d66483fe01e992a24f55a31d9cf44e21e3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
