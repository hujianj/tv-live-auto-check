# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 281040
Unique payload blob bytes: 186152
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65295

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21765 | b67a6b15960af4fbae996e407fee484c26cdf54b5bb1318317a6a4fed9f3fcff | ebff429d38482e189402b528661a96155ad67771 |
| live.txt | 21765 | b67a6b15960af4fbae996e407fee484c26cdf54b5bb1318317a6a4fed9f3fcff | ebff429d38482e189402b528661a96155ad67771 |
| live-verified.txt | 21765 | b67a6b15960af4fbae996e407fee484c26cdf54b5bb1318317a6a4fed9f3fcff | ebff429d38482e189402b528661a96155ad67771 |
| ku9-live.txt | 21765 | b67a6b15960af4fbae996e407fee484c26cdf54b5bb1318317a6a4fed9f3fcff | ebff429d38482e189402b528661a96155ad67771 |
| live.m3u | 41796 | 5e57b457455b575573b094b81f1eec43e0003c7043b77636f5844bc1055dd6dd | 42b813f8a9ad42c6ba91307f9a403e8988430aec |
| ku9-family.txt | 21500 | f179282235c2013288bfbeb784a98db70b7b514a84bf25c742f381ae9105e37f | bb3f46dd8d72fbc18f2d5b8f3c18226c16db40aa |
| live-family.txt | 21500 | f179282235c2013288bfbeb784a98db70b7b514a84bf25c742f381ae9105e37f | bb3f46dd8d72fbc18f2d5b8f3c18226c16db40aa |
| family.m3u | 41283 | f9748f9c3df7028120fd5a6e527d2e5c086c7a8abc1351612bf093a6e1361670 | 12d0468f1b9902c54592da467e08456ffdbdf2e8 |
| final-publish-report.md | 10640 | c9d0fce74d5ee166227061061f736f4a8a55a1cd5bc856ed690157d9270ee8ea | b00b2504d89a02cf8a8ab773f8144a52be2f4759 |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4725 | 5a4a7be482074c0fc72d76a2f1896ead5d0f4c231c26f717439fc192903589df | c2c16695675378f6ea96e2f4d8dcf443b879dd9d |
| publish-guard-report.md | 1607 | 738035065dd8be707c63e411423853e3ef286b370212d9f5fb54b31dcb3890e4 | 5270ecf6a28bae37edb9aca01a65edb8b4619093 |
| published-recheck-report.md | 26571 | 7a73fc072f04510e7d6ca933904492eaca17ec164cc91b764ea6429ce44f7bcf | 31e20b8b240f04e92746aba6469e087bf88d0b18 |
| source-report.md | 8093 | e04fd06a23d404fca67cbcb344c48ed682a3fe21ed5a515ad989fded8f218ff1 | 553d0c587a389eb320e82994ce308045113ea8fa |
| check-report.md | 8093 | e04fd06a23d404fca67cbcb344c48ed682a3fe21ed5a515ad989fded8f218ff1 | 553d0c587a389eb320e82994ce308045113ea8fa |
| curated-report.md | 1804 | a4af4c205e05a2271cf11d9cf287291087591c00c79999337507eaf235b13be6 | 499680e9395f1f7cfc0ce5bd94118f1313c17280 |
| sources_status.csv | 4138 | 34dffe191971be215a4183061fd1fd3caed3a342c13adee2ced1b8799c7c1f04 | 5305a2c434d293bb2b3c7406796bd226d0c345f1 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
