# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 332951
Unique payload blob bytes: 269901
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36876

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18438 | a03812ce57d6a5ef51005a2ce4a87b4d234b69612762019896ab7f523192325b | 73e46170fa8231a73689e3ae2099c584f70f933d |
| live.txt | 18438 | a03812ce57d6a5ef51005a2ce4a87b4d234b69612762019896ab7f523192325b | 73e46170fa8231a73689e3ae2099c584f70f933d |
| live-verified.txt | 18438 | a03812ce57d6a5ef51005a2ce4a87b4d234b69612762019896ab7f523192325b | 73e46170fa8231a73689e3ae2099c584f70f933d |
| ku9-live.txt | 22215 | 743c5d1596cdae94296da57eb0f3823f7dc2f83a4587f89b6f35e646e44fe771 | 3fb59b02434ed39661023405a256405a516f72b5 |
| live.m3u | 34537 | aace8e091cffd6c6edb9a7aced9d98cba5429e055ce8f545b19f5d7968a3377f | 6e8e805d59a38f9c9c90ebbbbf2ea9a32ef063c1 |
| ku9-family.txt | 18002 | 690bc3f8f79eb57ef180f366c3ea42f883be9db027e67479f0dcadfa55b8e822 | 3ad348d109974f46ab4b4771b156696ae24c8c28 |
| live-family.txt | 18002 | 690bc3f8f79eb57ef180f366c3ea42f883be9db027e67479f0dcadfa55b8e822 | 3ad348d109974f46ab4b4771b156696ae24c8c28 |
| family.m3u | 33729 | 6ffd732fe201678d847810b4ef698d832ec093ab55676bb4e9643b026418956a | a85b11cc97834e2d055b0bc6d1854d9c1f08f967 |
| final-publish-report.md | 11019 | 0a5d877ac89e2ba501195f5fe65b66a6f1497aa5a325f585edbebf534d662270 | 28187c406fd2a3fe86cc80ace7462e345e98a179 |
| coverage-report.md | 2200 | 71c6a84fb2b39294f70dc0da558663eaf1677c020638b91f8de6ed4caf93175d | 015f7f5596f1679731dcdf554b8fd66726b2ae15 |
| quality-audit-report.md | 4687 | 249458c61842a3be0318609e47ca8c25285390feec2c9da960aed937f437e494 | 5f010377b9928e5610b280ef594f2b6c7c9f2b39 |
| publish-guard-report.md | 1589 | bf653452a2982373be83d70859c422856ff150c8b7bf16a35fecb6cf0c70ee80 | ba03c278097096f409e1bb28929dadf31879e7a5 |
| published-recheck-report.md | 31142 | c35d47c76346dfcc9f77fd3ed2223dba7ffaf6f1ba72bc4195b158a0db6ef2a7 | 9db1d5aa885b729f14dea55d8884c240cb6ec4e4 |
| source-report.md | 8172 | 75c4ae19605f556169a123930397d4201bebfcb2acb0de16b33f7213dd0e888d | 5907be2a003388a061f4f1e3d03f224c992809e6 |
| check-report.md | 8172 | 75c4ae19605f556169a123930397d4201bebfcb2acb0de16b33f7213dd0e888d | 5907be2a003388a061f4f1e3d03f224c992809e6 |
| curated-report.md | 1831 | 8c5eaf5730a5bf5a62254f2dddcf15df44ee30ed44c22068e7d88d695e3ad825 | c06cbd5903e4e4982ed93d7298224cf6f7fc3b5f |
| sources_status.csv | 4239 | a1bc1ef52c431c01921a526b88f28a963cb0853d84044485499ab33e019e7d24 | 5b3559c95ee1bf4d8803792c39f1605f3139b50f |
| tv-coverage.m3u | 48792 | 0c90eac51a19beb26845e5933c5a442a6b401ad22c615dab11370073c9aba7e5 | ab134a15a526ae1cbddb9eda07845e788e34b9ef |
| tv-review-report.json | 18622 | 8947c912916a20666dc22999ff0c8b09ab11c8f1e7fc74d3bc4cee27bfc1d857 | 84762d7a67826c1d80a21aaba10cc681f13e77e9 |
| tv-review-report.md | 10687 | 46e3e58133a0fdd5d71ea9007c0f13e812ab3c640d49af70bcc64bd95f5b18f0 | df8f83635e1977f3add5b11a859e7c512dd412aa |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
