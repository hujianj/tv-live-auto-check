# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 278642
Unique payload blob bytes: 183435
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65757

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21919 | b43d7761883489e29d4175b534c2f641e8547216a8384bf8c38569caad3d8cf8 | 2c3f5ce0803b1032b60353a84887b04352be98dd |
| live.txt | 21919 | b43d7761883489e29d4175b534c2f641e8547216a8384bf8c38569caad3d8cf8 | 2c3f5ce0803b1032b60353a84887b04352be98dd |
| live-verified.txt | 21919 | b43d7761883489e29d4175b534c2f641e8547216a8384bf8c38569caad3d8cf8 | 2c3f5ce0803b1032b60353a84887b04352be98dd |
| ku9-live.txt | 21919 | b43d7761883489e29d4175b534c2f641e8547216a8384bf8c38569caad3d8cf8 | 2c3f5ce0803b1032b60353a84887b04352be98dd |
| live.m3u | 42024 | 98ace1d4d1a6fd207523cc4c7a70bceb0a7198c17182bcfb31c4031312a12303 | 3360e56359547961bdd83f66d1943180202cab26 |
| ku9-family.txt | 21654 | e77b55d5ecf9e64cde5e434616299aaa511623046cd304c7a262cb959f6e7829 | 554a0283ea286e402fa1fbc637f2e8b89f4163ce |
| live-family.txt | 21654 | e77b55d5ecf9e64cde5e434616299aaa511623046cd304c7a262cb959f6e7829 | 554a0283ea286e402fa1fbc637f2e8b89f4163ce |
| family.m3u | 41511 | 141f172c5e24c9fd3273c696650b2622cff4908598c090a4e987cbe9d4da1565 | 75c876197da90809c6448813a6fe7a07224f2d4d |
| final-publish-report.md | 10718 | 73cd2293383650c50d020c8326ca1004f25e398bd43469ea3bf58be22a68cc14 | 3e61ab8360bd61a613bec808fc6660e2d90c3b38 |
| coverage-report.md | 2230 | d69f3ee7d4da9e37abc904f8d57515ea2f214ad9f74d4d9cd863a5f3ba146e9f | 3a6b65c5d8e8658221d24bb8fbb7675f62eba879 |
| quality-audit-report.md | 4719 | f4ff6ab99bf83a239b011ecf0739b331830e94d05b29daa7c93ba1a7292ee854 | 1b191d2e2fc5c6ad3cdef3a8c5a71a504f52a726 |
| publish-guard-report.md | 1619 | ec06b51cbe24fa7aa62f940e5ddaef578bf27a305a82ac7b5df56ba640167346 | 8b9906497dcf15271834087cf2c01d49097b821b |
| published-recheck-report.md | 23241 | dfcb8393e3af9d1873d29c110942249f6c484fcf67d48640e5587770500c76f2 | b03df5477bafb3511982503dab6211ded37da527 |
| source-report.md | 7796 | 877a723960a1917a90beb05ff09f6394c53fba163e03bec02ffb2c186b800f2f | 3344d46e79d9f1aa08c553830ae168a6712719de |
| check-report.md | 7796 | 877a723960a1917a90beb05ff09f6394c53fba163e03bec02ffb2c186b800f2f | 3344d46e79d9f1aa08c553830ae168a6712719de |
| curated-report.md | 1805 | d8fda2db68cf17e9b383943ad727f60367b0241d70727b3320e011e4873a3fe1 | 32eeecd6f82733f6b17317cc8ab3b96728309857 |
| sources_status.csv | 4199 | 793d2b94b17e3182374ef4b23681bc5da45b1e738f90e0328bca019e4eede29e | 86a5e3bad7eb1ef74af30838c442a9b4b899a8ba |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
