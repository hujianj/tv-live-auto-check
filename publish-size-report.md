# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 318042
Unique payload blob bytes: 257254
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 35258

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 17629 | b7dc817fa855f6d0a31a76d63fa34cb5d092e0fd7c1d6d7fb0de2f7dd83963ae | ee82c55a502a4186591033619381e2ffd7bddf25 |
| live.txt | 17629 | b7dc817fa855f6d0a31a76d63fa34cb5d092e0fd7c1d6d7fb0de2f7dd83963ae | ee82c55a502a4186591033619381e2ffd7bddf25 |
| live-verified.txt | 17629 | b7dc817fa855f6d0a31a76d63fa34cb5d092e0fd7c1d6d7fb0de2f7dd83963ae | ee82c55a502a4186591033619381e2ffd7bddf25 |
| ku9-live.txt | 20658 | 3bd807c387a6fc7e3ac381213f4572fad17de483f40c2fc9bb22d3730eebcc87 | 21720f16c39bfe2b4d6eb26b1b1c6a50305c8348 |
| live.m3u | 34170 | 3fed8ecf04f44853c207ab0311ba6ad8c6cd5e97f521df5bb7098fa3e5a78fdc | b22de8204fd51dc9007e144010ea970054c17f6a |
| ku9-family.txt | 17351 | b11feac5bac580598b5b33e181912c49ba20dc7559886fd85d15505c04a34353 | b9ef356063f80886f7258f6a4767d77ced4ee146 |
| live-family.txt | 17351 | b11feac5bac580598b5b33e181912c49ba20dc7559886fd85d15505c04a34353 | b9ef356063f80886f7258f6a4767d77ced4ee146 |
| family.m3u | 33644 | f398c39bb99d36fdb95780985434809b8471cdecc6e5a782ce04cefd223f6883 | b7668730a7fe53f3c166ec3922b571a2eafb6d15 |
| final-publish-report.md | 10895 | 03af114be13bd7227b47a22214b4b86463ad8097e3295fa1330d0e35857beab2 | c94e25245e2c1b341c799e3527a6b29622d8390a |
| coverage-report.md | 2185 | 17a0b98166402293fe6835ea090fc8b49eb2e5a18fe20b14522d6fa3e7ebdf90 | 236a5d625ea6925638c4caece450b7d4a27cec74 |
| quality-audit-report.md | 4684 | 5182e0a1e5fbcd434ff840a5b3c94b8f8bd361dcf79b1a5bd4aa4409c3f05c0a | 297b2d431e9c3e9465558c4593f5021cec295ee1 |
| publish-guard-report.md | 1529 | 3e89441866a3a2a870cd648780bc5f961b503c1b43eba48edc3ca8cbd2d692f2 | 1163025d48c8e849fda39609cedbccd49aee4f47 |
| published-recheck-report.md | 30878 | 67b59f43a0a65ab14ea04c10705c9800f5f9e95b7fcac7da6d5d86f2c628deb6 | 784257d044db4dfe5090dfb7ec062c10554a2df6 |
| source-report.md | 8179 | 33277950eacf87a702d8629e18a9cd63d2e90624a7b702b6fd0f2e171a009e4c | e1d480153012f4ccee671e78cfdd4f48f77d7195 |
| check-report.md | 8179 | 33277950eacf87a702d8629e18a9cd63d2e90624a7b702b6fd0f2e171a009e4c | e1d480153012f4ccee671e78cfdd4f48f77d7195 |
| curated-report.md | 1834 | f73a401c8dd752d730f2718eaf4deb0ed07676b29206aee0222a1412d1292395 | a34ae6d0ed5333b0353195d04a062f87cc0cb32b |
| sources_status.csv | 4211 | 4c88890a99a75e3c19217e866abfdd501ee1b5fb39527e2930d8de3a22acfa2f | e5816c714987b4417154d38ce9754a0da9304203 |
| tv-coverage.m3u | 47114 | ddf42353bc93e48d9a24c81e091cdb52698a4b152ff4a5b242759f3bad10b1fd | 6e30da495a6c6f5616f801ecd2db46e25b07a4b2 |
| tv-review-report.json | 14139 | 66a85c2131cc7274137d9fc916e69ba570c784cf2f148428931c6ce61122aa0f | 341184da69b985f24f8bf6565e206d468a890a67 |
| tv-review-report.md | 8154 | 91260b2cda801381989341753770661f75bb76ed29694900acbece6da976537a | b36c9a46315545ba71cb277af9470bbeae561ace |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
