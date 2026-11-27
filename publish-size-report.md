# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 334668
Unique payload blob bytes: 270544
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37654

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18827 | ec32ca7a3bd216179bbb18e03fa1f7eff0bdcaa9f013983227c062d3e4ba33c3 | 10960af8926fdc4c5a7fa4c64beba8a33e9548af |
| live.txt | 18827 | ec32ca7a3bd216179bbb18e03fa1f7eff0bdcaa9f013983227c062d3e4ba33c3 | 10960af8926fdc4c5a7fa4c64beba8a33e9548af |
| live-verified.txt | 18827 | ec32ca7a3bd216179bbb18e03fa1f7eff0bdcaa9f013983227c062d3e4ba33c3 | 10960af8926fdc4c5a7fa4c64beba8a33e9548af |
| ku9-live.txt | 22267 | 8f38af35993153857dde98cbd8fe585e1d619423ed31b6f34e72354da61f669b | 0d0233ec99e0f3646bb02cffcc986b37ae2d1810 |
| live.m3u | 36317 | e36539c8d87c0db885fe81165c2cea407e8257d4f9a0c255f14bf106084ea6da | 74a8fd922670275bf6709db3b2389a766be39e22 |
| ku9-family.txt | 18343 | 5284fdfec42d85afaa2adb2618239b3f971644e00e3de8094ab7a53037d2b449 | 72cc6599ebbe8d7e6f3fecc16de0f496d0bd44c5 |
| live-family.txt | 18343 | 5284fdfec42d85afaa2adb2618239b3f971644e00e3de8094ab7a53037d2b449 | 72cc6599ebbe8d7e6f3fecc16de0f496d0bd44c5 |
| family.m3u | 35402 | bf7ecf23985884b9eadb1ea7d7ae6d29c99dbebb797f3cdda819e3f3df2c5321 | e5d21a9e07308f105590502299f3e26070bd49a2 |
| final-publish-report.md | 11474 | a3f28d029782da89b66f0ea47d547975bf415b59a6e6e4e5c1607326b7cb0f99 | 941b85d0526628359b1125e72cd65ef8ec39d7ca |
| coverage-report.md | 2200 | 753846a2cf309be5e31d51f508378e2a8f91dee1ba0d4e85ce90e047d32cea45 | 11d7891dbc4fc10abfff4f315e5c424fc979aa96 |
| quality-audit-report.md | 4710 | 054462c03b4f783333f8ec5fd6a4aac8168b1adcd5b467b00f177c0e2eb4b76e | 774182fd79d9870cc59e2cab40f2b6f7582cd059 |
| publish-guard-report.md | 1582 | 09167f2790dee0f32efa72d7c644e72270a4a7d727542e2336885db7b41dc499 | 870c9bc6ce93c3807f9d71494ab5d075afb679dc |
| published-recheck-report.md | 29167 | 7a678dbc92c93f4364b4cd9e38e684e9070fb64401656b5e917966952f216349 | a8526488a32711585a1fd00637c26ff07ac45685 |
| source-report.md | 8127 | 808b4a49b0d570173eace753b928144b20516416639eb2b9c28b1bfbc068367a | 0ed9d9bcc1217de1ee57f57ff6776f352892c167 |
| check-report.md | 8127 | 808b4a49b0d570173eace753b928144b20516416639eb2b9c28b1bfbc068367a | 0ed9d9bcc1217de1ee57f57ff6776f352892c167 |
| curated-report.md | 1835 | 517d2b7580013e78cee87839164e7597bbbd476c4a2e34d2973e27fa9ebcbd55 | 25c4c664a83a17d33ed8d6356bb98c9b3cfff1ff |
| sources_status.csv | 4181 | 29842aa996d048a597064d392f09cb74e3fea942b5a9bac15e398ef2b09252fc | 024e82dfba189f1c05b0c45a2f48e3bdf4d708ff |
| tv-coverage.m3u | 50601 | 94025862b021b8b5bfd788131691c238df65c36289db1daef2bf2e5227b6617e | 22acdcb62dd1422d4a4e0db8cdccf44b54a47b7b |
| tv-review-report.json | 16333 | 5795c9ad08b3e9ef20a2d7078272351a6954af45e10e03edf0bc351e8a924f75 | a6ddf161c150c215378108b009aeecfa7bd684c4 |
| tv-review-report.md | 9178 | 8a6b06e0c4ab8b97a32d62c7e8fda14b94fc9bc7d804a82bbc7d227ae9145c0c | dc200f66c687c1a68f225e32b054e541e170565a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
