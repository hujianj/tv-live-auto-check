# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 279022
Unique payload blob bytes: 185087
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 64569

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21523 | d740e0064460b896f4d90593e07b2b1d298e4025638823646c22549279952c46 | 4184637ae4cfdf4f52f23ad7c92a7dc4cd0cc591 |
| live.txt | 21523 | d740e0064460b896f4d90593e07b2b1d298e4025638823646c22549279952c46 | 4184637ae4cfdf4f52f23ad7c92a7dc4cd0cc591 |
| live-verified.txt | 21523 | d740e0064460b896f4d90593e07b2b1d298e4025638823646c22549279952c46 | 4184637ae4cfdf4f52f23ad7c92a7dc4cd0cc591 |
| ku9-live.txt | 21523 | d740e0064460b896f4d90593e07b2b1d298e4025638823646c22549279952c46 | 4184637ae4cfdf4f52f23ad7c92a7dc4cd0cc591 |
| live.m3u | 41443 | bc77bf8af2d4cd0d1757522e91c510cf11bf7b2e2c54231866cd5144b7d54fa1 | 7f32620b6f3c7a8fb0f6beab80f51fe7c6f5adc2 |
| ku9-family.txt | 21258 | a27f4ea3b67d75b3868964393dad9b1f95c53ae7bdb1045edd3b4f841df43fea | 4cd8541586b7c95ce6ab5aaeeb15eb844c89edef |
| live-family.txt | 21258 | a27f4ea3b67d75b3868964393dad9b1f95c53ae7bdb1045edd3b4f841df43fea | 4cd8541586b7c95ce6ab5aaeeb15eb844c89edef |
| family.m3u | 40930 | c360b717235ce288d36d40130eef69a4ea35c6b407b3db5da2fbc65bec6938ba | 7fe83e9dfb1c7a8ab0f5d1968f835260fc795475 |
| final-publish-report.md | 10709 | 69358e71f2eb57336a9ca48ef123453e68d282ad2ce7bd72236088bb3fddc616 | 7eea2ea028a80ef2cf552b9846c11f98db2bc18b |
| coverage-report.md | 2230 | 824e43249140c869d3320166f33a8469458758a6718d84c9085466944cc4f289 | eabc08cb07f0d3a63075020a591ef1afab72f7b9 |
| quality-audit-report.md | 4719 | 35b8cc31c38ca5f8e7c0b28c07fc8e1f9929e9a58b24e363420b573d89f51cec | 7be69812f10715e7d71d32837b1923cdcd3b4852 |
| publish-guard-report.md | 1556 | f54af015e5a4946e1b313202672feffda7a81602b0940eebdd8a2c29def3aa3e | 7de67fd98eacf00704da5d8dc3775fb765035e6a |
| published-recheck-report.md | 26669 | 6d9b8454668c429023424807ef57e5e56dca89ddf5d737c9a4dad8023edaa140 | efb28eb4a312da47e393dd1ddcd72bac6d7af16b |
| source-report.md | 8108 | d5d65b9c24ee4599c98a027c1c5cbf2c369141098db606ffd2be52f567fa119a | 1fa2056dd68dc4a3140eb6fbb4fd05135571c93e |
| check-report.md | 8108 | d5d65b9c24ee4599c98a027c1c5cbf2c369141098db606ffd2be52f567fa119a | 1fa2056dd68dc4a3140eb6fbb4fd05135571c93e |
| curated-report.md | 1804 | 0b00f96a5173a249702ea6f51023da4556e0471f00c76525d9954bf47ec7dc76 | f860d052eec0035ef5c8bd756f4c12989f2391d9 |
| sources_status.csv | 4138 | 0ab8aa70edd2d1c721f3d79e1648505e9ecbb9038e96563cdcd5700f5794e12e | d4ef4675c6d5460952d57fb0509834f418ffb407 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
