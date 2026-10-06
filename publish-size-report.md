# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 277945
Unique payload blob bytes: 184738
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 64053

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21351 | c63209640408cc0778fd92b355d61d9b78afbaf98a23b32f740505f28c0eb018 | 6bf9f01d9a9d246daab49a591cab14832425d678 |
| live.txt | 21351 | c63209640408cc0778fd92b355d61d9b78afbaf98a23b32f740505f28c0eb018 | 6bf9f01d9a9d246daab49a591cab14832425d678 |
| live-verified.txt | 21351 | c63209640408cc0778fd92b355d61d9b78afbaf98a23b32f740505f28c0eb018 | 6bf9f01d9a9d246daab49a591cab14832425d678 |
| ku9-live.txt | 21351 | c63209640408cc0778fd92b355d61d9b78afbaf98a23b32f740505f28c0eb018 | 6bf9f01d9a9d246daab49a591cab14832425d678 |
| live.m3u | 41066 | dc0d223390c68bc8d703c87c4d508620612477dce0a2506d0d37e1ee74261904 | baeecf51955cfdf3f0eee0b1e2f431f052944fc5 |
| ku9-family.txt | 21086 | 3116813f3d94140886d7c60afd315a5e7dbf8d0c7281c839ee6fcbebe551e69f | 93c54f6daaab2704bead0a3b59d995e2395dd3fd |
| live-family.txt | 21086 | 3116813f3d94140886d7c60afd315a5e7dbf8d0c7281c839ee6fcbebe551e69f | 93c54f6daaab2704bead0a3b59d995e2395dd3fd |
| family.m3u | 40553 | 5e3b8fc4742b8b2395775f4ddff218c0392efbc451d867a46a6b781df8a36da6 | eaffaa645760f7d4a9032a460fbfa77b972cd433 |
| final-publish-report.md | 10656 | e5007b5e8f4fc85327aeb7ac61cc8948c005bed8b2afe7073e3cf19a00a7b48b | c9df3197a4a423edd936f22638fae29cde12c00d |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4725 | 9b7190e53edd4f959e1d64ed8729c9dfe5ea7a957fd981868560b18647c6c347 | 7baf6dd71f1c0b8a57bbd9e26fb5d41cd8b88af3 |
| publish-guard-report.md | 1606 | 98078df48f91503c45ef5eec5d0ae5bada7005fc90e7d30db7d03b0026b00669 | 27c49bc27b71478ce87515077a3ecb21989e1295 |
| published-recheck-report.md | 27486 | 41757ad8f3079f669c78dbafeba12a9bd4fd68d850b1677a9b9c2fed8087f696 | 45709f03b0e90699174498ebb285b96defea3181 |
| source-report.md | 8068 | c32adb6f2226f982437b67342f9f8d43d0fde2bc66e4adecb396d69fc13eaf55 | 2c688cbb6878fbfd8d62d8c3624a3b9b217c3281 |
| check-report.md | 8068 | c32adb6f2226f982437b67342f9f8d43d0fde2bc66e4adecb396d69fc13eaf55 | 2c688cbb6878fbfd8d62d8c3624a3b9b217c3281 |
| curated-report.md | 1804 | 76847fd4e0cfd70aeade158797ec3892ff3eb656779c5b6793eda6d55a8cd28b | 9e47626195c3a19b66f1ca653aedca1a6201633c |
| sources_status.csv | 4107 | b393c17f644211ae201a40d0fcc275bd4bee15a7f2f1abb42b2d1e36aa2365c8 | 21038cbd2b5a90959ca0849a4e9da6bafea124f5 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
