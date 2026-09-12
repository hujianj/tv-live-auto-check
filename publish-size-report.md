# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 185672
Unique payload blob bytes: 130073
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36030

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 12010 | 5f106f14ea96ddbfdf48b207dba60a6925f1bec810ee136977c64dedb21d9905 | 004a8a42cd24be185cd3d6ac329a6acd56854a98 |
| live.txt | 12010 | 5f106f14ea96ddbfdf48b207dba60a6925f1bec810ee136977c64dedb21d9905 | 004a8a42cd24be185cd3d6ac329a6acd56854a98 |
| live-verified.txt | 12010 | 5f106f14ea96ddbfdf48b207dba60a6925f1bec810ee136977c64dedb21d9905 | 004a8a42cd24be185cd3d6ac329a6acd56854a98 |
| ku9-live.txt | 12010 | 5f106f14ea96ddbfdf48b207dba60a6925f1bec810ee136977c64dedb21d9905 | 004a8a42cd24be185cd3d6ac329a6acd56854a98 |
| live.m3u | 22420 | 42e56667922f9a974386fc1d8ad1d72bc07c0c169cfc2e523f8cccb9c1f4384f | 25cc8f9a856ea3b299dfbfd342f993b4d3b6b8ab |
| ku9-family.txt | 11632 | 4605504ae82a6cc0421256efaff503557244cf79f77edc5ac917b482af104fff | 70b06db6459ee5ac03dec70822d3436dad0e442b |
| live-family.txt | 11632 | 4605504ae82a6cc0421256efaff503557244cf79f77edc5ac917b482af104fff | 70b06db6459ee5ac03dec70822d3436dad0e442b |
| family.m3u | 21732 | e5e0e1dd9780e20092bbbbfd5d35bf47ccfb2df4a38b30032a82cc1dbf2c09a3 | 4716191ee97a38ba38f72f4074f731ce192e7b5e |
| final-publish-report.md | 10620 | e3957c741c9635ccf23c8b663a7806848423ff7c97bd912f0aab0b9c5f2c6398 | 578c07700a0002998f8816e08ffcd515ed01d015 |
| coverage-report.md | 2239 | a3a037332ea034e502f29662a030ec1296f1328009667ddc970e37c8eb91079c | 02368ac6057631d4e9848391d136842ca0ad5db5 |
| quality-audit-report.md | 4721 | dc91470254caa17d62b8a9a493132cdb5967cb6fc5799bc36b2f9c7459cc92eb | 96340d328b4a4991aa7ff9c058e4b3dee88a8eac |
| publish-guard-report.md | 1641 | 873ffdee6f8d04af95fd3f4db93d81abd2bc9a3298119af0ad4560fad48776b4 | 95e93ec8ecb4450be457753abf43ecabbcebf18e |
| published-recheck-report.md | 29186 | af5fa258c915547a349569ea23f183bd85f2b7d37e197056c612cde47d7b72e7 | 6d99939ccbfa91940cc4301916e021c38b06c2ab |
| source-report.md | 7937 | 05d27bfda829b7742c3b884d0c088d9218ee5340c9a2ef32882b07bec6cc7115 | 0680f69a4fd1d55f497cb7d429ae477cd1d5eb63 |
| check-report.md | 7937 | 05d27bfda829b7742c3b884d0c088d9218ee5340c9a2ef32882b07bec6cc7115 | 0680f69a4fd1d55f497cb7d429ae477cd1d5eb63 |
| curated-report.md | 1857 | 26d9c88f36b6eb58a67731a82f3cc2872579cc63d138689a849efd08db7aef07 | d0a10ab621ebbd6f30868fee5ef6ae846288322d |
| sources_status.csv | 4078 | e28617ca862f6bafad8e55ae3e3a8d917b49d1ad420a9937639fd77d4a324e48 | a04e4cc62da9bce8610f82de2d81bad18fa214f7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
