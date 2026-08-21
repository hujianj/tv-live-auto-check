# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2037347
Unique payload blob bytes: 1469303
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 477354

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 159118 | d9bcb380e48d56b09d758e0e450efbcfa364d2a7c6048293987136b657db4289 | dde134e0b3408e95d99f9d3609dcb8b6d75cd5f4 |
| live.txt | 159118 | d9bcb380e48d56b09d758e0e450efbcfa364d2a7c6048293987136b657db4289 | dde134e0b3408e95d99f9d3609dcb8b6d75cd5f4 |
| live-verified.txt | 159118 | d9bcb380e48d56b09d758e0e450efbcfa364d2a7c6048293987136b657db4289 | dde134e0b3408e95d99f9d3609dcb8b6d75cd5f4 |
| ku9-live.txt | 159118 | d9bcb380e48d56b09d758e0e450efbcfa364d2a7c6048293987136b657db4289 | dde134e0b3408e95d99f9d3609dcb8b6d75cd5f4 |
| live.m3u | 284993 | 9b20a668d59e2657751ff9ee3ffae9fd3e32c79f2a2f709f136f36fa60f714c9 | 00f4ef8d4fbc8e1dd858c627d819292b828b3259 |
| ku9-family.txt | 84062 | c2ddf69d1097abe983f9d2bd1c22683f0440ca08880ca973fe14e6720e5e6dd9 | 7e3adf3a2ed178bb40682c3cfe284ab419b8184b |
| live-family.txt | 84062 | c2ddf69d1097abe983f9d2bd1c22683f0440ca08880ca973fe14e6720e5e6dd9 | 7e3adf3a2ed178bb40682c3cfe284ab419b8184b |
| family.m3u | 149629 | 157e38e25a446dce668dba7b6aff4447c912a572f0bc206506d9be2d77e47dfb | 49e3544f1bd249500d217b567cd82ea445603ea6 |
| stability-history.tsv | 722722 | 5b3e5190d60d617a3637506bb9e010c75b25a1b210384263c6a62abcd520ebbf | c68d62d0832febaa7eb56743fd1b753d8b4f0583 |
| final-publish-report.md | 11858 | c1d57de360c869805873182065b683fbc0ee80a84d60301abcf4a997c6831259 | 7debb10313967efb6ead9d219110f56766b6821e |
| stability-report.md | 11842 | 896fe544d1079acdbbce98a50a2fe8e9e63f438115e5126de421b318f728042f | 99769e6c3f7ac07c6a19c15f78230e603fc995ed |
| coverage-report.md | 1291 | 89a4512f4950f006e60c2e42c1f0115e30b9f3ffc146f3f0e659781a988c1f00 | a8f39dd75b36ed851447f1d2f8323abc20c8730e |
| quality-audit-report.md | 2062 | 3c37c3547622711fc3838ef09d14ea12120d55b60beca289ed48a99aa78aa5ce | 504824160bff76497be9373434f07bb371efa77a |
| publish-guard-report.md | 1146 | 03ba5e8a3d5f71e6659533617111d7a42198d52ad59cbe4303534f98631a12ac | 77f8c5877b5bd5c390191fc5932de9fd3a022597 |
| published-recheck-report.md | 27436 | 6e3082ff50f25e915ae3443b985a5a57b9af89a325a3ba5028dddb08da2114ec | c51c6b31fa387c3a3b8d24a04ab4d64c4efc55e5 |
| source-report.md | 6628 | d6791b96ec7eac2d56afe3bcacec60f232e3270de384d19ef44a0f2cfe8d672f | a0f2e21055346a6f69397e766e8aea576f829e78 |
| check-report.md | 6628 | d6791b96ec7eac2d56afe3bcacec60f232e3270de384d19ef44a0f2cfe8d672f | a0f2e21055346a6f69397e766e8aea576f829e78 |
| curated-report.md | 3381 | 1209bf34596d242c9c6006b9c2b5a73a3bf953d29499ebb8c135f33ea21c229a | 1f2f3fa9ac4a2ea09d10d3fa95ee96b341dcd67e |
| sources_status.csv | 3135 | 20b6511b4ac36a10cd5af42c96e8359ab2670dd27f05b7eefdab2e68256c8972 | fa8d8fa7fcb52393d491eb380b605b6d2d11142a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
