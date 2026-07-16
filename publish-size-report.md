# Publish size and alias safety report

Status: ok
Working-tree public bytes: 2085008
Unique public blob bytes: 1448248
Max unique public blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 525450

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 175150 | 72864e0bc54c57aecc4b4ad19e977c3a8dc23120730d8b054ebf8718e19ba910 | 35f826d8ba95937721e0747d0cc50de557cd1296 |
| live.txt | 175150 | 72864e0bc54c57aecc4b4ad19e977c3a8dc23120730d8b054ebf8718e19ba910 | 35f826d8ba95937721e0747d0cc50de557cd1296 |
| live-verified.txt | 175150 | 72864e0bc54c57aecc4b4ad19e977c3a8dc23120730d8b054ebf8718e19ba910 | 35f826d8ba95937721e0747d0cc50de557cd1296 |
| ku9-live.txt | 175150 | 72864e0bc54c57aecc4b4ad19e977c3a8dc23120730d8b054ebf8718e19ba910 | 35f826d8ba95937721e0747d0cc50de557cd1296 |
| live.m3u | 317713 | 2b163127929ffd8b6347454ff6cf8e7b50fd9f73b8e710debd02d0a19170bdb7 | b80f768bff3dd1020dcc4eccda5b5ddc4a187a73 |
| ku9-family.txt | 105695 | 3f1d2fcb69004529a4c47f29087290f2fbd5bbf2ca34668465682d9272dbf2bf | 6bc1fe628adfd582446307fccf5a55a0ea771b10 |
| live-family.txt | 105695 | 3f1d2fcb69004529a4c47f29087290f2fbd5bbf2ca34668465682d9272dbf2bf | 6bc1fe628adfd582446307fccf5a55a0ea771b10 |
| family.m3u | 191829 | 60ae36e4dfdf8b441b7bdd5edb28c969e7f015a8312cc65125dd08dc644d7bc7 | 8e5e54ba0919c774211fe86e0e78a3ab4e9c8445 |
| stability-history.tsv | 592046 | 003b76f61ecdc72d45f8cbdc4b00dda11fe13b2ed907b1e04f84a4a615944735 | d1b52d62ddf63136ccc5adb0927869d6b7cc4a4d |
| full-check-summary.json | 18167 | 1b9d9e46abfd4e8e918f57274d7ecd94c946c862ccbebdff06b460fd38a8b42b | b5232b970590d79e6caa1ed9a3d90b73fa012cff |
| final-publish-report.md | 10852 | 88196cc0e344ad7b77420451a194060bd39ad229f4e47583f855934e26342111 | 9604a25f4fbcae73a97c9994c118443f10a6c657 |
| stability-report.md | 7769 | 7fb564d46a48d8f5a7591a924e7c9b83d830719ee1870b0fb26495c318f6931f | a7be0ccba4b72810727eab96db0ae3fbd5554e77 |
| coverage-report.md | 1123 | 863093058d183fb0fa931c24d4a0fb3702c1eb1ee46f0428cea0737b58c06cf0 | 04cad92da5b3211340509944375e9dd918734809 |
| quality-audit-report.md | 1250 | ee6cfbef417b127ec1520e08f173e96fcaf1dff30b98286e3f530d41bcdaa00e | 152e17c19744843f73f901f3bfecd5445d8d3664 |
| publish-guard-report.md | 803 | 1191d59054bd9ef6e4528049a965cad3337c46fe555081d6c25e787b9be1d4f5 | 15eef22fec4b8032b0a4dfd22929d7ec4fcb9752 |
| published-recheck-report.md | 14130 | 5bf284ef7bd0feea5e5c92ebad09b59265f4836cf688820c01db0daaecf9c1d7 | 838405a05cfc18bf471c88eaa85d65946a93ae38 |
| source-report.md | 5615 | 01d6d61b71af60e79fcb5db6bf9200c2f1636ed72bd98dfa3d4e18f6ad4b227b | 416433629fb286280b240ee57087f49546634ec4 |
| check-report.md | 5615 | 01d6d61b71af60e79fcb5db6bf9200c2f1636ed72bd98dfa3d4e18f6ad4b227b | 416433629fb286280b240ee57087f49546634ec4 |
| curated-report.md | 3659 | b70603396239c9d06716ad53360255412ef30d7324951b996547d746aab165e4 | bafdef45fff243175e5776d856c2f4378a5d3029 |
| sources_status.csv | 2447 | 37f4a53a15e8d37687a9952ed59e79b05fb2fce44a8d415feeb61fd7c32cf9f3 | 681cf0ff329051a4b20ec79456574ec1d36a1e07 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
