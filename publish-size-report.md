# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 311569
Unique payload blob bytes: 204996
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 74193

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24731 | 7ed62bd7dd9ea50e316725f41e4db674bd38db6ad0264ce6078bec2c01270b13 | 3120c4f23fc9a707367f36ea008e60c9da542890 |
| live.txt | 24731 | 7ed62bd7dd9ea50e316725f41e4db674bd38db6ad0264ce6078bec2c01270b13 | 3120c4f23fc9a707367f36ea008e60c9da542890 |
| live-verified.txt | 24731 | 7ed62bd7dd9ea50e316725f41e4db674bd38db6ad0264ce6078bec2c01270b13 | 3120c4f23fc9a707367f36ea008e60c9da542890 |
| ku9-live.txt | 24731 | 7ed62bd7dd9ea50e316725f41e4db674bd38db6ad0264ce6078bec2c01270b13 | 3120c4f23fc9a707367f36ea008e60c9da542890 |
| live.m3u | 47110 | a37573c429bfa77ceb2c0d8a56c55cf96fc50d0f1f3dc5c93656ec054432a762 | aaaa96bd4a763ad8e2cad4da83a18ded6b3ea337 |
| ku9-family.txt | 24308 | 56645852974e1ad7dee2aa28063f533a90954135fdeb356b83da7e3e5823b9dd | dcd9db760d677d0815435f5e87a3d5eafb810453 |
| live-family.txt | 24308 | 56645852974e1ad7dee2aa28063f533a90954135fdeb356b83da7e3e5823b9dd | dcd9db760d677d0815435f5e87a3d5eafb810453 |
| family.m3u | 46315 | 548bd1d921ea68866796c479f731f3467c8eb5f4de333e581e66267a27c433da | 3c592439e87ccf5d78d16931ae3fdda81a08a23f |
| final-publish-report.md | 10541 | 778d64860f9e70d0f64d6df94f30bfd8c592e6362700666869535a3da5d50f0c | 30f162a58b9a019ec4f2afd40887e5f86fbfe25d |
| coverage-report.md | 2215 | 03984471a2ea3c337ae3cf4fd5ac2dc602cb384198c251354804d81d67b9c161 | 44821c4044bfe90bc7968b5fa3602b541477b784 |
| quality-audit-report.md | 4717 | 9880f5f4de1749f0ae2fbffb8118d5dca3b538b86dad0ff6763a945d53fbe4e4 | ff936a819d4b63da25c2f1ef56aa8fc701aab6d1 |
| publish-guard-report.md | 1559 | 1a155afb72f70519c8d6df0aeb52f23d2fdc8a911b5096016062b9356f5a6824 | afc61e81c309e5de44c0334808a2280c16bd326d |
| published-recheck-report.md | 29429 | 4b4a2e4dd9ac2b5505c070da4021842d27025efc2b9c1266dbb94a6e0a4a4228 | b7a7dad95089471708aa0f0cb01781a39fdc70fd |
| source-report.md | 8072 | c576eb4bff20a5f8c8b4a028ac68bc27c1cb95587c282764adff78207614b89a | 2fb8807a860007c06eeea7f517a687a03b47186e |
| check-report.md | 8072 | c576eb4bff20a5f8c8b4a028ac68bc27c1cb95587c282764adff78207614b89a | 2fb8807a860007c06eeea7f517a687a03b47186e |
| curated-report.md | 1860 | 016fbd7a09ae51708810ab68b93dace6077dc7b7361df90a2bf3aafd25e14a73 | da59e6bc8bd80d86d757ad79e6646fc5e3c51a7e |
| sources_status.csv | 4139 | 95110f901a9aff34005c7ae10f06ed554e33c87bd3f407f5d761154d21d7e633 | 722cf32780fd19a8c0607954406ef1c09e1fd4da |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
