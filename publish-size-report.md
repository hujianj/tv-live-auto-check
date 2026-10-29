# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 362062
Unique payload blob bytes: 289061
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 43560

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21780 | c026c01fef0d27afcb58c593bc53a127dfbd64e023e481ecaf6ef4769bddc35a | a40790cb12330c8ec782bf978e3c0d4e5f80f27c |
| live.txt | 21780 | c026c01fef0d27afcb58c593bc53a127dfbd64e023e481ecaf6ef4769bddc35a | a40790cb12330c8ec782bf978e3c0d4e5f80f27c |
| live-verified.txt | 21780 | c026c01fef0d27afcb58c593bc53a127dfbd64e023e481ecaf6ef4769bddc35a | a40790cb12330c8ec782bf978e3c0d4e5f80f27c |
| ku9-live.txt | 24338 | 51e4af55dbfdc33fb0ec2e3193de2765a7a449676c942aae3940984820a28ecb | 37bd8f9f4b7ff6b9e4c15269d999a6962845218c |
| live.m3u | 41055 | 9ee690b2ec5d27765cd998ee2b370fc0abf01c2a2ef27815ed898318365aec65 | 89dbd870e8620ba5c3ea6dda892f8b77306508c6 |
| ku9-family.txt | 21344 | c826d5798a6050f9b906ff1c5be0284a33b27f09461dee41fdf018ee2b1abc04 | be4eadbe2b6cdd9bfae7188fd20be9d1ee694e1f |
| live-family.txt | 21344 | c826d5798a6050f9b906ff1c5be0284a33b27f09461dee41fdf018ee2b1abc04 | be4eadbe2b6cdd9bfae7188fd20be9d1ee694e1f |
| family.m3u | 40247 | 527875d74d31ade5d130af00917e397d37a5cce990927536510d334be4b7b316 | b52a33a0cfeb9cd3dcde806a63ebe9b8a3a0a331 |
| final-publish-report.md | 11077 | 953eab2b321ff71bdb25307dd96e597aa56d1a0f10844d502aba172b13c85214 | 8350cdea0804a4622926e5bd4d7f243ed5b88ff2 |
| coverage-report.md | 2200 | 0f476ad52a95ee951de0d575354e6618ad9cf7d23293db82612d3b30866b0c09 | f2d72c3a4a711c6622a34daa859138c7d605b951 |
| quality-audit-report.md | 4702 | 6a374786a2d9f533e99cecfbc185967e6c93758f2b25645b4bc9b0ec6feb8669 | ccd6958dc4a54889595342799c58a8ebaa8c159a |
| publish-guard-report.md | 1528 | 6e9cb36669ede3b9146c68be1023c08d0face8019fe2ad3826f09325bd8a61c6 | 4230cc955fc9aee4dc7e346da58cdd53b533901c |
| published-recheck-report.md | 31005 | 7b530115e4a6dd2d493ca9238d1dd659d5d576f60045c82620c6e6d0d229ad48 | 2be0ff2e886f2b82ab63c47419b51b7d435c5353 |
| source-report.md | 8097 | a8994103784135949ff1fd2c70d60636829cfa8e39a3082243c2ff382d6bf39e | b9d106d96661bfd2609c370ae08680b746fb3051 |
| check-report.md | 8097 | a8994103784135949ff1fd2c70d60636829cfa8e39a3082243c2ff382d6bf39e | b9d106d96661bfd2609c370ae08680b746fb3051 |
| curated-report.md | 1896 | f1ce98dfcb360731144b87e5645d8803a03a500fc70374cca5c19a3a516cd8c3 | 7a64308fce003e5f3d8c42cafb387937955ccdf7 |
| sources_status.csv | 4177 | c19509c23d0bb6338ad46f989465a94019a80bc25814c40e4e47ee322751d410 | eb4759aa4ed8952d8953f11ec6bee11c5bf44527 |
| tv-coverage.m3u | 54485 | 9848b76206af2172f7f2d4006b0c82f536a5139b81175016772fe515143c924a | 5c3caa974e81544f7ecde152b099fb2dff04543d |
| tv-review-report.json | 13655 | 1ac215a7c7673c4e0026157608089d2d43f1f2695db5d37fa09f0cf0b1b99b47 | 6d798377262b52a90cd08fbe37fdeb04ee057847 |
| tv-review-report.md | 7475 | 0304b2e17e7af20536f0514d5d0b17174227b93e152a4d1aec187c0f1bde9d96 | f03464ea54a91296ceb6bb3404655a9ee18ac8fd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
