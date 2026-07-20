# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2454741
Unique payload blob bytes: 1691706
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 659088

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 219696 | 77f5eb0a36524e8a89a8190151550bb1c9a29729b3fbb8cf23ff44519a5d9e7d | dd0ea224d1679b3f139a4d75f78d192e72e897d9 |
| live.txt | 219696 | 77f5eb0a36524e8a89a8190151550bb1c9a29729b3fbb8cf23ff44519a5d9e7d | dd0ea224d1679b3f139a4d75f78d192e72e897d9 |
| live-verified.txt | 219696 | 77f5eb0a36524e8a89a8190151550bb1c9a29729b3fbb8cf23ff44519a5d9e7d | dd0ea224d1679b3f139a4d75f78d192e72e897d9 |
| ku9-live.txt | 219696 | 77f5eb0a36524e8a89a8190151550bb1c9a29729b3fbb8cf23ff44519a5d9e7d | dd0ea224d1679b3f139a4d75f78d192e72e897d9 |
| live.m3u | 392564 | 8a1f9fabfe2f7256cfb2371649844ad34247e2ea9fa7ddac198c13e5fa2f352a | fea7729a6d09e01920d918b69df08e8a3bbaa8f1 |
| ku9-family.txt | 98107 | ba2f886af02d14c8415d16f2c968a2d8e79e29af52d2430f9d02325afb1afaad | 9371226871c99b64965691c506e89d06fdb3b704 |
| live-family.txt | 98107 | ba2f886af02d14c8415d16f2c968a2d8e79e29af52d2430f9d02325afb1afaad | 9371226871c99b64965691c506e89d06fdb3b704 |
| family.m3u | 176574 | 5055d71d6e1bb656c1a20eda539f70bca59112050690c270af74fab013039d3a | b7736954abe5384d04199268da0250ea0fa077ef |
| stability-history.tsv | 742161 | 488e37a24110e1ab6ac02eebf2ba61f0ff8de9f1d4cbef1e1df77df2222c078e | 6d0a6f888ecd61e10369d95898ce1e4850ce79c8 |
| final-publish-report.md | 11760 | aa592ae570ab7cc16bc1b1d98c93f87a411534091a12713a09aff27ed8c4058e | cdfc5c9d2b83d76c3b9645aa78a5e9e23ac2879c |
| stability-report.md | 10523 | 6c735a3ff83ba30543f3a566fa189eee0f5c54a93eb7f1a92a341fae12ab61c3 | 7fbb4b407ec722eed7e25ce839cc5198490bf64a |
| coverage-report.md | 1349 | 6ea48a526e750d00a9a9ba7cd4cce637a3d395f0815b27d672172c69ad5addb6 | 30e5a5b345eba59c61da4ed390f53b0b4977a71a |
| quality-audit-report.md | 1435 | 898a3d995eecd89f195f6ccc30d06e3a4c48b533d733341d08643b19d8721335 | 00ded13134b9d56140e87ef7928085799dd6c413 |
| publish-guard-report.md | 787 | b06f156342135deae403da9754050f09601f149fab7d7a519e5a9d4065b205f8 | 2f98d6128744422c9adbfe932406c59cf368f1e0 |
| published-recheck-report.md | 24707 | 05c21cb6438549a846bbe6876f32826b879bc403748382f524965f8ea6907149 | 5d988da0517199f67ba48d333acbf0b46aa8d87e |
| source-report.md | 5840 | ff2540744d4202d29b9a765845ee9f90d9112d2ff2efcedbe0ddbf54e3f982a0 | c6cf16bafce718e41bc0104a58ae5760878df69c |
| check-report.md | 5840 | ff2540744d4202d29b9a765845ee9f90d9112d2ff2efcedbe0ddbf54e3f982a0 | c6cf16bafce718e41bc0104a58ae5760878df69c |
| curated-report.md | 3600 | a3582cc392936097ad2cffe2215a1002018668bacaac4cfe8514b3f1909cb683 | cd0ce4a08b7b7444e20b78fb22266f66f4c128cd |
| sources_status.csv | 2603 | 577749c3c5e022132eeae37b60777f32098bcb6229eeed9e5527f7120ef9692a | 3df67acbcc33c5c02cf11dbbba82bcef2aad00b6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
