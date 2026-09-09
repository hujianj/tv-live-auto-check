# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 296366
Unique payload blob bytes: 195957
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 69540

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23180 | 2b1832f9a61fce46acfa4c8e0523acb6f21b5a7243501ffa4d6a666a8ac2226b | c7c040577c63d149f3773312320b256c38acac24 |
| live.txt | 23180 | 2b1832f9a61fce46acfa4c8e0523acb6f21b5a7243501ffa4d6a666a8ac2226b | c7c040577c63d149f3773312320b256c38acac24 |
| live-verified.txt | 23180 | 2b1832f9a61fce46acfa4c8e0523acb6f21b5a7243501ffa4d6a666a8ac2226b | c7c040577c63d149f3773312320b256c38acac24 |
| ku9-live.txt | 23180 | 2b1832f9a61fce46acfa4c8e0523acb6f21b5a7243501ffa4d6a666a8ac2226b | c7c040577c63d149f3773312320b256c38acac24 |
| live.m3u | 44092 | ac68314713f9f769ffd41ac6887b0c47ed00da9f8d3445d4870d7afb55365c6e | 614464d0697bfd97b9270a1fbfe9266c7b812735 |
| ku9-family.txt | 22751 | e17f9d41f59a51b0c2e1b07cba119e51ca64084c554d5f2853c40332373a49e3 | 295971f28f9e5fc4eb9c263d6e2459708c90eb50 |
| live-family.txt | 22751 | e17f9d41f59a51b0c2e1b07cba119e51ca64084c554d5f2853c40332373a49e3 | 295971f28f9e5fc4eb9c263d6e2459708c90eb50 |
| family.m3u | 43291 | eaf5080fecec60af17498d8568c6bca8acbd99d1f49809ab38f0686d01c54701 | 20c8a77816f3d0f60aaa9d01956818816fcd5b3c |
| final-publish-report.md | 10886 | 876ec7c2d375d23f0b0a1666be1cd6fe3d0f3554125e4002cb219f06b13339f0 | e4c3e6294f28120428b309d090ba3986ca3b01b6 |
| coverage-report.md | 2244 | f9b77ec480c63e8076c9b55a287d9427c905be19785a4843758529d3504070fc | 0d116b5d1e02767f6f82bb86c12b3cc2d774b348 |
| quality-audit-report.md | 4732 | 6cc959b53cd3ae04699a705ee3a1d40504de0be4bd1d37d83f247fd60f549e65 | d7ad506516a705b7b1204999a2e69f72d76da1e0 |
| publish-guard-report.md | 1561 | e76e0dcfe0ccb0b943293219eb5b0cf4a88f11de84b153951081b49f00c2c44d | 4226d9ea8728d813ca8a897a30a8a2f71d279a1a |
| published-recheck-report.md | 29103 | 2f42c184bfe138227ca007a9e85ce54698b8afcc5ddd667c438237d9197ddc5a | 4d7c81017aa513294fcd053979828f773b019a4d |
| source-report.md | 8118 | 930adbd8677958f14392ddf7371b0013b046437603184278fd876f40717f44b5 | 2537dcf51146d0f6c9436dafc64529e397a74ed1 |
| check-report.md | 8118 | 930adbd8677958f14392ddf7371b0013b046437603184278fd876f40717f44b5 | 2537dcf51146d0f6c9436dafc64529e397a74ed1 |
| curated-report.md | 1860 | 0f2cbc3dbc9a7bf62ad298660d929d7fc7711c6999a5dc09fc628f83806a3576 | 30a5b4b8e302afbed7a911b9aecda05422a96d35 |
| sources_status.csv | 4139 | 1b4391c541b53346d9d2511879b863654b7b0ac8182ebd3652c1d06f4570077e | f71abb26abca16631ff556bb331b166852feba09 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
