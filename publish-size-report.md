# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 329283
Unique payload blob bytes: 263825
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38506

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19253 | 69400078ec3bf08751dfae8b2c139ecc740174db72162779c2ded285df3c986d | cdda0c47eedf023a2ff5aa7c26cc11170901893e |
| live.txt | 19253 | 69400078ec3bf08751dfae8b2c139ecc740174db72162779c2ded285df3c986d | cdda0c47eedf023a2ff5aa7c26cc11170901893e |
| live-verified.txt | 19253 | 69400078ec3bf08751dfae8b2c139ecc740174db72162779c2ded285df3c986d | cdda0c47eedf023a2ff5aa7c26cc11170901893e |
| ku9-live.txt | 21906 | d9f0f509d54a01eef2ec5d62fd98f0e16403287709f50c4e76d6adb4637d29a6 | cbe0878495dcc7f1c6edd3dea44b84c14f5f3e55 |
| live.m3u | 36371 | 855b02a09a46a678a74c883bc1afb7a36c88f6b24d7c226cdde21dc412266c26 | 4aacf2895866bf55a3d1891b2f426370f382dca3 |
| ku9-family.txt | 18818 | 4236ae1b4f37f1cb092dfb42973ebb623d35b3e44e72bd079a74508f7f8a88a9 | 961fa64d18b49dd606fd945963a340c9755874e4 |
| live-family.txt | 18818 | 4236ae1b4f37f1cb092dfb42973ebb623d35b3e44e72bd079a74508f7f8a88a9 | 961fa64d18b49dd606fd945963a340c9755874e4 |
| family.m3u | 35564 | d4b7b73a24920e859a9623622c4bcbff8019af86a819b8acc92a8544892188a5 | 64bddb15101d53fba3afe12323372733113b68af |
| final-publish-report.md | 11134 | 6f6eb0161d3d937562c6f46cc6fcf1d0f5b5f9097d163a042c73fe018b5369f5 | c53b21b5c83a748493593999092fd524b8256590 |
| coverage-report.md | 2200 | 2e85793357af3774a0b2dc7d748b2f16f99e512166683ae35f086c8d2766734c | 9b3d4161aace54de3ab01e75a57768ce2e087c0a |
| quality-audit-report.md | 4710 | 9a455dd052adb34cadce024ba9b56c1cc1ff9db658931479b69f261182dc13a8 | 5b2b5c75e539014233576954db7b9de55dc497d5 |
| publish-guard-report.md | 1524 | be8d184499c371e5eb7fe1aac736d9c83aa4b3b8499899b3644bef897e73b429 | 3e278d648ad2f3c05e37a2205f9d720639bfa272 |
| published-recheck-report.md | 27253 | 43b604ed66baccfda9b933cc25dfa70cefa7d2bea9b49292d5fdf2382981d750 | 470386cb00478ad6b7ccc00a8c7ea4138f9c0c96 |
| source-report.md | 8134 | df4753f4699af38bcc88c8565d98e144b102f7e0fab43aa4976f20e770d8b60b | db9ad5c459bdca6ca9ee0995360bf387eb8abde5 |
| check-report.md | 8134 | df4753f4699af38bcc88c8565d98e144b102f7e0fab43aa4976f20e770d8b60b | db9ad5c459bdca6ca9ee0995360bf387eb8abde5 |
| curated-report.md | 1896 | efc3dc9bcb80de874e6d38f5ca0ebe7bb88b02173959894ec6b4d2ef1cf8e141 | e3eac4cfd9722411656f11678911249ac7af6fa5 |
| sources_status.csv | 4176 | cf9e36cf7715d0193a5e50c2634cfb49f96d972635f674d0f76eca02dadc9739 | 1e873fe9f0928e5dc1b96be0ceb2fcff7f3ad27b |
| tv-coverage.m3u | 49109 | 9361a0b07f26f2d011c0847d615acff24012ce692526329b19155d5c43079aa2 | 89759780bcc41032b77bd90888fcbde00eb5a640 |
| tv-review-report.json | 14076 | 639ca66f7662527b41f34ba8a0548b62d7c7e739fb0926fa968ba6b06f67c6bb | c1e4e52e474f86ef6af9666bbac9b8050797743a |
| tv-review-report.md | 7701 | 6df07fa05e5f300a0e34c2703d7d43f4d5ef24b6ca0ef55bd0e909f83a36b836 | c6091c31301bd0a4217b4642a9d84d66743a13c7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
