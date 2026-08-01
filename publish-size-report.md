# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2449911
Unique payload blob bytes: 1705681
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 641604

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 213868 | 15dadb8852489dff3d0f112bbea22ae8bb66fcb28ad789ec9f952ff5ec600638 | 666ac1b4bbd15e3d30e229cf79ba42fd1a6fbcc5 |
| live.txt | 213868 | 15dadb8852489dff3d0f112bbea22ae8bb66fcb28ad789ec9f952ff5ec600638 | 666ac1b4bbd15e3d30e229cf79ba42fd1a6fbcc5 |
| live-verified.txt | 213868 | 15dadb8852489dff3d0f112bbea22ae8bb66fcb28ad789ec9f952ff5ec600638 | 666ac1b4bbd15e3d30e229cf79ba42fd1a6fbcc5 |
| ku9-live.txt | 213868 | 15dadb8852489dff3d0f112bbea22ae8bb66fcb28ad789ec9f952ff5ec600638 | 666ac1b4bbd15e3d30e229cf79ba42fd1a6fbcc5 |
| live.m3u | 385534 | 6f58148f6bcf03616bbbd5f8114375e96d35e9e9bae1fe0f0f0151f481e923c2 | 49260e1f4291e695573bdb9083c054ac2a9d5496 |
| ku9-family.txt | 96804 | bb9e57d9be998b9550033604616a2530e19ee4fa3902d4715e12a77c8e6fde0c | dbe3cb07cbf9c78fe85822dcd9550bc3535d2550 |
| live-family.txt | 96804 | bb9e57d9be998b9550033604616a2530e19ee4fa3902d4715e12a77c8e6fde0c | dbe3cb07cbf9c78fe85822dcd9550bc3535d2550 |
| family.m3u | 176308 | 17bbb3c69fb4bf9c6885209e395af7dd8be905bd2d82b07e45a370f4d39c87de | 230c6c3042eeb53cf4bf25b6c09e6e66ec7ed73e |
| stability-history.tsv | 764922 | fcbd525e3ace34982c03c8f1d65c5b8d5773973ad545fe3d30e3c1d25c2ff8e9 | aaad5684ee3c619d528ea721b243ecb2c3fdd082 |
| final-publish-report.md | 11440 | a9f2bbdb88af366ca4f1ae27acfc143e6c7fb4ea1f242a2f2f6c59aff4a145c7 | 46959ab86caa297bba69952000c1fe47a2f1b111 |
| stability-report.md | 12892 | 932dbf7d48d7e42ba47f10b780242ea5be0adde626a5a9d287170f23cd2043fe | 389e0e6daf57c72c1ba8631401a19481a12c7368 |
| coverage-report.md | 1310 | 27dac15c7b898cc086a12c5b4683bd3db220e316e60a58855e17e5271b9cdfca | 44912b8063b05fbf1d9368ae98674666979a4c10 |
| quality-audit-report.md | 1504 | 981d4754592d36307d0a0746ac1009f5ddbe5a5bd86a0d661f2dd6aa704f5b29 | aab5955fd039e8c79f7d6474a17e8b9092aa3088 |
| publish-guard-report.md | 788 | 598de2e0a3b55efd9c0949db1046929c6cf0b364ede28920bee747c50fefd0ca | adb02c5bec73224a367f3bc2e10afcc825e25f02 |
| published-recheck-report.md | 28278 | c9aeb74749c604732771fc7a0584ca31e8cd618e7bcebdb72202589f864e792b | 682d5777b2b84d510d5e2df0d2a21adafcb4c48c |
| source-report.md | 5822 | b983d5ac776c303b49686ca69b336f6cf92766fc9cb4e7c03732bde6d8fa7f2e | b88e658b671f5159246428c21a73ff1c85c0b3f8 |
| check-report.md | 5822 | b983d5ac776c303b49686ca69b336f6cf92766fc9cb4e7c03732bde6d8fa7f2e | b88e658b671f5159246428c21a73ff1c85c0b3f8 |
| curated-report.md | 3611 | ef7dda9ff58d5f2a38a61869701a4fb4bf115cf40c0cd8b209424821c5eaa7fe | 8f29bfb3724add12a64ec8c3e4e1d2c57688a21e |
| sources_status.csv | 2600 | 9031ad3c9987d1fb8dfe27ebf91422d74df3092642082ec5dd0deeceaa92333e | 5b02c30929dcf5a77d2541828213d466c53b5b89 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
