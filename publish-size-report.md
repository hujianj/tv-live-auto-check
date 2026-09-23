# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 279863
Unique payload blob bytes: 185776
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 64725

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21575 | 90d261d1169f6d6279fc2b109d5f9336191a137f6050c0a3ecd65572ca97b80d | baf01e9a9c3821691dbd2bb93706031bef9bd880 |
| live.txt | 21575 | 90d261d1169f6d6279fc2b109d5f9336191a137f6050c0a3ecd65572ca97b80d | baf01e9a9c3821691dbd2bb93706031bef9bd880 |
| live-verified.txt | 21575 | 90d261d1169f6d6279fc2b109d5f9336191a137f6050c0a3ecd65572ca97b80d | baf01e9a9c3821691dbd2bb93706031bef9bd880 |
| ku9-live.txt | 21575 | 90d261d1169f6d6279fc2b109d5f9336191a137f6050c0a3ecd65572ca97b80d | baf01e9a9c3821691dbd2bb93706031bef9bd880 |
| live.m3u | 41486 | 2ced0d746d53ad6b4e9a1e2ee6a976ec1e770efce6b416945dcd1ce6c5fdc9ac | 20bac1579ed99e98a6d967983c604417f01cd96a |
| ku9-family.txt | 21303 | 25e1b2106f0fcef52da12be4c7adf5bb20765bf2aa07173293fda15efe54a07f | dcd5741043c697b16a60738044a2f467c3eef873 |
| live-family.txt | 21303 | 25e1b2106f0fcef52da12be4c7adf5bb20765bf2aa07173293fda15efe54a07f | dcd5741043c697b16a60738044a2f467c3eef873 |
| family.m3u | 40966 | 582900c3e7b89ecc5330f741788db69ef5018c9006ebccb3780ccdb3238a2f5e | 25b0e1fe65f0f74783342467233674f963fadb29 |
| final-publish-report.md | 10719 | 8164f4a17c1ad0a4a6b7c2b7cb41f5664e655f635750c556e1af8b9b77a7f48b | bc85cd8d0e7b628e0bb20fffaea1172885ef5546 |
| coverage-report.md | 2230 | 5b98faec5476bdf4bd198608384dac69a4c55297b0a05b065ae9f303c46eb240 | 3e2a03855e4096ad59b81c4032e907856fefd14e |
| quality-audit-report.md | 4730 | 3c8be7b35bed10948922a22321f507e303b8d29a148834e27aebf045dd776cd6 | 56b52ff088199f1fba9d9b16b150f3508e63617f |
| publish-guard-report.md | 1610 | e9f68578570af8e227a7ea288c46c2e010c1e0e2b2e38b80bfd1f381d1395937 | 7de5b622b54a00e1ca4fac9eb87da3edb251ac29 |
| published-recheck-report.md | 27160 | a59d8ef00a8de8d5b5221d4b81a3aa1daa0c4ccec494b0452eab465f13dac373 | a08e9b6c2245be5d2eb1e9755b312ce95c6894c3 |
| source-report.md | 8059 | 9ed11007619a5d696d042682647ce15c80dda27d903b7a9f6dd41ca7d784e686 | a6851b6e70bb8a44529f1b834d91a5c1800368a1 |
| check-report.md | 8059 | 9ed11007619a5d696d042682647ce15c80dda27d903b7a9f6dd41ca7d784e686 | a6851b6e70bb8a44529f1b834d91a5c1800368a1 |
| curated-report.md | 1806 | 33698e029a08ccfbd61b1be9eb132bb305bc1daf54f608a090c262be2919e21a | 44cc68c96d0a4321620e36fcec5b9918c1d35fc9 |
| sources_status.csv | 4132 | 8422430d362ca33b588081f353e4edf2c2b54767b0ecbdfe20d997a4ef484189 | bde9f9df22b039c1631c48759f0c66fcec2a888a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
