# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 1978537
Unique payload blob bytes: 1430425
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 459723

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 153241 | ac7ed1ee933473f4a72b07dc446114c2fc43e35eb63399cba2f56c1c3ae85aa6 | 546afc6938406cb6daf49f0f3c0da9a535943a7f |
| live.txt | 153241 | ac7ed1ee933473f4a72b07dc446114c2fc43e35eb63399cba2f56c1c3ae85aa6 | 546afc6938406cb6daf49f0f3c0da9a535943a7f |
| live-verified.txt | 153241 | ac7ed1ee933473f4a72b07dc446114c2fc43e35eb63399cba2f56c1c3ae85aa6 | 546afc6938406cb6daf49f0f3c0da9a535943a7f |
| ku9-live.txt | 153241 | ac7ed1ee933473f4a72b07dc446114c2fc43e35eb63399cba2f56c1c3ae85aa6 | 546afc6938406cb6daf49f0f3c0da9a535943a7f |
| live.m3u | 273178 | da267faeede997c276af0d5aeeecfd34cec6c02b4fe1169c1000fdfe4715222b | 2766cc0e800a9f33ecfa74a75577b7591c20e6bd |
| ku9-family.txt | 81792 | d44fe4fafca99ca8e29e6594c1efaa1f7039e41f6b6dd6ee5cbd4f4baa6884b8 | a36398c2cca41d9fdb4f40e3313aac5771e8a8d7 |
| live-family.txt | 81792 | d44fe4fafca99ca8e29e6594c1efaa1f7039e41f6b6dd6ee5cbd4f4baa6884b8 | a36398c2cca41d9fdb4f40e3313aac5771e8a8d7 |
| family.m3u | 144782 | b2e7adbc5c99f08120da2ff6f57eaf605192b292088670a54cba2e164f7a9334 | d7d5da6af9091822b992febd3de7d3b681cc3e60 |
| stability-history.tsv | 709224 | 434b069eb4fefa9cca51918464bc67dbc6c6c4fe246ec5365044064c98f6dbd1 | fcedf6c14f77946a0810ca08c49b3d5d735821e9 |
| final-publish-report.md | 11671 | a8f28b8809e3cbcbf8af1b4694a1e163155c530d53655181ff04068f25730f7f | 8d6f7464f4ce1e1b0dd39c4713129fefa42d09f0 |
| stability-report.md | 11980 | a961ffcedef436e1ffaf62887d0ecd19e5753d372e44fd3723fac7509f6aea42 | 4844c12d7f4d258dab19096202c16f8eb37635f1 |
| coverage-report.md | 1291 | 48104a67aad0e7a6bbf3dafd45846a1be42a6a23d0ee135059cf18cb7e6b6bc6 | 58829769dfd5df57f2d7cf5d39c7ba652290b691 |
| quality-audit-report.md | 2159 | 1d7d021c95d5c1cce9a802bfa174c43dba9a354827506cf5184f96d3f693a408 | 61f12b2b2407a14a0746fd64cefab06d09c6f2e6 |
| publish-guard-report.md | 1158 | 2545e69abe8bed2d550385691358c7690180ca83cd00541ce62f3bc5c4272be4 | 207954decaa04c28933c199aabf030c7487ebbbd |
| published-recheck-report.md | 26856 | 7543f155cf7e587390bc260dd68869a66dd816f2dd536e8d68c2cc1dabb5429b | 3c5be710d42530b948d8ab8233907b9a7c2a2629 |
| source-report.md | 6597 | b29f9cd40ae7fe3762ce2535bbc731c446444cb2577740b8084ddde1a8a940d7 | eb00d80a89cc38d72438fef2cc0b31f9949bda22 |
| check-report.md | 6597 | b29f9cd40ae7fe3762ce2535bbc731c446444cb2577740b8084ddde1a8a940d7 | eb00d80a89cc38d72438fef2cc0b31f9949bda22 |
| curated-report.md | 3362 | ee992032d1722744b90f2936247ed854ef4997ddfd66c5e55f36ba416effaf49 | a627c813e3b065ee5db6de1299cda4ada12421ba |
| sources_status.csv | 3134 | afce4a02ebf21de11bdea059cfc089675580b020427fe5e1f4e4fbf0a4cb3393 | 8a06b5fc8a02c0862c87f2e8da74a21c5c6c0c04 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
