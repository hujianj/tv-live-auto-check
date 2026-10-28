# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 249132
Unique payload blob bytes: 167212
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 55686

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18562 | 8c404df4788d98894d21c0060e36c622b0760756ca730deabdbdb6a2838b2967 | 19b93d3ec424e615ed9f69ca33fcaa7ce1f3b131 |
| live.txt | 18562 | 8c404df4788d98894d21c0060e36c622b0760756ca730deabdbdb6a2838b2967 | 19b93d3ec424e615ed9f69ca33fcaa7ce1f3b131 |
| live-verified.txt | 18562 | 8c404df4788d98894d21c0060e36c622b0760756ca730deabdbdb6a2838b2967 | 19b93d3ec424e615ed9f69ca33fcaa7ce1f3b131 |
| ku9-live.txt | 18562 | 8c404df4788d98894d21c0060e36c622b0760756ca730deabdbdb6a2838b2967 | 19b93d3ec424e615ed9f69ca33fcaa7ce1f3b131 |
| live.m3u | 34780 | 0c368144441e517ff6f4dffd78b7e8ccc4c9ee04143599602148bdcab7d25778 | 1dac0e2c6bcc05bcaef7c41661d1095e6c158cc6 |
| ku9-family.txt | 18126 | 32c55db78345e1b9952fce7bbe2bf81a8fbc2fe9146362e1a0e2f280b6b571c1 | c7118f48150a285eb78694fa5ff166570702b97d |
| live-family.txt | 18126 | 32c55db78345e1b9952fce7bbe2bf81a8fbc2fe9146362e1a0e2f280b6b571c1 | c7118f48150a285eb78694fa5ff166570702b97d |
| family.m3u | 33972 | 7c320d522be18a65e863aaf74fe10b539e74f4865aec79dc4fde398ee04bf2ef | 49589200a4c63deb33f593bd5d223075b9a39a9d |
| final-publish-report.md | 10920 | a44fa354f05d1436ecd4917d8ac063bb105f8fae983350dcc9421ed32e667e66 | b9f64f09fbfaf6880919d200ec858cf7be231ebb |
| coverage-report.md | 2245 | e455dfd819b92e515513e5c40b8f4127870aa916b9c871800d9e73d4bb1513af | 4128b1c27484e4b5c021ca3e237d3147812df0d2 |
| quality-audit-report.md | 4783 | 6c0cfb0431a0f6b9d67b10097011fe634609d09834b4d8537f6cd1c488363e08 | 1990039712ad4a3ab392e6a06acab722bcf5702e |
| publish-guard-report.md | 1580 | 05b21cc3362acf9fe7805d42458e3d4a3bdd4c768781815cd5b7a50dcd4be670 | 0e4539677562faec946f660ce53aabcb5b81faa8 |
| published-recheck-report.md | 28153 | 13d4f8fc015010d6a78f60ec12ab82181fa88b12e1f72184f567443c78f15f73 | a9dd0796c0cc2b7be53de29d1c1d814dfa499c5e |
| source-report.md | 8108 | 5b75a41d2b1393733a2b0d9756d2dc441425d436feafe1f92e328fe2a56c915a | c86f64ab0588899f37baf26a28920ea6739ef296 |
| check-report.md | 8108 | 5b75a41d2b1393733a2b0d9756d2dc441425d436feafe1f92e328fe2a56c915a | c86f64ab0588899f37baf26a28920ea6739ef296 |
| curated-report.md | 1806 | e4f2daba7f7b7a6c51626845a9a76c585e53f74bdbce4ec132c3760ad74f9ca2 | f628ff7af5dafe87f6ad093564c55aaca26fa467 |
| sources_status.csv | 4177 | 88a47fefd16ec76f318226b6da0552b6354e9165d5361f010cf5fbba4a17ff8b | 96af4c890189ad8054f49b3d972dd18719496a86 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
