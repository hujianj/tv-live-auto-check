# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2494240
Unique payload blob bytes: 1726929
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 663960

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 221320 | f8c29f1cdef1f1d3dcadbcc240294ab3cf4f927e39cb426d3993b56c9a653672 | 55d270ebecc2737e216b9721882423bffec076f3 |
| live.txt | 221320 | f8c29f1cdef1f1d3dcadbcc240294ab3cf4f927e39cb426d3993b56c9a653672 | 55d270ebecc2737e216b9721882423bffec076f3 |
| live-verified.txt | 221320 | f8c29f1cdef1f1d3dcadbcc240294ab3cf4f927e39cb426d3993b56c9a653672 | 55d270ebecc2737e216b9721882423bffec076f3 |
| ku9-live.txt | 221320 | f8c29f1cdef1f1d3dcadbcc240294ab3cf4f927e39cb426d3993b56c9a653672 | 55d270ebecc2737e216b9721882423bffec076f3 |
| live.m3u | 396797 | 7a88111adfb28f67d7c429ae898cb3e8fc7382cd2187b833eedd2ace8b29685c | abb8fd046e7cd031b6d45430de1f4063662103d2 |
| ku9-family.txt | 97503 | 67938b6f913ad952574960f92c92800da64a49882e40f9d60499e178542fc5bb | d3a476ea097615dbbe78c2052509f91aff054c80 |
| live-family.txt | 97503 | 67938b6f913ad952574960f92c92800da64a49882e40f9d60499e178542fc5bb | d3a476ea097615dbbe78c2052509f91aff054c80 |
| family.m3u | 176821 | 0118341e596b3df6087dee297929e960edc87b67e466d603f24fbfcc36e32bf1 | 892f68bceb886e429d2af18362637b5aa119e1c8 |
| stability-history.tsv | 766534 | 7edb23aa6405d3157100043d44a5b298818403480e684c55c3a94d5947884426 | 6562bbf8918035ca6f34cd893938a82aec4f651e |
| final-publish-report.md | 11440 | b694587c3d30c81b1f37b87a89dbfdfcf99b92add007fb8b83397f22ab3cac37 | fce9e8bf7350a1daa0f4491a1c2ab6b3c2965093 |
| stability-report.md | 12855 | 2acdf40191f2d23692454ee2d7a2afd594a7108b22ced530fe2f13510bfa3d81 | 7f5f18d8e55c065e8e82725e0fe6ae215135f1e7 |
| coverage-report.md | 1330 | 0972214f0a88006ed1b69653aefa631c7c3c251e47ee06d0b9a00fdbb07a67c3 | 50da67cdf497f80ddf5ee8b86551e4240fcfcade |
| quality-audit-report.md | 1435 | c4c14e5c1fe1f591681a7ecca044137255923f7d780138fdbe6871b75b10c1a6 | b911132324cc275e790903626c72ad4d868235c7 |
| publish-guard-report.md | 784 | 12951427a7c0034163617c224c97db97f3f56160a36ec22890d55b0fe8e194db | e5ed3b1fc873534fbda935c34fb725ee7254a861 |
| published-recheck-report.md | 28050 | d921a3a016c390e8f3cd84973df331674f0132a91522d147c7099a4a6b821ebd | 1de0aee8d116601decf66be5085983921fc1bda1 |
| source-report.md | 5848 | a489f86431acbc74c8ce6e30836db117d31e2e6865d7eab3de0ea3dd4584012a | 76461ad45bd8df900512c9e0e3b0c5ae3f74bf0b |
| check-report.md | 5848 | a489f86431acbc74c8ce6e30836db117d31e2e6865d7eab3de0ea3dd4584012a | 76461ad45bd8df900512c9e0e3b0c5ae3f74bf0b |
| curated-report.md | 3613 | d2c58eb0fc84fecbd79966bef7282806e1eb023964bce9925464440955dbcc6c | e0537ae3921b3a733a48aab201e1ac7d74b17395 |
| sources_status.csv | 2599 | beab4d8226727e0833d361a1632caa1d4f35ea5a8b1d3662fdf071588ba56e36 | b83a73884f258722ba9fbe9e17e182faa104d225 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
