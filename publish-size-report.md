# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 344694
Unique payload blob bytes: 279165
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38564

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19282 | 9ec480f764f66c03c09bd5e1ffa28218e35cdd03a51a8987dad7590e8281c73c | d23c187b8d15f2433153806e1ad4177774e9c6b4 |
| live.txt | 19282 | 9ec480f764f66c03c09bd5e1ffa28218e35cdd03a51a8987dad7590e8281c73c | d23c187b8d15f2433153806e1ad4177774e9c6b4 |
| live-verified.txt | 19282 | 9ec480f764f66c03c09bd5e1ffa28218e35cdd03a51a8987dad7590e8281c73c | d23c187b8d15f2433153806e1ad4177774e9c6b4 |
| ku9-live.txt | 23029 | dd556324eb9c684ff973af5142cdc08f0d138d04f90ba775b6273b184b520efc | de4f17273a46d54a510cccb3375138446ff7b794 |
| live.m3u | 37019 | 72cafa4b04758999b4b61edb218c927597e06c2857b4da46ab3a747ef96b6e02 | 514fff3f40e01122a14020d0982321f8812ecc51 |
| ku9-family.txt | 18846 | 194c1413a982853da5f28d3ac9e347d997befaf76daa97ec355c7af1b96d12d7 | 1f819d675258f9c4a1815b17cfbce90aab7f6a2d |
| live-family.txt | 18846 | 194c1413a982853da5f28d3ac9e347d997befaf76daa97ec355c7af1b96d12d7 | 1f819d675258f9c4a1815b17cfbce90aab7f6a2d |
| family.m3u | 36211 | f831c08bcd80db19e86f46bb4c12b7fa1ab32257482086275e6ee1513e25ca50 | b596eb3eb920346bf32b4ee321e3bcc4a2d183e3 |
| final-publish-report.md | 10923 | 1510e8dc9503c33d04e10034bb7daf7cfea900a47f75ba596f2ee4b6bfa57593 | 60bee4f10a4cfd1188d60e074dc33236d9059f18 |
| coverage-report.md | 2200 | 8f484940eba7352d36ba7cd55fd4d2f487bd0a13a16ce9217d0eae4d253cb787 | 7bd49e0d4b8f748183de38bc267ac805c6e35527 |
| quality-audit-report.md | 4698 | b7f30c19166efab796721c88cc3e941743c0419d8f4f97beff5ccbc1ef596ae9 | 36f2827f63ca57b8e1bc1ed9676343f272e28e8b |
| publish-guard-report.md | 1501 | c95f33bd70bab4ea670bfe2c370d054d79394544a7d93a4d29563761797f0b68 | d053d236bd29288b41d460684ca4ba735fef3828 |
| published-recheck-report.md | 30910 | 3bf898719a09713d382d576ae0849334f057851405b7b2cf45a8f96df36a0d76 | c4ecf37123e42f7c3d84cc91d9ef163567c90bf8 |
| source-report.md | 8119 | b55fd8c787458346a1938d4ad7c6adc848d2c1f437b03a95fe6a8a4459f08602 | 1071747f3f85da120e446061df314d940bd51458 |
| check-report.md | 8119 | b55fd8c787458346a1938d4ad7c6adc848d2c1f437b03a95fe6a8a4459f08602 | 1071747f3f85da120e446061df314d940bd51458 |
| curated-report.md | 1833 | a5ff6d58bc0512011b82bdce18448009974ad33ca1a40759a396153705230c11 | b91338acaa2f3418711eb2ba8c24ded0685fce8a |
| sources_status.csv | 4181 | d4e1de6f3403c3d2856b76be31f441ae4744d93619fef85cdbe579b81c172b8a | 7bcc30a92d4cdd252a39faefb93178a984bd5c96 |
| tv-coverage.m3u | 52015 | ff95ce70badf893c7183d3c8b039806dfe078c79b8393a3c470034695cda1e16 | e73a53c5aa3d95106c5d335e6f6a1c15590da535 |
| tv-review-report.json | 18069 | c7ebe34d7f4ddbc56fd6d43581345c45528b0e8e94e77290d54947056497b3d9 | 2ab5cb92c1b64c110fb96f7bae9d932b67ce117f |
| tv-review-report.md | 10329 | bd09ba37b8872b061eb58e04360d3bc9848a2781496f5f699749829d37833a85 | 2bb6d00c3c58e3863c4e3214ec141e455458881e |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
