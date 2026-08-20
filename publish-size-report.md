# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2015147
Unique payload blob bytes: 1457594
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 466305

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 155435 | 3116bfeb7294831d7192321a86eaa87ef9136d235a58ba208584d34f2e8aa49e | 90afa4576a31c05009b3813352a2835087f690ba |
| live.txt | 155435 | 3116bfeb7294831d7192321a86eaa87ef9136d235a58ba208584d34f2e8aa49e | 90afa4576a31c05009b3813352a2835087f690ba |
| live-verified.txt | 155435 | 3116bfeb7294831d7192321a86eaa87ef9136d235a58ba208584d34f2e8aa49e | 90afa4576a31c05009b3813352a2835087f690ba |
| ku9-live.txt | 155435 | 3116bfeb7294831d7192321a86eaa87ef9136d235a58ba208584d34f2e8aa49e | 90afa4576a31c05009b3813352a2835087f690ba |
| live.m3u | 279113 | 94721994ab118ed021cc4cf7d8bf0d5ddc368a2a1676b16c551e506f100f4895 | 612c20589f6cf6776ae1e6d7952633b117c365b9 |
| ku9-family.txt | 84667 | fdd741efe6740ca2fa0438857c8737ecd3b3af21d08d937273f413155377e6e6 | dda65702e0da8a04f7b4abdb50490937b3d16292 |
| live-family.txt | 84667 | fdd741efe6740ca2fa0438857c8737ecd3b3af21d08d937273f413155377e6e6 | dda65702e0da8a04f7b4abdb50490937b3d16292 |
| family.m3u | 150204 | 57dc04445c89f3bca847b3ed647f9f5fc39af7bb528279c319529ad03ec5cced | 56916fe4a1a738d97ebeb9e5c64e7ccbf6d285ff |
| stability-history.tsv | 719583 | 74132230a789b8dd20c9bf472d7d8a53b7f32e492cb26c112094ac058a3d569b | 43951aab512cb5a2e6284ea68687795ff9482669 |
| final-publish-report.md | 11623 | 281a98152f891f245d051b4078746d7515e19d5c2bf7de88d6f51fc5441c621b | 05a5b9e8e8d26fca664a77fda1cd6744504bf37f |
| stability-report.md | 11978 | df5780812ffef43582d42c22d977401571f9e492761ac59f6349cf699221dcd2 | 03cac5da121e815c2daaebf896802c8aa5f887e9 |
| coverage-report.md | 1291 | 135a5b23a205c52871c21870099e62c4ddf51177e37e3a15e3e6fbb2a4564464 | c721b50ca93852ced3f6558dce035cb76fa4b8a0 |
| quality-audit-report.md | 2161 | b048a87f7db80d7bf60f1e06453f7b2d014ac895c891e4e1315a99223ec4b4b9 | 8dcb6b307499eb824f019f811458e81ad3222ef8 |
| publish-guard-report.md | 1148 | 176222ea4b80f56c3a800735eed60efcf3e6d7c108532160c8fa2ac8ea3b54f9 | feb0f7b24193730b8c56ee0a03ce730c95b3ac2c |
| published-recheck-report.md | 27352 | 3b9f62aef4d63229f236386534692480a20b2204eddde2c85e6d04733cefc15c | d2da83d3897e1bdd5d6387630fda461996415e0a |
| source-report.md | 6581 | 20af3f3341cdc60551565c5dc18a5622fc0077adce465ce2756906907431aeb1 | f9bf566e8b8564d6a592b7558c74d06649da4972 |
| check-report.md | 6581 | 20af3f3341cdc60551565c5dc18a5622fc0077adce465ce2756906907431aeb1 | f9bf566e8b8564d6a592b7558c74d06649da4972 |
| curated-report.md | 3324 | 036cdff3a8f17040e44f869ba0e47bfd7d88869da02ee3d8c76cae750c3f3248 | fffcb5eaf6d2cf53eabfc2537d7e35be95a9e103 |
| sources_status.csv | 3134 | 5f6d686fdb8b3ef6e823c9c76770bd9316fbb7b73daf518c793baccf6b913a13 | 6db2ec367cc1ba9878ee9760c2e27fd07f6a1e2b |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
