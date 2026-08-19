# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2006750
Unique payload blob bytes: 1452579
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 462927

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 154309 | 80d11f5b2efe9c830e5677446ca2ba99ca07dc204e71878dabab18171b1dfdd5 | 31a51d9dc6733a43a4995c91594919a04c9c0a1b |
| live.txt | 154309 | 80d11f5b2efe9c830e5677446ca2ba99ca07dc204e71878dabab18171b1dfdd5 | 31a51d9dc6733a43a4995c91594919a04c9c0a1b |
| live-verified.txt | 154309 | 80d11f5b2efe9c830e5677446ca2ba99ca07dc204e71878dabab18171b1dfdd5 | 31a51d9dc6733a43a4995c91594919a04c9c0a1b |
| ku9-live.txt | 154309 | 80d11f5b2efe9c830e5677446ca2ba99ca07dc204e71878dabab18171b1dfdd5 | 31a51d9dc6733a43a4995c91594919a04c9c0a1b |
| live.m3u | 277594 | 518b761b7fa2218648d1fa75c24c8d450b1220b6bd5315890cd654378d226fd4 | a3a0d3ea2067c865a6560c9e716f8d8b41ac18c5 |
| ku9-family.txt | 84684 | bd2ca4d4e9f0434dd51700ba59b77a7680678c4efff722616849513606d7b97c | db8201c75c7df4eee9bc29c29d3c9d430ca90846 |
| live-family.txt | 84684 | bd2ca4d4e9f0434dd51700ba59b77a7680678c4efff722616849513606d7b97c | db8201c75c7df4eee9bc29c29d3c9d430ca90846 |
| family.m3u | 150568 | 2ea281efb9cab2b83d78063664cbe6633bf3dddf8acaf4cd37e3845dc6566d6d | ecb32c08e175f1992f36e501542a187f5b82d4a3 |
| stability-history.tsv | 716592 | 8497136722b1e24a328370225e4af150f28039dd6816746c96ff42463b9d0ada | 4457e441fca29f7e57f09c7849410251c15a6854 |
| final-publish-report.md | 11767 | 246cfaa3b249767f0ed3584cb397d918fb7ae73881ad770a5a3cbd76a9eae3e4 | 5f7bbbfd33258491f6cacc2b237235a84949b5fe |
| stability-report.md | 11968 | bc87ba0ad0241ae63056a12dbd82bb8ca117d46cee509cad5326cde4a0e4b957 | d9c5f2aef70fc4de55b4094aa02d127cb540a547 |
| coverage-report.md | 1291 | 18f5ad4a9ffb0f64d2ee6a625540190e002078e1ff32aea9f696f2789fe53137 | 914e9af9ce53c181182a0cdf3cc6bbcfa7f0fff8 |
| quality-audit-report.md | 2063 | a46eec05994a1555137ade2ad06af75675392d246ac90d6bc5b552bb5553ade4 | 3c9fe68712e52d2c2b58974e5f799cb4a23f78ef |
| publish-guard-report.md | 1149 | bb7a9f2c303246b232e3421a456f661d66b6c50864e922f9bf9da9915e5ed795 | eebfcf9e6db4d8cb4f0984fd13512835dffc9e3c |
| published-recheck-report.md | 27555 | 6a9f2294c95cc59743169599493307dc55b6204fc3f3fb0e21174d59a5547e6d | 2cf7b17800234a41b0adf7f665ea8ede5bbd5b05 |
| source-report.md | 6560 | 4ed118edc4871779556e06ee6fb3190ad827c1518300bc2257eb8d11ddb2f67a | 6debb74b93d100e962da53ad6ed7b64d322d0b25 |
| check-report.md | 6560 | 4ed118edc4871779556e06ee6fb3190ad827c1518300bc2257eb8d11ddb2f67a | 6debb74b93d100e962da53ad6ed7b64d322d0b25 |
| curated-report.md | 3344 | 7198f9171e14124819ceea176f07486db8711dca4a4964fe7e281ad8b52cb147 | 1714ca01ba58329bede9f43dd4b2a7f8bd03acaf |
| sources_status.csv | 3135 | ffc0681c4fb374a311bb1bd3711b5612d64a2ed5e5d818e431c28c69e4494fe7 | 889fc934d10f106a801281f8887276f8bef0d827 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
