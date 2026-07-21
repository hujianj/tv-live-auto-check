# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2478815
Unique payload blob bytes: 1710405
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 663375

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 221125 | 87a4fceff43ea4d8e6bc538b7c46ab7271b918d4a8a934cf0908c7ee1db4526d | 4c170e145ff919cb2dad82f6aa5354e168c69c24 |
| live.txt | 221125 | 87a4fceff43ea4d8e6bc538b7c46ab7271b918d4a8a934cf0908c7ee1db4526d | 4c170e145ff919cb2dad82f6aa5354e168c69c24 |
| live-verified.txt | 221125 | 87a4fceff43ea4d8e6bc538b7c46ab7271b918d4a8a934cf0908c7ee1db4526d | 4c170e145ff919cb2dad82f6aa5354e168c69c24 |
| ku9-live.txt | 221125 | 87a4fceff43ea4d8e6bc538b7c46ab7271b918d4a8a934cf0908c7ee1db4526d | 4c170e145ff919cb2dad82f6aa5354e168c69c24 |
| live.m3u | 394505 | 36e39a197f6a3ccc9b1cb470754824e8b53b5e346bb15c7485cef0177e95c36f | 07f9f275c0754abd4d23a597fcc404f5ac9781e1 |
| ku9-family.txt | 99183 | a58ea5e49f6ff83de7367760fd840fce0fb68f052037fc98cda63f91946e6c76 | ead70eed43c3f3642858d62b25bbd7c29e238cc8 |
| live-family.txt | 99183 | a58ea5e49f6ff83de7367760fd840fce0fb68f052037fc98cda63f91946e6c76 | ead70eed43c3f3642858d62b25bbd7c29e238cc8 |
| family.m3u | 177727 | 144445f45bf3a8f46ad08c1760a86d4f6266732e525a6b65e7ef0370c4ee695c | d4e24f264e09684a1ae66f8d0fb77a32d7902f0f |
| stability-history.tsv | 751502 | 9ca0b17a1f994950438d416dae5851f3579705730214cf04a991152cf3290392 | 602bf19d96dca4e95323db38dea5da12b6a2ecc1 |
| final-publish-report.md | 12338 | 5daf0c1c83ab54ce7276bdf24e37f40f1d0babe88c67b20b7b5d7ae8423cfef6 | 5a1cca080ef2cc1106fa1f48421775b5770b601e |
| stability-report.md | 10522 | 37f239f077d21ccefec1d160b2d5307d9f68feda49037462c0a06f52c496eea2 | 78fd20ec6eb2da8ef1159e9dd9b326f4c0af38bb |
| coverage-report.md | 1369 | aff7eec185843d8824aaa203e437aacfd8215137b0ba2a6e575a5398d5e34b1b | 0c6b46fe7586f805bb70b82c53f3c5e91800e8ce |
| quality-audit-report.md | 1435 | 0aa659bf1d2b074ee9f938970cc46d66e730a8c7be5dfe716ccb5f1a60ded481 | 9b424f84101599fdca2ef15549079cfd9534dca2 |
| publish-guard-report.md | 787 | e8b531208e7e1d4d06284c0c5bbaedbc0519cf065e42299a8a495564bbcae89c | f7c16b11d64c8f8f4e68bdde898717db834d050c |
| published-recheck-report.md | 27908 | cd1a75c82076f797502993d67e41234681b183ad6b2946f0e6399a117fbe7b08 | f11898a1ae192fb9f2097bc4796e38117560ab2b |
| source-report.md | 5852 | 004f121ba386daf101c349a8081f4a46e7c3596f24e15701f4f591fcb4d74c2a | 7618c176119e161c47fee92dea57b4c9d233c336 |
| check-report.md | 5852 | 004f121ba386daf101c349a8081f4a46e7c3596f24e15701f4f591fcb4d74c2a | 7618c176119e161c47fee92dea57b4c9d233c336 |
| curated-report.md | 3550 | f5f465ebbeb8a52033786f13524852749fea2945cafce3e3f9f54efd8cce8e6a | 9099bca2784b7ede30dedc31fd1f8c648e139f6a |
| sources_status.csv | 2602 | 435b9e07c126c04bda47d6ad5ecbe3af87d2d029a3c31c258833287b8bdca999 | ef49417cb2c27a192b2b696e5437ede9f488d01f |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
