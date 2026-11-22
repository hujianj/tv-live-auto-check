# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 332098
Unique payload blob bytes: 266145
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38842

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19421 | 681eb6fe593ede110542e6100b14ddcba77fb7be0e0d9ca90e7710c3081786d7 | 9eececbb08bbcb6b149935ea3d6a269a6119de09 |
| live.txt | 19421 | 681eb6fe593ede110542e6100b14ddcba77fb7be0e0d9ca90e7710c3081786d7 | 9eececbb08bbcb6b149935ea3d6a269a6119de09 |
| live-verified.txt | 19421 | 681eb6fe593ede110542e6100b14ddcba77fb7be0e0d9ca90e7710c3081786d7 | 9eececbb08bbcb6b149935ea3d6a269a6119de09 |
| ku9-live.txt | 21620 | 30585b7eb7b20eeaa18ed70e73c88f1aeea43a9f00d2e06579dab73d4ea7f3a4 | 9124515a9f3524208c53011d873e1c22cd77a7ec |
| live.m3u | 37300 | 81356df328432dccfb804ad4a1f01e5c073ffded699f8c819bf4c6ca50038c8c | 2af51430506d3df0b705a78ab948d5ca18040c90 |
| ku9-family.txt | 18986 | 1d23a383ad2b13566a7f61dfd307bf47a81655cc832bfdef0acc2488acddba86 | d2b03f0b9c866ee3de103a1496deb0227e030856 |
| live-family.txt | 18986 | 1d23a383ad2b13566a7f61dfd307bf47a81655cc832bfdef0acc2488acddba86 | d2b03f0b9c866ee3de103a1496deb0227e030856 |
| family.m3u | 36493 | 1e7b1708d9354aef340fa966617c4302c386163117c99825873f04cdebeb6ee7 | 8c30f4776332c50e8fb4679f6c5771345f429fcb |
| final-publish-report.md | 10959 | fe1b42dc5f0c4c5af780b13545f8805045b9ae3735e5925d0bff2415e023404d | a3fcae16a61cfaa4a9edad338da79cdfeff3d4d4 |
| coverage-report.md | 2200 | 8f56ff83a91ac60d1969a405a043c00967a709f6dbd0bcf7ec8af1cccb0a2b7e | 50f39830fcff9c41f554f96e851927262a4cba38 |
| quality-audit-report.md | 4684 | d3900a4cc546e398ebfd67e5c2cf9584b90b4becdda0c81d9d01d088adcc448c | 660bcf571c2736c2ba93d607da8d96c149330033 |
| publish-guard-report.md | 1567 | 6c58ab355485298fe2504236915f6744f1588e79a03ca24c3510f45edb32dd52 | e7ee44af79ac1f40b6a90b776e816f72a582a05d |
| published-recheck-report.md | 31793 | d9ea3055fbedcd6bbdf20d5d4502b6b1c7dba525e87045c6e977b6a3fb695ac2 | b895d045d62eefe9cb9ded17f386926da589f7f5 |
| source-report.md | 8125 | 48e2557444bdfd73c8c20be92fb56a6e46db8b1cd1b49e5ebeda715ee08b9148 | 884e8616d8c5e1c348b02fddf34b9948b4ae3f6b |
| check-report.md | 8125 | 48e2557444bdfd73c8c20be92fb56a6e46db8b1cd1b49e5ebeda715ee08b9148 | 884e8616d8c5e1c348b02fddf34b9948b4ae3f6b |
| curated-report.md | 1833 | 602d6eb6964d3100a88c7f3d91cac975a00adb44e33e4c03c6164d7308ba8a62 | 3001d8b9bcfa923ae45f5a4a0f9193484b014625 |
| sources_status.csv | 4181 | b11e4d31a7acd5e366a7a3e6695900b94ae7ff2cfdcb6129bdaa69e1f3574f0e | 48447160dd3294bddf3e2c0fe9e4af82f7a98914 |
| tv-coverage.m3u | 49625 | d1a3ce60f3d2a7154b1d03fcec824eb8511538a68aa79926ff4b6f3178652066 | 460f25ff11109a8d2a36503b193a477937d65ea4 |
| tv-review-report.json | 11379 | d354927c0a7373c2d05bfe186e5a07e37308a6c9bf6f28ba6f2a5956155e70f9 | 8c46adb134383ff4e5d58344b3421e020c7135bd |
| tv-review-report.md | 5979 | 7f8e157f8b16f1759dae0ae9f265865bb052ffb74fc3944e9be07d8f175dbf7c | ead253f35bf196e0a2c4980248e870a6716a2753 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
