# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 337737
Unique payload blob bytes: 273676
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37522

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18761 | 665a0b272bdbc8c23c74278bcd98343e44604d001cedbec984731150d18c391e | 00d6bdbdb069010dd817d3fbda3b196cb5298463 |
| live.txt | 18761 | 665a0b272bdbc8c23c74278bcd98343e44604d001cedbec984731150d18c391e | 00d6bdbdb069010dd817d3fbda3b196cb5298463 |
| live-verified.txt | 18761 | 665a0b272bdbc8c23c74278bcd98343e44604d001cedbec984731150d18c391e | 00d6bdbdb069010dd817d3fbda3b196cb5298463 |
| ku9-live.txt | 22419 | 72162d092e34e7e75b8f2f342391c5a3b7481d7d710a84a499085a6d3e355204 | ef32f06157fd6e3f8602a86c9e249c652345f09e |
| live.m3u | 36061 | 0561d1ae16c41effb2724df907be2022d865de76da038a795cebffbe84813449 | 2e590039dd1fcb96366aa4fc9d9880168bb98c47 |
| ku9-family.txt | 18382 | 6e789f698f7f8cddcbff0c4cf579d9e69a3596cf9a2471c80932cdbae5ccc50a | ece10b5022f8eba573ab3042c471a4dbc6ea39d3 |
| live-family.txt | 18382 | 6e789f698f7f8cddcbff0c4cf579d9e69a3596cf9a2471c80932cdbae5ccc50a | ece10b5022f8eba573ab3042c471a4dbc6ea39d3 |
| family.m3u | 35372 | 1e700452e601d33ff28423f6a398f522762bf5823aa522621d54fac33f651bec | 8d34da2a1a0a5b4c469f130592fa4082f2fc90e1 |
| final-publish-report.md | 10917 | 467a02262945ac1a7b960e091acc1ef0b4687e033430b65fe211bb27fb7f5927 | 2d84f6ac3ea5de26af7b32dc369890b827e5bd89 |
| coverage-report.md | 2200 | e7399567705c085a9d2d5223861b80051ae910918b333c41de6959a393f5a9d6 | b9a536938ddb8f14e1021555b742348e2fa62fd1 |
| quality-audit-report.md | 4674 | 3c5d6f843c4ed5539a2770f935f750535508453aa5ce3fc6f160b268adffed44 | 62069909a9f42ef80c8a0d583d7f61addeec1cc4 |
| publish-guard-report.md | 1530 | e790b85d73f2bd1b240ec3550950213f5bca227b6e3bf3d18b5fd176e403d789 | 3522048c33fd38f34d1133a6ab1844b0560096e7 |
| published-recheck-report.md | 30857 | 3a2496c9324c9329c7c3074a287450bfd2aac4df663f420a39e288767054fd96 | 6e23387a923bcbc2f2521dc49a4806d26c22d5a0 |
| source-report.md | 8157 | 8fb7622974c888ed64754a7d0956670fb11e40a1f2136088bcaaad31de318bc8 | 81fa46b3654a1611001b2d3427f61879b4f1a8b4 |
| check-report.md | 8157 | 8fb7622974c888ed64754a7d0956670fb11e40a1f2136088bcaaad31de318bc8 | 81fa46b3654a1611001b2d3427f61879b4f1a8b4 |
| curated-report.md | 1833 | 93fc741200bac33eaa70eec5488bcb887c02c9b68ae07fffeb6173808d15f9b3 | 0db42bc5c6ad1565f07a4a440b99a1991f938c36 |
| sources_status.csv | 4240 | 4a64e867729551a529e5f158d48d3607f64a10f8f10bd197a683d7b2e9306159 | 05f5de552ec1807cca4c24d80f3ef1e5ff09daee |
| tv-coverage.m3u | 50694 | f3de33e418f740ff11bc0849670d1d4d7c43f67bdc3d459abbb982945f661632 | ffc45cd9c5e10cfb1e36e2b45926cc2f6f308cbc |
| tv-review-report.json | 17562 | 26b416c564e232e0715db63e2de4fcc72bc4ca73d1060e70c37943f9a6fde937 | eb567db0728fb6646a3b6885a5148a930fcf2628 |
| tv-review-report.md | 10017 | 0b29d41a82246e78e8d46302d41f6cd6d0525940d14b89fa64a03729ff75c5e4 | 80f081ee8bd714632b9ce56b96db674980dee817 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
