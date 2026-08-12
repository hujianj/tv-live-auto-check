# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2149211
Unique payload blob bytes: 1545274
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 507507

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 169169 | 1575c82601a946a6aeff402c452bfc744b3c2708735c2b3b905458737a7e3aa5 | 98f1026583830dbf7b89570580092974b08df2be |
| live.txt | 169169 | 1575c82601a946a6aeff402c452bfc744b3c2708735c2b3b905458737a7e3aa5 | 98f1026583830dbf7b89570580092974b08df2be |
| live-verified.txt | 169169 | 1575c82601a946a6aeff402c452bfc744b3c2708735c2b3b905458737a7e3aa5 | 98f1026583830dbf7b89570580092974b08df2be |
| ku9-live.txt | 169169 | 1575c82601a946a6aeff402c452bfc744b3c2708735c2b3b905458737a7e3aa5 | 98f1026583830dbf7b89570580092974b08df2be |
| live.m3u | 304806 | c48052d6cf3d3df9b4c8e078d62bf474257f6c427541ffe0a3171b468b84ce5a | 36f0c1d6dbaf4e1fe05ee088d664071998e600d2 |
| ku9-family.txt | 89849 | 615571956dbb508e7b1916f4c7d013d11ff853c71b777aa727f1394074b5c4d4 | 8cacbb82ae4c82e787a397fea487ccc418fbaa41 |
| live-family.txt | 89849 | 615571956dbb508e7b1916f4c7d013d11ff853c71b777aa727f1394074b5c4d4 | 8cacbb82ae4c82e787a397fea487ccc418fbaa41 |
| family.m3u | 160740 | 9cb76a0212e8739949f658dfb6856ac00b254c7238a783d50ff6c5c8b241cac1 | 84f39323c1fb1ea0d0d2ea7c9c7381f229aca2cb |
| stability-history.tsv | 752529 | 4b1c79536d83ae557eee76f659b93d3f61c9933a9bb12e5c65bb790a0f35df88 | 4d556c10dd39dcc8f682db31c1bd6c56306f16bf |
| final-publish-report.md | 11585 | 99f626e1f2e4a34ef005693ab21ea036f9753d13de294a8bad78417109db1c9b | efcfb5f98a9dbae74742d63d8874cd926302fb7b |
| stability-report.md | 12282 | a6832155537a902845791c8a8ef3de02357250f88779556a6856981436054d69 | a5dd6d15bda25b06f756cc0a8bb4f3206f6af63a |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2065 | 05d7ab5c952d44ca2a18db62b5e6065b7f1e3f4178312fd31cca187080fbb14f | 30aac4614bef504c24c2c003fe42a22aa7a99f1c |
| publish-guard-report.md | 1148 | d6feec36b2494618bffb2fc8d74654b3609477c741684960edc1570400286008 | 2f7e85dce09b199a9b4ddf4ecc98e333a6cddc53 |
| published-recheck-report.md | 26680 | 7039b8b206e100a7e49cf8f6d0568c6137135b2a1dabba164921c562d60794ac | b76438240e5538deefeb5cc4be30cc6a33048fff |
| source-report.md | 6581 | 05403d3ec931e9a29c5a1ea28d8907afd94ee4719b5a2b7efc43d208f01330c7 | bf67b9d6f203806d1316be64feb262191e2ddc92 |
| check-report.md | 6581 | 05403d3ec931e9a29c5a1ea28d8907afd94ee4719b5a2b7efc43d208f01330c7 | bf67b9d6f203806d1316be64feb262191e2ddc92 |
| curated-report.md | 3409 | 9e642c41fd07a220ebc46289054faf36e94bde4664bad38d2c8431bd013128e1 | b3650cf9ea6436aa5890d515ed7a7f9c8ab86502 |
| sources_status.csv | 3140 | 47c3499f9bcd4ee9f2712218b74d408c95b610d624263c19befc14c5513b69d4 | 17670108b10ddb77cfd3bbdd05fbe107ab61f721 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
