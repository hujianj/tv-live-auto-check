# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 354476
Unique payload blob bytes: 283128
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 42386

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21193 | f64ddc55dbaca25e2db13abd20064b3e2bc26812369b1d620c8da5fc09e12615 | f997f3fa760a190a29fdd3aae89c85247e74b9c0 |
| live.txt | 21193 | f64ddc55dbaca25e2db13abd20064b3e2bc26812369b1d620c8da5fc09e12615 | f997f3fa760a190a29fdd3aae89c85247e74b9c0 |
| live-verified.txt | 21193 | f64ddc55dbaca25e2db13abd20064b3e2bc26812369b1d620c8da5fc09e12615 | f997f3fa760a190a29fdd3aae89c85247e74b9c0 |
| ku9-live.txt | 23751 | 51af3c24e255611dcb1956ed1d769316e2b8cf21527f35373a863445583981c8 | 3bc366046938c1723c5b03ee70116e81e39dda96 |
| live.m3u | 39851 | 00d5d8c01f4afa4a3cb9b5f23cacbb94a96c9f32fcffd030a13191c591a4ebce | 0e672e39c48e3e6730bae4d75f50736893f3b953 |
| ku9-family.txt | 20757 | d0db02fc9922cc3ac09b31c278526c902a8a3efed209b986ddcb6993c067e053 | 768f0c6f022ad21a0d1333a81b87721822db5b82 |
| live-family.txt | 20757 | d0db02fc9922cc3ac09b31c278526c902a8a3efed209b986ddcb6993c067e053 | 768f0c6f022ad21a0d1333a81b87721822db5b82 |
| family.m3u | 39043 | 939079a81eeac3a3ee407928418ee018b142f7d0df3acc916b6b1fdb90f275fb | fef0e9e39f2a53f43994eaa6b282dc7acb35d786 |
| final-publish-report.md | 11118 | 1a86e926c438285f25e6c18a527b2794cc4a7ff73240f852ecfb8536cdd57dad | fb006f4d53d504f163f4bcfae506c4e28d7b1740 |
| coverage-report.md | 2200 | b0da701e1c9912b174fd43c4f70f46f968a72933952e9c67a9bf2eeaea1b0469 | ba7d5544ed82c5e6ef8380e21349168ae6342854 |
| quality-audit-report.md | 4703 | 46270cc0b10b5fb92e8858f9c21ebfdaaa5ee20530fed8b3bdc135570849a2e9 | e919423c597899795672fcef52bddd14fad81eea |
| publish-guard-report.md | 1522 | 435899bc652bd082ddb0cc18a873d52d941bc1a993e8d26da1284effb3aef54e | 30c22c30b9d1dac41e64e672c06f8ec43dfb90ef |
| published-recheck-report.md | 30771 | b2bb4b94080780e44220fb09f1486e98871e5888397f30b88fa98181f741a7c5 | 10e5210a93f0c14c8c13b79acaa3ecfb5f0d4d9f |
| source-report.md | 8205 | 67bea7059d3ce55e5ee212fa234eabc6302e8528a0b95aa91dd5d8940a5bf64e | d4f97c4bbc18b138850e44e92e489bee24e19cdf |
| check-report.md | 8205 | 67bea7059d3ce55e5ee212fa234eabc6302e8528a0b95aa91dd5d8940a5bf64e | d4f97c4bbc18b138850e44e92e489bee24e19cdf |
| curated-report.md | 1895 | 4e738b39e5ceaa4fa0f22ada34336287f4c575a0f57f2e66422ad3a4719fcb3b | c8f845caebb6ffeff497d5937051afcd874e43c8 |
| sources_status.csv | 4176 | 77147bdcb54295fce037bce4842413d0f2920891409fc6699af69864d4cf461a | 369c3ac136e6183c80517ffb76a34f50e578ec4c |
| tv-coverage.m3u | 53021 | 82e0a9ccd4e0b416e83d11eb4940d0d13b7b7ae3a485d9afb1061a8bbcc02f7c | 9248d1f547760fc7ddb95bb16c3a00f81e6b74e1 |
| tv-review-report.json | 13551 | 936808c4db1437cb6ad23903ae5014e888d711a05b8c7d0d088d10b19284c4d3 | a07ba886278b0a434287d208e4e930bdf39cf4a3 |
| tv-review-report.md | 7371 | 3048ec364c539c22d293fb52fe40cba07e67b2c2f7006abc64287861960dbc36 | 1ed7d5a595292435b17b5de5d3bb1fca382cbca3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
