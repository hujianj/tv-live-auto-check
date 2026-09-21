# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 303754
Unique payload blob bytes: 199951
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72102

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24034 | 3bc1c3d5a2553caffcd80d7b70830d3b6454f7e83e4fdcb916c48af82ae800ce | f93f28ab53126e70c7bb46487567e6bd5c96239b |
| live.txt | 24034 | 3bc1c3d5a2553caffcd80d7b70830d3b6454f7e83e4fdcb916c48af82ae800ce | f93f28ab53126e70c7bb46487567e6bd5c96239b |
| live-verified.txt | 24034 | 3bc1c3d5a2553caffcd80d7b70830d3b6454f7e83e4fdcb916c48af82ae800ce | f93f28ab53126e70c7bb46487567e6bd5c96239b |
| ku9-live.txt | 24034 | 3bc1c3d5a2553caffcd80d7b70830d3b6454f7e83e4fdcb916c48af82ae800ce | f93f28ab53126e70c7bb46487567e6bd5c96239b |
| live.m3u | 45782 | 93d5a146b9912bd4b0f1626876c2790236afc3fe0defe13b1bea0be2909bdb56 | 39303e8663eac8e26b884e1f43a76e83c000e532 |
| ku9-family.txt | 23599 | a02de9f2fd1e53acad9f59b0c8c1d88a6a72187af9a1d1a4cdd88b58f6ffb11a | daabbb77a1973ce6677ad34f44dccb84c17663f8 |
| live-family.txt | 23599 | a02de9f2fd1e53acad9f59b0c8c1d88a6a72187af9a1d1a4cdd88b58f6ffb11a | daabbb77a1973ce6677ad34f44dccb84c17663f8 |
| family.m3u | 44975 | 7882610e92a3b094bfe36fe17a462da243ee1c21bd267836d77369815366d189 | 8291e750bb979c8786478748ee4aed645baccf8d |
| final-publish-report.md | 10778 | 08d15b3a47465506fdb0f625ed143087a582ea919565e36abc474c7d948353ec | 4895840ad62f8f38ad01fcd9ee07c0c16db8f439 |
| coverage-report.md | 2235 | 9e9733e3ad092dde18d0c33d5d91db94fc6e7893759dd770089eea86097e0919 | 36bf07100550c9e02d84f3ab8f3d4f2f7b3195de |
| quality-audit-report.md | 4729 | 01627e21ac2e8496800a277ad9f672a945d9a9fa24cdd1cd11fe2d30586b3969 | 327c653ec805d3577a6d9987208952917935ef28 |
| publish-guard-report.md | 1626 | 6c213db97098056cf70617604d61fb5d5781848a06e76ff7bd5806c0693fbd58 | 367e1024d40ab3b21784f400ac50a12cd603f1fe |
| published-recheck-report.md | 28155 | 0b352310d44c38746957584c188cc81b0aeb56f85465f8b4a24b1ba795c84b4d | 05d2fe27285745846e180baa478d5b125143dc7d |
| source-report.md | 8102 | 0f6036b19af8298cea069bdafe205fe50a34026bf1b4e80a5d3ecc80ef2d1fe6 | 4ce65a2cb21f97d83e8f1319efab86ba95fc4686 |
| check-report.md | 8102 | 0f6036b19af8298cea069bdafe205fe50a34026bf1b4e80a5d3ecc80ef2d1fe6 | 4ce65a2cb21f97d83e8f1319efab86ba95fc4686 |
| curated-report.md | 1804 | 620a210ee388f2fe85de1ec247e97916d4c4c2d95059b71aa1051473acb86a9e | 1a67d8091de014ceebefde95524703fb522c4959 |
| sources_status.csv | 4132 | 49faf8d6c2f6d7044932273d1a0f5cd1a0e19df3acb0643a7ce012c4570038da | 42498740ecabb47c6c060bf1dd92b6f02034437a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
