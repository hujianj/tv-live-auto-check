# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 271055
Unique payload blob bytes: 179601
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 62676

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20892 | dd9ade95528a873c0697c82c271ccf2e6dc9e0e85bd99e578fe9af680758ce0c | 030cb2723f4f1d82fe065f2b60f3548ce0522956 |
| live.txt | 20892 | dd9ade95528a873c0697c82c271ccf2e6dc9e0e85bd99e578fe9af680758ce0c | 030cb2723f4f1d82fe065f2b60f3548ce0522956 |
| live-verified.txt | 20892 | dd9ade95528a873c0697c82c271ccf2e6dc9e0e85bd99e578fe9af680758ce0c | 030cb2723f4f1d82fe065f2b60f3548ce0522956 |
| ku9-live.txt | 20892 | dd9ade95528a873c0697c82c271ccf2e6dc9e0e85bd99e578fe9af680758ce0c | 030cb2723f4f1d82fe065f2b60f3548ce0522956 |
| live.m3u | 40230 | 7e7e4b29b27491b2412eaede2f0063de93dee47a9f240337dd4199a82fd69e5e | 6ffd3eddf8f3283b6c55e22708df8054d295141c |
| ku9-family.txt | 20772 | c5dfddbf59dc4d0eb3a0a0dbfc7e679595ceb3375f7aedae68c2ab8207d025e7 | e82ab21763c17173fb5f859a430481776bbf38e0 |
| live-family.txt | 20772 | c5dfddbf59dc4d0eb3a0a0dbfc7e679595ceb3375f7aedae68c2ab8207d025e7 | e82ab21763c17173fb5f859a430481776bbf38e0 |
| family.m3u | 39986 | 202bd9b0a2fcbb90f64298b3a317f3a5522412b977fb615473bd853c23983065 | 45fc28a5b038d5af9feedef5e2d3a58944f01d60 |
| final-publish-report.md | 10707 | 88ed98c1cdc500576cdc9c25dea098a04d3b89c66b43fdff0ecc33dc071aa442 | a0669765ea8470aa4346819d70a5d3a834a1facb |
| coverage-report.md | 2230 | 824e43249140c869d3320166f33a8469458758a6718d84c9085466944cc4f289 | eabc08cb07f0d3a63075020a591ef1afab72f7b9 |
| quality-audit-report.md | 4730 | 673d138b0f6d7a7ad1297e2c95b4d713899826ae4830a0823b546f3a7bbc95f1 | 14e33d4ec29738976f4ce81154801aca6a1d9ed5 |
| publish-guard-report.md | 1500 | 2c8aed7e1de649ff25c550fa74e670c960500a942feab84fe6a03f135bbb5fd0 | 8f8b944ea14e9ce25edf01fec86c784dca17ea73 |
| published-recheck-report.md | 24727 | 5c6a56fafa5f063ab2b7e9fc77681365ddf6fa6c22fd57ecaa76f85d231c9cd6 | 7dccec326514239f353a6d62130becb5fbcb5033 |
| source-report.md | 8006 | 9fc4690cf66fed8458567c9a642d7db6044ab8681ad8a9d8d46cc32127f9d54d | 25ee5f201040402db9d0230b7472d2f0e0f8092f |
| check-report.md | 8006 | 9fc4690cf66fed8458567c9a642d7db6044ab8681ad8a9d8d46cc32127f9d54d | 25ee5f201040402db9d0230b7472d2f0e0f8092f |
| curated-report.md | 1803 | 6ff3024dc67f8236420b5582c14a96df7f03c54ef86b3ffc37c873ff440fd31c | 7b282cd9ad2c64c0233dd8345ec689b115e55dfd |
| sources_status.csv | 4018 | ce91ae8504cbbd7fb4217ff37873388f27d0b5535aeb0d0ae78968f6b6f50de2 | c5fdb328db8d75a215fe405eae6cc9e0261c78d2 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
