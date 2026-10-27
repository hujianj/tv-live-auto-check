# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 230970
Unique payload blob bytes: 155900
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 50466

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 16822 | 85b7fba11d3767cf486617309c0105952fda100b77b87713b230a4a6d7b94586 | 928821d37d6808f9f241aae9707567a1bf03a511 |
| live.txt | 16822 | 85b7fba11d3767cf486617309c0105952fda100b77b87713b230a4a6d7b94586 | 928821d37d6808f9f241aae9707567a1bf03a511 |
| live-verified.txt | 16822 | 85b7fba11d3767cf486617309c0105952fda100b77b87713b230a4a6d7b94586 | 928821d37d6808f9f241aae9707567a1bf03a511 |
| ku9-live.txt | 16822 | 85b7fba11d3767cf486617309c0105952fda100b77b87713b230a4a6d7b94586 | 928821d37d6808f9f241aae9707567a1bf03a511 |
| live.m3u | 31708 | 5b686976aa06d6b3432a16a87702ae9083667c882cae326205f7fedd948ec7a9 | 61d85983fec51ce4684484388b386f5ca5d3e095 |
| ku9-family.txt | 16557 | f955b77363394ea4d7b9110e83ac15a4bfadaff00b14e3dcd1dd0a13d3d09ff6 | bc07b8c1c6ebd67bde7fed4ff8029db9f34dbb27 |
| live-family.txt | 16557 | f955b77363394ea4d7b9110e83ac15a4bfadaff00b14e3dcd1dd0a13d3d09ff6 | bc07b8c1c6ebd67bde7fed4ff8029db9f34dbb27 |
| family.m3u | 31195 | 130065555c9cb6367a451eeeb763808e96cdf0192401b0552a4cc13634435da8 | d4ec33199edb6937b871c27500413687646356eb |
| final-publish-report.md | 10682 | a6df5acf16c18585940055bf1663fb3044b7737b24c272fbb930d839b3645942 | f426625d4287c7c9f721d58b76929dc697a30947 |
| coverage-report.md | 2235 | afe6ba322b1dddf3e6e696a33fb08e5925c904e863e2319701e3c0c32a988ed9 | 8c5eae0f1d3960b899b08967058f03613a845bad |
| quality-audit-report.md | 4784 | 21c707c845a8d701f4e49711c5db5c9798c6b7a3ecbcf689b1c54edc8bd00bb8 | 6f36c796ff896238aeaecd2fdb7b11f65a2e1aef |
| publish-guard-report.md | 1523 | a10fe5715191d003d889cab37c337f0cedbc52b3c6fda0bdfd91d1216bf66fca | 540d0e93c00d20b10f0af788b9ec911c6cf04a1f |
| published-recheck-report.md | 26466 | bcec815b65abdecb9b8544b7a128b5669d3ce228fe2dce46db74cf54a7ee7ace | 573d9039b283380c37dd8124126d61b6a72138a2 |
| source-report.md | 8047 | f2e7525ec6eabb6e429138485a951aa69cb51df66278535b534c4a05a5888b2d | 62eb57b5dd1e068cee43b6f95998a650d0b4539b |
| check-report.md | 8047 | f2e7525ec6eabb6e429138485a951aa69cb51df66278535b534c4a05a5888b2d | 62eb57b5dd1e068cee43b6f95998a650d0b4539b |
| curated-report.md | 1804 | b33e80f15b50c6fec2b0e14b52f565f96c84c3d2b61d632337d0a7489f2e0206 | 77a3d1e56c821269b9c35fa4a8075061abf3f3de |
| sources_status.csv | 4077 | 9f7991a7d933d36d633668d27f8df91d40dc24d79fd4175b391811e3eddb5211 | d1a60d777ea519e3c87361842a35560492de7312 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
