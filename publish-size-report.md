# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2114984
Unique payload blob bytes: 1531274
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 487920

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 162640 | 0c06d745ca3ce2f0f2b06e6dcb1140d8cd00e67dc7fa57871dd6faf2dfe41581 | b77505b4a8bfad393f2bf69dcb8fc0aebc7323be |
| live.txt | 162640 | 0c06d745ca3ce2f0f2b06e6dcb1140d8cd00e67dc7fa57871dd6faf2dfe41581 | b77505b4a8bfad393f2bf69dcb8fc0aebc7323be |
| live-verified.txt | 162640 | 0c06d745ca3ce2f0f2b06e6dcb1140d8cd00e67dc7fa57871dd6faf2dfe41581 | b77505b4a8bfad393f2bf69dcb8fc0aebc7323be |
| ku9-live.txt | 162640 | 0c06d745ca3ce2f0f2b06e6dcb1140d8cd00e67dc7fa57871dd6faf2dfe41581 | b77505b4a8bfad393f2bf69dcb8fc0aebc7323be |
| live.m3u | 297203 | 55f24d518fb7740744071d5b664afcc8f8960f2b1e4d423ee5e95af58303c276 | bd9051c1bccebfc3f88326a8d73eb36b26457efb |
| ku9-family.txt | 89256 | c0f9bd789979b88b209d35cef15cddc50f4ccfc0594f56d92da69611a361bbb0 | b9367fe7aa0d3fea96f744416fba30f7502fb49a |
| live-family.txt | 89256 | c0f9bd789979b88b209d35cef15cddc50f4ccfc0594f56d92da69611a361bbb0 | b9367fe7aa0d3fea96f744416fba30f7502fb49a |
| family.m3u | 160891 | 6204ddff04c833a27ffe31903253dcdea584f3a63bbddaa078c4a41c165d5a63 | 483cba19d43c2ce9d577c0826e9da9a129d2e9b1 |
| stability-history.tsv | 753695 | 12b6b3dfb51a2ead5c573b172fa6a16e44c531bc4ef94b79199c39a2781b4742 | 61551088f8e091066fd8c1c5b1cd02cf49e32cb3 |
| final-publish-report.md | 11734 | bfa05a69570e0c401b88f306bfc4c04fea3277b1fc30ffaa348cff0f9810d75b | f9b5723915e31cde5f7ace961a2d6b75e33f7f6d |
| stability-report.md | 10906 | 2adf239416db39202042f010263864c730da25b7d91f4b3910b9a2adf21997f5 | 2a3c291f69ec61d45d170a829c2d3e683f470086 |
| coverage-report.md | 1291 | 538b545c146dfdf733ccf4f9592de52ba4799181aa484fa923658f8926d6b838 | 9fa8604d2e4fd155d031a9b96d9e1c4502c66ab0 |
| quality-audit-report.md | 2134 | b735845b79dc95a174b2a76c3682abfde7b03624ce7203878e44b6cb658746f4 | 028c301288d7079112aa77349c8f672bc661a453 |
| publish-guard-report.md | 1117 | c63554d5be93f232f79ee44f7caa8df266c9603ea3a8aa698f70dccb30410e71 | 4e3337348ce3f6898e379f80b1d346b1a1228a8f |
| published-recheck-report.md | 27313 | 469c9b38e866f47cdbf5f32dbcea9574ff3a0eab14849619065af6957b5773ff | a3578f8e6849d35505ec72b21b3ca531595fa1a1 |
| source-report.md | 6534 | 32e5de1628ad72ef8899659ba09d80cdfe69b27c56f966fa678b01d297b2c79f | 66c475a8136e0dcef4d25cbe4346f0fdca066bbc |
| check-report.md | 6534 | 32e5de1628ad72ef8899659ba09d80cdfe69b27c56f966fa678b01d297b2c79f | 66c475a8136e0dcef4d25cbe4346f0fdca066bbc |
| curated-report.md | 3458 | f753750840dbd94e9997ac126cbc928fbae050738fcb4d8b948a2fb558265a96 | 9808634d7d97b25adf76dcf2292d9c10a2a49f89 |
| sources_status.csv | 3102 | 6deb98346e7a6c373e869591151e929ef31a2e210ebdf0c10d936b2ee7244df7 | 12e0fb28532c841ca814ff79d840cf3f9d72ae63 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
