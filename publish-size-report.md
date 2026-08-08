# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2463163
Unique payload blob bytes: 1713022
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 646386

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 215462 | 079926cfe518786d02f03ef3bf047a3c2331a8c7e3464b0bde8c5215c8764dbd | 2910663e12605e8cc3ba6f280e135564c314145c |
| live.txt | 215462 | 079926cfe518786d02f03ef3bf047a3c2331a8c7e3464b0bde8c5215c8764dbd | 2910663e12605e8cc3ba6f280e135564c314145c |
| live-verified.txt | 215462 | 079926cfe518786d02f03ef3bf047a3c2331a8c7e3464b0bde8c5215c8764dbd | 2910663e12605e8cc3ba6f280e135564c314145c |
| ku9-live.txt | 215462 | 079926cfe518786d02f03ef3bf047a3c2331a8c7e3464b0bde8c5215c8764dbd | 2910663e12605e8cc3ba6f280e135564c314145c |
| live.m3u | 388041 | 2da71b9aee2ccbd9bb66e81afad812df44a19aad9d4455174885c275096b35d0 | 57960537c902a7119beb0b2f060e90040296fe97 |
| ku9-family.txt | 97898 | 9be7199d547d984fe7cebda9c753e1469a3ef4507d646934ab196af2bf30e55d | 5cb855c8f403c2d9bf9628259f1ea59705e8242b |
| live-family.txt | 97898 | 9be7199d547d984fe7cebda9c753e1469a3ef4507d646934ab196af2bf30e55d | 5cb855c8f403c2d9bf9628259f1ea59705e8242b |
| family.m3u | 177491 | 984eca262ff58b554f7f244225af439323c3e6f5f0c39ae65966e920532f1aff | a08a0b551cf5fcd1af3591df267364dcfa04e5cc |
| stability-history.tsv | 765188 | 444bd8ceee6f08cef8167ba2b88abd21f3fe8c622474380ce13b114ebdec1fa0 | 9e3139697069b22ec54607e175418674d47882f5 |
| final-publish-report.md | 12106 | 8682ebf0efadad94eed864e34fbc25d6dafcb97f8990cae4ae01227749316bc3 | 6030fb658f28669a39f4a441c98f7c6f0b20d803 |
| stability-report.md | 11867 | 5d1bef069985a1cbe5455352a6c7a791bc023da66257f7a49ca7f40e19ef737f | b045101cb0f218c8c3cfe10b9404d377537e8b18 |
| coverage-report.md | 1329 | d49412cd40a1fd9a014b6082c4158707dc2893c2f5711fb981c113d530cbac40 | a084357a9982b706494e1e06eba61a28fea3229b |
| quality-audit-report.md | 1435 | 529949470fde71456df3456b6abfd79a5bc91dba6203442dbc18fcea2327a95e | 6634994f1078c447841327af9e7ba2571eaa52b9 |
| publish-guard-report.md | 788 | 64b2b7ed9399cb1b6c2bc3d3c6f12913af411a6bb598f4106c19a0aad57b5f89 | 3409cec95d3e8500b20e62d6bb44be0933199cf4 |
| published-recheck-report.md | 29380 | c9900749ba16823776bef5eed04dda50e76fb7d845ae48ed5b1ea504e1860f34 | b6d9ecebc8eceb3720da691b063ba7fc2ad14af8 |
| source-report.md | 5857 | dfa50d5b32613b0c843a45bef4c4b52552145b2bd756a40e5101c7d77f5167ea | a50ddf5d4886791905041017325e689bba8f1d24 |
| check-report.md | 5857 | dfa50d5b32613b0c843a45bef4c4b52552145b2bd756a40e5101c7d77f5167ea | a50ddf5d4886791905041017325e689bba8f1d24 |
| curated-report.md | 3581 | dba9021ef64403804394dc760a6b216dd3de224daa00a3533eff6679b8c31750 | 0ce0d1d986036e0088ce11273c672e58102448f8 |
| sources_status.csv | 2599 | 09ef93ff470daf58bd1c19df1af088c5aa3f02622ca4caf201584eb1b88e0e72 | 8ffaed52ecfeb1e0151c4c1f1b722c82605adb2d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
