# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 277424
Unique payload blob bytes: 184393
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63912

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21304 | 42d3ac2e02eeaf45b860d25fba5c92e35ed429a0585b3754523a59395e584554 | 4b5a1997cac525e23c4f7db32267ddbd93d93f7d |
| live.txt | 21304 | 42d3ac2e02eeaf45b860d25fba5c92e35ed429a0585b3754523a59395e584554 | 4b5a1997cac525e23c4f7db32267ddbd93d93f7d |
| live-verified.txt | 21304 | 42d3ac2e02eeaf45b860d25fba5c92e35ed429a0585b3754523a59395e584554 | 4b5a1997cac525e23c4f7db32267ddbd93d93f7d |
| ku9-live.txt | 21304 | 42d3ac2e02eeaf45b860d25fba5c92e35ed429a0585b3754523a59395e584554 | 4b5a1997cac525e23c4f7db32267ddbd93d93f7d |
| live.m3u | 41049 | 82f22ce6ee137e7e4052fa41e2e7df6d23f96f5944a8fd8c626524327660182c | 99ea6cd8fdcad6a1f52a4a4dd0dbc5553f75beb3 |
| ku9-family.txt | 21039 | 93eb962d2e3882f93e3b9dafac3c2ebce1ab6c82305ad560adf44a3d921a9b8d | a2af569459355e815bc66604f48785a81be112ee |
| live-family.txt | 21039 | 93eb962d2e3882f93e3b9dafac3c2ebce1ab6c82305ad560adf44a3d921a9b8d | a2af569459355e815bc66604f48785a81be112ee |
| family.m3u | 40536 | 92687f920c10857c0ed0183990201750e19acf8431bf9f2d22ffa874e72ef0f7 | b5787fd261b99f3dd725589b573943c552e9f3aa |
| final-publish-report.md | 10751 | 1d59275a0b2b674d007cb7b2e5bfaf6a99656dd3dfc9c17a632be719828280e5 | a0c7d2f583e2025833a37a85913ae0e460c4f5dc |
| coverage-report.md | 2235 | 93fd74eb97041b0faa0c9795514b7e065522e9cb7e2ef097531e48d0f9b0283c | 74ac497cb042c606c252311b4c37871634ca647d |
| quality-audit-report.md | 4731 | 92bf6a222e60ccb3e7b276c44e1d4f56aa11599061f7c30426534a0598287321 | 0df07d10bae64b8abfb96d63c8dab241e6bc0239 |
| publish-guard-report.md | 1608 | 3e9d7e64266d95b79cf5657f45d5cb134133964977eaaddb0dfa6501d1b17812 | 5fd68d18a922fd8bdba6c94ea4c876cee32dd4d7 |
| published-recheck-report.md | 27122 | 5041f2a8f2148e9fab85ee66ca636330d76fdc9f265dd15118ffe1daba95aa33 | 3e8b2c661a07a2bc6ed65ca99133fd47bb6e56b0 |
| source-report.md | 8080 | 1bea9ae79e00f6a9b01022b799bf7f913c199be1e4bb00b9377b0e6e9e2d5576 | 2b1bae5946872f1f45e452df8fb97a725710cabe |
| check-report.md | 8080 | 1bea9ae79e00f6a9b01022b799bf7f913c199be1e4bb00b9377b0e6e9e2d5576 | 2b1bae5946872f1f45e452df8fb97a725710cabe |
| curated-report.md | 1804 | a68110f080e78435492467f310f3cf8c4829017704fa36eb33378bf3b472bf0a | 140d0d101a5435ad28ec73aec5ad4e27adba4771 |
| sources_status.csv | 4134 | f41d7cc7955e0ec1b43683c7cbb723be6c9fa3054ca87ba543f9aa117ad08a1d | cbb64290b14645d86e9d2a85ef257224e6fb99db |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
