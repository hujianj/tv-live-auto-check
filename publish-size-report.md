# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2015009
Unique payload blob bytes: 1460575
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 462864

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 154288 | d4a84ee7730797cb663f94b28fa4ebd55f44fd9ae928fff5a1c9cbac69b90d27 | caefb915b0a960c232c27f6683e00716bfccd123 |
| live.txt | 154288 | d4a84ee7730797cb663f94b28fa4ebd55f44fd9ae928fff5a1c9cbac69b90d27 | caefb915b0a960c232c27f6683e00716bfccd123 |
| live-verified.txt | 154288 | d4a84ee7730797cb663f94b28fa4ebd55f44fd9ae928fff5a1c9cbac69b90d27 | caefb915b0a960c232c27f6683e00716bfccd123 |
| ku9-live.txt | 154288 | d4a84ee7730797cb663f94b28fa4ebd55f44fd9ae928fff5a1c9cbac69b90d27 | caefb915b0a960c232c27f6683e00716bfccd123 |
| live.m3u | 282460 | 0847abd767ab8fee643cd92f3662e4706423dce1b8a9c7bd5eefef00ef633092 | 4a9ed48dbbad6edd3b1a80757cac78701451018f |
| ku9-family.txt | 84972 | b03be4fa52fd32bbe9bb5ab11f3b97462dfac037e51d3d980428b9e0301f3783 | 8412a1035c81e87f32c5551e842e691bf1e80a9a |
| live-family.txt | 84972 | b03be4fa52fd32bbe9bb5ab11f3b97462dfac037e51d3d980428b9e0301f3783 | 8412a1035c81e87f32c5551e842e691bf1e80a9a |
| family.m3u | 153211 | 888a36c6a60cf74f35fa5f33451ceb2ac7d3967046e76a2e6b5afc95b5b5cf41 | 2fb37388dd079996e0377367ac159e9a1722ea0e |
| stability-history.tsv | 716898 | 4fd912cab4db966edc0300539e60b2babc6b2504497fe4781a5e73c40119b4a1 | fcba1cf27e9f2d7ebbc64f67ee3cf94bc628c6e7 |
| final-publish-report.md | 11914 | 4fb55ac5eb6a36245a597ae8419705e506cfba99d0fd7b96f93bc38d06d8500b | d174d0e63bad173e41c0ff8924cce9783bc01213 |
| stability-report.md | 11780 | f5a3e96389a8d6ba9bdd883b45c4ed9aa092cf2b8300a2eed89006a7055e20f7 | 5f0b8c7e7d6f496322ed53c8e6e76813812bbbe0 |
| coverage-report.md | 1291 | ab65bdc22fb2ce5a1016b66eb69eae11cd3191015e403b3a90842d7d08ed661f | 6eea0ab5434ec58d12d4d29a6e086c70b05019e2 |
| quality-audit-report.md | 2066 | b296bb4c6ecf316b8dccc7fa108fe63bd22fbe8a57b563a83263e0dc3f4c4e7a | 6194010c935090231cda38fd7de7153476da0806 |
| publish-guard-report.md | 1123 | f33e49c43a774c2642ea120963be068c70450e83410751e94111d42c08122cff | 7855db4ceac95d75ab1484c51c0269ee40e898ab |
| published-recheck-report.md | 27370 | a0fd62d90e8587b6baf212a2b178cd0a09e045a8dd50073ad1bf66be6c942d31 | 020f21261fa2506613b170514c4ea61211833fe5 |
| source-report.md | 6598 | ea4a65ed34b8100ea84fd2abf32e5c2a9ee49137319e0ecbfad9df6fdc43324a | 445e21eba9933c4acb6794909ce8960828879fe5 |
| check-report.md | 6598 | ea4a65ed34b8100ea84fd2abf32e5c2a9ee49137319e0ecbfad9df6fdc43324a | 445e21eba9933c4acb6794909ce8960828879fe5 |
| curated-report.md | 3508 | e164f75e77d87802f62b36cf50b786c2d4f59d164fb92750dac7354e39718647 | 67c16384ee7793c65352604ed92f1bd029c0ca0b |
| sources_status.csv | 3096 | 23ab2584ac3e7a1aa08bb8aabf8324fed1d263007ca5e9ed6262b8a2eddf0893 | 2fcd2b3520b865208c4522b16b9f2bd3e5444aa3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
