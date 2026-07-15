# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1721050
Unique public blob bytes: 1123237
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 592197

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 197399 | 962dd8d62eea1d0e5259ea0dfbdca0ec5572c1a862d2e3a7a9e0204cfe04ff13 | 71593b22bb55363ba79a9d76fa8850fbffb1d481 |
| live.txt | 197399 | 962dd8d62eea1d0e5259ea0dfbdca0ec5572c1a862d2e3a7a9e0204cfe04ff13 | 71593b22bb55363ba79a9d76fa8850fbffb1d481 |
| live-verified.txt | 197399 | 962dd8d62eea1d0e5259ea0dfbdca0ec5572c1a862d2e3a7a9e0204cfe04ff13 | 71593b22bb55363ba79a9d76fa8850fbffb1d481 |
| ku9-live.txt | 197399 | 962dd8d62eea1d0e5259ea0dfbdca0ec5572c1a862d2e3a7a9e0204cfe04ff13 | 71593b22bb55363ba79a9d76fa8850fbffb1d481 |
| live.m3u | 347204 | de6347e5d53608889ddc68171abc5801acc0df68ac4b80b8a01551a3ebd22d68 | 0632bcf9815f81d17332ad925cb380df54c6783e |
| stability-history.tsv | 521274 | 711d535072db2754ac51af9c1a91f49a6717425ce88d98d8007f3ce27ecf571e | e1716cb4b71e11eb17645ed903d426dbfa011d17 |
| full-check-summary.json | 14632 | 6148c3cf1ecd9482a83fcddda6f8c01e3182f83e6a4fe61f6d2a380249c258de | 09b37ee659f80c3794a97544d9b95ea8bc413cd4 |
| final-publish-report.md | 11503 | 99e5bcb22439dd72b94c027403a0f7ea7d32a945ec47f099778c51bac2c36a28 | fea63ff10e21ad43174e1569db3e84664dabf492 |
| stability-report.md | 7485 | 5cb7fa854a0ee7d72166aa710f63fb65e1a91f2674c38465d5caea58d69be575 | 4923af2334795897fe00c7f0246b3a53ba62d891 |
| coverage-report.md | 1123 | 2e17979f46ce372beb8ce82962488f5feeefbd2afc81b79738e1c812d8378e36 | 80aa5543b5ca5860ae53e849b8648aea41901550 |
| publish-guard-report.md | 807 | 44c382087e306d88c1abb8c63820ea9b608c8af94ae29ad095098d7a6fd9876f | d68b0580176413163de30107b1d2a397af4a0afa |
| published-recheck-report.md | 10055 | 4f45e3865f1f5027edefc999ff00db9d5f54a5d3f4e4d1b6e8062a5cad83eb58 | 34116095e9cfce4b8bc780471f2086b2141ec754 |
| source-report.md | 5616 | c27ec63a66f1e4555701fa7675701817b3e9d3bd9a683d3b78c0278ef7e6a37f | 2790495afb4e79a4b49a3c949e135b62c5f6f5da |
| check-report.md | 5616 | c27ec63a66f1e4555701fa7675701817b3e9d3bd9a683d3b78c0278ef7e6a37f | 2790495afb4e79a4b49a3c949e135b62c5f6f5da |
| curated-report.md | 3691 | e09bd020ec25e6e1b039ad8cbbad2103214787742a0406bd3433942cbf831e9d | eb2b3d897881ccded2bfe069dcb3cb3471c10ad9 |
| sources_status.csv | 2448 | c81795877941c448a3edb9a5b1cd16b0ad6da8c74dadcb7c75a4e8719c57aefd | a1620a3fd2c8530441bb7ba000e0c1a33636e674 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
