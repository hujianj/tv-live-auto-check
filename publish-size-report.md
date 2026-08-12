# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2143016
Unique payload blob bytes: 1542638
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 503820

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 167940 | eb66df31b23e8000033545c598df01fe1f073298045e0d70189c3268a2138f56 | b0a56303cb83b20b2174ea83b2d6bb3dbdf7f306 |
| live.txt | 167940 | eb66df31b23e8000033545c598df01fe1f073298045e0d70189c3268a2138f56 | b0a56303cb83b20b2174ea83b2d6bb3dbdf7f306 |
| live-verified.txt | 167940 | eb66df31b23e8000033545c598df01fe1f073298045e0d70189c3268a2138f56 | b0a56303cb83b20b2174ea83b2d6bb3dbdf7f306 |
| ku9-live.txt | 167940 | eb66df31b23e8000033545c598df01fe1f073298045e0d70189c3268a2138f56 | b0a56303cb83b20b2174ea83b2d6bb3dbdf7f306 |
| live.m3u | 302554 | b4d73ad2e897abeeec4ad932e9acfb0459f30d6c4e88a359b280ef10f248d814 | e682a2096df97b35d52625c9391c903a1ca64509 |
| ku9-family.txt | 89984 | 925b1cefcd0d5a99f053dc21bd9356156868334057034980ff9f8359ebda0aff | c4d2c6005342cb9f5ee32929ee86fa15eef26003 |
| live-family.txt | 89984 | 925b1cefcd0d5a99f053dc21bd9356156868334057034980ff9f8359ebda0aff | c4d2c6005342cb9f5ee32929ee86fa15eef26003 |
| family.m3u | 160924 | f75c8c532f5ac390231111f250f3240e4eebe7e0f81f4b954795946cdc0dd967 | 180f0ef7e5abac4189b1bc9b051e5eb8b9ffef23 |
| stability-history.tsv | 753122 | 1633fcb19790f2fa0bfa2c36b72b651bea64296af495f93df4d0fc220d403b02 | 6a748ebf87eb72d464b49a2491e67813f01d6f95 |
| final-publish-report.md | 11619 | 36f4251341430e82f1e08c93faf9a024cab914cd31e13b35987b421917086b15 | 91f87883f235a0d3ba0e4238907bd7324c019976 |
| stability-report.md | 12349 | 736ee521fa5f2e4fba84b0770b8bfc7f3500397750d3a0fc08de7065019c824b | 1f166b299b215b62f7a1d02cdcbc705c1b58470f |
| coverage-report.md | 1291 | ea82e15823e7643a6cbcbf0193dff304fafe6ff03fb9d1fe0c422c8bc7f3a8f2 | 68476f2f0b256546ee7e7dddd709b3841fdf74dc |
| quality-audit-report.md | 2065 | 85fa3acd485c9ba83345b6b88384944258ebc388340ca67cbbdaf0c95a497ead | e25f5e650bf37f78ccfec10ccd90c20894f507d1 |
| publish-guard-report.md | 1142 | f6e2da6361cb6a4609d9c756702129f4ad7beb1e230a062ed0f4b8380e4557c0 | b93dc5b5fe11ded31efce42c4cb6bfaf8b1b3d30 |
| published-recheck-report.md | 26550 | 7d802a26597a23183e4a4fa094be86c3a9d6475954b91ae66ce39ee1005f04a0 | 361e1a6e2ffc3b5a8186ad0f202dce0ffaac32d3 |
| source-report.md | 6574 | cebe3cbf9a22f33de889198ae390235c130d388e82d72f94ba0897871c06457d | 3227683777b0d66ed3d8911da032dce936642bb1 |
| check-report.md | 6574 | cebe3cbf9a22f33de889198ae390235c130d388e82d72f94ba0897871c06457d | 3227683777b0d66ed3d8911da032dce936642bb1 |
| curated-report.md | 3383 | 2db0ab5eb1ce1d05f2fc20c8063bd915925c2dc5130794bf468b5be3fa6245ee | 16c494d75f103ddaa6749f5c4d9a5855da977dab |
| sources_status.csv | 3141 | 2e1193db0f31790b3d6ba4e6ad04667af6c18f3639e76c67e0a9fd0927ad2032 | 214ac507b4f5330e1ea0236c13f92612fe5f27af |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
