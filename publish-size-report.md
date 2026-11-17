# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 346462
Unique payload blob bytes: 280800
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38452

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19226 | 42de8bf8d0056b1d61c1a9a0b2b1d57ef22f68fdfda20b4ada5757adfc90e3c7 | ac6a788c1b8f24f7c1113afc480b6533127f4d26 |
| live.txt | 19226 | 42de8bf8d0056b1d61c1a9a0b2b1d57ef22f68fdfda20b4ada5757adfc90e3c7 | ac6a788c1b8f24f7c1113afc480b6533127f4d26 |
| live-verified.txt | 19226 | 42de8bf8d0056b1d61c1a9a0b2b1d57ef22f68fdfda20b4ada5757adfc90e3c7 | ac6a788c1b8f24f7c1113afc480b6533127f4d26 |
| ku9-live.txt | 23096 | b816f957f76bda2897ec98b699b4739ed53c60c9800c1eb8e07d0e65bebe906a | 533611a90a619b997c5f802615cadef42e4c6ee0 |
| live.m3u | 37041 | 1d1915aec9318f2b630d3dc70d27d0e72b583df0728cd76c3aca16540e41b225 | 9af74efd87bf815fc84c2d5126575bed6d35945c |
| ku9-family.txt | 18942 | ed8a5b00351a56706cf993ba4dcfe7c0388e6bbc9d1eb11daf64b2c36d673876 | 673c1e101bfe7f31ac8fc1d36db26a5f350056a6 |
| live-family.txt | 18942 | ed8a5b00351a56706cf993ba4dcfe7c0388e6bbc9d1eb11daf64b2c36d673876 | 673c1e101bfe7f31ac8fc1d36db26a5f350056a6 |
| family.m3u | 36509 | 0b490247b07f9b752bfc251c585c05658f1cec2261df462595c53ecb3ffaa2a5 | 064a9ceaadd0324161b1636f26f5819fb693ea24 |
| final-publish-report.md | 10912 | 670ad72049e54664e2cf7bf7ab08f2c236e489fb495b41532a5d3a806c7f2882 | 3e2080acc4ff37f39467ae129db1f144cb078b30 |
| coverage-report.md | 2200 | dbbf480fca32f51f90b57ebc4f57216962df37e470016b7b41d4b4f9faa5c8f9 | e88e39b51772f198ac552ee36a2f5d9e2ac40929 |
| quality-audit-report.md | 4683 | 187e41cc2329abfd57909ac22c9c1a10c9a53c604b77a079f9edb6a932523620 | 4f97eabbc4f8db5faf255c5a7ec1cbef531be7c2 |
| publish-guard-report.md | 1620 | 2712f2871f65809bb0eb29254b536bbed68dc8bb3b3c312b2ff88f890fc31efd | 3b42b9e32184e65035c2881987187a8fc3d811a8 |
| published-recheck-report.md | 29998 | f677d75d63e4c30104ba722d54ebcc36586def130245479b2e716ca61f64bc7b | ec1126f69f97f98d08e7338e8486edfde7cdcaaa |
| source-report.md | 8268 | 2f971d4dbb75abd769e8217e9524829a6c911e81b12d5ca7ea1ee4a15e810b61 | d099443b3678d6950d26ef892d0e4d2eccb27406 |
| check-report.md | 8268 | 2f971d4dbb75abd769e8217e9524829a6c911e81b12d5ca7ea1ee4a15e810b61 | d099443b3678d6950d26ef892d0e4d2eccb27406 |
| curated-report.md | 1833 | 07bc15c18007471bbf670a943a57c6507a04b68970ff780f59148b1ac6a82a71 | dbe1639d92a8aa3d2b624e12760b1c6846469be3 |
| sources_status.csv | 4339 | b204fd4096c6ae109d3d81a20eca4bf000877437ab62ce99fb4d955ca7d4e8e1 | 02d2f743da08f571e12f4b11e81886e1cf45fa05 |
| tv-coverage.m3u | 52367 | efae76ba55a625dfe4a4c845aaee866fa9d2106c4f4365cb1eebd96683c59125 | c947f087258c5eee9db7090a05f2c490324446c4 |
| tv-review-report.json | 18948 | 307689c8fc4c11957c9cdf21332c94b8b53fe6d7433141be571bc3fe006de096 | da59cf5a78b8f37f4acc46c65ba0b01f14d4893d |
| tv-review-report.md | 10818 | f35f0d72a48af911fcea760af31db1e0072f7c3e5425918d1ebbb29a050d8f3d | bd12c5715db65e23ca6e2d1deb27b1da318a93ed |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
