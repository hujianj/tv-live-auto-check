# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2027114
Unique payload blob bytes: 1463236
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 472173

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 157391 | 227ff36f985bf27d735e8c7e788b2bcb39a61133b58ff04bc60573316da31931 | b39f80be38d32cb544064ddf27227f2bb0b7a427 |
| live.txt | 157391 | 227ff36f985bf27d735e8c7e788b2bcb39a61133b58ff04bc60573316da31931 | b39f80be38d32cb544064ddf27227f2bb0b7a427 |
| live-verified.txt | 157391 | 227ff36f985bf27d735e8c7e788b2bcb39a61133b58ff04bc60573316da31931 | b39f80be38d32cb544064ddf27227f2bb0b7a427 |
| ku9-live.txt | 157391 | 227ff36f985bf27d735e8c7e788b2bcb39a61133b58ff04bc60573316da31931 | b39f80be38d32cb544064ddf27227f2bb0b7a427 |
| live.m3u | 281181 | 51eac847d74531b86949800452985070bc74881feaab2d53178e1a1d57f12a82 | c29f097fbf4726453d29c6d0d3b72a4c9213cdad |
| ku9-family.txt | 85147 | 9e695e2a9aefde54c7b0cf29695bb4d9f0d930f111786682b0f5d89fdfe3aa8c | 9e31dfbcbe120f93dddbb392865613b30b1a0d99 |
| live-family.txt | 85147 | 9e695e2a9aefde54c7b0cf29695bb4d9f0d930f111786682b0f5d89fdfe3aa8c | 9e31dfbcbe120f93dddbb392865613b30b1a0d99 |
| family.m3u | 151014 | 4edf95d2e44b89c5b2772f1f67452f5ba8b20683adb855a5078c269fdd8f642a | d845ad67192a76a50ff89fa8468fd015df68351b |
| stability-history.tsv | 719203 | 0f28a6be7499f7f166e8d31257f141b8e9bd12ddfc918b02254fc4654c6c86b2 | b0c568d22b214180fc6fc0b9dde2777c21b03726 |
| final-publish-report.md | 11795 | bbe42cdfead4c30ef229188ba7ecbbeebba770993d0f9be30323b2123e6e88ed | 0f190e661269991165976a30ada81e28fc28d7ef |
| stability-report.md | 11999 | e48463f52b03d0595eebf7c588f7f70acf820d8c64b1c013dd9ada2256216f0f | 2408c2d82f035c32d9ae29811e8eba25e2688934 |
| coverage-report.md | 1291 | 89a4512f4950f006e60c2e42c1f0115e30b9f3ffc146f3f0e659781a988c1f00 | a8f39dd75b36ed851447f1d2f8323abc20c8730e |
| quality-audit-report.md | 2063 | 5388d382e9135992dfc6b89fc6c6cd879509f81ea3f0143c3e34d261d9e861b2 | 101c51aba5355253acde9b651b81265380b61405 |
| publish-guard-report.md | 1147 | d30343e018a867e9eac8e5e057d9f7a3acd07baf3776bd01bcb5f6a8ebae7142 | 92b04a02caa60c7d562eee5c1c71f5b7381b7584 |
| published-recheck-report.md | 27974 | b6ec860d0a5a4ac1bf5bd6326d9f99075ea4221c3c880bd9e3eb98c371e21278 | b26d8caed3f6f447db77e7bcc339211663c063de |
| source-report.md | 6558 | 95f1509e3f8b289b5c8cb21128f72e62ec655fca9ae683ff96e0b4893a8db0bc | b8d82692fa331730ba61fb6d9b010f8ee4f6f7d7 |
| check-report.md | 6558 | 95f1509e3f8b289b5c8cb21128f72e62ec655fca9ae683ff96e0b4893a8db0bc | b8d82692fa331730ba61fb6d9b010f8ee4f6f7d7 |
| curated-report.md | 3340 | 8ea32a17ace9aacbd5a03731a70f577f68eb54a62ba22f73a3b55d9e0102876b | 27711eeb8b4e35bcc909f8675a5ba2b247251fd6 |
| sources_status.csv | 3133 | 84aa119c5915dfe4143784b2c6e7516f2d0d05bdc4aac8856bd59fa6c3a0d122 | fb376371549f7a5791d84e9bf7f3055ea368f3ad |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
