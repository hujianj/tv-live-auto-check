# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 36313
Unique payload blob bytes: 24360
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
| final-publish-report.md | 2811 | ada12c78d8b0068fa5a28bbad2cedb1a9412be44edfed0dab91050fe781edfc5 | 9c5068f55a3caa81ba3a1df52c4554e52cfb8eda |
| coverage-report.md | 1399 | c6fe10be3b03c4b1dc19d43ae8d5e3bbaad2c1c80e51c07541f55f97dbff6dff | d953cc8fc8890e882dcaa1c929224756ee9f43b6 |
| quality-audit-report.md | 3033 | a46d6d215e0d9ec55e6050949917f667fd85173f9c260d0a53bb85af00b1e6fc | b813ea460f49ea71d88be1777e7125fb371e7268 |
| publish-guard-report.md | 1837 | 418f373f4d6deac4f4533ef3dda9ccd67b2c82121719a714773bd9315abb307c | e0144307087119da3d79e255750a7ee348f2783c |
| published-recheck-report.md | 1290 | bf2565706816c8f0826451e4f058b54bd9f2e9e1cf106af9849f7621b38ddfa4 | 52b1bcd4723fed17c46685ada15b5475cca582ab |
| source-report.md | 5812 | 7bee91b1e2f68e42cb597018a2d5533c98646cb41eeea57843f6f8f9cc28c5b5 | 76ea1494186c4d349787b1069567605b438c0980 |
| check-report.md | 5812 | 7bee91b1e2f68e42cb597018a2d5533c98646cb41eeea57843f6f8f9cc28c5b5 | 76ea1494186c4d349787b1069567605b438c0980 |
| curated-report.md | 1478 | 60ddf35267441a295a3a6efd5b8c43c248cb6930d07c637ea0636a44f7da7822 | 9e02db9b1dba4908eb7f59bf286200d161e2569c |
| sources_status.csv | 4139 | fdfc6cd9f58a4fa71df98da3b1c49c7c5553d5d14c7848c130413149893a938c | 889eb7e55d27e10ea1b84571091cf890b12b3efe |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
