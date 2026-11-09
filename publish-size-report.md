# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 329665
Unique payload blob bytes: 267232
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36446

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18223 | 1429fd549cfb159b483211a2f0b856e67b9607adf6051e7cc4f497f7808fc197 | f326dc985e9034e5205c2f9f0de994629266e1e0 |
| live.txt | 18223 | 1429fd549cfb159b483211a2f0b856e67b9607adf6051e7cc4f497f7808fc197 | f326dc985e9034e5205c2f9f0de994629266e1e0 |
| live-verified.txt | 18223 | 1429fd549cfb159b483211a2f0b856e67b9607adf6051e7cc4f497f7808fc197 | f326dc985e9034e5205c2f9f0de994629266e1e0 |
| ku9-live.txt | 21881 | 1bef4f2745f627592aef8abb434bbc357278f93ec31d21a3c2e6a3bb708bbb1b | 73f7d43270d91bcd6740b42c0d13f4750fd16921 |
| live.m3u | 35014 | 46f49b03a8b9fbff29bd186857e47947f455c65f52d56830cdb86a3311b9142a | b336400d13c01917e492a8916bae16c58f9b9403 |
| ku9-family.txt | 17844 | 9bd0dc7871bf58483a32dd0daeb3cbdc9963d706fc6aa8a59305e8c7fb095942 | 964c92ab39af29b223c894fe1db544b0d598f7c7 |
| live-family.txt | 17844 | 9bd0dc7871bf58483a32dd0daeb3cbdc9963d706fc6aa8a59305e8c7fb095942 | 964c92ab39af29b223c894fe1db544b0d598f7c7 |
| family.m3u | 34325 | 7a56e54c01189c67bed7dc3aaafc66a324e5222642a6760e30a7771900c7b532 | b29c350f96c86b539e32a403e07af297fd398bd6 |
| final-publish-report.md | 10876 | 1ca58420147339f7ff5c96c7646e566e12f5160f694e29633fbb5c15626678a6 | c006b06de700e7328959247f1d918c7421e90378 |
| coverage-report.md | 2200 | 039e964dad6066602248a060824a2d77cbfc1f2141a76c75efcbda479ed89a5c | e6bdca0ea0051a2fee883a514e08135a1fa7ada2 |
| quality-audit-report.md | 4675 | 04e9748ca6698a03999d4e38cc34f0beb4756c8cbca8ed09603374868b8f98eb | da66733b3da4441d179b0de5b533aef53765fd95 |
| publish-guard-report.md | 1529 | d81b79eab331ac334cdf5dcae862d121ea7f1e298aaf4aa3f01a51a9b8432887 | 06c5695e097a10242164a04e638daa15080c0d65 |
| published-recheck-report.md | 29405 | 750a6e92b875b2f8e6903b3e2db0a2141b7fcab3158062a4e3c4bbb8721ab615 | 6c5e5380103a304c0670d733931208d843a8e18b |
| source-report.md | 8143 | 68bc2dc23a9ca94ad1d9084e80484b34b042de50371268bd55e116780ae1e65f | 785223b677a2cc4295d1e619ae9d8f91eb1dea56 |
| check-report.md | 8143 | 68bc2dc23a9ca94ad1d9084e80484b34b042de50371268bd55e116780ae1e65f | 785223b677a2cc4295d1e619ae9d8f91eb1dea56 |
| curated-report.md | 1833 | acaf792bb0978e4501a74f08b35ed6cab2fe870956512bdafefbbc20439e27df | d0a97ac8e0c0c6e5682692085d99de3349e11546 |
| sources_status.csv | 4240 | 9a3c0022878131641bfe790c44e66b396cda425021b831f74f76a25c23b13ed5 | 238d106d3802a628839dd847b87f65b5748f6658 |
| tv-coverage.m3u | 49465 | 3fb1971c0def76193ca1c46a31a197023e3c3a7e599aaf38c1392c7931acd65c | 765248ba591a07044539abdeea74c8c8159bcbc3 |
| tv-review-report.json | 17562 | e96c3e05a5a58d59b5d42da615b28d1efa3e69dca01894d361aa5eb2511e3149 | b5e7baca32975940bae57952b8af42ddb26302d2 |
| tv-review-report.md | 10017 | 3ded2780d808adb56c8d5707c96bf40c0d15069caba6016ffbcbdcbaaf22f163 | 4a2923932fd5f67c3d02045f783a08835b549e4d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
