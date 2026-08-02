# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2485713
Unique payload blob bytes: 1721208
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 662256

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 220752 | 85b0c03b1fc1086b11af98d94418d4776af0a305f51ea58967c268b0dc46f8b3 | ddc8c4b59d68814c4bf67172d2f78c90bbb5a57a |
| live.txt | 220752 | 85b0c03b1fc1086b11af98d94418d4776af0a305f51ea58967c268b0dc46f8b3 | ddc8c4b59d68814c4bf67172d2f78c90bbb5a57a |
| live-verified.txt | 220752 | 85b0c03b1fc1086b11af98d94418d4776af0a305f51ea58967c268b0dc46f8b3 | ddc8c4b59d68814c4bf67172d2f78c90bbb5a57a |
| ku9-live.txt | 220752 | 85b0c03b1fc1086b11af98d94418d4776af0a305f51ea58967c268b0dc46f8b3 | ddc8c4b59d68814c4bf67172d2f78c90bbb5a57a |
| live.m3u | 396554 | c7ddb9807e18494f201af0f14cf2b7eac9f057a0517a2c437054787efc5516f0 | d20bf4db81fd80af1172eb9e1fecf9e31b1a5893 |
| ku9-family.txt | 96436 | 31dfbf9cbfd03b32a0f2313fcf34fe375c20d72cc4ca359de6730cf8426dbfc9 | 9eae891bcad31e6323184777f54000858cf6e004 |
| live-family.txt | 96436 | 31dfbf9cbfd03b32a0f2313fcf34fe375c20d72cc4ca359de6730cf8426dbfc9 | 9eae891bcad31e6323184777f54000858cf6e004 |
| family.m3u | 175597 | 0a14b4a8be70e00bb2c3fbd8679de53c1217f0fcbb4f9d8f93bd279a01c728d1 | 88aaab35c85c5b82e40ad123b3d3939dce41e025 |
| stability-history.tsv | 763253 | ecf2f0ed3b7056a6041c81f787a66de4b6f3f3be1ea4b6ff537f55a36e915b94 | cda663e08d67047d0a813a9274ed233ce0ab819d |
| final-publish-report.md | 11501 | 890246f8fcc532b76e24e7996365678bd33ff08f5ecdac6f80244c8f4f3cd21f | 4531134f4595b42a3a6679cca1b495511f28037f |
| stability-report.md | 12888 | 04f234cd4ef87dad9c435cc2969ed43d58a7408b207ec84c4a0c5084d9b08b4f | 91cb85bd538515e8e74afc3153083264def602e5 |
| coverage-report.md | 1329 | ec04aa9ffabf026f295c1be58e8515c57433989330f6a5bba2e1d2894ed02daa | 277eca8fd7576addd6a5eb4f5dda1bc622b7a325 |
| quality-audit-report.md | 1504 | 11d0ae8076ca37bbb451e6c6922576497260a43b52405f03b7839f734763dfdb | d73cc219702a007e6c8b844e21b1598e5c42b6c4 |
| publish-guard-report.md | 786 | 24a6933e86f45d0424ee60492edf1d27613618449ede308e93000d48774edfb2 | fd28da1bb862be92c724003e93460f8974c79b7a |
| published-recheck-report.md | 28631 | 3c3133db1ee125a4c399ebce57f5d1533747ef99c152beaef2a52951ff161c71 | a5d8a36a5bd40cdf309b0b2c1dbd87434620747e |
| source-report.md | 5813 | c2e7d961698b107620704c2e663ea00ec9e1ffd8c3196a56d3eb6d8620543017 | f56e62f5ac46cb671a9aaf0541d045c8d4898ba5 |
| check-report.md | 5813 | c2e7d961698b107620704c2e663ea00ec9e1ffd8c3196a56d3eb6d8620543017 | f56e62f5ac46cb671a9aaf0541d045c8d4898ba5 |
| curated-report.md | 3565 | ed9a029143ed256141adb6d225149400aca3e674cec0b94fd46461a16329ca61 | 7ae98d44e034efa9a927cbefa1d1e7d6e653f3b5 |
| sources_status.csv | 2599 | 438350f65c2df65492d2505a8e9c2b405728da7528eb0af45b4269d1186accc1 | 9e3936ecc9a63c3c0cf2edaa09d55f314546f008 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
