# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 358633
Unique payload blob bytes: 285817
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 43344

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21672 | be23697c939bb2a2ccb5962a7fdd038ddbc5a0ee7a7d018c9cc71fdf42fc8ab4 | 288543e5a1a5e2196b83b3f89b3998d76fa3c7ff |
| live.txt | 21672 | be23697c939bb2a2ccb5962a7fdd038ddbc5a0ee7a7d018c9cc71fdf42fc8ab4 | 288543e5a1a5e2196b83b3f89b3998d76fa3c7ff |
| live-verified.txt | 21672 | be23697c939bb2a2ccb5962a7fdd038ddbc5a0ee7a7d018c9cc71fdf42fc8ab4 | 288543e5a1a5e2196b83b3f89b3998d76fa3c7ff |
| ku9-live.txt | 24088 | 390e9061dd6a3862b5583c7a1cd0419b7128dea3240c3972a67858f3c511f36b | 81235a4fb6b16f63799405f32fd070db4ba14a8b |
| live.m3u | 40790 | 30a2a71a90721b75be7b395a2d664ad5fc436f9e53489a6b5a6ca68c557b729e | 2e2544c4207ec1f806ee70556b88dd5a33f48b24 |
| ku9-family.txt | 21311 | 544adaafdee0a7ff8e6259ad99ab6ad4be2f969e3a709331766e4f731cd242d2 | c5839fa93da76699426730a95a19cdb7eff91f07 |
| live-family.txt | 21311 | 544adaafdee0a7ff8e6259ad99ab6ad4be2f969e3a709331766e4f731cd242d2 | c5839fa93da76699426730a95a19cdb7eff91f07 |
| family.m3u | 40119 | 0abe957ea88757faefa37b7e2e7bf8911d80e0c8ee46cfeadd1df9f8915f8aed | 3c09b779e7f54a2700c3a8d62d5c8e4768449b79 |
| final-publish-report.md | 11108 | 6c59cf85067278b95a1f0b200d4bc2b6b1d69c8d843036ebd02c9817e49841bc | e60b991d5758f52377b9269917693639c85984aa |
| coverage-report.md | 2195 | a184d5015ce6947282fed97cf0c6a59717a3cb6221408aecfc95cfa0a430ce33 | 4e5d9071156463ca1251238a6093acd6fc8375bc |
| quality-audit-report.md | 4693 | 639caaf55fffcd9895764f710152fb63a239c240c77065baa5713b475d09294f | afed0a8a83054051e33052fc8406012b9b44f340 |
| publish-guard-report.md | 1561 | 35e85815c412c0ebfa26b059703eb1403bf7a777cbd500a7cbdde1602c5cc83f | 14475635ecf5047e82d4be2e570d7d75ab8ea63e |
| published-recheck-report.md | 30126 | 8cd47fc8bbdbd60370e31d4cbe22e83018545b818733fc5b616da93fc0f615d8 | 784a95ad32177de15d5a3fea11c609c6a8e3855e |
| source-report.md | 8161 | a8f2d879c286f0f07cb49d6a32968cf9fc4119e216af47c192250bfbb4f48879 | 22fe5057a08a359d9c7a388df6c61f603ce74605 |
| check-report.md | 8161 | a8f2d879c286f0f07cb49d6a32968cf9fc4119e216af47c192250bfbb4f48879 | 22fe5057a08a359d9c7a388df6c61f603ce74605 |
| curated-report.md | 1896 | cc7ca11f39b576d227a81c5f4101c964ed8371fe4d8ee36181dec975c3fe14f4 | cde39bbacf9ee7fdaa63d5f63075f5b8dd1e5e14 |
| sources_status.csv | 4239 | 374fd08291c98e32c7e0b4828602b6569dd5abfe21b86d67e808e4c83b57f51d | dd0f9c52912eb119dbfb889912c5df9b3c3da60a |
| tv-coverage.m3u | 53806 | 1be2ef4bf8b249329a17a574bef80c64ad02c48318cf98f2936e38a4baa98c7b | 4fac0e3e9c7432c413086f7f78e4c02b49ede64b |
| tv-review-report.json | 12921 | 8c785fda073c893452637d6bb6d9e6f6605c7482f6cfd77dde05d51e75b7eb2c | f77d7f264c44ae095a3e7037e00077e582c8671a |
| tv-review-report.md | 7131 | 4352d9cc8c8333c657bb21ea7d9737229871a054df148e05d7fe033d5e68994a | eb88097fe1971ec432de9d404c84ba422e7ad6bf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
