# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2072426
Unique payload blob bytes: 1501242
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 478443

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 159481 | b771c4b8e3b7c1feb5d2b890d21b0581cd21d052a7aabcefe14bbfc35ea47c7e | c40b9bb30a14f228487cf07fbdbee61c833a2b2f |
| live.txt | 159481 | b771c4b8e3b7c1feb5d2b890d21b0581cd21d052a7aabcefe14bbfc35ea47c7e | c40b9bb30a14f228487cf07fbdbee61c833a2b2f |
| live-verified.txt | 159481 | b771c4b8e3b7c1feb5d2b890d21b0581cd21d052a7aabcefe14bbfc35ea47c7e | c40b9bb30a14f228487cf07fbdbee61c833a2b2f |
| ku9-live.txt | 159481 | b771c4b8e3b7c1feb5d2b890d21b0581cd21d052a7aabcefe14bbfc35ea47c7e | c40b9bb30a14f228487cf07fbdbee61c833a2b2f |
| live.m3u | 295138 | 7c31c2007cef1abc324e42d1e2f49a6e7adb71e58c79cdb688618efa4b1de021 | 29b495bdfb93ecb226f7374489b681a16b8734b9 |
| ku9-family.txt | 86197 | ef976e2226f8d44ca628e243447d0ccb8579ba5cc6204e55514d5462e7ea05cb | 746171e80a1720ef7f8761dc35bd284f4f75412e |
| live-family.txt | 86197 | ef976e2226f8d44ca628e243447d0ccb8579ba5cc6204e55514d5462e7ea05cb | 746171e80a1720ef7f8761dc35bd284f4f75412e |
| family.m3u | 158180 | bac0b73039237ee683e4041178a3dcf002cb31aadaa46eb4d98292a6a1d74b4c | debe2af228b7d4ab724875954d0a87cf35dd8d28 |
| stability-history.tsv | 735715 | 910580bfb4d53e77cd76dd1b5177a27657aa400dd82c4e3d89950cc27a56490b | f85dcb5111ca2b8ffc0b95b3e1a9c4b7b8b2e682 |
| final-publish-report.md | 11732 | e19df7cdae8bccc0f16425f2e2e9656b6a3e1c00ec417c4489922d42ff3a7eb7 | 415f49883c408c4086470d1df897c40665109385 |
| stability-report.md | 10809 | 31c500ac965aa4509e801851eec4b354867da3c770f3ff7cb2f420a16fdba9fe | a5258d9e835c0c955368d6c3193f328644476824 |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2066 | ec72b6e65879ca38fe289f958b08dcc1b2cdf8e7e491ae4577832348e508a5ec | f03bfc7e667139d034cc2be8ed38b92e26a35d25 |
| publish-guard-report.md | 1039 | e2e17af41a638c2d2fc35eb99b49540b7cdcc771e1843fed41505852821fbb6f | 227bcfd98d0c331f3c59946920a5e6ed05b48f23 |
| published-recheck-report.md | 26464 | 201cf8e5ff99d040abafb4646c133eaf1a167908c65aebcbf656169fc6c47cc9 | 71c1942ac7c13f10d48062b01b1f22da8d25e1fe |
| source-report.md | 6544 | 5abbfbaaed8178141bd6a908f843aecba1af6f90900df4da5c9ea024070892c6 | a5bf489942c6ba98b1dc69b7c075d1004150aa21 |
| check-report.md | 6544 | 5abbfbaaed8178141bd6a908f843aecba1af6f90900df4da5c9ea024070892c6 | a5bf489942c6ba98b1dc69b7c075d1004150aa21 |
| curated-report.md | 3523 | 0a66244b0bf8911b975b83ac9d8725905455614bb5f737380e26e3f9ff5232ee | 96e6eb4ba43f3b06c4676c2dce2e4f18e8e51edf |
| sources_status.csv | 3063 | 48e4ebba833d311deb3fa778acda297a7e2fecdafa07c8e16a8e61d90417f17e | 99522ca4712d80017150c897c3f8f681712c16ab |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
