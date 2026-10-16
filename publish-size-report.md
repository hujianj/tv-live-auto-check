# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 329056
Unique payload blob bytes: 214903
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 80052

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 26684 | 343b196e20ce5ae0a653ce6823114a1345b60a72461c7d31aa3e4b07eadcb3c7 | bb2b08f8a702401fe5ecd9ebb6ad2d1396ced5f0 |
| live.txt | 26684 | 343b196e20ce5ae0a653ce6823114a1345b60a72461c7d31aa3e4b07eadcb3c7 | bb2b08f8a702401fe5ecd9ebb6ad2d1396ced5f0 |
| live-verified.txt | 26684 | 343b196e20ce5ae0a653ce6823114a1345b60a72461c7d31aa3e4b07eadcb3c7 | bb2b08f8a702401fe5ecd9ebb6ad2d1396ced5f0 |
| ku9-live.txt | 26684 | 343b196e20ce5ae0a653ce6823114a1345b60a72461c7d31aa3e4b07eadcb3c7 | bb2b08f8a702401fe5ecd9ebb6ad2d1396ced5f0 |
| live.m3u | 50364 | b137d5328414459a2a9fdbc304e3d5a2f88865c739a36e31338f92faed6b7620 | 69f0dd20661871240e882164f2d10e8d65eca880 |
| ku9-family.txt | 26230 | 4cbdb8cfadbdd467685320f74c2a0cccec27e9e12b643e4308ddd326a5811f30 | a4959e79fa036f2edad5cd86c7c72175722a5b35 |
| live-family.txt | 26230 | 4cbdb8cfadbdd467685320f74c2a0cccec27e9e12b643e4308ddd326a5811f30 | a4959e79fa036f2edad5cd86c7c72175722a5b35 |
| family.m3u | 49538 | 1cdf2ab8bb6c3e8ffa0cfcbbc2e30f74cda1f37994e127d2008573e06ed2ea61 | e4c8d55ae0f99717d121176570aa747dfd108b19 |
| final-publish-report.md | 10852 | 629d465553eb486b72ea701d972fe828813caddbc6a8c68bc1f3271fb7f52d03 | 2c970aeeb627c82eaa4e340537aa20f44b922f37 |
| coverage-report.md | 2170 | 771f19ce26707983098aa54de64fbf882715a9bb885e162003e2231a928b196a | ca4dcbd605dc172dd1104f2ede2393eb9e0d6f80 |
| quality-audit-report.md | 4681 | 07f57666631f9fb201b0fb3c818d3e26c083151a533feb7605eeda3ee37e091d | 7af7f21c6814049da8513c2e9f229c0e1b189e05 |
| publish-guard-report.md | 1537 | 98a2f70d1ded2f37d55fd2bd71483eaf7c18d41f7aeaf3d1cca54c75bcd08783 | be9213e1c5dbe5cd89f0da2cdc51e828204e9895 |
| published-recheck-report.md | 29093 | 502e84ffde3f069012d0ea6996b7f774acee172d72a27436f48193ada0694514 | 54810f2ca1d5e222b69e3a5193840d4d1cefd507 |
| source-report.md | 7871 | 21a139e534eedb4378f0dbef12cd729414cf36eca06274c978b1438778740611 | 9a691f098e1956621bfcf03c4def7f3257002acb |
| check-report.md | 7871 | 21a139e534eedb4378f0dbef12cd729414cf36eca06274c978b1438778740611 | 9a691f098e1956621bfcf03c4def7f3257002acb |
| curated-report.md | 1804 | 57199a4b93dec1e82eb5ccb7e6e455f3b2f585dc39ac503c2f587b233903d116 | 60578c6d7f6f1148f0528370227e6d6d250e96ae |
| sources_status.csv | 4079 | 40c2b2982781832509711dc0bcca76352205b64b3d35e29261b389c4da502ecb | fcd3abbfd640f9c9101b4229a697a020412301d6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
