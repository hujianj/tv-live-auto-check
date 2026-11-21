# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 325109
Unique payload blob bytes: 261496
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37224

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18612 | d9fcc1082d590240338fb3dfee11ba06792a1cb265960c2b41a7acde52ed4fc9 | 0fba758a2a6daf1af0535eb16fa10c1b38b011aa |
| live.txt | 18612 | d9fcc1082d590240338fb3dfee11ba06792a1cb265960c2b41a7acde52ed4fc9 | 0fba758a2a6daf1af0535eb16fa10c1b38b011aa |
| live-verified.txt | 18612 | d9fcc1082d590240338fb3dfee11ba06792a1cb265960c2b41a7acde52ed4fc9 | 0fba758a2a6daf1af0535eb16fa10c1b38b011aa |
| ku9-live.txt | 21980 | fa00a2b27c6d2aaf3fac50ab21f05775722111ff7935dd32fffc8d482e8e7be3 | 982efff54f657ac361a20ab64b9d424c656d4401 |
| live.m3u | 35946 | 58defcb60306424ee33500568457bea8403819f0902d727a7fc12664e1654f3e | 1c63da255676332be43add6634362e13e100a544 |
| ku9-family.txt | 18258 | e124c585aa16736b409bc608145dd572b7af667fcca9857d317445012368b260 | 30f6ac36f70cb4eb7d5f964454ae0992dd19eaf8 |
| live-family.txt | 18258 | e124c585aa16736b409bc608145dd572b7af667fcca9857d317445012368b260 | 30f6ac36f70cb4eb7d5f964454ae0992dd19eaf8 |
| family.m3u | 35282 | 1dd5440523f58ac25b4ea1f4a3efe563be84b81699e308c21150c812ec01ee66 | 1bbb419fbc64dd311e26fffedeb009df73d3a4bc |
| final-publish-report.md | 10858 | 47fe2daeab086ba13a4497f517b8a91eb03b86eedda0e32e5a4f52b1c3780136 | 429c2d4d9d51c07db3b9f704e9aee97a6365fd57 |
| coverage-report.md | 2200 | 6facd78237384ed79c57434cfaaf96549bc8e16bc876dbf1826a07a45b332685 | 49bc21fc4e1c9310e436fe992c0206fdb96ee287 |
| quality-audit-report.md | 4688 | 70ac12931a4a5282f1df3416c62cbfaf4da89873e2cacf287f8422a33406ee56 | cc0b955c5d667c8e412271e862fc0c3dcde951fd |
| publish-guard-report.md | 1531 | 0fb85046e7c280c40561625b7c6a97d4a640b002ffe65bdd2236aa31e230209f | 434fefd269ba6a7fa4f34cd2dc7e64f9f1939d35 |
| published-recheck-report.md | 23888 | 3bd4df2c0cafc37fc53bc4bb90158896551dc14b8cbc317bec43610ab81d49f1 | 12b6953a834b677f4f6d46d7d333e7f95f504da4 |
| source-report.md | 8131 | 62c270259e5f9517ca908975aa41e37440f13d27987b724d70a4d36b2711741d | 59143acb626aaf1237ea4634d6aeffb51ebc81d5 |
| check-report.md | 8131 | 62c270259e5f9517ca908975aa41e37440f13d27987b724d70a4d36b2711741d | 59143acb626aaf1237ea4634d6aeffb51ebc81d5 |
| curated-report.md | 1834 | f351210c1c623a8d2b43802995b02e16fb93d3833a0a7db7eba5bc3881829929 | 4ca47d27375ad8cb10887406ca5f13e7e1e78469 |
| sources_status.csv | 4181 | 0aa5734ea64d5e94b454084cf2cfe059d719ad7820f1d4954ec10118b15d1dc4 | 01fe0c39517e5be17ebfa9ade2634331e14f58d6 |
| tv-coverage.m3u | 49835 | 53bbce7c192ad5023535a2e6e67cbeb64e383a4bf331bb5f02a4432e7ae4b612 | 9e6ea4dd52537e22b01bfc277875c5a83f03be5b |
| tv-review-report.json | 15421 | 8a8b3487963b18ee5228df542f63e7dccf0b09b7b744bcfed6ed8ecd81029974 | 4baf35421dacc9f52d7d60449edbf17028a153cc |
| tv-review-report.md | 8851 | 4ff0d848b0cff9b55b7933d321472867f2d87e0c2d60bf372a691c9f8636277c | 0987a3b01a5715c515b1a30d84e345cfcdbe17ef |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
