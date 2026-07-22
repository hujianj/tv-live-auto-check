# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2456728
Unique payload blob bytes: 1707445
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 646776

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 215592 | 3f2fc78893ffbd16e72f2affa78e4cfba109d4d881b88a1f6b84aaebb64144e7 | c4590c1614db10323c48120551297f7a4c4f3bba |
| live.txt | 215592 | 3f2fc78893ffbd16e72f2affa78e4cfba109d4d881b88a1f6b84aaebb64144e7 | c4590c1614db10323c48120551297f7a4c4f3bba |
| live-verified.txt | 215592 | 3f2fc78893ffbd16e72f2affa78e4cfba109d4d881b88a1f6b84aaebb64144e7 | c4590c1614db10323c48120551297f7a4c4f3bba |
| ku9-live.txt | 215592 | 3f2fc78893ffbd16e72f2affa78e4cfba109d4d881b88a1f6b84aaebb64144e7 | c4590c1614db10323c48120551297f7a4c4f3bba |
| live.m3u | 385603 | 45839c9a73772e5ceba7cf0458a862f5748e9d01a916ac45c48df55170b54d02 | 0451ef06d3e3627c32d3cffb0a0577773d77e148 |
| ku9-family.txt | 96665 | 837d5b005cd582d2e95fb0edb2479a54c26a9da7c51a03c90fcb9e6051ff227e | 7d9c6f56d54242171f7d55dfce89af827507dea1 |
| live-family.txt | 96665 | 837d5b005cd582d2e95fb0edb2479a54c26a9da7c51a03c90fcb9e6051ff227e | 7d9c6f56d54242171f7d55dfce89af827507dea1 |
| family.m3u | 174611 | c34914f8bc45cdc03e9fb7343d7e1d6d2be1aace3bd2bc4e06b56c7cc60fbe60 | a560b3521c67ec1ec377d4551d193ed9068b1585 |
| stability-history.tsv | 772568 | 95b4d55074d07063772d61212496bc08eba8b83dbbfab4e3140092d0587315fd | 8cd534518a30944ca15116204acbe6785c0ec0ac |
| final-publish-report.md | 11830 | 3beb4854e864fa39edd215c764687174e49e2446310529e67bd82f018d025efc | 57c2a78ead63635b7b35c892677047cbb53198fb |
| stability-report.md | 10375 | 02a008533b5d07d27944da07eeeea52f3882d54a9c06bad2b58e0210fc98d5ba | 0081ee54c5c833c5af163e31ce3e906ae68ff0bb |
| coverage-report.md | 1329 | 0bee7b1a333434aed668549cbabba8b35a73e321b83958ba5e15b2a607dc9050 | 1837bf7e8d96397ebde22b12a95f1dab5588855a |
| quality-audit-report.md | 1435 | 185cb2ec30fe1bcfd07827fd5f1466c3c921e41e1d12339fe371a5cefdfe4b4b | 5ffe835e99a4b07c5685c9ab3754f025d8a9bfa3 |
| publish-guard-report.md | 790 | 04a3e086a74c9359dfb95a4f4e6bc3f75a01227892babd64844c5acf36d13fcc | 1bc8851a3b2260e90a54e9943d069bb709bdc98f |
| published-recheck-report.md | 24590 | 2d810b836134395e14f608a0274b88deb947f0f736bb344b72fe9a0fd7981133 | 8a21b0a6071c7b28cbb35cf3adf980feebb41694 |
| source-report.md | 5842 | 299989c3ad34a3e6c0afe07958758adefc2c2f4307ceb400c4ffd7579b25e9fa | db20e07d8d3b38701dfd72821d50b94af77a227f |
| check-report.md | 5842 | 299989c3ad34a3e6c0afe07958758adefc2c2f4307ceb400c4ffd7579b25e9fa | db20e07d8d3b38701dfd72821d50b94af77a227f |
| curated-report.md | 3613 | 52f9945b8d81862bb0f1319cacc36b59d5116827a0e56405027c7004e0e41ba4 | e41f6fab40653bedb7550b3bde86a3f52204588e |
| sources_status.csv | 2602 | 35227fe0bd17e222a8a65a9bfb744ec2046801a16b06377d5f85160b4c811c61 | f8bd99ff2dfc17bfe8cbac65681469308f1247a6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
