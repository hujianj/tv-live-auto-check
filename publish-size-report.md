# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2045095
Unique payload blob bytes: 1482083
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 470490

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 156830 | 81e78e237625056378bed2881cb3c3e93264340d32b602c3b020d4956a5372f8 | a356bf9c7ad02c2fcf5f722816702fbd2053ff39 |
| live.txt | 156830 | 81e78e237625056378bed2881cb3c3e93264340d32b602c3b020d4956a5372f8 | a356bf9c7ad02c2fcf5f722816702fbd2053ff39 |
| live-verified.txt | 156830 | 81e78e237625056378bed2881cb3c3e93264340d32b602c3b020d4956a5372f8 | a356bf9c7ad02c2fcf5f722816702fbd2053ff39 |
| ku9-live.txt | 156830 | 81e78e237625056378bed2881cb3c3e93264340d32b602c3b020d4956a5372f8 | a356bf9c7ad02c2fcf5f722816702fbd2053ff39 |
| live.m3u | 281791 | 4a217a3b923e3e60307f6699aef3f433bcb0562b26bf0ec09a4a7ed8f5de8845 | b0963f057947f17cf633c94c0818b4cd6018cdc9 |
| ku9-family.txt | 85935 | d786cc4e429bcc769cae5d31dcb90444997e767033c527725ecc7f4074db364c | 05260ada4e19a0105bceb5d1c019e20731bdb1d6 |
| live-family.txt | 85935 | d786cc4e429bcc769cae5d31dcb90444997e767033c527725ecc7f4074db364c | 05260ada4e19a0105bceb5d1c019e20731bdb1d6 |
| family.m3u | 152399 | 77d61dec64167472b0ff580dc0878ec2f2f44131f28a4ea43f01b7d2ecfe29d4 | 8e371ee546da758c86f5726d7286b7d88d2f338e |
| stability-history.tsv | 737021 | 86cc704fed99ec04931d1a37204e20f0f43a3504e5d8f6142d905924e9ef1da1 | 0031c651a714346f5e4ebcd51d248d819dc8c824 |
| final-publish-report.md | 11626 | a435d337650261568b4b579cd652bd9df2f72b95986b179d3f1ab53a16822769 | df935aa9410728ee900eef6f0760f3cdf5f1faac |
| stability-report.md | 12194 | 7d2a9f919195e19a95390782e2f08fcb975e4c8c0edc6c80afcbe120f02bfad7 | ab11b6598d4c998088c53d6e3d66b32038e2c0ed |
| coverage-report.md | 1291 | e6d16cb2e91a23b37f87a667fb8bfa9b144a094ede1956ddaf7631ea0be8205f | 907ba36c30a4c52632ae3a2ded822761a38ffa2e |
| quality-audit-report.md | 2063 | 29f8f4a47434773c387474bf5380f331a3774550ce8407ca03c6548fa0af6b08 | 1eb40eeede9df6a4707fc826fef63ce40b2617fb |
| publish-guard-report.md | 1147 | 5d4f826f7422643598cb2e293b5df74a740e5e83dc666bca43c1c11b61b01254 | 3d72588ea3c1a874eff867b3fe0e543a9ec04c10 |
| published-recheck-report.md | 26758 | e6cac4099d7e49d0b74f3bb23662544a50532f7cf7cba9a10f0cb2f14fce162b | ec14cdbc6fec817d5680130b9b408acab7b9315f |
| source-report.md | 6587 | fd1948e4a29397a95177da0af59e4d6ad15cbb3dd0e2db040f9a0d5ec4319b33 | 315a43a7c54f5e76631fdb2fd0d02b2e50325704 |
| check-report.md | 6587 | fd1948e4a29397a95177da0af59e4d6ad15cbb3dd0e2db040f9a0d5ec4319b33 | 315a43a7c54f5e76631fdb2fd0d02b2e50325704 |
| curated-report.md | 3307 | fcd91115b9d5055361596a895fdcdbb1fa6a8e5f54a3ca6c6605f352b1f97597 | 38a9abccccce1d55b9f31835d86000175b964421 |
| sources_status.csv | 3134 | 8ceb24c6dab70f81d3952623a68e14c789f96cb86b4b7b8b2e8b9eac2a90e7fe | f6178f8a3c1e22a164f224706821f878b96720cd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
