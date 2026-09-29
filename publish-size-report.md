# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 271117
Unique payload blob bytes: 180635
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 61980

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20660 | eac63fd8289457457f75957ca46c621e1bf7cc4303d44ce2129cb6fa7f122fda | c5dc158711ac2e81b54250d748c12d31af6b0089 |
| live.txt | 20660 | eac63fd8289457457f75957ca46c621e1bf7cc4303d44ce2129cb6fa7f122fda | c5dc158711ac2e81b54250d748c12d31af6b0089 |
| live-verified.txt | 20660 | eac63fd8289457457f75957ca46c621e1bf7cc4303d44ce2129cb6fa7f122fda | c5dc158711ac2e81b54250d748c12d31af6b0089 |
| ku9-live.txt | 20660 | eac63fd8289457457f75957ca46c621e1bf7cc4303d44ce2129cb6fa7f122fda | c5dc158711ac2e81b54250d748c12d31af6b0089 |
| live.m3u | 39729 | ee0555977e8987b81cbaefdb1376f9c5f77d376a6bc41aa854a1410ff1c3716c | 1078e05fc24454a06ad50283ecc85e16ec1e8f14 |
| ku9-family.txt | 20382 | 4a629480e1204ee857dfff29fb8a9d17183fa228000f63f2fca566a048c868f2 | a6e4041eb95776b1cca61d3cc9341cec9933524e |
| live-family.txt | 20382 | 4a629480e1204ee857dfff29fb8a9d17183fa228000f63f2fca566a048c868f2 | a6e4041eb95776b1cca61d3cc9341cec9933524e |
| family.m3u | 39203 | 5f03227bcb8ac57fbf24ef220dee613c913e196451012fa8deca77123ae2b519 | b2a842cc2fac624c0ca26ff4aa713d9f81251143 |
| final-publish-report.md | 10884 | f950d3daf0ca983dfbd8d9263702c4876d78e812fbbc577e566113644b157951 | 98e5fa7ca7072f4bac5c30f62cf45c00cb56a64a |
| coverage-report.md | 2230 | 824e43249140c869d3320166f33a8469458758a6718d84c9085466944cc4f289 | eabc08cb07f0d3a63075020a591ef1afab72f7b9 |
| quality-audit-report.md | 4730 | 73ac3fcc4f91dc0760059c4ff398dbf41273069ed8bf6696c12136c30ac09769 | 74056d9796eeae70074fc10262ea41c87e545b0c |
| publish-guard-report.md | 1555 | 004ab44247c679236dcbeb7134ef415761095853c4b81f10c1f13c765260a8f5 | f67eef10d2b267858e9da756cc0a66b1b8aedd15 |
| published-recheck-report.md | 27206 | 0f38a5635e466b2c1cc6732abfb5dd80e6625566e3335a74f629d56048d58188 | ff9424d5dbfa22744a55b507cd230e5a33d63d43 |
| source-report.md | 8120 | 47d3e90630f0d74abb7a06aadfcd99d75b3b885ca46a831270fa71e8d32b2d04 | 03a9185d3bc6462b54f68a0f00c4fb68d9c4a6f0 |
| check-report.md | 8120 | 47d3e90630f0d74abb7a06aadfcd99d75b3b885ca46a831270fa71e8d32b2d04 | 03a9185d3bc6462b54f68a0f00c4fb68d9c4a6f0 |
| curated-report.md | 1804 | 4ca0439d0152adbc54e156d831f29eb3675d9ea1ecf9813a88d8baa3cf373d2d | 0733cfe160fe59576caf54ba1f56fd1bd6f5aa43 |
| sources_status.csv | 4132 | c6d1f7bf695e7d0b1fb19b11c5c93754733d41ba5a6fe453a23c66d637631fc7 | fd1b1b8a4a24dbb2b10d14906f6c69dcccb1ea58 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
