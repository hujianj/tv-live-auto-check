# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 289149
Unique payload blob bytes: 191393
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67611

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22537 | 2c1fde90784bf111bb6af501f35f00ee7e9898c0e296efd078d8ad04ec502207 | 1d0aa5ddf24c8e3c6875e325828c08c87c272bd6 |
| live.txt | 22537 | 2c1fde90784bf111bb6af501f35f00ee7e9898c0e296efd078d8ad04ec502207 | 1d0aa5ddf24c8e3c6875e325828c08c87c272bd6 |
| live-verified.txt | 22537 | 2c1fde90784bf111bb6af501f35f00ee7e9898c0e296efd078d8ad04ec502207 | 1d0aa5ddf24c8e3c6875e325828c08c87c272bd6 |
| ku9-live.txt | 22537 | 2c1fde90784bf111bb6af501f35f00ee7e9898c0e296efd078d8ad04ec502207 | 1d0aa5ddf24c8e3c6875e325828c08c87c272bd6 |
| live.m3u | 43186 | d00820abc4fbd90b7a71904a8a304806e7267ab8a454b5caf1c5973bc7159855 | 83c37774447819d3e2f70845d1e920a3fa83358d |
| ku9-family.txt | 22189 | 266c54c6a4ab9851e9072a9d9cd837d7c97430b963aca5927e0756008e807899 | 6fc58e99759962c0807d53eb3106eefb1a4777f1 |
| live-family.txt | 22189 | 266c54c6a4ab9851e9072a9d9cd837d7c97430b963aca5927e0756008e807899 | 6fc58e99759962c0807d53eb3106eefb1a4777f1 |
| family.m3u | 42528 | d272c07b57de89ca38ae3ab83ba75a248e6db4d002c7dd259efa8d3ff8c28480 | d91717e93048f49f0c5f32ae5ef7da7726d9c2dc |
| final-publish-report.md | 10834 | 3705b8ad700069f60dc37f8be504998d2aa7277d200a5319cdd0eca5ccddea56 | 6c753cdd4b5cc16dca3afd5bdeb91672f99d1123 |
| coverage-report.md | 2210 | 762da0f4f6fa95533fb3fdaa9acfc34cf8c068b2ec68b1d9f84de94e59f40824 | c2b2b8fa62baee1e8e4c520251b383ecab1c6817 |
| quality-audit-report.md | 4701 | 9f27ebeaf663ca5127be084063c0438723828072951a27356e85bb3d03e6a6fc | 02de8689500b3ffe2d24f8db0e03fb31a60be65f |
| publish-guard-report.md | 1503 | 6260c326c5e02e81bf2997272b379c66f78ed85f696b1dc139a8e625d089c123 | 05c09068d131c9f9ce3f85e85d636862bed38271 |
| published-recheck-report.md | 27926 | e3e51d16a09a14c033e96cc4e174f489fef9fc5fdb69656b7e2ebb0c513df6c9 | a68da249a72e86c01cc7c3286324b9c3ef53d74d |
| source-report.md | 7956 | 3db748f07502a84be2c6907b3e01de2d7697032d7a66d3ce43d49807a4788d80 | 571fe6c8f91a08f6090276fb2e8fdf5c1fcf3e1a |
| check-report.md | 7956 | 3db748f07502a84be2c6907b3e01de2d7697032d7a66d3ce43d49807a4788d80 | 571fe6c8f91a08f6090276fb2e8fdf5c1fcf3e1a |
| curated-report.md | 1804 | d2e1d68f8cbceca9fe346f2114c3a4e7bd721c55e1449aff75b5468677e1e128 | 22affbd9cdeff227a6a0132844685d5a2cd53af9 |
| sources_status.csv | 4019 | 7dab026cb179500c38b80350faf636a8f3ce6a00391743e4c4f30c8b3fa8e56b | dac42cffe9e7c2241ff35be059afdf34a7e421c6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
