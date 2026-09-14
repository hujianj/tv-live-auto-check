# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 306004
Unique payload blob bytes: 201240
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72948

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24316 | ae6f500f0f90cc3c08ee2e18ce8c85a366dcc83dbf295847d9aebd0beb8733ea | aa92f6a74c169c9612eeb5ea5aa9fc8f0bae280e |
| live.txt | 24316 | ae6f500f0f90cc3c08ee2e18ce8c85a366dcc83dbf295847d9aebd0beb8733ea | aa92f6a74c169c9612eeb5ea5aa9fc8f0bae280e |
| live-verified.txt | 24316 | ae6f500f0f90cc3c08ee2e18ce8c85a366dcc83dbf295847d9aebd0beb8733ea | aa92f6a74c169c9612eeb5ea5aa9fc8f0bae280e |
| ku9-live.txt | 24316 | ae6f500f0f90cc3c08ee2e18ce8c85a366dcc83dbf295847d9aebd0beb8733ea | aa92f6a74c169c9612eeb5ea5aa9fc8f0bae280e |
| live.m3u | 46386 | 5f8c0dc6ec8390655c797942a6e36bee0a78917a444825f0c18ff808b174cde9 | a65b1284a996cad3610ab6e22809906209adc4ee |
| ku9-family.txt | 23887 | 6da7033a166ad1dcb1f0d3e44940b1313e1d0d14904f3373d5f0c8a12c653f27 | 0a2722b7c891e695f2ff6717c4c7b27a0a1d8314 |
| live-family.txt | 23887 | 6da7033a166ad1dcb1f0d3e44940b1313e1d0d14904f3373d5f0c8a12c653f27 | 0a2722b7c891e695f2ff6717c4c7b27a0a1d8314 |
| family.m3u | 45585 | eb8d91e6a2c201764b52910414e565e95836e6b61d769b250925955b12d75d41 | 3e588fb65e9d2d22d2b546d2868a325eb36cb2ec |
| final-publish-report.md | 10798 | 761f72b65bce3138de3ced9c9f61cb73bec886615a5ca37c5216c19e8b82fcdd | 75f61ef8c9973cd36e2dd44780fe4d0931efce41 |
| coverage-report.md | 2244 | 1eeda7ef897c43328513eaddf57cd797be683bab0d72caf120380986efcdf770 | b43b7e01e5eedf92d62c486ec0a687422d7d43b6 |
| quality-audit-report.md | 4732 | 0984d08e9f189650846f566b9b0be9def142aa828cb6d8b1fdfff4c7a4a5890c | 6c44099589aa28ccc23811ede8586d4e7f9974c2 |
| publish-guard-report.md | 1556 | f2f43b777458cdcf63e5dc76258a48eb6e734e8721b03fc94ba4a40aa4445acc | 07191722036c41d63e93e56a395d74861dfafb07 |
| published-recheck-report.md | 27830 | 1681ea57bdf86a19c8f5514d083ef1546fa18936389ad9a16e12a223e6624ad5 | 49b2918b67a456428558d7faae21d323b6c14b56 |
| source-report.md | 7929 | 05130988c40277a09a45f9cfa58ec29a4defdd180084373a03973e1998c6eb7d | c73d9db41b888020be33b2ecc68b8aa191163e81 |
| check-report.md | 7929 | 05130988c40277a09a45f9cfa58ec29a4defdd180084373a03973e1998c6eb7d | c73d9db41b888020be33b2ecc68b8aa191163e81 |
| curated-report.md | 1844 | c87071b27c864f003ba87ec2661e4ba89eb734c8a376ef152b7d380408632a6d | 3ed2ccf3c99ade11a4688c129712f69d20945c72 |
| sources_status.csv | 4133 | 0413a23cf5a4a15afd54d68644cd36faa7ce56ddf10809daf7b08a238e329bba | d964aefe721d627ed309112ece8b74e1ebea30c1 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
