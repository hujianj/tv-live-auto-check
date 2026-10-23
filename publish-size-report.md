# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 291159
Unique payload blob bytes: 192879
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67962

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22654 | 9159dc81a633d96fa44c0d0b8afdabd4dcf88a2b372c4ec55b405ef109865d8f | aa6d893570c815b9b416249c2e8d133ad7d68bdf |
| live.txt | 22654 | 9159dc81a633d96fa44c0d0b8afdabd4dcf88a2b372c4ec55b405ef109865d8f | aa6d893570c815b9b416249c2e8d133ad7d68bdf |
| live-verified.txt | 22654 | 9159dc81a633d96fa44c0d0b8afdabd4dcf88a2b372c4ec55b405ef109865d8f | aa6d893570c815b9b416249c2e8d133ad7d68bdf |
| ku9-live.txt | 22654 | 9159dc81a633d96fa44c0d0b8afdabd4dcf88a2b372c4ec55b405ef109865d8f | aa6d893570c815b9b416249c2e8d133ad7d68bdf |
| live.m3u | 43195 | 8bc6c731ae829e1f937c30e6b8ff1afc876fdfc52982474e830b0dd2516bd441 | 0b6dae341bbf619bd72f0b9566cde892ee995f3d |
| ku9-family.txt | 22224 | ff3af43c4193298660d887ff885fcc4d86bf29fa9b23b8c03c4b4ee6fbaa6bed | 6d8577d771059e7e1322e23e3fc47865e55c7834 |
| live-family.txt | 22224 | ff3af43c4193298660d887ff885fcc4d86bf29fa9b23b8c03c4b4ee6fbaa6bed | 6d8577d771059e7e1322e23e3fc47865e55c7834 |
| family.m3u | 42393 | 703d235a57010bad69329222d2b97f05e3b28b2960363a2e89038d0cdce2faf9 | 4ce4befb8c1fbb61a0b7ebd2d3dc49187c52461d |
| final-publish-report.md | 11020 | 11a54d5a6c7c46d4eb113c67cc82a975059daad8a3c4f41512f027b526ffb3bf | 7606d2989a2ebecad68296e7027823a14fd21bd5 |
| coverage-report.md | 2255 | b39635cec1d923c96b008520cdf9f892fdf2f23043cdf7f33ad366bcd88259a0 | a252f80989c0b6977d1ce3312d5833542ac308b2 |
| quality-audit-report.md | 4747 | fcfb607f6b1bf3650b4b089b2aff167f06e25990d45398f74cb807ab6391985a | b037461354b3c7d4d1de242c3d922091141ee34e |
| publish-guard-report.md | 1673 | 09c7aba86b37112de4df5bdb8fb14cf930912c7723bf4c4ae2998378ceccfd66 | 047e310c6f50b68f6f1b4d7f5b641b205af7dc49 |
| published-recheck-report.md | 28674 | ec95c20953c2277c5e08285d4791af8fee4b858d409b7883e1b3d1661dbe1d5c | a0b2b2372205d482cb60619889704e231b638e98 |
| source-report.md | 8094 | 7bee58ddcec74a1fcc1c0aed5480fd3e942fc5477de5c6b6023513a75c0c9a42 | 55841d392d1ee8b90f46856a1f7565ae9e9006df |
| check-report.md | 8094 | 7bee58ddcec74a1fcc1c0aed5480fd3e942fc5477de5c6b6023513a75c0c9a42 | 55841d392d1ee8b90f46856a1f7565ae9e9006df |
| curated-report.md | 1806 | ece6a5b4f1c25c1de67da1d2ea7570488544e66c68f4d9f941875bebbf1dba53 | f718654a5e0d626bae46a8a9daa70b4f09c57dde |
| sources_status.csv | 4144 | 576535cf2d9dab5796983fe6a0e59c51a574eaf6b2fab5f6bd5c8124d2cf84d9 | 438b8afc4cc38bae288bc2cc1548eb6720e1494f |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
