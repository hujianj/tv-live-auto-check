# Publish size and alias safety report

Status: ok
Working-tree public bytes: 2279151
Unique public blob bytes: 1541927
Max unique public blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 622470

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 207490 | 2f3d8a1b024fbd9a0212aa309b7e2489f98a1838bf06f66f84ba3af2ead54528 | 5998ea1c051473fef9e0b5da13d04dd27d325d53 |
| live.txt | 207490 | 2f3d8a1b024fbd9a0212aa309b7e2489f98a1838bf06f66f84ba3af2ead54528 | 5998ea1c051473fef9e0b5da13d04dd27d325d53 |
| live-verified.txt | 207490 | 2f3d8a1b024fbd9a0212aa309b7e2489f98a1838bf06f66f84ba3af2ead54528 | 5998ea1c051473fef9e0b5da13d04dd27d325d53 |
| ku9-live.txt | 207490 | 2f3d8a1b024fbd9a0212aa309b7e2489f98a1838bf06f66f84ba3af2ead54528 | 5998ea1c051473fef9e0b5da13d04dd27d325d53 |
| live.m3u | 367012 | 35ce767ecb4b3be9881bb914b7b3bd3e719817acad4615aafa68bb079ac30a9d | c636cd180bb47062a528c3d2340d655168596a06 |
| ku9-family.txt | 109079 | 4309645470ea94d60f2d1176d18d045bff807ed25ccf2b6f822d1ed7342abc19 | 555c674b4ee529b4b75934b25e61896e22fc4e7e |
| live-family.txt | 109079 | 4309645470ea94d60f2d1176d18d045bff807ed25ccf2b6f822d1ed7342abc19 | 555c674b4ee529b4b75934b25e61896e22fc4e7e |
| family.m3u | 196192 | a70ac1000d7d36e488c8f69e6382698968c078b7ff27458723212cb673fd277a | 78c9a0d05934e99ea286071aeda84de5116f6553 |
| stability-history.tsv | 598429 | 84fb4e5216a79a2cb53b2c8e6799aee8155280d51e46c267fbc845e6fbfa93a6 | 6942a78239225944d6e9efb3acd0238849be0364 |
| full-check-summary.json | 18363 | f622bc1f52095adbb935e95e4b8f8e84b2fbb4f58b7c923ad0ccaeda4cbe40d4 | 33ee5e70a96cfc2535aaeed2aac8b1adf619576f |
| final-publish-report.md | 11624 | c7018bb6bb7e666ba6e60b02a240962bbd2f34c123c0645288eeb2e4867ed452 | 7b30fed3ab35384cf9c26b0c8a4fc408495bb966 |
| stability-report.md | 7720 | 7c5d5f8f60c695f41ec6d74c0eff49ecc58d4b67b47a920a846e33db688f2c13 | 472c829d93f992d9280002cb549f4c9f554c0c3c |
| coverage-report.md | 1138 | 99122b2e59b1ef4e6d8d0582474fb2c6c3895f47968d7126db0a546246a77fe5 | 42b4421b6ac435bfc4e2a91ff12f0af3a3145b0e |
| quality-audit-report.md | 1211 | 2787c9e988597792ace9aede124d5b3633129145181d152f9b24af810be779c0 | ef5c2db83ddf7953f2e90489e7be34b4daa979df |
| publish-guard-report.md | 807 | 5af5d18ea91b2ee2de25e6049db6655b08cc3da82cfc879e74486886750df453 | 66bf12f8b1aaeaa7b816c191039e0a1f76072a22 |
| published-recheck-report.md | 10995 | b75c0e84ddcfc995bb01c131f2e769a46c97429206d4906ce01e61f1edbc2e39 | bd3cf5f77b241b182b2301c4f251d20e1e116b59 |
| source-report.md | 5675 | 7fa55783e870a63aa3ed7e495e7f80672120ae7af80f37fd6a3eba46f8753ed2 | 20328d03eb87d2df5635bbc57dc2986fdea207af |
| check-report.md | 5675 | 7fa55783e870a63aa3ed7e495e7f80672120ae7af80f37fd6a3eba46f8753ed2 | 20328d03eb87d2df5635bbc57dc2986fdea207af |
| curated-report.md | 3745 | 9b56953fabfb7a78b6f4b4a39fc51594761aeb6279cb5b9286197f281715571c | 5462c994e7447c0c0d78bc7638c101cb0dc1f3ac |
| sources_status.csv | 2447 | acb98353262ab4acaadd84d872ac77a9d84d3cc1039136d94f53e4522c91eb29 | cc59a633cb01da627ce0f7b0d0ff75c0e3ccf6d7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
