# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2018465
Unique payload blob bytes: 1459733
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 467532

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 155844 | 913e13ac2aaa73640db8cd36c895621e4966e735b6493917c90da39948c2659e | 48f1c117951e4af6313722ad35d615b12d3880ba |
| live.txt | 155844 | 913e13ac2aaa73640db8cd36c895621e4966e735b6493917c90da39948c2659e | 48f1c117951e4af6313722ad35d615b12d3880ba |
| live-verified.txt | 155844 | 913e13ac2aaa73640db8cd36c895621e4966e735b6493917c90da39948c2659e | 48f1c117951e4af6313722ad35d615b12d3880ba |
| ku9-live.txt | 155844 | 913e13ac2aaa73640db8cd36c895621e4966e735b6493917c90da39948c2659e | 48f1c117951e4af6313722ad35d615b12d3880ba |
| live.m3u | 282459 | 5432f84fe7aaa6c4efefa50f05a0bf7426fb96cdda87cced3cff816257d39ca8 | e66bfea03f0bb4c58ea3c90c65c129a78dc44948 |
| ku9-family.txt | 84371 | 049662be802635c7397dad935dda40f6959c6a636898d1037fafc1b5cdabeed7 | b055129595c1576e7494699c111754ee2d754109 |
| live-family.txt | 84371 | 049662be802635c7397dad935dda40f6959c6a636898d1037fafc1b5cdabeed7 | b055129595c1576e7494699c111754ee2d754109 |
| family.m3u | 151411 | ff8a45dfee680dab3598ecf553bd34741d8ded26d8cef3c6ba9e6ae117c3003b | a9bf444192d0bcf076c85ee6a9571ebaf60fe148 |
| stability-history.tsv | 716350 | 61098724d05dedc234592c3fe3212d195c2af60566897709af63e129392a4bf9 | 95d6e24034d835636256cf6b94a3fdc62b523f6b |
| final-publish-report.md | 11951 | d8fcf36b67148590d3d8eca9c6be380c9b7a0d2cc27e8fbbf41f0aa9fddcac70 | c02a13480a491f9620db77c7410b0d9b69c57a4d |
| stability-report.md | 12729 | ad91a1ace3f7fdf2718b54c36378c51f2070116483406cedc64980a5ec8e63c2 | b3d6e45f22b02f6d835199dc411143862dfcd432 |
| coverage-report.md | 1310 | fa241740f2227a67dbd514714b92223026caa8127a0ccb36d49b8d683629499f | ecc8a0b91e6b07802376e7cb63c32c742ca816be |
| quality-audit-report.md | 2067 | 12e8f4a0f043e8f84b8dacdfefd8f56842e6f73271ac544b8823221c1bae993e | 637c6a5dc314ee65cf76cb70235fef2162812d4f |
| publish-guard-report.md | 1164 | 750b57f7b3711ddc403596c51cdf8c37d90afc59fdc59fbccff6e8df2a3a0356 | 5631aa3caeff4ac628ae8936a512f506bbab45df |
| published-recheck-report.md | 26562 | 14680087d2fe479a324084cf6d796e4ef1ca1a7aa9324f74d205bf231e08e97c | dbc9841029cec4a66cf7b0eb50298e8b8894810c |
| source-report.md | 6829 | cb9c4cd6ee6451ce4ba00b506220277491a1f1102a736cb4353e5801251217c8 | 7644cf189ed1072837352223f5fccea3723c2d10 |
| check-report.md | 6829 | cb9c4cd6ee6451ce4ba00b506220277491a1f1102a736cb4353e5801251217c8 | 7644cf189ed1072837352223f5fccea3723c2d10 |
| curated-report.md | 3378 | d471423e6f8f75a0378a18657e58aaa3abdb132d087c617e3ed125a2002de6e3 | cae24138fba55fb51ec3c28373040ab01ea73b08 |
| sources_status.csv | 3308 | 96c3653b71db5fadaa846f23ca7dfe2a4af53c87592c6b4fe58b1adfb2ef58b7 | 78c6fe0b59576bebb30b7858bae256e0885cc44a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
