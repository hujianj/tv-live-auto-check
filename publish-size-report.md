# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2080148
Unique payload blob bytes: 1500755
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 485466

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 161822 | ad21aa922518e7a2e5fc3fba5bf0d9109237372bc047bb009165ebc1fcc696df | 4c0a1765e9d13a670c4a4791a9f38d2cadb54df7 |
| live.txt | 161822 | ad21aa922518e7a2e5fc3fba5bf0d9109237372bc047bb009165ebc1fcc696df | 4c0a1765e9d13a670c4a4791a9f38d2cadb54df7 |
| live-verified.txt | 161822 | ad21aa922518e7a2e5fc3fba5bf0d9109237372bc047bb009165ebc1fcc696df | 4c0a1765e9d13a670c4a4791a9f38d2cadb54df7 |
| ku9-live.txt | 161822 | ad21aa922518e7a2e5fc3fba5bf0d9109237372bc047bb009165ebc1fcc696df | 4c0a1765e9d13a670c4a4791a9f38d2cadb54df7 |
| live.m3u | 288639 | e13d61a551269933e76a7a3e1280e6f5116bd7a45973615aa8c01db2d6bb52fc | 7a7e44776ea9bd5e2b53ac65c6b3e50b17e7bc41 |
| ku9-family.txt | 87365 | c3860abf4de5406b4f0b30ee6d07d0258fb4877b313b77d28b72226bc34c0132 | ad96fa821fd44e073af501d57fa5f21e72ac6495 |
| live-family.txt | 87365 | c3860abf4de5406b4f0b30ee6d07d0258fb4877b313b77d28b72226bc34c0132 | ad96fa821fd44e073af501d57fa5f21e72ac6495 |
| family.m3u | 154803 | e4e5698a78e9c96ba517e8b0cd46f490d1edb77a5d795d32b86ad631c7663f09 | 8073fd08564bae14c66c489bbfe7ac5c3e388dc3 |
| stability-history.tsv | 740093 | 494d1fc52d32f916b8dcc3ea4dd545f9087c43d4aaa4bc2cc93bbcd967156741 | f54deeaa1783799b40cf9e649b17492f986ce7cd |
| final-publish-report.md | 11487 | f3a7b6bf8880bfb32205158ccf81e03f45773319c1cc27f9d9ae794c9927b6a6 | 12a69f2e1568b81bc69325c21ba046752e4fb45a |
| stability-report.md | 11688 | b10ea6ad9cfeed551619eda6093b5b424d9076ce68b3627bd14213199927fa4b | b8306d6a6fc1f9d5daf1225b9f232e7440d95894 |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2065 | 59c50b8257cb3b2c692feaa09838b3428683c1db2d6dfc2ff72c105b33197a09 | a4e338a5441d515ca218189eb222eb359a851b78 |
| publish-guard-report.md | 1153 | bdbf325f89f60aff44b40c2101050899d748fbcaf8ced9e52f696340a3c957aa | 7276a26a218b4db6ce1cdb1ccfc771afbe767a77 |
| published-recheck-report.md | 27314 | 1bb9a6bfd72ce3f7762bcf166d6b619eb73823e8137a1061332336c5f1b1890e | 1d7be92a987aece0e0cb784c6b9fc1b2ac2c3263 |
| source-report.md | 6562 | 24b9f8c229e5e2551d7aaf8f6910c765c4fe8f1b9ce51a4dd6aa58c0b00cdb49 | 7b3c38fe9d04c482b8b270eb7cf54f337e95b132 |
| check-report.md | 6562 | 24b9f8c229e5e2551d7aaf8f6910c765c4fe8f1b9ce51a4dd6aa58c0b00cdb49 | 7b3c38fe9d04c482b8b270eb7cf54f337e95b132 |
| curated-report.md | 3339 | 4f6831ef9764f95ad155c8189aa0dd2f8cf74b8ef1a1f22810ad6d8b729b09b6 | f82a624ab14bc53b6c2d0af36a8b2e37be6473e5 |
| sources_status.csv | 3134 | 506634e2aaac6952c50ba983b5d90f09fc058d70627be21183b79a0a3736f5bf | c1ecb3b230ffe7eb56535fe9538c921a4470322e |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
