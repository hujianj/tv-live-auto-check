# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 277403
Unique payload blob bytes: 184401
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63873

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21291 | d72c3c09f42975b74632fdf966c1d32486497c8fce9ab860f91d520b93c9a783 | 079b92613dde91b03f2dd3e50e2a5f809f101e40 |
| live.txt | 21291 | d72c3c09f42975b74632fdf966c1d32486497c8fce9ab860f91d520b93c9a783 | 079b92613dde91b03f2dd3e50e2a5f809f101e40 |
| live-verified.txt | 21291 | d72c3c09f42975b74632fdf966c1d32486497c8fce9ab860f91d520b93c9a783 | 079b92613dde91b03f2dd3e50e2a5f809f101e40 |
| ku9-live.txt | 21291 | d72c3c09f42975b74632fdf966c1d32486497c8fce9ab860f91d520b93c9a783 | 079b92613dde91b03f2dd3e50e2a5f809f101e40 |
| live.m3u | 41013 | c92446011f686123cb0093f2041d7f623a4add49a556f8a88490bc2c0df8097c | 7327c5b8e394b1f19ffa4fe1ac752fddde5c4bff |
| ku9-family.txt | 21026 | 806106f43342cc11fa0619c5946ba43fa8a96aa9259d34d93d4140fbd5d319d9 | 37d48b50a72bc242c3d94157ff7c0ac59ebbd360 |
| live-family.txt | 21026 | 806106f43342cc11fa0619c5946ba43fa8a96aa9259d34d93d4140fbd5d319d9 | 37d48b50a72bc242c3d94157ff7c0ac59ebbd360 |
| family.m3u | 40500 | 2788a5dad6d10300ea6716eb3fe1fbc9ad49b6d18a58d66ce6375e0fefe491ed | b59c632dfeee90787e341262f31e15fd494218da |
| final-publish-report.md | 10803 | cc9153e6f80e47885e015a4670a496b83e372a91a7b3cd9923b81fb39e699d26 | 22eaf191215a6200c589f69d8268c5c8e5e8a6be |
| coverage-report.md | 2230 | 824e43249140c869d3320166f33a8469458758a6718d84c9085466944cc4f289 | eabc08cb07f0d3a63075020a591ef1afab72f7b9 |
| quality-audit-report.md | 4730 | 7133156ed9328059b5b0e59f0cf62f6d9589f325a917b1c2992d794851b1999b | ba7f06699773a35b3f5c8182074b3deb6e5bcd08 |
| publish-guard-report.md | 1558 | c76821263d1ba954ab31b5c5886528869701b01d7a03cba1b529a1177607508c | fc98aaf951fe60e78fbfc148f8d30349b0b0e10b |
| published-recheck-report.md | 27211 | 0a5a6e06776ac7fc3afe651a907fbe577a8b7d1c6035e0815b6b8ad6e3a58fec | 586d03761d8a6b934688ac8c44657de7de5cef21 |
| source-report.md | 8103 | 5b4591016bf9c19cbd3473aab00c9154931b351ada57ef1c1039d0d5c1d0eeca | 63f8635c4c2ac774004a2de6f052c5f8abcd0e48 |
| check-report.md | 8103 | 5b4591016bf9c19cbd3473aab00c9154931b351ada57ef1c1039d0d5c1d0eeca | 63f8635c4c2ac774004a2de6f052c5f8abcd0e48 |
| curated-report.md | 1804 | ce758191a737f0087788349510db35cf07fca337bbd0e462a61dd6fcba01d391 | 595419d1dad12220686a7560346db06385dfc3aa |
| sources_status.csv | 4132 | 81ce9c64b5bcc3f84eff9da108e9c975a97b8c10f094c1ad050c50446364db14 | 41707ffa7182ca0538bc953f040b91e88ac55196 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
