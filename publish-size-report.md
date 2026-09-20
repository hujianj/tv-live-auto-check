# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 308888
Unique payload blob bytes: 203510
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 73293

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24431 | 3c5249333535ca485056bd566db00273ed4081cce267ccce2568986c25aa10d8 | 3caaa87b512d7369bcfb3999f900a38acb8ca6e9 |
| live.txt | 24431 | 3c5249333535ca485056bd566db00273ed4081cce267ccce2568986c25aa10d8 | 3caaa87b512d7369bcfb3999f900a38acb8ca6e9 |
| live-verified.txt | 24431 | 3c5249333535ca485056bd566db00273ed4081cce267ccce2568986c25aa10d8 | 3caaa87b512d7369bcfb3999f900a38acb8ca6e9 |
| ku9-live.txt | 24431 | 3c5249333535ca485056bd566db00273ed4081cce267ccce2568986c25aa10d8 | 3caaa87b512d7369bcfb3999f900a38acb8ca6e9 |
| live.m3u | 46539 | 1239dcabe467db94a448f3c09bf8ddd25a266153e76cbc181884ce3dd112c8f8 | 1a8cf1c39000cdb2cd1a8edd0c937b4b9d0ffc45 |
| ku9-family.txt | 24001 | b888765515940a96682df292a39e23587a55d21cffff4695ac750864f8537271 | 18832d9898f24aca1291fc32d47fd4c8b3147397 |
| live-family.txt | 24001 | b888765515940a96682df292a39e23587a55d21cffff4695ac750864f8537271 | 18832d9898f24aca1291fc32d47fd4c8b3147397 |
| family.m3u | 45737 | 70ca19d2ed69d1aa0ffa86e2eb77b1c7094c81e5bad17bc229a38f522e54a681 | 42bcb1791b79a766fde837c19928522f44c7e60c |
| final-publish-report.md | 10826 | 5addbb660cffe95528284aa8bb4d1fa305eb1787fd6a1a89f4b5be5599d83ddf | 2088588258f10316455567176f59090a086c0adf |
| coverage-report.md | 2225 | 2adcf3e30cb66a5cb071fbcaa8fae04acf0cf16e08e01307138d93f94a46ed0e | 1b9b4231b2792db5fadf1254c3684985a78f938c |
| quality-audit-report.md | 4719 | cac121c001ded2435dcdd50a67edf44ad9b4de925695bcbaebf407c84d8c08f8 | 850efcf83fd9833f2d2d7469d7701e0e491d4902 |
| publish-guard-report.md | 1612 | 0044ca7e9d8d0d5715edb54472754561e320a5a1563874725c079c585ea0d834 | 931fe65cd7c63627ba7a5b3e56ede349f6793118 |
| published-recheck-report.md | 29400 | abf397d02717c1014597c01cdef3146e8e3fd95a4725e007d2a239b3b0d81a18 | 3c7e80d8f51e7407694acdfb6327e7b7c4bc0718 |
| source-report.md | 8084 | 030916ba5a6f796e0c3ad328e576523aea4d7a3eaa589bb43d045b8e73392f16 | dc01818f11ec27a0e54a9bb11a00ff8d20623992 |
| check-report.md | 8084 | 030916ba5a6f796e0c3ad328e576523aea4d7a3eaa589bb43d045b8e73392f16 | dc01818f11ec27a0e54a9bb11a00ff8d20623992 |
| curated-report.md | 1804 | e2884685d215dbca4eb9cbc47edc4edc691d848a5c22e4bc0a6e517eee7aa73b | e492d4981819d57abdbe9fb7123f23b4e576c824 |
| sources_status.csv | 4132 | 2a9e4e84227b97707e349ad61b6ee7aaff1ec91937ae3277b88660aeb7fe800b | 4f40b58f6c16edac7f3658ab7f39e2f4577c8ec7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
