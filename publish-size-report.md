# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2448884
Unique payload blob bytes: 1705623
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 639267

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 213089 | a193eff0c0f18dcd4fdc588611b27683655f3a71db5aa2aae8b2bd3900681f08 | 061f34138449b8d5b804d716dfd7bf86e693dd7a |
| live.txt | 213089 | a193eff0c0f18dcd4fdc588611b27683655f3a71db5aa2aae8b2bd3900681f08 | 061f34138449b8d5b804d716dfd7bf86e693dd7a |
| live-verified.txt | 213089 | a193eff0c0f18dcd4fdc588611b27683655f3a71db5aa2aae8b2bd3900681f08 | 061f34138449b8d5b804d716dfd7bf86e693dd7a |
| ku9-live.txt | 213089 | a193eff0c0f18dcd4fdc588611b27683655f3a71db5aa2aae8b2bd3900681f08 | 061f34138449b8d5b804d716dfd7bf86e693dd7a |
| live.m3u | 383213 | 99ec650d0c58bc5fd5f4ee6bd544383f2bfb829daf13548f2b83104612e8a10d | 1e4889437cad7715210db2714774022bd32c1d0f |
| ku9-family.txt | 98156 | f7f099c699b98029ddfdba8988a92b8eff4f936141586a7d395ec78c585f8374 | 86d9ee9f2cb2f791f6ece75f06b5584a6400d6f6 |
| live-family.txt | 98156 | f7f099c699b98029ddfdba8988a92b8eff4f936141586a7d395ec78c585f8374 | 86d9ee9f2cb2f791f6ece75f06b5584a6400d6f6 |
| family.m3u | 177547 | 5753b4f9f0c616636f50e7b2b7cc2ed1c2cbca2817b49a3d071eba8d8b8f615e | 2ee4a91bb5d0436304cedd5d124f5c2f8d5fec04 |
| stability-history.tsv | 764173 | 345dbf3122e2c28c22ae52dad020991649ea74c79a1f707604f60bb279d7ff0f | 8f4469568cf0c6646b2eb8a377d2aee1abad4b46 |
| final-publish-report.md | 12029 | cb703fc0a90125838bc4297e94055279f022cded547cee373f319136a4467377 | a5a70bab70b683c436ad32f22f2fe46c2b89e12a |
| stability-report.md | 12875 | 808f77554c108b65e80d2dbb1e81fa184566cf3f9550f082578efbf803b656b1 | 1f2514418507c46855523c4591b21423f28a20b4 |
| coverage-report.md | 1349 | 4d336872b2aea016300d03f92fa6eed4a46e73e649206951e3ae60e1a8a4301d | 010d7386a3126cb5d26f9d3ef07188e4850eb7f3 |
| quality-audit-report.md | 1435 | 9cc7d2b3c83d41c5c747fd2a5462f9cb2e5c6e9f0e5b0df4276964a8a84e31d7 | 473746b65b6a2ab454babd439b816ace99775a35 |
| publish-guard-report.md | 785 | a919c320ec802d3f7007b93a34c6d12642640b9f362a13e63f1ccc6142f07db6 | 59a3a3ec2fbbf96aa2830cfa5321b97c9776db5f |
| published-recheck-report.md | 28951 | 5b614303994818fbc030d7573334b19a987429fffe98ab3e45cbc7b18f10e26e | e6acbf1ce4a0a830a40845fecc33bf68f7d8a71c |
| source-report.md | 5838 | 4980625d080476579c351fc353e9f7a28a13533f7cfb4617072bd216d29395ad | 903f12cf521625b164b222d5615635513b93a3f3 |
| check-report.md | 5838 | 4980625d080476579c351fc353e9f7a28a13533f7cfb4617072bd216d29395ad | 903f12cf521625b164b222d5615635513b93a3f3 |
| curated-report.md | 3582 | 0c87c5506ba4b7af019d66046a7058b51727846d5ca560c5ac2ef7c28fcca3ef | 6b7d77c859829fe012f0d7db3e36e616eb184abd |
| sources_status.csv | 2601 | 5d9fc055b6615fb78f1e372314b762955e5a8d3b56fc8632452892b4fed930b6 | e370d543596f4fc5e7d6f2b25f96fc813b1dcb30 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
