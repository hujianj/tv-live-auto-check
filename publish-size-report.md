# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 278315
Unique payload blob bytes: 185545
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63642

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21214 | 6c8338664c45627a703e3c5aa567b91b3675e59ba4ee8a0dbad968fdf35fbdf1 | 52cfa2fe651a39f1e76d734b55295d81f208426c |
| live.txt | 21214 | 6c8338664c45627a703e3c5aa567b91b3675e59ba4ee8a0dbad968fdf35fbdf1 | 52cfa2fe651a39f1e76d734b55295d81f208426c |
| live-verified.txt | 21214 | 6c8338664c45627a703e3c5aa567b91b3675e59ba4ee8a0dbad968fdf35fbdf1 | 52cfa2fe651a39f1e76d734b55295d81f208426c |
| ku9-live.txt | 21214 | 6c8338664c45627a703e3c5aa567b91b3675e59ba4ee8a0dbad968fdf35fbdf1 | 52cfa2fe651a39f1e76d734b55295d81f208426c |
| live.m3u | 40638 | 494ea98d8061196b8db5f3fee198aab4de0d456d778d258853e4c6484ccfe1e4 | 7a533a6ed5dcb3a2a6bc7c688bbc3443210e6d3c |
| ku9-family.txt | 21062 | f80edeb36a35029c9a18ac946375c3eef904ba2c257a1442b49ecb6225c53235 | b583286d6af68164b135bde7025ed2c06d399787 |
| live-family.txt | 21062 | f80edeb36a35029c9a18ac946375c3eef904ba2c257a1442b49ecb6225c53235 | b583286d6af68164b135bde7025ed2c06d399787 |
| family.m3u | 40362 | 7734ff247ba37247660a3dd400a1cd9a7e7e87b79c2d04007a5b5c0322c6100a | d3d9a66a68dac447bf401e448a4947a73cf0f104 |
| final-publish-report.md | 10776 | 49e3ff97c2b1daf2607bb0da0bb767a220d00d66f191969208c26a6c69b5d0eb | b473921ad4aa17618f6ee050a0cbe393a5cbb4ed |
| coverage-report.md | 2225 | 6d323488febc4a4ccfb9efd16830c717b2f483cf4d271581aa635f959e5a50f2 | ad8544076e9bd3281731b489d563b58c030f8258 |
| quality-audit-report.md | 4720 | c8825a604e9465bb1d39d1379ef341489055645ee3c79f099d8f9f2ac2640333 | 4415712b4cc23e1dbebdb1d66c5fec1212d23050 |
| publish-guard-report.md | 1600 | 3054d854e9ed34094b4e5d488f656d8f9a97fc1e0f3137e1e8bd8700007b9493 | e1a75163424c8de8837fc6b86a9afc5e1e8658f1 |
| published-recheck-report.md | 28983 | 4fe56f6718366ec58abaa97a8eb059beb8ef431b0f0a80aa8c28d35327bfe3a3 | 2e5285f99f1db42769b9d0e1b6cab932c5d4b7ab |
| source-report.md | 8066 | e3905e6f0461f1053860098fe66307576254f0c3b4bc91ee49603923626fb38c | 6f7c2b149181792922402081a5fbe6cb8ca3fe57 |
| check-report.md | 8066 | e3905e6f0461f1053860098fe66307576254f0c3b4bc91ee49603923626fb38c | 6f7c2b149181792922402081a5fbe6cb8ca3fe57 |
| curated-report.md | 1767 | da15bd807410cd5f2b7c55925f7fa8af99cd865585ddd9001c287db17acea07b | 262f93da9aea694e3ecfe8060d0bcc297a8cc1ae |
| sources_status.csv | 4132 | aa50c93a0ba7ccf740f78b95eecbc55cfef9d438b767bce365f5f95b77939ded | 74ae3d22d5304006309e27313114b41397c18766 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
