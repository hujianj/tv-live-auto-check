# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 338770
Unique payload blob bytes: 271993
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 39374

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19687 | a4385feaeca1a416de34ed538f4d721ee0c47387b4c4f3982da043d4b24ed2b2 | b682455217050bbb0505d5cb6066948e573fb2bb |
| live.txt | 19687 | a4385feaeca1a416de34ed538f4d721ee0c47387b4c4f3982da043d4b24ed2b2 | b682455217050bbb0505d5cb6066948e573fb2bb |
| live-verified.txt | 19687 | a4385feaeca1a416de34ed538f4d721ee0c47387b4c4f3982da043d4b24ed2b2 | b682455217050bbb0505d5cb6066948e573fb2bb |
| ku9-live.txt | 22511 | f23fbb37709df117ccc1e5aa41e77bd367462b262426596d11fecb5a55832909 | ec70902a18d3dc2379701c10287658994b7d03d2 |
| live.m3u | 37947 | 270e3b449c247a199f50771148f5018ea34be3011502a1466700fb06eb63395f | b3843844f3d9b51341ee54d38f48eaeb52806eb3 |
| ku9-family.txt | 19252 | a3e80b82e7a1287f9fc55a5974e6142a99f3c827a6a798224420de1b94528db4 | b4180c9a1bdb67d782c8642fc5cd02297c6e9ffa |
| live-family.txt | 19252 | a3e80b82e7a1287f9fc55a5974e6142a99f3c827a6a798224420de1b94528db4 | b4180c9a1bdb67d782c8642fc5cd02297c6e9ffa |
| family.m3u | 37140 | ad6f292b16433b1221c861cee8885bf7702ff9b86aa2661a71e51678db7ea867 | 0d21e723fb79b50da814dc85d8ec9ef054928b6a |
| final-publish-report.md | 10902 | f171ac58071e9263587b43f1c0aacb9f617053bb64d3d4984ade57a0e15b9d21 | 76ddae9fffa3b533cb6d69d0d63e66b3ff6f789b |
| coverage-report.md | 2185 | 5518ae9ff90247a3aaf927ce53040eef584f808b00d774a8dd93d18e9f5a3032 | ddd24760283ddad5c5918991e99ee1482d81b07a |
| quality-audit-report.md | 4679 | e4582dac9d39879114975e1cf8fdb230b341feda7d1bb9c68b4679eb8857e81f | a5f3db7936eace90523eb8cf305fe57e008858c6 |
| publish-guard-report.md | 1529 | 305acb4fa8ed2c08469ecce8d5166becc2fbd9f8a628bd02c486fd7c41159b09 | d8480025563961104e2164ecbf75ecafc9c82b00 |
| published-recheck-report.md | 30637 | 162c1aedf7a4461a9e92efac681d5929b3536229cbb7b0e03b5cf54e1a6ee5dd | 31a281f4d8fe0e54092f2fc7d5a9cd73c3239baa |
| source-report.md | 8151 | 651891ac52e907596d4d4f345b9678899001f9f55e7c2627ab852c174211023b | 6c5ab5bdd66e41d041b1c8772f924eae1b8cf237 |
| check-report.md | 8151 | 651891ac52e907596d4d4f345b9678899001f9f55e7c2627ab852c174211023b | 6c5ab5bdd66e41d041b1c8772f924eae1b8cf237 |
| curated-report.md | 1834 | 3d058de054adcc3609c793915405095a6bf115bdd3d1b2a444dce7959e162532 | ee42e66a595c8916eaac7c48b741c9459767ec19 |
| sources_status.csv | 4181 | fef964e2c46258a78cd63d704710a31cfc759d9de7217af0b0adab7fe425f1e2 | 2c62feec11a5d44fbca213b31c739ad043b33aa0 |
| tv-coverage.m3u | 51112 | 0db0b2be25b018a42bf8870e0292541e082883eb51653e77cf83fac32f1dc79a | 930f3fe5bd78aae2e8d9401ceed9aafa7dc595f0 |
| tv-review-report.json | 12823 | 727be85a2f5456a052746e2ebe8c0be842d59dad6a3e390e72968c5c1881663c | cdbfeb294bf3760d2ebb52092bc7a25aa75f6155 |
| tv-review-report.md | 7423 | 1150e24075fd9f7790fc2b03412c0ca8b517c9fcb49882505d7d0d293034207d | 946af6f3d7bf0db9c2b200ee712481f3b2f1aaac |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
