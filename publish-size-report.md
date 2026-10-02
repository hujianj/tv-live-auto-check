# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 285824
Unique payload blob bytes: 188113
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67410

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22470 | 2d7be68c79985251981cf8c89f11467e70c8e312167c55ac41800420901a9370 | fc6b3bd9de1e14a02f351e59bf50d5cf0ea83e7c |
| live.txt | 22470 | 2d7be68c79985251981cf8c89f11467e70c8e312167c55ac41800420901a9370 | fc6b3bd9de1e14a02f351e59bf50d5cf0ea83e7c |
| live-verified.txt | 22470 | 2d7be68c79985251981cf8c89f11467e70c8e312167c55ac41800420901a9370 | fc6b3bd9de1e14a02f351e59bf50d5cf0ea83e7c |
| ku9-live.txt | 22470 | 2d7be68c79985251981cf8c89f11467e70c8e312167c55ac41800420901a9370 | fc6b3bd9de1e14a02f351e59bf50d5cf0ea83e7c |
| live.m3u | 43022 | 6792eb7aaaecc2969c52d75043e1403c6543991c11b330a7df79b70ddf014007 | 09043a80feb139107f83c3c9e3ce4bc311129672 |
| ku9-family.txt | 22205 | 6352a61e0cbfa06a675e48703b296d67923285c79e814061edee6d3f3eb2f799 | a6e5d0c09a8fa10f5a3e56252be9d6b621f3f5f2 |
| live-family.txt | 22205 | 6352a61e0cbfa06a675e48703b296d67923285c79e814061edee6d3f3eb2f799 | a6e5d0c09a8fa10f5a3e56252be9d6b621f3f5f2 |
| family.m3u | 42509 | 5aa10d35f85e738035e94ff84e8fb4542b4ee2894519a596bd4b4438e06cc3a7 | 4bbe0949e519777ce164b9b08e635e8b94fa065a |
| final-publish-report.md | 10733 | a5e5b12b69798693f1c14194837a073f97157daad451a84f8e03ac9d51717452 | 766280dd702b001f1ba9c56085cf266c782f8706 |
| coverage-report.md | 2225 | 9313f064185056853c66e4ddfa913b2ab0b89e0700b4be411210d5dc030ff152 | e007670077b15ee778ecee54d3dc82da93345ac8 |
| quality-audit-report.md | 4718 | 11d291152e4f8befc89b4d330e12d4b0416d1b86bb5efc9b1e83db1e82b4b522 | 620ee263cd6a105e49bf1f4d447d746bbc63fb4b |
| publish-guard-report.md | 1558 | d282bd27b84fa8edbb26f1ac1a469f686580b7b2a701be0aaa8d5068d5227724 | f72783e2648bc510ef19cf7af25f910e67bfb337 |
| published-recheck-report.md | 24636 | 6cc7fff84c6c1b11409efb011f9a665c0d5a8d5bcfc52b2408c49a777c1b0c4a | 79e1403e19c230196f347775f58950fa6b4c84d8 |
| source-report.md | 8096 | ca5e7839015ae5e7d515d9c8e60a0fe559b1a7e8d7f29a4170bd8d10a5245d2c | 35e14d73fda0c92d2e6160fe184f9ff1f9a0596a |
| check-report.md | 8096 | ca5e7839015ae5e7d515d9c8e60a0fe559b1a7e8d7f29a4170bd8d10a5245d2c | 35e14d73fda0c92d2e6160fe184f9ff1f9a0596a |
| curated-report.md | 1804 | f55324c6957d72e87d7253565605acdab5ebfaf8b7263dba99426cd5d3d0eac3 | 2a4591b451881eeb977effe26d07767ce222ad38 |
| sources_status.csv | 4137 | 926548a00879409b41887b3c2dd384a26d70c9f56beb675e6289d5c6994d30ee | e0a43a9bfc0e3914621aa67cad8f6d3b2fefc5ff |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
