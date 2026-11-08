# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 348279
Unique payload blob bytes: 282241
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38832

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19416 | 603303c81354da4fdcba6a853cb0031f3edf61a659216d3d13deff60e2f9aad5 | d77f7010301ac83313cb41b1bba38a7cf62f765c |
| live.txt | 19416 | 603303c81354da4fdcba6a853cb0031f3edf61a659216d3d13deff60e2f9aad5 | d77f7010301ac83313cb41b1bba38a7cf62f765c |
| live-verified.txt | 19416 | 603303c81354da4fdcba6a853cb0031f3edf61a659216d3d13deff60e2f9aad5 | d77f7010301ac83313cb41b1bba38a7cf62f765c |
| ku9-live.txt | 23246 | 80ba71c9532cf4dd324c8b1d47f290afffd093bac505724fa018e5a97eba3c48 | ff58a72f89ffdbc33f31a739a48f6468c59d5dd8 |
| live.m3u | 37240 | e16ba1fc5be70adbaca2c76b2d19c4c96bb80f50d1b7a0f83b9b0b079ec5b3b4 | a80a24796d41c2f7dd750037e3cd74cafa50527e |
| ku9-family.txt | 19037 | 755615b70df65563633b01a73bf9e3ecdd74ce51c7c2a83e296c0153b94bc72e | 15c6bd286d8f1e4ee25148b3c4693c52e177ba97 |
| live-family.txt | 19037 | 755615b70df65563633b01a73bf9e3ecdd74ce51c7c2a83e296c0153b94bc72e | 15c6bd286d8f1e4ee25148b3c4693c52e177ba97 |
| family.m3u | 36551 | cccacee2b9aa56162a5e931d347e730809c08390036b01439ed879067d6571d9 | 3e13c3efc90c51bb6c105244a54fb70be0ecd1c2 |
| final-publish-report.md | 10939 | 8a39610bcc494f861986356e02fe589f6d08ae8e869883d88fdb19a8633c28a6 | a932022133baccf6af81efcebdec279f5d297dbf |
| coverage-report.md | 2205 | 702bbcdea1a78b3830d2726a7b23ef94d533ee2a0eb26b7869ec91a48235eb58 | cc9d29779b5b0f28dc918bc923d40a9e1e01d870 |
| quality-audit-report.md | 4683 | 36dcd64bf0bcd9c1079864bde58ac29ac648ea5fbd84c03a3377dbedb9d74d5f | 969ef4d2b47493304983aca5543006abf4252256 |
| publish-guard-report.md | 1583 | 8e19ca398741daae3917399f9091063220b32aafdf52868a53b6ce4013bd56c9 | 8f3897bee10430c8b6514b3492793f51e0bbfa91 |
| published-recheck-report.md | 30580 | 26286ce9b1b6c418f15c96e9004801f80afdd03361fd3c1b686fed0fb1294b3e | 125ea96560ec5acb85ee62130c1dfea764972356 |
| source-report.md | 8169 | 22004a3d808f0cd6ed57be1fe7f0ffc80b6f9414af20bfde79072546968f4ea8 | 6b7ca695711f4da7be28eacdc25811027060091a |
| check-report.md | 8169 | 22004a3d808f0cd6ed57be1fe7f0ffc80b6f9414af20bfde79072546968f4ea8 | 6b7ca695711f4da7be28eacdc25811027060091a |
| curated-report.md | 1834 | c00fdbe0eeb66003e80b5a91b7b69f580a7f4f5e15929c10188860389d23f562 | 1007d3ad1e363d604edd2f2990feedcdd2460b13 |
| sources_status.csv | 4240 | 010cf31373f183c963cc6feccf8b646cbf9a40242d156e14fe685a2b2a0d3bf3 | bb6c88ded5592273e735a958b9029ffd98a2ad67 |
| tv-coverage.m3u | 52534 | 93837e5305a874035583ce6bdb38ddfd0e24e8d3e2f252bd49a15abc1868da1c | 3f3acf57df460993395d413e3fce886f1637da0c |
| tv-review-report.json | 19057 | 34de2850f33b7bf110d010cdc96fab947eaea8afbdc8d4a32c74f25c2d75e754 | 41278bf54664fae8aabaa5a235b56eba90663205 |
| tv-review-report.md | 10927 | 86c7fbd14b2bab975a2722cbdd4ba087b65e30a003bc2886b7c5311902f28010 | b66a61fae92d600ef19752d5b01f891e825c5fba |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
