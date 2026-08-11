# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2137891
Unique payload blob bytes: 1547309
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 496779

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 165593 | 760916c94c798d7fb4e273f1f566f5a78713724b4e396f1ae5ebc9daa4a7d81f | 9023d4f33cc86789885094b9179e7dca54395b4f |
| live.txt | 165593 | 760916c94c798d7fb4e273f1f566f5a78713724b4e396f1ae5ebc9daa4a7d81f | 9023d4f33cc86789885094b9179e7dca54395b4f |
| live-verified.txt | 165593 | 760916c94c798d7fb4e273f1f566f5a78713724b4e396f1ae5ebc9daa4a7d81f | 9023d4f33cc86789885094b9179e7dca54395b4f |
| ku9-live.txt | 165593 | 760916c94c798d7fb4e273f1f566f5a78713724b4e396f1ae5ebc9daa4a7d81f | 9023d4f33cc86789885094b9179e7dca54395b4f |
| live.m3u | 298078 | f6d3e76ea5a802391361398b443ca09e8f3f20049e546346eda5909c7b5b6d9f | 25eb454df95adcd4cc8635318d423ec737579f95 |
| ku9-family.txt | 86878 | 9df4519969c4fc316b4b020d766672fbe65bb01e9544ad86f948e6dc7e270682 | b2156adcb58f37b8f8e6d76a7b7edef06c6f6d5c |
| live-family.txt | 86878 | 9df4519969c4fc316b4b020d766672fbe65bb01e9544ad86f948e6dc7e270682 | b2156adcb58f37b8f8e6d76a7b7edef06c6f6d5c |
| family.m3u | 154834 | a76151560d00766f7efc5133b201e8ccf90edfe5b1ee401f45dc751ecb374c90 | c4b6e066ccf23ed437c10be1018738c9b51190aa |
| stability-history.tsv | 772995 | a63ca6822eb970ab66d323e76a4e3e113908b60a940d9f89111d9de7dcbb3981 | 9406b253720ff254dfcc70db7912f2332218ebf4 |
| final-publish-report.md | 11575 | 41e7ba155c94f081131e29e2c2774648085da09637c82a9d0a0380f3d2149562 | 32ebdae3dbff4b9476d4a1e994c07d95882e0dc8 |
| stability-report.md | 11391 | f3fd0f28668f1156d581cf44025dd90ca0c79ad52bec37d5b407873574a40b7b | b6926f23c73b370fa7408250afe05eef73c08b16 |
| coverage-report.md | 1291 | e6d16cb2e91a23b37f87a667fb8bfa9b144a094ede1956ddaf7631ea0be8205f | 907ba36c30a4c52632ae3a2ded822761a38ffa2e |
| quality-audit-report.md | 2065 | 8942a6d6a59c344e8bff4e115e6e44683c982a4e13d7ffe733dc45a136fa4fdf | 5ff098731a081ecd3d552dc5f8784aae30ddbdc2 |
| publish-guard-report.md | 1332 | 2837cc374ec9595fb0c6c6982da74eab432055ce6837b8cbb0136c1bcf6afb5f | bfd5b458443d1854e7340ebb129b0c1fefa3c005 |
| published-recheck-report.md | 27274 | e909d9f62b229d8615833743eddd60078f971cc4a9d97b3d104dad52a087de52 | 7ee1acbc7c7e239132ceec65326a6325c43d2a03 |
| source-report.md | 6925 | 62af2b5479b9a8144ceb0363631739a198fc0af4dd5f6c2e0a354c8504429c95 | 1de5bda8259b0b762a38d8140229255f20308989 |
| check-report.md | 6925 | 62af2b5479b9a8144ceb0363631739a198fc0af4dd5f6c2e0a354c8504429c95 | 1de5bda8259b0b762a38d8140229255f20308989 |
| curated-report.md | 3356 | 069c1fc72bdcca19d7a66674e7ad878845bdac3fec0e7e8eb028ac4033e660f0 | 0ada4644bab8adebfc1f9361b5b226127202bf9b |
| sources_status.csv | 3722 | 4ae1ba29db3c25c63597c6886bc434a9d43532edc8046e362dce5152d7752944 | 0db68421dd2c97c249ed0461fecf15c68611fe2c |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
