# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1831172
Unique public blob bytes: 1194396
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 631107

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 210369 | d5ce6b51600bb54e86b9a2948448f3b3872dbfc2f62857ef262b96b565e5f9ca | fc5e3115bbf95b7aca33fc3fc60606fa2bdffdb9 |
| live.txt | 210369 | d5ce6b51600bb54e86b9a2948448f3b3872dbfc2f62857ef262b96b565e5f9ca | fc5e3115bbf95b7aca33fc3fc60606fa2bdffdb9 |
| live-verified.txt | 210369 | d5ce6b51600bb54e86b9a2948448f3b3872dbfc2f62857ef262b96b565e5f9ca | fc5e3115bbf95b7aca33fc3fc60606fa2bdffdb9 |
| ku9-live.txt | 210369 | d5ce6b51600bb54e86b9a2948448f3b3872dbfc2f62857ef262b96b565e5f9ca | fc5e3115bbf95b7aca33fc3fc60606fa2bdffdb9 |
| live.m3u | 373402 | 7c8b4e91ab91db8665be2b11b438090bde14d4a4f45143d06dcd47e7bff5256b | d5d7e7324299e97ef80a93261975a2df420dadfb |
| stability-history.tsv | 547398 | 5c34dcc47cb42f0e08c5f32b68eba8781dbba933d76018dbf37407efc415180a | 9b64a225bb711ea768e8abf334969d37a7aee668 |
| full-check-summary.json | 17769 | 6803824f05fc56e83a6f9bcb542a51b535912af18a904fdcbedb24c198d603e6 | 6cb150ada9e85131d67783420d30481b641e3d5c |
| final-publish-report.md | 11612 | e053bfc1f9230d61b10a7ec555561b2f712408ffb51e2e14efb9c69d827b53b1 | fd59e0db4a7a418193bd3c3fe09d70fdcb546650 |
| stability-report.md | 7791 | 8394422e86439d5decef1560d3cd3cb8265b9f1804e2d1d662a86ff66e33e859 | 5686a957d8ef460538da535648fb98ee8ce280ef |
| coverage-report.md | 1139 | c8034a0429f4f9a0c0cb0cf36d08b577d4c65f62497d7415f02595666a0307e9 | 7714187fbe3e722f793239a40729701edd3c3066 |
| quality-audit-report.md | 1190 | 5160c7344025a950d9147a25b6315c94b5e175c358b77e326848bb48a40e6f48 | 7ab856ac52abf726adebcad862e898afb83e850e |
| publish-guard-report.md | 798 | b2f888c2f5124d7f22d36212ddba7e6b1afb0c9cf08ea95eaded961bbadc6518 | 003a905cac8ca648b9708beb5d9993612c97f82f |
| published-recheck-report.md | 11087 | a4e1e8956af60be4d4cf5766cb7470651d79eb980632d9f0cfe454475ab45002 | 167488374f5f633611b9008ea9d731f8da713daf |
| source-report.md | 5669 | 0d18de4a8b6eed743e44c5d763900b2a134d7130a54cab53d3faef2df0ad0907 | 966311fb62aa866dfb623c27cb9e262ce1c73534 |
| check-report.md | 5669 | 0d18de4a8b6eed743e44c5d763900b2a134d7130a54cab53d3faef2df0ad0907 | 966311fb62aa866dfb623c27cb9e262ce1c73534 |
| curated-report.md | 3723 | 0db055a0a840dd641d5d9ab39c9aa8c2ccd3c357324b857ec66839b2a24f48ea | dbe45f831a42d185e33e9bd67e5f11b8768ed81c |
| sources_status.csv | 2449 | 762e098ec4cacc351ae07eaeaf12bad121207d4ac221a14f40e28c995f63bf1f | a80adf05a5768f89580a28274b12941003e82661 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
