# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 325015
Unique payload blob bytes: 261593
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37100

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18550 | b969ed403856477dfc54edbd5c4859441fc7483898b2935af93e337d1cfcee39 | 50c72e77013455ac3af94a1438e862e80e54d8c7 |
| live.txt | 18550 | b969ed403856477dfc54edbd5c4859441fc7483898b2935af93e337d1cfcee39 | 50c72e77013455ac3af94a1438e862e80e54d8c7 |
| live-verified.txt | 18550 | b969ed403856477dfc54edbd5c4859441fc7483898b2935af93e337d1cfcee39 | 50c72e77013455ac3af94a1438e862e80e54d8c7 |
| ku9-live.txt | 21561 | e4a45e91dbf027e24f1eaa0699ab334a61b8f2a2e92dceb0771b0ab8ed433329 | ddf2bac170f71961d608a87771b6d8e7fee59a1d |
| live.m3u | 35803 | dcb8c99e25384ef12ec3e5cd383428d08c7896543f11e63dff7395e6431cb1d6 | ee974e32837e19c17bfe5286bc23097da9f523a9 |
| ku9-family.txt | 18114 | ebe0d65a87299f6c6c09aa695b80b229dbf5dba099d58d21f4d11b35bdcd782e | 547a93e3d68570e945ec82e199335281557b57ae |
| live-family.txt | 18114 | ebe0d65a87299f6c6c09aa695b80b229dbf5dba099d58d21f4d11b35bdcd782e | 547a93e3d68570e945ec82e199335281557b57ae |
| family.m3u | 34995 | 2445ca7db9ae7100019f87dc6d393f141d82d83f23e248398514a817b075b4f1 | 53d596e515f1f62ee02552ea8ffbe7c158ce5d57 |
| final-publish-report.md | 10873 | 55ce6d31e0ace157f171140c0957ea86587a3f61d8a44f6b73d2b8dc7e427cdd | 370b63f7af0ee67c023edb106e0515900dce55cb |
| coverage-report.md | 2185 | a04cd300d635b15bb472f25f1f052eeb41adba870fa60447207e436504565b7d | f66694e85e44c56593fdedfd990ca7e211ffbdd6 |
| quality-audit-report.md | 4689 | b5dc2d95a89c28a48a3967be8311750b177d7d9002c466769534fda0a1718584 | f5c49be462dd80334633315646f286d6ec9fceb2 |
| publish-guard-report.md | 1530 | 3b99fdc40d309a8ac52367a6983c5bfeaa32db20628b7f894e837f396c8b7e88 | 2e911d1b15b0800f8d3c66db377be7bbe5dc0cd1 |
| published-recheck-report.md | 28184 | b1d3cfda5e2e7e03a3fe81a5e5634ad82bda967b7486260b5366142993dba8a0 | 3c0f15f7ce2a51e4b6586063d51f6947a34460cf |
| source-report.md | 8208 | ced08600d34f229591916ee6b9eb281c6ba8decb4b44176b77411f37621a95c1 | 273719cc4a86c22fa6479c97cd2b174a367ef8a9 |
| check-report.md | 8208 | ced08600d34f229591916ee6b9eb281c6ba8decb4b44176b77411f37621a95c1 | 273719cc4a86c22fa6479c97cd2b174a367ef8a9 |
| curated-report.md | 1834 | 3e5fd85777781ae1c0a59f36f989f3fb7b69fee1ceb9a11b49e39766cd410af4 | 6fa8405c02570abe81cebdb392f30b4a29998d50 |
| sources_status.csv | 4242 | 26b1d21c469dcb35045404c3fa5d9d51e917c5340d8b72604cf5b74742a518fe | 15902d46fc6bbca30812b7c65d9e27dc21f2f30e |
| tv-coverage.m3u | 48933 | 1773f71daa66dc0a2a8122c25e67731878dc5c956a813afcbb54a3022d248018 | c7413b6ee21e738c97228f4e18e82b24ecb3cc12 |
| tv-review-report.json | 13841 | c735999fb7fe8ae67b47295e0f6e18919ee4d8c25c3f6882897d52eb3197ffce | db2aa4632a097ef11fbd108ba4236068d397e42b |
| tv-review-report.md | 8051 | dd25e9fe7c32761a747d36b03f298a5c4ec4974cacb611f9cb8025b010c8c3f5 | c6ce62b0467ba70a5247256182c8a8f586cf3e79 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
