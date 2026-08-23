# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2013602
Unique payload blob bytes: 1453504
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 469467

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 156489 | c5063062b3e450832f6d9a6296521ba63bb1f3426d9aace8bfe712caa77a3929 | 1d6bc8185f5df3e17e3a7c86664f52f6083d6ead |
| live.txt | 156489 | c5063062b3e450832f6d9a6296521ba63bb1f3426d9aace8bfe712caa77a3929 | 1d6bc8185f5df3e17e3a7c86664f52f6083d6ead |
| live-verified.txt | 156489 | c5063062b3e450832f6d9a6296521ba63bb1f3426d9aace8bfe712caa77a3929 | 1d6bc8185f5df3e17e3a7c86664f52f6083d6ead |
| ku9-live.txt | 156489 | c5063062b3e450832f6d9a6296521ba63bb1f3426d9aace8bfe712caa77a3929 | 1d6bc8185f5df3e17e3a7c86664f52f6083d6ead |
| live.m3u | 281993 | 530d9f9a17d6a54e8bc567c95060e2efa7dfdd329613711c619dedb9a0db8a73 | a7cf7c81a2a81e5432ac7dbb4d4f7e4f6bf18c99 |
| ku9-family.txt | 84071 | 5ec5013c25c02b4bef75aed599105bb88a70fb2404181eac48250d39f1c8f7c6 | 131e89ba009e6537f92f8c4a6b2fc9889ebb6c32 |
| live-family.txt | 84071 | 5ec5013c25c02b4bef75aed599105bb88a70fb2404181eac48250d39f1c8f7c6 | 131e89ba009e6537f92f8c4a6b2fc9889ebb6c32 |
| family.m3u | 149453 | abe3474bb34f82014fb41199faa5ff84262246e16acdb6b9702c66eb8ea8870e | f34f0740e0bc0346baf82c816b2bdecad4a3a97c |
| stability-history.tsv | 713735 | c138de42047efade2ba4d2196f131037466568871d992d0434f4f3ccf1730be6 | 3689f50c541cd3494fed9781e3f0714c54b5b1a2 |
| final-publish-report.md | 11807 | c66daf8f673ad10ecade0528e69336d9aa53efe47535210479b58e99c24a486e | ab0a054e3a6d09a3ff31bc0e7dd8ffae2882b083 |
| stability-report.md | 11686 | 1caf5d696584a2d05f8fc7aa4b6e77bf2aeb57df28c8bf5ceaa21e0459d8dd06 | db2c068c9a4f6da382dbcfb8a0d0ad1fb21d4007 |
| coverage-report.md | 1291 | 03adfbf36f34804edb4924b160ba79c5a4b500d67fbeafd5a2693bf7a4764acd | 7b285a524a364da68c5b7ea4019094cd90e6b16d |
| quality-audit-report.md | 2062 | fad5594247ae8d4009346e0608cfef581d33c0352bf3f0928767dc7b493732cf | 45974b65aecec2a5e1e71fc857c2c407d2441f65 |
| publish-guard-report.md | 1151 | 7263d039af9c0916859b15aa13f6add8e9c25d4ef38b4e2c3ac05a4fe2fac9fd | 41d12b0826ce4113f847a2188c210c92893de71d |
| published-recheck-report.md | 26708 | c8ef998777683fa1d36a539f265d644aa122c93aab0892b1ea0618f57dc163c1 | 910a0b4faac2f5aeed8601bc6c1580a5f3393221 |
| source-report.md | 6560 | 6b37f81ce41e3faff1a6e9330f6f85f10c47c46156a881ed5545aca3907019a9 | 145598b4bb722da28bd32e3d36f65e5312b1f284 |
| check-report.md | 6560 | 6b37f81ce41e3faff1a6e9330f6f85f10c47c46156a881ed5545aca3907019a9 | 145598b4bb722da28bd32e3d36f65e5312b1f284 |
| curated-report.md | 3363 | 059a5f1e8b7c92174164d8bb3283b7482d5e91dfddad10bdecdbbf3646d62900 | a7f756d8cb422c3e18ac429661ca228f9b02bc60 |
| sources_status.csv | 3135 | 2dd7e59a1e8e90f604e5e923ec4037f35567022ac07d529ad45a70c6242d26d1 | c995547f7e6baf4f1b227e29048be8ece976726d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
