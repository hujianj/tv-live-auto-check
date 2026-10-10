# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 278118
Unique payload blob bytes: 183319
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65214

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21738 | 2e6d338459cf31ff2e118b93511318a4c72f4f47add44785a7c8b5c549ec3723 | 66ae8945cac6a88c48b644354d3bf2b62e05312c |
| live.txt | 21738 | 2e6d338459cf31ff2e118b93511318a4c72f4f47add44785a7c8b5c549ec3723 | 66ae8945cac6a88c48b644354d3bf2b62e05312c |
| live-verified.txt | 21738 | 2e6d338459cf31ff2e118b93511318a4c72f4f47add44785a7c8b5c549ec3723 | 66ae8945cac6a88c48b644354d3bf2b62e05312c |
| ku9-live.txt | 21738 | 2e6d338459cf31ff2e118b93511318a4c72f4f47add44785a7c8b5c549ec3723 | 66ae8945cac6a88c48b644354d3bf2b62e05312c |
| live.m3u | 41657 | e37a7f45717cddba543444d0eca2d0aa2d0f5ffdebaa228a09065162442eeaad | c146b1ea05c1ade116a9e8b8109ead3d286fef41 |
| ku9-family.txt | 21473 | fd2d23402f272fd0295460618cf2884737e1dd83f9af091047785fd6df3ec20d | 022e5e547f0d991fe2a57ed6f4f3c169b0697ba9 |
| live-family.txt | 21473 | fd2d23402f272fd0295460618cf2884737e1dd83f9af091047785fd6df3ec20d | 022e5e547f0d991fe2a57ed6f4f3c169b0697ba9 |
| family.m3u | 41144 | 1fffe4c7ba09ac1260acd309d49d337538432616289f7d3983bb7ebe5160f155 | 09e8e9e428396afd59d61a4af7228a225058d4d4 |
| final-publish-report.md | 10698 | 989361adaf3a58f77a2375d88449a7b3167f6cc81517620da8aaedea75ad195e | df20d22d3cde0aeb6a5e0035d3da6c73e70a83cb |
| coverage-report.md | 2230 | 6711913cae9052adc88121e3dda536d976bdb20631169f3270baa631ca6b1f91 | 4d9a9a8a45d363cacbe6e3a98ed690daa6155b9e |
| quality-audit-report.md | 4725 | 93c293536ea37e1a4cf5794a0427f7a207984f1e1c9bfe47c284bbbb6d9b86d0 | 1a360a6439a9757246ca1e694db129f31e1ee2d9 |
| publish-guard-report.md | 1609 | e581fa3448c9f57a7dd31712b4dd5d2ff0f4d73b15655761f9590c2a3958470c | 8c943eb6d5b940a3347b931ee69f959f84f3a9f9 |
| published-recheck-report.md | 23991 | e8d286032f4ec2f172ebba8891c3a3be03102d82de5ab9675310b201b32b6a70 | daf2411cca26b3facf3f6f4a4d8ce98b3d8da81d |
| source-report.md | 8112 | b321b7e06c0a340b993d6e2aca1eedbce3ac63bd9b4808a02adeb4a8b033953a | d2b5f927614510d2089ebcf3cb833e11b8ae18fa |
| check-report.md | 8112 | b321b7e06c0a340b993d6e2aca1eedbce3ac63bd9b4808a02adeb4a8b033953a | d2b5f927614510d2089ebcf3cb833e11b8ae18fa |
| curated-report.md | 1804 | 1d022ecdb6b6cc268530d27ae3280b957e1091f8bd82774323d9febcb34c0ac9 | ae7b344826bb3bd3ac0fad6c48196eb1e31dbda6 |
| sources_status.csv | 4138 | 1ab6c0ff745177eefb0c36601128da30f543e9d311046bc3eca2d75aedfbacfc | 9e1f623fa594f954efcb52281e885cf2f86a408e |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
