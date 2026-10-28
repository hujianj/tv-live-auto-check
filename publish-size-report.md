# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 249714
Unique payload blob bytes: 167908
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 55461

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18487 | 8ca1f96b98b729d11323c5404dd29ef03983966c2ea60d18bdc69c22167884b1 | 39fe74b85d8df9e66cc76bec66a01f9eb90db4b3 |
| live.txt | 18487 | 8ca1f96b98b729d11323c5404dd29ef03983966c2ea60d18bdc69c22167884b1 | 39fe74b85d8df9e66cc76bec66a01f9eb90db4b3 |
| live-verified.txt | 18487 | 8ca1f96b98b729d11323c5404dd29ef03983966c2ea60d18bdc69c22167884b1 | 39fe74b85d8df9e66cc76bec66a01f9eb90db4b3 |
| ku9-live.txt | 18487 | 8ca1f96b98b729d11323c5404dd29ef03983966c2ea60d18bdc69c22167884b1 | 39fe74b85d8df9e66cc76bec66a01f9eb90db4b3 |
| live.m3u | 34762 | 74f0119d405d4dd215dc5092e597ae9a9329ada0c929bebd37895c9e4ef10ec3 | fe59f9105abcf93333970d5ec3953fd4f0027f93 |
| ku9-family.txt | 18209 | 3f9aa32efc1138c34d97270ae16d70cd11a4c42978a5f5cda547d7df93c19a9f | df42dd49d97260a35246d69e44c007b9866ce5d2 |
| live-family.txt | 18209 | 3f9aa32efc1138c34d97270ae16d70cd11a4c42978a5f5cda547d7df93c19a9f | df42dd49d97260a35246d69e44c007b9866ce5d2 |
| family.m3u | 34236 | 5f99a414bd61a429261df72aaa374e0375f2d03a640df1aafa73d1ddc0a85935 | 8f8e755ef5847d5d4b80620d1a0653c0c5a02e76 |
| final-publish-report.md | 10748 | b4208d4f701fc1420ba69b0e13247290bb7fa64a49b41fa668174e1b1ed9b0af | 5d1b8ae43c88c690d6d9e936a34ec42eb189d4ef |
| coverage-report.md | 2235 | a17b3a60f47e5e3cd399680d0e12d7f5bb4a56c7dc942423a1ea878278e0450b | 57dacd3632c4e4ad7dfdbc4f57e3d3753fcfac7a |
| quality-audit-report.md | 4788 | ad95950469c57023f17336df0aace3cd77a70bea49e0145e743ada34a45f635d | 9d4918da4e41bac1a0bbbe116eaabb655406483d |
| publish-guard-report.md | 1555 | 7632f973793565309a75b3c70ccd9d4a6f0283a54b022e41ec763d0e595027f7 | 275aa99134df78fdd94c96b7755697fb8d3356d2 |
| published-recheck-report.md | 28740 | 37acab07305b033949b990be2c2c3c493760e47a4a87c1e94298486413b62dda | 89ac85d7f70bd6909d08a20d4c1dc49fcf0229bf |
| source-report.md | 8136 | 16ecbb9d30bd358357ddaebd243bd8f3a674ca1ad8c60a6251670bb1eaa4b18e | a1549d5a9a9c7fb482a2c078cffa210d9372e3eb |
| check-report.md | 8136 | 16ecbb9d30bd358357ddaebd243bd8f3a674ca1ad8c60a6251670bb1eaa4b18e | a1549d5a9a9c7fb482a2c078cffa210d9372e3eb |
| curated-report.md | 1806 | 249d5b48a111b1276bf53aae5ce72b79c4f4ea34a735fc09929c877b3fc46062 | ccd55f54809f3c4a29c7be0dec8837c3e7d30b7b |
| sources_status.csv | 4206 | a50a228211df42e816e8c58392b113ef4d7f27d0fb0b64799aca06a74329f3ff | bc00c991cd440412c2e2e88832c5df2a9c5513f3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
