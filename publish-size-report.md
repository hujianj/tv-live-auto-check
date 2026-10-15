# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 303346
Unique payload blob bytes: 199470
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72270

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24090 | 3fb47084e7b0dd19aac33a269a96a925da98adc82ecf7f5bff96414957f37840 | 90830a19b6d62c7156a0b64459642fc1fcb4219c |
| live.txt | 24090 | 3fb47084e7b0dd19aac33a269a96a925da98adc82ecf7f5bff96414957f37840 | 90830a19b6d62c7156a0b64459642fc1fcb4219c |
| live-verified.txt | 24090 | 3fb47084e7b0dd19aac33a269a96a925da98adc82ecf7f5bff96414957f37840 | 90830a19b6d62c7156a0b64459642fc1fcb4219c |
| ku9-live.txt | 24090 | 3fb47084e7b0dd19aac33a269a96a925da98adc82ecf7f5bff96414957f37840 | 90830a19b6d62c7156a0b64459642fc1fcb4219c |
| live.m3u | 45811 | 903144702b0612fc46f35f4f40c61a0dcb147d4dfc4817b1bdfac2e60f26d040 | 02934034bf515ee6996459101f9a40fc92c2cbe2 |
| ku9-family.txt | 23723 | 998cc94ad4ac9511c62a0b28555b393e48721bcd1f6a0e37308ab38b520742bf | 6bc2db65d8b68e9e6fcf4c93f4dd25fa317c92e3 |
| live-family.txt | 23723 | 998cc94ad4ac9511c62a0b28555b393e48721bcd1f6a0e37308ab38b520742bf | 6bc2db65d8b68e9e6fcf4c93f4dd25fa317c92e3 |
| family.m3u | 45134 | c95b1793a34432205a282ab996eee73c787776900fcd86df632309921a1ba8f9 | 0b77be219abecfb28b9033e15a524c739990b52b |
| final-publish-report.md | 10696 | 35c5e630ec62e52d42e417eb92e66c17e81051af5b9c6ae2ba68d079cc790794 | f1ee6172992aabf25538568cf8346d64b10875bd |
| coverage-report.md | 2180 | 4e14db0f40c4a6de16cc00a3eb705b5926f0cd7866bb692bd628d44b42281b7c | 286acb232cfdde45fea9b5bdcd0c0d3f120100e0 |
| quality-audit-report.md | 4698 | 9ea9cf0d9af0ea94a06dcdaf4fa2d0b2767a1443b69f7174abbc1a602fec2abc | ba2545a477d17e30a1d4dbe15ac0e34725fa4ea9 |
| publish-guard-report.md | 1534 | 6dda64510c73b8b7e4cf775afc10d2dbc794480605db51331a3fc84c44f367ba | 3702430469a10739f5f55f3119d4dd8a82980421 |
| published-recheck-report.md | 27835 | e95a84f8b89829c59849e52bfa58a6712922246273505393558c3c63049010aa | cab8eadc072a7ac55c7bfba5e5d85e9f7403383e |
| source-report.md | 7883 | 7e3001cf83854d5132c4f20d41ac70db47ef32756521e450048e15c552b6b4c0 | fe0a947b63c4e444a2e34654ee19f92c05e0fcbf |
| check-report.md | 7883 | 7e3001cf83854d5132c4f20d41ac70db47ef32756521e450048e15c552b6b4c0 | fe0a947b63c4e444a2e34654ee19f92c05e0fcbf |
| curated-report.md | 1804 | babf3f44fe062b5414f1fc4082028078689e9807b76bb7430971e2bc4deeafb3 | ae2ffc88b90d18de05ad92b7ee60f96e9c6eaa03 |
| sources_status.csv | 4082 | 6d072b6224025652d550b0e88f440e6064c3665812c784cc9198fe67713b36d9 | 7561a51dd47aff3302246977097e145e96d114bd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
