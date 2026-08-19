# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2014484
Unique payload blob bytes: 1456013
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 468711

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 156237 | c3d3926eaae56aa029584fe0757b0634e89584b8bf8612e890b2bb92a60ee9a6 | f26464bf7fdf5fbf97a3351caa7aa104d85f8856 |
| live.txt | 156237 | c3d3926eaae56aa029584fe0757b0634e89584b8bf8612e890b2bb92a60ee9a6 | f26464bf7fdf5fbf97a3351caa7aa104d85f8856 |
| live-verified.txt | 156237 | c3d3926eaae56aa029584fe0757b0634e89584b8bf8612e890b2bb92a60ee9a6 | f26464bf7fdf5fbf97a3351caa7aa104d85f8856 |
| ku9-live.txt | 156237 | c3d3926eaae56aa029584fe0757b0634e89584b8bf8612e890b2bb92a60ee9a6 | f26464bf7fdf5fbf97a3351caa7aa104d85f8856 |
| live.m3u | 281409 | 0dd49c9aec45251fcab0b11fd1f3673be36a3c91617219503323f4bd13047702 | 20ba6fce4cf725d86837752f18560d777a3f8204 |
| ku9-family.txt | 83187 | fc3f1298782c99b1158e3a4daaaabe8043ac0da9fbb86a28b127b13c8fef6f79 | aa7e590590dd10d0e85c8b50992549b101ee35e1 |
| live-family.txt | 83187 | fc3f1298782c99b1158e3a4daaaabe8043ac0da9fbb86a28b127b13c8fef6f79 | aa7e590590dd10d0e85c8b50992549b101ee35e1 |
| family.m3u | 148096 | f7279d4a31934a36b1adb50a37d515adce7df5168b5279b7a590e5ae054bdfbe | 5036daccdf6e008a1345959b10ad7355873388fa |
| stability-history.tsv | 718927 | 365886c2c90385bae1b19aa5f4ee224e9eb9525a975c55bcc7028c3700beb3a7 | d800d77d532ed19165ca3e165e35e7971073d1d4 |
| final-publish-report.md | 11736 | 11800dd0350f2d726bfc4941b7b1882e530b3bcc26f83317d8bc36333a464581 | c0e1fca961bcb43061f92326f1273464758b95fa |
| stability-report.md | 11986 | db1dfe398cf76c3fa399cce646e8f1f5928044e27957817762c2f4f2563a65c1 | 9b0c3d5b028c4a0a65719a1f764509bdec692770 |
| coverage-report.md | 1291 | d2bfaadd1c46463d71e7b41c774319cbe08e4bb89d61e660c5d5c4dbbdf404c2 | 992ea923afa7ce797f446b939fc4c9cd10ea7948 |
| quality-audit-report.md | 2062 | 70fcbe6d821cc3295c21e2361d8d28c4e0e9429cf019e0799ca622df19aa92ad | e727d3ff3c9da9508cbf57e6622a8bbf4e149bb9 |
| publish-guard-report.md | 1148 | 21e8f73d1695f19f15896cbfe159d89189bd61cdc23cd717551988bc80452894 | d031d7d811120d3a80b39fd21cff5cda998d8d72 |
| published-recheck-report.md | 26872 | cca28e6c2ea5b537f447948ce233a426eb0c7633f579700c1e00f54ad85a9f39 | 4969093f2bdddba370e602df0dafa870b647909e |
| source-report.md | 6573 | 11224c4fc3540228dc395b9b020df3467d912bb8ebdec45b91ea0283742b4695 | bd107954749a43b362dc84e6efc7122a94145a55 |
| check-report.md | 6573 | 11224c4fc3540228dc395b9b020df3467d912bb8ebdec45b91ea0283742b4695 | bd107954749a43b362dc84e6efc7122a94145a55 |
| curated-report.md | 3364 | 7d2e60c25fb9a9aa2a4ccd9477055cddebb2c865e5c3a5d38bd08bd9a9755d63 | 76e7441c147c7e392bf78d793471b6b55209e5ff |
| sources_status.csv | 3125 | f8304a2fd2a749881f97df009332f97f2ec3da8710dff5178e0b3d173a256a6c | 1a1127d7bbc6cc112e1239ee92ab69ce09399b97 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
