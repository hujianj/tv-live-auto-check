# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 274199
Unique payload blob bytes: 182727
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 62847

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20949 | 847208f4fdc30eaa2d32f1d4d55e34da57d02127cb3a0f9332403805c0a63eda | ec12bc082029f4f714989ea0f12cd3b22a651b09 |
| live.txt | 20949 | 847208f4fdc30eaa2d32f1d4d55e34da57d02127cb3a0f9332403805c0a63eda | ec12bc082029f4f714989ea0f12cd3b22a651b09 |
| live-verified.txt | 20949 | 847208f4fdc30eaa2d32f1d4d55e34da57d02127cb3a0f9332403805c0a63eda | ec12bc082029f4f714989ea0f12cd3b22a651b09 |
| ku9-live.txt | 20949 | 847208f4fdc30eaa2d32f1d4d55e34da57d02127cb3a0f9332403805c0a63eda | ec12bc082029f4f714989ea0f12cd3b22a651b09 |
| live.m3u | 40504 | d539907f1a49b2b14b85dc8c05dcce52eda1b7c61965ef39bda4193009fadfad | 3b9ec69adebd0ff6c493a12847e8910d58b9ad6e |
| ku9-family.txt | 20671 | d071d37f2425a062ff6fd5f7a16b7b78e116e3a69382e58f3c62166b9aa7a41e | db37a233a7757cddde678e2c22beeadf7bc19481 |
| live-family.txt | 20671 | d071d37f2425a062ff6fd5f7a16b7b78e116e3a69382e58f3c62166b9aa7a41e | db37a233a7757cddde678e2c22beeadf7bc19481 |
| family.m3u | 39978 | 8bc7783b6a416d6b7ea10a38698b2281f67969eba3402de0aba30f93e995d120 | 324ce2a524d8fe57235f6921f19c32a8bad38522 |
| final-publish-report.md | 10658 | 12d47e78a8d32662bae2f9178e212f7a1d9b1319dd3b0b0d38e7eda10906d913 | 322949f2cf8ecc7cf8ae80639c2270ae96b18fee |
| coverage-report.md | 2240 | d215bbb5f4c2d42fd096212e9f812efe981f045792dae35d8a0d936c07040983 | 12cd0ba39289f3a61463245b701e027fa2733bb3 |
| quality-audit-report.md | 4727 | d3bf0d37dabeeff6ad24a43e9aca7d5fbf25bc371b1270229a4543b5fdfe0e57 | 7ead0706232e7074c5f095f64020c954a9075d39 |
| publish-guard-report.md | 1590 | 1cef010a60733e3f0dd4aae9bf3d7de48cdf05f9bd4e7c8101c985e1527dc904 | c1b476f6dd31519e58faa3254a76126b743d8572 |
| published-recheck-report.md | 27610 | 0a1d2d4adfca0beae8ade349eb5ac4c64b36289ee4db87167af189ecf89712bd | 897190d3af3481d717aa1c7e557ef04de16d97c8 |
| source-report.md | 7954 | d5cba719c435e7ea4029bf1eddbbaba6cea2bf2da3c3a8be7f43be192fb10f76 | 75cb8f6915b7ace94eac2e6b9bb901c9f183f8ef |
| check-report.md | 7954 | d5cba719c435e7ea4029bf1eddbbaba6cea2bf2da3c3a8be7f43be192fb10f76 | 75cb8f6915b7ace94eac2e6b9bb901c9f183f8ef |
| curated-report.md | 1804 | cbaf4e43509403ed6f95b4ec035aba3addb9c66f643e1a856289bff2065dc347 | e2f4ef3a230bdb5cbc098ce90f13b79069a58b09 |
| sources_status.csv | 4042 | 58e6c17aa4e402502d91cfa4b3412a5f2346ad31d6f92d1811abde1d550908d4 | 88a0d3f8d5107ed13961243c8944659266115610 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
