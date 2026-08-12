# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2124643
Unique payload blob bytes: 1537232
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 490950

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 163650 | 60ba3c61d9fea90c1a30c202ca5dc1496f176b5af82986ef23558d8f8a691b4e | 297ed62901f106dbcb4fac1f2715676c56992cde |
| live.txt | 163650 | 60ba3c61d9fea90c1a30c202ca5dc1496f176b5af82986ef23558d8f8a691b4e | 297ed62901f106dbcb4fac1f2715676c56992cde |
| live-verified.txt | 163650 | 60ba3c61d9fea90c1a30c202ca5dc1496f176b5af82986ef23558d8f8a691b4e | 297ed62901f106dbcb4fac1f2715676c56992cde |
| ku9-live.txt | 163650 | 60ba3c61d9fea90c1a30c202ca5dc1496f176b5af82986ef23558d8f8a691b4e | 297ed62901f106dbcb4fac1f2715676c56992cde |
| live.m3u | 299849 | ecd6236a8162d0b5dae660f38c6ad45871753d1cc3bbee2baad272c7f564fb29 | d5750b3206975b4f4b2dc3ededea5704e83e0cdd |
| ku9-family.txt | 89926 | c48b8976138c26ce14d24852435ff66a46005742b5276903b37eb79741bf1dc9 | c9ecd6167c33eeac67db0f345f4a5a1e13a2b5b9 |
| live-family.txt | 89926 | c48b8976138c26ce14d24852435ff66a46005742b5276903b37eb79741bf1dc9 | c9ecd6167c33eeac67db0f345f4a5a1e13a2b5b9 |
| family.m3u | 162535 | d9434050836111c764033e6ea5212235567fbcf590734b21c8c40796ac9d900b | 335021707b93fc7a00fece886db85fe6288c09aa |
| stability-history.tsv | 753284 | 8001b25d23f35bcd5ad11caa1e6a320221d01fc9c3006851c8dba25906594e16 | 86be2c4b6a933eb21a325539c2463e178fcf27e6 |
| final-publish-report.md | 11740 | c7ed6b2d16baf411e8e0b3c5bb2c2213c217c692ae00f5ed507c14d181ddd0fc | 24d40056a8fc222ddf78a90f8fb26c604e78283e |
| stability-report.md | 11874 | cc68a6821a1fe0f1982fb5d7641a0b637f449ff6454e6cae01eda1e0a22587d7 | 5cad08f781fffb249cebe6ef62da3018b7289107 |
| coverage-report.md | 1291 | 79ee0ec9ea9a07a01ce9bbb79183b296e5f93cd736329639a7d607b6627d778e | 30c685d5d50f4f9cb216991e964245f7d8f670b8 |
| quality-audit-report.md | 2067 | 143676a167b4f684d0d4cae703ebe573ef638f31f1707ab15e751a5e600bc2c0 | bb3bc277332bf883dd6103b5d5e3925b3516bad6 |
| publish-guard-report.md | 1116 | 59fc90acd9c873f4b8dc5531cd800b67cae845e101536e24d10497f4d04da240 | 41ac7405515faaf96db117a21a1e076dbb502ae5 |
| published-recheck-report.md | 26800 | a7bb79273eb5d2a1c904b241318e0ebaf46c67af0bca9730c933930b610d3465 | 04074c8734d06367739d3454f1cc4721a2799526 |
| source-report.md | 6535 | 324eec9748c9d370ac591d49081f45f70c6208898c8517b20ae1a6a584c62112 | 1c911564456ce7f29c67640be11e34074e2603b7 |
| check-report.md | 6535 | 324eec9748c9d370ac591d49081f45f70c6208898c8517b20ae1a6a584c62112 | 1c911564456ce7f29c67640be11e34074e2603b7 |
| curated-report.md | 3463 | fad7d7df5d7550e876ea6ce167b1c15fa3501c6c0c35a66adcec0f91d05fbb58 | 1587324742b1142a08d4045f65a31e3a7f729289 |
| sources_status.csv | 3102 | 6f1e84d3a3e589b322e80166d9ea914ffb7f145dc8ebd6d5a36cfbd4dea0a0f4 | 5ecd808e0c0eb0d3bf96b281b5d96cf1bc9b7640 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
