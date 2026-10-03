# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 283099
Unique payload blob bytes: 188207
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65301

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21767 | f6bf96d0a41d46527ccf06597f6ffd6f091836237ab38d637a20d9a636321d28 | 2322c89e2441bf21695997a2ad1c461a3fa8ea5a |
| live.txt | 21767 | f6bf96d0a41d46527ccf06597f6ffd6f091836237ab38d637a20d9a636321d28 | 2322c89e2441bf21695997a2ad1c461a3fa8ea5a |
| live-verified.txt | 21767 | f6bf96d0a41d46527ccf06597f6ffd6f091836237ab38d637a20d9a636321d28 | 2322c89e2441bf21695997a2ad1c461a3fa8ea5a |
| ku9-live.txt | 21767 | f6bf96d0a41d46527ccf06597f6ffd6f091836237ab38d637a20d9a636321d28 | 2322c89e2441bf21695997a2ad1c461a3fa8ea5a |
| live.m3u | 41861 | 7a56dd2f9f348888b16aae7078872a47e245b28162b4bf3f55b12e438809276c | 334f0d23c90aacd9cb04e1b3c0243c37aa6bb57f |
| ku9-family.txt | 21495 | ae7205f6ec915bcba6fa5e553de39c0a6cc0f038ef560ede126536a149295d6b | e10c8ed446eacd865428b4c6b607fed95dfa8125 |
| live-family.txt | 21495 | ae7205f6ec915bcba6fa5e553de39c0a6cc0f038ef560ede126536a149295d6b | e10c8ed446eacd865428b4c6b607fed95dfa8125 |
| family.m3u | 41341 | 1f588cd0c6ddeee2e10397703ba59ecbaf79f86bbdf653c41b8556059c12181d | 17304f697ea4528dc493556807399bfe3e7e2040 |
| final-publish-report.md | 10717 | 603301c04a007c6b224af4481bfd6dda09d84e552391d76e19f0cfbba2cf8c2e | aedb519d0737b1892f77a5c693ed70004ed6d183 |
| coverage-report.md | 2225 | cd213be854904d6aeb98fddf1e6afeec462849a5037468e754682d914fb0b318 | 20a688cc6e46f732a97ae90ee342b6961bad845f |
| quality-audit-report.md | 4724 | 40c2c0ffff572f530ee0698e44b24379ccb3136dc92a188016487e2b48d9cf18 | 152fb818c0a8cbf539d54dc8b317f3817b54d914 |
| publish-guard-report.md | 1556 | b9103a140cf55d3dd51ec5c23ef3f2e9ce72ae5deab42a36271b72a523aa2e5b | 58101e64eaf845df63a0f754eb623845edc206c1 |
| published-recheck-report.md | 28484 | ce492347ca2fa08575b306b39adca5a67d1dbbd4041f36e24f79dd43219c6252 | 37c1249e493ecad3dadaf13f6ab471726a9c1dc3 |
| source-report.md | 8096 | d1c499f8755c526866b88b365aaef74aec71d0e66c95eff60c69778a7bdd4b0e | a5f1dc0afab9b2bebf140a204677ac7ca06adecf |
| check-report.md | 8096 | d1c499f8755c526866b88b365aaef74aec71d0e66c95eff60c69778a7bdd4b0e | a5f1dc0afab9b2bebf140a204677ac7ca06adecf |
| curated-report.md | 1804 | 260f78c05464731c3cde4133e19ebb823c82a840bcb185be44f80fead9560244 | 1ca9c423cd17a27dcf77d1af59a48a5fa8a77679 |
| sources_status.csv | 4137 | cf81c00802ef8811da2414c54083f2fbdee6c28a0861eb2870818697ef7c7387 | 1d1e110dcbeb864847e1c2f184ddca0c2b9bcea6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
