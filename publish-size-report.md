# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 320640
Unique payload blob bytes: 257960
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36720

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18360 | 14eb42d36ffae3bf6330ca91c27609079bf1c7e737ea8707fda29abc6df0d82f | 6b21beed442b4e52bbc56a0e9e019c39fa4c1ab1 |
| live.txt | 18360 | 14eb42d36ffae3bf6330ca91c27609079bf1c7e737ea8707fda29abc6df0d82f | 6b21beed442b4e52bbc56a0e9e019c39fa4c1ab1 |
| live-verified.txt | 18360 | 14eb42d36ffae3bf6330ca91c27609079bf1c7e737ea8707fda29abc6df0d82f | 6b21beed442b4e52bbc56a0e9e019c39fa4c1ab1 |
| ku9-live.txt | 20919 | 371bfaf875ce4c9f0b8098b444369e6d42bf3c05be5a9a2ee0c853d3aa1977c1 | 7011b07728eaafc0dfd5c42fa8e74de4fcbc1050 |
| live.m3u | 35314 | 867254476d801bf6508255a891781905e1774a0534d353a9a506f728613f57a8 | 6819e978aaafa973f9ffccf3535a00acc251ff6c |
| ku9-family.txt | 17924 | d2839008e0a1c7443cbfbf5f2dc1b3cd48373e40bdcdbb928408f0cf8a58a32b | 59ecdcf676eeadbda123d6ab43e9b21c23dc7e2d |
| live-family.txt | 17924 | d2839008e0a1c7443cbfbf5f2dc1b3cd48373e40bdcdbb928408f0cf8a58a32b | 59ecdcf676eeadbda123d6ab43e9b21c23dc7e2d |
| family.m3u | 34506 | b8bce2928f68a57191b1b5540d85a9c13f6a51d28c874dab697a0e3568937c88 | 8d557925f95c513fc06f21c43e299b562db9d067 |
| final-publish-report.md | 10918 | 2bbf64e2cb7efcfca0c79171a499d5f91a086b77995f349a2d4e30247f6cb3df | becab466d2df21bce3296663c53d05976c3d064f |
| coverage-report.md | 2200 | 3ae7616731b2183c1dec1984ca3d2caf6ede4bc155d7d8a080af27ff8c3d8e29 | 09621428d2d4cf5ae779b1ac1ad5f9aa306e5558 |
| quality-audit-report.md | 4685 | ee9c14908e6ad73ff8d743f986b107d038a3fb6e6defcc6d68ba1f478c61287b | 04b591c8cc82116b5a1260e62362af52d7e2231e |
| publish-guard-report.md | 1485 | 0cdee5993295dc2dc82b77462882b6338b30c83a2f89b5effd423ff951086e4f | af5916e1e63e3deb13da32e08179c9c370450aa6 |
| published-recheck-report.md | 28447 | ce5d89db3bb60a816cbdae17f83d6a0f2f989381fdd880b2ff92c22a6f016e0c | 7fb7137d175d2e4253d69d56abcd91a3db0a179c |
| source-report.md | 8036 | 3f14296922c23aeb886911e6cd15d4347a7ce3b0b0da7b7f8918a7947d2056fa | 40c0a74c487e9eb8b1c1672c0750b231b17dc467 |
| check-report.md | 8036 | 3f14296922c23aeb886911e6cd15d4347a7ce3b0b0da7b7f8918a7947d2056fa | 40c0a74c487e9eb8b1c1672c0750b231b17dc467 |
| curated-report.md | 1834 | 18a61e76b0d335a8ea0f79b9e59a01d1829f8af19e595b7e22ef96dfa576617e | 416feba3dc33b41e891db877be4cc530d7cb4db0 |
| sources_status.csv | 4121 | ef2b0f86ce2ec567b72162c87ee3aaa529629a3ee8d5f0264a51f2463a3925b2 | c13f813633c59e1a0f6021753e89c3595c557494 |
| tv-coverage.m3u | 48042 | ecf60e348972d73560fd70536d23da42976702b2586f18044ff1b6956c58af9f | 16ac78cd8948f898ccc0a8117e57410d40e28906 |
| tv-review-report.json | 13696 | 8e2a6928d620531306fde0cabb7e8848a886ec86a0c8b00889d04ec832596ea6 | aa7e80d2690f7bceb9c7d516b6a43744322f2884 |
| tv-review-report.md | 7473 | dfaeeaf0a76702f52c8ea420d95769be6b0c27bbd81f9713b8d36f961c76cd2d | 048f7976391f3b4f6339f1c16b90c54b53bcf7c1 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
