# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 351677
Unique payload blob bytes: 281163
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 41856

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20928 | 055c5bd7839a419082d3af7df7cf6f3ceda24e0b2ea0379703b01d271bb2ff90 | 82a4328d1c1e733b2f9239374eb65b8d99838f93 |
| live.txt | 20928 | 055c5bd7839a419082d3af7df7cf6f3ceda24e0b2ea0379703b01d271bb2ff90 | 82a4328d1c1e733b2f9239374eb65b8d99838f93 |
| live-verified.txt | 20928 | 055c5bd7839a419082d3af7df7cf6f3ceda24e0b2ea0379703b01d271bb2ff90 | 82a4328d1c1e733b2f9239374eb65b8d99838f93 |
| ku9-live.txt | 23486 | b75fbc3d598632673fc80fed23f59f73024165a2dbd4ed24c8e0508ba6f18378 | 4eefe0a47b0e73aaa61eae25827268ccd43e304f |
| live.m3u | 39536 | 997f15d5926621eec6907179bd0b434a512475443792d7c57d1f3331a4a739dd | 4b3fea440418d79e77bc752fbec293f5c4204fae |
| ku9-family.txt | 20493 | 80a27e0bc0da1ec0444e8c1811a97abe0e1714310bf0403c5ab16539a12dd968 | 93ee77bd6a5c3df9588f31deb14f818dfb3139e9 |
| live-family.txt | 20493 | 80a27e0bc0da1ec0444e8c1811a97abe0e1714310bf0403c5ab16539a12dd968 | 93ee77bd6a5c3df9588f31deb14f818dfb3139e9 |
| family.m3u | 38729 | 4e5cf477af19adc8247859fa9e8a80310a9bdac8eacc15e3cc1c5cbaa9116865 | 6d53883406603503e5e8a5e23b0237ed7b7574a0 |
| final-publish-report.md | 11064 | cb208467194f2e3081197094aa1cb9549efb34dacf321ef1db2d87f56220aaee | 1fce4fec40566e5ebad21b25a530f5ef4b498c47 |
| coverage-report.md | 2200 | a8320fd7f50e775b702b7265d2fae1f22d5fd93a62e4aed27843039832e2207f | fbb4411c008655c78c96358ac6418f87629b5e07 |
| quality-audit-report.md | 4695 | 39bba141441dd13789a691b7772300398636bcda31c68987a9d2503be327702e | 4b6f22c6f9efdeaa3ddae2a2255ed6aaf72faf1e |
| publish-guard-report.md | 1559 | f19db26e6937955de1c6f47fc6590d0d86186fc2b6906597e1ad06782bf998b3 | 4e3fe2057988c492dc851ebfb3bd57fad436a612 |
| published-recheck-report.md | 30264 | e17a742990dd8c272ffaea452c6d8fe39869f0dc6657e7dd983bb8aed97d9ce3 | bb275a9c30e481cd401e43e37c9a0412a613d9d2 |
| source-report.md | 8165 | cd48b4fec8f976ac28549d9f032fbe6c07a4a8540448a436e57567f51974746b | 7934d50578ef137a2ebb6ebe6aad0a365d90065a |
| check-report.md | 8165 | cd48b4fec8f976ac28549d9f032fbe6c07a4a8540448a436e57567f51974746b | 7934d50578ef137a2ebb6ebe6aad0a365d90065a |
| curated-report.md | 1896 | a11642ed7b8e74dfe584d50aadab9db8fedea1f974493f06005cb8c20591eaff | 7b5fcace57bdc69f9d77891de4942cc0d7a00477 |
| sources_status.csv | 4236 | 9e1a33230881dedf8e435a3836b88faa2ba86a1dd1959810ecf17e95a705fb85 | 069593869b489f128d5a2911acaa39d1cbec98b9 |
| tv-coverage.m3u | 52680 | 07cb753e11e4bc2be5eadb40ccef67530ab4296c4cc82ce7552c7886669f787f | 1fc860f41467c79b154b38e3ce8ddccd0dcc7ac1 |
| tv-review-report.json | 13706 | 132064be737f3a31af0962e2d0a822e81591b2e0022662e5b0c946b9f2bdf5f5 | b78f75dd26a90c15367fcd7f0801d27f8a46635b |
| tv-review-report.md | 7526 | 73cb7a1ece7e1b82d9c5080c0c67152c5288bcaaf46eaf73650d78aff560c57d | 89a63d2b700beb99354adc8557aecf732cb4fb76 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
