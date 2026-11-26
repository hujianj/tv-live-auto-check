# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 326386
Unique payload blob bytes: 263036
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37136

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18568 | 10a845ea3f232c61e83fd8b3ad5c2cf983d738aae53fda471cce4f3bd9a678fa | 901b05fda539d6308a37cd382a3f701c6670ee4e |
| live.txt | 18568 | 10a845ea3f232c61e83fd8b3ad5c2cf983d738aae53fda471cce4f3bd9a678fa | 901b05fda539d6308a37cd382a3f701c6670ee4e |
| live-verified.txt | 18568 | 10a845ea3f232c61e83fd8b3ad5c2cf983d738aae53fda471cce4f3bd9a678fa | 901b05fda539d6308a37cd382a3f701c6670ee4e |
| ku9-live.txt | 21856 | fc488ae6458cc7b3b6c3dbf1a09d0ec6a92642a7715276f2b61ca0ce3df52af3 | 808fc0b37a158920f8aaecc3082c3a92dcfdd770 |
| live.m3u | 35913 | e5e64d38314aad5f0f6267b81cc2f5d0170f2417825231feb56afd500e869055 | 02e5b0cf97e20ae5b7bc093f676560ffa52faa57 |
| ku9-family.txt | 18084 | 370b7aac38a65c6fd815ab680f06967b996a3b8c6039d78c30c8d0c48d7fbee0 | 67e834da6db0095d8f5701455efa83671a6b595b |
| live-family.txt | 18084 | 370b7aac38a65c6fd815ab680f06967b996a3b8c6039d78c30c8d0c48d7fbee0 | 67e834da6db0095d8f5701455efa83671a6b595b |
| family.m3u | 34998 | 6778d2249c6714792708cc3e61ac4d5742fb9f5e4d2828e3974935fa5076a8b6 | 24fa7df9c8eb0aba2675ea79d7c781300ac39430 |
| final-publish-report.md | 11271 | 2ba719837a2201eb5a242cbcf2193cb52f830365776c0d24828e96241017a474 | 5bb4d8cbcaefd5816e1de2c6783dce84e42b03ae |
| coverage-report.md | 2200 | febb67642fbb76bff835a77b8692ff825a44a5c8b25ed600b42aa8ad9347d07d | cfd190fcae5b67d563c78f5b0a009e860d4fbad1 |
| quality-audit-report.md | 4679 | 7863f32cf04b3f76d540d982fc047a82586ce28acb60befa6d3682a0b5ab0f00 | 497cf94d13250f7fcc12ab9bbdc44e8c062793b6 |
| publish-guard-report.md | 1584 | eff5af771f614946693fc036502fa93ebe2aad2c7c39a3e34e387f69263f16ac | cc2a8638efcf89ee3147cc5ab5f0f89bdafd6af9 |
| published-recheck-report.md | 25615 | 65c19e9e717dbe5198374ecb19e7dba737b3bd348d85cc538af3c9ba9d994c6c | 446aa5801d20e56995b54777c2a014f1240dfd1e |
| source-report.md | 8130 | 2f4f792ceb34da3a0f25835a16f62cc44fe9b6147f6945a761af3ee32faffe4d | 4e81d4f50b3ce0a1a70308b7cb6b0cc2341cb2a8 |
| check-report.md | 8130 | 2f4f792ceb34da3a0f25835a16f62cc44fe9b6147f6945a761af3ee32faffe4d | 4e81d4f50b3ce0a1a70308b7cb6b0cc2341cb2a8 |
| curated-report.md | 1836 | 9cc883e55433b00e0df84e4fc7bd89b92920cf239305268fef2b144b49a80519 | a3bfb89943c634410f409ad5e0536c1167dc9c6a |
| sources_status.csv | 4181 | 50f9d17154ae1e690eecb0f100abb8f931da178af7f425720cefa0f59ea07fe4 | d5a14024575de22ee2686210c96800d59efd3cae |
| tv-coverage.m3u | 49804 | be2e0abe8ab2f938c83ecb0364c5457965df8ae79749ea0d3a438f8cc3565fbe | d2c734b4ff805ce6ee8848a61a7762d2a104c1cc |
| tv-review-report.json | 15541 | cd2a25e1fe3362d9151ea61c2085075a6b4909942f4deabf48e2e24d5bbe9bd8 | aad111e6ed12e80b684a28f0a7f1af7eb30432d6 |
| tv-review-report.md | 8776 | 0c4a69505c5910df4c356f69140c18ee787425ba518b55f0fc22f5405478e899 | 98aa7f840fdbfe6a33e55b666ec9eb24f5c421f7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
