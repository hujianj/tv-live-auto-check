# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 271073
Unique payload blob bytes: 180098
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 62358

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20786 | 2df08339a4b7ba4ce7c0a556d7615464f03e20fe94b3b4e200d7adc26acd0693 | 1f37b04339947c12cde0379ef4a591caed155bc6 |
| live.txt | 20786 | 2df08339a4b7ba4ce7c0a556d7615464f03e20fe94b3b4e200d7adc26acd0693 | 1f37b04339947c12cde0379ef4a591caed155bc6 |
| live-verified.txt | 20786 | 2df08339a4b7ba4ce7c0a556d7615464f03e20fe94b3b4e200d7adc26acd0693 | 1f37b04339947c12cde0379ef4a591caed155bc6 |
| ku9-live.txt | 20786 | 2df08339a4b7ba4ce7c0a556d7615464f03e20fe94b3b4e200d7adc26acd0693 | 1f37b04339947c12cde0379ef4a591caed155bc6 |
| live.m3u | 39757 | 107e6d31c703001e355a9db7c5ba0e718e91da889d92d0a03a8514a66a964fe6 | cb5e2d71a7c24db97dc13cb249aa2abe740ae9b6 |
| ku9-family.txt | 20514 | 540e29c4ff879ff23d933651ef039b68eb4fdf688c92c064170b7f91d04b6aca | 191eefffd234950ad3a8d9c1c1197230a589bc67 |
| live-family.txt | 20514 | 540e29c4ff879ff23d933651ef039b68eb4fdf688c92c064170b7f91d04b6aca | 191eefffd234950ad3a8d9c1c1197230a589bc67 |
| family.m3u | 39237 | 3ef4d2d0103efe15378adb2048cdd90dfb1891d57bb6af1d11aba1b772a5c141 | c6b15bae11eb255de7da5e1d681ebc96eef41132 |
| final-publish-report.md | 10886 | 3addfa05f68e14d7eb8475df56a0ce2a00549a6ed62bfc8e5caa994e2deca239 | 2244cb6b8574b39350601af7421de187888568b3 |
| coverage-report.md | 2230 | 316cc134d8c8d967b28d27c8446f04a6b97aa572130d4bc45bd0f78a138e2e70 | 7e83fea985b0e5769ae2813564db684c913946ee |
| quality-audit-report.md | 4730 | 4498539d1f071f1396c25ea1a13c55ce5e6d770c70070bfc93f963e90d1604fc | 0b839f81546b7f352ffc76933dcad2998e0f8302 |
| publish-guard-report.md | 1559 | f70339a9ac97d1554042a94be52af2148112a7357c3a446499483b627ca36ec1 | 5352d0a93cea06d8ff489e2f9aceab9ccd41d65f |
| published-recheck-report.md | 26311 | 5fea70af45b85e9c34461916e545e97b9bd8b26dbf6dbff127cf5ec79c13d98f | 83f8a239774d98f8a7d5aabe38530ab6a5449238 |
| source-report.md | 8103 | 70932d120f98c90b04ee39b2df83b48ca7eb3909b1dce0b1d6d2360977e62d8a | c59d35efa54a7f72f7e6b64c559becd0894f2490 |
| check-report.md | 8103 | 70932d120f98c90b04ee39b2df83b48ca7eb3909b1dce0b1d6d2360977e62d8a | c59d35efa54a7f72f7e6b64c559becd0894f2490 |
| curated-report.md | 1846 | d24b0a8e0c418de3d5cf8eccda34e3db3fd569c7328a83ecceec604cdf33da76 | 91e425fc58cf310e1f7416b84e1ea519f0a11f51 |
| sources_status.csv | 4139 | 42de0a92bd7e138112e3c604d3709c5261f1bb91a4b6933a3427ac0f9bc7e7a8 | a1b01b43fafeeb804579f01b07d125997492f629 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
