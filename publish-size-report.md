# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2506291
Unique payload blob bytes: 1734885
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 668394

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 222798 | b5c20621bc8a2f0cdef73c33a64a0e204a13c3bca0584f634fe4098b19b77947 | 08cd25ae97922d68267e7d62a9d6ebb6d29b1652 |
| live.txt | 222798 | b5c20621bc8a2f0cdef73c33a64a0e204a13c3bca0584f634fe4098b19b77947 | 08cd25ae97922d68267e7d62a9d6ebb6d29b1652 |
| live-verified.txt | 222798 | b5c20621bc8a2f0cdef73c33a64a0e204a13c3bca0584f634fe4098b19b77947 | 08cd25ae97922d68267e7d62a9d6ebb6d29b1652 |
| ku9-live.txt | 222798 | b5c20621bc8a2f0cdef73c33a64a0e204a13c3bca0584f634fe4098b19b77947 | 08cd25ae97922d68267e7d62a9d6ebb6d29b1652 |
| live.m3u | 399015 | 389601c2fadad6cfc1bbd3c7293be401d23d770ab1b394f1eb628640aa56cf98 | 6929248c8adda0a6910647eb7757e4af4a99566d |
| ku9-family.txt | 97185 | 959838715d76b5992de1c4936264386d98afdacd36afdb76248617e452833a62 | 9079ffc8a6e71ede5f462c5fbf3a9120ed11cad6 |
| live-family.txt | 97185 | 959838715d76b5992de1c4936264386d98afdacd36afdb76248617e452833a62 | 9079ffc8a6e71ede5f462c5fbf3a9120ed11cad6 |
| family.m3u | 176203 | 9fd4af7528717f9f79f9a597f1a4b6fa1ef0e77a249a72edd42f4cd34123ff7a | 69d1dce5d7c113a9d7bbb54a7e80c318a64ed496 |
| stability-history.tsv | 773313 | bd5d3cf2f494f939db762b8a565690001991bbba1669e976d3d94fd5390e7031 | e2a2aedda60fd783b84186531fe0c271510496ef |
| final-publish-report.md | 12520 | c562e27709b2767263c6924489af1a284093ffa28ebc9b412c5ec30c89dc3a35 | 12480ee1b6087102469383a200c355faca36adfc |
| stability-report.md | 10263 | 69972f7eb15bf882aa99f298e25235549fae1fcda742cd0b8ae38dec282cadab | c19832d067fd803a777df4e91191c509d96e4e45 |
| coverage-report.md | 1329 | 5b03928342225e214cd6cc25cbf179f881827dfcf1fb525415f0ecb94012c814 | 3f7afee1306b086d3cfea1ae3440fe5dec2f0755 |
| quality-audit-report.md | 1435 | d01a492846efd3cab07554004961cd11657aeb60bcb7f4fbb6a233bf1f5af491 | 8ef17c83f6ff6ca8510c34cfaa7b2b04dae31787 |
| publish-guard-report.md | 791 | edd559bdd39ba4c1be6e6149e45cf272b4a90450144bd9de89236bee96f2577c | db333cc99632d3844360c0a4a7c49c48121cbf31 |
| published-recheck-report.md | 28022 | fc39b4159214d6f7bbd9214d92c0ccd0e8b0f9284d5059c4e8ba2fd84c91d79b | fdbf901e2092a060a2693ff0b9737e49222302f2 |
| source-report.md | 5827 | 375099fb02216769f4d2fad90a9c383a878d0e49b5ec5f30cb9a2ca1b686cc53 | 2a2ed0f73d24a11ae45ed25df34fef48669ca93f |
| check-report.md | 5827 | 375099fb02216769f4d2fad90a9c383a878d0e49b5ec5f30cb9a2ca1b686cc53 | 2a2ed0f73d24a11ae45ed25df34fef48669ca93f |
| curated-report.md | 3581 | 6b007125de162d5fb03b0034a626821af27163469c36a9a59f0317708b268d65 | 6566d53456a6e428e50f65d041216056577dc6b2 |
| sources_status.csv | 2603 | b012ceb244340df3a750bbf8a15de4974fa574c779eaeebf6152f91e26569183 | a6109a10e7c65cf572b97b9da53eb5472425eeda |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
