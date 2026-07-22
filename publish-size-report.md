# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2441147
Unique payload blob bytes: 1694706
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 644196

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 214732 | 0e85c01d14b807b5a375c55b8c10d3a752619054a27ed23962ba2d37804e32e9 | 0d5a4aa76669488aa12863a552bee7b82329a98b |
| live.txt | 214732 | 0e85c01d14b807b5a375c55b8c10d3a752619054a27ed23962ba2d37804e32e9 | 0d5a4aa76669488aa12863a552bee7b82329a98b |
| live-verified.txt | 214732 | 0e85c01d14b807b5a375c55b8c10d3a752619054a27ed23962ba2d37804e32e9 | 0d5a4aa76669488aa12863a552bee7b82329a98b |
| ku9-live.txt | 214732 | 0e85c01d14b807b5a375c55b8c10d3a752619054a27ed23962ba2d37804e32e9 | 0d5a4aa76669488aa12863a552bee7b82329a98b |
| live.m3u | 382869 | 17a920f1f22c6cf88e942711c533a269be45cbaff4815b8014320f01d609f0fb | cff54b60628317da6e7df4ea349134758af11dd8 |
| ku9-family.txt | 96408 | 18642a0962ac727d94a55ad38182cf7a36afdc7144f7c70fbe503f0ef262facc | cd647835c144c21902c581f327b264fa013f22a7 |
| live-family.txt | 96408 | 18642a0962ac727d94a55ad38182cf7a36afdc7144f7c70fbe503f0ef262facc | cd647835c144c21902c581f327b264fa013f22a7 |
| family.m3u | 173526 | e0884c5b08a111626250060c983c52809a048539080df320a7321263e2bda398 | 3f6fc7b18f698b98405108be3fad3234ffcbdfba |
| stability-history.tsv | 759131 | 688662a7975c2566bb6d0aecb58fad1dbaf5fab0136e31843effc9100eb3ff85 | 8082c9fbc1e9d18bdb2b4bc728666053c2182634 |
| final-publish-report.md | 13229 | 37ab721c159a452b8f6bf30f1f1ffade7e3f5a03288e96dbf9017dd4a8177eb6 | 41f6dece3cc0e02f0c6c050cb008b444259ee18f |
| stability-report.md | 10353 | 48fe0d92a9b422c07102487daf5822ac94bedbf44379117246cd5db73941a319 | 632a14b6c3e6a0fca071d6c6c008671c9b984d0f |
| coverage-report.md | 1368 | 5e93f58fbf7f60a9d43e4f0913b13c86e4d0a12074bdee3b5bde502337a734c3 | eeabf53367e3b3aab60eb075e16c07f2c5e6a87d |
| quality-audit-report.md | 1504 | 32f01fa463710f4a092888c571b40e328ac5413bfe7a228ae11ba0af8cfa6a33 | e6a3ca5a1c93ff5e7e921ba9f100df278a3b8db7 |
| publish-guard-report.md | 791 | 11d38ced59a5a2721096fe79d18ca70dc4ed094f0e5fd7b9d538a5aa1bf2891c | 6fc2c752ebaa27a06e582ebb498cd7c4b45014a5 |
| published-recheck-report.md | 28749 | aba9c4030d8e523d59b0d10348202c8d39c05fc209bfb1c1f59b3d9391b175ac | bf3fb10cc2d1f1e295dd7bde274ee5e181c405e6 |
| source-report.md | 5837 | 798034beb46b8311d476fc987aa31c31bfe560060f514205c73090b2a3a795dd | a5c2c35907b36285c22dcffd8a8c55efae8c3d40 |
| check-report.md | 5837 | 798034beb46b8311d476fc987aa31c31bfe560060f514205c73090b2a3a795dd | a5c2c35907b36285c22dcffd8a8c55efae8c3d40 |
| curated-report.md | 3607 | d375b358b360a8641d3964cc12e33cfc9af4dc0aec27875419f6984aa522698f | 1cc399671e882e5a6cef117090996967f0211a2b |
| sources_status.csv | 2602 | 7a8441f14e79c45e1b61a6f168aee9f701f07663361ecec363183acfde4333b8 | bdf26eaeca356f27ec30fd6aa33ded96017ec25d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
