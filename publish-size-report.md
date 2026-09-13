# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 305987
Unique payload blob bytes: 201731
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72447

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24149 | 0821462aab01ac422c89766a311148d3db58b0fd2807c3f2523e27b9078e7ff8 | 7e8508c6dec158158993cdcac27a20b809b8ea76 |
| live.txt | 24149 | 0821462aab01ac422c89766a311148d3db58b0fd2807c3f2523e27b9078e7ff8 | 7e8508c6dec158158993cdcac27a20b809b8ea76 |
| live-verified.txt | 24149 | 0821462aab01ac422c89766a311148d3db58b0fd2807c3f2523e27b9078e7ff8 | 7e8508c6dec158158993cdcac27a20b809b8ea76 |
| ku9-live.txt | 24149 | 0821462aab01ac422c89766a311148d3db58b0fd2807c3f2523e27b9078e7ff8 | 7e8508c6dec158158993cdcac27a20b809b8ea76 |
| live.m3u | 46239 | 4a61f22f00dacc2af68614bba15fed4271e3a1ce7840954910f552c912640d94 | 1a0d15d17b5a422ddd30a396d8491bb1256d6522 |
| ku9-family.txt | 23713 | 61c934b7c3ec446b285bfc4722b6f3363eac3b9a03fcaafee25c276e3ccd3edd | 20fcd81c97ca37a09d68705bd6f353c96c0b1096 |
| live-family.txt | 23713 | 61c934b7c3ec446b285bfc4722b6f3363eac3b9a03fcaafee25c276e3ccd3edd | 20fcd81c97ca37a09d68705bd6f353c96c0b1096 |
| family.m3u | 45431 | 65940402637bf33452fb94a89910530d539b9163cf49cbd3ff6d5f3a81c5d769 | feee59500fc56ebeeefcc7b6c2a86cdd243525cf |
| final-publish-report.md | 10634 | 41e616e91259a5f4cd925c34fcd66df58273914b603284676c7104cac68436a6 | 47b1b2462ad4313125901dcaf2843d1accbd55c1 |
| coverage-report.md | 2220 | 2789433961e4a75b39c49ca7860088ec87d884732667425f72be5496544647a9 | 3fd0b1727e0d996999ce209c8a42276dfe296e5a |
| quality-audit-report.md | 4718 | e90634a24bdbda659c89a2f3b3d0f09639edbd7aa1859fb730a7d933e973f672 | fb8e666a8bdb08d8a7ac7c322c4ad307c4c4a1cb |
| publish-guard-report.md | 1568 | 1efa81baafa644a4abf83917f4e1b791994599b425d0173c31f2b41ac96a8efa | 578366eb33c3dd2846f20402ed7e9d3a4d519445 |
| published-recheck-report.md | 28963 | bee985dd4197d367da72dbddcba86c3d5bf7893668583feb2ff587f688b6323d | 3163b0f1f7f32732a08114b45e624e017dea00c7 |
| source-report.md | 8096 | 3512c671ea9ccea10ba9e98c64bf37e78399d7edad68bf2ed07c9a92381b19af | d100c417698ed84ea543ff32c497242123e46ba1 |
| check-report.md | 8096 | 3512c671ea9ccea10ba9e98c64bf37e78399d7edad68bf2ed07c9a92381b19af | d100c417698ed84ea543ff32c497242123e46ba1 |
| curated-report.md | 1861 | a42453232434ff6682f1550839035eb2da2a3287431fd9e186c2473fe0bdeccb | 7ef3712df86672528c35b7b2ebeb7388d30e2738 |
| sources_status.csv | 4139 | 0e7e224a0edf8948784c6f5eef6c45a5ba1a05408cd6cc0beffbeba8543d444d | 09327f5cd721756bce8edb48e0f13f8922677911 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
