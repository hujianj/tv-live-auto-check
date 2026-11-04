# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 279903
Unique payload blob bytes: 226160
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 30658

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 15329 | f2afdd59c94988ef6b754d71211bb95588061de7eeb863733bc130ae6c78c73c | 2a7f528dadb5d3e976e7a7b5b7c34f843ff5f3e1 |
| live.txt | 15329 | f2afdd59c94988ef6b754d71211bb95588061de7eeb863733bc130ae6c78c73c | 2a7f528dadb5d3e976e7a7b5b7c34f843ff5f3e1 |
| live-verified.txt | 15329 | f2afdd59c94988ef6b754d71211bb95588061de7eeb863733bc130ae6c78c73c | 2a7f528dadb5d3e976e7a7b5b7c34f843ff5f3e1 |
| ku9-live.txt | 17607 | 26bb2507c14969e23a863d6f5e400bc9086095f0f1c64353d80121a8d642d6c7 | c0d5184cbe565da5e7daa5b8b435d88bb6b55d7b |
| live.m3u | 28738 | b31e96126b7f56f0af7bbf99b6817457ce3e2b661a73c7e4e54e4568d47d8ff5 | 510c28b7c9551eca165c721d82fe85924fed4d24 |
| ku9-family.txt | 14893 | d725ba9cb71081348b48f1e79dfc79a9139d96cd5334ab7bcda657781cbecdd9 | da154c5f0f4357afb471f4162f5f61541a3904b2 |
| live-family.txt | 14893 | d725ba9cb71081348b48f1e79dfc79a9139d96cd5334ab7bcda657781cbecdd9 | da154c5f0f4357afb471f4162f5f61541a3904b2 |
| family.m3u | 27930 | 7554f0f3eca02fb9f1c4f675c8d362726810247f22b5a1c356f2c8e469e46a2e | c6e974c0e6267210ad73c17bec039d2fc6a8e809 |
| final-publish-report.md | 10945 | 2607a21d3c1d65c1e58a0e28fee82423b3ae478ed0bfbd221d373b4ab202ee76 | 1554c8226aa3a9d46f6c80291b1ae59e19288fbf |
| coverage-report.md | 2205 | fcaaf0149478e723a35acb137d521149097b36eccf5e8596740c7aafdae1e7aa | f8dfc476338b0ffede4768dd0aa9c344d153557a |
| quality-audit-report.md | 4668 | 5677b43e41443cb7d827adfeb05af11c5306049c49776c19d950de53cf04ce91 | 216387bb991f2c7825f29b3f7361e30898907c64 |
| publish-guard-report.md | 1640 | 98639b5f55e4fffde797bbb8f68e40d4f15a9e663051ffab63ec0d11fd1cb0f9 | 4d7e1ec19bcabdab75a1d4738aa91b38742e061e |
| published-recheck-report.md | 29814 | b7bca85d53960ccb182e95e2b9b23b4a441d80ae03360482a2d1915c4bac537e | 503373718d8c9467c119f51550a5837212337ff4 |
| source-report.md | 8192 | d4d5818a815884db42165e4eacdf63c88305bb5c26a6f066fcd0c7c42422c1ea | 95a39b4907a2aae9f97378b6170e94b31fbcce48 |
| check-report.md | 8192 | d4d5818a815884db42165e4eacdf63c88305bb5c26a6f066fcd0c7c42422c1ea | 95a39b4907a2aae9f97378b6170e94b31fbcce48 |
| curated-report.md | 1829 | 1fbd0b58400c8656008facc2a49c40ff12b13bb5461a135d152948901213753f | de405d85160a48725787aa1891b21e33961d740c |
| sources_status.csv | 4240 | a2cf2ecd192434bce5cc60ec4a329f46f0e42c15d6f556a90bb8c275707832c7 | 39d47d7084069e134c44b9e7ad63c56ba4a7dc1f |
| tv-coverage.m3u | 39425 | 52b50939fe6c88f07ead0092a6199e92c5516ff8baa1c115e977dbbcb1101466 | e7498f23339a030e4bafcaeaec87b6754d75c32c |
| tv-review-report.json | 12150 | 9854349dd6a8231151847e58b113b680442a9286e2f070f71ff63731e95666f0 | 810ddf17b40ad22bf9f31f7edab9330490e7e489 |
| tv-review-report.md | 6555 | a9a0111d51fd70925ada4d73c1fae28e16448de0febfd535c9dd95423e647eb6 | 6028abbdf3336b7b14da02da1662277d32839adc |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
