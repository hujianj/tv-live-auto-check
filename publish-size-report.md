# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 337794
Unique payload blob bytes: 273013
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38092

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19046 | 77eb307fa912c5579e84e04f42cbcbe3d7344f1c63ce759d084fb674edc8b85f | fe5382ac728a5f09d73ee462df789af45ee17ea7 |
| live.txt | 19046 | 77eb307fa912c5579e84e04f42cbcbe3d7344f1c63ce759d084fb674edc8b85f | fe5382ac728a5f09d73ee462df789af45ee17ea7 |
| live-verified.txt | 19046 | 77eb307fa912c5579e84e04f42cbcbe3d7344f1c63ce759d084fb674edc8b85f | fe5382ac728a5f09d73ee462df789af45ee17ea7 |
| ku9-live.txt | 22607 | f55d800ff8d1fe9d2ffe3d87e7cb033011005f0c45c5354cedb9c809cec9aa64 | aad744ea32cd237e8e09a89bf11f3c650ec2ccd3 |
| live.m3u | 36700 | c1dbdd2b6458a30b310411433dc1abba52e580090a68971c742cb4396bfc1356 | 7750fa1358c321c332fce00e7d44d634315894a7 |
| ku9-family.txt | 18562 | cf0c68d20cb166e792eb2d7637a03040aa3aba16c9e282c6736c2d9e81576521 | 7b47099c63c0f87865787fffa4a7bcf4e64c3bd3 |
| live-family.txt | 18562 | cf0c68d20cb166e792eb2d7637a03040aa3aba16c9e282c6736c2d9e81576521 | 7b47099c63c0f87865787fffa4a7bcf4e64c3bd3 |
| family.m3u | 35785 | 435d24864621bba2e2a079e7950ad8bbe9f22b1d11a30f370d8ab790e017e86e | 5f95b652da4e06e3c90176213b3e0c6c82b69e82 |
| final-publish-report.md | 11368 | 8c17667248e8daf798193cd40b8b2dcc170241f42d4d6e0e06424b2fff0ab4cf | e45863e4fbeafaf61b8dc70ee9780b4da49e8081 |
| coverage-report.md | 2205 | 1d0004523b550cf4a2b7ae300ffae96ae8985286065fe40c512ae82da273d9bc | 976023940a6a5c500bb1ed2b2296bb8553326e4b |
| quality-audit-report.md | 4681 | 5997bf78640f059bb04d560a7993decfef097a08d545137b4da4e4cfe18cce5b | aad522a43961e7fb66d99996143fe0e13da75fbe |
| publish-guard-report.md | 1592 | 727c62cc0e95a47beb7e718d6df9f79e460dc30a1f13a6db7d395db760b4ec0a | 121c44ba094016865853371ca3489d0fb812e95c |
| published-recheck-report.md | 28706 | ee35672786ccf495c769c34d36e776149f00395a4de5ac38b316308c56ae0458 | 28603ab7d7d6b78b6768f1990d8f710a30bf9cc0 |
| source-report.md | 8127 | cf9fa20c10a8b4f6a7adc29e35fe81462224f1a27744a32b8cc7fff6ba669bfd | 0ef73afbf882f8ee8a24465263b18cf06ac7f06b |
| check-report.md | 8127 | cf9fa20c10a8b4f6a7adc29e35fe81462224f1a27744a32b8cc7fff6ba669bfd | 0ef73afbf882f8ee8a24465263b18cf06ac7f06b |
| curated-report.md | 1836 | 2a9376ded42efda41bb7e3e8d59102c1ece9ba358908a7d4d1167a6712757668 | 0ad081e215437bca3709509657e0c397ba6a73a4 |
| sources_status.csv | 4181 | 07ba26655c7f57f595e805ade3ac06490cc462b8f49af5b638acd3670f899904 | b45317c3798a93d19d1a08da886816743a949e18 |
| tv-coverage.m3u | 51285 | 9bb7ed46a1b3f6faa2c37700157256e00b91c4f022599a2a472d33d93e30cb3e | fbd4c7116bfcf12b2193bc436adb2d460deb138c |
| tv-review-report.json | 16841 | 3ce48551952b018ab8696a401d0a770ca19e62709d04fbdbbdb6918749787812 | 768ae43b964d37ddc72915659f8b85a46e8b0875 |
| tv-review-report.md | 9491 | 3ab9b938b35602be615f9d17a12e2d304c1d30c203317bd7c04997dd267a3b8d | 78aabe48b1a90fe7c4c59bf16395c109016a188f |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
