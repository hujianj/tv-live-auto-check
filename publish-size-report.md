# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 183984
Unique payload blob bytes: 128055
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36426

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 12142 | b1630a161dc2d3c4864d89838761064854bb77f8c73d97ec52f589802be90c62 | 7e6147a6a79f63c8d261f6855fe3e2fbe679de79 |
| live.txt | 12142 | b1630a161dc2d3c4864d89838761064854bb77f8c73d97ec52f589802be90c62 | 7e6147a6a79f63c8d261f6855fe3e2fbe679de79 |
| live-verified.txt | 12142 | b1630a161dc2d3c4864d89838761064854bb77f8c73d97ec52f589802be90c62 | 7e6147a6a79f63c8d261f6855fe3e2fbe679de79 |
| ku9-live.txt | 12142 | b1630a161dc2d3c4864d89838761064854bb77f8c73d97ec52f589802be90c62 | 7e6147a6a79f63c8d261f6855fe3e2fbe679de79 |
| live.m3u | 22671 | 43a599f846662360ae84fa07ab8a41c67d0390fdc0ce629e220ac31e940c2284 | bad9bba93052400cabf83b049dc89194490d5c29 |
| ku9-family.txt | 11719 | 921e3d2bcb519aa2911ed935e3c7667c4ec5d80702d51af3f60a8f9737b197da | 5f03bebaa13a5bbc167bb880568964a3cf8dbadb |
| live-family.txt | 11719 | 921e3d2bcb519aa2911ed935e3c7667c4ec5d80702d51af3f60a8f9737b197da | 5f03bebaa13a5bbc167bb880568964a3cf8dbadb |
| family.m3u | 21876 | a9f8abc12ccb2f606fb4ab56138ef7f8253e1766d69628d87ed9c173c1c26b06 | 047b632d531620cb399e655223162c4ca7cf1e4a |
| final-publish-report.md | 10538 | e64f1fe44b8dc4a77092cc4f2c157c1f418d3e461e4b70553f1af7764fd417ac | 24629b98b66a82db36374d2333fb55ec41cd55c5 |
| coverage-report.md | 2230 | 17dbd74aa84d9e1df48385899dc93c9e0b7c861b8073da34ed54c8a36177b375 | 493783a30b82b4966a7270beebedae57089ecc8b |
| quality-audit-report.md | 4719 | b85b126e2be306b4d33acc8fcc83fd82c626bc692b9648c5a872b11433912381 | 0a3624c63e972ef5b6ed57fac4a24026927cfaab |
| publish-guard-report.md | 1672 | 283bce919fc05f157a4fb8d875f9059b05bfe1a9f5c93f9c34126c8b3d0012ec | a51692477c6f99edc6bae88323b41e0acaebd56c |
| published-recheck-report.md | 26729 | 84b060c78c1988051d1145d554ae0629327e732835878ffe32eedb13fc68f2f7 | f199b889e59760a93d172f36007855278bf7281b |
| source-report.md | 7784 | 5caa0da06c8353a11cda40dcaba294862feb1e102f95befe873d79f039440857 | aa1e5cf8f3f82d2bae65857cc6bc61b5b71d0ff6 |
| check-report.md | 7784 | 5caa0da06c8353a11cda40dcaba294862feb1e102f95befe873d79f039440857 | aa1e5cf8f3f82d2bae65857cc6bc61b5b71d0ff6 |
| curated-report.md | 1837 | d6ddf1107785a5a60f69df0bb1fa4974a7fa5f7f49234542cb18f147b675d0e5 | 856876293e3c826a7fc0bb7fc3733c9f7d893ca7 |
| sources_status.csv | 4138 | 07b913803ab163918e2c7cd33579bf42bab867e3d80371fe6f5ad55c4273135c | 788570f396e7bffabd2c52bb2ca88a006d283d02 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
