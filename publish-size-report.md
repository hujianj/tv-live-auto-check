# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 283205
Unique payload blob bytes: 187703
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65802

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21934 | a66a2f6026337a843fd12e8f5d197226d7007ac2fe0c87bb37360e27f840d076 | e7f4665ad49c0bf66647bfc6ddde4743305bd0f2 |
| live.txt | 21934 | a66a2f6026337a843fd12e8f5d197226d7007ac2fe0c87bb37360e27f840d076 | e7f4665ad49c0bf66647bfc6ddde4743305bd0f2 |
| live-verified.txt | 21934 | a66a2f6026337a843fd12e8f5d197226d7007ac2fe0c87bb37360e27f840d076 | e7f4665ad49c0bf66647bfc6ddde4743305bd0f2 |
| ku9-live.txt | 21934 | a66a2f6026337a843fd12e8f5d197226d7007ac2fe0c87bb37360e27f840d076 | e7f4665ad49c0bf66647bfc6ddde4743305bd0f2 |
| live.m3u | 42099 | e3a75f16e43bf6f3ba0cf283bed812cb4a737f4f028bf987f33d167c8e453e1f | b4b7b43c43171ac27f4687d355905b306f3f00e7 |
| ku9-family.txt | 21662 | 2edbb6a1c53380afcd4e50ca47a876e350d71475d21b3b9ff18ceda3c6bff86d | 9ebc2a60b601baa05ae31bd68b09bd946eaf0582 |
| live-family.txt | 21662 | 2edbb6a1c53380afcd4e50ca47a876e350d71475d21b3b9ff18ceda3c6bff86d | 9ebc2a60b601baa05ae31bd68b09bd946eaf0582 |
| family.m3u | 41579 | 412401e5476fc0bb2988b7ff462f13ce7c01ae6d4305c5d8bfc5440768c3a6a1 | 88da96ae815f034e95ec279cb17ddb34224fa157 |
| final-publish-report.md | 10649 | 25c89d226c7fbd5059448702858e1615d307a3b94b530d8b0c9f5f58bdd6398e | 025138b4d99d2ea65ae1b82b37cb344b0635537a |
| coverage-report.md | 2230 | e4ba9f7c20c07fbbdcc767d3672c62c3fb173d64ee92d9ce01d82f5babe4a2e1 | c13ce745c01dc2483ecee73bc053965a2ac677d7 |
| quality-audit-report.md | 4719 | b43f28fc0a12bc445f7554cb0da49b6096444130bb74397ec614ecc54c19d11e | 24ebbb6185bc0d3cb479aedc38b186328f7d899d |
| publish-guard-report.md | 1523 | eb17981b0d2e66d3892002eec9b62a1898cb6a503da2755316effa0464238678 | 509429caf19f80ee886cacdaa2f4cef7e602b5c5 |
| published-recheck-report.md | 27388 | c2ec25cc1b8d23d6ba3defb8643c5a3e7bc2fe35cca58d32f202df912a6ebef5 | 9aa9a531490bb81e7cbdc029dc81110c03cc501f |
| source-report.md | 8038 | 06779a760a199a6d0a7b284bb8061096cb0cb011318a2dec5a54e4a3c1d8a5ec | 89205d24cf25768289f88f3d1f7851e675dcf582 |
| check-report.md | 8038 | 06779a760a199a6d0a7b284bb8061096cb0cb011318a2dec5a54e4a3c1d8a5ec | 89205d24cf25768289f88f3d1f7851e675dcf582 |
| curated-report.md | 1804 | 5cb0a2d7bf85ad0ba3531cc748dbad8bd3cf3d29d5f8184dfe60dfa131d5ff44 | 9650f828ac7e805ccec93dfbe75825c5cc22841e |
| sources_status.csv | 4078 | 079d22507201ccb2eac60b75fd68f03cb9d1d1d47a6fc944395b45e88e8e763a | bd751b912536440cadef063c6c3464bc71377c64 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
