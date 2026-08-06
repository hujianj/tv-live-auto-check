# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2472802
Unique payload blob bytes: 1716523
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 654672

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 218224 | d6c1a9b7c8b6ecd8dc56302c778dabfe348d1587757197db0eac9a1e4f799c46 | 1020a40e68505557e4b4e5359b86323957324344 |
| live.txt | 218224 | d6c1a9b7c8b6ecd8dc56302c778dabfe348d1587757197db0eac9a1e4f799c46 | 1020a40e68505557e4b4e5359b86323957324344 |
| live-verified.txt | 218224 | d6c1a9b7c8b6ecd8dc56302c778dabfe348d1587757197db0eac9a1e4f799c46 | 1020a40e68505557e4b4e5359b86323957324344 |
| ku9-live.txt | 218224 | d6c1a9b7c8b6ecd8dc56302c778dabfe348d1587757197db0eac9a1e4f799c46 | 1020a40e68505557e4b4e5359b86323957324344 |
| live.m3u | 394479 | 4c09a61a5049780b4080b61a0c56ff2289ba4588ceaabcd0390fa77cf1a5e0bb | bc9c8aa872a7607f23c878ef628e5373967b5d19 |
| ku9-family.txt | 95751 | ee770aad62179cf93170ab7a45ee05b1ef9dba01fcdce182b4321104b7e22283 | 37a40b5d2831ca3b742b4f332e9dfd026abf2ec5 |
| live-family.txt | 95751 | ee770aad62179cf93170ab7a45ee05b1ef9dba01fcdce182b4321104b7e22283 | 37a40b5d2831ca3b742b4f332e9dfd026abf2ec5 |
| family.m3u | 174861 | a69d162f7b2ce873fa6460632e054c255d42ef8051885c1831d60cd6053c774a | 7b29a2425075b3c210718105f93918598d535430 |
| stability-history.tsv | 765206 | 2f1ba5c6688ec2289605c6a4122e31ac5b9c88f008cb84256a4133a52f39fea1 | 940e176856582ffa13ad1cd1886e492c26a80870 |
| final-publish-report.md | 11517 | 4a1e1fe938f996e3a7de61e651d998b814ef697659922264004bf7ff5524fa4a | 4fea322e4245ad033c7b72d83cb48c65ffc1f6e3 |
| stability-report.md | 12736 | c9efed3989459d85bcfa84d70d7907f27ff5734582644f28e099457043e195df | bc103881abd671517a82c0653242d76e8e015222 |
| coverage-report.md | 1291 | 26a98c21c8d1e7c1f111c894b6da488d0cafcf99e84fb680209bc9dbfcf76ced | 1f1937c59c1a620785aa0b38b7622b2c536c186e |
| quality-audit-report.md | 1435 | 1bdff894eefb7247d6afef03a421af6ff4abceb8f4b546794a82f07bd822e2ca | bd63059fac5efc3bd9f3f4f34db139cf4ab8ded7 |
| publish-guard-report.md | 789 | b04d59ae521dc04f91d25b42f7e59200ce1d3b1e07cd1f60b7d375bd3505bead | be476e9472e121788557812789e143a683ac3b28 |
| published-recheck-report.md | 28149 | 5e80f1e5353a5cd6ff1adfc1f7a723f4920221d064f6f1915d458dcc960bc480 | ba73997dfa4d98d3a76e83181190c8a75a9bb7ef |
| source-report.md | 5856 | 734d91c3c81919bb7e150a44144e237bc911ff89473843cfe89a30aaebcac7ba | e22e2da4b186872eac7ce03d2dcd50e16c74f2e0 |
| check-report.md | 5856 | 734d91c3c81919bb7e150a44144e237bc911ff89473843cfe89a30aaebcac7ba | e22e2da4b186872eac7ce03d2dcd50e16c74f2e0 |
| curated-report.md | 3627 | 85790826e630395f1c7538485cb152de2a163f3e0daaf71975145378a078a166 | f6f2a516357a1d408247055a6a052e5b3f9cd399 |
| sources_status.csv | 2602 | 585a3f6c1f9a45a5385085fbcb74faa7a2c6e06a725581461d69c646cb23b187 | 253424a52ff62ae0f68fe43c6d3b00e63f1418dd |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
