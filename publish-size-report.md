# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 295797
Unique payload blob bytes: 194877
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 69825

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23275 | f98e7e6c6f77a5988ee8a10b27ab691e65af83b803ae715dccc8e2f3fd474a08 | 09350cf65b2ef1cab18c2f203ff3bc29b1ca1227 |
| live.txt | 23275 | f98e7e6c6f77a5988ee8a10b27ab691e65af83b803ae715dccc8e2f3fd474a08 | 09350cf65b2ef1cab18c2f203ff3bc29b1ca1227 |
| live-verified.txt | 23275 | f98e7e6c6f77a5988ee8a10b27ab691e65af83b803ae715dccc8e2f3fd474a08 | 09350cf65b2ef1cab18c2f203ff3bc29b1ca1227 |
| ku9-live.txt | 23275 | f98e7e6c6f77a5988ee8a10b27ab691e65af83b803ae715dccc8e2f3fd474a08 | 09350cf65b2ef1cab18c2f203ff3bc29b1ca1227 |
| live.m3u | 44492 | a3ba5f3021e62a8a892138d61825adcf66b07c1fc813544109d4f429139c9347 | c8815b2a686360f0481f8bd00153dd17988837b2 |
| ku9-family.txt | 23010 | b582959b04378d73e9791cf0229eb6f49b2e9c0c75db737d40d8de8c89548b33 | de95bf87dba56a8917e1b9fd614f50c5354a870b |
| live-family.txt | 23010 | b582959b04378d73e9791cf0229eb6f49b2e9c0c75db737d40d8de8c89548b33 | de95bf87dba56a8917e1b9fd614f50c5354a870b |
| family.m3u | 43979 | e66292b2a00baaea1c6f3d7a4195b7c1e374511612023684d15368ed55649c09 | feda1cc8ef3159c061650b8662f9c5d49336531c |
| final-publish-report.md | 10749 | f1958aee463b482dc9c07bf404c4c8e3aa9a9aafca0831abe59e799f1d21eaed | bb247fa99c46e8f9f1596f172707f4f868a8b634 |
| coverage-report.md | 2230 | 610c69973e3ab07562fb6af490421c098ab557e9288afbd19eda54aeeb6005f0 | 80253a07560e806ff65359e44c6a1b267c1aec21 |
| quality-audit-report.md | 4720 | 2fca39b9f3cdac272fa523eff441e1ff76f69346bc5b338c6e038103545c02db | bca03e34a5d140683fb1f33063c185a0028a4175 |
| publish-guard-report.md | 1561 | b6a572626c45a983b9d0d8ce6ceab497ca5ea160746e8bb99ea04465a823354d | 4176da035f3f28849ed99c76424072d2776e42a5 |
| published-recheck-report.md | 26840 | 3cc929f5e4d09bfb32c888ea4f544e98c0f52b4bd6e2ff50605764b324e50a92 | 9a22c35bb4f19ce31165a312d48f2de515ab8e97 |
| source-report.md | 8085 | 0f10b50dac23c6fd64fc01c6525bdb5eec8722ae4904826bc3f7c345703e36cf | 58daac1f1d162ec3e00af31af3a27d7dc4b63ea0 |
| check-report.md | 8085 | 0f10b50dac23c6fd64fc01c6525bdb5eec8722ae4904826bc3f7c345703e36cf | 58daac1f1d162ec3e00af31af3a27d7dc4b63ea0 |
| curated-report.md | 1804 | 21b1366ed417b1a3ba1b4f3f1a5792815cc16d88974ccf78c1c387ac0bc9158a | f6f42b865ed15cfe926efe65f1924f956e5a237b |
| sources_status.csv | 4132 | 22cb1e7a5c093a77b87791e248931bf11205d46d9ac2f3ec2ac28085c49e95cf | 7dac9cd72ce4823938468b69bdc7c449669d69d0 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
