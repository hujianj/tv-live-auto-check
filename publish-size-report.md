# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2377663
Unique payload blob bytes: 1642594
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 631809

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 210603 | c85b8f749bd4817de33b85bcd2b04514b64b5e17a3faeae68013604ea747b7d6 | bd6a1e6b845ab6bdf7c34ba30995a59c83c1301a |
| live.txt | 210603 | c85b8f749bd4817de33b85bcd2b04514b64b5e17a3faeae68013604ea747b7d6 | bd6a1e6b845ab6bdf7c34ba30995a59c83c1301a |
| live-verified.txt | 210603 | c85b8f749bd4817de33b85bcd2b04514b64b5e17a3faeae68013604ea747b7d6 | bd6a1e6b845ab6bdf7c34ba30995a59c83c1301a |
| ku9-live.txt | 210603 | c85b8f749bd4817de33b85bcd2b04514b64b5e17a3faeae68013604ea747b7d6 | bd6a1e6b845ab6bdf7c34ba30995a59c83c1301a |
| live.m3u | 379522 | a6bde6d706fea4ebcb08c53575acd60da5cd148f15ce43ab800c92c64ffd317f | 336ee426ae369010dc1c04505023f26e9699b73e |
| ku9-family.txt | 97376 | 7ac7ab17c48de5195c99e81750583a3e2ffee078d9d4d758eec0605e89a1fddf | 891566a0350e23a3c5c9b4b6544aa6f625f268a0 |
| live-family.txt | 97376 | 7ac7ab17c48de5195c99e81750583a3e2ffee078d9d4d758eec0605e89a1fddf | 891566a0350e23a3c5c9b4b6544aa6f625f268a0 |
| family.m3u | 176822 | b663de835b8ed983d8609194fe513bb4abb9bc01e094db839c1def41522176f6 | 0f8ded04d624b8cc7f60f7fd3f96169af613db96 |
| stability-history.tsv | 708345 | 19d393d287fd8b96565f885bfc887ecc164ddf05fc6eaf7ee8b7bf8f37286077 | e92a2f05b13b7937ace4c97af894b24ada082548 |
| final-publish-report.md | 11721 | 00c0bf3d1244f351b4082d6d77affe5874c2cdf5d4ebfc2a9b96743c9adba660 | 48c25b60cb78736ad1e306e2a67472a693ae8c5b |
| stability-report.md | 12508 | ea6e380917287fd3369192b4395c3a0cfcc2dd7ac6909579c97f15369403f76e | 264adc8407fb8b80942b1e412bac282364dc989f |
| coverage-report.md | 1291 | 1038f740ec5d63bbe590c138b2fc668e37d638e9b11b29ec38988b18acf4a675 | 1e66c9232ff70ba90a972ff1ef7f2a7337fe3ee6 |
| quality-audit-report.md | 2181 | 13ac04aea669110a4661e220e889bebe5707ae504c71210789b036aa063671f4 | 0f53bfd8a919584c5613ecf45e015983c3e49313 |
| publish-guard-report.md | 862 | 4eecadc627753e451b495047828abc344253c542c545c2232c74bca0e4467881 | 5254c7c5c848fe43419a2b889d264e96e6ebfe36 |
| published-recheck-report.md | 29348 | eea3c92b56a76562ca76c054f614a28c768651c70415da5ed402915e807fc29f | 66f4825b87c4a2d5a906d192c42e680ad66db959 |
| source-report.md | 5884 | 9d473c9b397347e82c9ffdac4dddf854adf6e10568b7daf25709de58827fe2f8 | c7632fbeac02e6765e4674b2ab0c392c7584b7ea |
| check-report.md | 5884 | 9d473c9b397347e82c9ffdac4dddf854adf6e10568b7daf25709de58827fe2f8 | c7632fbeac02e6765e4674b2ab0c392c7584b7ea |
| curated-report.md | 3475 | 7496f4f9d72239dab3a2fc02a9ffc371fa30f4b0a0a0536bb37a451ae396abd1 | d2226277037a1d86293989c229fb72268e9f46d2 |
| sources_status.csv | 2656 | 87b06be9f51e3b0065e7d06d904ee8a37877767c1096cbac0c00730cf22a9e23 | c5614ab1b15854daa112466656256c160deb0ecf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
