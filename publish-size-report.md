# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2027803
Unique payload blob bytes: 1464878
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 471477

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 157159 | 8f538414698e17433b3d45aff5fc33d1275a61153db886754fc0238c4a19a0cf | d6e5536d7d78a48b0bf0aa318a22b9993b72587c |
| live.txt | 157159 | 8f538414698e17433b3d45aff5fc33d1275a61153db886754fc0238c4a19a0cf | d6e5536d7d78a48b0bf0aa318a22b9993b72587c |
| live-verified.txt | 157159 | 8f538414698e17433b3d45aff5fc33d1275a61153db886754fc0238c4a19a0cf | d6e5536d7d78a48b0bf0aa318a22b9993b72587c |
| ku9-live.txt | 157159 | 8f538414698e17433b3d45aff5fc33d1275a61153db886754fc0238c4a19a0cf | d6e5536d7d78a48b0bf0aa318a22b9993b72587c |
| live.m3u | 282279 | a466f3a7bab451302a1c52d67bc078cb1da1fc21002cd3ef7ce4ccb31ef31456 | a60b8fe3e0a1e66cca45846c1e67261efb45be6c |
| ku9-family.txt | 84802 | 0673d68afe3bcb51658a7190400248d65c8aee0ec464e6a063a65c439b6bba81 | c2af54469574bc832f43309913731f0acc08a45d |
| live-family.txt | 84802 | 0673d68afe3bcb51658a7190400248d65c8aee0ec464e6a063a65c439b6bba81 | c2af54469574bc832f43309913731f0acc08a45d |
| family.m3u | 151076 | dbe8f721f904f3466549c610404048b1304f23405fc2ba3efd01aec6b86db824 | c086bc26a117179be91caf3862e471cccedf48b3 |
| stability-history.tsv | 720590 | 4239de30fe871a8f3b4ccf20d38a6c0c3ab0aa75b1aae171db1ce042306654f2 | c967de8a839355ba8620ae257f47fb9003477208 |
| final-publish-report.md | 11952 | 24ff7871d16b009d82451df758d386112d63cbd6643df90dd150999ac8471052 | 817a3dd8ca093718381f38bc6e19a425156a3ee9 |
| stability-report.md | 11676 | 7654dc2c5a04c1e4ba7646efd547a279614820947a9e05e72b41c399bd327f8e | 4473d18334e87af07b36a273bd39f353ca7924ee |
| coverage-report.md | 1291 | 0483300cbc64b6067b5932ce009054597dec601a1184680043a11b9903076ce5 | 159f6f84903a1757cac009e3d010bc36d5695646 |
| quality-audit-report.md | 2141 | c60099c2ffd5f4e30395e2521d52f5789540933cd08428268d3801750ba21457 | 6d52a2830865a55146c2357a4db3299066511e49 |
| publish-guard-report.md | 1142 | 3473e7822c4d6509bd4e3c05be61890461598d264dd441a12ed023549acbec1a | c281f5a5ae010bfc19b79647ce4cc1abfd436ecd |
| published-recheck-report.md | 27641 | 2226fd836937ad29ea11d6b524e69ba02a7110794e30499a2d21aceed758088b | 62df5ca20e9e65c84efefd955207c329bb7f9555 |
| source-report.md | 6646 | 7a453d44a6594c5bd19ec7f973198321f72705cd05ff1666a8ef02812526c265 | 054be7d7cfa4840ddcc69d144a921cb47b00c352 |
| check-report.md | 6646 | 7a453d44a6594c5bd19ec7f973198321f72705cd05ff1666a8ef02812526c265 | 054be7d7cfa4840ddcc69d144a921cb47b00c352 |
| curated-report.md | 3348 | e34dc24877d8ea3cc0423c7bef717c7ff9bb2bec3bf19133d5d3c60ed8ba5e10 | 3005a507c3d53959963ec6d411dfdebc607d2f2d |
| sources_status.csv | 3135 | 2adf4fb70e9477f88c0f25a761d09f2b32b2f77b6eb68410278926005a82ff1a | 0a21625a623dbbd57396ff70ddfd86ffc9deeb46 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
