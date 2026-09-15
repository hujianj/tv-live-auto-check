# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 288462
Unique payload blob bytes: 190423
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67704

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22568 | 345116b29ae064129de0704b866a24b471b6f3f7bf69dbea5f3aa3a4f9920261 | e06c8f0334f4a7ea8828086d525adad932dd47ea |
| live.txt | 22568 | 345116b29ae064129de0704b866a24b471b6f3f7bf69dbea5f3aa3a4f9920261 | e06c8f0334f4a7ea8828086d525adad932dd47ea |
| live-verified.txt | 22568 | 345116b29ae064129de0704b866a24b471b6f3f7bf69dbea5f3aa3a4f9920261 | e06c8f0334f4a7ea8828086d525adad932dd47ea |
| ku9-live.txt | 22568 | 345116b29ae064129de0704b866a24b471b6f3f7bf69dbea5f3aa3a4f9920261 | e06c8f0334f4a7ea8828086d525adad932dd47ea |
| live.m3u | 42967 | 5625a83b28441e28f96b71fa13d46ff7a12e65a64491cb1ab09921d133c31e26 | d7479f54c60dfd46e53233fff53e71b0b4d69db2 |
| ku9-family.txt | 22209 | 665059abe95d9dd6b51f51a0ce078967a0cb9f855c3914dd34dfcd675f74dde3 | ca8d5918996dcaca440ef0e5988b2030aea9d04e |
| live-family.txt | 22209 | 665059abe95d9dd6b51f51a0ce078967a0cb9f855c3914dd34dfcd675f74dde3 | ca8d5918996dcaca440ef0e5988b2030aea9d04e |
| family.m3u | 42298 | e00833081d300bbe265ab31a99ba888fbfaf03062112122e85333b12f14c4fe4 | fa861c0849e245b7e5ef79307879522dfcefec7f |
| final-publish-report.md | 10862 | 914206ea0b18f2776b864ba294d6fc7b3341ad89fd2d5402558ed6eb8274b7cb | b9a0b3512108e9985e1c0ee7b602a850c031d703 |
| coverage-report.md | 2225 | d856bab8070537d5e50c15a9dc0ea99d4d9dee5bddab41586a6a7d9f0b82113d | 33b161109d3346a0a7524c3ebb7a5527552a7918 |
| quality-audit-report.md | 4732 | c61581289136a5b7448c1961935506577588bb5b283415b997e72eadf7ef7453 | 0e87f1039af9baa5663b39053f9d6f1dbeb24720 |
| publish-guard-report.md | 1563 | 2ee390b2851eb29055247adca1e5218d70adf9f98c3a7dcfec3467e9630fa8d6 | 1ea2ab7f841162814f461b5afd013ad7ebc666e8 |
| published-recheck-report.md | 26874 | 14043fe8dc14dfc6979987773d54d0ad68e375ce3783f3d6bdab5d3acb5318d5 | 573621fbc1c3a8897676f5233c205e4a246f4466 |
| source-report.md | 8126 | 4d795f0917e9468a99867ad0ac63cc861525e0d40c3201d54a861bf91a7c2a8d | 2885c08e7499e8959d710c342b20208f8ae72415 |
| check-report.md | 8126 | 4d795f0917e9468a99867ad0ac63cc861525e0d40c3201d54a861bf91a7c2a8d | 2885c08e7499e8959d710c342b20208f8ae72415 |
| curated-report.md | 1860 | 0b66aee2225c897842f2bfb2153d441af62198e2eb335c9ada83490bec39d026 | 1629fbd92ed1a6df048691af155ee0137b314a56 |
| sources_status.csv | 4139 | 77e0f749b8ccf2439e309aca43d683665610cb7244181c6710d8c9bc2c05e9e1 | dd5fa83d21dcfb06b23ce37e4b66b95c650d2404 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
