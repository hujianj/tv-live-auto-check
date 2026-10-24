# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 295232
Unique payload blob bytes: 195075
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 69429

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23143 | 0d2b083832091a9c2886e74041fb713117493ca463b638b112292d2f6cdea5be | 30dcfe8883d2da48f87fcd006b7040363809c822 |
| live.txt | 23143 | 0d2b083832091a9c2886e74041fb713117493ca463b638b112292d2f6cdea5be | 30dcfe8883d2da48f87fcd006b7040363809c822 |
| live-verified.txt | 23143 | 0d2b083832091a9c2886e74041fb713117493ca463b638b112292d2f6cdea5be | 30dcfe8883d2da48f87fcd006b7040363809c822 |
| ku9-live.txt | 23143 | 0d2b083832091a9c2886e74041fb713117493ca463b638b112292d2f6cdea5be | 30dcfe8883d2da48f87fcd006b7040363809c822 |
| live.m3u | 44175 | 1af65c5520531eed2030cda63f8048e6be8d14475284084a311675c6a5debec0 | 607f09f2c7ef966db3c6147bf6a38cdefb3f5d63 |
| ku9-family.txt | 22720 | 2db698db4be3f9db48e17c2096a6753bbba5c07cead909dbbc2e1cdfb11fcb7a | 82cb78a2ae380c168599ac023bc65381aabb1a06 |
| live-family.txt | 22720 | 2db698db4be3f9db48e17c2096a6753bbba5c07cead909dbbc2e1cdfb11fcb7a | 82cb78a2ae380c168599ac023bc65381aabb1a06 |
| family.m3u | 43380 | e610559df3e4d85e9237adb0d6c4316eb78705b3d78515f7ff3c36e600d0a4c7 | 0e72bb5438d5c84138844aa31bf9ea2d4b659606 |
| final-publish-report.md | 10824 | 8dafe2a68c551817502d166788bac8b1834d5b487d9adaef90bfb5c5594dc838 | 610dbd9602b749071b261110a23d2a526535a03f |
| coverage-report.md | 2240 | 30411c9e7c49e92b05374bbd9820e4a9ef3dc4fb14949e62ac2f356ae811a823 | e813c3ff3a911e0420245843e8fbbe5647949fad |
| quality-audit-report.md | 4731 | f2a3fcde2c0bdec2bc86a1a98b6076fd44b2154e9ebf8e6e3eb7adaacd1e0053 | 3fa5225cd22571cd7513211b1840be6da74ed2f1 |
| publish-guard-report.md | 1587 | d820005897533515a80cd60d34d299814d8ac13c903aff4d651ca4ee48e3a17d | 25ba94e2df746dd7260a7b4b31a80d672e0da883 |
| published-recheck-report.md | 28408 | d3d3d5f59cf1eafb7f051a166a54354d82a00f55a3f7df1800f2450f7db68916 | 1cf9020b7dbb754612e0bd425f4be8015e182b0f |
| source-report.md | 8008 | 251adbc26f22b0de2653e61e53b238e5dc46390f24653873aaadd1e55f26bec1 | 38aaa573e2f5e36de71d7ce5867561120aad5d99 |
| check-report.md | 8008 | 251adbc26f22b0de2653e61e53b238e5dc46390f24653873aaadd1e55f26bec1 | 38aaa573e2f5e36de71d7ce5867561120aad5d99 |
| curated-report.md | 1806 | b2070b89b44a8cd96dd865298043a16ddaaf6b15290b44448440567a3ee7f9c0 | 8d5f43f3481824c79baa00b309156e5c830cb9b1 |
| sources_status.csv | 4053 | 110fc91296553872af855f51cef9dfdf8c0e7041655b815d511b02cc38ad027e | 7a74770c88a6e7f8f927485035a7f59de911fe4a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
