# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2457121
Unique payload blob bytes: 1686560
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 667104

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 222368 | fd4fdfce08b6c431dc356d0b4d9052ed7b0b0ec6218950b475f8f09fb73484b1 | 1c4e9ef6e8c016de59d9956040ffc6700d83e140 |
| live.txt | 222368 | fd4fdfce08b6c431dc356d0b4d9052ed7b0b0ec6218950b475f8f09fb73484b1 | 1c4e9ef6e8c016de59d9956040ffc6700d83e140 |
| live-verified.txt | 222368 | fd4fdfce08b6c431dc356d0b4d9052ed7b0b0ec6218950b475f8f09fb73484b1 | 1c4e9ef6e8c016de59d9956040ffc6700d83e140 |
| ku9-live.txt | 222368 | fd4fdfce08b6c431dc356d0b4d9052ed7b0b0ec6218950b475f8f09fb73484b1 | 1c4e9ef6e8c016de59d9956040ffc6700d83e140 |
| live.m3u | 396948 | 8b19df1cf529cfd32fd2d71842669d83b28be9e02c7a3159a83d31ab5ff5eb4c | d93d770af794bd7c98f5a9be3bf128fc53bf00bc |
| ku9-family.txt | 97601 | 09d4b1e6c88d420f482003bafcf253f4e5959bb90b68e3630955fc4344cbc854 | dea8fec56c0630ba991be8e467f65347e3774c5d |
| live-family.txt | 97601 | 09d4b1e6c88d420f482003bafcf253f4e5959bb90b68e3630955fc4344cbc854 | dea8fec56c0630ba991be8e467f65347e3774c5d |
| family.m3u | 176833 | b8b1e710bbaa985c28a31e98cb659a83ab421299c70cfda37d69993d33fb85ae | 6d37210c94ce2eefa3ef356ebc7de077e2c46a64 |
| stability-history.tsv | 726227 | a046953d11775a714a3e4ec1577637ffb8dc2a3a73ee8dd060d8efa9deab89ed | b4dd399b8725a7a851787216dbdfadd9f35dfe8d |
| final-publish-report.md | 11813 | cb91c4e2df27842ec548ef6c4caae00d5e77b8d9069ae0b659e848beb0cc330c | 038c0da3067012e72deb33b5614ed506a378462d |
| stability-report.md | 10606 | 63c59db785e5d4943288e6fa94f57298b512f140b1e199a0612941c780a28403 | 863fdccfd60ceba0b33abf2f35d48a740cad2552 |
| coverage-report.md | 1329 | 260d1d65351fec1724a4c644a4d07a6c0f18d6034682f708b56173382314f945 | ec839b13d59b78bd6421d8f23e70cf2ae6f1e6d1 |
| quality-audit-report.md | 1435 | acb64ea5d6cd20671208666254fa3a4a9f0e52638cadbf93a98e259d1ac109a5 | 5a0bf5771cbf3c78879366a3f29027204ac2184c |
| publish-guard-report.md | 787 | 545158e565e13cb0aa108c4433574eae57cd522ea37a83ff844aa89dd4574ec2 | baf8813c0f0c392dc4425c1944590fc993b6c089 |
| published-recheck-report.md | 28558 | ed03ee909f6a284abe1141cacd78e2ab6f37777f813cf627bc0f5f20b69659ac | d09a7d12572bc944fece00d46fb5810b7968245a |
| source-report.md | 5856 | 7636f870738cbfc9c1989e5964ea5c21e25dce0549368e3ebc0945e67762f1bc | 0a799f0c46a5d68ad95134418dc79dd34e118fe9 |
| check-report.md | 5856 | 7636f870738cbfc9c1989e5964ea5c21e25dce0549368e3ebc0945e67762f1bc | 0a799f0c46a5d68ad95134418dc79dd34e118fe9 |
| curated-report.md | 3596 | e21df463c8fa9b7f504166c45794a1eb82034415d06535a1637c6a3d4843afb3 | 759e60537fef54074b3f154661a75eadce5285e5 |
| sources_status.csv | 2603 | b76e4a83f34d048257f08c64afdebc9989206f02b3078a816fe45407230831ed | 945c1054c779698f62b997d3b20748803af7b504 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
