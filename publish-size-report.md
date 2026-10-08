# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 295180
Unique payload blob bytes: 195531
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 69015

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23005 | 0252e25ad787579770c5c146ec26ab87726ed62f29c6ff3e83e567e5c94f99ea | ff38ed61aef58300f40bc332778527ef203a1247 |
| live.txt | 23005 | 0252e25ad787579770c5c146ec26ab87726ed62f29c6ff3e83e567e5c94f99ea | ff38ed61aef58300f40bc332778527ef203a1247 |
| live-verified.txt | 23005 | 0252e25ad787579770c5c146ec26ab87726ed62f29c6ff3e83e567e5c94f99ea | ff38ed61aef58300f40bc332778527ef203a1247 |
| ku9-live.txt | 23005 | 0252e25ad787579770c5c146ec26ab87726ed62f29c6ff3e83e567e5c94f99ea | ff38ed61aef58300f40bc332778527ef203a1247 |
| live.m3u | 44124 | 1ee7101ff36ca1f1d145cfe42247cd02e74ab84980350f1ebc6177b8998ccfd0 | 6869dfcbe61f63cce25daed6c6c6d537b29b4e4e |
| ku9-family.txt | 22569 | 0590ce74c8b757b8742b506a0d882711b6bb68224bdfac570f0de2a0063a2796 | ab1494085e4c5a468acc4506b63a9328deb49246 |
| live-family.txt | 22569 | 0590ce74c8b757b8742b506a0d882711b6bb68224bdfac570f0de2a0063a2796 | ab1494085e4c5a468acc4506b63a9328deb49246 |
| family.m3u | 43316 | 9a0d230862a1b66f7c70dfa96e118b4386e167b132e4f4a9de5cb0bc6bb93219 | b760e1cd752be22c1cfc8bb2e29001f4ec0bcd0b |
| final-publish-report.md | 10726 | ac56d08ee454e3047ab08d09af637c3e2650e4f85dcbd9575ebb33fd739a2a23 | 26ed66a485792d5907451302d54c4c067e7bcd40 |
| coverage-report.md | 2235 | 0ffa5e713b9a342a015ec4c6daf46aed5b15a200857fddeddbb516fbed105326 | 9aca8c4854c4c4a947591d567ca0c1562f8656c6 |
| quality-audit-report.md | 4721 | 1f654d1ff6892b8bd37d1edbc859ff927a0c82de9c11932e8ce3f5e1624b0267 | aacb73dcf809c1de9d854fe4d9f7b9fe75fad5ea |
| publish-guard-report.md | 1581 | 80282f856abba189ae9bb7161ad0c3681382172879488a4ce4dca0327ac72b59 | 0e8cbccdbc2e82f19d9a085fce5891b5e5dd8e2e |
| published-recheck-report.md | 29307 | fefb08dfed0ef6ed1d38b919b11f27bc0d329da66f0f57574e250e979481bbd1 | eec10cf1a6ba14a757df19c31b7011552b6ce840 |
| source-report.md | 8065 | 3a824fd925a9c0ef8e8891d57aaaadb5e06c7ac53c895c29da8286f8eafe844f | 17dca0a2921dc18c65ba31a435f754e17f635f3d |
| check-report.md | 8065 | 3a824fd925a9c0ef8e8891d57aaaadb5e06c7ac53c895c29da8286f8eafe844f | 17dca0a2921dc18c65ba31a435f754e17f635f3d |
| curated-report.md | 1804 | aecedf8e28522220b8801789aec89216ef4ca3a1ae4badf429747327dba6c4f8 | 48dbf93fba0311307cc73bb18fd536e7a0bed4a5 |
| sources_status.csv | 4078 | c201c5d664f7fcee8b6ecaae744887388706ee9adc7b8da9c9c25f560c16dbd3 | 626913bb064ab41ad55a44c931bbf878962472bf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
