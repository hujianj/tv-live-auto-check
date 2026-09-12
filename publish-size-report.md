# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 203239
Unique payload blob bytes: 140727
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 41139

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 13713 | a3a4985b8df379f13a603d08568aba93e4ae94f28a476579fa762027a8129411 | 485eb65e85e9aad93bcad0e593b48aa6dff426ed |
| live.txt | 13713 | a3a4985b8df379f13a603d08568aba93e4ae94f28a476579fa762027a8129411 | 485eb65e85e9aad93bcad0e593b48aa6dff426ed |
| live-verified.txt | 13713 | a3a4985b8df379f13a603d08568aba93e4ae94f28a476579fa762027a8129411 | 485eb65e85e9aad93bcad0e593b48aa6dff426ed |
| ku9-live.txt | 13713 | a3a4985b8df379f13a603d08568aba93e4ae94f28a476579fa762027a8129411 | 485eb65e85e9aad93bcad0e593b48aa6dff426ed |
| live.m3u | 26100 | e3c3a785a811f9d7f99b210a8ebe1278a86832287d67444c3c3c2b44fc82db51 | a44c926ef36e6da3d76a4c6c2254839ab1fd201e |
| ku9-family.txt | 13284 | 3cf5b6132d40b587fedb15c3d7412106cdbbdca2fc6008c6042ab36a40acce3d | d52f326d1928c683f33cc0820e809794befc1699 |
| live-family.txt | 13284 | 3cf5b6132d40b587fedb15c3d7412106cdbbdca2fc6008c6042ab36a40acce3d | d52f326d1928c683f33cc0820e809794befc1699 |
| family.m3u | 25299 | ff808f24bb87b9f3381086f9e74bf76040a3424a7b4ef92b3b0f2e0ef6898dd1 | e918246b3c64bd22ab095927684aa471d7792e1d |
| final-publish-report.md | 10681 | 2b32f427f1921b134d4bad017c4a0ea28284a0b7197ee413f2b9b3f54bd0a5d5 | fe37524d91b470aeb3de0f03f01294e82040b86b |
| coverage-report.md | 2254 | d22ad0da2e31b911555ca504dd4e454e75ce86631463d1d86fac08505200ee61 | b8f415a2e928ad650ff63c5fcb1a8d9744758609 |
| quality-audit-report.md | 4736 | cdd5fbd41fb408a3b244c1851c0e3756a5cb448d2802c03d0a2c49f15bfecf07 | 09ffd36ed8e6cfff3696c5ec6d8d23c3d91eed90 |
| publish-guard-report.md | 1578 | 03bf33426a5b93f27e7cc23a5a7d185e55650368a7626ff507255b4ce0fc6e51 | b0c142349ad3022ee3f7cefef16034d5c86b5ce3 |
| published-recheck-report.md | 28938 | 77dbe6b70e44342476b1d8c21605ec46f6a8ebceba9e107698076f3d54d45c89 | 0d0453733aafb79a5dad4659f172dce2121b3c12 |
| source-report.md | 8089 | 418a8f3f40ba4452726e654e777fdb1efceac0767dfa34fed6ef35179685e97f | 66fa56aa623949f1f195901763e52f3c5c60c0ba |
| check-report.md | 8089 | 418a8f3f40ba4452726e654e777fdb1efceac0767dfa34fed6ef35179685e97f | 66fa56aa623949f1f195901763e52f3c5c60c0ba |
| curated-report.md | 1858 | 8b179b19fdb505928642ddf24dcbe8b3ee5ad5bc12d006f798c7a7526bcd06ea | 9667e53e6a6304072c077ffd55f7d2d8778d61bc |
| sources_status.csv | 4197 | 09d672b4ed3a4e0265737c2330d60a90a73ecdb1818ec9ea83d570b256d296bf | d172a4f75c341ad43817401afc21ecdb89cb051c |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
