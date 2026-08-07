# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2447410
Unique payload blob bytes: 1703316
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 639870

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 213290 | 140837d49ab0d327ee4b413c22418eb33d4341577b5bdbfb5dcf696d4215e596 | 9bf0b4bd21825a7d21df5f69bd1eedf984d67e7f |
| live.txt | 213290 | 140837d49ab0d327ee4b413c22418eb33d4341577b5bdbfb5dcf696d4215e596 | 9bf0b4bd21825a7d21df5f69bd1eedf984d67e7f |
| live-verified.txt | 213290 | 140837d49ab0d327ee4b413c22418eb33d4341577b5bdbfb5dcf696d4215e596 | 9bf0b4bd21825a7d21df5f69bd1eedf984d67e7f |
| ku9-live.txt | 213290 | 140837d49ab0d327ee4b413c22418eb33d4341577b5bdbfb5dcf696d4215e596 | 9bf0b4bd21825a7d21df5f69bd1eedf984d67e7f |
| live.m3u | 383080 | 486778cbc280ed6c7b6bd76ed9cf1dab95e8cb577faa729c6d1682ca7b028977 | 41d3d6357a32e451b96934d897993916b24f9078 |
| ku9-family.txt | 98399 | 3944ea883134f5715a6c0b6e4357bde7ee66a551d69e8fa27856632d1e67a007 | 1c7c584a72fc5d2fc956f2e8374a02bc24f64c90 |
| live-family.txt | 98399 | 3944ea883134f5715a6c0b6e4357bde7ee66a551d69e8fa27856632d1e67a007 | 1c7c584a72fc5d2fc956f2e8374a02bc24f64c90 |
| family.m3u | 177807 | 59899294ee59f5000ad938be908bac6ebe7fb88047bd9230c8de6fa4ad74e8db | f98e5b1a1ed8701687378c73bfdd863a0fdcbcdf |
| stability-history.tsv | 762421 | 6c3393fd2e1789f5ccd992e7685cd2f4249496f2f330744b6740d85dafb2ab21 | 312bd30200dc1d6d0207c521090ca8100442898b |
| final-publish-report.md | 11746 | fcafb294b061a61e1686b315c8355deea2dce6ef4033b96eda5e387d8f89da3a | ae813fe6359ce70118a9a0fe6363aaa355e01d34 |
| stability-report.md | 11550 | 7a66c5a529987f93ffbd762ade4de3c486bfcaee69c80d4920c4587f93648468 | ace1e8b3302c1dcd5885780fd61800188c2b74c2 |
| coverage-report.md | 1350 | 389350e52fd493277571b076868464cea61be6f7bde1c99f8e32b9719877249c | aba07af4963e806bfe8468b3e4d89f007ee08b40 |
| quality-audit-report.md | 1435 | 901c7a03a15e4dcc38762e150b5d525d7516a31cce507cbf63cfbf736b6fd126 | 5707a9f7e89d1266fabdffcce761618f01616355 |
| publish-guard-report.md | 783 | 84c217f5f22194a69c9bdceb4250e9b93b36df41e6a7df43eb0bbe607b4f4fa0 | a315afb16c9f50bb7e38dae7959aa9ceb29837b4 |
| published-recheck-report.md | 29476 | c866b1ede49a433664091df7e8e2a78b84f37035ee595b6eb10a52cf98350238 | a8e4ce67bc50383b4481d16d18e62c76971bc37d |
| source-report.md | 5825 | c2fce82e4d57c0211b749b8797b82846515ceedba8b18725c7a089b2b23eccdb | 63de202b3a901c4f53b087508bd0572da06898c3 |
| check-report.md | 5825 | c2fce82e4d57c0211b749b8797b82846515ceedba8b18725c7a089b2b23eccdb | 63de202b3a901c4f53b087508bd0572da06898c3 |
| curated-report.md | 3553 | 49e5137c3be41f046e28c972a0efd9c6af5791950f1a55a90ad3807f25ece827 | 651efc14c6e3ae9f8d6ebe031beb0653e882a636 |
| sources_status.csv | 2601 | 62bdcd2d0a2f525a20a683b5863ec9586dff05d4f5270a37197a17fffece9885 | 4775dfc856a198bac51473e1b0789d68125b163a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
