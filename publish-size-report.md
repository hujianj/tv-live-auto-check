# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 358993
Unique payload blob bytes: 286287
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 43322

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21661 | ecb69b028b6c48f59820d1a100442c7aa77181f7045d51db4b49af842c728921 | ccc3ac5b0b542c41e3a76c113f4c31f316250276 |
| live.txt | 21661 | ecb69b028b6c48f59820d1a100442c7aa77181f7045d51db4b49af842c728921 | ccc3ac5b0b542c41e3a76c113f4c31f316250276 |
| live-verified.txt | 21661 | ecb69b028b6c48f59820d1a100442c7aa77181f7045d51db4b49af842c728921 | ccc3ac5b0b542c41e3a76c113f4c31f316250276 |
| ku9-live.txt | 24077 | e77fb1d4eb0928aaa1b01d217afa7c7f2d198311d737363b608e1904ed0c94aa | 9af96b703ae6a1a705719869942d2f334966f3ba |
| live.m3u | 40798 | 13764424bf7e94cef6fd6f1897c3347b034edab56183c26ebf43f0ec4ae284d5 | 93919c3cff93f0bfeb6d3bf518d159bf34ce9569 |
| ku9-family.txt | 21225 | a5afd215d2d10ffbbcf7b3d6a69e252353dff6c58b0aebf1c64fc15d62815aad | fb22730bdcdea268de0afeb5409eeb8341c4c1af |
| live-family.txt | 21225 | a5afd215d2d10ffbbcf7b3d6a69e252353dff6c58b0aebf1c64fc15d62815aad | fb22730bdcdea268de0afeb5409eeb8341c4c1af |
| family.m3u | 39990 | c473cf5f16b2c900c31c3240063700db243d48b7b9690d6b4e3825924f4e13bd | aab1ec3c375f4b1a29018c9c490611474d27d860 |
| final-publish-report.md | 11139 | 371ece2d4797f813f1702738a61889f1cd7b86ac045ab05b1a800e2976d863cc | 3a29e98e70f7099e8e6689cace020685f130489b |
| coverage-report.md | 2195 | 57dfe6fd120e00167df34c9343a0b3d50cc074c5ec22cf644e48b3d05f930c45 | e3d854422ac4820182da99e5107603bc270de519 |
| quality-audit-report.md | 4675 | 5b1524e3e7153bd36c6aa6923395a47e744a1f0e21530a5c0bcbad907d83ace7 | 8a7afea6b64de7ed4f927ed11146f68b45f2f71c |
| publish-guard-report.md | 1552 | 6a70e08ce765f112d6e6b46b554c907e51e6b6e6f88f7ddc47c9e24072a8ef8f | 4bedd105947ba8026d96dc1c07e13735383b1b50 |
| published-recheck-report.md | 31086 | 88c8bbd7c402d467a18a5a4cf5f18c1a79ba389f610070fb8dd20fffc029fd85 | 7bd13358b77781c905eff7f78841d52083f046b2 |
| source-report.md | 8159 | d891588ef6fb5d0bb72710ef6ae32487506a6ad59f2e0b0b6cb1487ab89ce4f4 | 9c88ea02b80c72eb7bfc16def937906c2d2b1c44 |
| check-report.md | 8159 | d891588ef6fb5d0bb72710ef6ae32487506a6ad59f2e0b0b6cb1487ab89ce4f4 | 9c88ea02b80c72eb7bfc16def937906c2d2b1c44 |
| curated-report.md | 1895 | dbb36fa944e5f855708e323cb23ef261d210af23b6840380b6a8f2fb395e51c6 | 29ce5d25faa4acb3e8d764e5fac2ebc780ad1e8e |
| sources_status.csv | 4237 | c5ffcbbe96b52d32c030e1ce642a4f633e2f2fcc556b4a1fd8515ed8277886f4 | 6f6f12cacfb4fab2310cd2951bc6f4bfa28be54b |
| tv-coverage.m3u | 53814 | 73c6909e88b68c621cf9a08960428568a8a9301b9f46d13f1469ce1e2c884b0e | eb2ec9d98e2de3c95f4e64e45f2c73441c98f5a9 |
| tv-review-report.json | 12787 | 2b195872c3aa2cc81a77e5a56ef19d1bde81ff8c4e9f4859f13d8e31c252a36e | 05230aebbae5494edd3db0aae77d759973e6bcf8 |
| tv-review-report.md | 6997 | d961f7d63e7046a2cfc69d69e2d94718624e95bf9c28dc7bc5efed5021f103de | 81abfcf7cb68a30f82282eaf9801769c479ea2d1 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
