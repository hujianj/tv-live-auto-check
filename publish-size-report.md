# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 286803
Unique payload blob bytes: 189505
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67110

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22370 | a0b7290cda7e83b577cae95f6d66fd632281da6cead95e65bb5e7262bffcc6eb | a7418510867abf36e2f5f211af4f726b9f005597 |
| live.txt | 22370 | a0b7290cda7e83b577cae95f6d66fd632281da6cead95e65bb5e7262bffcc6eb | a7418510867abf36e2f5f211af4f726b9f005597 |
| live-verified.txt | 22370 | a0b7290cda7e83b577cae95f6d66fd632281da6cead95e65bb5e7262bffcc6eb | a7418510867abf36e2f5f211af4f726b9f005597 |
| ku9-live.txt | 22370 | a0b7290cda7e83b577cae95f6d66fd632281da6cead95e65bb5e7262bffcc6eb | a7418510867abf36e2f5f211af4f726b9f005597 |
| live.m3u | 42774 | 1979524bbf14a58187dabb569bc48e5d0f81514fc9b455491f8c29c73eb79e59 | 9e8f1a7257a8d1e62c80fa875689e63aac7e83dd |
| ku9-family.txt | 22105 | 66db12a2ef3b11377260349da4edd0ff35d02413ba65d0304823851ec778ee61 | afcfca7efb83129b8c28902b4a65b39678bac3d4 |
| live-family.txt | 22105 | 66db12a2ef3b11377260349da4edd0ff35d02413ba65d0304823851ec778ee61 | afcfca7efb83129b8c28902b4a65b39678bac3d4 |
| family.m3u | 42261 | 46e141e5df6b8ff622e8f7e856f4a6bc4365935c7324caff78c0972a61c630bc | 62c2d295f0e81ac95095dcd80106f5b9ecce569d |
| final-publish-report.md | 10692 | afc630d28f7d41b94baf5a6ef4ed95a3bf096c15293b56558c64c224e656e5ff | baed40500ffe9c11503e9380ac12f133b02b7070 |
| coverage-report.md | 2225 | 9313f064185056853c66e4ddfa913b2ab0b89e0700b4be411210d5dc030ff152 | e007670077b15ee778ecee54d3dc82da93345ac8 |
| quality-audit-report.md | 4718 | 08a506858a0e6e7f7991e86a6e62ddbe2add22c6795988ba5087124cbb0091d2 | 2bc895829f1bcd8b12b58e7146ef71b82800eb8d |
| publish-guard-report.md | 1557 | a40b37ebe5589eea6924452f5bd9de6cc4e9010b6c9f69c3c7de518d5d6c0455 | 925433a314d432426604d215829c3adc64fde392 |
| published-recheck-report.md | 26778 | 5db219d75a530b5c30034bd231b6deeb5f02f455db021bbb74aa3a6b5ece1d1a | d46d53220c2a57e924f4ceb521db5453ebd45717 |
| source-report.md | 8083 | bb6d43d9cc638545104faaf140070ffafb62f63809237b5aacd1f29ca6307b32 | 4e1a02e97de8144806abbe9e40ba0ec3b531a6f3 |
| check-report.md | 8083 | bb6d43d9cc638545104faaf140070ffafb62f63809237b5aacd1f29ca6307b32 | 4e1a02e97de8144806abbe9e40ba0ec3b531a6f3 |
| curated-report.md | 1804 | 9c42fa3c67916a48b437aff767ecd8f6a0226d9c552867b006009856dafed42c | 4278bbebe6fd80777e5cbcd3354f14ace8d6a864 |
| sources_status.csv | 4138 | 6c328533aa85e6dc983f472d3a0aa7ec6d1c85e72e6b948981905da5ebb1b209 | fb0fa81490bb6bd0dc3ff9c2430fa7d85e3f0d7c |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
