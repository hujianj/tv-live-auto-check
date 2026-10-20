# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 274448
Unique payload blob bytes: 182296
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63267

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21089 | 497c1c44d5517d33a563034e211404bda45a32cadd8407c42525b2ba4f833db8 | 0fab9c51bf1a48cda033a013ec8357a72b98c2ac |
| live.txt | 21089 | 497c1c44d5517d33a563034e211404bda45a32cadd8407c42525b2ba4f833db8 | 0fab9c51bf1a48cda033a013ec8357a72b98c2ac |
| live-verified.txt | 21089 | 497c1c44d5517d33a563034e211404bda45a32cadd8407c42525b2ba4f833db8 | 0fab9c51bf1a48cda033a013ec8357a72b98c2ac |
| ku9-live.txt | 21089 | 497c1c44d5517d33a563034e211404bda45a32cadd8407c42525b2ba4f833db8 | 0fab9c51bf1a48cda033a013ec8357a72b98c2ac |
| live.m3u | 40601 | 3774f7a52f3cb526557996f35334059d8a9ddbf8c20d5a991eae3300aaf36a96 | 4403f5fce7a856f5b873aef7402ccfc9921fdaf5 |
| ku9-family.txt | 20811 | ff0d76e65c0598820d915613e499eb8489da7a358cc0e3b4da59f823a12c67aa | 74431a6f8ceda6c35e9c81c92480617ace62affa |
| live-family.txt | 20811 | ff0d76e65c0598820d915613e499eb8489da7a358cc0e3b4da59f823a12c67aa | 74431a6f8ceda6c35e9c81c92480617ace62affa |
| family.m3u | 40075 | faf52fb8f492bb13b0d948f1a74eea9f51b606b0fa781dce2521fabdd1580f24 | 6a566460ca7fb24ec4e828ab008fad216e276fc2 |
| final-publish-report.md | 10744 | 4addbb5b07b31b68f0e7096d5f998715838a12c7c10333d070e379693d5aef5a | 663d075039aba416c1e3966fc7cab49061b3f568 |
| coverage-report.md | 2235 | cc6b8628c76d57aeb6d7a0b14254efeecb1132b2a8878fa67e755d2d6a79ff7f | bcbe9cbe385411a577676eebc26ea5f2250e8bfb |
| quality-audit-report.md | 4728 | d6c15a1b7959651edf36f7875975a4bdce775dc51c61830ed5e71871beb07336 | ca6b30ca1d594a74e6e89eabf1dc50c2af37d620 |
| publish-guard-report.md | 1611 | 52998f246eb14f941bbc86c5a5a7ea6e5f425139d067e86a90147f9b7b41cfe6 | df37855ed00d413f7bea07281e0776f69caf1eb4 |
| published-recheck-report.md | 26415 | be3156a30be7c339b4405360e101795a16ab046f311f4194520aa83ae30b9fd2 | eb1254ca569b208a4a440df43179022ed49a6c42 |
| source-report.md | 8074 | 69c879d883ad68f256dc554901331a99ae6396d5a6800455a0b4a273983a6dea | 7fe2e661a28c949e6e4b9b85f9be1000097c0879 |
| check-report.md | 8074 | 69c879d883ad68f256dc554901331a99ae6396d5a6800455a0b4a273983a6dea | 7fe2e661a28c949e6e4b9b85f9be1000097c0879 |
| curated-report.md | 1806 | 1e5681b6de9669eb929a8a1d18f584bce4ae70ef5dea6716270c0fb51199af8e | cb03297dcf8104cca5be1f26cf1e8bcc5856e486 |
| sources_status.csv | 4107 | 752c7f6133cd6c5abd7d08e92b6f7e35d6c9fb5e5f71430c532b8589782970a2 | 521b345e855f704acc1acb833a7afeb76adc3bdb |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
