# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2377737
Unique payload blob bytes: 1643797
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 630126

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 210042 | bf0da96f0fb37994374fd0dbf4f836fefb3d483de75540464642113a1bc596bd | 6ea1167a90aa9f8f6ecc7a61d11d0aec6e7add1b |
| live.txt | 210042 | bf0da96f0fb37994374fd0dbf4f836fefb3d483de75540464642113a1bc596bd | 6ea1167a90aa9f8f6ecc7a61d11d0aec6e7add1b |
| live-verified.txt | 210042 | bf0da96f0fb37994374fd0dbf4f836fefb3d483de75540464642113a1bc596bd | 6ea1167a90aa9f8f6ecc7a61d11d0aec6e7add1b |
| ku9-live.txt | 210042 | bf0da96f0fb37994374fd0dbf4f836fefb3d483de75540464642113a1bc596bd | 6ea1167a90aa9f8f6ecc7a61d11d0aec6e7add1b |
| live.m3u | 378167 | 7871ec3f2783122b919adbe6bee75736f0731cf066243a1005e4289e7d101735 | 07c62be7e3ff8fccd2def6c8289fdb978e910c57 |
| ku9-family.txt | 97923 | 6c624df8376a507432b3ccca96b5fbfefe854f6ab23128ce540da8d2ff662d5e | 6172a3a6c7747191545bcfaf76cde70028d06be8 |
| live-family.txt | 97923 | 6c624df8376a507432b3ccca96b5fbfefe854f6ab23128ce540da8d2ff662d5e | 6172a3a6c7747191545bcfaf76cde70028d06be8 |
| family.m3u | 177275 | 072fe40ad0cfdb9c840a0abc38623aa3a79b36eaa67c9b5819d13955ec661c75 | 7d2ed782763bb31c2af40fcbc3f480d168e93179 |
| stability-history.tsv | 710055 | e3cc3438d382f63b8f65d7f7518085934a5e1ec857434c8fe28a6d0ef19b2a4f | c776801bffad4207737176dfcd4061f2aad4fe52 |
| final-publish-report.md | 11733 | 5df5ff525f603c21d6f4cc39650b0183f49eb7a250b8b249a710fe90ee1483d4 | 50f33455a05ac40c00b4b0b05cc20ce0da2f0d70 |
| stability-report.md | 12666 | 26b9407692975ee785ca678635bba03b7b529235298bcc7b37debe6db3d97d18 | 4f9b360d7c880a7e0b6902d8df55ee8e44c8b528 |
| coverage-report.md | 1291 | 1038f740ec5d63bbe590c138b2fc668e37d638e9b11b29ec38988b18acf4a675 | 1e66c9232ff70ba90a972ff1ef7f2a7337fe3ee6 |
| quality-audit-report.md | 2182 | fde96eeb886dcb13ab4dba171cf9bc2c5ebaf0df473f603c2aba732547340c73 | 4a53e68e86e525fe8cf93607ac1c865863f524b6 |
| publish-guard-report.md | 863 | 4def60b7c4a0b1f4d9b4882cf881283e0990570dbb4e9b958f1d2bfc00facb08 | 9d5d9a691b46a8de3e9e917e60286731f45e2403 |
| published-recheck-report.md | 29516 | de734822ff9d709e3397cfd32645f7093b54571733cf1bf05fff75e443648534 | d9512b2669fa4af074a30ee65a039fd79db3e526 |
| source-report.md | 5891 | b2df24c98aabcec34a8cb40d88e9583639a2caaa9262b791a6f05bac53ddfa23 | 48198eb1a673ba05abd8b6d9829c539a1bb7227a |
| check-report.md | 5891 | b2df24c98aabcec34a8cb40d88e9583639a2caaa9262b791a6f05bac53ddfa23 | 48198eb1a673ba05abd8b6d9829c539a1bb7227a |
| curated-report.md | 3537 | badadf70419ada5fd2172618f9599030df231427a029a02a78e7ca47e4430381 | 9531c386ece94df5967759846d1cb36a175811de |
| sources_status.csv | 2656 | 87b06be9f51e3b0065e7d06d904ee8a37877767c1096cbac0c00730cf22a9e23 | c5614ab1b15854daa112466656256c160deb0ecf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
