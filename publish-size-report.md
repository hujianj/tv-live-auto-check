# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 329550
Unique payload blob bytes: 265758
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37420

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18710 | ba6fe385764f9fbcad89ac6a21842472b471b3ce950110536012676e1d5f164c | 72a8dbf8407a7dfcc3056a8003c31b941c40958a |
| live.txt | 18710 | ba6fe385764f9fbcad89ac6a21842472b471b3ce950110536012676e1d5f164c | 72a8dbf8407a7dfcc3056a8003c31b941c40958a |
| live-verified.txt | 18710 | ba6fe385764f9fbcad89ac6a21842472b471b3ce950110536012676e1d5f164c | 72a8dbf8407a7dfcc3056a8003c31b941c40958a |
| ku9-live.txt | 21963 | b16c8d96b2120136aa75965ff2e8e333c3e866e5d7757509a6fb3f6219b4c7b4 | 3cb0a6c833250099683c215dd79628594e479f73 |
| live.m3u | 35743 | fd1271e77ab4a8b51720e4b26a0a1e867ace1d951a96caa447ec2aae6956881f | 9adf7a6ab30d18831ee5eb987ba5d8cc6d64ed11 |
| ku9-family.txt | 18274 | 9368330446022d8a67dbed5e36e1c1d7e9a14cbbc20613c3ef0497884ccc8084 | 438ea92178595b9218dd0ddfe6bc49c5127940a4 |
| live-family.txt | 18274 | 9368330446022d8a67dbed5e36e1c1d7e9a14cbbc20613c3ef0497884ccc8084 | 438ea92178595b9218dd0ddfe6bc49c5127940a4 |
| family.m3u | 34935 | aadf84b0c9671fdd4d1700e65c396bae2aed677d5cc72792eabce794c2446a32 | 5cf3f2cdbd04c2175213f2e1fc69cc1ed0fbd95c |
| final-publish-report.md | 10908 | 70ffa15859490fe370116079e9b7367a71a9dcb3b4fcacf92131e2e02ed4bd9f | c5e2bbd0697152c3bea5694fe12f709679cd60d0 |
| coverage-report.md | 2190 | ca688beb3da6f47f7b6fa6b0835a3ca31cae14e24b2abe5e42fdfbf4e5dcca88 | dfe351433317fbd5f8e014cab11735cf2036134b |
| quality-audit-report.md | 4674 | 768024c96237dc9c7fdbacf4696f202cd1c68b7b4ef54f4bcd09c953efbe16b4 | a8bd70b2956af5291a08194ba2665a9010d8dee8 |
| publish-guard-report.md | 1505 | c69b8baf039f062af010cbebae8a5d6eb18693e8433eb8f4c0d0471a025cd8aa | ba6488a11b97a59508aecf53c47db7b9269657b1 |
| published-recheck-report.md | 29497 | fef82cdc80e5f53ceffeeb49a4f21cfa17bf4b32fb2ff1168f70b36d2ebeb1de | 2d7a1ceb6e206e15d82555a9e62854731daed281 |
| source-report.md | 8098 | fed1617e25eacb79f5c8f78ce7fada0cdf9c77355cc41eccc22451122e2e80c2 | e72a572c64e04817e8cc3c5aeac810b85b32dbaa |
| check-report.md | 8098 | fed1617e25eacb79f5c8f78ce7fada0cdf9c77355cc41eccc22451122e2e80c2 | e72a572c64e04817e8cc3c5aeac810b85b32dbaa |
| curated-report.md | 1833 | 4d5402639c4537d358e3e4f64ae9647201f3ff1dec2d503ed7f7380b149a6eb2 | 1b7ce39f5f268b7fd52df7e98e4741a4685bae50 |
| sources_status.csv | 4151 | 6f6a25e2d938ef489913d3c44e02c90ae4ce7fd08562c55a27a887975af0fe01 | 2b752a071b116ec39b02df8e0770f8004d5de4c7 |
| tv-coverage.m3u | 49405 | 8551568d98bd8a33e0f88e4547bc428699ea3aa23838b9a7d8b8413720eb0f94 | 788016a98659bd94a75a27f0e669beba287472f4 |
| tv-review-report.json | 15221 | ee39b76346b95e4fcb8babd750f312a226f9c84ffdd93ab2e77a814ffc01ebd8 | 588fd349b7e7d5153a4143cc0b61dbd71e8328f6 |
| tv-review-report.md | 8651 | 6af92ae82c950e70c476c0e12c48741d21ceed68cb310ba672bef804bb35ce39 | eac0410632cafcce8537a48b2ca7a43b3e06ebbf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
