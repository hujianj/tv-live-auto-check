# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 243658
Unique payload blob bytes: 163078
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 54687

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18229 | 98f3ddcea77aacdfde93d90d6df59763ab3c5372b0df32c1bd5806be6baf2014 | ffe6978329438f453e0d323a962cca034a609eb0 |
| live.txt | 18229 | 98f3ddcea77aacdfde93d90d6df59763ab3c5372b0df32c1bd5806be6baf2014 | ffe6978329438f453e0d323a962cca034a609eb0 |
| live-verified.txt | 18229 | 98f3ddcea77aacdfde93d90d6df59763ab3c5372b0df32c1bd5806be6baf2014 | ffe6978329438f453e0d323a962cca034a609eb0 |
| ku9-live.txt | 18229 | 98f3ddcea77aacdfde93d90d6df59763ab3c5372b0df32c1bd5806be6baf2014 | ffe6978329438f453e0d323a962cca034a609eb0 |
| live.m3u | 34291 | c6f4c5073c0d34b408b583ade9dd1e27504a3d3b229cb0cd58176c281693515d | ab7ac2bf4f0cc47eb3586a4f20bb8686884fa6e3 |
| ku9-family.txt | 17807 | fee288544d6fc062b196045d3a45e825d2c6020a1a80fc8f832396ff9c178de7 | 17bf53271380f3d81a9ca3ab05b9e9a77d090a50 |
| live-family.txt | 17807 | fee288544d6fc062b196045d3a45e825d2c6020a1a80fc8f832396ff9c178de7 | 17bf53271380f3d81a9ca3ab05b9e9a77d090a50 |
| family.m3u | 33497 | 5beb241a9b7c118c942cfb2a7a2a336784c82afc5820e21954c3e582065f73fe | c9f8e455a536acbac5ad198d9e1a5f5f7e5da6ce |
| final-publish-report.md | 10774 | 9312f9fe7370f2c5a8dbfd0fd51a545704a7afaa0c340284accadf45d6875e3d | 9791d4129f3317df02d10be78baa75b3bd74fa07 |
| coverage-report.md | 2235 | 70edb1ebb43e774eb9630d32dd0fe1a351ca34b12ce8a23c827d4e7164ee1c6d | 9384963ca42b433c7716b3c4669fd79e6c55772e |
| quality-audit-report.md | 4789 | 5a6ec415401a6f7c756be10beb3764067d96f1d6823a15281848e7b6f9d09ee6 | 1fd55229077038788f7e2b1af3cad7cfa6eb0442 |
| publish-guard-report.md | 1612 | b486d307ab2806fdb3a2c9831e49ff05289f63be1110c26e42efc00c8366e9f7 | 8bbb61452a27a92afe209b0117052c820eee74a3 |
| published-recheck-report.md | 25813 | 67380f13cecec6306b8af75c8177e9acd31279d6fb6278f101c50287a460a14f | 5b44aeb3df2d6cefe50924f0f23724bdb9c8f58e |
| source-report.md | 8086 | d5de529d3fa553d2e1b4028dd3c8c319508fa848f275df959ed4cf54af678853 | 4d30502fbbc0d3ef14e87bfafc4bafdb7002fe0b |
| check-report.md | 8086 | d5de529d3fa553d2e1b4028dd3c8c319508fa848f275df959ed4cf54af678853 | 4d30502fbbc0d3ef14e87bfafc4bafdb7002fe0b |
| curated-report.md | 1804 | fc06be0922b933e2ea4ab1d852e3c46a8ed9b03195d5daa75a12cf1c1ad4ebe1 | aa79f4531b5b902582053b621a1745a433a5a5c9 |
| sources_status.csv | 4141 | 008968c30d3ea4cf61442228d302ec28682b4f440f885cd9d7d05201aba8ad4b | 685e12258f6956a17fa0a58b651858d9aa3d0473 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
