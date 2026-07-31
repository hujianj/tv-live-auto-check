# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2459751
Unique payload blob bytes: 1712475
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 643302

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 214434 | e480a753b69550daa1043301b505195ed8dcf5f131259386aca135644663d1d7 | c25722527bde775106c7acf9d3c9eafda05636f6 |
| live.txt | 214434 | e480a753b69550daa1043301b505195ed8dcf5f131259386aca135644663d1d7 | c25722527bde775106c7acf9d3c9eafda05636f6 |
| live-verified.txt | 214434 | e480a753b69550daa1043301b505195ed8dcf5f131259386aca135644663d1d7 | c25722527bde775106c7acf9d3c9eafda05636f6 |
| ku9-live.txt | 214434 | e480a753b69550daa1043301b505195ed8dcf5f131259386aca135644663d1d7 | c25722527bde775106c7acf9d3c9eafda05636f6 |
| live.m3u | 386874 | d2dbe9170f925fc805f17b5815823ba80c38f1a2d54604f36236022743cddf90 | bf8d012d735094a158c9903f16756032bddcec26 |
| ku9-family.txt | 98122 | 34b6cf9aae8aaad91af1b67265a53f490516c4b7cbb0fdfc04b141df0ab816c2 | aaf682a0c70082705385c7595abda739f5cf7b56 |
| live-family.txt | 98122 | 34b6cf9aae8aaad91af1b67265a53f490516c4b7cbb0fdfc04b141df0ab816c2 | aaf682a0c70082705385c7595abda739f5cf7b56 |
| family.m3u | 177810 | e9ca8635425c8b40219ddcb6519289430a5c4ad3aa158536d4aa64b6cd698a61 | a2eab84059df88d4505d3652ec9d0bd09dac7c14 |
| stability-history.tsv | 766571 | 20f7bd930bc5e2e58dadebbecb7ba08bdcc31978397d1e8bc95d1ea7ddff418e | c0efe187f541f3d781549a8d910ebdc89f550ac6 |
| final-publish-report.md | 11408 | efc5efbdfdf2709201d931128d2915f2cb9f5a108eb0f8fa75d8ffd14cabf288 | 85487b075a132b21427e038e9fa2c3cc8f48471d |
| stability-report.md | 12917 | a26175130ba7022accc2d4cac51af053a7be99d8ffaa7367d9395c66e5e3cc3f | 01e32ac8b7c8b22be20720ab0926321a84a08754 |
| coverage-report.md | 1369 | fbe1fb134f3bf74a3607409d72c4687ff03e6c8b5263b80032f8d1176e7f0676 | a71a43eda6d5cc085a0cb62f3b8d89cf882be166 |
| quality-audit-report.md | 1435 | 2d1999cb5c0663b2c79c885995fd6b6eb4b8fc6acb926a835fc30c6cc8a360a4 | abf3160010c8945a3ab7d2f3e0d913ddcdf7d841 |
| publish-guard-report.md | 791 | 5af2c7297e0a015e2bc2baeaf848057ca95a53981d0ebbe02ffdcd3db3270ceb | d00de5f376edb852254cd3db61e29c2693a073c6 |
| published-recheck-report.md | 28703 | a3635b5db72359cf632e2d0ab48d501f1e69ac6a3750e830514e868af27182c7 | c65c41595591289acc2f06cf0385e481e84bd660 |
| source-report.md | 5852 | 6255d5a860fbf6bebc6fb63d8c90a840f98ec642ced724c884450686d1008826 | 8ecf5c32b488ff338d78912179054dfae731ddeb |
| check-report.md | 5852 | 6255d5a860fbf6bebc6fb63d8c90a840f98ec642ced724c884450686d1008826 | 8ecf5c32b488ff338d78912179054dfae731ddeb |
| curated-report.md | 3590 | 264ab9b8b8d3712c2d07fcda2155dac596cbca374b6aa2a6f652ddca9f52c544 | 3234a43f59b91ed62163580a8b9c14644af8dc71 |
| sources_status.csv | 2599 | 6b3b4f9c2761ec29b5f252f2133262ce4b00cc0ac3eeff28995c9665d9be9f0b | 114c325c8aa6167042d7d56a66daa45cc6923330 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
