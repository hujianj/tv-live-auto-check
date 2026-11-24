# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 291808
Unique payload blob bytes: 235128
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 32556

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 16278 | 8b066549e12b0e4e5c5b90dbfcca7f3ed9b8ddec510a8b5360aa4ddcd3590c99 | 584b9c19a0706a1fa4fa2d4cf6225c013285eaca |
| live.txt | 16278 | 8b066549e12b0e4e5c5b90dbfcca7f3ed9b8ddec510a8b5360aa4ddcd3590c99 | 584b9c19a0706a1fa4fa2d4cf6225c013285eaca |
| live-verified.txt | 16278 | 8b066549e12b0e4e5c5b90dbfcca7f3ed9b8ddec510a8b5360aa4ddcd3590c99 | 584b9c19a0706a1fa4fa2d4cf6225c013285eaca |
| ku9-live.txt | 18661 | c29b7d2f716f3ce7264fa0eec1047ea10e689f464551f1aefbbef0efe3d44ce5 | dc6298ab1c25f0d530c1ad013b6fdea5bd99d6be |
| live.m3u | 31554 | 2e2b7b709ec938d7c793be80beda2f298a093e891ea5be71cb7fa4cbc83d2379 | 1e91e00a5104ac297b74c1fb6154856ca7859ee6 |
| ku9-family.txt | 16000 | 674be1f3135f9fba42eb2f304b8a47d39fe33c244abf30525ed954109efb835e | b3f1006cca353a5df3de42b721bd22bc5251e0e8 |
| live-family.txt | 16000 | 674be1f3135f9fba42eb2f304b8a47d39fe33c244abf30525ed954109efb835e | b3f1006cca353a5df3de42b721bd22bc5251e0e8 |
| family.m3u | 31028 | 39f86d6042fefff2881e18ae157f833dcfb1cfc9138ddfca7a76ea3ac3b0f549 | 6823724b8c28e222537bf295ca6f38b4f89851fc |
| final-publish-report.md | 11266 | fb6ec0a06c4e34d375bcc45a0d818bdecd185d75628548443e26ccaea5abf318 | 083afc87d4ddc0dc9f023254a94019d52b988291 |
| coverage-report.md | 2205 | 9eea5ee282f9726fc3719db3a3811bfa3c8b788a2222b0111425f3d5faca8c70 | 1770cb724d55ed23cc1b85cd0332096d8b52fa1d |
| quality-audit-report.md | 4690 | 9f69c38eb252d9532116d417160ad9893727438a01807920f9ce68e34b027ecf | e8417d7faad8fede67d4d707cf96b70f091be6f0 |
| publish-guard-report.md | 1577 | 9c139998636638acaaaf9fdca7fbc4e6199f7bbaccb36bc67760c8f155d251b3 | 717df36f8231b5a9a36d4777bb8c9f964eb8be76 |
| published-recheck-report.md | 25126 | 2af5a9599d8db615209b9b548dec37d52a58ab5963e53e33b45dd318525bd127 | 9eb578e45458858e91db335c8ebf30603e017578 |
| source-report.md | 8124 | 4a9d1421408d866ee096f734fba3a3b09cb31befefe1e3ecd05e6fde06c735a9 | 7678539330895ec7abd9d85eedc608990d2e8d9d |
| check-report.md | 8124 | 4a9d1421408d866ee096f734fba3a3b09cb31befefe1e3ecd05e6fde06c735a9 | 7678539330895ec7abd9d85eedc608990d2e8d9d |
| curated-report.md | 1834 | 834a1f01e7fe65e3c62d057eefe8b3c79a42f3254364da5daf57dc23cf2a0870 | 71ec8b113900393a64237bb5fff56058a789f160 |
| sources_status.csv | 4181 | b80ccb7387fac2d11cdf92bf3982409a8a401db663234a170945eb35020eee73 | 29ab3ed2814e1e6b738b1c39717ab1f36db02765 |
| tv-coverage.m3u | 43222 | 9bd8d3fb0412aa9d3e9319ed945aebb783db0f02f1c73e4751d572996a7c0fba | 56868379f600b4aab8f4cb0ba99a51c5e00d04f2 |
| tv-review-report.json | 12586 | 376604c117fed5ccb179f2dad4b69f63015b8f2b3ca0ca0fde7be82c69891286 | 5ec33921d5f984bb32a842c54f1272a89bab1fac |
| tv-review-report.md | 6796 | 86fa606e37d0f5f5e30d6e245cc41df0006b2e79be6546fb100d05483323a46d | fbddfc8ce17607008743263834641d1afbcce602 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
