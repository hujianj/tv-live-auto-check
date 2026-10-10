# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 301156
Unique payload blob bytes: 198789
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 71016

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23672 | b20d0a2af422bb2e8ee69c9d551ff1ae3d7e878cb62a517cfc5fdcec6fc36666 | b1ee28faf3a0c8d4926f1ff74bcdb0a8de86bb6a |
| live.txt | 23672 | b20d0a2af422bb2e8ee69c9d551ff1ae3d7e878cb62a517cfc5fdcec6fc36666 | b1ee28faf3a0c8d4926f1ff74bcdb0a8de86bb6a |
| live-verified.txt | 23672 | b20d0a2af422bb2e8ee69c9d551ff1ae3d7e878cb62a517cfc5fdcec6fc36666 | b1ee28faf3a0c8d4926f1ff74bcdb0a8de86bb6a |
| ku9-live.txt | 23672 | b20d0a2af422bb2e8ee69c9d551ff1ae3d7e878cb62a517cfc5fdcec6fc36666 | b1ee28faf3a0c8d4926f1ff74bcdb0a8de86bb6a |
| live.m3u | 45107 | 08ed52e65bc39319b9061e582d2b41b8d32f7cd6f215df48efc5b1f9ea686dff | b82d5cd11ad5437b2a013297a26361f1e8b922a7 |
| ku9-family.txt | 23249 | a5cd3a2898831bc1bb93dc7399519ce0c10ab7b0bc9086a52abcb406f8e55830 | 7ba7918d32fd4438de9895f408b519d24c6b65b0 |
| live-family.txt | 23249 | a5cd3a2898831bc1bb93dc7399519ce0c10ab7b0bc9086a52abcb406f8e55830 | 7ba7918d32fd4438de9895f408b519d24c6b65b0 |
| family.m3u | 44312 | dad107c3fc4050dbcac785e5c6a4eb1a3927f5bd0b4458ddc5898eb5eb960093 | d4b5fd364d3080f5b9875dcd0150d7b96010385f |
| final-publish-report.md | 10789 | 0762712ce7f2dd39d378086971665c7b718fcee94a2dae270ed92030135d8f5f | 173a4b547b38bc1da2ab57b239f9f7d513f57489 |
| coverage-report.md | 2235 | 0ffa5e713b9a342a015ec4c6daf46aed5b15a200857fddeddbb516fbed105326 | 9aca8c4854c4c4a947591d567ca0c1562f8656c6 |
| quality-audit-report.md | 4721 | 9c9157683b010ffeef8bd745f627fe029490a0a539937da9af30af46c5c4d9d6 | 96fb5b256504284519b774fb861356269b6d8ba9 |
| publish-guard-report.md | 1611 | ae44898c4f7c1047b7db02f53edcc13a9c099b80f60d73bb3878bb40cfa83c63 | 2ad6e42281f87ebf9762397b294996a555eb54f0 |
| published-recheck-report.md | 29049 | a2f1032d7687e9350657c315cce1758079113b4b916d4c3b8d643c7c193237f4 | 6532042328ca82cfc53701e3707a65b005919b00 |
| source-report.md | 8102 | 2101ee208ac73d118ae2c34742e17090c75404d687847b30680c01f342899577 | e9a981e5a6975fd21a50216e2c474635cd38f6ac |
| check-report.md | 8102 | 2101ee208ac73d118ae2c34742e17090c75404d687847b30680c01f342899577 | e9a981e5a6975fd21a50216e2c474635cd38f6ac |
| curated-report.md | 1804 | 5ae879745712ac76bf749c4b5a9c35db1dba8dbaad2ec2c3732cf4fdd3b45a29 | a4053c09d254b0057400271d52c971cbe06a4a0d |
| sources_status.csv | 4138 | bc2b80e8652f6e265a7d7f7d14aec3369b13bc308af997f29e5e17ae4ba7818d | 02d5aafbdd7ffd09c762d86dbe0a4d5b08955bf2 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
