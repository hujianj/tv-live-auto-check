# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 307574
Unique payload blob bytes: 202501
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 73116

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24372 | 9d5e6ca823d4bca1f1221203fefc9df5ebc1661aab5416b9a01fc35a204b1d03 | da869a4025fddccdaa4449d3748d3a705cf28632 |
| live.txt | 24372 | 9d5e6ca823d4bca1f1221203fefc9df5ebc1661aab5416b9a01fc35a204b1d03 | da869a4025fddccdaa4449d3748d3a705cf28632 |
| live-verified.txt | 24372 | 9d5e6ca823d4bca1f1221203fefc9df5ebc1661aab5416b9a01fc35a204b1d03 | da869a4025fddccdaa4449d3748d3a705cf28632 |
| ku9-live.txt | 24372 | 9d5e6ca823d4bca1f1221203fefc9df5ebc1661aab5416b9a01fc35a204b1d03 | da869a4025fddccdaa4449d3748d3a705cf28632 |
| live.m3u | 46618 | 3f6187e7b96676ce2a7e2dd3482019ef7b01b6241a0abcab51a4d75da5cc5d16 | fb5f32c4be4ecb91a9d42c214e7debc6b6a59f71 |
| ku9-family.txt | 23943 | 2c2b7bbd28d51971ea29e698d4c871d5b9147151930e855a37f6d2d75ec41307 | d1c7101b06ff7db21de0c5269dbcd9bee6a5e1f6 |
| live-family.txt | 23943 | 2c2b7bbd28d51971ea29e698d4c871d5b9147151930e855a37f6d2d75ec41307 | d1c7101b06ff7db21de0c5269dbcd9bee6a5e1f6 |
| family.m3u | 45817 | b005e4be2956dbf4233d6c21e2cd91552ea8a01b245a8c2eb7797590894e58d1 | 083501e2baf320714fc8c1f6a0ed320edaf30f67 |
| final-publish-report.md | 10439 | ac1a30543b11f97d7151905f6d8ee0a8b9b743204f3c7f67c93f21f1bfd4bdd1 | 7b0e27292fef3c647ebcf442386a6dc3754caa55 |
| coverage-report.md | 2229 | ef3501d49f6be5669755c752b331641cb31b3e309a75305589e0d0e5c836551b | 92e2fcd8a3acbf22e0cf82ea6e4617c67c171155 |
| quality-audit-report.md | 4716 | 0078c8a08eb3ab72c1ff19ce3baaf977478d6958c61026258b94a0c1135ac971 | 8d737e24fe07880bddbfd57ae37dafdb4fac3d8a |
| publish-guard-report.md | 1535 | 55e438dfc4637b4c7a599246d1a69f4bc1593e2e61453cb7f657fbd0a93327d5 | e8e5b048ea4a9305cd70cc30490a8af8044cb78b |
| published-recheck-report.md | 28878 | fc0a18da5e351f89923a8893c74570fa1a901f6aae43bb25861773da191a342d | 906f67d601df5f12a999056c584edbf7cbfe99cf |
| source-report.md | 8014 | 856de7cf3a17f3a3fb2e9897824c8e0df488d0e971a9795216563c84dffe58b5 | 63c697fcd5bf9124155103ea80b14c7d02892e7d |
| check-report.md | 8014 | 856de7cf3a17f3a3fb2e9897824c8e0df488d0e971a9795216563c84dffe58b5 | 63c697fcd5bf9124155103ea80b14c7d02892e7d |
| curated-report.md | 1860 | 93681b88e4f0fcb326d6c7ba668147134b6e9286004a62354c989bb83b3b0483 | d406d00fc20e8535ad97a673c75d6ff79c61350a |
| sources_status.csv | 4080 | 93cd32490d413d5c0fb4732d3db9f3732e8225c45262cb6caa2e37429c12c3eb | 0c7913bdf0941de58d1d9543a2a98c38e5f2de80 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
