# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 256771
Unique payload blob bytes: 170975
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 58395

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19465 | 16cf02b6d59e86efb1de11cabf3c6c5242a428ab9c7e9a43b5d5bff664b96eff | 77463e8b300723027fe0488b7e04b399c406aeaf |
| live.txt | 19465 | 16cf02b6d59e86efb1de11cabf3c6c5242a428ab9c7e9a43b5d5bff664b96eff | 77463e8b300723027fe0488b7e04b399c406aeaf |
| live-verified.txt | 19465 | 16cf02b6d59e86efb1de11cabf3c6c5242a428ab9c7e9a43b5d5bff664b96eff | 77463e8b300723027fe0488b7e04b399c406aeaf |
| ku9-live.txt | 19465 | 16cf02b6d59e86efb1de11cabf3c6c5242a428ab9c7e9a43b5d5bff664b96eff | 77463e8b300723027fe0488b7e04b399c406aeaf |
| live.m3u | 37393 | 73fb22d4c32958dd065e571fd100f89582175edf6ef8f2b6020b1a016651a217 | ee5bb4d4b57c1b6f23942d5d20e7f454cd1f48ee |
| ku9-family.txt | 19352 | b929646e7e4c1001296b855bf4d2a274f9da42295ce35fd2382f8e800d6f6cfa | d8aba32ff1b0ae6843805c45823e61fef6370b81 |
| live-family.txt | 19352 | b929646e7e4c1001296b855bf4d2a274f9da42295ce35fd2382f8e800d6f6cfa | d8aba32ff1b0ae6843805c45823e61fef6370b81 |
| family.m3u | 37156 | 4e01ffe5fa9eb45c8bbe5b5dbb36f51e9da507c5594cb0992c331b6f68eebb8d | 57299c952b86e6125b6c6d2d19a695c7b688d6f7 |
| final-publish-report.md | 10871 | 4d428c468a6d1fadbfdaee7140d41db5a01af29c0e711bfd01ac61de92640bee | a323d990314a0b3668222093e6563eb98df4701b |
| coverage-report.md | 2250 | 87a845e5139353158771c6a8ec41e1d86d3c71ab9916c877b7d9e44e10ff1159 | 67348d3991047e82cddd2012bfc7583b02d7a1c9 |
| quality-audit-report.md | 4748 | fb582d43b6cecd132f995017c7965b592baba4f1f5bb3c13c7e6c1effd020e2b | df487f9e58e6523549494baadfe6fddefcc19f57 |
| publish-guard-report.md | 1588 | 075e436627bd4219c793edea7cb9cca725274ff533bc0d3dc3689dc5218ff7af | 416ab01056fe4fed13ab4a1483e27200fa6ec7be |
| published-recheck-report.md | 24244 | f3d11c9b346b8cdf378cd6f7ffde44d4098ad5d473b4c65c40d4e5578c6474f6 | 486c82eb070ae46d92cf2744e3b74061efba68ad |
| source-report.md | 8049 | 89961991735549e61330e68e927855f758ad4e4961dcc3638c53857693f271c7 | 14641e7dff59cc26a104f8229d2c1098b00140ab |
| check-report.md | 8049 | 89961991735549e61330e68e927855f758ad4e4961dcc3638c53857693f271c7 | 14641e7dff59cc26a104f8229d2c1098b00140ab |
| curated-report.md | 1806 | dcb735d11f431ed99d322380b691522e8040b6ac332c76c09b52d6a433cd7af3 | 534b8dfdf61238d61c733f0d08e291da4367b221 |
| sources_status.csv | 4053 | ade69364f092138f7ac9cd6ba10a47ab28fda90d5d6fdbeb56ced3d6c9f1115f | a3a697fd548c333053620a6feb824bcff1a5087a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
