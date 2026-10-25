# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 275352
Unique payload blob bytes: 183291
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63219

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21073 | cf3a642b4b7d3aecd4bdf4a0281b3a4921a9bb1b4c28a9dc7e9fb7a346965534 | a11f81cc931543e97703fe6ff538a79d2222a32c |
| live.txt | 21073 | cf3a642b4b7d3aecd4bdf4a0281b3a4921a9bb1b4c28a9dc7e9fb7a346965534 | a11f81cc931543e97703fe6ff538a79d2222a32c |
| live-verified.txt | 21073 | cf3a642b4b7d3aecd4bdf4a0281b3a4921a9bb1b4c28a9dc7e9fb7a346965534 | a11f81cc931543e97703fe6ff538a79d2222a32c |
| ku9-live.txt | 21073 | cf3a642b4b7d3aecd4bdf4a0281b3a4921a9bb1b4c28a9dc7e9fb7a346965534 | a11f81cc931543e97703fe6ff538a79d2222a32c |
| live.m3u | 40539 | e7bd4725e6f0730bcc597cf96aabf662266cfcb422accb9be14c802307dc1a23 | 571c35e6c607b280282ce5e7769217cfca52a0f8 |
| ku9-family.txt | 20808 | b703071a3ff1d8d83733aacd12c41f1d1e61b958041a956c5da88a2029bb48fe | ed2bd1b81dc47cedb13aebf5189926d4fc4130d5 |
| live-family.txt | 20808 | b703071a3ff1d8d83733aacd12c41f1d1e61b958041a956c5da88a2029bb48fe | ed2bd1b81dc47cedb13aebf5189926d4fc4130d5 |
| family.m3u | 40026 | 8746dec8a48ec17ec2f8f23ec285c38cac8b7396647c4f3457e49f3b0b13928f | e860a8e9560597ee34e6afb8a0bda3aeab647b2b |
| final-publish-report.md | 10824 | 3a33b588bcbb2105630775b5badc32103f6cd53501d2ddaabb6e9d3cbfb6d25d | 70fe3f7d6f900ed2b29dd7419d17447e5ebe57ff |
| coverage-report.md | 2235 | 2b4358ebaf22f575d3abd1506c33b1ad40d201b6cdeceb7b8d03d034d85f9a4a | 0410dec680cb7df2057950abbe05f337762baad9 |
| quality-audit-report.md | 4735 | 46093b9d446abc1b77a432e85be12f94279b7495d76d32611f46b6a0067df8a6 | 10ee525133ea438c6a39d77d47adf738870c4802 |
| publish-guard-report.md | 1531 | 9ca7ec9e589a5a3e5fc30429ae417f86faccbf8180816ecfc2389e685291e3f4 | 84f7e73f2438ae8ec2bbcfe8a0d34b01143fad57 |
| published-recheck-report.md | 27595 | 20258d5bf0f8eead0da1794240b83f778aebb2f9005536c4ede956dc250cc2ae | 4b1f16c61c012e2b640364277d3fd028bed8b36e |
| source-report.md | 8034 | a6722fc5252981c9d639054c7b4dc421df72d389484b14c782a1c569906066ba | 7191b9a6b3ebf53581058ab76b3b9a410c1ac894 |
| check-report.md | 8034 | a6722fc5252981c9d639054c7b4dc421df72d389484b14c782a1c569906066ba | 7191b9a6b3ebf53581058ab76b3b9a410c1ac894 |
| curated-report.md | 1806 | 8283d145e7f245d2fc4d0dba123f6331e47d6e96a4a806ae1d7b771b6f1800e7 | 87b79a3b4667c6c82db4f0d3424190a7932c0d0d |
| sources_status.csv | 4085 | 7f495fd733b9deec68d7b7d0e70a40a2397a1ed2256d8851be17e3531559286d | a9f65f5791940d09f72216b60e491b11f5374b4a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
