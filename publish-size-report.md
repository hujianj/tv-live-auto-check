# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 36006
Unique payload blob bytes: 24091
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 2685

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 895 | 776963f10b172609120a58bf887e53e7aee2b3ffba54995b174ea9d7d01b1d49 | 610539f1be390b03fb38c95f3997d1d63f1d0c8e |
| live.txt | 895 | 776963f10b172609120a58bf887e53e7aee2b3ffba54995b174ea9d7d01b1d49 | 610539f1be390b03fb38c95f3997d1d63f1d0c8e |
| live-verified.txt | 895 | 776963f10b172609120a58bf887e53e7aee2b3ffba54995b174ea9d7d01b1d49 | 610539f1be390b03fb38c95f3997d1d63f1d0c8e |
| ku9-live.txt | 895 | 776963f10b172609120a58bf887e53e7aee2b3ffba54995b174ea9d7d01b1d49 | 610539f1be390b03fb38c95f3997d1d63f1d0c8e |
| live.m3u | 1666 | 2262bb265b89898dc6d81c595c8eb96a44fa505f8aaae9b9c542c3ca6cc2f95a | a7642411a1074eb26f3e21919b48ef69320e145d |
| ku9-family.txt | 895 | 776963f10b172609120a58bf887e53e7aee2b3ffba54995b174ea9d7d01b1d49 | 610539f1be390b03fb38c95f3997d1d63f1d0c8e |
| live-family.txt | 895 | 776963f10b172609120a58bf887e53e7aee2b3ffba54995b174ea9d7d01b1d49 | 610539f1be390b03fb38c95f3997d1d63f1d0c8e |
| family.m3u | 1666 | 2262bb265b89898dc6d81c595c8eb96a44fa505f8aaae9b9c542c3ca6cc2f95a | a7642411a1074eb26f3e21919b48ef69320e145d |
| final-publish-report.md | 2830 | 855866ac86c5aad7d6750347e19e5fe0f3bef9a224241c94c1e62af5b108b3ac | d4491d55a2a6eb5e3914bbc5ca71ce0796b16cb0 |
| coverage-report.md | 1399 | c6fe10be3b03c4b1dc19d43ae8d5e3bbaad2c1c80e51c07541f55f97dbff6dff | d953cc8fc8890e882dcaa1c929224756ee9f43b6 |
| quality-audit-report.md | 3033 | a46d6d215e0d9ec55e6050949917f667fd85173f9c260d0a53bb85af00b1e6fc | b813ea460f49ea71d88be1777e7125fb371e7268 |
| publish-guard-report.md | 1587 | 31943be05b10d9c57ec008370405b11a7aee32fa5ffd525bf1a9f43018a9c462 | cb27285dd2ec56b3e364a955a04186c0b29a1b82 |
| published-recheck-report.md | 1290 | ee871a86674acaed4c90ad12addb1d5625e0b60364e90b3506ef4650309673fe | 044877180ee734378e3207482f6b0696c73b79d0 |
| source-report.md | 5774 | a84b1ca61b43ca39d4f5df7171570a250515bdfaf9b262567bc3038a493139ff | 858506a2230fc7ede25a8d52e525d43391f8a3d4 |
| check-report.md | 5774 | a84b1ca61b43ca39d4f5df7171570a250515bdfaf9b262567bc3038a493139ff | 858506a2230fc7ede25a8d52e525d43391f8a3d4 |
| curated-report.md | 1478 | d8818a4d1f20a228f26534f67432fcdb27e6ec0f6347fee5d8e6a0a6b5f34d66 | 7ba247fa47ebb65cd8f4795b176790b80e2ed874 |
| sources_status.csv | 4139 | 4c0a1e1f7137eb0f6e8e64d3dc046550d162595fe9c2d3f7ef16b8ac810a5640 | ae476b008be04d4c9fe48484aa9ba7b2a6a68110 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
