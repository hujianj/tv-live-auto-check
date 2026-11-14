# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 329461
Unique payload blob bytes: 266633
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36736

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18368 | c1d90217537fb08a92cb3ec0ed19355d1634b13f1b97b5400825e0fe12d2c9d2 | 84ea8937b463892c0fd01df1544e791b4be5b6b2 |
| live.txt | 18368 | c1d90217537fb08a92cb3ec0ed19355d1634b13f1b97b5400825e0fe12d2c9d2 | 84ea8937b463892c0fd01df1544e791b4be5b6b2 |
| live-verified.txt | 18368 | c1d90217537fb08a92cb3ec0ed19355d1634b13f1b97b5400825e0fe12d2c9d2 | 84ea8937b463892c0fd01df1544e791b4be5b6b2 |
| ku9-live.txt | 21955 | d5b5c915fbec72c00e4292a6f5fdc02ee03ebcc302f8c5c797414ae299df6499 | 7c08e5747a967da369fc135b1b788246c94914b7 |
| live.m3u | 35113 | 204cd0639656129a66b0fbc6be47f20c8129c2723e4ad98c6f0c231fd63d6d57 | 1ae77bf29c153404341a1c00ea82c9f4ddf6272d |
| ku9-family.txt | 17932 | d50695594210f3fb6082469f91d6c3461a6c17e0016f58ec537c5853588b1820 | e8aee70112ea84602a0fe588a978d0fa2d264426 |
| live-family.txt | 17932 | d50695594210f3fb6082469f91d6c3461a6c17e0016f58ec537c5853588b1820 | e8aee70112ea84602a0fe588a978d0fa2d264426 |
| family.m3u | 34305 | 2e2ed4dac29f482653e52bd80f138da11e63973d43e3920cab80b355108b7cae | 6c6b6ac27dfb7082775171f642b058e82df7a309 |
| final-publish-report.md | 11469 | 459a954649aecf01296f732488bfe4ea4fdd98462eda535c0cf0144d0a3e85b6 | 5bfcaf20f231730cf2b46fb57c3a1197013f47f9 |
| coverage-report.md | 2200 | cd4b1c654690cecc683e26d576a1317b8722f6ac4925bb99230c3d329daaedf4 | 74dc38c90f8cf7d1400c4701d8a22bbe6ca00d8f |
| quality-audit-report.md | 4719 | 62080492a8d1879e9dbc196dd7e5468d5ef94e20ad2c7a1f74bb8d3faca9e36e | 3e0632534561f1850dfe37f2c6f765be5d0df922 |
| publish-guard-report.md | 1584 | 40c82f36ea3b6bc21d69534549f17e0494a1e280692fe04248d1569caf9aef03 | 0863ec91cd6c3e19bd5d9fe0f60d022ee87ca1ec |
| published-recheck-report.md | 28385 | b38f35f53af8241ffe113becb1d5cbfb76acffd7646d3923eb92473a0fffc2d9 | dc0be9e4d22ce58556bb6dffbd8f1701b2bc625c |
| source-report.md | 8160 | 30d667d192c0b1f667075c33c7555c06ff94d6d1cc377dfdf1e9dfd48f401765 | c0f8f3125c1a9dd9904274c18c5d1554a71d3a94 |
| check-report.md | 8160 | 30d667d192c0b1f667075c33c7555c06ff94d6d1cc377dfdf1e9dfd48f401765 | c0f8f3125c1a9dd9904274c18c5d1554a71d3a94 |
| curated-report.md | 1833 | e6c6ef8426d18f2230033ad6a079f0ce36180a9c89e7f204929949a84c5575f9 | 8fc2c3344edcfbf7b9d7d30ca1d01f1cd665acda |
| sources_status.csv | 4241 | e89c338ff14a73166bcbd3ffea7757d0a857cfa776494bd348af1662c6a14aed | da1e3b99e7c46aaea47b220db0f1cd2e30a3cba3 |
| tv-coverage.m3u | 49428 | e865c41d027d0c0246d0df640d512ec3a592da00c7a11919a885eb10d171b5ed | f59d1e58041f9ec19eb891b0962f3ce85dd8ea43 |
| tv-review-report.json | 17243 | 5969cd5e5d733a95539fd34d295764b9a96f74d15a7fd6e03f8574647f763f3a | 080083390ae5e42f17ff5c4799057245dbb18cae |
| tv-review-report.md | 9698 | 4e0c1a88e7fb26ceb0603859cb205c257eaaf28cff1c69feadf224a23ed4bf3f | 18cf22af27c5bbcd8a5c606694503ab575c5a7dd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
