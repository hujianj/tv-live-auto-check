# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 309955
Unique payload blob bytes: 203967
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 73794

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24598 | 7b0224dde4a6207616be5e57617f8cccf7b75d4205389229e094efcd4d345226 | 43e496d00886d06d954a71edce73b029685865bc |
| live.txt | 24598 | 7b0224dde4a6207616be5e57617f8cccf7b75d4205389229e094efcd4d345226 | 43e496d00886d06d954a71edce73b029685865bc |
| live-verified.txt | 24598 | 7b0224dde4a6207616be5e57617f8cccf7b75d4205389229e094efcd4d345226 | 43e496d00886d06d954a71edce73b029685865bc |
| ku9-live.txt | 24598 | 7b0224dde4a6207616be5e57617f8cccf7b75d4205389229e094efcd4d345226 | 43e496d00886d06d954a71edce73b029685865bc |
| live.m3u | 46929 | 20e5f5572f1a4f2f74d91d34c78a43cfc726a832d0b577cd2bd271dee1ee999a | b5200368c0aa4831a06236cb95d9aa38cee3939b |
| ku9-family.txt | 24163 | 38fa22839ff2772058cc8f29bccdcd08e4389ad26bc48702161159843b985739 | d2e15f942c98f04af12deecc6083c452edb028a5 |
| live-family.txt | 24163 | 38fa22839ff2772058cc8f29bccdcd08e4389ad26bc48702161159843b985739 | d2e15f942c98f04af12deecc6083c452edb028a5 |
| family.m3u | 46122 | c613bee48149b710822462a1d97596fd53fd57d480bb9d5a8490d62640e20b74 | 8fc22af7f68c3c6a00ea205d8643398452b09971 |
| final-publish-report.md | 10814 | bedff11d5b1274953c548d8fdab343436115d54f7350ab1cac0f1b8a947888fd | 011b66aef3b2c34735f0d306abd7ff91774d4e5f |
| coverage-report.md | 2220 | 5a5be94b83d512ca0e2b90eb00d18c480d25320cef5599c7e53de9765c9c5d08 | ea0a42a71fb36dd08b6cd0ee07bf850bed916864 |
| quality-audit-report.md | 4718 | acd55aff3ee0c2ee2fa437f0660fb7bad69a6b2444b1dc31bee1b721723537ae | 1b5f98564ce51ef5b8cf4b44171a9f39029f7e28 |
| publish-guard-report.md | 1528 | 93deb39ed2300394fe67c1349956b04d0980276bc0e8f005c4e4304a7f1fae29 | e7d455a4cc30fccae8529349931f76c204a65c4d |
| published-recheck-report.md | 28903 | b7509eb6cf805cec742e0e02b764dfa6716ec639df9c5cd4e444ba8e7ad823ec | fe52c0ea1d2fb8c5ed0008972ee625a853e99257 |
| source-report.md | 8031 | 3a3300dd25b8c4f237b8ec8c83b2bd49322c1d02b230dd95d42b01741af1dd92 | f5ee7d7249e93c989d81cb45a293f58df56e8c1b |
| check-report.md | 8031 | 3a3300dd25b8c4f237b8ec8c83b2bd49322c1d02b230dd95d42b01741af1dd92 | f5ee7d7249e93c989d81cb45a293f58df56e8c1b |
| curated-report.md | 1861 | 020c749e50c906ce3a911e8fddebbb545cb74f6de4e6ddf8bf42507abecd4062 | 3ef21be86a7da5cc13ea487b7a893ae70ef110ee |
| sources_status.csv | 4080 | ccf05ed533c0b353bfb8994bcad8359e4e380ad4cc61eb21afc91008b927cd26 | ccdc4de0f808248a441b5ed66974eea4218db587 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
