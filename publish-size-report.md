# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 293602
Unique payload blob bytes: 194298
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 68763

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22921 | 710fe7d0da011dc83ac95130091df31732a58d8a241b83d03aea47df05296b62 | 76ec228c95d11dd81a74711f059b8d1bbe8ed573 |
| live.txt | 22921 | 710fe7d0da011dc83ac95130091df31732a58d8a241b83d03aea47df05296b62 | 76ec228c95d11dd81a74711f059b8d1bbe8ed573 |
| live-verified.txt | 22921 | 710fe7d0da011dc83ac95130091df31732a58d8a241b83d03aea47df05296b62 | 76ec228c95d11dd81a74711f059b8d1bbe8ed573 |
| ku9-live.txt | 22921 | 710fe7d0da011dc83ac95130091df31732a58d8a241b83d03aea47df05296b62 | 76ec228c95d11dd81a74711f059b8d1bbe8ed573 |
| live.m3u | 43956 | 56346eb7aea4efaa5db945b98dbb6d4b6a96d957bfdba1fb202ed7c547e7c163 | 468e93b8fd81dda417e45664c6065c4c67a59f5e |
| ku9-family.txt | 22505 | e4630ac3ff8d0a131ffdb309389d08a141de285befd13f659f793974f5d5fd25 | f66d12b94a44b81a41d45f6c63be206d1a638bc6 |
| live-family.txt | 22505 | e4630ac3ff8d0a131ffdb309389d08a141de285befd13f659f793974f5d5fd25 | f66d12b94a44b81a41d45f6c63be206d1a638bc6 |
| family.m3u | 43168 | ee91754911e47a508df67c356115ceff96a72431a82c2b63592aeea431a3860f | f319f554eda549b0c79da5e8b7dee762f3f81957 |
| final-publish-report.md | 10748 | d48dd5bd814864b0ac6a417be3f9dc397f92094e75995d95d520fb37d8c0daa5 | 454f12e08eb70a8bb872c2aa404d63b1275ed51a |
| coverage-report.md | 2235 | 1e466d22d3f189c345abaa54fb8b9a37c8d21ecc2f4711e2a07eaf1c747f7fcf | 45faff79d1ae3f61616ae01e535f3c0f121e6201 |
| quality-audit-report.md | 4730 | 881ab79a74580cff06de0eab6f0c23ebe09e745fcdac41ad8efac6f027dd8ddb | 48636cb028a5f3f6b3eb6dc6335235c7c3ee8b18 |
| publish-guard-report.md | 1524 | aa1aa14f9d06a81631f8c72349ff9c6109113ae79f98eb6245acbac366606a55 | ccc2d99518834345bee4b65b90eefb9e958323ef |
| published-recheck-report.md | 28585 | ce97eea850731549f0fdbf4aee977edd7a4c99b4f90d5a409c1e470801f28820 | 7a1092660742559d431df70bad27c8dd8a5b7f0a |
| source-report.md | 8036 | 4d353401985deb123a9ca17d72a61517abfa4b6d3d3952db409706a376997d00 | f272c6d9ad82a5d195c523e110ae6bdb2523bb21 |
| check-report.md | 8036 | 4d353401985deb123a9ca17d72a61517abfa4b6d3d3952db409706a376997d00 | f272c6d9ad82a5d195c523e110ae6bdb2523bb21 |
| curated-report.md | 1806 | 52986da7ca5e3bd0ce7082b533fe951961b42b78edfd1700c2a4cbe707f4d966 | 258e664c770a73c301e6ab69376529b999b81c20 |
| sources_status.csv | 4084 | 9ac7f522a676e269d9b3626d39367480edb48bbb22d8212e02fde94dc3cc3050 | d73dc661b974b2b8ddac1c4f1e148eee516ac1f3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
