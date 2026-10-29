# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 260708
Unique payload blob bytes: 173574
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 59634

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19878 | cef6283c96076c2ec5c244ed010a624a3b3f38501412237d2de7fbd677897998 | ad86d6f8c23ff71dcdfb376e1fa7d9bb0fd51531 |
| live.txt | 19878 | cef6283c96076c2ec5c244ed010a624a3b3f38501412237d2de7fbd677897998 | ad86d6f8c23ff71dcdfb376e1fa7d9bb0fd51531 |
| live-verified.txt | 19878 | cef6283c96076c2ec5c244ed010a624a3b3f38501412237d2de7fbd677897998 | ad86d6f8c23ff71dcdfb376e1fa7d9bb0fd51531 |
| ku9-live.txt | 19878 | cef6283c96076c2ec5c244ed010a624a3b3f38501412237d2de7fbd677897998 | ad86d6f8c23ff71dcdfb376e1fa7d9bb0fd51531 |
| live.m3u | 37573 | 59e83614d850c21f9a35757b71a6a484996b573b98a20b624b3f3c2f2987face | f35d311727a4c2ddfbdb7f3786b5b5c77e6407e1 |
| ku9-family.txt | 19453 | 4eb47755e980527946c2d9e313c20348ce96af84e13983ea6fab32cc7e1c0c8f | 481a9223f029d27e2f69ae54a75685960e9bd5de |
| live-family.txt | 19453 | 4eb47755e980527946c2d9e313c20348ce96af84e13983ea6fab32cc7e1c0c8f | 481a9223f029d27e2f69ae54a75685960e9bd5de |
| family.m3u | 36776 | 1a4888e63cdf214e534696bc0ba6b62846591ae3145a8efebd9d473a10c43d56 | 08a37a46a8dcb14157e3e2cce256aff22fc034dc |
| final-publish-report.md | 11054 | 134cc662d8c9e43079ddd923649a2d8e8d645cc97d54c3ebb3abc368b6e61cfe | 6e792d047041237856640d2421741c51f95f4dcc |
| coverage-report.md | 2200 | 5e6e4fbd878df7e1b17b4737d3da99a30148c7487ad46e55b623e38cb56b4676 | cf4b55026a42906c8e113c80be5eb3e63e727f19 |
| quality-audit-report.md | 4689 | da02e6a9fa4f355565d1793708fb595283fecc1b2337c7215b8759477e50f6fc | de69e71aa440ceccb349b8f6e72040ce5afd1ac1 |
| publish-guard-report.md | 1497 | bc5bab96f9a606258dbb0fa02711b2b33f2e8cac03e84fa202ce63f949ba8bc2 | 17582440819ed24762c65b5c9aa2089442b6daa0 |
| published-recheck-report.md | 26396 | 4cf430bde265b333e2ff810025456a4dc4d73327a8164c281f45ca90449a04da | 7fa6585f60ca21203a6dd201e09005a8eb5a7f85 |
| source-report.md | 8047 | 3b6aebd4b7a18be53bae31043f1cd7e462fb1b16921cec9b97f8e9297f9ed1c1 | 5db7d3fd37eda3756d7448b8024a29c17c12c07e |
| check-report.md | 8047 | 3b6aebd4b7a18be53bae31043f1cd7e462fb1b16921cec9b97f8e9297f9ed1c1 | 5db7d3fd37eda3756d7448b8024a29c17c12c07e |
| curated-report.md | 1894 | e6cdd4bad1ff06b055b1d18c1140dbf2ee9bdcb64d34a13f87ae2e3d8cea3bc6 | b93bbf6638ad499197addfde0df382981e873dfc |
| sources_status.csv | 4117 | 9a8814ad8058d1b60590f31ab9714bb36bb1f18d6f858c3583233c5396206e2d | a1464da6551a41263748c0364dae50225bb23d1a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
