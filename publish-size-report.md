# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 277851
Unique payload blob bytes: 184699
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63975

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21325 | eda714a5c41bc0428f97459a76ac8d4c7d413621a984f9ee0b46bdf47ae10096 | f8e60ede57f8e19a813ad9370df6405f03470ec4 |
| live.txt | 21325 | eda714a5c41bc0428f97459a76ac8d4c7d413621a984f9ee0b46bdf47ae10096 | f8e60ede57f8e19a813ad9370df6405f03470ec4 |
| live-verified.txt | 21325 | eda714a5c41bc0428f97459a76ac8d4c7d413621a984f9ee0b46bdf47ae10096 | f8e60ede57f8e19a813ad9370df6405f03470ec4 |
| ku9-live.txt | 21325 | eda714a5c41bc0428f97459a76ac8d4c7d413621a984f9ee0b46bdf47ae10096 | f8e60ede57f8e19a813ad9370df6405f03470ec4 |
| live.m3u | 41070 | 2a8192646adfc77fa2c23bd90bb57103a71d4dff533b330dccd48bc0be266090 | 89f27308873f768236b8ce7c02cb7af5edd1647d |
| ku9-family.txt | 21060 | 4f72ba1d8d8ea7566f2a6596095afec21f56d9d0f8c224d570476e371415725d | 55feccc56f754ef5063fa768b9482aa62b4a53c6 |
| live-family.txt | 21060 | 4f72ba1d8d8ea7566f2a6596095afec21f56d9d0f8c224d570476e371415725d | 55feccc56f754ef5063fa768b9482aa62b4a53c6 |
| family.m3u | 40557 | 60dd1fd8684b391d152b3dff587bdb802d146360a17d46ac57cd57c62b341286 | 31f09628ca7da6d4ef5bfdd0574037783fad321b |
| final-publish-report.md | 10759 | 3b2704af094148762201333e54dd3203521978f0c7883b2597c2d1a1c52f911f | 346eba67dfa661e145491bdecd7dc26b8560254f |
| coverage-report.md | 2235 | cdce9c54a6c8f141479f128c1ec9aad54ad1a51b601fd3f41684889c4d784ab4 | c82274f3f47ba04f6104dccec476d66ca4fe3638 |
| quality-audit-report.md | 4731 | dc099f5e5a0c5498a5e6259ce7d412469936e85a4736bde9b266c926dff81863 | 14d05e76cfc4f87b9f3b58ba812c49e5d4604b0f |
| publish-guard-report.md | 1609 | 68c412a524a88014af193d6865a6475133aeaedd76e3b9b40a906126343c57fc | 8bbd913b7d96e0d13e4f72e2c247e092eb72fd9e |
| published-recheck-report.md | 27300 | d0be82e211ec03d47d2b524b14d059a035064b5b7868d912f11a739e6e99bccc | 8a682968138b33fef2b64a1417837f2eb7d9e899 |
| source-report.md | 8117 | 2bd14eed1129e9b1430e494dd5bee8cb7aaaa8a21cb6a40cf73ec893c008f1ba | 02bafc1feb72c225e97d8e9e31b82922308683af |
| check-report.md | 8117 | 2bd14eed1129e9b1430e494dd5bee8cb7aaaa8a21cb6a40cf73ec893c008f1ba | 02bafc1feb72c225e97d8e9e31b82922308683af |
| curated-report.md | 1804 | 3df30872546ea7010354bc6d7e8eaef85f7b4d6f92408e5dfe1a725b750988f9 | 09b229b6e49a77cfd9367661caabe4c6d09e0d9a |
| sources_status.csv | 4132 | 070397a3a4e89e7866a06c00d03eaa6924612f90aebe710162fe2a2fce824fa0 | a4de19864ce170625cddadd7c558abf203ad9231 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
