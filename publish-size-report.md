# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 258287
Unique payload blob bytes: 172254
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 58626

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19542 | 93d470ef976e0df8b7889240c2c8c3abcf0ee7c6afcc2385571cb414cf8a9c37 | f1c626349f0f8d2095a15fb39556e875092154c1 |
| live.txt | 19542 | 93d470ef976e0df8b7889240c2c8c3abcf0ee7c6afcc2385571cb414cf8a9c37 | f1c626349f0f8d2095a15fb39556e875092154c1 |
| live-verified.txt | 19542 | 93d470ef976e0df8b7889240c2c8c3abcf0ee7c6afcc2385571cb414cf8a9c37 | f1c626349f0f8d2095a15fb39556e875092154c1 |
| ku9-live.txt | 19542 | 93d470ef976e0df8b7889240c2c8c3abcf0ee7c6afcc2385571cb414cf8a9c37 | f1c626349f0f8d2095a15fb39556e875092154c1 |
| live.m3u | 37343 | c2208c2b7ac9b5cff6ad6bf5925f488aa3dc9152f1e89856e36bf2c6727de35a | b6b3a4b737783ea943786c1f9ed021734c9c826d |
| ku9-family.txt | 19277 | 5291ee70c99c1a6c1b0c07d3bc5a69ed7a2fd2c7c8938754beb96e92c39731dd | 91fa53adab4e1df0bddd7ba3d045a60719bbdd35 |
| live-family.txt | 19277 | 5291ee70c99c1a6c1b0c07d3bc5a69ed7a2fd2c7c8938754beb96e92c39731dd | 91fa53adab4e1df0bddd7ba3d045a60719bbdd35 |
| family.m3u | 36830 | c7cc01703d7c9a6192a244816bd810d69b0f0a3bcce1cc4b1b018a45899d3c2a | 58990a1a580f1d203751cfe54b7013eb6a3d7640 |
| final-publish-report.md | 10757 | 6005e73e8b76221db0065421c4b51fe06e0938c06b638b71a08bec306981c404 | b1de37de26284636d53c8f00b7a4057db81ccaef |
| coverage-report.md | 2240 | 8ab9da48344064ac435335ed832b73b60ca784476b3df5eb72eca563da516d5c | 5affe4146214b3eaccf8477bc76151698e50d343 |
| quality-audit-report.md | 4730 | ac64f8e87e0be3b278d060c8a0c346d0f512e0652176bb3ebd55ce57d6b9b3cb | a3409de49265102a1f864e82e2dcd0bbb787aaa8 |
| publish-guard-report.md | 1615 | 8953a02c997c37279b586e5e024370a3a9f9b074a6a52877589c6ac90f9d74db | af0acade5c42040220c187755946932304d57bdd |
| published-recheck-report.md | 25852 | f3f9fee42cf11b4d746a5977e244aecafaa2573dc8693d5ccde2628211530819 | 714e5d1016582497a17bc288fdf6a079b14d9882 |
| source-report.md | 8130 | 0a7c1df671b89cb9f86197333ef0ee989bdf58d519e0e2a8a3f1fff02c34749d | ac2e9cf80c41c5b64fa6e15d653f36f0fbfdd07f |
| check-report.md | 8130 | 0a7c1df671b89cb9f86197333ef0ee989bdf58d519e0e2a8a3f1fff02c34749d | ac2e9cf80c41c5b64fa6e15d653f36f0fbfdd07f |
| curated-report.md | 1800 | 416cd470620a077c529cd29e4b7b347cf17b92aeff5090f32be9be9820f32511 | be8d19f065010244938af3f80e20f83e1958a8fa |
| sources_status.csv | 4138 | 0083adb4339663f0217c7a26f4712f0bc0adf8891f6c4d6c987e6e1d7a762b52 | 5930d613f8317e255728554620efca754a93ada2 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
