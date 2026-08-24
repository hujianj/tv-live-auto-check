# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2019053
Unique payload blob bytes: 1456944
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 471756

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 157252 | 59ccfe504195fe9e956c006615fd2214530e09833d4cffe9c0e063fe00baf23c | 5196173ce0f013ed8744f62348b7b2fa3bcf8266 |
| live.txt | 157252 | 59ccfe504195fe9e956c006615fd2214530e09833d4cffe9c0e063fe00baf23c | 5196173ce0f013ed8744f62348b7b2fa3bcf8266 |
| live-verified.txt | 157252 | 59ccfe504195fe9e956c006615fd2214530e09833d4cffe9c0e063fe00baf23c | 5196173ce0f013ed8744f62348b7b2fa3bcf8266 |
| ku9-live.txt | 157252 | 59ccfe504195fe9e956c006615fd2214530e09833d4cffe9c0e063fe00baf23c | 5196173ce0f013ed8744f62348b7b2fa3bcf8266 |
| live.m3u | 282011 | b9d6fd00911cf5b1ddaea0e77a8ef6de1a5ee77fa1e01844453d3e3aec7240f7 | a5d7b530a069f45cf6afd964c8726d0664a4837c |
| ku9-family.txt | 83779 | 3121b9ff4c9aa387c7937174335bc52bb4c881f603194460cc96c11683a95ddd | 11ec386dd85140e6c58f24f47ef2a26fc81b275e |
| live-family.txt | 83779 | 3121b9ff4c9aa387c7937174335bc52bb4c881f603194460cc96c11683a95ddd | 11ec386dd85140e6c58f24f47ef2a26fc81b275e |
| family.m3u | 148920 | 0e4f1d1e059ffc77c2d6c13d367841ae86fab8dfa44740b244dae36e3c415df0 | 8b59b1a2633f773fdf713ccd47b06f2c9dea8a21 |
| stability-history.tsv | 716542 | 52289ff5ff8b9a7a114ce7031b2cfdca8cb1cc679886e225214fefa838d330d8 | 563f2e20b1ff5af1c07916ee27e53b00b28a7d87 |
| final-publish-report.md | 11859 | 78bc53bdfee1d2dc19a3b0ccce443512065c4e802b77f4178adc62b27de10262 | 8bd2c51cdb809aa9df2c26749961f1b21f4a140d |
| stability-report.md | 11963 | 4dbd506861a5187fe33f2954e47cc7b456c9c1b9bff06d6bbad0fe90c28cfa18 | cff251be0606a79f7ce5da1460e5b2041b728a31 |
| coverage-report.md | 1291 | 92ec7a4aca1846d0e97716f3acbf8fd231f3d7d38c58db019d49405941e1e29c | 710ccdf73cec84abadd494cd537e7c041220dd7c |
| quality-audit-report.md | 2062 | 730a56c775dd16a32b986a49149d09675e3e6872b06233dffe08797806a70893 | b20ee5639ffa802f2d2fd4cd465189d041f7d1a6 |
| publish-guard-report.md | 1143 | b8f598c1f237c7e6bb8933ff9a9c792a5c02728d74dcd6bb761ad74aec05ea33 | 7d12251bbaa01b200eb0e9c809373abea696546b |
| published-recheck-report.md | 27053 | 035d9150d9092e63597b8a977f691205004a3ccd0a2300955bc6b5725cefc2bc | fa2caafc52368d7d6b45f7264d7d3026c83aba01 |
| source-report.md | 6574 | 226a44c9ab31f37e6ea53bb9a6e166fc67eff134e4ce6e67078ef402de28744c | 4316a55f30b90d89ef26995f0d3ca1702ea02530 |
| check-report.md | 6574 | 226a44c9ab31f37e6ea53bb9a6e166fc67eff134e4ce6e67078ef402de28744c | 4316a55f30b90d89ef26995f0d3ca1702ea02530 |
| curated-report.md | 3361 | 7ac8c48fc358d406d406bfddb041acc909cbc8666ff5191994f886b24f0e4df9 | d8accf0fb744b393ee2f7862e7c663dc900d6e5d |
| sources_status.csv | 3134 | bfefe92337f1a14cf6a09cc66f832696a428b0e01f951b44c434226adf8417e7 | 1236b1698e4fa96e79fe2c70ee792cd0381d7e0b |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
