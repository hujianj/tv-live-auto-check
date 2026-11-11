# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 340277
Unique payload blob bytes: 274848
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38468

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19234 | 816ae89427bca0fd81e647dee034d17cabb296e5132a452648cece46be6d5770 | 6105f63f747990ed2bf67f513b1f155a0b059a1d |
| live.txt | 19234 | 816ae89427bca0fd81e647dee034d17cabb296e5132a452648cece46be6d5770 | 6105f63f747990ed2bf67f513b1f155a0b059a1d |
| live-verified.txt | 19234 | 816ae89427bca0fd81e647dee034d17cabb296e5132a452648cece46be6d5770 | 6105f63f747990ed2bf67f513b1f155a0b059a1d |
| ku9-live.txt | 22918 | 25408ab942f0c3d1d5fc6efaf715df42274a23016603e7e2208387271c53c22a | 057a946af804eb389839f4b94cd8f41b6b92111e |
| live.m3u | 36903 | eec419826a5ceae6d9e92ff0da617fca9c7632fc9b86bd4909bcdc240e82bed9 | 7ccaa2448485dfc69bc242a96a3475da3f45ca26 |
| ku9-family.txt | 18798 | 8f8b6d860fd1375878a2aa9397010bc0af5ef09136ac66729b3a65227eb409bd | d32c4316a25820fe650eef9b89ef9772001ede75 |
| live-family.txt | 18798 | 8f8b6d860fd1375878a2aa9397010bc0af5ef09136ac66729b3a65227eb409bd | d32c4316a25820fe650eef9b89ef9772001ede75 |
| family.m3u | 36095 | c5e5be8d0078e647c98afdf846eec146b63a476912a082ed299710e89d13166a | f320f0a240266c8886ea60490fa5aeb39e4b7dba |
| final-publish-report.md | 10909 | 1a28f5324da105eedf36998f1512590689f00f2c2d2f1b69ee41538c1f345062 | 6e1efd9713b0fe123afca4aeab5a696ae810c337 |
| coverage-report.md | 2200 | e46d30cb63034296dfb81ec9bffdf63ccdc6fec0df511ca6befe2af34a7ad8fe | 666028e2c9c445f660d0b2eda858c3b856595ca8 |
| quality-audit-report.md | 4681 | 6d78c71eed0b93b7c9592a9e74ac470cd56b15631e1e39796f455807ad124a7a | 9219772755d96511af93c72c90738fb071e1bb1b |
| publish-guard-report.md | 1531 | 5b67e912ab4033c562f30fc0299b291efbb9df5254a1d44a4c2d9680fd3e2900 | caaa6c69df689b0a6c4f665956841a498285dda6 |
| published-recheck-report.md | 28170 | f481d8efab6aca0e8d7f338d830f2debeac188da5717234ebf92fa3947928dba | 6ce134c3af87284a149e34cf5b115baf8d5e4ee2 |
| source-report.md | 8163 | 349a580bf189ba8e9412622fbdcc7d5455e908c01d82cb88ce79985124e515f7 | 4388e9a19f41515c8d5adcb069d0e706c51f8284 |
| check-report.md | 8163 | 349a580bf189ba8e9412622fbdcc7d5455e908c01d82cb88ce79985124e515f7 | 4388e9a19f41515c8d5adcb069d0e706c51f8284 |
| curated-report.md | 1833 | 3d447c9f01c7c3398267bacb47625f15a4ee1d467653aa111a7021467a06cfef | 4d353b853a805bdcc0933ae95c8a50d90acfab8f |
| sources_status.csv | 4241 | edf17a3cfd86e3aa99ccff67b0f5037b7ee44f43b3500cc3d3e2735bbafad0af | f9f40dcbf5b9ef346a98674e3f8a08a97c8c65c1 |
| tv-coverage.m3u | 51713 | 3126d4c1b0f57aa7b5d480f1d120c7a9cbb56e80629f1dae8d65d0650b4e2084 | a96e36035f2a5ead5c2d535ba2d86d976108af3e |
| tv-review-report.json | 17502 | e081a78a87f3d9eb808343029ad5f024d5abb84adfbc6ad2add1ee41fa923df8 | 9e1878d2058bfa3ee872c2dbfbe8139609c0beeb |
| tv-review-report.md | 9957 | 8bc3eb0ca6ef00f87dcaaed0622b325c3d9947c6b85c2904d62c7c3178f19027 | 58cf28df32c7c1d959e31278513edae7e2435342 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
