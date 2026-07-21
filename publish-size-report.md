# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2483894
Unique payload blob bytes: 1709072
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 670788

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 223596 | db43eca6e7d1f0e406a5e432c7be0c4205b9fa94b9e3880729743b34577b5c91 | a00143a13c09b6b8447af35971dc7ed4c198f10a |
| live.txt | 223596 | db43eca6e7d1f0e406a5e432c7be0c4205b9fa94b9e3880729743b34577b5c91 | a00143a13c09b6b8447af35971dc7ed4c198f10a |
| live-verified.txt | 223596 | db43eca6e7d1f0e406a5e432c7be0c4205b9fa94b9e3880729743b34577b5c91 | a00143a13c09b6b8447af35971dc7ed4c198f10a |
| ku9-live.txt | 223596 | db43eca6e7d1f0e406a5e432c7be0c4205b9fa94b9e3880729743b34577b5c91 | a00143a13c09b6b8447af35971dc7ed4c198f10a |
| live.m3u | 399986 | ff02a79a52568e5b48bb34689aabfaf1d6055eebfd4ba081d8a05bee0f893a03 | 48676828c138aed27aed7d8fd16dd3a933c5d742 |
| ku9-family.txt | 98168 | 5f3eee73851c22cd5fdbd8fcc58cf00e755e6ff733fdd8bb542fdbdaa07a5b4c | 8a9b5d22b43006d3c6ac84594f157ede37917a23 |
| live-family.txt | 98168 | 5f3eee73851c22cd5fdbd8fcc58cf00e755e6ff733fdd8bb542fdbdaa07a5b4c | 8a9b5d22b43006d3c6ac84594f157ede37917a23 |
| family.m3u | 177190 | cbf5613d4f36c72dd5aacf8c7144d51cac424f4a9116da14db650e7eaa620dfa | 9995844de82464838775003e3cf3c28f535ecb25 |
| stability-history.tsv | 744727 | 1b5c44c7675b39985cc78ff77783fa0868238bb557c170dfbe8e3594626e2a8a | 990982bddad6ee8c3d04d535a33d04764b6b8306 |
| final-publish-report.md | 11697 | be01b49370b3cd204ebcb8a61b7fa98c36575b6c1e52b33d3766d3f2390d8381 | d6e33b654753df9c20f2577a73181a6c3d376d2d |
| stability-report.md | 10519 | 58b25b93e204c6190d5d3e25f590ba65dab5e9c4ad9374f1d103266ca89de0b4 | c152be6993deaaa3a3af4f8bb498abe8491029fa |
| coverage-report.md | 1350 | 05b4cf7d9b7f94c85b92fbf876e8ce213db0a38ca1aaec254fb68d3dd191e999 | f82da5374fe90c5c0ba7d4336b04edb13bd57e69 |
| quality-audit-report.md | 1435 | 041865873a660ede925532b214771d426bc6c8aca74fc9f928d246ae94be9c8a | f1055036f8e72653c9d22090ef009d61f639360a |
| publish-guard-report.md | 789 | ef51631cce1d79b689f136d0c10083a284a09ea344585245152bc14437dafaf1 | 010b6911fb7ea65cede81c08115e3458c89684b1 |
| published-recheck-report.md | 27555 | 7b220c948870e2b01b2e9625a6dc33be7f01677a2021128389efe8b103987387 | 6168aaab1a37996ba6de22be451934a351e52283 |
| source-report.md | 5866 | bda146df54b09cd4cae979a5ca50146c2c0f07de26f63509f0067dd70933dabf | c77663d59fe0928902b078bec41233171487f91d |
| check-report.md | 5866 | bda146df54b09cd4cae979a5ca50146c2c0f07de26f63509f0067dd70933dabf | c77663d59fe0928902b078bec41233171487f91d |
| curated-report.md | 3591 | 8df99b178118880a0d0e0bde5d98aa6b4f56438df8be5d50a57cc1bd25e37277 | 552c564d64e140cc3388057c97d369612a0b8dde |
| sources_status.csv | 2603 | ab3ada532f936b87c2f9591ffded924a3e4451752a881bbd077241fdbc192f11 | 6b719d3a614c296911cd18e72e628b6a26a6c7d2 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
