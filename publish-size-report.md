# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2371365
Unique payload blob bytes: 1639883
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 627804

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 209268 | d9302e14b70bf1b6aa70026d4361b604e228a262b2bd24690a87da80fed98b3d | b349210b02fc53f1abb6181940efb7d3167abdc9 |
| live.txt | 209268 | d9302e14b70bf1b6aa70026d4361b604e228a262b2bd24690a87da80fed98b3d | b349210b02fc53f1abb6181940efb7d3167abdc9 |
| live-verified.txt | 209268 | d9302e14b70bf1b6aa70026d4361b604e228a262b2bd24690a87da80fed98b3d | b349210b02fc53f1abb6181940efb7d3167abdc9 |
| ku9-live.txt | 209268 | d9302e14b70bf1b6aa70026d4361b604e228a262b2bd24690a87da80fed98b3d | b349210b02fc53f1abb6181940efb7d3167abdc9 |
| live.m3u | 377159 | 2bedadb2f77635361f03000c54ff2a0ad4d3e5d8499a7aa9ba8bde07a7a1f5ba | 6a10b4929554f29f74f4f48ccc53ffad70a13fea |
| ku9-family.txt | 97780 | 215370b72c2a5b33465167aa6cc6d9bd83f5d7edeb043abbe0adf68e8a47942b | 0b26ee2b5919e256e22398aa71823e8c66da7587 |
| live-family.txt | 97780 | 215370b72c2a5b33465167aa6cc6d9bd83f5d7edeb043abbe0adf68e8a47942b | 0b26ee2b5919e256e22398aa71823e8c66da7587 |
| family.m3u | 177426 | 74608991ca78253aed925b250f945b3e2d8980e4fd10e7cf7e2b676d4c4dc076 | 00e35937293564e0768f2acbcc38978315907b18 |
| stability-history.tsv | 708614 | ab63985ad24fdc88d8fc30639a59ddce43452352c89c7937e37cdae4e6cfd3eb | a60142bcf92d9013a0c2c147e1e4d3685ff9a4d7 |
| final-publish-report.md | 11689 | 2cb21cd3dc2690996f5820ace5d9b910a182ebced64ce0c35ecbf859539aeeef | de664e4aa2e9eafd9292dfc67cc897fdb08e560a |
| stability-report.md | 12467 | 814faf3020fa4ef2e22ec28ca9154d12511b71614a090f56c759fda544a946ba | e83358904789b242819eb2260c6b62f4c6a6e005 |
| coverage-report.md | 1291 | 1038f740ec5d63bbe590c138b2fc668e37d638e9b11b29ec38988b18acf4a675 | 1e66c9232ff70ba90a972ff1ef7f2a7337fe3ee6 |
| quality-audit-report.md | 2178 | 6eec28429c075e3f94a13da5ab8c4ae5a4dc2e18d08cec03d18795fc29a46df9 | bca0207a0d59d29481e153e665ca9f5983c697ef |
| publish-guard-report.md | 858 | 3e14361c64de0685ac5a43b4ed9a165e5a7ca1724bbeb4732abb5f0bdfd49303 | a3314948c186ca94e99bb1d9355ebef921baaa0d |
| published-recheck-report.md | 29106 | 48622e570accb34ffac53f4e4ce908b33670b047d5a205779207d0ad936f823d | 7ca0da77ea91e361dd27cdb831bd768b23431ad1 |
| source-report.md | 5898 | 85aa0cbeca0b9e0f8468b35adbdc92712cf6aff754957de5b7c429074e8a8748 | a259a002984f4b332bc3dde465b7d1cc64cdbb49 |
| check-report.md | 5898 | 85aa0cbeca0b9e0f8468b35adbdc92712cf6aff754957de5b7c429074e8a8748 | a259a002984f4b332bc3dde465b7d1cc64cdbb49 |
| curated-report.md | 3493 | 7a96b49706ff88acce85d41aa4ec4b7b68e2d701fc6b70a322d4e970cbb72ec4 | 57d16a7f8f6f751b643c4e035eb51385e8e98a7f |
| sources_status.csv | 2656 | 87b06be9f51e3b0065e7d06d904ee8a37877767c1096cbac0c00730cf22a9e23 | c5614ab1b15854daa112466656256c160deb0ecf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
