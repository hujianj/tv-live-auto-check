# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 339983
Unique payload blob bytes: 274568
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38474

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19237 | b3e9b53f1ed0f8b591a93cb07a269af44a33a598c0cc728f67e9be1d9fe981d8 | fb7bd63af9954c15c4c78607000fcb1a157a8cf0 |
| live.txt | 19237 | b3e9b53f1ed0f8b591a93cb07a269af44a33a598c0cc728f67e9be1d9fe981d8 | fb7bd63af9954c15c4c78607000fcb1a157a8cf0 |
| live-verified.txt | 19237 | b3e9b53f1ed0f8b591a93cb07a269af44a33a598c0cc728f67e9be1d9fe981d8 | fb7bd63af9954c15c4c78607000fcb1a157a8cf0 |
| ku9-live.txt | 22746 | 02ba880bcfd66ddfb7db0eba3282bd82106d98fd00c26a5823eec23fe3f992bc | 6111c1dc969b3359d0b6f31fc9c7df7776b8e265 |
| live.m3u | 36937 | f5b7f7671c082aad6be379d1bf56e521942ca3e70927f342e5ff6193ea9cdfaf | 4311a9871cf98e76dcc05017ad73909d692b8b1b |
| ku9-family.txt | 18801 | 76c089772ae241d3caddd212183a7f733d6129de81532b33ea8d9aa5f9a5e2c3 | 8d77572b44a630b0cd9243d6fb3e88f4241669ce |
| live-family.txt | 18801 | 76c089772ae241d3caddd212183a7f733d6129de81532b33ea8d9aa5f9a5e2c3 | 8d77572b44a630b0cd9243d6fb3e88f4241669ce |
| family.m3u | 36129 | bde8544f3236c8bba610dc36fd9eccf0b3b141f2089c998691e6a171f8c106c6 | 133f469cbcbb6ac4515cff71008ef1f6f27ba2de |
| final-publish-report.md | 10903 | 60cc6df529b6bea834d001551d9cccafd0faa916cb9d2787b8301d083a449938 | 0c332c2efa77f29b78959e90a7e8011ff956f040 |
| coverage-report.md | 2190 | d0e9750ed94e160349cdec7fedd75410118a703be6d3357bd6c878a8b575046f | f958fcdd434ea035c70357380b33c709c5b18d35 |
| quality-audit-report.md | 4653 | 95ac031323b640082ac52078c82c944218a7fd347b946eb3b45461d86098e688 | a0b0181cf01f57e0ebc081448e31c215a04d819a |
| publish-guard-report.md | 1532 | c652c518e55a8cf7a2f70484139185638e5ecb60b8785b19970a22548aae90e7 | ed0d107ea3867432884a2e15088a499a34d2268e |
| published-recheck-report.md | 29149 | 3e06caa6ff8fec8445d4c3c81ac2dadfc789d1bbc31f6f8fb0d16255ab41b13d | 9321cbe300b7eaaf11c2d418880664d55f33a583 |
| source-report.md | 8140 | 134f5bf09b9c2b1588d6e942954eb258d6a168e0b4f5714385e5b6f70b5ede7c | 36994ddf7dc87e00ea7b1099ec84c276a10c3846 |
| check-report.md | 8140 | 134f5bf09b9c2b1588d6e942954eb258d6a168e0b4f5714385e5b6f70b5ede7c | 36994ddf7dc87e00ea7b1099ec84c276a10c3846 |
| curated-report.md | 1833 | fc10135a7477406c34c7afd3fbbf0bc61badd1a4533b3b99b8aedb7e0a73364b | eb0066a0220bb861863552edad4a7df70351a579 |
| sources_status.csv | 4242 | 1f69d2a03c04824ae74c8eb8ae9b4d7746899904121faecddb1fbb711940845d | 128796330d8e6d45601214505d41784cf16a424e |
| tv-coverage.m3u | 51409 | d79296ef222595fd126f0e5f3c6248d2a7c5555c718ecf62cc2f763aae6b57b5 | 0be9ffbe95e0e5481fe171b4f40680b1fcb1cf09 |
| tv-review-report.json | 16911 | eef86f778a65ebbc099af4b91babad1733dee273d122bbb0f13e02a4f1ba67c6 | 21107ba8b26019209cdaba4fd5c45d37643f43b1 |
| tv-review-report.md | 9756 | 5a1e853a34bd606fef9ada0f274d98039a451036eef434c8541c448df4a5fc2b | 0215dd31d4fa31a38b617ab96c6d2c37f3613309 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
