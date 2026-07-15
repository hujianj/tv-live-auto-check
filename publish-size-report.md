# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1828658
Unique public blob bytes: 1191407
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 631596

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 210532 | 88a927107ae4b052777e5abfccdab771b833b15c5c64476d0b1c1c6a228f39bd | 7ad4fb83b2752d153e3c484086bff68a6a9ca6d6 |
| live.txt | 210532 | 88a927107ae4b052777e5abfccdab771b833b15c5c64476d0b1c1c6a228f39bd | 7ad4fb83b2752d153e3c484086bff68a6a9ca6d6 |
| live-verified.txt | 210532 | 88a927107ae4b052777e5abfccdab771b833b15c5c64476d0b1c1c6a228f39bd | 7ad4fb83b2752d153e3c484086bff68a6a9ca6d6 |
| ku9-live.txt | 210532 | 88a927107ae4b052777e5abfccdab771b833b15c5c64476d0b1c1c6a228f39bd | 7ad4fb83b2752d153e3c484086bff68a6a9ca6d6 |
| live.m3u | 370644 | 0a8c0a3133b93474295b2759a308cf49f0fe94fb3e3ea943d3e448f2e365a0a2 | 9eb763abde5c13be8141be88665fbc5ce7541313 |
| stability-history.tsv | 547297 | 4f621a1e2ce04c199306ff0c806429b6d15eec6aac1ca8ca13335ba030fb2bea | 315b3d65c66f68258c472b5f955bb5bf8d85b070 |
| full-check-summary.json | 18131 | 4d3ae9546551a1dff3d4df7b8dacb906ab90b572d5851e0fb3d2fc242b2ba8b1 | e17168cdd4a31402ba862d6ece5b4e1eb10aeee8 |
| final-publish-report.md | 11690 | c7924b0474daaa4651ddb697f6076b5518b5a17833ffe571537b0d42a2ccd18a | 663cef7c66c5c94ed64eabbd0d0299d1b7baf5c6 |
| stability-report.md | 7654 | 17a8d3a57db02493a038fe2df119a2d21ba8b705ee3746cab6b4f5f02bdf299a | 2aa0a38fb6608fe65dfdf9099b2649b2c1170cf8 |
| coverage-report.md | 1139 | 05c6f8e37fd161a3451ef96744b8c86442c1b9d5dcc567a5a0b184a839b49de8 | c842ab7fee022592f7ab206789b80ae6930c62a0 |
| quality-audit-report.md | 1335 | 68246af9d488dcc55427b3052ed1fd1a99a7a6b7c7908f5c05ffab17b6d0ed47 | 32b53ac5a5be6ef2857082d48cc8fb6ccdca59df |
| publish-guard-report.md | 797 | 11dc714ff2fb2a3667d052b4245326609f5857b95180861f1b1f7d2c45c90818 | b53817f6850d15b25b33af4b33d4d9c71dfe4585 |
| published-recheck-report.md | 10402 | 6a41e458ece21a75b055300b5adb39bb6d98c337e8c5fc10d718dd7c038e1e84 | 8056a158a0fb4d6318bb37ace06d97e6a9e17220 |
| source-report.md | 5655 | b88b454d29b04e2947107d620bb160b07ca491da113699b8d3557ecfbfedaf13 | 4f0eecc91cda09c0c72dfc5a23c0a9ada303eac7 |
| check-report.md | 5655 | b88b454d29b04e2947107d620bb160b07ca491da113699b8d3557ecfbfedaf13 | 4f0eecc91cda09c0c72dfc5a23c0a9ada303eac7 |
| curated-report.md | 3682 | d0ab6318e3a6be5385c33a16e438bccb5e38df6e2e133b061a919065f2f7207e | c6626d5037356fb7ea24d37d3dd21212e4b71068 |
| sources_status.csv | 2449 | 0ff27d3463293f499b4bc8d695610fa52d9d3a0c9dcae8423a0c06303de7f238 | 70059dbf5c609fef54228bfb7dc95ac0200e8389 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
