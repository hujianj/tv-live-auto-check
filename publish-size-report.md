# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 286905
Unique payload blob bytes: 190694
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 66447

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22149 | 54bef5215dd6f387706be73660478081ecf65911470d30389026d40de7736b4f | c5be24cf432e020a669c9095beb8f3595178cd44 |
| live.txt | 22149 | 54bef5215dd6f387706be73660478081ecf65911470d30389026d40de7736b4f | c5be24cf432e020a669c9095beb8f3595178cd44 |
| live-verified.txt | 22149 | 54bef5215dd6f387706be73660478081ecf65911470d30389026d40de7736b4f | c5be24cf432e020a669c9095beb8f3595178cd44 |
| ku9-live.txt | 22149 | 54bef5215dd6f387706be73660478081ecf65911470d30389026d40de7736b4f | c5be24cf432e020a669c9095beb8f3595178cd44 |
| live.m3u | 42634 | 2e55f5dc84655bf308adb0541e1f5146b85c45d3a9165074aec00a63072fdaf3 | fc8536389a7a7b7536c90780e58e06209551de60 |
| ku9-family.txt | 21727 | c23f5be7c8c5df0686f9103dbf3a76da58b5efc863e0efa0806286adeac51341 | 466f61b574e15f794c38e93a8678b3a1b288c8f9 |
| live-family.txt | 21727 | c23f5be7c8c5df0686f9103dbf3a76da58b5efc863e0efa0806286adeac51341 | 466f61b574e15f794c38e93a8678b3a1b288c8f9 |
| family.m3u | 41840 | 995049ca5b7d56fbccb704cc4f4a7eba8d153b1cb40a15938f1f53ac0cf26cfd | ce4b9f69fd2880b5d035eab6f93031b59a9391e8 |
| final-publish-report.md | 10678 | ba4965901deca3403c36d77014c8bf730d68b82e305b6358bd2718236b150120 | ec41d3fa5d31911dfe37e3470eab4f88dd0350e8 |
| coverage-report.md | 2225 | 7a73010fd3544f71b25402a46b6c56ecff50ba882925647f788c8db9fc413907 | 78481b0a1d24eaf4a0b398404e06719b2d0bd77c |
| quality-audit-report.md | 4733 | 410251427b06037eba27fb9da11d9fceb966ecf205edbc2f85be8fea82058731 | dadbe098d9a8f34502b1e65f10db60b1c4edb7ea |
| publish-guard-report.md | 1531 | 7c3b4de24583cdab4e33d4546cfc572e5394e609bb9cf111521fb06742e279ed | 2de2afe372abb36415acb74a59b0350319af76ad |
| published-recheck-report.md | 29249 | 0655cb87afc6d985c6e1e0804ae1b4713be8dba58b93d6658aed918b488c2644 | bab43953c232a31b08bce89442a53ee600a78774 |
| source-report.md | 8037 | b544554beac4248fd85ab79d170e8b2cdd9fe8ef4e5c23eb902523a5b9eaa727 | 1d37de0356c97ffef0bef380ff59b02fe26b2423 |
| check-report.md | 8037 | b544554beac4248fd85ab79d170e8b2cdd9fe8ef4e5c23eb902523a5b9eaa727 | 1d37de0356c97ffef0bef380ff59b02fe26b2423 |
| curated-report.md | 1806 | fd2ae006baf2ff9fc51615289962dccc16caaaab46d32a86b1399226d32da791 | 7de0ece285df75fbfc83abc02c84b12c2ee4fbec |
| sources_status.csv | 4085 | 2b92b8d3f389afe9be31bd1ce4c840b7426343eff79de4be3a39505fca201283 | 6864586309b2ee7f4cac5dec0fb1c2649df4a9ca |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
