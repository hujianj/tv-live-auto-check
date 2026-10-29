# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 259921
Unique payload blob bytes: 173974
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 58590

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19530 | f125b5e857d0ec85df2f3b08941c96291673caba1f8cb0797becb919a37646d1 | 0295d4525fd622ef0aa10dcb09d804c033ab31f4 |
| live.txt | 19530 | f125b5e857d0ec85df2f3b08941c96291673caba1f8cb0797becb919a37646d1 | 0295d4525fd622ef0aa10dcb09d804c033ab31f4 |
| live-verified.txt | 19530 | f125b5e857d0ec85df2f3b08941c96291673caba1f8cb0797becb919a37646d1 | 0295d4525fd622ef0aa10dcb09d804c033ab31f4 |
| ku9-live.txt | 19530 | f125b5e857d0ec85df2f3b08941c96291673caba1f8cb0797becb919a37646d1 | 0295d4525fd622ef0aa10dcb09d804c033ab31f4 |
| live.m3u | 36889 | de3848cbd2822ec1e1236f9731f6382e9779cd527ea54a4fe7f59e61abd03ef3 | 4bfd453acdfbc6756d9eaa4352c4f27926ffa92c |
| ku9-family.txt | 19105 | 89892986cb3e960600f3fc51388af0ef87a381d68ffbef562de3ec119e588a04 | cd335be566061e26bb8b412c422fca5d821ea8d9 |
| live-family.txt | 19105 | 89892986cb3e960600f3fc51388af0ef87a381d68ffbef562de3ec119e588a04 | cd335be566061e26bb8b412c422fca5d821ea8d9 |
| family.m3u | 36092 | b983a9ef02b80c794741db863af1e89189d578e3500b5ae2e87123f06d1488d2 | c0e95b951f0765fc72a6488597bf43c331aec7a4 |
| final-publish-report.md | 11057 | e3b138e920f255741e9bc9d352b0d3642b54e3bcdc1570572b316d9a5ec923d1 | 2d43061ec82ec06cf148f06fa4a5800377a837b9 |
| coverage-report.md | 2200 | c088c2441ef74e411135c2590d894aba1d3a29a75761e8d451bded509efef4c7 | 19c2bcface9019651eff3c50c292181ef1383423 |
| quality-audit-report.md | 4711 | 52579a1b7ed3961a4e96f0a4fdb5686ae4785f05ea02848faa081ca3dd7c2930 | 2d13516015c218590e6ea8eae6a80a30385e37f2 |
| publish-guard-report.md | 1554 | 13e464411e8eb9e764649a60680400a6ffffede52830141159e27ca0ba79ffd2 | 3ebbcc8693efe10af6d654fce58cbb9e4f023e0a |
| published-recheck-report.md | 28453 | 8accc9057e8049e296f8b955bcd4b1b9b61b700922ae28282f2f7d412d1609cd | 29d44efdd3bdeb02bf457a4c8e7292929cdf8b4c |
| source-report.md | 8252 | 05828bbfbbf40c0d46cb828544f08b672044b131b95dd44005650c6961e43e04 | ba80972984bd73e2f8624cf0367003c04151e491 |
| check-report.md | 8252 | 05828bbfbbf40c0d46cb828544f08b672044b131b95dd44005650c6961e43e04 | ba80972984bd73e2f8624cf0367003c04151e491 |
| curated-report.md | 1895 | 68f14a18d7549f352ecb68d4d062462c3eec9ac944c05c3b5dd5caca20d55e14 | 023eed3e842e1b6302d7dace9f5e1786953b32d6 |
| sources_status.csv | 4236 | 123bea3f73b69eafb34003c681ac9412cf890005edeebde122f4230e4d7338aa | 1963ff707c0cc52487ffb148a75210f026d4e669 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
