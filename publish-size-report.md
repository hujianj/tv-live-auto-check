# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 368845
Unique payload blob bytes: 296654
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 42986

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21493 | 6c4dc4cb2090404e3a5c43e5fbb29d163dbc2f41ed2375f68cd3b4a3b83678b4 | 3b24e45637b31946e6aff7502536f4dc0a92ce21 |
| live.txt | 21493 | 6c4dc4cb2090404e3a5c43e5fbb29d163dbc2f41ed2375f68cd3b4a3b83678b4 | 3b24e45637b31946e6aff7502536f4dc0a92ce21 |
| live-verified.txt | 21493 | 6c4dc4cb2090404e3a5c43e5fbb29d163dbc2f41ed2375f68cd3b4a3b83678b4 | 3b24e45637b31946e6aff7502536f4dc0a92ce21 |
| ku9-live.txt | 25348 | 36e4540fe0e08c8702fe208aebef0d701e4da233033b87895ad48ad4be53f809 | 88d9fc898cf9defb6d970a0a9b3248f2f91e6bfc |
| live.m3u | 40499 | d6b8fa337dacece16a0f434689fbba2c528a604af4d9452f305fdd57669d5331 | da76d80fd0e6577d2b296ad81351ad9e7ba48a3f |
| ku9-family.txt | 21057 | b6f7c7205385cbcf943b01467f9cb64ac6926838fa2806773364f19ef1d00528 | 36caedd20813434ee5c2a8f03ee54e01a31c692a |
| live-family.txt | 21057 | b6f7c7205385cbcf943b01467f9cb64ac6926838fa2806773364f19ef1d00528 | 36caedd20813434ee5c2a8f03ee54e01a31c692a |
| family.m3u | 39691 | 3902878b78255faf999de855d856af7bc5cc9b31ee13da651d9b710ebc211a76 | 27fe814bc5799b52ed4c2930a7386f63f8d3468d |
| final-publish-report.md | 11173 | 3451a33f4ee0ec6fac894b79cf1d7e41ddfaabea5176f0da0010d90ffc8f7985 | 7dbc39015a5f00e2f13debfe00208db3d75890b2 |
| coverage-report.md | 2205 | 7cb959a72267c061f25d9069718a3cd918112a56535c882da599c7731e26f9f1 | 6f4b24936880098dd0580797e12af0192d419556 |
| quality-audit-report.md | 4677 | d009036351550d936970221592b465543d8ca9dd918e6d010211a41c5a89c8ba | ab3649dcfebc833f3d8093a336352095f952f3cd |
| publish-guard-report.md | 1613 | fa3b9f0402c9f8d71dd0f853e276c093b79fb95fc8ad87b9b65f3d2de1cbd32b | 46461e41e2d977bb9035ea3a4ac3ff296e0d39b1 |
| published-recheck-report.md | 28620 | 3186c0b4f9b63ba60990ea52433d4d1405b16691fe86b4b93e141e7e46198cc6 | 806774f4ac7ef5da24b5b642065f810571329318 |
| source-report.md | 8148 | 7bbbae192335504c500837a5cd450c28bf0759c81aace3dc5bc0ee48b601c7d6 | 08cf295fe253f00dae6a5a58dabdb42c925d4dc5 |
| check-report.md | 8148 | 7bbbae192335504c500837a5cd450c28bf0759c81aace3dc5bc0ee48b601c7d6 | 08cf295fe253f00dae6a5a58dabdb42c925d4dc5 |
| curated-report.md | 1896 | 695ec4e5f4400802fb5f20154bf77a958a2bb0fa8681dd2037470cf1f0bea5fc | 50bb5c21d0ea4c54e10846f460f9cd758c23293c |
| sources_status.csv | 4210 | a2d0c3fc5bed0fbd58bffdd419935e0753ac12bdb49614cbd019b2cf5ddc49be | 7b377500501dec4939592a6a22804abdcfb9075d |
| tv-coverage.m3u | 56048 | 6f36fa2af920e96ea735106cde3a5f7d94bdeaad5c6fb402327dcacb16a3055b | c137846bc913fb58c468b8b452383cd35a2e89b4 |
| tv-review-report.json | 19053 | 526b69294f5af47548f0ec512ec870d1d3941030ae9f3214e6c4f2d514e6b46a | 5d9e8280a2581714ea3966f633357ac25733f033 |
| tv-review-report.md | 10923 | 35cf8d67294f01d27f7ac1bb8441df1946a88005eb797383a750dd6c135dd32b | 789379fbc6d88536a8c0c89792d133ecb1acd9be |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
