# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 281047
Unique payload blob bytes: 186468
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65229

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21743 | 5225850e61935420a1185ee95e88857ffd56030eb81c47cb16fa81c561752803 | 27e232f3fb755567af70a37c90b530fb78ffdd64 |
| live.txt | 21743 | 5225850e61935420a1185ee95e88857ffd56030eb81c47cb16fa81c561752803 | 27e232f3fb755567af70a37c90b530fb78ffdd64 |
| live-verified.txt | 21743 | 5225850e61935420a1185ee95e88857ffd56030eb81c47cb16fa81c561752803 | 27e232f3fb755567af70a37c90b530fb78ffdd64 |
| ku9-live.txt | 21743 | 5225850e61935420a1185ee95e88857ffd56030eb81c47cb16fa81c561752803 | 27e232f3fb755567af70a37c90b530fb78ffdd64 |
| live.m3u | 40786 | e9aa4b327459b1c8e301aa62cbb8e44a7693eabe1ff8677a0d4da30518969920 | e84d169cb9c1e554cc67bed75287fc6ee08655f9 |
| ku9-family.txt | 21321 | bbb88f765cd53ca0cd6784c6ebde3849787abca3f0a7f3e089e15cb537f54220 | 7b078e0eb921811c3bba12b8eddbed8c29731911 |
| live-family.txt | 21321 | bbb88f765cd53ca0cd6784c6ebde3849787abca3f0a7f3e089e15cb537f54220 | 7b078e0eb921811c3bba12b8eddbed8c29731911 |
| family.m3u | 39992 | 581521255167ef608f3c2e683e0e597ace70ea52456a400a7fb99c42db003591 | 0dc3f2936318e5819fd19db58a56ec768dcdff2c |
| final-publish-report.md | 10697 | b6cfe6ef34a978aab421d42b5808cc30303e07b8b58d1487da80da4e72d29b35 | 765c667abd5d8cb79842d67ef83a34d230ceb1e3 |
| coverage-report.md | 2220 | 18f58053c9bdfeb054604c2bbcbe7582a6b3a67959427960b182bc5f8d5f235b | a7d2367407f7f16962b0a051a0899615e09f3c97 |
| quality-audit-report.md | 4731 | 71ab62418e09534acbe534c2ad56882d6a618f58281af424741e4e1c9fe5a19a | c05d1833e02e7c6a4560b9c898f1784e79e3c6ea |
| publish-guard-report.md | 1593 | 0feca0c76f906a5368eb7faf8fda40906eb5dff5d6756d3934c0cc47a8709c30 | 7588ea603133a11d2e6ae6bd610ffe9fbb0e9f6b |
| published-recheck-report.md | 29418 | 5adbdd0f263b2650c6a35e9efff1e4754589cfe783ace798312ba99edbdbd9e8 | 6f5904f3a742c1b35040d38224c9d5ffbf6e361a |
| source-report.md | 8029 | 9609291a5a63260ad3db38f1527d776fae405b1ae3d3bc9af8d71300bd7a6a80 | 86eecfde7ba9d1c852c50399f8e7e75910dff00c |
| check-report.md | 8029 | 9609291a5a63260ad3db38f1527d776fae405b1ae3d3bc9af8d71300bd7a6a80 | 86eecfde7ba9d1c852c50399f8e7e75910dff00c |
| curated-report.md | 1859 | 944b37d8c648cac7bc7ba8bead64140b05d992e611779e7f96b62d1c7600894b | 053bad1634389c0048b613373b88b25f1c7121e8 |
| sources_status.csv | 4079 | 8bb04eb93463a649777898b2c29b159324a9fbe11fc9b0a088093771e6471f62 | 89eb32518df3b2947daf36255516e1547be9c522 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
