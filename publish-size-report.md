# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1883012
Unique public blob bytes: 1190641
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 686694

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 228898 | a7b7d347da4c9f351ed800900d084f891a360a94f2594c5cf8c87faf1ba06152 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| live.txt | 228898 | a7b7d347da4c9f351ed800900d084f891a360a94f2594c5cf8c87faf1ba06152 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| live-verified.txt | 228898 | a7b7d347da4c9f351ed800900d084f891a360a94f2594c5cf8c87faf1ba06152 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| ku9-live.txt | 228898 | a7b7d347da4c9f351ed800900d084f891a360a94f2594c5cf8c87faf1ba06152 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| live.m3u | 402237 | 7bdc2ca291c72d34c7db5ba826d3bda02af7bef989c2994af23ac5302171940d | 38d3523720b192a286bb18f96db17580de417d20 |
| stability-history.tsv | 504309 | 511b34ff18aabb17d4c9c534012f4a5d36a892140c6e8a331fd36f8a39a50671 | 72f8aad381b33c10c57ba0cd9b29a38366d9aa1e |
| full-check-summary.json | 11442 | d1f26f461e9372e85cbd9b2aac234f322d402afaa13ccd712890cc260cee5189 | 09c612dbe430aa15c23e1754b566750598dc9525 |
| final-publish-report.md | 11642 | b4198108aceeb6008d597b1def840ca775ef6ef1463c51c8bec32411e87f5d3a | 03cdf8e60e66db43b731c6bca2c9605ef9316dc2 |
| stability-report.md | 7448 | 58ed17d2c38be21133fa04f09fea5058a5e61fdad1ff7c2944a0df569ced0f9a | 55f6f598f2fa42945686c5dabaa1eda4bcd07290 |
| coverage-report.md | 936 | 65ef93339bbe31696172d3629dc1ec01f19f0579a85bfa3fb8eea8fb931afcca | e6df60c667cc41880bcf7b7b6f1467148f585497 |
| publish-guard-report.md | 803 | ca6b8ee5459092839f38a49d3b4781b699687de76af189d2ee566f04f24d7857 | aa14c815879af87328835b455d5d67e5634d77e5 |
| published-recheck-report.md | 11476 | a3b998010c3e9a52b912bf016f899ab689e1bce50d9e901bedb45ae3e4a9a434 | 4f9c74e3eb581fb897810d7e2fe92c8d01197761 |
| source-report.md | 5677 | fb152e6da0e54c8e726bbb6e803c23acb413c5106e78632e37eb079662716398 | ed11cfc67b6f04c4a5b8ac16d7243764b0de1f22 |
| check-report.md | 5677 | fb152e6da0e54c8e726bbb6e803c23acb413c5106e78632e37eb079662716398 | ed11cfc67b6f04c4a5b8ac16d7243764b0de1f22 |
| curated-report.md | 3325 | 601cbdec79576974c906dc047b4a1e76330e17a168989d76d2f43ae44c117554 | fe1404fa94c50f94d5fa133c82b89dfa7650d6d3 |
| sources_status.csv | 2448 | f87c0a52b652188c847b53acdfef5b8584df71a275e55c9d0fc370bb2b7179cc | b30300644f19aa1d8b85e84ad1569cd777a9f6bf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
