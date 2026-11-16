# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 332311
Unique payload blob bytes: 269374
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36840

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18420 | ad96cfea56e4e13148ace2929c4e6fa3f249cecec60962b72de4f961cf119187 | a9579354adac4d0f91e30b1952bf257f0b3ae362 |
| live.txt | 18420 | ad96cfea56e4e13148ace2929c4e6fa3f249cecec60962b72de4f961cf119187 | a9579354adac4d0f91e30b1952bf257f0b3ae362 |
| live-verified.txt | 18420 | ad96cfea56e4e13148ace2929c4e6fa3f249cecec60962b72de4f961cf119187 | a9579354adac4d0f91e30b1952bf257f0b3ae362 |
| ku9-live.txt | 22015 | a248e9af025082abdade2f177f3bb8cf02c8c8672cfe6bca0ac500966d99e023 | a72330f43f6b8f0c44047e3d642096b01cdf7771 |
| live.m3u | 35151 | 095e1cc9ca29f5274b2eeeeaee590587e86805e19ef877d70ba8c528c8115a12 | c998e0ccb59f6d812f9006363c4fe0f07c2a8e99 |
| ku9-family.txt | 17984 | 749b30d8473e405babc1877ffac9e7b1c2cc9568a40436dc0c77c7c1e8af455f | baa8f3b5f80f4658dfea262f551e007330b91c67 |
| live-family.txt | 17984 | 749b30d8473e405babc1877ffac9e7b1c2cc9568a40436dc0c77c7c1e8af455f | baa8f3b5f80f4658dfea262f551e007330b91c67 |
| family.m3u | 34343 | 5825582b3ef990f370b7a766651f54943425b6d5f14cd7e4b83e935c5bdd59c0 | 0d0bb6483d768802b33d893c993cc1fb1729ab34 |
| final-publish-report.md | 10925 | c2f6d890d2afd94ae25f888612467f8476e3c24d0694c11186492c067bbbd48b | 089c7a4f282361d6ebb00860d0601110f6055a75 |
| coverage-report.md | 2195 | b39641f0c2c1ae6878231fba77ad35e8c56a4579ea55e1a6fa0a0431757c8045 | 121e5e77ce6fb2dae6ac3edc8fbecc20ee62ae79 |
| quality-audit-report.md | 4697 | af8c527942cb5fc590a5800964a6c82c95c0964b29070c395fc357dff687850f | ac57d2815ecdb5ebeb01125dd34d3eca10755add |
| publish-guard-report.md | 1501 | 7af5f8672d07e03479c9b1eb21b00b6d62be21d84b75536b47c9b90f3f892628 | 868b2ea1bf80105fec54969ed936c5374e0cee7c |
| published-recheck-report.md | 31609 | 7e124561808184db7728ba5ae9a2c9c67c0b4b629e83a0b0656bb43fba1e4ea1 | 4a2426dc735f47d380bd716d51bc82b11ca09f1f |
| source-report.md | 8113 | cb17c44140b6811b1fa0f38efe63c0559bc79d7d1dc70f08a0f35d7313b88f76 | d854b62f074b66bae4857e7b15bc3594705b961f |
| check-report.md | 8113 | cb17c44140b6811b1fa0f38efe63c0559bc79d7d1dc70f08a0f35d7313b88f76 | d854b62f074b66bae4857e7b15bc3594705b961f |
| curated-report.md | 1831 | 0e8e6cbc183e5e23fd8ab8b55eecf52ba870a9a428f2d394e90113ee90bc5724 | 5cee3ecf96d36f15fe92fbb7ec49360b0636d816 |
| sources_status.csv | 4182 | c2100a1212c07bb0365f79542df312d9a80f3fd3ce2d5defd097ec01a553dc29 | 6b3266274c427305d3e03e1f06d9cfa27e071eae |
| tv-coverage.m3u | 49364 | b596564990ed476423f61bc192c15f334e79118b8e10b27adcdd68cf2aa97eda | 77c1385f86a0a533a1f195604c6760921b6035b3 |
| tv-review-report.json | 17197 | f7c6c522839c066d9ea4a47dbbbb0aa8f5920e162952231f55d965f77a848ad5 | c79e67cb2b1872a741c3b56a362790c1d77e34e5 |
| tv-review-report.md | 9847 | b5a8118669528877da5a7b65e1f5c9d4dc1c9f3b3dc118d9ce02075ac8788750 | 232178f26032ca1f690fe050d8ad1bd193bd95a0 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
