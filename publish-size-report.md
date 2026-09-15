# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 224544
Unique payload blob bytes: 153512
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 47586

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 15862 | c46737ea08bd671c67ea987ebfd4e6d4988f7a806b2c4494a91433e679fd2057 | 85dd1a961eaa9473d5003f8e8c3d081862e0c8b8 |
| live.txt | 15862 | c46737ea08bd671c67ea987ebfd4e6d4988f7a806b2c4494a91433e679fd2057 | 85dd1a961eaa9473d5003f8e8c3d081862e0c8b8 |
| live-verified.txt | 15862 | c46737ea08bd671c67ea987ebfd4e6d4988f7a806b2c4494a91433e679fd2057 | 85dd1a961eaa9473d5003f8e8c3d081862e0c8b8 |
| ku9-live.txt | 15862 | c46737ea08bd671c67ea987ebfd4e6d4988f7a806b2c4494a91433e679fd2057 | 85dd1a961eaa9473d5003f8e8c3d081862e0c8b8 |
| live.m3u | 30105 | e7a68b317f83de8832fca1c00fd01d3c1833f893d00d8e35ae282ef0d416e5b1 | 205f717dbafc4de782fae0afcdde4ae7ca2d8082 |
| ku9-family.txt | 15440 | c89efbac1aa2144ce1752fbd1e0796ff7be2bee61f041677975940b6c6935149 | 477a5648222fe76cce843445389d74bfbf65f8ad |
| live-family.txt | 15440 | c89efbac1aa2144ce1752fbd1e0796ff7be2bee61f041677975940b6c6935149 | 477a5648222fe76cce843445389d74bfbf65f8ad |
| family.m3u | 29311 | de2f909609e71c512b7aaccae891a8dcb45f79cb7d7708c9347dc516a5fc6927 | af410ecea6a0a35669f51ad3f8a53963bbca62c1 |
| final-publish-report.md | 10653 | 33f1b1499c78f38633402f6d0ea44bf9adefb0521823d3d69de65f25b87cae5f | a7745361282fcc177ccd7c43de20c19e30ecd84a |
| coverage-report.md | 2244 | 0bd0ac64bf6d946e5377c74371ca51175b47f7563d43b1a534ecfad43183395d | ad1168b3ca4662773a4590e34c3c86332fa3d8b7 |
| quality-audit-report.md | 4721 | 53447bdd18547dd318f28263aac60d48e72774649c12e76f517523baf5c3ce5d | 145f7506395f2bab9670d7db776beb5b0a97de18 |
| publish-guard-report.md | 1684 | c561e8dfa86788172c6b01ce5a6d9199be5e4531369bf620fc31df904f1dc8ed | 9401f9c8381d13c70baa63d271c89130b6b1e838 |
| published-recheck-report.md | 29490 | 2ec7ddb1f87f83e05f43ebb56eec8c4d565fd4c8438e31ef62bc9b94834642a8 | 556f9ed240389169e6ebcb14a0ec3867c6b27195 |
| source-report.md | 8006 | 49d1b66e820dc17b02bb3beda7105a17c6a1c50d2e4b5fab94438f24902051f7 | 53a7e543a27edcb9841eff519fc68370c07a3c02 |
| check-report.md | 8006 | 49d1b66e820dc17b02bb3beda7105a17c6a1c50d2e4b5fab94438f24902051f7 | 53a7e543a27edcb9841eff519fc68370c07a3c02 |
| curated-report.md | 1858 | dfeae009a2caeee0ae3d708d48cbf08a7b81ca466786abafe91a67a1cc8aadb9 | aa47b7244701e51f458794aa963fa7c1a6767f58 |
| sources_status.csv | 4138 | 79da594e7e508bc110433c05adb35a51144ff0b93437786b2d5fc612d556569a | 63cec4a0c0a1d5ca61d13b931cfef56203b523be |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
