# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 326404
Unique payload blob bytes: 262690
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37326

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18663 | d0b7f6e03cc9bf9116387ce1b2a2807fc613ff2348f29017ecdb04ae66151845 | e7c495511a6558be9deef8f1da70f0aebd7acd85 |
| live.txt | 18663 | d0b7f6e03cc9bf9116387ce1b2a2807fc613ff2348f29017ecdb04ae66151845 | e7c495511a6558be9deef8f1da70f0aebd7acd85 |
| live-verified.txt | 18663 | d0b7f6e03cc9bf9116387ce1b2a2807fc613ff2348f29017ecdb04ae66151845 | e7c495511a6558be9deef8f1da70f0aebd7acd85 |
| ku9-live.txt | 21247 | 80cebb0dc5fb8af28ce70856f8e52cea2672ebaece1b02cb5be3f29ce10cd938 | 01c6983ff790429d14ee57aa0207802d0faee10a |
| live.m3u | 36068 | f6f0a37245dff50c4c1b24565720ae71ccec774ad656f1bfca1195cab65a2792 | 678930a52b8c59fc585c90a1af04fb4667209c31 |
| ku9-family.txt | 18228 | 8ce059fb8a85129871ed89f72ef399ffce42d70f9ea266f692eb46ee7fb066c3 | 611d21de70f07f20ec7afbfd44ec9136421448b4 |
| live-family.txt | 18228 | 8ce059fb8a85129871ed89f72ef399ffce42d70f9ea266f692eb46ee7fb066c3 | 611d21de70f07f20ec7afbfd44ec9136421448b4 |
| family.m3u | 35261 | 4223ae0c53dd24a65b41521dfe0173703996a63d5b57805b0919a8af93e69d3a | d80b557ab1793f435d524ec4d7ee59d2ca42685e |
| final-publish-report.md | 10924 | 0cb18f9ab195af93ec8165d878dca47c1bac6b5966dbb80295406d95a34d757f | d90a72277a17106cb033d589fca31c51446a22d2 |
| coverage-report.md | 2205 | dbf8cd6a3bd6f90bfcb36d2f9301ff42750878c8fedb61872465d804b5ba98b2 | a80931c6ffd9028700b8647152450cbde8de89de |
| quality-audit-report.md | 4694 | e44de4656f2e558c6eb9129578fb94bf69ccda2363621cc013b43e1f0d5299c9 | 5dc93e74f0d080d9a77f29b6b5ded6cbe4ac6449 |
| publish-guard-report.md | 1568 | 674877a953a213ff4146316872fcf079ad68025b407b255b5f9d9d39c62e8e51 | 78a8b15befa5235003aee98f2fba445d4a305f9d |
| published-recheck-report.md | 30827 | a6b7a7301a111f388e09280d6bf7fc8f46613e5cfef27e827d47623dd9ec6c24 | e74142575a599eefca0c0d63e71deeb1ee4db1cd |
| source-report.md | 8160 | 9ca6702e18c840c827e2b89e52a3a1e00ff4db6d45a454b1a7b3f7e8b7dd0dd5 | 5659b3071302ae01af3316a0e8e8e6b04fff5b85 |
| check-report.md | 8160 | 9ca6702e18c840c827e2b89e52a3a1e00ff4db6d45a454b1a7b3f7e8b7dd0dd5 | 5659b3071302ae01af3316a0e8e8e6b04fff5b85 |
| curated-report.md | 1833 | e196937bde4a1030294f4ee0a07de60ac56079d13c70e7e4695fdcaf9d6334dd | ecb1bc46e6d5b227fcf11aa8da35055cecd50028 |
| sources_status.csv | 4181 | a0ab309e22866d312aafaed4cc53e230ef2ce71088a0574d6bb114d45dffcbd4 | c6c6b43e5385a12863c6adc8fc2988f7a5060240 |
| tv-coverage.m3u | 48866 | 004e2fa050683cde5b3d572e25cff40702e4b14d881500855f571f98a04af35c | 78bfb9712d1736d129c9fd3fdde18e1a4a3be409 |
| tv-review-report.json | 12975 | 8d1848b14db3ad3221cb9cd75c9c37f4b97cf9107f35939808cc557a00e04795 | f22472c96aca8366662cee6558542873e762afbc |
| tv-review-report.md | 6990 | da42caffbd06e4f988314cb884b5b6924806032b5d3b25a9610652db91110ce4 | a9433a0e8adeba501441f8daebcdf824bd2660cf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
