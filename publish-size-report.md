# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2436512
Unique payload blob bytes: 1698772
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 634485

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 211495 | b9140586ed5fcfd2cee1d187f992d4dc90ea7cf136f38a055b1ae7b4447e2964 | e06058a67f5ba30b8f503900d2446e44e2548fbb |
| live.txt | 211495 | b9140586ed5fcfd2cee1d187f992d4dc90ea7cf136f38a055b1ae7b4447e2964 | e06058a67f5ba30b8f503900d2446e44e2548fbb |
| live-verified.txt | 211495 | b9140586ed5fcfd2cee1d187f992d4dc90ea7cf136f38a055b1ae7b4447e2964 | e06058a67f5ba30b8f503900d2446e44e2548fbb |
| ku9-live.txt | 211495 | b9140586ed5fcfd2cee1d187f992d4dc90ea7cf136f38a055b1ae7b4447e2964 | e06058a67f5ba30b8f503900d2446e44e2548fbb |
| live.m3u | 380613 | 578e777c944454a0ccd6dfd0915b5301f369a7ed5b56da3b50cf22f8034c843e | 022ba13efecc669c48fcb024b4e42441c95aff1a |
| ku9-family.txt | 97422 | f4695fde09cde717b835df41f1195427a9d569f4be1628d9909554a33047ca71 | 57065750a8456ffb84a3862b96f2533f99ed3666 |
| live-family.txt | 97422 | f4695fde09cde717b835df41f1195427a9d569f4be1628d9909554a33047ca71 | 57065750a8456ffb84a3862b96f2533f99ed3666 |
| family.m3u | 176948 | 53fecf1c487bfa81cbb64759a7a445f11da1c79fde079b6bd85b0cd0ab7b4c63 | 1b1f256b0737f5d6d1094848c2433e889dc7c094 |
| stability-history.tsv | 764189 | a15d1560faa3cfd2aba55892d85e60c071d846608eeb5c42075696a9c80ce3b5 | 6050352b200b6bfa426cc5ec1d0124108bdb6ac5 |
| final-publish-report.md | 12101 | ec58d4a900f377a9a39d6950f9246b08c2479b0644cf605a0b4e719e3e34efee | 32e32f055f4826f8068f61348944c528f2a65934 |
| stability-report.md | 12844 | b3f9bf68c089173120bdb4881e198f9ba4d69988ee821c8604b281e9f6c82920 | 8a8b65601ca4393c3e802c6607c846b905f64892 |
| coverage-report.md | 1310 | f5f8b199c54d027e090e469290dc240f2fb1300f8498859ac955a05fd7aa9d33 | e898e26f386105568e69888eacc536ea7ddc55ac |
| quality-audit-report.md | 1435 | e1871f2c198b773b804d7385923390ae06714a6f48f6a16246c5a7e9bd29b1ff | 914cc5711eb00b9052dc608113f7a16fd7f1b0ca |
| publish-guard-report.md | 792 | 65bf5f7fe5207c6edaa9432880996942808b07acdb9119d618751fbc14a9daa1 | 1b4e53445fecfa2dd03c755dac3b8f0e8510031b |
| published-recheck-report.md | 27595 | a2e1f851930d60b5812c06af1b0bbe4ff424dfa3f25d8a9fb1aa8dc728d8147d | 31aa7800292c13bc3646d2abf41846697e1476ae |
| source-report.md | 5833 | b110e40809e666296b20f9f380626d45a464b8de58ac1313e10b34dfae68f28f | 163856310b07904b5bfcdfff4d63a1b75a6e7e1b |
| check-report.md | 5833 | b110e40809e666296b20f9f380626d45a464b8de58ac1313e10b34dfae68f28f | 163856310b07904b5bfcdfff4d63a1b75a6e7e1b |
| curated-report.md | 3596 | 2a803c4020b37d651059c3234bd7cf4d99651ff5ea17870650963e1e5bc4f361 | 9673b24e92a926bc367495446d83f499931fc521 |
| sources_status.csv | 2599 | e3890db676ce84379224a9d3cec9972c59a29dd65a3c16fea1485a9e74d809c2 | d7f03a70ccaf04f2ddc82415ddeb74264b5b4ae0 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
