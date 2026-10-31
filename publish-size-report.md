# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 373847
Unique payload blob bytes: 300784
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 43592

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21796 | 2b3c1f3d27a0fad0159df7fbf2c5f1a899bdb59d9d1d9e898f4351d196dff0cc | 5051968becbf76d0b50d2c37885cad6700964f67 |
| live.txt | 21796 | 2b3c1f3d27a0fad0159df7fbf2c5f1a899bdb59d9d1d9e898f4351d196dff0cc | 5051968becbf76d0b50d2c37885cad6700964f67 |
| live-verified.txt | 21796 | 2b3c1f3d27a0fad0159df7fbf2c5f1a899bdb59d9d1d9e898f4351d196dff0cc | 5051968becbf76d0b50d2c37885cad6700964f67 |
| ku9-live.txt | 25673 | 73167b6ded908639eae202eca229e7108a4648088d8f24d8a6b20605c2c2c825 | 3907b6d337e5bc8521ce041b13065671950091c0 |
| live.m3u | 41093 | e00aa39bdb235bd9a5bbd265b13df08ecdfe37e0b47d99135d76d77ef9c37ae9 | 99dfab2f4b78c69fcf1c85bcc42b6abe318a0941 |
| ku9-family.txt | 21360 | 779350829230d6e4e6c7e545e97006dcbc68f799b6024930d6533e6517a0c0ec | 5ebfeaa259c0cd6a68ded66f206908ba05c0c490 |
| live-family.txt | 21360 | 779350829230d6e4e6c7e545e97006dcbc68f799b6024930d6533e6517a0c0ec | 5ebfeaa259c0cd6a68ded66f206908ba05c0c490 |
| family.m3u | 40285 | 63417d348c2b26f08e8b9cc64e25ed8ed2f1ba8c4dcbab3673d0e9de3aa3c74a | 8f3265e76353fbbeda156c06b91aef4ecbf98709 |
| final-publish-report.md | 11106 | 7ad30ebe6f22a718dee101f8becd805355cc9c43a20483fea0809989280edfb3 | 7320e66f9cc44d942f9e1c596f9250bb3883cbe9 |
| coverage-report.md | 2205 | 60ea0197dc57c188469726bfcfd420060974843f22866ceb424921d8e6bda0dc | 594b93b87e7d88f9e7783ec54e2591ccab4ef1f2 |
| quality-audit-report.md | 4688 | defed9ce50569edbc863857f985a77ea736e19c0dbcbbcac168ffed93f5c5a45 | 453677c9c1c27091a62035304bdba816cce37a7d |
| publish-guard-report.md | 1530 | a546a6385b5529c736c59894b3981db8488dd99b520297acd95ce9eb9fc44a8b | a96dc2c6c26dd6ed6f9b0c0542e50aaff93bd5dc |
| published-recheck-report.md | 30617 | 6c8a0ec39cff988ffae483e09c8cc6c63052095bb28caf32bbf70666d544951b | 24b5616def8b170d86f56019cc22c7cfd6a2bb2c |
| source-report.md | 8111 | 8838379357454fdf6a2eafdb2d7941dfb24b373b88a4558e90fcefdcc0522c11 | 0859b5df26ccf9381b0d06bb97f1e89e5eb5b4b2 |
| check-report.md | 8111 | 8838379357454fdf6a2eafdb2d7941dfb24b373b88a4558e90fcefdcc0522c11 | 0859b5df26ccf9381b0d06bb97f1e89e5eb5b4b2 |
| curated-report.md | 1896 | 57a67eb659f6cffb532e4cc5f25537f771595da1c858502797cef63e8862742e | 064719626a828f24ebc4b654fd4d88571650c27c |
| sources_status.csv | 4182 | 7ddfe703c7a9ec1997b9e13205888487c87630e9ed6c0b440847ce7423910f43 | 2ac19f44536477e9e42b025aa11529d5ae7d9d43 |
| tv-coverage.m3u | 56715 | b86581f0b30f7511ae857ae86f0fac9a7a3a0497c94e6aa04bfe1b8d57faae4c | ad026fe31d7de679efd3303fe1330bf9ba1c08d9 |
| tv-review-report.json | 18731 | 8f729c6a1cdf7b785fa8c3fe9d91aec9d57e609aa3c385960aec6bde85892f8e | 25a09494eec1d699863622058c1a0bd5817c2b63 |
| tv-review-report.md | 10796 | e825fb9d0de012f5905418dc68dd343885f0eb789ba7696c8aa0041adc3f0d05 | f458bf32fddf17b5040c37e5cbb7882265164878 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
