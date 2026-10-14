# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 302576
Unique payload blob bytes: 199480
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 71607

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23869 | cb2ba6533ca37795d1c5843c0b20e7468726cfb9f1bcd1a1eb479a38ccde0a3d | 2cd13dd9aeb35bb55d0aa4d1b283216fc6d7aea3 |
| live.txt | 23869 | cb2ba6533ca37795d1c5843c0b20e7468726cfb9f1bcd1a1eb479a38ccde0a3d | 2cd13dd9aeb35bb55d0aa4d1b283216fc6d7aea3 |
| live-verified.txt | 23869 | cb2ba6533ca37795d1c5843c0b20e7468726cfb9f1bcd1a1eb479a38ccde0a3d | 2cd13dd9aeb35bb55d0aa4d1b283216fc6d7aea3 |
| ku9-live.txt | 23869 | cb2ba6533ca37795d1c5843c0b20e7468726cfb9f1bcd1a1eb479a38ccde0a3d | 2cd13dd9aeb35bb55d0aa4d1b283216fc6d7aea3 |
| live.m3u | 45555 | 43a920f8f7f66912b708268eae507bb9e5a993a4070192599a7dd327272e6542 | fe62c1aa4a9afe7bbc4145fb8b90cee46dfe04f2 |
| ku9-family.txt | 23453 | 613b6d39b4ad4c43aac83d00874b94cf5c8250e1a3a92721b01d289800d010ac | 31a82c8f65d83bb3610990b541dd2761413316bf |
| live-family.txt | 23453 | 613b6d39b4ad4c43aac83d00874b94cf5c8250e1a3a92721b01d289800d010ac | 31a82c8f65d83bb3610990b541dd2761413316bf |
| family.m3u | 44767 | 45ec3b9a8d9b0c61d1842be4bdd0c3da983d9b81d3fdb462034d0aa370c1eeb3 | d6301c091c68038925c38165c20f3520de427416 |
| final-publish-report.md | 10808 | fa33ad37f30ae0894cbdbe276fa96642889a252bcb5f71881988e0d13466e2ab | 785cf64318abac064114384482d355a1687350cb |
| coverage-report.md | 2210 | 63c7f8941ee229cbae3400033b602607ab680bc717010d89d989ac2d90b6ae5f | 7093519392b76c838c90caf919736483e8554d25 |
| quality-audit-report.md | 4716 | b8201f17fab3632ffde8475153100a365a74f638405b5821e00d501ec0eecf51 | bea8b7269b16fbf438311391a30dd8d565b708ae |
| publish-guard-report.md | 1577 | cf06db6af279e9d2137fa7ac1f0830760ae369b22109798724a4546d1da2a672 | bbb7fb5f1aa53a4cc3a8e83acf4c5fdcd7f3dfa3 |
| published-recheck-report.md | 28607 | 8969e2f729d6221ec76b4d8c4d164b047442543284c17500c92cb3ea457599fa | 3d291506292f5cdc790612e952f9d0529ab59bfe |
| source-report.md | 8036 | 5b1e2fd9622db5872a82c556cbc602e72c46bf1b9028c43ef9185ad719d97cd6 | bc26bd0f62cbc218669b3d0083974fd7fd874e3a |
| check-report.md | 8036 | 5b1e2fd9622db5872a82c556cbc602e72c46bf1b9028c43ef9185ad719d97cd6 | bc26bd0f62cbc218669b3d0083974fd7fd874e3a |
| curated-report.md | 1804 | a4bcdf1da2a3059b6ef46dfcda0efdd692d0eb6d3ecd0872548ac239122ffa8c | 80f0f5f569254b366a4f1921da108834602ab33f |
| sources_status.csv | 4078 | 6415f1e0b5d5304fa48d3fcb739e96db228453ff329b5bdd74b26d68dfd84118 | 7f30a85944a177769cba7befe2eecf0935f1bc99 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
