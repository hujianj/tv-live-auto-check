# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2123896
Unique payload blob bytes: 1539356
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 491205

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 163735 | 9906149f4fa3527040bc8f4969ec66367d0b8f8abdbc146c81aad7784589556a | a9d198983111373ff8a41ad2fe0d30adda2ad114 |
| live.txt | 163735 | 9906149f4fa3527040bc8f4969ec66367d0b8f8abdbc146c81aad7784589556a | a9d198983111373ff8a41ad2fe0d30adda2ad114 |
| live-verified.txt | 163735 | 9906149f4fa3527040bc8f4969ec66367d0b8f8abdbc146c81aad7784589556a | a9d198983111373ff8a41ad2fe0d30adda2ad114 |
| ku9-live.txt | 163735 | 9906149f4fa3527040bc8f4969ec66367d0b8f8abdbc146c81aad7784589556a | a9d198983111373ff8a41ad2fe0d30adda2ad114 |
| live.m3u | 295030 | a7bae65e491e4cb4bda3c7061715f5c986b7d099aa809541d4b9aad12047106e | e57e75cd7fc3328da6a67a92f61bf20cd257bb13 |
| ku9-family.txt | 86395 | 1ca224cb00457edcdb555e4d7bbfb31780acd741a57377a44b20dc3268897651 | 74f7d7ab11e77af94dded459bd520f45cf8fc3ea |
| live-family.txt | 86395 | 1ca224cb00457edcdb555e4d7bbfb31780acd741a57377a44b20dc3268897651 | 74f7d7ab11e77af94dded459bd520f45cf8fc3ea |
| family.m3u | 154390 | b75ef1945c73537d7b8ce9daf85ea5abd58d7fb4ab1803db58e641e27fc33763 | c9d9495cea607eacbb5d2dd3f0e88bd7f3067c65 |
| stability-history.tsv | 771279 | 60d7df87cc88a1f083b12ea3274e7ebb216c74d403dc1ebd2a2e5fa2bd44df2d | 3162359048047daa576e86bfa99f2763e39e94b5 |
| final-publish-report.md | 11608 | dbd04dccd5b755fa7ad92ea0ee782e5d8230dbdcadc5c033319fa740eeac5497 | 1854ac3221d86eff523bfa8c5ba2ffd684bd7220 |
| stability-report.md | 12292 | 4d4abd81b115b907969e1b37ba9f2cfcfd61d2715d5fce6152274d6d8c676cfe | 41efd1014bcda73e95383986d8fac1d3146c95ec |
| coverage-report.md | 1291 | f3c8fd2cb1770f496e6af15a6c3913c39b69b59a16cb0ecc1a94c2607f4410c9 | a9834426a05908da99a71189587d6565c42863f5 |
| quality-audit-report.md | 2065 | 1f2d10e9a056434625fb6b82f935e9201b830e48b3c04a6886534dc54f9a7557 | 705296563b8a85824628d50e8b0d683bd39af47d |
| publish-guard-report.md | 1454 | bd470aa4103c3fa0d1a0ecf949914e2e85a7d487fb3ff977005065c7533c5bf9 | 1f7b21f17d49c685da71df68fb6b21e6ce85ae50 |
| published-recheck-report.md | 25812 | 001e0890bb6a6f87377afde2034f4f6cc974d1fa1cdfae20c349025c2dfd0d3e | 559157f74eb27fd84a47dcda0315dc5efa7ddfef |
| source-report.md | 6940 | 79e166aca0cc5cb6e53317b47934d2d3cb59be9700a9fd83a40edeecf75937ad | 909acc273c84c687387d7b14d8bb75e6da88c691 |
| check-report.md | 6940 | 79e166aca0cc5cb6e53317b47934d2d3cb59be9700a9fd83a40edeecf75937ad | 909acc273c84c687387d7b14d8bb75e6da88c691 |
| curated-report.md | 3343 | e23bcb0e0d55a059104cf7bc18150cf653549aa14506d332a7773d1063c54d8b | 48ca8555b58eef7c26319f2092edcc020506a18e |
| sources_status.csv | 3722 | 7edd09caeac8b5f9eacd32cd5792da9cdd5c5e67a5f66aab1dae9ede9b2b4083 | ec40ecdaf7e4635f5bf735b0f83c9ee0f4ee7adf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
