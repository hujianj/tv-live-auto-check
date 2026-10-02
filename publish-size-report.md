# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 278767
Unique payload blob bytes: 184716
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 64710

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21570 | 3e5a7aa017a0460dfe7efa4a61b5ad6f48b006fd25abb42cb7dfff7e17107f66 | 792ee8c5c4250017379143f48111f1234f3231b9 |
| live.txt | 21570 | 3e5a7aa017a0460dfe7efa4a61b5ad6f48b006fd25abb42cb7dfff7e17107f66 | 792ee8c5c4250017379143f48111f1234f3231b9 |
| live-verified.txt | 21570 | 3e5a7aa017a0460dfe7efa4a61b5ad6f48b006fd25abb42cb7dfff7e17107f66 | 792ee8c5c4250017379143f48111f1234f3231b9 |
| ku9-live.txt | 21570 | 3e5a7aa017a0460dfe7efa4a61b5ad6f48b006fd25abb42cb7dfff7e17107f66 | 792ee8c5c4250017379143f48111f1234f3231b9 |
| live.m3u | 41436 | 6ada9b8cca09cd2c06f2730680aad833c4e35d1f1ebaab892c70d45b38290079 | a2eee85fc29a8da499eab693f6825fea778c5e9c |
| ku9-family.txt | 21298 | 86cd6317b7b909b46eb9ad8169843564b701cea31a88c69380156bead46111e4 | 28c4e0c2337359e9ffe88b01fa521119960accfe |
| live-family.txt | 21298 | 86cd6317b7b909b46eb9ad8169843564b701cea31a88c69380156bead46111e4 | 28c4e0c2337359e9ffe88b01fa521119960accfe |
| family.m3u | 40916 | 1d34d9dedbee2a2897a3c41e5dffb820a73643192215c0c0d03972929a41b2d9 | 518905c2e58aaa535995a3accedbe2bfad4b1e20 |
| final-publish-report.md | 10788 | fea72f025f33c9c64781e0378bde0c71564387e3c3053f455735ea71f5f42cb9 | 12e1bd3f7a5b2dbdd029a7cb3c2b23a38b4c8f5d |
| coverage-report.md | 2235 | 0ffa5e713b9a342a015ec4c6daf46aed5b15a200857fddeddbb516fbed105326 | 9aca8c4854c4c4a947591d567ca0c1562f8656c6 |
| quality-audit-report.md | 4720 | 3e189e4f6798970298bd57a7c1fea3e4db5e0aeeed516754421c6634e6c26191 | 86de6e3ddd441d427e628aba7b072977dc257a2e |
| publish-guard-report.md | 1581 | bf502233210d0c792601ef993327354ecfa76cf59578607d2d315cdb11c45dbe | 642361b79c49a74268b1b9408352eaa1c0da1780 |
| published-recheck-report.md | 26247 | d86399dc4484fd972d927febadb77e79c98db27bee30672ed4fd1b15d9c00786 | 521c8943c1d8fad67898723ac009ed6a9631ae50 |
| source-report.md | 8043 | 832b54ad8dcbbc92aadd2220e10cd31873272062137210e6b1371f4eec90c919 | 6e177aec1cb638e62176881c69eead6543f82356 |
| check-report.md | 8043 | 832b54ad8dcbbc92aadd2220e10cd31873272062137210e6b1371f4eec90c919 | 6e177aec1cb638e62176881c69eead6543f82356 |
| curated-report.md | 1804 | ad389d0e91faf11a8003f1c40b0f163b3dd9edbb5699cfe2a5bccc4d1eb7fd12 | 518869636c130c3dd1edb14ca0291edd4e36bf51 |
| sources_status.csv | 4078 | 01977819ce60a19f096f12807b7c50926fda3df1a4f48044b3c970e71bd7d809 | 9eab00ddbdb98b341fad58ce67eb3dff7ed17d60 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
