# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 331898
Unique payload blob bytes: 264939
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 39500

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19750 | ccbc699d45f32b5e9232e3903e4a63b0812c0d0b2379014ddd30519af988876c | e459e8ee82ff66a41fca25dd3c889cac214da106 |
| live.txt | 19750 | ccbc699d45f32b5e9232e3903e4a63b0812c0d0b2379014ddd30519af988876c | e459e8ee82ff66a41fca25dd3c889cac214da106 |
| live-verified.txt | 19750 | ccbc699d45f32b5e9232e3903e4a63b0812c0d0b2379014ddd30519af988876c | e459e8ee82ff66a41fca25dd3c889cac214da106 |
| ku9-live.txt | 22227 | b9ecc027cfcfaf8075edf2090afbeaf23753b8670273aa447375690608968c50 | 72627bdc1f1d6ae32d54845997a71f405732b623 |
| live.m3u | 38007 | 5cce11aed9b2af3f3cd0627f11637ef10a838b6e4f617aff3590d03bea1fdbe7 | f92da3b8ded22e45a4c8f9090402b72ff84a1996 |
| ku9-family.txt | 19315 | e5d540130f38c80caa18671ab35a32884e34812bc1f298b1689a8fc390a1acd6 | 1d41dcfb5eebccd8cc9597666f8b9f7f5a0ce221 |
| live-family.txt | 19315 | e5d540130f38c80caa18671ab35a32884e34812bc1f298b1689a8fc390a1acd6 | 1d41dcfb5eebccd8cc9597666f8b9f7f5a0ce221 |
| family.m3u | 37200 | 1d7380da99411ca481903364e1abaf4e171d4391fc9e6a131b9330ad59f2c42e | 9b43de83d132b20424bc5dd5c9ab1e475788aa75 |
| final-publish-report.md | 10870 | 3ac9f324d916a01d5067527e69a92d754d896fe9b6185b20ee093c7521a1eb2c | f671f662591b3328bdc08fa8b3696e099f33b104 |
| coverage-report.md | 2180 | ba06bf288d5a31eb168c9051bbd062cc3ce07424da010de0c79d0bd2b008be33 | 94f7d1d5ce2ed67215a14be4e0c893966b212125 |
| quality-audit-report.md | 4669 | 45545f3fb984079c4788afa777da2d927abaa399ff2e11ef1b39fa7e3d81b644 | 7db2dd5df3313bd28651c483c3b23dac5b32b4a9 |
| publish-guard-report.md | 1532 | 92ff327ea541398be8543a3dd1276e9563de1c6ec056d3d7af1cc3eae24c9d20 | 72160b20c9729177654545b7380c443ac8e9844a |
| published-recheck-report.md | 26421 | d923fccd056f2918c06f5acd1cfb84d288e10a0c272142e05fdbb1749ce3210d | 943c69a9d7c2e2ce5f17b435a0e955a63a733b06 |
| source-report.md | 8144 | 82f2a6d48386b03d2a086c1cd76d993945581fa1849cd856b4d0fcc10cf5f5ea | 58876f08ed44b3ae12559363a9281cc350ba090a |
| check-report.md | 8144 | 82f2a6d48386b03d2a086c1cd76d993945581fa1849cd856b4d0fcc10cf5f5ea | 58876f08ed44b3ae12559363a9281cc350ba090a |
| curated-report.md | 1834 | 743ec70595abbe4f6241d38cdbf3548dc28cffe6c45b29fd63bd13781f5b3ee7 | f606c6165288f9af41a95b435855f879854f35e2 |
| sources_status.csv | 4181 | c5a32feb0d9d367a497681a8a1e43f8f4c76932eb764f8107345de8e743cb6a2 | 194e9736c86036ad844f483ddc0889433f8e66a1 |
| tv-coverage.m3u | 50534 | 8feada4a546d8cb315b356aac3fa24bbf6731c26dcaea0fa7c82b0289dff7688 | 371af8f1696a191934532dc170e4041b015376e4 |
| tv-review-report.json | 11445 | b8434c594fd8050b87613e7c6fc0f626094edecb589b49ef85150639e56c833b | 05baca5fd6245394702f84a66e5d24526ce230aa |
| tv-review-report.md | 6630 | cf665722e7bbea0dbfe921015c031c24cc97d38610548a18ee40e261faf79172 | 14ef7bdb0ea7c8dc74a7c457ea31043ab86a3174 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
