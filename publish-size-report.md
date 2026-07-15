# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1819074
Unique public blob bytes: 1200271
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 613122

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 204374 | d63796308adad812601d95b13b2ed62783700f874eefb87d712ea98cc5cd4950 | 5e498f144b75ea7d8bc9d3ae8af44430e6b12463 |
| live.txt | 204374 | d63796308adad812601d95b13b2ed62783700f874eefb87d712ea98cc5cd4950 | 5e498f144b75ea7d8bc9d3ae8af44430e6b12463 |
| live-verified.txt | 204374 | d63796308adad812601d95b13b2ed62783700f874eefb87d712ea98cc5cd4950 | 5e498f144b75ea7d8bc9d3ae8af44430e6b12463 |
| ku9-live.txt | 204374 | d63796308adad812601d95b13b2ed62783700f874eefb87d712ea98cc5cd4950 | 5e498f144b75ea7d8bc9d3ae8af44430e6b12463 |
| live.m3u | 362814 | 9d983658581a41b011be53bef75063a620385dfbf416ce547535d2102d887982 | 0340791570f1167ddce613618b6f1722dcf20a20 |
| stability-history.tsv | 569330 | 3bc2fe3e536eded3bcc2c58e7113ee3a28493bc3dc7407b651fae4262c74a09b | 8f38617aac85bd03ef39288e218826e0124b8125 |
| full-check-summary.json | 17414 | 6146b4cea2978e7ea23147ca4a76f7608cdffe1304b81ad58038fa6cff923f84 | 7ffeac6b6e1f340d5b4340faf154530c68023180 |
| final-publish-report.md | 11598 | 4b2585481217cb577e40fb5ade56b610df45d12f56bfe3bc0912df39bb3c22a3 | 1b8b12f2a665e711253b9b592a031f0c1602cdda |
| stability-report.md | 7749 | b9bde9d341cf3bb8fc9a4bfc3461d54b60a20c008c144132ca7f5a5932724527 | 055313c31e03ef9fff641a2fe386b3c5f741d292 |
| coverage-report.md | 1139 | f7dd484d3615408c9bc3f236a511ce0898e90a9b8214d1f7d40c7f21b300739c | 346edc8d27a18e0d050100fac9b16b2c9c5a3117 |
| quality-audit-report.md | 1057 | 0c8352a01d545c2d6b59931e52d27959b3fdafef576f25c1aaa497268b426fb9 | ca8029e320c8661b47f4e4b6ec27375235cd8845 |
| publish-guard-report.md | 793 | 1f9fe83ae3e4cb9a899690530774bec85c46955d82e4f3e41524d839503a7526 | 466cbca7172c97919b20b92f526ac5e6931c5bc8 |
| published-recheck-report.md | 12175 | 7718f991c7762c7fbdb654a8b964dbcd2e587b9c8ac5839181e0cbaf93771e92 | f37ad97d8e3fd82be6cc20a0fd32c8bd035a6046 |
| source-report.md | 5681 | ffcd157b53d9bedf8692fd8b0d18c3593208c05127fc886a0e102582a645528d | c7be1fac64e63bcb229db3eed367c28fc86f6069 |
| check-report.md | 5681 | ffcd157b53d9bedf8692fd8b0d18c3593208c05127fc886a0e102582a645528d | c7be1fac64e63bcb229db3eed367c28fc86f6069 |
| curated-report.md | 3698 | 4fa8e55505385b916af5e9e9fd0e7b80e95a4cbc292144a7069f84850a1ce8c2 | 2feba46dd71b4ad8f442a1026a4859f2c1b8e158 |
| sources_status.csv | 2449 | 02ad8c430dd503a0cd4551eb1ef6eaa121133f24c8241d7f8a2fa6a349e7a5d7 | a39573558d2c04f5a042ca1b881edea2338923be |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
