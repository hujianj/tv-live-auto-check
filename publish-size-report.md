# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 284367
Unique payload blob bytes: 187651
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 66762

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22254 | e0d445668aef94b3fbfced88c38758146972a96f70e8eebf0d074495ce27bb83 | 753d9749e63c6b785a6ba13c38de7b6230aaf377 |
| live.txt | 22254 | e0d445668aef94b3fbfced88c38758146972a96f70e8eebf0d074495ce27bb83 | 753d9749e63c6b785a6ba13c38de7b6230aaf377 |
| live-verified.txt | 22254 | e0d445668aef94b3fbfced88c38758146972a96f70e8eebf0d074495ce27bb83 | 753d9749e63c6b785a6ba13c38de7b6230aaf377 |
| ku9-live.txt | 22254 | e0d445668aef94b3fbfced88c38758146972a96f70e8eebf0d074495ce27bb83 | 753d9749e63c6b785a6ba13c38de7b6230aaf377 |
| live.m3u | 42662 | 9adbd1412115ab2220224cb1c0598c6b650d04e864f56e25ff59baed586a812e | 815af1b4e4f2a0dc83e68a2fc411a2e3b2076e02 |
| ku9-family.txt | 21906 | 3ed76b9c209b82ffcf72f1a1ae89f5c96ff794ccf317454250b4b4d2a9f431cf | ea68e6d504213c46af7b28704f37b9258fc560ab |
| live-family.txt | 21906 | 3ed76b9c209b82ffcf72f1a1ae89f5c96ff794ccf317454250b4b4d2a9f431cf | ea68e6d504213c46af7b28704f37b9258fc560ab |
| family.m3u | 42004 | e2d2c24bf79b09bdbbbb1ce6f73fb218679f002dac701bb67d4800f33d3b7c93 | 7a7d4a8b062570a41310213dbc9632548bd13fac |
| final-publish-report.md | 11096 | 2361e5f267b6b7041ebf96e317426c622d629ebf817e73afe18dce9574d67734 | 6c926405b0ea43c33eca142620ccc1817df117e1 |
| coverage-report.md | 2275 | e2ec2e48abefd042df0355436367b4c1759d724c6a2b839d2a5570e825fc000d | f8c97a2a95982049b6f9bc2f663ed1c6a3bcdfb9 |
| quality-audit-report.md | 4736 | 4d1b38ecc5671c2a00affa142765d12ee3a91805664ed8fbe0aef115abf2c1fb | bfe3817d4dc68a4bf871dcad7226cb2da69dce6a |
| publish-guard-report.md | 1653 | 35312671a12ae624f5d711924823c722251bbd5c3650282eaba2924356815b61 | 033c60ca0e1b71a1ab12827d1458425b4c785445 |
| published-recheck-report.md | 25134 | b8f5c606d3223418b229bec6c9f9f1bfa7cc8aef37776ca9035741184c87c51c | 51676a52b4fd4ef5be9204af7aba5a78b31a2ba5 |
| source-report.md | 8048 | 2fd78d4dd17b951d23143d92fedc0748c36f0a50f53cec7c025aa0d6a4e76e0b | 590f9965681be9a42fb522501b1a4045014f3eb8 |
| check-report.md | 8048 | 2fd78d4dd17b951d23143d92fedc0748c36f0a50f53cec7c025aa0d6a4e76e0b | 590f9965681be9a42fb522501b1a4045014f3eb8 |
| curated-report.md | 1804 | b81b4da8ae3c9feaa0065827a3ab0fe949cb5ad8d4c353995cbb8dab7d28af2b | 41d9c4d386b1640f82b17fcc9dd97056b92fe4f0 |
| sources_status.csv | 4079 | c701b5dad90c4e518f83c19a957ffd3c8e5b246beb55fb32e8143283a6ba3804 | 82b191a6e080b8e28eb11ceca6bc7ddb9e7eb280 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
