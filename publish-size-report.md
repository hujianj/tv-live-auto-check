# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 305607
Unique payload blob bytes: 201687
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72204

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24068 | 6550400790fd35128452eab86d19a8274a379929b7f4073a7b206920539659c2 | a3548127e07c5a4e53b68fbf4d3508afff05db42 |
| live.txt | 24068 | 6550400790fd35128452eab86d19a8274a379929b7f4073a7b206920539659c2 | a3548127e07c5a4e53b68fbf4d3508afff05db42 |
| live-verified.txt | 24068 | 6550400790fd35128452eab86d19a8274a379929b7f4073a7b206920539659c2 | a3548127e07c5a4e53b68fbf4d3508afff05db42 |
| ku9-live.txt | 24068 | 6550400790fd35128452eab86d19a8274a379929b7f4073a7b206920539659c2 | a3548127e07c5a4e53b68fbf4d3508afff05db42 |
| live.m3u | 46134 | 6a108f7da62f01c54a3c8c272793d00ee8a95860469522b578d8d4c220c4f5d9 | 5923eb358a6c46aabf9b82e0bfe26b15cf7338ee |
| ku9-family.txt | 23652 | 67fe5a40ca3bfdaccb1202d2d57c7ab3fa5adb85e6c9021ad59a631a934532af | 2c8bc41a761c0804bb362a045532b0010d6ca93f |
| live-family.txt | 23652 | 67fe5a40ca3bfdaccb1202d2d57c7ab3fa5adb85e6c9021ad59a631a934532af | 2c8bc41a761c0804bb362a045532b0010d6ca93f |
| family.m3u | 45346 | 94da1c777a9b780824615924be17f7c715513a89efc9f5238e44c7449eb6faa0 | 1f9f5128fe33fa94363dbc8407b51d288212ab10 |
| final-publish-report.md | 10690 | f4a170fcd49386941f1221fe03437f6595910659d3a0600ed13b941d11967cb7 | 23c810748679bc70406163f03416e0cc5a0bd024 |
| coverage-report.md | 2220 | 00b08747ba1e76f18a0b8cf95f2d6cb4202803da7de087fde643176730bfa514 | aa9f8814d342939ab9c182ee4b5fb381447d2510 |
| quality-audit-report.md | 4718 | e8a95571cfbef3d12030d0a8119b238ebfdd02144057a7d0f7425888c2d9b58f | ee168e63ff0833e517ee8ed59f5bb7a8658a87a0 |
| publish-guard-report.md | 1559 | 314bec46671961a7326f89d439dba0fc9ebbf5dad811eebdfe6f094658a2fd5c | f2a1134e2f16ad38f406a36b7ca93d526961c375 |
| published-recheck-report.md | 29267 | 58bc238897ac6651f81d05bc55ad98f9f58868c8df59c030da29767e0296b628 | d4bef77ad19fa5ba8a658791bb6cd251896a5ca5 |
| source-report.md | 8064 | 4a16ce4fa9f716e885573e8134ebbb2cd304eb4a3e5e09122bb962540cda183f | 551ccb21d638593a0e0e3ed56d1ee1ce2f1265dd |
| check-report.md | 8064 | 4a16ce4fa9f716e885573e8134ebbb2cd304eb4a3e5e09122bb962540cda183f | 551ccb21d638593a0e0e3ed56d1ee1ce2f1265dd |
| curated-report.md | 1861 | af3b89ae30690f6a4b158feacd8a504f5a0b12e60c93dac48e84b2bb31edb9c1 | f2609c6edaab2f36a629219b11c2d6626fb08ef7 |
| sources_status.csv | 4108 | 83eaf711543c66a383221e69d07a2a1904d0536c26edc46189e7d227ff736707 | 4370d16a57448b3a751f2f98f1ca0dd186d19d58 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
