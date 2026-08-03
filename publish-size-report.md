# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2459197
Unique payload blob bytes: 1710159
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 646962

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 215654 | 1f4891ed391d30dc267088b17db938ef8a04ed428bd88ded4b2e899213fe4347 | a16c664c6f5aa620e1101a91d609a6f14a499e15 |
| live.txt | 215654 | 1f4891ed391d30dc267088b17db938ef8a04ed428bd88ded4b2e899213fe4347 | a16c664c6f5aa620e1101a91d609a6f14a499e15 |
| live-verified.txt | 215654 | 1f4891ed391d30dc267088b17db938ef8a04ed428bd88ded4b2e899213fe4347 | a16c664c6f5aa620e1101a91d609a6f14a499e15 |
| ku9-live.txt | 215654 | 1f4891ed391d30dc267088b17db938ef8a04ed428bd88ded4b2e899213fe4347 | a16c664c6f5aa620e1101a91d609a6f14a499e15 |
| live.m3u | 388465 | 63d6ef6efce5a12274f27bb11f7f02e3c0ea359fbcca4245bc7b4408b9e670ac | 7b823047a9c3b4ac049929da32bf17a21a2cd4e4 |
| ku9-family.txt | 96261 | ee42c7603bbb09c9768a2fc68918259eaae0a17a4c2f3269c52106652311c6b3 | 1b500389a06b9675e611f0f0c69b8dd9d30deb63 |
| live-family.txt | 96261 | ee42c7603bbb09c9768a2fc68918259eaae0a17a4c2f3269c52106652311c6b3 | 1b500389a06b9675e611f0f0c69b8dd9d30deb63 |
| family.m3u | 175252 | 0c20b23af08ca884ea88274b225282fcf94d3c020d8b2d610a7e38b63505683a | 21093e711850b06483afc11f33f45f0e7aef83b0 |
| stability-history.tsv | 766887 | 89db4d80be25a82758fdda26eb59716b63d05be5ccbe546d35028bbec3f84ead | a185bcfdaa72801888380847fb4d5fc8fd7de285 |
| final-publish-report.md | 11661 | 7dee358cb782bb55708519c310ef69839fa2ee1756a5907ac2c099763905e5af | 73c67abc117d01ac64c54a8fb0b332b9f2214292 |
| stability-report.md | 12838 | c9b622792851761ac6b99e1179e4a7151d146d0c7dcb333b9c71291c1e6c963e | 91511b04afa7edecafd76e2d16856ede31adb8d4 |
| coverage-report.md | 1348 | 319b8cf5e719b868b9905a0cfa1d5058de41a019ca5421485d8a7c699109f7ca | 2fa7d728ebc8cc77ae1bfdf31edb001fef5834c9 |
| quality-audit-report.md | 1504 | 2627c723671b6bbe0b9ee1cbb3079596007fd423ce824b0f696ac09ef66afd7d | 660c7ce4c3c2cb23441be3b69922619e44da5bf0 |
| publish-guard-report.md | 785 | b6494289f393b4f9419a6751f383666643e047da5cefe78e67d9096a6669d9f5 | 487ec462a0c53cc34af9efbe508b2da7c256fdc1 |
| published-recheck-report.md | 27523 | 6d07a6483528d94819ae94c09e12c9f22f083ae85ba96ac5b91762fc161e3d9c | 1bc9b39c130aba3425995f9f1868b17ee604f395 |
| source-report.md | 5815 | c87790180a77ecc062b96df95e438e5f42d2dfe6323fb7ab620c51ee7beb92a6 | 897b8fdfd5ca162b9da40fc03de4f34bdb2b3fb5 |
| check-report.md | 5815 | c87790180a77ecc062b96df95e438e5f42d2dfe6323fb7ab620c51ee7beb92a6 | 897b8fdfd5ca162b9da40fc03de4f34bdb2b3fb5 |
| curated-report.md | 3566 | 4c962debd8a1a42ac224b67d627927e72077985f9e287f193fba30b974766e88 | 49cca7d517ac7ede7aa7f55bf8eed6d6492da045 |
| sources_status.csv | 2600 | a0c3169592d6403fa6e1c1ae2fc1047bb1b737ec78904bc46212c54ce53cf0d5 | f9c132cbf40a0ecfeb8dd9caefccabe50c821b66 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
