# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 343753
Unique payload blob bytes: 277644
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38916

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19458 | 749cbf1353a7b3ac83cf7697397d12799299b20fe1c87b9c1527fddcac665039 | 54f69a8c6d62308569f32117df64f133f31768b3 |
| live.txt | 19458 | 749cbf1353a7b3ac83cf7697397d12799299b20fe1c87b9c1527fddcac665039 | 54f69a8c6d62308569f32117df64f133f31768b3 |
| live-verified.txt | 19458 | 749cbf1353a7b3ac83cf7697397d12799299b20fe1c87b9c1527fddcac665039 | 54f69a8c6d62308569f32117df64f133f31768b3 |
| ku9-live.txt | 22960 | f949af9969d2bac3c4e13e1d2cbae26f9733b628e93ad2ed9af99312ca5c4e24 | 39f54376cd15fcfe5248871de1f650aae3137c66 |
| live.m3u | 37188 | f3e7ce2a2b1bccebfc816a35bdee62fc5f14d6ab11342480941811fda6c8a943 | 59155b8b3dda6bde78cd9096e1788d7af7cc5d4a |
| ku9-family.txt | 19022 | 6f7953a3280cea6c05aaa148ec811aaf379369f9727ccd12397e8634582cfebf | b45a7d175f788fedaa1000a7df504216c53dad29 |
| live-family.txt | 19022 | 6f7953a3280cea6c05aaa148ec811aaf379369f9727ccd12397e8634582cfebf | b45a7d175f788fedaa1000a7df504216c53dad29 |
| family.m3u | 36380 | 6cdbbc9ca87ce0b6954d47adfb45b39fe385e867b56cd6d30b02d9c45f41d693 | dc1a2089d41db9e6b3c7212eff99d7fc5758fd7d |
| final-publish-report.md | 10944 | caa594fcac21ef141dfe59894aa6d348688a13243d0fa48ac1619ada33193c3b | f7c28df2cd11122dfcfd01cf3fd3698a097d3cc7 |
| coverage-report.md | 2195 | 65153cf9b46ae5344e9e38f3e812bd27c9ba4ee3705e4f0b8692baeb5add3715 | d1a1bcad7034252301f1ceb2713c9d0d248000d4 |
| quality-audit-report.md | 4681 | 90476564b2d8b2f2435f16dfb58cfefad300371b7f1fc91c65e6fd2f9e10e419 | 4b33511df55498df7a66f0600a235eb24d68adac |
| publish-guard-report.md | 1531 | 4de55802e42c068889bb31a16c4f9cc56d70018e4022363cf065710a137538fb | 3958eee56a0bfc265cf825fe3157e87f1dd2e64b |
| published-recheck-report.md | 30645 | 59d743f8512d4d62b7f905f02b719692a8b01cf8459acaa2501f5d979b24ceba | b00fc7d328d2e8f317797b59fd3a244a55153dfe |
| source-report.md | 8171 | a54ef9eeb9817377f8ff7c92a52bf293dfcd15ee642d426eebc4d79aff5c9ea9 | 9f481b0b99a04fab006ee85d5eb49b3c17c9448f |
| check-report.md | 8171 | a54ef9eeb9817377f8ff7c92a52bf293dfcd15ee642d426eebc4d79aff5c9ea9 | 9f481b0b99a04fab006ee85d5eb49b3c17c9448f |
| curated-report.md | 1834 | 0996608b16e1b19e3c0d2bb1577304835b3dddef096c7648748a9bc9d717c75c | 67dbd1cd61245455dca96303e229e767c3311c57 |
| sources_status.csv | 4241 | 9fa893e6fdc3add8ae4ea2f9cd430c5b94aac1ed193c7f49d801ac977c58dab6 | 7f24fffb5e71fe223d02eeca34d8faf8e27c4d2c |
| tv-coverage.m3u | 51653 | c053ad3c94d769bd8a82bdb8a0c35498238a2989598043b46016bd1fffe6efb1 | a66f6b13926d46be9554bb6a359ca73ac7e7732e |
| tv-review-report.json | 16948 | 90bcaf80ebcf031d32a27e39c55891460bfb1f04c4f6e873fd2e1e7d76a3def6 | a1eeebcf55ece251febe8a7824252e2882a18ea9 |
| tv-review-report.md | 9793 | 94031b527b50240883f04daa3db74d8e3c805a33be24f81469d7f20315bd6be9 | 2675159d071b5416ab33ef68bdc7076bfdf11214 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
