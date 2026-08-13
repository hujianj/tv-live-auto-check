# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2162300
Unique payload blob bytes: 1553227
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 511818

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 170606 | cbe375f7b34d55127cd9750c52b3fa3ba1cb2e598adaef216c125bee77fb8c90 | 9fed7d8b295c469dc3cf7baa66e222bcbcc0545d |
| live.txt | 170606 | cbe375f7b34d55127cd9750c52b3fa3ba1cb2e598adaef216c125bee77fb8c90 | 9fed7d8b295c469dc3cf7baa66e222bcbcc0545d |
| live-verified.txt | 170606 | cbe375f7b34d55127cd9750c52b3fa3ba1cb2e598adaef216c125bee77fb8c90 | 9fed7d8b295c469dc3cf7baa66e222bcbcc0545d |
| ku9-live.txt | 170606 | cbe375f7b34d55127cd9750c52b3fa3ba1cb2e598adaef216c125bee77fb8c90 | 9fed7d8b295c469dc3cf7baa66e222bcbcc0545d |
| live.m3u | 306478 | d1458e6af8db5b075e8d4909f531972abdc967b16a02d759bb8688bf1b4d4c8e | af5f757619f1cfb04ae31dae419f2869fcfd43fc |
| ku9-family.txt | 90689 | 6aa523a03d47fae387c31647c5f8c21de4838d9a4c86def441a7fde29a9c74f0 | 303ce016cabf67164c85b5221d96e72fc4cc30a3 |
| live-family.txt | 90689 | 6aa523a03d47fae387c31647c5f8c21de4838d9a4c86def441a7fde29a9c74f0 | 303ce016cabf67164c85b5221d96e72fc4cc30a3 |
| family.m3u | 161698 | 6de43e83c900d328827b9b3a19520693598d40ab29f331ce75d490ea5229640e | 291c826e85ea80b91d45e427121e95126c7da34c |
| stability-history.tsv | 756884 | 0206f0d5a799398b2a4cbf49a44af4f604ce4aaceac89f61fe6aa43ca80b4775 | 20f4754319f7bd226a8aa9eb905f8d4f04cdd9e8 |
| final-publish-report.md | 11552 | 29de8dd26084c0eb8d013aad2e9dd227de98624a0683c3fd0a3de08b697db200 | fd291547642994f5923626095ac85eff2ff0a6b1 |
| stability-report.md | 12317 | 314797f29da1fef781c72882ce325560cf03e13c4c9a21a1cdf6fea05e725da0 | fb311a83964e85e58c21d7af21ce239167efccab |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2065 | 5d4b886684d44489e7d15873e69b0d48a6bb226cdc7b365718b0f497e8fd5148 | df7879f1cc408c664dd4983238d4f30917fb64fc |
| publish-guard-report.md | 1144 | be53f307b7637b0d09d2db00b2d705aa8dfd1aeee253fad227f1f6b13cd32cbf | 17f5dbc96fcd1c816cc945a90300275a2891d01a |
| published-recheck-report.md | 25433 | bb5a05bf68ea68c75439069f8094cfc43f4bc15be596ab1debe1d06141343d16 | 009ca98a6e5cbe8e6e6fde6aec3fc7069a1ce703 |
| source-report.md | 6566 | d118f74adf403f5e406c0b02e5894537856442c0eedcbcf86c697dd1115ba533 | 931a96cbf84def13f192bea6d4e9d50fbeb779e0 |
| check-report.md | 6566 | d118f74adf403f5e406c0b02e5894537856442c0eedcbcf86c697dd1115ba533 | 931a96cbf84def13f192bea6d4e9d50fbeb779e0 |
| curated-report.md | 3363 | f9453f3bd4d8b96d54dd1b45fb1b19d1e1a82d7a3c4426fd8fb4cbe16ec15986 | 84a610f59ebb2a3dac5777e1c1209469c4e2c0a8 |
| sources_status.csv | 3141 | 0ef7b451f5f5a4916a0cce957b9071450af52c9680cbafc699c5f289e3a9973f | 901976a25a618fbd3ff4e87ae4b7cabe9cf9719d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
