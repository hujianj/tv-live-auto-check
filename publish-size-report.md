# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 299621
Unique payload blob bytes: 197888
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 70533

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23511 | 7fbb8ab8e5b20c8b9f223609c5d9ae1bf66101a5238a3560efa9ec37d3393362 | 7ee725df66b44f8d50d96394579764a3771a8cc1 |
| live.txt | 23511 | 7fbb8ab8e5b20c8b9f223609c5d9ae1bf66101a5238a3560efa9ec37d3393362 | 7ee725df66b44f8d50d96394579764a3771a8cc1 |
| live-verified.txt | 23511 | 7fbb8ab8e5b20c8b9f223609c5d9ae1bf66101a5238a3560efa9ec37d3393362 | 7ee725df66b44f8d50d96394579764a3771a8cc1 |
| ku9-live.txt | 23511 | 7fbb8ab8e5b20c8b9f223609c5d9ae1bf66101a5238a3560efa9ec37d3393362 | 7ee725df66b44f8d50d96394579764a3771a8cc1 |
| live.m3u | 45029 | b6bf932a7a7d17175637ef4e5d838a1eb0e05669d97a29bead4815a4f06327a2 | c98f390ff0498aae41a9aceb0e9598689ceecf89 |
| ku9-family.txt | 23082 | 26b445df01f5a4dc7712c476631516d693bf08a847b6f93bc167110edfc96396 | 9b25343d612f9716b71d08feef78193797a9f82b |
| live-family.txt | 23082 | 26b445df01f5a4dc7712c476631516d693bf08a847b6f93bc167110edfc96396 | 9b25343d612f9716b71d08feef78193797a9f82b |
| family.m3u | 44228 | 8a057864e3cd39ba0a8e8c1c756437db73591450f23954a3fcb074e6aa9e5938 | 7dce2fc483406f8a7117172eb5fb336cb518b668 |
| final-publish-report.md | 10800 | f53e43e88517f6630a19bdfb123680d3cb58925f013f1f1b308c0abd0e400fbb | c57ae0ec744a6832e7f419d2945481bd9cdac1d7 |
| coverage-report.md | 2230 | 836134b694bdd788ec4155175feecf7efe41b11a0edb9e318f7b029b9d75f9f2 | 20cfb2d6dd18c2685d1bf1a2398a6eeb9e178f3f |
| quality-audit-report.md | 4733 | 2c9e733190d5e38e58e7eaa1a8a30274201b559f4dbed2be113b92f80e8f8dba | 3f0707e3da091047e638534aa2e8f4458e9b8fa7 |
| publish-guard-report.md | 1612 | 9efa810906b0de4e25c14f9fee2f206995fc0103094f706c07bbefed2b5f24d3 | 9f79b1aa786d75dc37c71f809bdf35377964e50c |
| published-recheck-report.md | 28603 | 17b7767074fe02be6d1772f2437515bf4c83a068d6ec243cfead143b82ad7882 | 851885a31f4046099f2b8c364c54141382af6a4d |
| source-report.md | 8118 | 6aed79688e2515cbaaf291bfa4c17764e6c9a01d078aac81860ac585aad521bb | 5c15086c03cdcf344a0de3d57f86ba94d5f31a64 |
| check-report.md | 8118 | 6aed79688e2515cbaaf291bfa4c17764e6c9a01d078aac81860ac585aad521bb | 5c15086c03cdcf344a0de3d57f86ba94d5f31a64 |
| curated-report.md | 1804 | ecad9ba9416c4b5de07e7074eee464e730868c71909dc09906362e36e8fe6635 | 05415a4d818c97ec62e0871ab423f3a759337e33 |
| sources_status.csv | 4138 | e2b5e4fda3875d62df4b6a7be14df7ecee2eb099df397b80ab10ae6ba2f015fe | 769adeefc4e9e3e8866042cfae732d4f8532550f |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
