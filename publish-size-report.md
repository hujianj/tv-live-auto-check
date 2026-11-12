# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 335189
Unique payload blob bytes: 270558
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37894

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18947 | 01124b567d137f70863acfbdad6be9c056d96e15288197b383979a903ce76c57 | 593b674b8d7b7a3c73925d618bdce52676efa775 |
| live.txt | 18947 | 01124b567d137f70863acfbdad6be9c056d96e15288197b383979a903ce76c57 | 593b674b8d7b7a3c73925d618bdce52676efa775 |
| live-verified.txt | 18947 | 01124b567d137f70863acfbdad6be9c056d96e15288197b383979a903ce76c57 | 593b674b8d7b7a3c73925d618bdce52676efa775 |
| ku9-live.txt | 22512 | 467cc34e06da31d6330f6c22c7b78a549a5b845c9a6f53fafe99c21224df4892 | 48e0f519d28a191666a7742b7a7ddd6e56a0c90b |
| live.m3u | 36341 | c0cb572d17d4ed3f498b3b75ea5fe5b2a38a609ed10d59503df6f9e7f443a377 | c1391bc76e24603478f5803c8590411dcc0994b5 |
| ku9-family.txt | 18568 | 507a01ca8fd53380ab52dd6aac5dbe1ec7189d851137d44e731b3c8c8661a001 | cf4557f753f4f7f2a1d2e01b966dfd684e42e0fa |
| live-family.txt | 18568 | 507a01ca8fd53380ab52dd6aac5dbe1ec7189d851137d44e731b3c8c8661a001 | cf4557f753f4f7f2a1d2e01b966dfd684e42e0fa |
| family.m3u | 35652 | bc1d6575be437438645c1064849ca77a90db411cf94cc818feb0ef40fb75c287 | 5ddfac64c9f4f9daf9b6210718a5bb89f7044151 |
| final-publish-report.md | 10930 | 3bab7a2b5da779b4c99094d840e7d8c487dc81ccbf3689eede74e51a9c222071 | 02f1e7b25454855d87520484914a494e10441cb3 |
| coverage-report.md | 2200 | e46d30cb63034296dfb81ec9bffdf63ccdc6fec0df511ca6befe2af34a7ad8fe | 666028e2c9c445f660d0b2eda858c3b856595ca8 |
| quality-audit-report.md | 4681 | 8997f69855bd446a53ad3e0a10c4e3b62cec72919ee5b1e6026ed41b0baeb30c | dd5dd5702e24ed9146baaca30c00ed379fc071c5 |
| publish-guard-report.md | 1529 | ef52aebc2a600cb81fc77dc024c29de9e4aab5e0eb57e1813fdeb28c999a834a | e14e6be8950fbb8cf9b59ff597050380079b362e |
| published-recheck-report.md | 27363 | e07e212ee3ad1dbdc37fdee72c6010ed016c2cd591ede1932aa3857ef0299a27 | 78febc433545b6e9fa73b4ac79e0dde0847c7d78 |
| source-report.md | 8169 | a31b25b51116805221678284e033eddfaa9542763213025a06dcc5741e921dbf | d2763356e41b824878aceabd2d941f0f2cc77711 |
| check-report.md | 8169 | a31b25b51116805221678284e033eddfaa9542763213025a06dcc5741e921dbf | d2763356e41b824878aceabd2d941f0f2cc77711 |
| curated-report.md | 1833 | 441b088386e3f7e5bba1255f8e058608cdcfab97e8a32b033d0ddbe2e9d9f8dc | 48f937c5bed0847c22b34c38759f06730d84eff5 |
| sources_status.csv | 4241 | 403387c8655a826628cc448c8a2f30e7edfd02eb4f0bbb2b593924b92b07f1b9 | 797e8ef0b4aca6d819704641123df7f98d285307 |
| tv-coverage.m3u | 50836 | 6316da5c05c07cba857efecc7cc18955c289b0d24e09a3ea8bc55f3ad05a631f | b365ad46fc374376adb365af7e2830be9e96c7d6 |
| tv-review-report.json | 17053 | a3c70aa6979adb908a5e64d8f69142274017212a57a4dc331c73901b1d71c8dc | fe5344881f0854a412f4be261001a8e0376e43d8 |
| tv-review-report.md | 9703 | 094d348f937976c64234d5b1cfbc17efefc444999feb2d5d828187df7e95a9c0 | a06ef0465c86b88b5a326d14970f69f7da27c2f1 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
