# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 290480
Unique payload blob bytes: 192635
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67623

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22541 | 8247045614fae3e1799588d393d97e32451d0ad5b32e2f61713ba61f2b4ec5d6 | 5965932e43151d6deedbd89ab232de937410aebc |
| live.txt | 22541 | 8247045614fae3e1799588d393d97e32451d0ad5b32e2f61713ba61f2b4ec5d6 | 5965932e43151d6deedbd89ab232de937410aebc |
| live-verified.txt | 22541 | 8247045614fae3e1799588d393d97e32451d0ad5b32e2f61713ba61f2b4ec5d6 | 5965932e43151d6deedbd89ab232de937410aebc |
| ku9-live.txt | 22541 | 8247045614fae3e1799588d393d97e32451d0ad5b32e2f61713ba61f2b4ec5d6 | 5965932e43151d6deedbd89ab232de937410aebc |
| live.m3u | 43209 | f804a351845969ad419ed67dfa4799b6793a56980250507a71db173ac6c0a1b4 | 2c11aae249201af71a5bd08667709ef844eb94ad |
| ku9-family.txt | 22125 | 34eedaadd1a0d32446baae5c86164ff3da75b2e4ff539ca77655064879416d93 | b33b99ae428a9cb3aa7945e68e4cc5203d2b615f |
| live-family.txt | 22125 | 34eedaadd1a0d32446baae5c86164ff3da75b2e4ff539ca77655064879416d93 | b33b99ae428a9cb3aa7945e68e4cc5203d2b615f |
| family.m3u | 42421 | 15b52b08dedae448b3d9616b51fab4d7511041c4d8a89eca16e442d6bb4985dc | 1e1cb4e669276c89d9a1680676def778d0f20215 |
| final-publish-report.md | 10961 | 64851e8fd8ebc63dfe803c98c59f0035784ffdccc6c6373d0724279737c611fa | f0cbac0c71122185c5a35fcc15ef6e3291bb752a |
| coverage-report.md | 2280 | aa2f7587b74eb9311243ee3668dc1c55edc7d6a014dec01c2f0800c2cb446339 | 328d0169ae4397ff00e107bb5e98b699224aa160 |
| quality-audit-report.md | 4746 | 158b9931e217aceda27fc7b68f9762cf8c61e4c89a280d7e00d50ae50ab9d358 | a9bfe0bf7d0162e19a37fb3eaab9b0dd23166ec1 |
| publish-guard-report.md | 1679 | 334ec1e8eff0ac4a924f905c427bd276509196d7962544d644d07c8ca4ab9ee9 | 77946842c893242f84c187d9421ad07589061371 |
| published-recheck-report.md | 28632 | 251ce19aacc7d7abb366ceb01159c1a0535a2b4f0a20d7cff181b2b4407de263 | 676c5ca5bed307e07b76fe0cdbdc73122e0e37fd |
| source-report.md | 8097 | 2ab6ca85343cfc1565239578f20df66d573ef3ae8c8888d366e4462ebe90aa99 | 5c413f2265ef1337b4a06bc6ee3226b873c5ddb3 |
| check-report.md | 8097 | 2ab6ca85343cfc1565239578f20df66d573ef3ae8c8888d366e4462ebe90aa99 | 5c413f2265ef1337b4a06bc6ee3226b873c5ddb3 |
| curated-report.md | 1806 | f2183fc89425404de9cce9ab722b2de5a1ee412323ec95eb9913cd1991f8c653 | 46b733eb6e3f3f4e576c3e9139e2585179ae48b1 |
| sources_status.csv | 4138 | 3e018ad318cfc35495efa0b50b8871809ae3de0ef4870be0a788815ba18234f7 | 5a56a7b6eb420204755f35e1aa4ae9ae58ae4fe6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
