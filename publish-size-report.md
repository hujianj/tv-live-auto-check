# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 379905
Unique payload blob bytes: 302262
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 46518

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23259 | 5424ba56a6bf07982c93628f9d2909a45244fb11f6ce1a51331ee8b846252934 | 98211c5d20222c7c51e5f09e61d089d1baf2ff89 |
| live.txt | 23259 | 5424ba56a6bf07982c93628f9d2909a45244fb11f6ce1a51331ee8b846252934 | 98211c5d20222c7c51e5f09e61d089d1baf2ff89 |
| live-verified.txt | 23259 | 5424ba56a6bf07982c93628f9d2909a45244fb11f6ce1a51331ee8b846252934 | 98211c5d20222c7c51e5f09e61d089d1baf2ff89 |
| ku9-live.txt | 25561 | fd8727ad1201843155580c3f0030965b037f6ec956e4a6c9a0318823b57a0b15 | 4d3e2f2700318eab37227be3b1f0e85114e42cdc |
| live.m3u | 44662 | 5430bb49ed8d38cfa1b953cc8680f41c855b482d8c4057ddfc0b9f9b6f52cf7b | c338f3acb2a4e043ad967239e1c9e66201540595 |
| ku9-family.txt | 22823 | 0a0c174683f88996652a7e2c37a0e6f0c5e0ce9d4774a5fda7d71edb606f7209 | 00d47c7bf7fec0e1b3983f2046aabb1ab87d330a |
| live-family.txt | 22823 | 0a0c174683f88996652a7e2c37a0e6f0c5e0ce9d4774a5fda7d71edb606f7209 | 00d47c7bf7fec0e1b3983f2046aabb1ab87d330a |
| family.m3u | 43854 | 491ee97710a428c7b86efbb7163a3a23f93ac1c4e0a94baeb1752aa903a21d20 | 47cec45ea8fad70de182ca2f1baab2e94db55705 |
| final-publish-report.md | 11114 | 5f71935cb9dee5f577d8f4bb7a25b5fbff983409f18fa9e850da4eb04f66e4d6 | eb5dd306cdca2fb2c7f9f7f1bc857b690d4f5e54 |
| coverage-report.md | 2200 | 8a9324edacd749d3e5b011c53147793dd760557907860864be45c557fdc78703 | 033bc9fc3693cb6f9316dfcd45bbd7cfedffffec |
| quality-audit-report.md | 4705 | dd896aadff53e361947f04cb937cd03bd8a3cc1a2f47d27f28576a13355f5633 | 0616f560e80ba190b2409a341712862bd4d574ed |
| publish-guard-report.md | 1568 | c9b37c62ac98e663f10ca41346d1158d9d1bb9e7fdbe15c897909bdb423d3ef0 | 80f3d61241d5b894847b68af646027d084b5aed0 |
| published-recheck-report.md | 30603 | 399874a49311555643e98b4f9f2a4a683b1ff538ab01e8c21d00a95d38a2439f | 2d79b542903880687ad423c54526cf6e809d499f |
| source-report.md | 8302 | 66e99c12b1c1c37988c5f8254bfd7276d65853e18f98939e3c24a7359658efdb | c6c4cb7586d74cda886e9597ccc78d47b90b2ff8 |
| check-report.md | 8302 | 66e99c12b1c1c37988c5f8254bfd7276d65853e18f98939e3c24a7359658efdb | c6c4cb7586d74cda886e9597ccc78d47b90b2ff8 |
| curated-report.md | 1897 | 32dcdd93d8a581d5e0348a3da35e6a5c464aba1d65023a0e6e98f3f22add54c5 | 92ea98d3630dd8880614a15866e6099f90891ff5 |
| sources_status.csv | 4241 | 50da6d8fd60e436df4d7133926cdce33e83047334b9a53b71b68b7dcee011bef | 1e40a0882eb971c512942072a61798a514cabbce |
| tv-coverage.m3u | 58426 | 169cf8699b92c352e6ebdddb3d6e1341588ff3229c3eac944fef65b9ce41fcaf | 3dfe29278c5b1a5d7015f1fdecac15bb39b644a6 |
| tv-review-report.json | 12321 | 5d98a3a47b66e8fec7a66095cfe446d7022349cf7ec8543422007ec7a79bfb21 | cbe79af5f2d3ede14031eb0b5c0fc4c300954657 |
| tv-review-report.md | 6726 | 3bfcc093b6977c927f9f1c10b884dd51a78cf17eb3926f98377ac82d5ef559ae | 070bb1fa3a2d3ca75c825ae7a53627357a91dd66 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
