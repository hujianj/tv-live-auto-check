# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2138816
Unique payload blob bytes: 1536694
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 505665

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 168555 | ad5af21ae7f27fa089f6171e3f3212cdb313aa201daa6f53544f48427ef6cbae | c24cdde66a741fd4f3a442b30886e7dc2ffc7ed0 |
| live.txt | 168555 | ad5af21ae7f27fa089f6171e3f3212cdb313aa201daa6f53544f48427ef6cbae | c24cdde66a741fd4f3a442b30886e7dc2ffc7ed0 |
| live-verified.txt | 168555 | ad5af21ae7f27fa089f6171e3f3212cdb313aa201daa6f53544f48427ef6cbae | c24cdde66a741fd4f3a442b30886e7dc2ffc7ed0 |
| ku9-live.txt | 168555 | ad5af21ae7f27fa089f6171e3f3212cdb313aa201daa6f53544f48427ef6cbae | c24cdde66a741fd4f3a442b30886e7dc2ffc7ed0 |
| live.m3u | 302943 | d217e6a79fdedf6a5e57465666da6b2fbe3da4f8711e1a2ecacafab51f0e1b8f | 9a0d99046e91842e5c4fa546f6710273510509dd |
| ku9-family.txt | 89886 | 428c9ab8b18b73df8b2882b36b3c962fdd2016c24cb61b2834f3adf4bebd4c83 | e4373ba61a40c3563b969f18e113ca5f06533f8b |
| live-family.txt | 89886 | 428c9ab8b18b73df8b2882b36b3c962fdd2016c24cb61b2834f3adf4bebd4c83 | e4373ba61a40c3563b969f18e113ca5f06533f8b |
| family.m3u | 160645 | fa4c052eb3785a68c8ed67d414f3b77316e9ddc00712a4192e125852bf6bca52 | 7e3087a0752404e0653c108ec63d9c3d398fe918 |
| stability-history.tsv | 747661 | 3457948cfb77706746a9ecce8f2bee52d9f3f21f5f7673daf765a823bd2f8f74 | 56fe81e7d8b150072fb20b6ed2654f1d53cf966f |
| final-publish-report.md | 11686 | 1c36e2b4df4a2091fa7f6766e4bc17c6fda2cdffb4ce0d169f911e42eaae8dfe | 57f0bc38e77aeaf559522a94b2aaaaca272f7bd5 |
| stability-report.md | 10980 | 4d8d74bb79f90d9b5fc1cd10f61b195e8804667803171f7fc9feeb739334e9c4 | a2b0983b2ce754b00b259782d6a7d89eb711e380 |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2065 | 941640ef9253215095e392b69aa2be31afd77d97917fc312759b23426ba28e2a | e48e5c4913319de6cec7b3c6f66e9e3f541011fb |
| publish-guard-report.md | 1153 | 59928c574910843b6e261086148c4aff03db0d50240f193e1dffea2c8af2364e | 4c2e46d5592873857feb4163b852f1368c0123bb |
| published-recheck-report.md | 26809 | aa7ffb23b4ad331d7deb1b70266a9d383b31529d81c3d2800b2d7a2d10dc54f6 | b198a60f6ec281fdfb98b3bd0f9959f7a5472367 |
| source-report.md | 6571 | fad19e631e70bd5983bb769dde5523768daaebcdcbfc35482660bcaeec55e0dc | d2a64600c9f55416f275d89023d1b109f23eeece |
| check-report.md | 6571 | fad19e631e70bd5983bb769dde5523768daaebcdcbfc35482660bcaeec55e0dc | d2a64600c9f55416f275d89023d1b109f23eeece |
| curated-report.md | 3310 | d8d078661474bfd47669c185ef588bb24a75ee8497c7e403224f7145304df082 | 2f10e2097395943278cfd05d11ae5273891231e2 |
| sources_status.csv | 3139 | b314d7afd063fbe05b756e57b067dc1474c90a21b2bf1e9d2c32241fc22a8a08 | c5118b16974c29d693dad73a8c766f341170c1db |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
