# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2408892
Unique payload blob bytes: 1681096
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 624258

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 208086 | 78c93e1dc25f2ed7cb423692f7448a07682d7503e26f6c14e8106f6dca8241d4 | c679e18b1d054b6797039cbafa0529ba18720cf0 |
| live.txt | 208086 | 78c93e1dc25f2ed7cb423692f7448a07682d7503e26f6c14e8106f6dca8241d4 | c679e18b1d054b6797039cbafa0529ba18720cf0 |
| live-verified.txt | 208086 | 78c93e1dc25f2ed7cb423692f7448a07682d7503e26f6c14e8106f6dca8241d4 | c679e18b1d054b6797039cbafa0529ba18720cf0 |
| ku9-live.txt | 208086 | 78c93e1dc25f2ed7cb423692f7448a07682d7503e26f6c14e8106f6dca8241d4 | c679e18b1d054b6797039cbafa0529ba18720cf0 |
| live.m3u | 375007 | 94c1ed4afca2d02c677f74e6a909720685dd50c8f9b9405a768edb51af0b9cbb | 364af4fc38d5224bc39b72fd6a1c5416007f5ac2 |
| ku9-family.txt | 97665 | 6c601604eed66bbe4c584fda78176ed61e4376a34593ce9eab9d0b40b2078f90 | 8f8b15cff4be96275b02dddfc273e7b93e3ff401 |
| live-family.txt | 97665 | 6c601604eed66bbe4c584fda78176ed61e4376a34593ce9eab9d0b40b2078f90 | 8f8b15cff4be96275b02dddfc273e7b93e3ff401 |
| family.m3u | 177497 | b56faace716b5110527c25ca4ca4cdd0a527bd959ee37274a55ca310534dd6f7 | 1eb49e3000227a3fb132d2f15f003f4e85fde120 |
| stability-history.tsv | 753781 | 4a997c4ccd0e2c403a881dd1cc17e586bc05fb7ce4ec858390f04c627fcb27e6 | 6e090e993d96b4a65d0d1574ddef69c1e2a98fd9 |
| final-publish-report.md | 11552 | 20e351d79c482e6bb0c0bb9d1a0e6c78c1e9fc01a3781b83b8c95af633342c56 | 7c288b517dfe0bcd92887bc4176e83e72ac94cb9 |
| stability-report.md | 12132 | b386f73265144bd017c8681a35c19cfaeb504257490ac2dc5422a1895779f106 | fd37091d8ab57b60248194c228f1465f6a40e802 |
| coverage-report.md | 1310 | 6e1cd1045a07d630b8f216dec42a84e86647e12b8cc7797163c52a25b5f0ef6f | d5a9bf508323132b65bf95ff22eac7bc1f311417 |
| quality-audit-report.md | 1435 | ce16f93ef6ca78f4b32f24422abcd94f0ed97290ea6d923d88d92ae20d352eb4 | 4743fc5861c16fce295a82840a56b05f6c7acfe7 |
| publish-guard-report.md | 871 | 8dd2ef3080064b322aa1ce8f36c8422b331f03889fb1c4b62dc7d20679b8605e | 4d14cf17917f2a1515947ddbbcd9b80c6bdbc225 |
| published-recheck-report.md | 29719 | a4cece22c6e010e5c112f0c50d855f4f17d142bd60b6dabfe660b8f78e7f7cdb | f79102c0ac282bfadb49b856e88b083581a8144f |
| source-report.md | 5873 | 3cda6318712e0f8b96b7e75f64e9cbb081c1bfd80e570fe312c58e4e7eab888d | 74e4544e8ee1e90b97b3880bd6a609dbe1628cbe |
| check-report.md | 5873 | 3cda6318712e0f8b96b7e75f64e9cbb081c1bfd80e570fe312c58e4e7eab888d | 74e4544e8ee1e90b97b3880bd6a609dbe1628cbe |
| curated-report.md | 3513 | 4de867275b0a32e6c8888eb66ca235219a7d3bd91bca842fd167cc661a98bf16 | d40aad5219ebfd8adad7e85bd2278825be5bafcb |
| sources_status.csv | 2655 | e88a8fa66d194b22c43771831b9254495adfa180e20f5b865729ddd0af46a271 | c2690e5c10358e341755cfa51268abad9b64ddcd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
