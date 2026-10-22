# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 126241
Unique payload blob bytes: 67613
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 21711

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 7237 | 743ed5cc46074f79db08e20d3d792bab8f4bbe5f268b9c1d7c02343d2b29b72a | bc4ae759a31155e2264a1d7cada4b0ad5226e395 |
| live.txt | 7237 | 743ed5cc46074f79db08e20d3d792bab8f4bbe5f268b9c1d7c02343d2b29b72a | bc4ae759a31155e2264a1d7cada4b0ad5226e395 |
| live-verified.txt | 7237 | 743ed5cc46074f79db08e20d3d792bab8f4bbe5f268b9c1d7c02343d2b29b72a | bc4ae759a31155e2264a1d7cada4b0ad5226e395 |
| ku9-live.txt | 7237 | 743ed5cc46074f79db08e20d3d792bab8f4bbe5f268b9c1d7c02343d2b29b72a | bc4ae759a31155e2264a1d7cada4b0ad5226e395 |
| live.m3u | 14389 | b488be99acff3147674bedefd07d7b4f544f39cc5134e1a83edfe8144db73260 | 54fc253c8470035b3a9d92ae76344cfab0eb2f44 |
| ku9-family.txt | 7237 | 743ed5cc46074f79db08e20d3d792bab8f4bbe5f268b9c1d7c02343d2b29b72a | bc4ae759a31155e2264a1d7cada4b0ad5226e395 |
| live-family.txt | 7237 | 743ed5cc46074f79db08e20d3d792bab8f4bbe5f268b9c1d7c02343d2b29b72a | bc4ae759a31155e2264a1d7cada4b0ad5226e395 |
| family.m3u | 14389 | b488be99acff3147674bedefd07d7b4f544f39cc5134e1a83edfe8144db73260 | 54fc253c8470035b3a9d92ae76344cfab0eb2f44 |
| final-publish-report.md | 9541 | b464e16991e8cf5006704f1032eaf7e5d286573b6099c965457d0d1e5ae8dcac | afd38ca28208344c30fdf7e6a2479a1540d618b3 |
| coverage-report.md | 2285 | 69177603a6e9d19fe7024263df2216af79086dc1b025abb643c5ee47c513a33e | 452dd9c1ec83d7bdcb0a0d4d1a376481c4c0b83b |
| quality-audit-report.md | 4770 | ab216a371c6de6c73218853759182fbd0945e555b88d05ee39655ab90f9102cc | 15ab6ae9e475c2966d9d98dff519a07bb6916bb0 |
| publish-guard-report.md | 1824 | 7d7c98846a3d7e30b789446d6902bc94239ad421a5bd2996d70db7357990e56e | 44a90243f715277778b186243c6a97f0c977e81c |
| published-recheck-report.md | 13718 | c5286304d250add099900255fb0c57ccd84a8bff8bac8130395f67bac86448f7 | 810e262da17cc97356288a9c7625df0f24c81519 |
| source-report.md | 8054 | 3294959996d7be6e47c59f1f5c136e837706d7de4d376299f3563bec6e5ab7d6 | 187ad1abfeef255cac1e62a161431141dd69d774 |
| check-report.md | 8054 | 3294959996d7be6e47c59f1f5c136e837706d7de4d376299f3563bec6e5ab7d6 | 187ad1abfeef255cac1e62a161431141dd69d774 |
| curated-report.md | 1652 | 854e0ef345f96d7d45a38b8c5434ac5ba6049069c34931d951f5256d9cfde33d | 2ccd9e39d63a3f133e951e28bdbe78ec21715024 |
| sources_status.csv | 4143 | 566af0b0335870c8fd71a7d1629decc9c1aee379f2305e9c23fd381fae3cd2b3 | 4cf1ce22b928354ad85e638337d0a9e5f3726a9b |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
