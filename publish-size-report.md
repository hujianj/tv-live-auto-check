# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 259897
Unique payload blob bytes: 173845
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 58764

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19588 | 904e8bf30bb55faeec538eb588daabbfa3ae9b694a920d8266636afc6af730cb | 2dea447e5a2cad970404f0caabe93ec226c5e056 |
| live.txt | 19588 | 904e8bf30bb55faeec538eb588daabbfa3ae9b694a920d8266636afc6af730cb | 2dea447e5a2cad970404f0caabe93ec226c5e056 |
| live-verified.txt | 19588 | 904e8bf30bb55faeec538eb588daabbfa3ae9b694a920d8266636afc6af730cb | 2dea447e5a2cad970404f0caabe93ec226c5e056 |
| ku9-live.txt | 19588 | 904e8bf30bb55faeec538eb588daabbfa3ae9b694a920d8266636afc6af730cb | 2dea447e5a2cad970404f0caabe93ec226c5e056 |
| live.m3u | 36443 | 8cb98ea43b77ca3af07bf95e471bb3481a9355bb417cafa7d6408339fa19cbe7 | 2db6f4b4a8494dff28963a56bb6a23f818f56dd5 |
| ku9-family.txt | 19165 | c8fea09cb08287d2dbd91525e28f1867f10e641043984684783c14072aae11f5 | 73b159fb2302f20528336c8702074f630c84c19e |
| live-family.txt | 19165 | c8fea09cb08287d2dbd91525e28f1867f10e641043984684783c14072aae11f5 | 73b159fb2302f20528336c8702074f630c84c19e |
| family.m3u | 35648 | 9f31b3d037bba8c17b1766f7038a06d9e01cc1b53204d43de7871f81d569e2c4 | 7059d7a8b5a11bda429c1862e2e9879e3e52469c |
| final-publish-report.md | 10995 | 7a5c8fa893270afb4986a82fdccf58017953d963682334d5d62fcb645cfe601a | f40f35e83a5d2e9c5c0831d50bde09e72c6a29e6 |
| coverage-report.md | 2250 | 6a3f9119c7eafdc47cf61972bb4df5fad6c70e736f3555c80ccb242edc731285 | c39468cc17a46b6cfaa61626dd97b5caaedd97c0 |
| quality-audit-report.md | 4745 | c6eac05fb6ab71eac53a1069198f8375e7aadbbb149c4ec1cf626416d852910c | eee9ea6f067e33ca085272e1ec04e46cffbb158b |
| publish-guard-report.md | 1670 | fa004101edc986d8899e830752493e96a3af141ffcb5106a30f0b90c7d94cc91 | 1e3c975ceb5a362a87e9247722e6be28a4f790ef |
| published-recheck-report.md | 29279 | f08e193a8225340b2ab756137d5b8ae7d0bb2150bbbf95ff56eea46385121030 | ec731ff68122ebf3acc3c7adb69cac69a2b94c2d |
| source-report.md | 8123 | 0236f09292c5fd32c9ca249b79578552b5af4173accca2f4071018143a2ec36b | 843dd4158e6791b723fd549231fdca94a6a013c0 |
| check-report.md | 8123 | 0236f09292c5fd32c9ca249b79578552b5af4173accca2f4071018143a2ec36b | 843dd4158e6791b723fd549231fdca94a6a013c0 |
| curated-report.md | 1802 | 18cd34ca6a6e1bd9a0d6bc4359eceada04d12a8c2da17b4e804b7d405f6845e8 | 81f4115887206156c684fe83fed1f59205f0c29f |
| sources_status.csv | 4137 | d886467d121d8e2fd612447e06ef924395e12cd0314b979e17d55fdc32caa4bc | d6e83e8a04d12e3c205edefb32fcd50d6965f2d1 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
