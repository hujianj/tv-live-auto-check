# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 324871
Unique payload blob bytes: 261109
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37236

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18618 | 3c957b92e0e087e8be2f9fed500ce9fc24a98a44f8e2791a83c2343723136886 | 0928aaff211eea9a9177b08b860cca7b526b8edc |
| live.txt | 18618 | 3c957b92e0e087e8be2f9fed500ce9fc24a98a44f8e2791a83c2343723136886 | 0928aaff211eea9a9177b08b860cca7b526b8edc |
| live-verified.txt | 18618 | 3c957b92e0e087e8be2f9fed500ce9fc24a98a44f8e2791a83c2343723136886 | 0928aaff211eea9a9177b08b860cca7b526b8edc |
| ku9-live.txt | 21420 | dafbbf3763d81954b1dfe5ce6248046048aece30d29144ec0e97c62731b572c0 | 1c7344944d756e2744c26d5a64010b8d77eb3de7 |
| live.m3u | 35836 | 88353ee00d18e3761f22b70643af1f7972308ab677c95b32ac65f3886f88b8d8 | 3e1651df6d8ce55c774a9c8c1f4c3913aaa981bb |
| ku9-family.txt | 18340 | 8cb94ffce43f16ab2115f3722021942f80718ca812f9ebfa57c8e6d478da7c7b | fd69a71e686f66316bd630bb94f1876bd6e411fd |
| live-family.txt | 18340 | 8cb94ffce43f16ab2115f3722021942f80718ca812f9ebfa57c8e6d478da7c7b | fd69a71e686f66316bd630bb94f1876bd6e411fd |
| family.m3u | 35310 | 2a28d72ac2b155cd2b6d82ccb0310c0c8a3a530e7e0c24090fe0f5de54889c29 | e563b9541ac6d7df7aac3b74922bfbac5a54ec75 |
| final-publish-report.md | 10875 | db514b3353819cdb8401e16b8a44bec3050388ba900c727a431ea5b7b50a81d6 | 8fa1f9b324e7bb0bb47788a53b329bdfdbd276f5 |
| coverage-report.md | 2195 | d732b6dbf16cb6c501b85df4bef6aa4990b634c0b227e8f29fe8c0ecd6625655 | ff3e5be5669116e66bec82b9b4853ec6090d9118 |
| quality-audit-report.md | 4681 | 6a527afe959fcc0ca1a15e6c1c86820c7a8c6635eff8fffad58395b08569caa5 | 1689b21723c2ee59893a1996412c3802276f2bd4 |
| publish-guard-report.md | 1513 | 1dc2fef5fa05126296b9b4b9716ff14839184afcbc2753cbb8bfbab9dfdd13b6 | cfb0f831981f4cb86a99a78bd96244e0ba15bcb7 |
| published-recheck-report.md | 28242 | fa2eea8a7641bf18b89f08fe6ceea134879afa54dd12fe1c280add9bf0a22777 | 9560d9d88c1c6ad78b89580083db961753f4f84c |
| source-report.md | 8186 | 46acde2276e8aec2d901439ded2e4e7af676ac139b7a1c0aed8d591070afacd3 | aa322c8416aba6619d717e9b951f23e128300208 |
| check-report.md | 8186 | 46acde2276e8aec2d901439ded2e4e7af676ac139b7a1c0aed8d591070afacd3 | aa322c8416aba6619d717e9b951f23e128300208 |
| curated-report.md | 1833 | 336e16121143a3eb44e3e4643fd0123935776981f8ebd5012d5fd974e1a7881a | 5ff7657699fe5849f69de2b497db6dcb84b5cc12 |
| sources_status.csv | 4242 | 51c7b46fbb23a4539a59a850b6d823461b839b19d6118cec5697b519430ae708 | 62ab5f49ce8ca2ec4c5685c340ddffb400d65068 |
| tv-coverage.m3u | 48809 | 6ecce270458cd8019a9371b1450c038ee98ba4e3ce3df343d498be19cd95738b | dfac14c058502be6a27ef7416cf98dec65d5f250 |
| tv-review-report.json | 13497 | c50130c8a08cc62400bb9dcb5f328c1777bd653d475965a6e5f9dc0edd9b3ef7 | a3f70d40435b9998a8014d5ee1e320c4ed5a9367 |
| tv-review-report.md | 7512 | 77604f9f8c6287222830222eaf073e719ef715155365854948a300397a606d44 | ef87e894728d0518f37f4da2bf089e0a63927f5a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
