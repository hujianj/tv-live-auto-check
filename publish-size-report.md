# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 298430
Unique payload blob bytes: 197026
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 70350

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23450 | 7fb23bc0d1e2194959de83e966a3762f81388b9c826832e21acfe421f8ac8e73 | 7650771f8d4d04195683afa2be899f22275adfb5 |
| live.txt | 23450 | 7fb23bc0d1e2194959de83e966a3762f81388b9c826832e21acfe421f8ac8e73 | 7650771f8d4d04195683afa2be899f22275adfb5 |
| live-verified.txt | 23450 | 7fb23bc0d1e2194959de83e966a3762f81388b9c826832e21acfe421f8ac8e73 | 7650771f8d4d04195683afa2be899f22275adfb5 |
| ku9-live.txt | 23450 | 7fb23bc0d1e2194959de83e966a3762f81388b9c826832e21acfe421f8ac8e73 | 7650771f8d4d04195683afa2be899f22275adfb5 |
| live.m3u | 44791 | 66db6c7c5d8d54bc0c0230f896e3e0f3210026c3bbfffc606ff40f51a170873f | d2e214eb28cc8aeee3bb2bb8cffc1a82942de0c0 |
| ku9-family.txt | 23028 | 4d77e941970a44e2d3fcbc09ca8cf9649518856667443056774d28502bf03101 | ddbb02df62a3d7dc44192cb2284e0e649b7ca7c3 |
| live-family.txt | 23028 | 4d77e941970a44e2d3fcbc09ca8cf9649518856667443056774d28502bf03101 | ddbb02df62a3d7dc44192cb2284e0e649b7ca7c3 |
| family.m3u | 43997 | 81019ba67a3dacbd41e8e2c7f665cb0959fbdab23b2a5a8f3efdb26605a875ce | 23fc2150975cf06f5ca47ee47728c3d45a82b555 |
| final-publish-report.md | 10774 | e26f3a44168c1bf9ff608a10ab15dc5052d97564a5df8dc6ef534ddff02d7472 | a1cee12448ad569125db9747452830e0096ab930 |
| coverage-report.md | 2245 | 6b566ffd5545487d536ab9382e2ce8ccfbd508621e4f69adbea58adc6c696cf5 | acbf79afe413710e1ba48e275623843cd801d826 |
| quality-audit-report.md | 4721 | 03e820597fca3c6df1ad3edba3f863a6ac7db9168650c0d90bfa693ed491c38a | e45d5aa159cc709a542621cdd5ffb7b1a4e937fb |
| publish-guard-report.md | 1583 | 4e241d3d91d5316f7744afdeea1f806c2369497eb380040f61de27dc1b7d8918 | dc14d5b2554aaefb9dca56ae52175a9ef7fb59a3 |
| published-recheck-report.md | 28520 | c6e33f075d3808ba2bd9bfb1948fa70b14b40ca70008a552e2ec62ca563e4e21 | 896a559e591289163bb6084fc442218e45150471 |
| source-report.md | 8026 | ed65d9e4277b9ae22e70a97f3a65619611120960776dee313df8b6d018bb58ab | a044eb899628feef4e2993b3e44ef5d97ea2533d |
| check-report.md | 8026 | ed65d9e4277b9ae22e70a97f3a65619611120960776dee313df8b6d018bb58ab | a044eb899628feef4e2993b3e44ef5d97ea2533d |
| curated-report.md | 1806 | d3ab5a934a59ae48a892bd8a320e568002e556c45c7dadc1d902d8e1d53c8052 | ce25d38490bca125fa5b56b6265ef3963e03939e |
| sources_status.csv | 4085 | 246a9e3b52d2a89a58e0b38e3515646901e856d1d071c7d4891e3bdf85b61df9 | a29c451a2b4335624c70ca74fdaa5666f1cc7ffd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
