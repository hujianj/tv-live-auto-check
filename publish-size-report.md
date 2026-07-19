# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2442018
Unique payload blob bytes: 1682219
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 655686

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 218562 | 52bceb10d55d238347ef150b13281aa73636da0c606df003b55ce02aeb1114a8 | a147efaa4355c328f253fb2874d85191493596f8 |
| live.txt | 218562 | 52bceb10d55d238347ef150b13281aa73636da0c606df003b55ce02aeb1114a8 | a147efaa4355c328f253fb2874d85191493596f8 |
| live-verified.txt | 218562 | 52bceb10d55d238347ef150b13281aa73636da0c606df003b55ce02aeb1114a8 | a147efaa4355c328f253fb2874d85191493596f8 |
| ku9-live.txt | 218562 | 52bceb10d55d238347ef150b13281aa73636da0c606df003b55ce02aeb1114a8 | a147efaa4355c328f253fb2874d85191493596f8 |
| live.m3u | 390236 | 47d1961507a92c735cf3605aae409c0045153c7734cfc008ae49c233fda431f0 | cca79637b3633e42c8955bdc7de657b2cfc7c242 |
| ku9-family.txt | 98256 | 0b634ed84fd14cc1a512ebd2d3fdfca438b9d9bf391d22ff04ea2d8e5ac0c1e4 | f04f4a74f1323a0465617eb8f976c1004ad02f34 |
| live-family.txt | 98256 | 0b634ed84fd14cc1a512ebd2d3fdfca438b9d9bf391d22ff04ea2d8e5ac0c1e4 | f04f4a74f1323a0465617eb8f976c1004ad02f34 |
| family.m3u | 176850 | 925c35f81877747fcc3e99921d5f892b7a16ddc4137acd31803663c9514fd939 | f6d5a85842a6fdc792bb13d07a0a4c2d7590b52e |
| stability-history.tsv | 732119 | 1c6cdfcb54afd4623759845b58a32431f4ecb02e02ec3974379476fcfcd40e8d | f8bb6dcd83ddcf868395a5c6d8bdb3c13c17f0c6 |
| final-publish-report.md | 11696 | 697c2752d2a998c59f1c12ba5e7329eb9ba976d6c504bfcace4abce452569023 | fcc3fdd6a0f78c5f1f7bcd2bd4042ddf102683ce |
| stability-report.md | 10607 | 02910e5eecb56e019fda77c5d98534c23f2da1d53fd875950433fb1fd60e8b0a | 82bbb69d39b83d47bd97d47ecf479e21633dde94 |
| coverage-report.md | 1349 | ed7669a4146f61136d0108d8fcbfde8a5098144d6d0a90b550ff1f14fbe409ec | 92982e7f6d8358c9a40945059502de98b33cb1cb |
| quality-audit-report.md | 1435 | 3666a52b857f6530e0280824c31d90730f5179d31e989cef11b8b7e9301ae837 | 2f3141b630e8e96c76b4931625309b51135eccef |
| publish-guard-report.md | 787 | 9858b6cce40b8e1664f9b38d47c3c3098f886c05de1f857b1c88475752ceec59 | e32568e45d7d1c46f42bfe99c5db8453be29cfdd |
| published-recheck-report.md | 28251 | f05788d25c4cb8507e8e87f45bdb211bd53c3576b8216e6ca1373550954764f1 | 69168be510ca271436fc0fa65980079e358ba3d2 |
| source-report.md | 5857 | 514f629b6b77a7357069d5337332a31f521c3adc15c6caa589bb15210072a306 | e4f4ccb046a449c5c5fdf8ec589d8f1bb7866857 |
| check-report.md | 5857 | 514f629b6b77a7357069d5337332a31f521c3adc15c6caa589bb15210072a306 | e4f4ccb046a449c5c5fdf8ec589d8f1bb7866857 |
| curated-report.md | 3612 | 62b7ce47c5b1e2286e0bc31149a5ac4fff6a8abe084d9019cd0bc42c0966fce6 | 2bb7f047312baa8bd64f1d391700d8fa1de96072 |
| sources_status.csv | 2602 | ed8474bfee4631fced8fa27f2c73b9c45737cf64f4f4c22ae71bbdd6ff87894e | 826aefd90d6b10fa577fc4237aa9d404fa6c9731 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
