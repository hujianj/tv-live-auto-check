# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 344229
Unique payload blob bytes: 279052
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38334

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19167 | 1557c40d6bf6ac676c9178bd959146d27a3270251565a42ae844e5a52783a65b | e9d2ac1210c391062ed5838d4eebc8afbaf32709 |
| live.txt | 19167 | 1557c40d6bf6ac676c9178bd959146d27a3270251565a42ae844e5a52783a65b | e9d2ac1210c391062ed5838d4eebc8afbaf32709 |
| live-verified.txt | 19167 | 1557c40d6bf6ac676c9178bd959146d27a3270251565a42ae844e5a52783a65b | e9d2ac1210c391062ed5838d4eebc8afbaf32709 |
| ku9-live.txt | 22971 | 87bacd53a21bf9eb0b08185269ad9c9037c20f28ab0305850d6f8c6a43cece76 | 8befeed9582a8bb02641db0060abcb4a8fe8596f |
| live.m3u | 36826 | 190819fcae9363bbaf539632322c5a368b3d5413ebd188665228bb3fbebffed9 | c451505e883dcb96ba53888fe20aaa5d464d8e5d |
| ku9-family.txt | 18731 | 4ada56013e15ec59062c27eacf81848c82633af8d0ff28fec423ba42d394ccbe | 453dc1a362f19e0fb85e363ca72912becc4b5e04 |
| live-family.txt | 18731 | 4ada56013e15ec59062c27eacf81848c82633af8d0ff28fec423ba42d394ccbe | 453dc1a362f19e0fb85e363ca72912becc4b5e04 |
| family.m3u | 36018 | 36571856f67edc42877c9b7790f84c18475401775004cb317579b9912b6f9998 | be8cc5eab32bd8c5d49d0e182d84fa56056a06c6 |
| final-publish-report.md | 10923 | 993772cd82c86cd495d21e27c4879048a6235badb800993b589795fddbf2e8fb | f0ab92baf1b8b945f39a841aaa71f11c6e7e7219 |
| coverage-report.md | 2200 | 344e6a2a3904788053d9bc815726eafae1ecd98f4959e29e307eb6c9da0b8ca9 | 4762c19e29c923083a1b15a29f7dbb096c48ec58 |
| quality-audit-report.md | 4709 | 044c6284a201be7810b654a98cdc2053df2964c88f7bb30faf8a1e8d4895d2a0 | 47df086820e6699902f3a8c2999e7b6064acb1dc |
| publish-guard-report.md | 1508 | 28e41a9144c7cc3e673d206a33ec44a1836330f6bb2ef7fb56c3f4d99932b3d4 | 390adefaa812aa841eea46e5fed00e93b766c76a |
| published-recheck-report.md | 30324 | 0a16d2f779cdc4d63b69153b765d83b086fc3f707a5d447811b5e5102a3f354c | 89c06aa4a63965bc792d6d6d9ce923009b69fc32 |
| source-report.md | 8112 | 0697e0482f89b4897c76ad21583ad702da593b0d6ae7051cb686ab417098b29a | 0c4cab4750084cea4d8fe27b40eab64bd9861d30 |
| check-report.md | 8112 | 0697e0482f89b4897c76ad21583ad702da593b0d6ae7051cb686ab417098b29a | 0c4cab4750084cea4d8fe27b40eab64bd9861d30 |
| curated-report.md | 1834 | 04c4026267dd535735c623ebf1a3eaa1de56cd580442fa177b673ccfce80bb12 | 473eb5a6ade81d1908f6c49bdb54e1486ec51e26 |
| sources_status.csv | 4181 | d7b0f855d299528c548de0c4bc9d6771549ce3c58172348f20725700b53d024e | 218adfbdc339f1939634855d67fe541ab8ce776a |
| tv-coverage.m3u | 51953 | 1f4279df0404fdd9158d6cfcaec0c1485bf10a9171789ff1d9a906294497f60e | 0b7fa46498925372c2886a64ca7a4b8995192cfa |
| tv-review-report.json | 18765 | 76aecd346e91649c9d2be6c587668fce3bfb41f7e7e82fad717229e903e892d8 | 0eb294521d3c1cb6beb5860e49011031d8b2d463 |
| tv-review-report.md | 10830 | 1727e55071c78157ba348aee4cb944d0223f1c4cbfeb0ea30be8d21b25dd4ef1 | d535939e4d040aa0331b4f9e680395a2550a6aad |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
