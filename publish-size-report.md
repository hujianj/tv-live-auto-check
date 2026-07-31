# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2398695
Unique payload blob bytes: 1682955
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 614304

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 204768 | 618bb3438c507462b49f1d464092b1687bf8c881eff1ca0b50ec64575ee1b7d5 | c503071f04832008edfe0f5b200c159018b5704a |
| live.txt | 204768 | 618bb3438c507462b49f1d464092b1687bf8c881eff1ca0b50ec64575ee1b7d5 | c503071f04832008edfe0f5b200c159018b5704a |
| live-verified.txt | 204768 | 618bb3438c507462b49f1d464092b1687bf8c881eff1ca0b50ec64575ee1b7d5 | c503071f04832008edfe0f5b200c159018b5704a |
| ku9-live.txt | 204768 | 618bb3438c507462b49f1d464092b1687bf8c881eff1ca0b50ec64575ee1b7d5 | c503071f04832008edfe0f5b200c159018b5704a |
| live.m3u | 370356 | 53ec8ee4992e4838b49f2aba3146b5fecda121f5af0003d33b5fb30b16d162dd | ebf612075895b912d710e55ba6fc43ae49f4deff |
| ku9-family.txt | 95583 | 39e05fb07624253a58b55e8ebc73e99980f4a894d631becbd66150017ec6ddcd | d94ddaa898ed1b3051ae2847aa9704affbd52cdb |
| live-family.txt | 95583 | 39e05fb07624253a58b55e8ebc73e99980f4a894d631becbd66150017ec6ddcd | d94ddaa898ed1b3051ae2847aa9704affbd52cdb |
| family.m3u | 174113 | e1108f0ce6f5abe0db6912a7ddaad0262b131f208dca34cf717b2ef154559a44 | 4ab09433636aa345e494700c006dbf18e7be8250 |
| stability-history.tsv | 768643 | 50ebfcc26eac352a28bdba6c0953af192244002a506dba1bc78d99c5029d907f | f37f06d40f3175e7aeb49b46d33a86adbf68fdc9 |
| final-publish-report.md | 11534 | 7e297eef6bd05033b4033c9a35412292c971d5eb2f2fd4c3ecc7918b4da18ee2 | c25d53ee62a46e955e6c9686c3c4d9f3ee00bf3b |
| stability-report.md | 12928 | 1c0651f9c16f16bd62bdd5879a4be8d5bbc350f8ef15a231c068d76b875a6d15 | 905606010838e5aa91c2c54d51c0a7367e17c713 |
| coverage-report.md | 1310 | 5202d6bc3553cf3710c0b8ade5dfd632bb3d6cff6badbd141565c34ab6a9c3d6 | 88b1867697863ea1787b5f5ddf3064bb5b2693d1 |
| quality-audit-report.md | 1504 | 4ab53a75b3957980f7609365c442fc5163877cf49975f3e1961e2d363db21d16 | c69270dc93898fa63efc6937ae95cb71e51a6a66 |
| publish-guard-report.md | 794 | fa9aa9e1c192c94c62c3abcd4ac3d9a4e463ef553338f7310985aabd98d50a11 | 5e96d2f419e622a9251a8d2ebbaacfbb94382c87 |
| published-recheck-report.md | 29386 | 41db9b879c079b754719f97fc2818b1353bbdff362aaa805b5ffb5d44de91fbb | ac3e43fe4c0536585482bd46fdf223ad2852d8ce |
| source-report.md | 5853 | 572b61dde2d29fe55c2d38da81bef300a5a9aa18f293ef92521b78163c5aa207 | 4613bdc1feb0cf5b144d496fc8286e858ba0be98 |
| check-report.md | 5853 | 572b61dde2d29fe55c2d38da81bef300a5a9aa18f293ef92521b78163c5aa207 | 4613bdc1feb0cf5b144d496fc8286e858ba0be98 |
| curated-report.md | 3583 | e796134d424b901a7d5c888caa36bee6a80c11ecc44c7addd70f76bf6096e019 | 4422a16736469346de6638493572e74313bea6c6 |
| sources_status.csv | 2600 | 6f653c4fd112671eccbb015fb071d1b6ebc50c5d657c09c90b2fc9dbb6238816 | 3a1d5acf5a6fed6b0cd5729d522604b4c1498eeb |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
