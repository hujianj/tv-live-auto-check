# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 336995
Unique payload blob bytes: 272737
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37760

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18880 | 087ad460e115ac4d73ce17c16e81eb60c57ac65c65ebc9bc717ddd25cace28cb | 3142791bc2f64f871d6d345dd601587f2bb3a218 |
| live.txt | 18880 | 087ad460e115ac4d73ce17c16e81eb60c57ac65c65ebc9bc717ddd25cace28cb | 3142791bc2f64f871d6d345dd601587f2bb3a218 |
| live-verified.txt | 18880 | 087ad460e115ac4d73ce17c16e81eb60c57ac65c65ebc9bc717ddd25cace28cb | 3142791bc2f64f871d6d345dd601587f2bb3a218 |
| ku9-live.txt | 22475 | 6d2c1a617d5f3de662abcbc3f53b98e6b6639c7a10d5d342a504833f4e463b08 | 299b6f37599f40912461a4e78fe3370581f6181c |
| live.m3u | 36225 | 755df2d564f4f9b8a989e91d9dc2f3f54a5d5938712ae1ce412ef09ad9ef47be | c1005c9d2cab5fee28b97e52c5c6fc10c4244e02 |
| ku9-family.txt | 18444 | d7f58c1d0a83b7752446ac9827db915bdd924dfdf0079d2c8fe059f5220bac14 | 637fe79f01b92806015e2c29da5f230e0d9389f7 |
| live-family.txt | 18444 | d7f58c1d0a83b7752446ac9827db915bdd924dfdf0079d2c8fe059f5220bac14 | 637fe79f01b92806015e2c29da5f230e0d9389f7 |
| family.m3u | 35417 | e8e79feed4a055aaee945bb91b99101ad7b7a21d13491890c9b86de1d8507943 | 5d8e4077854ead81e267e98563c826ff57654eeb |
| final-publish-report.md | 10942 | 2a943cbac83ce60cc1d0a08523579b40fc19a26d7f16cd8ea3b3b29ccd4952aa | 59361052e0c49e559bbd042f5136529e44e56d54 |
| coverage-report.md | 2195 | 3d86250a887eca84befc977333afe81c9967df91edb65828fb6fcbe8997834dd | f359e66bd7c4eb5e83f7dd849599b32a2700ee3e |
| quality-audit-report.md | 4691 | 15c68441530f243c9403b4b4ce6787941710e29b9d268d46cb0d969d2cbbb58b | f3ededa5970d39c8798fb1961a22dd9f28e7e9e0 |
| publish-guard-report.md | 1473 | d908e73b6dd56b7ea4109d5b5f122376cc1a62a54583c5d92bd57bb16aa6d8ff | 5a5bb61d04166c6420dcb4c11ae165aae171a02d |
| published-recheck-report.md | 29910 | 94de8c4466d372ad96e047de559dd2df96fd40e1d849da5750a41b785170b8d1 | cf4b67a9dee6e9d5fe48ca9b9369e1867be00581 |
| source-report.md | 8054 | ee4b9f22551334cca78328230656742a14ae5c30846328e470a88bd6ffa7b4d0 | f6d950f4d2a533b4c362582d903a6417fa4e471a |
| check-report.md | 8054 | ee4b9f22551334cca78328230656742a14ae5c30846328e470a88bd6ffa7b4d0 | f6d950f4d2a533b4c362582d903a6417fa4e471a |
| curated-report.md | 1834 | 670a5a1cf83208da3c3be2abfa84363a670fcb62f8e0377d788064ab994577cd | ed9c449883d9bb53d229401384dfa7ff314309e6 |
| sources_status.csv | 4123 | d7e7f32e6dfe26e2fa5d99b5d72f22c5deee3e3b3727c90e46d63de212db6ac1 | 18de16abda1c13192146522e57ccfecba6e40ee7 |
| tv-coverage.m3u | 50724 | 944f6520517b3fef92b31f884e69b5ccbd847b1770ec9c759ca524cd04ec1780 | c8e5f50b409e5f4d39a9d8ae4796599ce8cd6981 |
| tv-review-report.json | 17350 | a1893f0ceb70241ac4a8e1bad03f97cb07bb71ebee06c0b20cb22623ab3ca1cc | 62de5df10eb011b68b2024bccec173d2753f818a |
| tv-review-report.md | 10000 | 9e1e359c47512383211c38820942efca41aacbeaa241b6cd75d6c237ff469afa | 670590a4f9100d141b5c17a2dabc358f9af73d87 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
