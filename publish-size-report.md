# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 1989242
Unique payload blob bytes: 1442304
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 456981

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 152327 | 490b4997b98e20e4a79c2991409998d6e71553ef3e98c1d4ffd040bf0955f2aa | c1edfba1260e5d486116ca7386612b7e804e1f53 |
| live.txt | 152327 | 490b4997b98e20e4a79c2991409998d6e71553ef3e98c1d4ffd040bf0955f2aa | c1edfba1260e5d486116ca7386612b7e804e1f53 |
| live-verified.txt | 152327 | 490b4997b98e20e4a79c2991409998d6e71553ef3e98c1d4ffd040bf0955f2aa | c1edfba1260e5d486116ca7386612b7e804e1f53 |
| ku9-live.txt | 152327 | 490b4997b98e20e4a79c2991409998d6e71553ef3e98c1d4ffd040bf0955f2aa | c1edfba1260e5d486116ca7386612b7e804e1f53 |
| live.m3u | 281859 | 248a936197c93686d03895dea598d31737f6c4ca15b318a3eb81588e2fc90dd1 | 903f965fe924e14f2aa2495b2d1343c7e51db2fe |
| ku9-family.txt | 83421 | d5e98ec768d11512cf67a53949e925f66db4aa7f2752a24b54b1052d49a9b9fc | bfe5f17885e4022fb18694c298138d23aec69eeb |
| live-family.txt | 83421 | d5e98ec768d11512cf67a53949e925f66db4aa7f2752a24b54b1052d49a9b9fc | bfe5f17885e4022fb18694c298138d23aec69eeb |
| family.m3u | 152849 | 589a16406f2517b33beb0b84db0cd6614844252c01d65df6a221d54b24d130b3 | e6167f196cadf643ff41f95facc34542ca54ae1a |
| stability-history.tsv | 704205 | 66a64f800b6ee5b3815d58c637e300061637480e05313c76c269eb474b2c91f0 | b8471c2a0d204f1bd67831498dcf506c6e718dfd |
| final-publish-report.md | 11715 | 6d3ea72bf29ac62cd4d5a96f8e248c8cb46ce36007f100338d4037e812723967 | 63093ec9824371812a80844fe6eedc45e8b89084 |
| stability-report.md | 12246 | 558c792288cf896f71cb864bdbede3ec03c7af22011d7e5deb74cc586049ac52 | 6cca71ee1a5c12d190227094187a1dbf6e02064c |
| coverage-report.md | 1291 | 9c1c40f10af61d3ee98a5c84fd3c93c9fa45cc39a76ed077505cc15a1ae0eebd | 832f42acfd97e27b6cd00f6d1914eb90a3861546 |
| quality-audit-report.md | 2065 | 871d0547f36d6a3e37685b39c582f066b7330a1e1eb76abc2f379b1a7931aa58 | 402d4d5755c7e97dcde005c29a71dcbc4978e125 |
| publish-guard-report.md | 1047 | 93709a3a8e17f828985b6bda00fcdb02f4140db0cfd89ef89fd3885c83f892a5 | c827be3bd11e1e4cb650d8c8d7b0f9f436681f8e |
| published-recheck-report.md | 26173 | 9bb3ab080255905690244cf0dc886fbb17a1a02cc0d05e78184ef2559421bd94 | 2a020947bbd5072fd6c2348f0660e39b1cf14c71 |
| source-report.md | 6536 | b5116e69a0b8fa79e6188b7f88b9bc1995edbcff5bd38bebd00c5132a38cd13d | c88c01fe4bd5160b86c56d6743e73a37b737eb93 |
| check-report.md | 6536 | b5116e69a0b8fa79e6188b7f88b9bc1995edbcff5bd38bebd00c5132a38cd13d | c88c01fe4bd5160b86c56d6743e73a37b737eb93 |
| curated-report.md | 3519 | ec42c8a90a513264682eaf8e872988ed85958e8a496bada766ad31f2cc0091f1 | fea48657cd9f686c757beacc40e966bd596161b9 |
| sources_status.csv | 3051 | e60d3bc5a196ded4d55141191383acb5eb26332e7ada6774608c401a3dcdb628 | d8e08977f5de019cf22c16732419ed330d01ce40 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
