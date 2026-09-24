# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 248752
Unique payload blob bytes: 166611
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 55767

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18589 | 68ab7a1e106716a2796209308e2255cd92e24825b3e6232251ddd546e2c4192f | ee622cdff75e43a9de007cbc931fdfa7a4fbca5e |
| live.txt | 18589 | 68ab7a1e106716a2796209308e2255cd92e24825b3e6232251ddd546e2c4192f | ee622cdff75e43a9de007cbc931fdfa7a4fbca5e |
| live-verified.txt | 18589 | 68ab7a1e106716a2796209308e2255cd92e24825b3e6232251ddd546e2c4192f | ee622cdff75e43a9de007cbc931fdfa7a4fbca5e |
| ku9-live.txt | 18589 | 68ab7a1e106716a2796209308e2255cd92e24825b3e6232251ddd546e2c4192f | ee622cdff75e43a9de007cbc931fdfa7a4fbca5e |
| live.m3u | 34773 | db5b6e5c4392c4e8ba68a119e5bba8c792e0a34cbbdf5587b6c1af8bbd6bd3c7 | 757dc6ac3713e42b6a8b07450e83bc5d0a08a845 |
| ku9-family.txt | 18248 | a550da1bf25903c5ed0aee7050c1f18f14aa986d55c44d4d299cd204f75cbbaf | 8bcf62d3c6def149771204a12f9bbc9516e2e780 |
| live-family.txt | 18248 | a550da1bf25903c5ed0aee7050c1f18f14aa986d55c44d4d299cd204f75cbbaf | 8bcf62d3c6def149771204a12f9bbc9516e2e780 |
| family.m3u | 34122 | 1173fda62abfd6438693cc7922b63bc17942fc650316f4cb2a5c270b1db5702d | 8316de4222c13c6d2a0bad9e43d983d6ff0ce63e |
| final-publish-report.md | 10829 | e3c080a3970c40f04b56b8db1c51d3e0d73837405947e08700eb9455a92fdab8 | a4de852d2e6610ca100324b28e24ed5d1f2a3df6 |
| coverage-report.md | 2240 | 8323eb1196636e0c4ad6adfebcc9c95772c772318ad1efccb07f78693a53f120 | fece466e94a03b78c964c358875edd9cae24bc9d |
| quality-audit-report.md | 4785 | 36d6acd2101284e5550def4cda554bae9ce2574d4c69737a2f7f3975d29b56ac | 387d37e1096e236965f815364873dba687343da1 |
| publish-guard-report.md | 1670 | 1e16b580155865af66649ad9b6b6fdf5f6889fd1af7ded5a0402243c3ad67bfe | bc07fcfa47dc0d8ad3a5799ba533564595d68697 |
| published-recheck-report.md | 27298 | 7cfc084f39eb0cc7c541fb613f24881cb043f89cce75c7a776792cc8f166b197 | e7a2bb3f661d823f55e77c915e756db063ab6462 |
| source-report.md | 8126 | b9c23c15de367c8a7a3e580ce5bd0a3d4dc8f58aa20c84272a444d93ad7c3e1d | b929e790c850ce65d50f9587d0d727e81e55e7b2 |
| check-report.md | 8126 | b9c23c15de367c8a7a3e580ce5bd0a3d4dc8f58aa20c84272a444d93ad7c3e1d | b929e790c850ce65d50f9587d0d727e81e55e7b2 |
| curated-report.md | 1800 | 2fd214be528beb4199a783687cf18c7a53e8c88e7293ac732e732762182b065f | a81a62ec41c2cd8c18704f8f78783168bfaeba34 |
| sources_status.csv | 4131 | 8f7cdaa98d47a9536e4be5e79b899baa7737a3c10fc716cd87a1239784fa8fdb | 5927ef9541773a427c1deb0d567c64f7724d77e7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
