# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 310594
Unique payload blob bytes: 248617
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36238

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18119 | abc5f8ed5e885111d86c66f823d2f2bdc87f8dac8a5123200c933af5513e522f | b892cf50af878c091dfe423b7cf5ecaadfbc5fa2 |
| live.txt | 18119 | abc5f8ed5e885111d86c66f823d2f2bdc87f8dac8a5123200c933af5513e522f | b892cf50af878c091dfe423b7cf5ecaadfbc5fa2 |
| live-verified.txt | 18119 | abc5f8ed5e885111d86c66f823d2f2bdc87f8dac8a5123200c933af5513e522f | b892cf50af878c091dfe423b7cf5ecaadfbc5fa2 |
| ku9-live.txt | 20344 | 6f9d5aad9a86f425098282a46893281f95f981b8cf1780bd8b2d5611ce5d813c | 1170acc59890b962387db94c72655d4fe7894537 |
| live.m3u | 35180 | 664e4db5101622b60cdcb03a75e7a3fb572679e8dca880a046fe6de4c58b75d3 | 63a5db7a6a15bd93b483fe26f10b748c71b3cfc2 |
| ku9-family.txt | 17635 | fcf2806c0675738858bf23b8d485b1c26246334c2c924681b9e784c7180f19f6 | ee758c130be1bf0a1c2b1522e9791d40b320a53b |
| live-family.txt | 17635 | fcf2806c0675738858bf23b8d485b1c26246334c2c924681b9e784c7180f19f6 | ee758c130be1bf0a1c2b1522e9791d40b320a53b |
| family.m3u | 34265 | a2bb0b31f13d612c9e8ffaa8b0b252a700fbf2cdaa24f3b5d81bf6ee980975a9 | 63b483b5031b546410f85cc8143111eaaae7f194 |
| final-publish-report.md | 11285 | 5bc548971e4230791fc71f5e00176b7a48c71e24d63dc8714dd2614221a00094 | dc1d558b22bcb5e72297a9c7dfeadc65febe898a |
| coverage-report.md | 2205 | 2d17f66bea6bdda8c0700699d73df21bdc67e2d0de103d1c6de6319c7ba7c982 | 25f27251cbfaaae4b612e8b87f9ba5880a7a2eda |
| quality-audit-report.md | 4681 | f8bfb83a5177f20812b7b3838ed4db72d2a3e3857f72f630e1bbf8f9f980dfee | 66f581eb4bf7e21690f6b86b8c778152cb606aad |
| publish-guard-report.md | 1568 | 80cf7e5f47f9ca8de0a45e5b9074b144b7cc891b0d04ae96cc945510b688cb07 | cc4d5b729f7679661513066496a017c709e05fd9 |
| published-recheck-report.md | 24415 | 764921e9d455cb3bf90caf2ebba8cb7f379fab56de88d8c2375d6b890798962b | 4695e5b0a3c766ce3f30824322221fe974ec1385 |
| source-report.md | 8104 | 4bfd9c36c3e23012d37fd864caaf8b003fadfa83ec0ea54a5bd8bc4d11653e62 | f23e3080b8b59ce9bd85cde768092f36800bdc2f |
| check-report.md | 8104 | 4bfd9c36c3e23012d37fd864caaf8b003fadfa83ec0ea54a5bd8bc4d11653e62 | f23e3080b8b59ce9bd85cde768092f36800bdc2f |
| curated-report.md | 1855 | 0b654b80a69c75923fd8b160da0385aa9a9b04beeedeaae82707e7a105fc4248 | fefb753b2ba4797de1e9f11a34b0650122d753a0 |
| sources_status.csv | 4181 | 094cb0391c6be28bd905699571918b6e8f55d0c4b8d85ce6ff72836a1a86bc5d | e956a2806cc663c12898c57c51e4483fbaa04907 |
| tv-coverage.m3u | 47198 | 39612b5892325f38c6174926cf45bbc3925d0d4070d3127234220bf9ff38fb4b | a7af3996e5d2c449564e5f4cf0fd0669812ffe71 |
| tv-review-report.json | 11491 | 3cde9899682e1774f5183eeb4ebe83b2abb3c83b11808edffbf5592689a17274 | d62a955684e879de1dde2916f244813021d71ca8 |
| tv-review-report.md | 6091 | f3c1f4c8d3afb7eb01dc63522852ea423438696a97e86ddc7c34305d702a29e7 | be1573ec4d08646ad69997279defebd65b187e81 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
