# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2425105
Unique payload blob bytes: 1686019
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 636468

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 212156 | d613208dafaebaadb8abf68fb337b47160f5d50f0757661bc52a65ba98703941 | ad24743645adaced3803c8e1555111e30375960e |
| live.txt | 212156 | d613208dafaebaadb8abf68fb337b47160f5d50f0757661bc52a65ba98703941 | ad24743645adaced3803c8e1555111e30375960e |
| live-verified.txt | 212156 | d613208dafaebaadb8abf68fb337b47160f5d50f0757661bc52a65ba98703941 | ad24743645adaced3803c8e1555111e30375960e |
| ku9-live.txt | 212156 | d613208dafaebaadb8abf68fb337b47160f5d50f0757661bc52a65ba98703941 | ad24743645adaced3803c8e1555111e30375960e |
| live.m3u | 381909 | 3de04691c3ee658f2c237731dd95d4e9672cba271079a668a578785260443eeb | 960e59d60be07b593ceee03ac53953dacc37df03 |
| ku9-family.txt | 96750 | 2cf1dc0f1636074366fa52e732a4344cf23f645e34c40c1cc5ac9a31214716ce | c4383163750db36f72d9822da16b4fc3d7082e2f |
| live-family.txt | 96750 | 2cf1dc0f1636074366fa52e732a4344cf23f645e34c40c1cc5ac9a31214716ce | c4383163750db36f72d9822da16b4fc3d7082e2f |
| family.m3u | 175612 | d3eb9aff87fd04f6422c95daaa1d4e51015a82919b8efc28ad618d3bac7a1f0e | 0207c5fd3e82bfb82e278b97a1f1dd131bb22ee0 |
| stability-history.tsv | 752486 | 703ecdd6ff722fa6a9d7b00293a2035471746690017bf89b2a81b1364f28fdf5 | cf9edbf7ed6a1116f9cb4af5c35b4d125a3e0223 |
| final-publish-report.md | 11606 | 56ad991e1894208891705a4f46ec53560a482db9457b16a2b5416c21907ddb44 | 3035d2df26728187c3fb5fd2280455c48c8f42ec |
| stability-report.md | 11963 | f5915e2f6e59cc0eada487e9ad831a48ecd3d8c1cee9f7493c2126466c10131a | e9c5de4d840456a66bdc44639dd7f73e1b8483d9 |
| coverage-report.md | 1291 | 9dba84f81ddb8fc0e5b6e72346215f0ab8801904d2f62164a22cbbd1e9e45711 | 05bf4f8c32af8cffc238322735216e08f4435b56 |
| quality-audit-report.md | 2179 | 205286fdb2cebb44aa4f322acbfe65f6450c946224aa3d0bf1c7eef441535b21 | d7bc13a210e87b8d9d1b9a2c4055fc52a10dcb1c |
| publish-guard-report.md | 875 | 5877634ddec5d237457c09177d7df6778c49799bed39cc56e53eac7069e90168 | 525a5e9d9fab205946f189ca2d6ce16bfeba8f34 |
| published-recheck-report.md | 27230 | d67be5b8a47f217b25ae5f73e9f3cea3ae6431397808d9e7b08f9d4c1ca26700 | 691eb53a65964c284449f41f79e705c9c1d337b9 |
| source-report.md | 5868 | fef137e772c6640a951d6134fb6c49d6ad8aaf485bf778e7c30520cddda27d21 | 07469e74eff5b108e1af3a2e3ebd99b2acd51320 |
| check-report.md | 5868 | fef137e772c6640a951d6134fb6c49d6ad8aaf485bf778e7c30520cddda27d21 | 07469e74eff5b108e1af3a2e3ebd99b2acd51320 |
| curated-report.md | 3438 | dc2fa2a8931e37031ec33403b9e0764433fc202a53d5abac9ff236b12123fdfd | 839a6ca983a0c7175e04ad8179637de54795dd2f |
| sources_status.csv | 2656 | 6f79bdf05eda76e3f95591b6d7c922b7a14f7609e7c63103b6b706af4a705d9e | e8237f8d3fd0bdbb022d667bd324b70102945e25 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
