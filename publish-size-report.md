# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 282724
Unique payload blob bytes: 187089
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65817

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21939 | a50997899894e869393e6484c570d6a73a9e7b963c1f9414cef3d060bc04871e | 7a8a6b420cd36f75f8439cebeafbdc4235510f7f |
| live.txt | 21939 | a50997899894e869393e6484c570d6a73a9e7b963c1f9414cef3d060bc04871e | 7a8a6b420cd36f75f8439cebeafbdc4235510f7f |
| live-verified.txt | 21939 | a50997899894e869393e6484c570d6a73a9e7b963c1f9414cef3d060bc04871e | 7a8a6b420cd36f75f8439cebeafbdc4235510f7f |
| ku9-live.txt | 21939 | a50997899894e869393e6484c570d6a73a9e7b963c1f9414cef3d060bc04871e | 7a8a6b420cd36f75f8439cebeafbdc4235510f7f |
| live.m3u | 42163 | b472309b36fcf17e544e7b18ec969dd1aabff95912dd533fc1618966b60e0419 | 9a0321635ac6dcc82282f78a0b89563ad2265b19 |
| ku9-family.txt | 21731 | a738600857c11174ef45856747d3ddf0f3464d305468c72e256fd13855ad4d02 | 08d07ae1d725feb1123a194cbdcef6f4c64e88c2 |
| live-family.txt | 21731 | a738600857c11174ef45856747d3ddf0f3464d305468c72e256fd13855ad4d02 | 08d07ae1d725feb1123a194cbdcef6f4c64e88c2 |
| family.m3u | 41769 | 75149c932d62d3c830f6a0d795d0b4a20fada7e0f25aeba7991e7484690dc54c | 0374ed630a306725a68fa115a240767d51922a6e |
| final-publish-report.md | 10654 | a90b646a27582b59d8abd8b918802dab3870d6b3c00f9a50b15a3bfe6c326c8c | 9831a37941a94b3d19a33271e6ae4974d4571792 |
| coverage-report.md | 2225 | 9313f064185056853c66e4ddfa913b2ab0b89e0700b4be411210d5dc030ff152 | e007670077b15ee778ecee54d3dc82da93345ac8 |
| quality-audit-report.md | 4718 | b52ed8fdfeb0a78db83c2483fc7a6c74d3497d52d51fe35ed0ea3331ac7fcae0 | 0cc34c4e3f51eef33eeb64a6484b6f4d279eedd1 |
| publish-guard-report.md | 1557 | 16a252bce1e15cfd01ecadce2c1fd3edac8d2d248ba5f3216d97767bf8bc855c | 4f6222d3897d7b7ecb62cc8a732f018b67e43139 |
| published-recheck-report.md | 26305 | b990755fc9454ddc5402d9cc2694150ce30e63971498f1af985d9b0bd8d2b591 | 2e373eb0cddc5f3ae9b4ce76a8b76ba959befde9 |
| source-report.md | 8087 | 72952060bf47849808eb394816d0a515effe0f081c99bf839665a09b00de192b | fc1a1c46cae7362abdaace1c79225d2961743a14 |
| check-report.md | 8087 | 72952060bf47849808eb394816d0a515effe0f081c99bf839665a09b00de192b | fc1a1c46cae7362abdaace1c79225d2961743a14 |
| curated-report.md | 1804 | e4d758bf8f22a29c66de145d67920aabb71c18df86ac7e7532e75854dfc055e3 | b029b29342ed14febf83ed0578c58514a913533f |
| sources_status.csv | 4137 | 17bff468c48512e2d57f96536bad207d01252f6ea143583ef5cbc3bd6911e64f | 15ba606141c181c356506948b609fc62ecb58f9c |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
