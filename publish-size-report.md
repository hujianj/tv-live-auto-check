# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1807882
Unique public blob bytes: 1179099
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 623103

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 207701 | d0bddfc5dedb01ac5cbb4a78b7b3508161eff876f3cf98b82c4432d0d3f78d57 | 1535d4299608ce7652370cdaa15f21afbb040fcd |
| live.txt | 207701 | d0bddfc5dedb01ac5cbb4a78b7b3508161eff876f3cf98b82c4432d0d3f78d57 | 1535d4299608ce7652370cdaa15f21afbb040fcd |
| live-verified.txt | 207701 | d0bddfc5dedb01ac5cbb4a78b7b3508161eff876f3cf98b82c4432d0d3f78d57 | 1535d4299608ce7652370cdaa15f21afbb040fcd |
| ku9-live.txt | 207701 | d0bddfc5dedb01ac5cbb4a78b7b3508161eff876f3cf98b82c4432d0d3f78d57 | 1535d4299608ce7652370cdaa15f21afbb040fcd |
| live.m3u | 368294 | 419329addaeb70741e72d1c6132e1730e694dd7d5bd72997cafad453c7092c7e | d7d626ff4ee3299b84e622c9136505a304ffb03c |
| stability-history.tsv | 539946 | 8cb6355635212086c325db8ed3cf876bf7de12b2d52177f30cb988a15ed1f219 | 23dbca219a198048b9e354344f90ca7883417e28 |
| full-check-summary.json | 18071 | a74613026bf1b3f949f4084aee6d82bdb12a52c09ade7bd06c2985bac6d35f08 | d100864c3f3b3e17bd8d898e4185b124ed46982d |
| final-publish-report.md | 11608 | 84a9da1f8de01fd8fdab2a1bb7cf7bac77da216b46dc0823371b5daffffc50a5 | 2542d5e10b7aa9fcc0823b1371066ae0fea07f03 |
| stability-report.md | 7726 | ef3167dfa690b4a46b8ebeaee82eb67e085ffe65f1770e023633612d01870ff0 | a4fb03248da01e71d9d7bb79846c7c20f2b91a86 |
| coverage-report.md | 1124 | 5d2db904a4e8c21da08463f0c62b42306f02ddaa0befca20096666ba9d7d5939 | 16df5af44ace90242cde1cef736acf40df57fead |
| quality-audit-report.md | 1282 | 1a5b21ccec3706bd948c4301918c780cd969c7179f172b72fc79ce5647bdc82f | cf0db7bd4bbaee39285338104512800070bf2296 |
| publish-guard-report.md | 802 | e93976b93d90f345e09c2cc9f7a618129fbee36771f20ed0c73cbd893c0cdd75 | 558a0ae79cac1181001f0cb1cfc8c2ee7b8f851e |
| published-recheck-report.md | 10685 | 40f1d3cead7315b060d60f06e8563895c5267e4048921861979da07fab3a33d7 | 4fe8d1a90c9a0ccabb7312583fefcec401205749 |
| source-report.md | 5680 | 334a19ed2c791fdc6c03673c2779160edc415fe852b8062a8aead0dd65d22b4f | 216d643f4b443cf86fca11b8d6a66e6167332085 |
| check-report.md | 5680 | 334a19ed2c791fdc6c03673c2779160edc415fe852b8062a8aead0dd65d22b4f | 216d643f4b443cf86fca11b8d6a66e6167332085 |
| curated-report.md | 3732 | d8b6e73bac6e9d3bc1399cbcfbcee2086ce97eedaa81b624068989f366844c05 | b1276392656e696c476aa436f0d2fd5e6b0f024e |
| sources_status.csv | 2448 | 8e720c179cddf81aab804bfb0ca84c736159c5ca0afaddf0aca1eb9e49ba1f5c | dbd0d7ec1abb33386e8213129b7e52e95de34ffb |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
