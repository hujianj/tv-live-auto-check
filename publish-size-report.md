# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 309568
Unique payload blob bytes: 251767
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 33314

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 16657 | 45540d8f27974098ab0f09391c2f2a869bb1d0f88e2ff443b318e30d7315601d | cf6901f9a926ffcf3879b9c0c3ec487401ff558b |
| live.txt | 16657 | 45540d8f27974098ab0f09391c2f2a869bb1d0f88e2ff443b318e30d7315601d | cf6901f9a926ffcf3879b9c0c3ec487401ff558b |
| live-verified.txt | 16657 | 45540d8f27974098ab0f09391c2f2a869bb1d0f88e2ff443b318e30d7315601d | cf6901f9a926ffcf3879b9c0c3ec487401ff558b |
| ku9-live.txt | 20181 | 85bb177aeb7d563b8129ff3506ffb357e6b68cb4e424e3fc347f40df5b3422af | 0996cbf324dc344cadc03d8739f0b8abdc337a1d |
| live.m3u | 32018 | 744a84973b1866e71cb7647198365bfd668b18f0cbcf480fc7c165d5a4fdd308 | 6442c325e361e85d7023c198862719f40bed0815 |
| ku9-family.txt | 16379 | 44ebaf588c15e764ebfc35b980ac4bbed404ed0825f790b3bf2faf208eb1a1e8 | 52f4b92c4b2292bec6ee4841746956430655e675 |
| live-family.txt | 16379 | 44ebaf588c15e764ebfc35b980ac4bbed404ed0825f790b3bf2faf208eb1a1e8 | 52f4b92c4b2292bec6ee4841746956430655e675 |
| family.m3u | 31492 | 902ec2f829c77bbc2d60da77519a3c6fac552047a659c507400e11cd6ac067da | c32d51902cefe201580688dcb5bdec7dbbacc12e |
| final-publish-report.md | 10947 | 900c91ae778ece3e2d035b4177560df8c8e8d9d247211cb71e1ffcbbc6848644 | c965c151b0047cf06a361525b4ba4a6b7bb99662 |
| coverage-report.md | 2205 | 582ae7246be1a57e3e54f7e88f811943f8c02e2d4a0b8c187ab01f07089f5017 | 49c56d2a4cdca57f599fcd80f5ce62c21c0d729c |
| quality-audit-report.md | 4671 | c37ab5129555a048b3c7c4c0f474337545af0a8efaf4abe3500bcd1cc044bd48 | 5443fa327fad8cc2c988f2f07a2dbb996d051107 |
| publish-guard-report.md | 1565 | 30eb8db8ed77671a01a925303b3e1f71eec285ff3abf858ba89ed6d253036cb5 | 31575abb674818a0d8403dd3a6d729b9263e003e |
| published-recheck-report.md | 29234 | 260935a3340093f73389318be95e573a14a9a4218e1b555302c0c87073fea448 | 51297685d7cebb3d27f4bd778819673eaa25d5b3 |
| source-report.md | 8108 | fb20f9db2bc082ca5a4d5981a16297ef888e84d8464ed4b5e05b0fb6330862cf | 311bc5fb318ef77cd93f07e61b6049ce8b18c887 |
| check-report.md | 8108 | fb20f9db2bc082ca5a4d5981a16297ef888e84d8464ed4b5e05b0fb6330862cf | 311bc5fb318ef77cd93f07e61b6049ce8b18c887 |
| curated-report.md | 1833 | a93b9a6e993b4f54fb3bc99894c4412f15a34d30deaf5a7c6bf4d226415a66d2 | 66cdc7ef004e9b78e2047c0ba1a44d5c633d3ee7 |
| sources_status.csv | 4180 | 454d01b384a6a0a75f8f8fb2f9fb020c2d92bdee18db387a7d08e87a8a243803 | 61b1d1e5c0fcc6e0e318794d0f8b74b2861f1705 |
| tv-coverage.m3u | 45659 | ec8090bae676ee6791bbb71484fe4e2a43e5d4bc0c6ed313a52265cedd441a37 | b1d1aa059b5e2372af2b8405aaa32a45c0e2d136 |
| tv-review-report.json | 16994 | 78e7ac6700d0c19599c5f0570fe5650d2b2a9e3e44eea2f927f19e167df77f58 | bcf08fd260fc3779d21855c024a3d1ad53e2d9ac |
| tv-review-report.md | 9644 | b51a1ee910cd54fea3b259be6ecc425fe5c660fc26fb761a5f0c17567b996a5f | 23ed6f1c2adaf654e77f3e3dce444c83e1e909d0 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
