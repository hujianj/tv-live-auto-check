# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 315751
Unique payload blob bytes: 253447
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36370

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18185 | 0be4145f4063038e922fa50261580903b7ec679f827b56c9f82c01ce2cff0b2b | c1fa65219513bf66dd5470f3e0ed91ffb9649b70 |
| live.txt | 18185 | 0be4145f4063038e922fa50261580903b7ec679f827b56c9f82c01ce2cff0b2b | c1fa65219513bf66dd5470f3e0ed91ffb9649b70 |
| live-verified.txt | 18185 | 0be4145f4063038e922fa50261580903b7ec679f827b56c9f82c01ce2cff0b2b | c1fa65219513bf66dd5470f3e0ed91ffb9649b70 |
| ku9-live.txt | 20488 | f4c05524e700f052908c100ea01c8ba624338a5b60acedf16f08d8cb68be607b | 16113f84cbad09c91117f16e13d00a45556e463b |
| live.m3u | 34176 | e00f0373e5fd26c4176f8116881c72f7a514bf6a14ba781a6856d15d98773696 | 4e5ab4011202aa3d582216c4087eeff14b73a55c |
| ku9-family.txt | 17749 | 40026a9ee07e3c43bf8705f652efb209d639cb5a18fb604536ea49e73521d87a | dab243dc3a2f78dd3010453b86fe7eebbe54624b |
| live-family.txt | 17749 | 40026a9ee07e3c43bf8705f652efb209d639cb5a18fb604536ea49e73521d87a | dab243dc3a2f78dd3010453b86fe7eebbe54624b |
| family.m3u | 33368 | 6499bca1bd5941ac6e33802616a36023e55c248bfdea45e079d6be17ebaf632d | 8496ac218b702d40e47723290ba45431884d32c1 |
| final-publish-report.md | 11055 | 5227d86dd01c4f9a9dc39276fac2d739d1a8358d030e2e58d003b5989df20a3b | a1e2325abe115c7d8530818ce28400d3eb32f328 |
| coverage-report.md | 2200 | 55d22f4f5ab376a3683068089d9560322d28a32106682aa95868e3efa69c804b | af683c0503b0f97b091da09bb87428789e882512 |
| quality-audit-report.md | 4677 | d72be74e997400713770d0d7e74cf9a10dfefac55c3d92dad76dcd455ecab984 | 43bcc40c0568fc5e7987e176249c8ee1de607e5b |
| publish-guard-report.md | 1537 | fe179b322d978e41233f1f4dee08cdf2043c68b6a6d313dae3a6b3aefac8748e | fc9aeab77b09b88600c6d2dfc2582ca8f6338db3 |
| published-recheck-report.md | 31200 | 029274cb8f9557cc5db405eaa50b72c545fef16c3ed25cc371638128c0eba200 | 4164d850d609c63a9d546e079ef65e6f879bdf03 |
| source-report.md | 8185 | 48673e297f98b49e201872d13cae8fb716aa963d12fe9f62533b94e7bcde9f95 | c573ceb5be817ec80d2180dd99e8714f44d16ee3 |
| check-report.md | 8185 | 48673e297f98b49e201872d13cae8fb716aa963d12fe9f62533b94e7bcde9f95 | c573ceb5be817ec80d2180dd99e8714f44d16ee3 |
| curated-report.md | 1832 | 95a2b342c960c6614334f63b9478cd309496b77808816a3fa0977c1f7fae1953 | f2f616be552dd486744ad97d85a44dfc95258e40 |
| sources_status.csv | 4240 | c998ff2cf4f4d14321a47643a4947b42557bb9dd8e7cb32c50319f6349489fc4 | 704e6208d48007f6a43ff097642d2abe077b251a |
| tv-coverage.m3u | 45782 | d5810771a5e45de1ce132dc69aed46555bbc44434e54c18db266baa9b41890cd | 9612b5e1f167cf2fbcb945103d2100ccb2693abd |
| tv-review-report.json | 12184 | fb4e3c7c57208154fccae4ba1932638fabfa5ad3e561341250c6492dddea04b1 | 273da92c155df0438bd65daf233c2bacb7b80d98 |
| tv-review-report.md | 6589 | 6e3e5e3eaa9da72ce40e91eeb5f502a354a3cf2c3ca829936b5601a294dfdb1c | 9b7dbcdfc69c70201875cb49d47a46e68a42d7f2 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
