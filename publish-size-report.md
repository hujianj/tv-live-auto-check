# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 275932
Unique payload blob bytes: 182889
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63900

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21300 | 5d5cadbe0e47eddf76b9acb4d37ff48253eb4f5b06f8978982b2bf589593186e | a6e20f242ebf48146622e30ba4219b82e7a317e4 |
| live.txt | 21300 | 5d5cadbe0e47eddf76b9acb4d37ff48253eb4f5b06f8978982b2bf589593186e | a6e20f242ebf48146622e30ba4219b82e7a317e4 |
| live-verified.txt | 21300 | 5d5cadbe0e47eddf76b9acb4d37ff48253eb4f5b06f8978982b2bf589593186e | a6e20f242ebf48146622e30ba4219b82e7a317e4 |
| ku9-live.txt | 21300 | 5d5cadbe0e47eddf76b9acb4d37ff48253eb4f5b06f8978982b2bf589593186e | a6e20f242ebf48146622e30ba4219b82e7a317e4 |
| live.m3u | 40948 | cf1ad3e4e71601aeb73219be72821188a9935542795ad50796d7591dc5605ad5 | 1a6d08bcaadc719f028a69b9693a03b61c4bda34 |
| ku9-family.txt | 21035 | daddea8c8b2704c5e1f6d93a1826e53aa6bfab815d145c7b4680fd2bf7c55f2b | 05cab4d1cb82635dd1a668f04d692ee29dee2317 |
| live-family.txt | 21035 | daddea8c8b2704c5e1f6d93a1826e53aa6bfab815d145c7b4680fd2bf7c55f2b | 05cab4d1cb82635dd1a668f04d692ee29dee2317 |
| family.m3u | 40435 | d2638d1bc48b0e4cdc6b0f23313d22b20549e048d4b36ac4cf1d05394433a032 | 7e01447bfde1dd85eeaf84635ec9ada7d3050e90 |
| final-publish-report.md | 10717 | f6ad26889ac315ab7b0198affe3c9c31b4de98d0dfa4ec43548d501f364dc802 | bf11aabf5a788ae865a932cf3d51dbe91906d973 |
| coverage-report.md | 2230 | 824e43249140c869d3320166f33a8469458758a6718d84c9085466944cc4f289 | eabc08cb07f0d3a63075020a591ef1afab72f7b9 |
| quality-audit-report.md | 4725 | 56d823dcff429650d860327a5cc5cf1d1891f7049e8d156f92b288373cabc298 | 8183cf47ae41661c9da48c28a4a12807c744f307 |
| publish-guard-report.md | 1556 | 7bc313dcc95ffda7be9ae19a1acd45e10e5eb691fdfb9758d826e25210f88d5e | 26b81331a811454ee68122a3e42b4a273e26e691 |
| published-recheck-report.md | 25894 | b23488d587dfbb5988c9be7ff77370482f2873ca7b90794f8084a784e343e5e1 | f1843a6ef31fff7b43473bb74fc3ac438c5a49c5 |
| source-report.md | 8108 | 34f89cf8193c9a36e928dfb308cef25dd36fe34e56f32e46b0901e221254cbe5 | 03ac5835cfad09db2cc277d4b9eaf135677c6962 |
| check-report.md | 8108 | 34f89cf8193c9a36e928dfb308cef25dd36fe34e56f32e46b0901e221254cbe5 | 03ac5835cfad09db2cc277d4b9eaf135677c6962 |
| curated-report.md | 1804 | 55a6694fc32f17b8a44cca2cf8c166b5e4fcfad0a1c6b1fc6c4a4d7511cae66d | 2dbf7082ee600ea2842260f8167b53cf793df63b |
| sources_status.csv | 4137 | e8de8b5151cc2429f5097372369eb83406ccdb95dc16d2c800358628e047377c | 98cc4e1c7075249432538ae23aa029a46128c9f5 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
