# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 279642
Unique payload blob bytes: 185902
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 64428

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21476 | e234382e1d1349c6ee03b04686caaf7e3e3aa951028d1197cf255730bece4963 | fac5b79faf22dd74c0f0726c377163178adc6481 |
| live.txt | 21476 | e234382e1d1349c6ee03b04686caaf7e3e3aa951028d1197cf255730bece4963 | fac5b79faf22dd74c0f0726c377163178adc6481 |
| live-verified.txt | 21476 | e234382e1d1349c6ee03b04686caaf7e3e3aa951028d1197cf255730bece4963 | fac5b79faf22dd74c0f0726c377163178adc6481 |
| ku9-live.txt | 21476 | e234382e1d1349c6ee03b04686caaf7e3e3aa951028d1197cf255730bece4963 | fac5b79faf22dd74c0f0726c377163178adc6481 |
| live.m3u | 41321 | a857fa8b937b3cbb3194b61a4283719d792bf3650d827c835d28e386981276bf | d71b29ff5773186cae93ce9f2e5eb9ea9584a2da |
| ku9-family.txt | 21211 | 7a384d27a5d6f4f97ea10b754b88bb22099473d23c14bf249fb16cb460d0c585 | 5800b9f9003f8fa65de0dfcf1e4d5aae3073468f |
| live-family.txt | 21211 | 7a384d27a5d6f4f97ea10b754b88bb22099473d23c14bf249fb16cb460d0c585 | 5800b9f9003f8fa65de0dfcf1e4d5aae3073468f |
| family.m3u | 40808 | 49d8ba157a614c91a1620a7b352ebfe523d67db94f2978112b320a0b16b8b935 | f84f90e4acd01497082c69f4742a190a199144fe |
| final-publish-report.md | 10643 | 675fb8c71ce83db7dd78d4e1754cb8085b1edfd5d066bf39e4b7360b19b065b8 | 95c97c3da8b73e8948e9e4983f4dc18f10455d8b |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4730 | 7e951f5f3e719ea55838ed92aa734114fb8254b85062c6ad5fd86b7f53acba95 | f2370a935f0e77de597085a8a1e1f4e8615bba62 |
| publish-guard-report.md | 1607 | 38efff3e607dd5060f8c5473fefa698df6bdc5fd5010c619625261c02a50d7f7 | 84dcfec93a0b47de66f72b7eb5844460acd8ad46 |
| published-recheck-report.md | 27834 | 982c62999baca58145961e706f21d9e7ad7208f123a12540597ecb8d904ec602 | 3efae7ca186941e9a7e5518c3933aed4dc0bd955 |
| source-report.md | 8101 | 386afe1176a6358382b460afcb7ebbccdd33ccc9db12c56ebe049638b3d1ea74 | 543e57dc9ca57cb4907beb4de98189b15fd9ab80 |
| check-report.md | 8101 | 386afe1176a6358382b460afcb7ebbccdd33ccc9db12c56ebe049638b3d1ea74 | 543e57dc9ca57cb4907beb4de98189b15fd9ab80 |
| curated-report.md | 1804 | dd8c6304cdadc9320400812aac897ed8125616bd4d5c9cf7af6bb0ae6644ee99 | f6383a6bc10c9926a180a032ba9117822710f3f5 |
| sources_status.csv | 4137 | 54b1f3c8f4800e58e9baf35eebccebcf1dc1d853a75ec6984de1cf30b1935971 | 7c033ac6b48b5976e3441a0c2454e6c10a24521e |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
