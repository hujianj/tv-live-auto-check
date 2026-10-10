# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 304371
Unique payload blob bytes: 200801
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 71904

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23968 | 811f9dfae101d364ee73208a664a56b02822a50c92feb81fa3449d63101bb94f | 42b6623814ddc84447d4c34797c2b6bff801285d |
| live.txt | 23968 | 811f9dfae101d364ee73208a664a56b02822a50c92feb81fa3449d63101bb94f | 42b6623814ddc84447d4c34797c2b6bff801285d |
| live-verified.txt | 23968 | 811f9dfae101d364ee73208a664a56b02822a50c92feb81fa3449d63101bb94f | 42b6623814ddc84447d4c34797c2b6bff801285d |
| ku9-live.txt | 23968 | 811f9dfae101d364ee73208a664a56b02822a50c92feb81fa3449d63101bb94f | 42b6623814ddc84447d4c34797c2b6bff801285d |
| live.m3u | 45663 | 1f70ff704b40015f9a833bbec2f33448bcf870c3bb7ce7a2f97531d5cf44ea7b | 3ccf315648aba5292315fa9471c8fce76efb7a70 |
| ku9-family.txt | 23545 | 6a166d7fdca499288cef6edaab908081fbad8a1e08fa9b87c6a95f11103d0b79 | 5004ff27647599b470c5b446f3e5c8db45ea8414 |
| live-family.txt | 23545 | 6a166d7fdca499288cef6edaab908081fbad8a1e08fa9b87c6a95f11103d0b79 | 5004ff27647599b470c5b446f3e5c8db45ea8414 |
| family.m3u | 44868 | e81f3d8bcdba1982f9484ecde511d9826804905a3c43fa7f400ff524ab4a8165 | 35229fc303e7b46f000ed5b187ad442c722e0d1a |
| final-publish-report.md | 10816 | 6c362aedaa2d65088403d57da2166c575f8267642349dac506a4cd9ad37a434a | 492182bcfae0c808b6e5fa28069ce18f7f5c637c |
| coverage-report.md | 2240 | 2ebce86cf200ffdbc964aa4c13522aa1da592b841e70c4e00047546306806a50 | 350d1b1ad8d7c1949fba7e8c91cc4e7c3e3fe2fb |
| quality-audit-report.md | 4722 | 4b5acbc0084412ec3041908837f464c5b136636b1528b615f0983d7847bb05fd | beaf25cf35fb4a5d2e27c44f45c9b4b0114eb96d |
| publish-guard-report.md | 1608 | c92404c09636a72fd8eca2788371d2e76d73028b15f6f68dd349fcf064ab8de6 | 699aeefd8ab9235042fb0ac62e5f5204c5f02701 |
| published-recheck-report.md | 29308 | b5524de07938bf361e302797889cb762aeb873193fb89de0ecebb4dc60fbf76b | fd5784a724c7fe049c4b49ed70952278f1ef181a |
| source-report.md | 8121 | 0a581148e3fd476f6f0a82591416b2eb7844fc5f52ce339504a00e1374d42782 | c769d3a84d616a909405f5c5841be48ee6ba4e33 |
| check-report.md | 8121 | 0a581148e3fd476f6f0a82591416b2eb7844fc5f52ce339504a00e1374d42782 | c769d3a84d616a909405f5c5841be48ee6ba4e33 |
| curated-report.md | 1804 | f85b65120c6c3a34df9929866c474c6fca81851b138cb7d649daa56b5640dedd | acf460c188d13ecf8bf481fdd1f16f11702e5691 |
| sources_status.csv | 4138 | 2b6cf0f6709b93881b6e4bda9868d43f031844f4c71afc002da61e24d05d07db | ca3a42ee04a64ef702f01c24983516c4d4fb76f8 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
