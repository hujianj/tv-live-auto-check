# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 305465
Unique payload blob bytes: 201506
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72216

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24072 | 7d1123fa490e0476c1dae38381418aaadb2c274c5f0bcb0e766125f9a1b1b154 | 8fcf4933cd3ed05ba39381aa3ca24150257ca6bb |
| live.txt | 24072 | 7d1123fa490e0476c1dae38381418aaadb2c274c5f0bcb0e766125f9a1b1b154 | 8fcf4933cd3ed05ba39381aa3ca24150257ca6bb |
| live-verified.txt | 24072 | 7d1123fa490e0476c1dae38381418aaadb2c274c5f0bcb0e766125f9a1b1b154 | 8fcf4933cd3ed05ba39381aa3ca24150257ca6bb |
| ku9-live.txt | 24072 | 7d1123fa490e0476c1dae38381418aaadb2c274c5f0bcb0e766125f9a1b1b154 | 8fcf4933cd3ed05ba39381aa3ca24150257ca6bb |
| live.m3u | 46059 | e3b32358387d64d2804492f27dba035529b35f39b6f6b7063b88ac1aeced717a | e2832ddf8e2aa719a7c0af417179853633a999a9 |
| ku9-family.txt | 23718 | 297514e5981ca9a7d8251dc7197ca5b2b1a09ffb46a4e4057a0522286d467913 | 52f2f8e0812d2c83f9f664ada4e9285cea5fdcf0 |
| live-family.txt | 23718 | 297514e5981ca9a7d8251dc7197ca5b2b1a09ffb46a4e4057a0522286d467913 | 52f2f8e0812d2c83f9f664ada4e9285cea5fdcf0 |
| family.m3u | 45395 | 2c64f971b39fb2cb74c718cd393c9b1ab1048b700276414998efe701e7229770 | 9fc4b89f68f0d1412180a36bde6d567a7de41b20 |
| final-publish-report.md | 10673 | 83da1eb7e182d4153682193ff8c9a7fe0436ba0f3bbdb2373783088edbd4f444 | 8d3effe8289c97ccdde2a55b553e491de530989a |
| coverage-report.md | 2230 | 9c84379ad820c50b8715a09e2da88188df3b63ea74e760d5ea6ce6806e293d0a | 561f2067c382556946cecef0d859d1292841c272 |
| quality-audit-report.md | 4728 | 42623ab78ed43c75d44970520b99efa1d833480a5619b80e1f7bca486f97d6fd | d30e788191da1da5901d0870c944350c144ec4d1 |
| publish-guard-report.md | 1587 | a71a8326356e100c3bbde5ead48c83a668cc0fd6785a0ca98507ad2d6947b7f9 | 35769e57ef708cd217a2aefeecbb2c3a54bb9d59 |
| published-recheck-report.md | 29143 | 2c2e695c18ef722429e0eb709741a25d220161ca697a8c459d06e23e83bffef2 | 23a291a7e8ff876fc632d937f2437dcbf6a87606 |
| source-report.md | 8025 | 5f8f334fd9b800e8fb4968702dbe5f81f2dd864326d98c30d5313255d9b48099 | 209cbc8261ad11916317f9924218a555f426cf0b |
| check-report.md | 8025 | 5f8f334fd9b800e8fb4968702dbe5f81f2dd864326d98c30d5313255d9b48099 | 209cbc8261ad11916317f9924218a555f426cf0b |
| curated-report.md | 1804 | e5e5cfad968ec7875907ff2d4b6d9fc426730250d1d08f416de17ec9f3c46fc4 | 3b40862edf5183b5db69dd2228df4c16c22a6124 |
| sources_status.csv | 4072 | 6bad56c0162ac504ba69c3dc96e4f44a39d9f4efcdad6be3ccb2d6cf9146f6b9 | 2c88a603fa29878d7d2222c4f74bd9976e6ac8fb |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
