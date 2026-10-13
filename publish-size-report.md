# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 300977
Unique payload blob bytes: 198880
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 70815

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23605 | cac436c5a2f6bb897aaf472437c85dea6e5dd84ccf1f723c1c35736293fa9fab | af092031830a10588bf059da2d0726f155922d21 |
| live.txt | 23605 | cac436c5a2f6bb897aaf472437c85dea6e5dd84ccf1f723c1c35736293fa9fab | af092031830a10588bf059da2d0726f155922d21 |
| live-verified.txt | 23605 | cac436c5a2f6bb897aaf472437c85dea6e5dd84ccf1f723c1c35736293fa9fab | af092031830a10588bf059da2d0726f155922d21 |
| ku9-live.txt | 23605 | cac436c5a2f6bb897aaf472437c85dea6e5dd84ccf1f723c1c35736293fa9fab | af092031830a10588bf059da2d0726f155922d21 |
| live.m3u | 45239 | 6b31d6bcb07090f7993336a956107e80e1e0aa4f81f16c165bfd651ac0343db2 | aae0d1a90f5672cec6e08a5e3ef0e0ec128c7598 |
| ku9-family.txt | 23176 | 186dbbc7edca4062553771e39f011bd2e6c3ac2d56d8bd95d1003b28f953ddc4 | 5175e5dac0a09f63f3b6d8cfab5e995faceaa4da |
| live-family.txt | 23176 | 186dbbc7edca4062553771e39f011bd2e6c3ac2d56d8bd95d1003b28f953ddc4 | 5175e5dac0a09f63f3b6d8cfab5e995faceaa4da |
| family.m3u | 44438 | 05bba0a8a236fee138011bea7113d86c54f015768834e27c969202948ba317ff | 9531174d4f5c46c69278d340b6670b23b777670f |
| final-publish-report.md | 10745 | 3789aa8bd2ca0881b642c2e02c4ee4fe8a38daddea23f8cd47d41b2badebd8e4 | c5180d1084281a8f2d1fd26e99cb7ebe34804f14 |
| coverage-report.md | 2220 | a4ddfa4368acb37a194d9888f5f9b0db583750a11fc217282b1b447e531325aa | 48fe4ea82d8b5c3d10d949018437597e1a72cfe7 |
| quality-audit-report.md | 4718 | 12d7e33e32f0e3b9c3a6a26c1b170e24b7d3dbb5598406abb9936fbae7852d26 | 264bf3a7458ff856bbcc87ac23b673ac774a06d9 |
| publish-guard-report.md | 1558 | 93ea9ae8d55ff4967d4f1c7f1985687f834908e110040c224e1783499f1703d6 | 89c8593d6cfec121ba5c0ef3740f0f03add56749 |
| published-recheck-report.md | 29133 | 453566d1e510b81ada69c80e93a838638063ae63296aa440b79fe3b60efe26d4 | 44ff45ba1113cddd7544f72d846e67b10afda3c7 |
| source-report.md | 8106 | c1dac4255177d83408f4d85f3a5c4f32eae94c93282225a6e4320125acb88d38 | b2c777253ae4eed1f3806ccc8e0dca3008e6f9c5 |
| check-report.md | 8106 | c1dac4255177d83408f4d85f3a5c4f32eae94c93282225a6e4320125acb88d38 | b2c777253ae4eed1f3806ccc8e0dca3008e6f9c5 |
| curated-report.md | 1804 | 61bc6aaaad6106aeef8d2905f803e568d836a07d6e20f055b0ec844ac7830f39 | 2735466e3657b58fe13720a84a81a1d31803f226 |
| sources_status.csv | 4138 | 6d555fbf41cbdd67dadc70de715ea58c9e6985068646a7c739070e1238fd4bb7 | 90722185e4a92f19c14e250becbab458f93734ea |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
