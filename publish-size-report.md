# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 300631
Unique payload blob bytes: 198697
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 70686

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23562 | 57d7ad82b4979f6dfdab1ec9f371be31072a295a10750b22b206187aa72a7793 | 6415363b886a8d2cc9245c1f6a2c61112fb30b64 |
| live.txt | 23562 | 57d7ad82b4979f6dfdab1ec9f371be31072a295a10750b22b206187aa72a7793 | 6415363b886a8d2cc9245c1f6a2c61112fb30b64 |
| live-verified.txt | 23562 | 57d7ad82b4979f6dfdab1ec9f371be31072a295a10750b22b206187aa72a7793 | 6415363b886a8d2cc9245c1f6a2c61112fb30b64 |
| ku9-live.txt | 23562 | 57d7ad82b4979f6dfdab1ec9f371be31072a295a10750b22b206187aa72a7793 | 6415363b886a8d2cc9245c1f6a2c61112fb30b64 |
| live.m3u | 45068 | 5764525bcbee0f954ca6a50ce88cc4d666e8368b92aefec02196a222a9f8bdac | b7f59481263821d114a7ac0e0ce4a06cd2838b6b |
| ku9-family.txt | 23146 | ded56dd5302a5990914cb20710405494793d9f4b2983684767fecbf5fdde9a4f | 06b10f6af693c21a5c15c31342a1c09c2f551eba |
| live-family.txt | 23146 | ded56dd5302a5990914cb20710405494793d9f4b2983684767fecbf5fdde9a4f | 06b10f6af693c21a5c15c31342a1c09c2f551eba |
| family.m3u | 44280 | cfe359316f9c1be00b782b84d50c0c718a53868f1a194c1e7b351fbb9fe2001f | a50081c93d79a26a6c5688cb7579529ebe02fd97 |
| final-publish-report.md | 10751 | e7a58ca8b3718b330e2f136af7bcf9104f8d6ea034f78f780adb926058db5004 | 7e34be335fe5c8d7ec6c41b1adde687ea332c190 |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4720 | 1be650d8e534af1d09e79695fe8e22226f8bede80159487d484baaf69a5a4a35 | 27c25b3b666da0c4b6c7db12cb1d4bb8ef208871 |
| publish-guard-report.md | 1605 | 21db79de76e3a66abb567f3687dbb0a37f61d51cbfe936036ba297e3f7abe9c3 | 6797dfd1f5fb163a5e9a7202547dc1a607a64f16 |
| published-recheck-report.md | 29291 | 82510c59c5b8cbafe0106d9c0b459009e174b007de3000f7c61529b192c31898 | 10a2d5876f1d0875211c15c6f26ba2fe88d0b175 |
| source-report.md | 8102 | 7b59254ffca3fcfbd74196764dd39257e52e903681a6d792fb9fbd1d22ccb988 | 80d5891f3e3bcdb24faede83787c7f216f523cf8 |
| check-report.md | 8102 | 7b59254ffca3fcfbd74196764dd39257e52e903681a6d792fb9fbd1d22ccb988 | 80d5891f3e3bcdb24faede83787c7f216f523cf8 |
| curated-report.md | 1804 | ff5a461e38042864ac4a855b45d28c18381225546f2248147bb5845798936af7 | f35e558077cc118767a3c43f83fc0aef3aa930f5 |
| sources_status.csv | 4138 | 7aa27dadf56f348e44ff8db6d5e3c8ef447e8a4c675a6b5b7676bb0a787f5ae2 | ae583a741e067a6b537d0ac5fa17a5c52db756b2 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
