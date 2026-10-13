# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 297785
Unique payload blob bytes: 196016
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 70518

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23506 | cf7407634a8fe24d65090c5b259725bd3b80fbc9e538c99de15a7aba00aa8f20 | 3ff8114917669841b55243c6f31a811a55068187 |
| live.txt | 23506 | cf7407634a8fe24d65090c5b259725bd3b80fbc9e538c99de15a7aba00aa8f20 | 3ff8114917669841b55243c6f31a811a55068187 |
| live-verified.txt | 23506 | cf7407634a8fe24d65090c5b259725bd3b80fbc9e538c99de15a7aba00aa8f20 | 3ff8114917669841b55243c6f31a811a55068187 |
| ku9-live.txt | 23506 | cf7407634a8fe24d65090c5b259725bd3b80fbc9e538c99de15a7aba00aa8f20 | 3ff8114917669841b55243c6f31a811a55068187 |
| live.m3u | 44950 | 471ed0e545b602f268a4b06798cddbc337069dc480d2afd34db0cec5b119f14d | ea659005a2018552d429942fbf8ac01d41654d3c |
| ku9-family.txt | 23140 | 91a7b822611feca73970964d9ba6142ca2de2e4599d2cc3195d5361178234b1f | aba729772f2519ec4632a8ca35c98b45d43bf7fc |
| live-family.txt | 23140 | 91a7b822611feca73970964d9ba6142ca2de2e4599d2cc3195d5361178234b1f | aba729772f2519ec4632a8ca35c98b45d43bf7fc |
| family.m3u | 44274 | e152fb28680c94b1806bf1a7c29a27ec2d21ad4903ddc83cb11d3a7a781449e6 | 089e8dbab953e763c48e9048a7fb706d9bcadd55 |
| final-publish-report.md | 10711 | fa286ec53208635120a48acca0cfff099c7a7a76fda271c4125c5a79c3bed6d8 | bc5f89d473dfa6f4b006bb1cbccebc6e5502b470 |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4720 | f0a1cf16857511cad4523099b91da6e92dc6125ecab63faa3e0054a57d133192 | 05349a1cda544afda24b727ef2e95b7e9beb4a53 |
| publish-guard-report.md | 1622 | 5a9019b064a6616a096c10d382dd4015db2195c869d510b4f2dfa428d5c8ed3c | 1c4cf3772a97f059e20886fb9ee70e3c45e2d94f |
| published-recheck-report.md | 26810 | 5e7c793d95c1d7f9d4dd95285a27cc461bc15650bad7e49e5e0a66a9b7513ce3 | 7c9b9803540f710a5e1c862d5149b68ee510a120 |
| source-report.md | 8111 | b260243ae5be9f09f6dcdecd9edf67bca76c345d6095c8413e9b842c63ca06ab | a34cfd076a63797dd2f501942a65a29aad2445f7 |
| check-report.md | 8111 | b260243ae5be9f09f6dcdecd9edf67bca76c345d6095c8413e9b842c63ca06ab | a34cfd076a63797dd2f501942a65a29aad2445f7 |
| curated-report.md | 1804 | 849d5eadbfb78439d8847536e3f5d72ceb2f7027a3a4857fffaef013a20e0f1f | 4fd11efcb32fa45eede85ea6ac912f0e00fe1a3c |
| sources_status.csv | 4138 | 60631b8f99374fc77abc7a41ae033e8563d0e58ae4b27a182c856e0b57daa4f9 | fab0e7a1cee4981003518fb2a1940164a9e6ea22 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
