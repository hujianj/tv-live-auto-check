# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 290909
Unique payload blob bytes: 192792
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67863

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22621 | 515d3c6381e9ec3d07580d2c2dbebc738f91d92b1053ed24ccb51a09b99e9ab8 | ec11d54e5f4765ce9fad42c0b8ebeca4bceae881 |
| live.txt | 22621 | 515d3c6381e9ec3d07580d2c2dbebc738f91d92b1053ed24ccb51a09b99e9ab8 | ec11d54e5f4765ce9fad42c0b8ebeca4bceae881 |
| live-verified.txt | 22621 | 515d3c6381e9ec3d07580d2c2dbebc738f91d92b1053ed24ccb51a09b99e9ab8 | ec11d54e5f4765ce9fad42c0b8ebeca4bceae881 |
| ku9-live.txt | 22621 | 515d3c6381e9ec3d07580d2c2dbebc738f91d92b1053ed24ccb51a09b99e9ab8 | ec11d54e5f4765ce9fad42c0b8ebeca4bceae881 |
| live.m3u | 43074 | 4ce82870b547c47a3b04b00671c6562598f781ffda0cc23332792ca375f661b7 | d3c7dd8576a31aa29bfa1a3afd9ceb440d125014 |
| ku9-family.txt | 22186 | f580f733d15e160ec36b3a6fd58c6f2fc4c10fdf817a2cc89483219f3ea87e2b | b326cbd16557e11781e41e4e7a98b8df33dea708 |
| live-family.txt | 22186 | f580f733d15e160ec36b3a6fd58c6f2fc4c10fdf817a2cc89483219f3ea87e2b | b326cbd16557e11781e41e4e7a98b8df33dea708 |
| family.m3u | 42267 | e0da077c80846b20d4d7b6f5b5e03db24ed497e073cbe32c27f5ebf63b0b6465 | fd10b6aef33226045e11204b390d808a71fdc4b3 |
| final-publish-report.md | 10831 | 7a29be329badd4c0c680d520bd628d727b042efa8e05ed35abd5c07b9c42b2c8 | 14cfe04f0e4c76c91e97b4f57844d37c0eddb95e |
| coverage-report.md | 2235 | ea1e3f4c41d0cafe9ed8c11cbc5ba9eea8eed7799ba21c39bd5828064366510d | d98f0d22848f36c7aea15677a605e459a16c7c03 |
| quality-audit-report.md | 4729 | c553cad9902bdcc4cf99dff003c3a306ed1df23e54e359c3999e109a9185af46 | c460998a9fbc3628125fabf3ebda7c011f289112 |
| publish-guard-report.md | 1586 | f9f77700919110cbf2445493b5e6cc6d3f2fe5094acc96aa148c42774416d7da | d92640eb4cf9f01615a27ae75dc3827bcdac9c38 |
| published-recheck-report.md | 29309 | f459c43f614a192421b4cf41b70d648054ed6377219917d783ff06aec5cea5a4 | 0f3003df5f91fd2bc3164a187873b07c90a01739 |
| source-report.md | 8068 | d0391dac034640496c15da897e82db001c1756cec635cae175d272ed08d7bb2e | 839fde14eb312c93e9048fb7e3b5baa4bfc9e4f4 |
| check-report.md | 8068 | d0391dac034640496c15da897e82db001c1756cec635cae175d272ed08d7bb2e | 839fde14eb312c93e9048fb7e3b5baa4bfc9e4f4 |
| curated-report.md | 1806 | 1d991cd412a169f7b4c481d68b7d43f5e5f9785466210664b578af54b86781a2 | e41afdb9735576f9f401d31f01870efc500bcc62 |
| sources_status.csv | 4080 | 4948494e35e85b1ef2abf825426c7b9c2cd42fda0ddbe729a2e77f194dece512 | d34673a5a0b6d2cba4c6e9ee0683b693da587bfe |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
