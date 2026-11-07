# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 344340
Unique payload blob bytes: 278920
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38406

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19203 | 3bcb0760c467096ffb687700a1c259eb740f4199da2585439590be70cb243992 | fb4b520c739f426aed42fa69c05f0687358c4fa1 |
| live.txt | 19203 | 3bcb0760c467096ffb687700a1c259eb740f4199da2585439590be70cb243992 | fb4b520c739f426aed42fa69c05f0687358c4fa1 |
| live-verified.txt | 19203 | 3bcb0760c467096ffb687700a1c259eb740f4199da2585439590be70cb243992 | fb4b520c739f426aed42fa69c05f0687358c4fa1 |
| ku9-live.txt | 22941 | cd84f2ae6d93b57316ab21eddb60ca8f437c7edba3b5349741bfd4fd3929cc10 | 6a8a0e3f62aeaaf2dfe0f2d3232874a9fac0662e |
| live.m3u | 36835 | 791c6896074cc3ac98f4f91033d1132b1256e4ce358db911186d03df78f85a80 | bd4617102c6bb49139147bbbb66b5027270648e2 |
| ku9-family.txt | 18844 | d22cb3d6e4c1d17eb75e69133561ad051c5238a6d5f303ba7cb68e2c89c6cc87 | dc5848292be69e34d385d5517e7fa4c434dd1ddf |
| live-family.txt | 18844 | d22cb3d6e4c1d17eb75e69133561ad051c5238a6d5f303ba7cb68e2c89c6cc87 | dc5848292be69e34d385d5517e7fa4c434dd1ddf |
| family.m3u | 36166 | 5ffc6ee1d8ff980200a4c50f1a379417d3b47ee55d89a4f42af77182b832cacb | fe50deba6d84c57263eb6436e8dc6916082ef643 |
| final-publish-report.md | 10911 | 0c73e9d2d1f1c9ad201924f75074ef7a8b9c822c7c5a98b2f06d6e018d6ca56a | 50850213a8f7740ddbfb198b86634527f250a417 |
| coverage-report.md | 2200 | e7399567705c085a9d2d5223861b80051ae910918b333c41de6959a393f5a9d6 | b9a536938ddb8f14e1021555b742348e2fa62fd1 |
| quality-audit-report.md | 4674 | fc4121ba37bdadbf0fe1abda23191b9a551bca66aac961c69717eb5efeeb0d32 | e383502fb4bf459e1eff4a237eed03fde3aaf1c4 |
| publish-guard-report.md | 1529 | 0920db8fda4d090e674a238372778334f166d872f8e76881d13d903980364026 | 6a267b873a6365d7de54be91984fb2d2bc9d091a |
| published-recheck-report.md | 31014 | e49f68fba2bf164181ecaaa4c64c240502489788df918891904fb794526686a5 | 923163fa7c5b2b062a0c38dd8c7f4906587c93d0 |
| source-report.md | 8170 | 2702f901b98e9f0b1ddf2b1dd98387bed7459e624537223831fe8efbaf21e19d | cac28a07ee79c4722c1c00a28152e0b882c7e904 |
| check-report.md | 8170 | 2702f901b98e9f0b1ddf2b1dd98387bed7459e624537223831fe8efbaf21e19d | cac28a07ee79c4722c1c00a28152e0b882c7e904 |
| curated-report.md | 1833 | 577a2b1148c32fa8c0c3b3b113305acd960713847a5f076086f3449cb4d03b07 | 2dcae4c47d355e608c20b7f0d068bded392e9c51 |
| sources_status.csv | 4240 | 6220ccbef505913693bae5b5b93fad5197fd90eedb6038592f80adc6dd4602c5 | 59eba599a7da01c599480e08a40c10861c02f25b |
| tv-coverage.m3u | 51778 | 45eac2047a0d899ebde9d6f0d2fbe5485732f1751e28b6e54feb90b7ce410c11 | b4ef06c095aaf24442a1f18b5f6083af45a91643 |
| tv-review-report.json | 18161 | 7eb1eae54534db34f35b9fa35b65e025940413d2ee76c75278f3695eaf73613d | b9d7998be4ac9c3677a3c5e5ae66bc8b3b61eafe |
| tv-review-report.md | 10421 | 31a83995ffc074e239059ce9620214103bb7223b56f5646682fc3b69a6e07a37 | 9ca7596ba882621e401ae8b35af7f6cb9f5f6e09 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
