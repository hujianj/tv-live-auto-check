# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2442703
Unique payload blob bytes: 1702115
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 637107

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 212369 | 56c73a5c0efa5a6a3d6f27d288b46bd5a84efa8722ef0cc5ded2258e26f64a99 | 0a334a50fd165f8f9a499c934c1f2031864ca5fa |
| live.txt | 212369 | 56c73a5c0efa5a6a3d6f27d288b46bd5a84efa8722ef0cc5ded2258e26f64a99 | 0a334a50fd165f8f9a499c934c1f2031864ca5fa |
| live-verified.txt | 212369 | 56c73a5c0efa5a6a3d6f27d288b46bd5a84efa8722ef0cc5ded2258e26f64a99 | 0a334a50fd165f8f9a499c934c1f2031864ca5fa |
| ku9-live.txt | 212369 | 56c73a5c0efa5a6a3d6f27d288b46bd5a84efa8722ef0cc5ded2258e26f64a99 | 0a334a50fd165f8f9a499c934c1f2031864ca5fa |
| live.m3u | 381221 | c9c88b2d88bc6b1d7c95537296b659fd3e1761a6ed8750da0ac6d5e337540a93 | 5ca930b0a2c7debe32f06633a701a68dc35d544e |
| ku9-family.txt | 97637 | 445ef0d4c3879dfae36b4de039fbaac5be67826a1b8273bfca7f52c1e7111e72 | d50821b2ef1a8cc48ab2eef6cfba188fd7e1bc30 |
| live-family.txt | 97637 | 445ef0d4c3879dfae36b4de039fbaac5be67826a1b8273bfca7f52c1e7111e72 | d50821b2ef1a8cc48ab2eef6cfba188fd7e1bc30 |
| family.m3u | 176225 | cb7c59ffb4e6992f6fd8a411ce8f7eca235d080fa9ed097a75f7a5dedb1ba33a | 730c94e87c49e78a5301212244636754984db032 |
| stability-history.tsv | 764764 | 73cb2b8308d1a2a49b860ae3a86737e8f5e1a141d761278e42cb9e435ae40d80 | 01c64c6c0a586298e9977b962c439e63122c5aa5 |
| final-publish-report.md | 12761 | 420e7d69692395e51b9d48fc9a421fdbb1f32b44bfa2fb5cb56352d15c115db9 | 4a2d7d81d6b89c7510d6c819b5c012e1c5d22444 |
| stability-report.md | 11631 | 0c2b7f8392a3d295fbea11d3cd1fac629515107c0f8e2824c81cfc9d4a4267e4 | b6ccf695bb95f8594e9d7ca1dfe07c22705cf777 |
| coverage-report.md | 1349 | 08b90bca68bac07379601429008cf7f0ab361e89df8b99350a1b01bbca4d2d42 | 7351b5b02e5d2fcb656038ff33682cdef3b4d8b5 |
| quality-audit-report.md | 1435 | 9d245d68df65d59942e44afc3ce2e7e5aa484b46713e711e41b1d6c379a07e91 | c8dc208329ac9d0de4eacd68b49ecd838adaee64 |
| publish-guard-report.md | 787 | 0d4ac6fd19a9e6ed680a05e9142ae4ad39761daedcafc3275fc5cf45e1be0d24 | 811a6eca2c29a904a3cd93c74286a7589cda6ac6 |
| published-recheck-report.md | 29900 | 777b5f650007c94048439dd92fcc7c54931d3d4d1b5ebce40f5c4eabf4ee0fa4 | 3918ba332a27198eaedd180323f67d5279254b4e |
| source-report.md | 5844 | 3ca5ae75d0c6164718aeb66a3096d6da5cc177235af2f5151a7404c04c667ba6 | 53678c2fffaab33d5ecb24a98498887822230465 |
| check-report.md | 5844 | 3ca5ae75d0c6164718aeb66a3096d6da5cc177235af2f5151a7404c04c667ba6 | 53678c2fffaab33d5ecb24a98498887822230465 |
| curated-report.md | 3591 | 5473436e47f3aa90d21aac960614baa81b71e65f30b694f84fe269788acb62cc | 33b2475488792381850c059a4de075c0e48fea4e |
| sources_status.csv | 2601 | 603923a2247bd144c0f4c4763b77a6b7a1058ed71ec710977e54502568c6a5fd | 1c06d6e255239fdb0c4493980f983ee84285c899 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
