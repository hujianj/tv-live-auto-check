# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2147517
Unique payload blob bytes: 1544723
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 505716

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 168572 | 672a9199115152f400fb810f9a7c4067d2e2ef041e1798945f6814dbf2a640be | b63c879d8510b80556655ed3ba71c3d8e5896f84 |
| live.txt | 168572 | 672a9199115152f400fb810f9a7c4067d2e2ef041e1798945f6814dbf2a640be | b63c879d8510b80556655ed3ba71c3d8e5896f84 |
| live-verified.txt | 168572 | 672a9199115152f400fb810f9a7c4067d2e2ef041e1798945f6814dbf2a640be | b63c879d8510b80556655ed3ba71c3d8e5896f84 |
| ku9-live.txt | 168572 | 672a9199115152f400fb810f9a7c4067d2e2ef041e1798945f6814dbf2a640be | b63c879d8510b80556655ed3ba71c3d8e5896f84 |
| live.m3u | 303030 | 9a9dc589200ac72a4f089a5334860cd7c4a4b9d70ec87a96b6f1477cebc35926 | 6db34de9f8c21a15308dc3de74ba11ccb2368255 |
| ku9-family.txt | 90534 | 5e41d388a4c6daa0901e1975f094a764f77b01f880771121f61270a444ffa5ef | b18e9e9c2dbbc764b46e976d11ef41071c723690 |
| live-family.txt | 90534 | 5e41d388a4c6daa0901e1975f094a764f77b01f880771121f61270a444ffa5ef | b18e9e9c2dbbc764b46e976d11ef41071c723690 |
| family.m3u | 161629 | 9ce564c3dc952a111a673d94eb8e4e3f1f0592e62c254f93a9556e40c31176f7 | 7f18427ca3c84e32eeba5dff93dc8f68471eac78 |
| stability-history.tsv | 752669 | 897283e86548b50af44ab350fc6cbf42913ba9506ac67b0111ea6b9cef27edb1 | 65a8d3b6fec624d1d1996b084db91f7b1e1aeba2 |
| final-publish-report.md | 11545 | 0a94494ed4f4b87908f9d7322d52e34e0228656996e50e01bd34244395474ce2 | 2a930e63651b2baba8224d28e5635e0eed2fe7b9 |
| stability-report.md | 12188 | d8162766e64df6a7de47294541f44acf486052512de403f0982201ba93656041 | 17aec217992be9c962d5f981000a14caaeb4166c |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2065 | 41343b7fea8c4b18611f98b371c5c68b39b1dd64183c00f94872d1df29b31fa7 | 105f0b5d0574573177bca41578fe77592d09b42e |
| publish-guard-report.md | 1147 | a5fa6663a03c0b974a3a46c847e02660a2a8cc631aa9582c4257b7d17ad9258a | c02d1c1f952e0ea7897d9f28846fa6f72ef29ea5 |
| published-recheck-report.md | 27015 | 3aa839d999282739ef09c2200b0948726e53bcaa6a93aab82e2a4e8907898b62 | 627b9aaff89ae5dda882afaf337d02f23dba7b0b |
| source-report.md | 6544 | f2fd418aabb1429f0bf903eb9ff5494670572d5c477d426497332b4bc8bb0c5c | 5e87d78bc7372ae8402b7cd28e6ad1adf260f1e8 |
| check-report.md | 6544 | f2fd418aabb1429f0bf903eb9ff5494670572d5c477d426497332b4bc8bb0c5c | 5e87d78bc7372ae8402b7cd28e6ad1adf260f1e8 |
| curated-report.md | 3352 | 85e1202a681381838fc7b6fadde61245a9c1ded2bdb77ecd8cae429518683b0a | f1d8eed65a3b9a2acf04e632d2b97e9f43f649fc |
| sources_status.csv | 3142 | ee528d254e286ddbeb2f05858665773ef1870067f3b976e0e783f93e77a05464 | eb501db38cf99fe91ec4ed7e6f53e696a0a4b41a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
