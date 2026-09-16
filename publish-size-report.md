# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 301220
Unique payload blob bytes: 198890
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 71007

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23669 | 3f4cfc0e7312a9ed0d8e5ad4c7747a390c153b71562908abf5a1af5e5021d56b | 18be23ef482f4538e87aa1315e0cd7d6d1af964c |
| live.txt | 23669 | 3f4cfc0e7312a9ed0d8e5ad4c7747a390c153b71562908abf5a1af5e5021d56b | 18be23ef482f4538e87aa1315e0cd7d6d1af964c |
| live-verified.txt | 23669 | 3f4cfc0e7312a9ed0d8e5ad4c7747a390c153b71562908abf5a1af5e5021d56b | 18be23ef482f4538e87aa1315e0cd7d6d1af964c |
| ku9-live.txt | 23669 | 3f4cfc0e7312a9ed0d8e5ad4c7747a390c153b71562908abf5a1af5e5021d56b | 18be23ef482f4538e87aa1315e0cd7d6d1af964c |
| live.m3u | 45221 | 09b5e35eaf20409048c15d1ba7813767c8084649317c51dca3bf50c030cae72d | 56d71b40d5bd987af21704c94643c8dff8af9c1e |
| ku9-family.txt | 23240 | 3121108a26ff754e13a98fdcd1d72ab302c85d74da7c71b14829323911276e0d | 85a720313f505630a9e18f9691a75abc86ac3df9 |
| live-family.txt | 23240 | 3121108a26ff754e13a98fdcd1d72ab302c85d74da7c71b14829323911276e0d | 85a720313f505630a9e18f9691a75abc86ac3df9 |
| family.m3u | 44420 | eca7bb42da09e6b930893af490f708766654efa2536ec75d46bbeafc1209e726 | 32e4c55f1630372ee0612adfd9363bfe2bc1baed |
| final-publish-report.md | 10800 | f121cfa29b348e79611965cf7db683926fe32ddfc87b37a50d8f8c6cdbab9244 | 66f13ed65d05ac4bc2a1c7463f71f7b9b9ae4ef4 |
| coverage-report.md | 2220 | 7305d79f4e437679df3763ded4ac57ec390554bf02a1abb47174c7a0b2358d36 | a7ca41c87a68268356b0ed30a930f50bf6672f08 |
| quality-audit-report.md | 4718 | d138f5090c3d6f9b363b786646aaf8167207d0038e3d6b085d102588b5757bdb | df0a87906231f0af5cc99bff36e4835d1688546c |
| publish-guard-report.md | 1567 | 9da9e9d3ec6406f2eace2a17aeecee9e8edfb6f98e242fdecb675d95536399f7 | 03d9a67f43967bed6910160d4d1ed98abff68d2e |
| published-recheck-report.md | 28952 | bb2de3ffaf84f034ddb7f1417fcfd0d5a6cfdc8613500ec9424d9c73ffd685b8 | 2467512ecee324a79ac7f11a393a946df5cf0251 |
| source-report.md | 8083 | 2c70f40e2354b0286e1c9b115499ef05f7ce5e6b6f42e5bb079c81e1536bcec0 | abf02b33399e06883bc965a05fd1e9352636c209 |
| check-report.md | 8083 | 2c70f40e2354b0286e1c9b115499ef05f7ce5e6b6f42e5bb079c81e1536bcec0 | abf02b33399e06883bc965a05fd1e9352636c209 |
| curated-report.md | 1861 | a6127a5972d79256d8414d50ddf5a619f3a0f38411919fbf8a06391508475356 | 904fa3840da5f75e09de66b5f3e833bf7ed43af1 |
| sources_status.csv | 4139 | 366e61cad81c86ac51a36eaa8296c53ce8a8f2fbc15761ba0baf5f73e4cfe0ab | 008914b6c286c28a869a9f81e5eff569b12f7784 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
