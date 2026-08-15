# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2121120
Unique payload blob bytes: 1526273
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 498984

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 166328 | e7480669ac22ced7f7a4111c5bcce4a0c9b1a1a525c73bac869c4508c83f9e3a | e32dbc1c56f7fe1a04503ad3cc4f70abcf889cd3 |
| live.txt | 166328 | e7480669ac22ced7f7a4111c5bcce4a0c9b1a1a525c73bac869c4508c83f9e3a | e32dbc1c56f7fe1a04503ad3cc4f70abcf889cd3 |
| live-verified.txt | 166328 | e7480669ac22ced7f7a4111c5bcce4a0c9b1a1a525c73bac869c4508c83f9e3a | e32dbc1c56f7fe1a04503ad3cc4f70abcf889cd3 |
| ku9-live.txt | 166328 | e7480669ac22ced7f7a4111c5bcce4a0c9b1a1a525c73bac869c4508c83f9e3a | e32dbc1c56f7fe1a04503ad3cc4f70abcf889cd3 |
| live.m3u | 299372 | d2052453f303362717139f7fab6087c7b77abb1b49717c6b25f85ee3a1ea728e | b63038e20ba81a5523e6d784d8c96bd4151f76c2 |
| ku9-family.txt | 89329 | b5f7910bfc586b489afaddab433730c898e7a24fcf4f9a147e02a66ca9c28309 | 54a72d61f9735cbaf9cc706011d3dd8c4e1ed06c |
| live-family.txt | 89329 | b5f7910bfc586b489afaddab433730c898e7a24fcf4f9a147e02a66ca9c28309 | 54a72d61f9735cbaf9cc706011d3dd8c4e1ed06c |
| family.m3u | 159149 | 0166592400d92716681d9085fe8a78a10a572cce09dace1d6b23ab15f51237c2 | c7ac634e75b963d5614c51111960672162d3d573 |
| stability-history.tsv | 745340 | 60be01810ed96f8c40bd2340350e6766b00d85bf05a885da9202953f73768620 | f75c1cc8452e6aa95acc7c01b9b8d71af55d13f8 |
| final-publish-report.md | 11476 | 57552c4d33d6b756a5e205728e31fc9e20893ae21aef9c95d849211590f335bf | 059073254551cd2687c211eaeb47840b2dfcf77e |
| stability-report.md | 11598 | ca56da7e8d2f419ac1294149309d9a88f173af67dce36819460b6f83aa890d3c | 076be7c4f3717d33267953aaf46d72ebd93a7688 |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2064 | 9d2c900b39c90818ac9a5eb868a596cf3288d32ab2bf2a8b8eca9e3604cff9cb | f8f3cc639f6f4ec827b799261e6abceb066ff28d |
| publish-guard-report.md | 1152 | 8840c694768ba701bcf4a932c7c3ffcb48ed0dcc6b3fd5ef9ee91c16054bd544 | 1e0b6c5a3888210bf6d4a465547f00461e7ce7df |
| published-recheck-report.md | 26151 | b252c25937277f10e010ac14cdaae1af8d3daac51ea7ffcef81cf9d375e2cac4 | f85e89395f73fc9f76e0b75d61d264c87811bf85 |
| source-report.md | 6534 | 7e45585ac2abd7cc9196e182a58883408cd3470751c029eb0cfc259962d9f73e | 7680b97eb047e7272dead12b6d132022c7659128 |
| check-report.md | 6534 | 7e45585ac2abd7cc9196e182a58883408cd3470751c029eb0cfc259962d9f73e | 7680b97eb047e7272dead12b6d132022c7659128 |
| curated-report.md | 3350 | 1064f28c8bfcabfc49a94d9658eb1fc8a5797c7ab42a0e0e33dc3ceddcaceffa | 30b9c17f00b24042443cdbc516c86ec643809b22 |
| sources_status.csv | 3139 | 9aa80ab1c66630e4ebd6eba712d7272bebbc65a25b94231504ad597b9d4774da | ef5480695912630f6af47281c30f0ff9f801573d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
