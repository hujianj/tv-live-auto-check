# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2141256
Unique payload blob bytes: 1541519
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 503292

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 167764 | d61dd2659762a2829d941dfa3d064667ab6883b10f5db5e52053fc6a4df39d3d | 9d817e65d17a1a610cf9c546e64722eae68966c4 |
| live.txt | 167764 | d61dd2659762a2829d941dfa3d064667ab6883b10f5db5e52053fc6a4df39d3d | 9d817e65d17a1a610cf9c546e64722eae68966c4 |
| live-verified.txt | 167764 | d61dd2659762a2829d941dfa3d064667ab6883b10f5db5e52053fc6a4df39d3d | 9d817e65d17a1a610cf9c546e64722eae68966c4 |
| ku9-live.txt | 167764 | d61dd2659762a2829d941dfa3d064667ab6883b10f5db5e52053fc6a4df39d3d | 9d817e65d17a1a610cf9c546e64722eae68966c4 |
| live.m3u | 301277 | 2a69914dc0c6a92a1e689104a371fc7f70025b01b6c673f7a5c856638d3b2a44 | da520b85eb596d99f7d9c6a3bde55585c27c3ec1 |
| ku9-family.txt | 89886 | 03e43cfd1f593410613ffd2e38c15bc04ee8895ca0aaa5c9648433bed3d35eec | 87caceec2ee50bcbd462e9bfc69cd4f5adfea035 |
| live-family.txt | 89886 | 03e43cfd1f593410613ffd2e38c15bc04ee8895ca0aaa5c9648433bed3d35eec | 87caceec2ee50bcbd462e9bfc69cd4f5adfea035 |
| family.m3u | 160344 | 330b89688abfe93df7e005c1c97cfbaa9523e93b34d6a90d21fb0a86258485c3 | 0f106b19afb8ffd1f7e29f975b88ad83c5670f55 |
| stability-history.tsv | 754649 | 56257bfcb5da4f97d368c0a8b6840ea38056e854b139a09490a4b133c362b17f | e1746d370fb470b623bc6a340ca06b5f356457e7 |
| final-publish-report.md | 11686 | 87fb8bc8f76d1319cabcc92493fca7d63e1b38f28bef803aadbce6d278313000 | 6633358366eafc5eff64169b620f69ad0cc512dc |
| stability-report.md | 12273 | 8e49db437bcd781c2e17babfd9a911aa83ad6c7ef208e77617d21d3e69db3c41 | 06438d4856de5c2407e7bbb26260eb7227f90ebb |
| coverage-report.md | 1291 | 3ea3e6e66a92d7ed4f3ee0ba894d6c5766b04b950941bd0c9fcd29a582194dd2 | c8a7c535830106ce92b530ff0fa8b569b4b5fb50 |
| quality-audit-report.md | 2065 | f48af358bb1f5ca206b10f29720db3a25f76bf5f0be4799c343ab2c58ba924b2 | a660d3ec977755da9660b16307c19fa8de868699 |
| publish-guard-report.md | 1143 | 0f4423df92d7539dc5dd3dc58caf27bfca132ebefa30c28896f787898fc4ce59 | 170b274937cfb47169f41944568fb39557682ecf |
| published-recheck-report.md | 26059 | 199294a37d2ae86115728b597a46f29acff3ff7655b0ac782721474be5824b1d | d94f1ac1a97c2815e9c8cdad42bbae2a13038f80 |
| source-report.md | 6559 | 84b59244cbffadac98b5fcbfb51c4f7e00009c5e4e0f08da410fa1f44df16f7a | f39c5a7a30a9b97994bbdd42d0811473d1787155 |
| check-report.md | 6559 | 84b59244cbffadac98b5fcbfb51c4f7e00009c5e4e0f08da410fa1f44df16f7a | f39c5a7a30a9b97994bbdd42d0811473d1787155 |
| curated-report.md | 3383 | d41565a0ac65b446aa60306fe44d617a59535b4194ab41cbb5f53c5a51e73aff | e24bdc1d92b47a353c603d0e83c6fe49f2f476b4 |
| sources_status.csv | 3140 | eb2c6ee73037b9ff154d522c8a7ca19a20fdd8c22ac48566eb161c551da9b92a | a4b227c8319423d5f319c9949ef2442b68e4d8b2 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
