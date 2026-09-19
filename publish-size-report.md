# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 309624
Unique payload blob bytes: 203772
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 73686

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24562 | 7efc620fbdc3ce64ab05eaffcc6a71e6a681b98c130303b8481eb8da1f811b9c | 0580ad8ab765ed21e1d82e3c7e1a3ae1d3158349 |
| live.txt | 24562 | 7efc620fbdc3ce64ab05eaffcc6a71e6a681b98c130303b8481eb8da1f811b9c | 0580ad8ab765ed21e1d82e3c7e1a3ae1d3158349 |
| live-verified.txt | 24562 | 7efc620fbdc3ce64ab05eaffcc6a71e6a681b98c130303b8481eb8da1f811b9c | 0580ad8ab765ed21e1d82e3c7e1a3ae1d3158349 |
| ku9-live.txt | 24562 | 7efc620fbdc3ce64ab05eaffcc6a71e6a681b98c130303b8481eb8da1f811b9c | 0580ad8ab765ed21e1d82e3c7e1a3ae1d3158349 |
| live.m3u | 46851 | 6bf66cab88fc05958a7232edfb6dcffb9cc315f0f146b1ddfe455d5d3a30f85e | e6933ad1a4df83357b28de1333316687311476b8 |
| ku9-family.txt | 24139 | 57d7744e04831271b9164da1335ffc0e8a11a19f238822933af60f18cfe7f371 | f70e9659d26dc4c82f47e44984c2bb01f72af10b |
| live-family.txt | 24139 | 57d7744e04831271b9164da1335ffc0e8a11a19f238822933af60f18cfe7f371 | f70e9659d26dc4c82f47e44984c2bb01f72af10b |
| family.m3u | 46056 | a00cc24f5087ff108ceb2ad80366e2115350b59617a25cb390047379c97a8fe7 | 6738b33da6485864de3827ed4fc397343ba5c80e |
| final-publish-report.md | 10703 | 8d725d87bb7ba145683b7e58efc66e476f0b83605f880caefef424be8068af36 | 77036ec33fe6eab3c223b9583f00389acfb724d6 |
| coverage-report.md | 2220 | a6531e157c5f17edc7b0be3b1b319e9c162078728ab19a87ab19d07f26c2c10e | eaadf19cd99cb0d70f799ffb467bd020ab4f6af9 |
| quality-audit-report.md | 4718 | 55fcd00f3cc97bbc38dba75488c5318bfaf69b6db3fc590026b2ac15bbe2fbbf | 9f0eaa43d3f31de51c3d0267e868590518d5380d |
| publish-guard-report.md | 1534 | 5d7017916925581da5f1ddf88bebadb68e46d1da2655274b78eef554ac067892 | eed634d79d70a00d3f9c9a11210bec7a54340f48 |
| published-recheck-report.md | 29078 | 0d0f6ab214dc759e15cbb832185361cc671f91c866fa7d002ddf5cd7bd4e5fdc | e5f86a33923b9126feab96dc8f452ada4ee2a7f2 |
| source-report.md | 8027 | 800fe82a8c0fc61f8809bb7efaf48f60390c8e595f7aeb1e81c46a2341dc6669 | 8ca0ac0acc84017d1167123fd2c5379d0274b235 |
| check-report.md | 8027 | 800fe82a8c0fc61f8809bb7efaf48f60390c8e595f7aeb1e81c46a2341dc6669 | 8ca0ac0acc84017d1167123fd2c5379d0274b235 |
| curated-report.md | 1805 | 886de5ecac172ea9219be9ce35df4a50ba2b6a9dc2be7c96991cfab85d465478 | 7a397056b0d1d1a7be50dd3445136e5ad3cf7317 |
| sources_status.csv | 4079 | d5e162480e2637d3b11b65074bdd0f51024ed285b1ac8b88590b348f440a2e10 | 6c3cfc5359d41cc258961cda86210bb277e53544 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
