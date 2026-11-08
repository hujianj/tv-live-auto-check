# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 333922
Unique payload blob bytes: 269665
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37712

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18856 | 5c0c7cbfb74a18f46b996e83e931c6baffae2e26b8b672a8cf1c5542496a162f | 9b5279ce532020b27d539edeba123f6c1684f95b |
| live.txt | 18856 | 5c0c7cbfb74a18f46b996e83e931c6baffae2e26b8b672a8cf1c5542496a162f | 9b5279ce532020b27d539edeba123f6c1684f95b |
| live-verified.txt | 18856 | 5c0c7cbfb74a18f46b996e83e931c6baffae2e26b8b672a8cf1c5542496a162f | 9b5279ce532020b27d539edeba123f6c1684f95b |
| ku9-live.txt | 22594 | 768e4e9ec729d02f5c4dcfa030e807bfd028de8cf8849329e746fc8d4c453998 | 03dc30063d33d4be357c2a35e0581affec603a37 |
| live.m3u | 36059 | 2af81ef5105d412e847f0000a8d166e130379a777a43a55b8e68404fd65ea8b9 | a90d18a5730b6912af6b5a966a9f1979a805cba3 |
| ku9-family.txt | 18497 | 7d96af99fa1461aac327a30714a0da99a392a59ac081b1b0ba5e6b8a6cdb95f3 | 7d075764374b5243df13323f505227d2bd83314b |
| live-family.txt | 18497 | 7d96af99fa1461aac327a30714a0da99a392a59ac081b1b0ba5e6b8a6cdb95f3 | 7d075764374b5243df13323f505227d2bd83314b |
| family.m3u | 35390 | 5772d60af359786ee581f0890ba162051ecad52f0249cb418d946eff61162fb1 | a0df608269aa06d4b45c114b5372073d1fe3a6d9 |
| final-publish-report.md | 10932 | 58d0d9f0f455d904ccca85719f3a7e476d0a2857f9b72a8aa2edeac1bd84ea6e | c08c1b6cf7307b0f225843d1bdd98ee6fe164003 |
| coverage-report.md | 2200 | 57b6178f055be605ca4e1cc32a4319725912264da7a669b5c591b134f8bc988e | 28eb03eef7fb2b5b33f607ff28c1f3eabfa851a3 |
| quality-audit-report.md | 4679 | e87bbefcc7f8264129853b1aeb841014f045bf41612097afed7ec467f86b88ea | aa82fb467bb438be091ca79205c43bb60a9a8b77 |
| publish-guard-report.md | 1473 | 877e1592b667563a12b98989b64dbeee26f7ba475f4d306cdddae0d79ca74002 | c4e4454238c11bb4ffe22b4f8349021b944c0429 |
| published-recheck-report.md | 25383 | 8efabc9313b629c19e159e77658e7ef176e0d3d67cdcf9c29f5ee377ccc248b2 | 822178e5493f9f257eae22d766d3ae268f13420e |
| source-report.md | 8048 | ffe76da942d7e7387ec4be48579ba885049513b851d4f75cdb423598c7ef9c8e | 8d25b20af32959d0e60c03a911ccb95f28f9b6cd |
| check-report.md | 8048 | ffe76da942d7e7387ec4be48579ba885049513b851d4f75cdb423598c7ef9c8e | 8d25b20af32959d0e60c03a911ccb95f28f9b6cd |
| curated-report.md | 1833 | 7138fc0bc6f03462f39ee3bb7acf5f0f4bbf76ac66123290a1fe789e58146737 | b9a3dddb0bf61c8d40551af91169536595ee6a2c |
| sources_status.csv | 4121 | 486e364e03f691d7ea056df898860701236b89933b3d9948c905a155eafac672 | c4323aa6c5b6488cdc816cf1df3b2e8508ba502e |
| tv-coverage.m3u | 50846 | 5ceeb6c3a5e0001b47a39528f02b7a5e6fc5218e5a179c962819e4768b1323ab | a44e5306572a266872c78d5a3b481b778985c61a |
| tv-review-report.json | 18247 | d0346c9e515dcc8d3cff3689076f1740068209fa37aa8ba05ffd21a8272a35ef | 21549570df0e5aef29933484dbce01d9a72c73bc |
| tv-review-report.md | 10507 | ee6e3879599cc11ba6b1df4649a0b7c122a1fa9b71cec419028d8ca9b589f4f8 | 04c8e8e7bdb5f785df3e848e7b506e95ef778188 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
