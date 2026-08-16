# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2078861
Unique payload blob bytes: 1510386
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 472086

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 157362 | c24fbbde80dde49d164932c86fcf3c8434511b5b4aa936f567bcca2ff97e0da4 | fa09eac9d1775ab50bc99b428c61aac827af74e9 |
| live.txt | 157362 | c24fbbde80dde49d164932c86fcf3c8434511b5b4aa936f567bcca2ff97e0da4 | fa09eac9d1775ab50bc99b428c61aac827af74e9 |
| live-verified.txt | 157362 | c24fbbde80dde49d164932c86fcf3c8434511b5b4aa936f567bcca2ff97e0da4 | fa09eac9d1775ab50bc99b428c61aac827af74e9 |
| ku9-live.txt | 157362 | c24fbbde80dde49d164932c86fcf3c8434511b5b4aa936f567bcca2ff97e0da4 | fa09eac9d1775ab50bc99b428c61aac827af74e9 |
| live.m3u | 289116 | 65fb3cf02403517ebec76d9e2027e6c3538ef6a77fb931665f8440091e868423 | d324f209068308f2c0356accd8270b7b2600aae2 |
| ku9-family.txt | 89853 | 32fc168184b36353ba450db3fe50048cb83aaf4b64f514200a4250d32352d7d0 | a15fcf0f0a3fe87e047151a89f968f1021cfaf46 |
| live-family.txt | 89853 | 32fc168184b36353ba450db3fe50048cb83aaf4b64f514200a4250d32352d7d0 | a15fcf0f0a3fe87e047151a89f968f1021cfaf46 |
| family.m3u | 162373 | b972ffd5be55d89de95ff2f4b70b7d452a0416046f2d566b48ca66b81eb30e9f | 9bb8bf8e6b59edf4b34888ea18d03f8ae4fa3660 |
| stability-history.tsv | 744752 | 5a4019df2a9e2e9e4cec884de1ef12b8f979aa66b9ff47c5e1014e715be4149a | d34e9ba9cc0bc91ce3d2b5476682b012f28b5948 |
| final-publish-report.md | 11599 | bd647cf5a544033b25b1b20f898c48a6827b1678bb5b9719bd0ec82d5e027106 | 4c8339753298c93b7ca8deac19cecdc9fca92434 |
| stability-report.md | 11592 | 1cb36e5c7e8d521d79cb620f0dc1810656ec6b8f692f82c9d81d04e7a3634f0f | 5c7ddeab9f8f9ff5e40d5b56425126bdafd2a615 |
| coverage-report.md | 1291 | 9a9febb3a3366cccede711986bb4620c8f6847cc1065f60e7ef6e7a1a5ad4e63 | a9d86227fc108f392f1b966be7c9fc51af952511 |
| quality-audit-report.md | 2071 | 9a66e8138a87817c49d1589f3bea646982230aac3cc0a8f80491b1b944b20e47 | 0871860b98015769bfcd6b4da00f2d26066883ce |
| publish-guard-report.md | 1037 | b10efe3911d0bd14e1bfae5ba22195bbbcd3aba6196a61c70d20217197a3617d | 9cf2f15ee51bdc24ff9fbbf4bf373ed09337a665 |
| published-recheck-report.md | 26207 | f0aab90e61241f82a24ebcc8064fb54c9753cda8b83702352ceee1f18c074832 | c69aa3a7c5494dd8a842cc845b718c3cfba8cf2a |
| source-report.md | 6536 | 2dd7738435ce96c196430daf3cc54ba9e88750a1f5d3c38be7833b7329321a74 | 22d63696b6bdd03378405a3aa04aaeff4fc43625 |
| check-report.md | 6536 | 2dd7738435ce96c196430daf3cc54ba9e88750a1f5d3c38be7833b7329321a74 | 22d63696b6bdd03378405a3aa04aaeff4fc43625 |
| curated-report.md | 3539 | 109c3c1f8d3cc15928c4ac043cfc790f344884c8a5e2f81217f8ee3adbdcb5ff | 96b51e791968c9d07927f48c4f1796f94a559561 |
| sources_status.csv | 3058 | 2896df69567566fad34a6a26409f419c9aace83dff9a271d5fb83f6f392789ac | 2c794f2119a1ae03fc549af70d57a97b23354efd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
