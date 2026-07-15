# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1808526
Unique public blob bytes: 1188219
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 614583

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 204861 | f7e1f5a5d540582a6947946e4a0f2a96d796b66af3255930cb673f5468affc31 | fdc6b3f0d2c13e733a8e02b5e12d7527dfa6df04 |
| live.txt | 204861 | f7e1f5a5d540582a6947946e4a0f2a96d796b66af3255930cb673f5468affc31 | fdc6b3f0d2c13e733a8e02b5e12d7527dfa6df04 |
| live-verified.txt | 204861 | f7e1f5a5d540582a6947946e4a0f2a96d796b66af3255930cb673f5468affc31 | fdc6b3f0d2c13e733a8e02b5e12d7527dfa6df04 |
| ku9-live.txt | 204861 | f7e1f5a5d540582a6947946e4a0f2a96d796b66af3255930cb673f5468affc31 | fdc6b3f0d2c13e733a8e02b5e12d7527dfa6df04 |
| live.m3u | 362205 | e856dfc3d9a0951fc6089c224616853158283c7a5c128a477bf7bd4fc6954160 | 1bfa03fff3d599cdb6586e168977d42789de2892 |
| stability-history.tsv | 557025 | 11aa4cb075233d44c1ca3decf1b7212e748125651e8982001c3034bd3820a3fd | 716d7257f1ccaf745bbcaef9d81dde8908770121 |
| full-check-summary.json | 18308 | 12bf3c624652933629b8c257f83f0cb60c3e82377bec373d4588e0590b5a5006 | 9fe6ad6df9bc91b5e4d49b5b516ffb9fbdf73ab2 |
| final-publish-report.md | 11678 | 6202be3546e7ca0306660a61a8e3653da44ae9658c6906ff0752b348f146f86c | 2851bedd0964f881b76a76bec76610a2088d901b |
| stability-report.md | 7727 | c736fbf1984502c56e67fff8d2e868f6caa5e53a1dcbe2514316755965ab8289 | c6ac57222aa17e8af4d296cd1a8e074faaf3c215 |
| coverage-report.md | 1123 | bfe722da1c0cfb12ef2af184a2894b8f40d9eed6209f91cf4439b2cf12185712 | 71a4c5ddbb5efe070538498f31e501d02c275ddf |
| quality-audit-report.md | 1303 | 54d9d54a6eb45cdf635460e68e8d458bad27319e1ca3a9b6b5bfe81e0e80556c | a1c974f5632852562c2a66ea1112418473845174 |
| publish-guard-report.md | 793 | 073d6fbae762a4d8a5d4131384508ff600422aa8233dc7aed19d4658da830620 | 54e4ba06d566f7f31c3378485c162ac80352ed16 |
| published-recheck-report.md | 11239 | 48a3a7d9dcab18ab1c28748fa3ee303887639a1000b3798d1993ac6dcacd760c | f8f0e14ffcccb07328f8a4c7421dea12a404e1f8 |
| source-report.md | 5724 | 6cb1f3338f7bb145976c87208a4bcbe6071f160e7690d994e8e4a85f9f2b4aae | 432fab63dec3b6a2ec10371cc67c2fcf2e177c80 |
| check-report.md | 5724 | 6cb1f3338f7bb145976c87208a4bcbe6071f160e7690d994e8e4a85f9f2b4aae | 432fab63dec3b6a2ec10371cc67c2fcf2e177c80 |
| curated-report.md | 3784 | 28138fcd82a0fd59b2147315c12feb75fa2ca26ae4d7bf20673eb9663ceb6b0b | 5697411ada930ca8d6e5d8a50290fe20b774130c |
| sources_status.csv | 2449 | e05690b1a7bd02928b2d6c60b7dcd76f917b2ebd0ef090f8615a4ee0444abea9 | 715372d1be9bf5296854297f156bcaf45d8ba978 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
