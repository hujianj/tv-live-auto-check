# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 246967
Unique payload blob bytes: 199526
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 26318

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 13159 | 7e15663899f3ea1910afb0c4ffe2ee818807ba47d6a1e4981d5088b8917e8bce | 71dbd562eb747bb4feeb95e5f1646983767059dc |
| live.txt | 13159 | 7e15663899f3ea1910afb0c4ffe2ee818807ba47d6a1e4981d5088b8917e8bce | 71dbd562eb747bb4feeb95e5f1646983767059dc |
| live-verified.txt | 13159 | 7e15663899f3ea1910afb0c4ffe2ee818807ba47d6a1e4981d5088b8917e8bce | 71dbd562eb747bb4feeb95e5f1646983767059dc |
| ku9-live.txt | 15216 | f04d3e2f553c2e6ffaaeb88e7fc151a0dc73fbc6114471e2a86866fee002b32c | a57caa456c4958f69a559cf0b7fe1f0c9d3e0e3b |
| live.m3u | 24664 | 959c6030ce74f89537bb78e79b1d52afd11e36e38049b43c53a06cb931a773c3 | 1cb18d824b927c96d3a646902fba6350e92f6ffd |
| ku9-family.txt | 12875 | 14fc2b8545f251f510ae82f1336a051d252cd9f9b6a309b5b7e66315892974e1 | 69da5a5b4c45d0b66de0f6cc8e1f017d3f90e93e |
| live-family.txt | 12875 | 14fc2b8545f251f510ae82f1336a051d252cd9f9b6a309b5b7e66315892974e1 | 69da5a5b4c45d0b66de0f6cc8e1f017d3f90e93e |
| family.m3u | 24132 | 8e894cc4fbc44531271fdc5805248ffb33b2b1acf63d7ec08b1bea4ba8156238 | ca5e049396ec81e67a542b92c237a63adefcb82f |
| final-publish-report.md | 10666 | 66fda5a15d5f33dcb81fd1dedc7d44b33188224801b766c05c73f4664d238c50 | c723eb158e3622d0da5b55cf71e4b2fb82d1b6f3 |
| coverage-report.md | 2200 | 4f533e55577f18244f13e6ff882b0d58177d9eda766a238f09cb6774dd778bb4 | c533c582d196ca983b9ceace826b96306813a806 |
| quality-audit-report.md | 4694 | e6c5ee968fe6bf52e7b8333752497e239408b4a61a418a82d715d8051993dd16 | 1d8e71aa7144821893f94e4952ca0bbe6cebe623 |
| publish-guard-report.md | 1534 | 9ab9e718593b7744e04ec9e6d97905c950138d4ea9879583f1987dda917c12e9 | 99e7d464068a4abcc3f6b6d6a55f2b997c8936e1 |
| published-recheck-report.md | 25406 | 94b4ad879091453bae4fddf90d3993993e1b75efdeacecde13bcfe8a922be9e5 | 2a3d020d6179d7be350edfedb7570a9c0ba083e5 |
| source-report.md | 8248 | 413ab2620b1db18dc8e78e839cb7322773e95e0f0274b2521e09700cdc2e2d36 | 9881e0ea74188209be49d38fb1f272164b94d068 |
| check-report.md | 8248 | 413ab2620b1db18dc8e78e839cb7322773e95e0f0274b2521e09700cdc2e2d36 | 9881e0ea74188209be49d38fb1f272164b94d068 |
| curated-report.md | 1713 | e84bb690f48ef1c40ea4556167ea67392369f1d212d5279c73c74cba017037d1 | 071c935b237286f577cb20ccea7a79b92fd9ddff |
| sources_status.csv | 4240 | 09adbbfb062b98dcdb68b36608abab86e29d939206bd52a8d1e1fbf30a5adf7f | c12dd71949e99dfc9d60d10fe50e55c181417a91 |
| tv-coverage.m3u | 34016 | ffdd462685c6bfc6d5591a7e8c12cfdee5cfca7ea4481338effd2f5f58859606 | 31e167bac13170dd83f5ee032ad8980d73514109 |
| tv-review-report.json | 10886 | 5d87fb65bc90124ac148a02a15a7d733a04cbfadc739a0b279ee3f18c72130de | 46e515b89095dce3c23ef5cca968b845bb98ba8b |
| tv-review-report.md | 5877 | bd9cd0687197b712d8c23355b55c0cc0a3cf95aec45c7b54d6b60d3503fbaab6 | d2df67544c0ae8979b52841f614297ededb7490d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
