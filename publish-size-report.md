# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2133691
Unique payload blob bytes: 1540925
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 494538

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 164846 | 74e23bd354881f5a225f53725286237d224c3ec22cd5f18485b41260ba2dd314 | fa0d100a1c20d23dd6652412f36f99c96b1afdf8 |
| live.txt | 164846 | 74e23bd354881f5a225f53725286237d224c3ec22cd5f18485b41260ba2dd314 | fa0d100a1c20d23dd6652412f36f99c96b1afdf8 |
| live-verified.txt | 164846 | 74e23bd354881f5a225f53725286237d224c3ec22cd5f18485b41260ba2dd314 | fa0d100a1c20d23dd6652412f36f99c96b1afdf8 |
| ku9-live.txt | 164846 | 74e23bd354881f5a225f53725286237d224c3ec22cd5f18485b41260ba2dd314 | fa0d100a1c20d23dd6652412f36f99c96b1afdf8 |
| live.m3u | 302179 | 37c2ef28e6dc257da3ae46200278d130ff059e571cd39819d61c46955a57dea8 | 35e20e9fbe232cf999a9f8622b426c21f4b9c71a |
| ku9-family.txt | 91713 | fad4ecc1d7375df05f0ef708a8bcce82a17b56fca426df44fe380903389ad3af | ab557644b6857e7e1f90ea5f26771e5287cc9e98 |
| live-family.txt | 91713 | fad4ecc1d7375df05f0ef708a8bcce82a17b56fca426df44fe380903389ad3af | ab557644b6857e7e1f90ea5f26771e5287cc9e98 |
| family.m3u | 166577 | bec2b5b7708808cf9f64f8a63fab0a111779927ab64a79e742bb8f4004f5af0d | ebbb2fac097a226c26b2e89dfa32c272dca44003 |
| stability-history.tsv | 749832 | 338e6a372bff68c71e3e5e592a24d2649828bd53bb0d66b1af433c9a594d62f3 | 2ab689f8781dec82ab9d940b0a039e1601247f00 |
| final-publish-report.md | 11617 | f1cd5b0a7037790f8be8b06dbb6e27d24d220e2d0d073434a30735057c59acb6 | 039545153177aa5914093dffdcaed86dd741a5dc |
| stability-report.md | 10306 | 9c0a6a27eeb63534f6dfa4c8cf12746f8b6e74291509f43102dad71306ef8130 | e147e3679059c56aa7cd3c5e4b47a540f14f61ca |
| coverage-report.md | 1291 | 538b545c146dfdf733ccf4f9592de52ba4799181aa484fa923658f8926d6b838 | 9fa8604d2e4fd155d031a9b96d9e1c4502c66ab0 |
| quality-audit-report.md | 2067 | fa47d4ff043c096476c32205d131abe22eee73d148ad9c3f3eeec1807e5ff6f8 | ab22cde3030093c3167577dceb031b6779f13d93 |
| publish-guard-report.md | 1038 | c279264a9869bfcef18722e16fbd42f41f06ee80e013e724c03597c013b56ab0 | 54dcbd7051d71f310be13012fb39eb68dbddaf0c |
| published-recheck-report.md | 26300 | 81767a0b45f9209fc437c73a2bb682562797c32b8f7211463e952fc446ca5171 | 6f9da180c107c5168f6700a8cd38f85814f979c7 |
| source-report.md | 6515 | 41144f453b0fb413e14932e414d9181195296af1eb78c8fc0ae0c325510bca2c | 0100f6bf84ea3300b853dd294d79899686af1fb4 |
| check-report.md | 6515 | 41144f453b0fb413e14932e414d9181195296af1eb78c8fc0ae0c325510bca2c | 0100f6bf84ea3300b853dd294d79899686af1fb4 |
| curated-report.md | 3580 | bf3725a58e140c0784f3a935efed4b13550db3fcac979b7f278a0e2f803a1330 | 46ef7700b870bdca3073b5963598c4e95b58a778 |
| sources_status.csv | 3064 | c01d3747e521006e9e32042613b314c37bcba575fc240957dd87fcc2e933cdae | ddd20460b0688807c74e1e5a5052e682ff5dbc46 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
