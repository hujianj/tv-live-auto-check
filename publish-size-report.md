# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 330539
Unique payload blob bytes: 267389
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36826

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18413 | 463af9a3da224ab9f5b797efe87143a542ba480ef850e7916b6a681d2a214c7c | f6c29232407aa0c30a140b8c77e3b066316871ff |
| live.txt | 18413 | 463af9a3da224ab9f5b797efe87143a542ba480ef850e7916b6a681d2a214c7c | f6c29232407aa0c30a140b8c77e3b066316871ff |
| live-verified.txt | 18413 | 463af9a3da224ab9f5b797efe87143a542ba480ef850e7916b6a681d2a214c7c | f6c29232407aa0c30a140b8c77e3b066316871ff |
| ku9-live.txt | 22130 | 0f761b15fa091d1388d9e956d19ee85e81fc112c1318b28a16d9c73569d2570c | 94f3639152a7bd736b8fc228df562029b10fed89 |
| live.m3u | 35481 | 94e0b7c7f3e88cd81a558ce47b5b57d5e18e1ba5b42feaa8eef745d2f5fc39d0 | f9507bceb413107dbd919c505672dc5728105bdc |
| ku9-family.txt | 18187 | 5dcd9d3ef38118b863307381a8946c0ed6e7cce03937d7ed1c6bdbf104ec1d55 | 849202e2aa6be655e1f15c618e1530718004d072 |
| live-family.txt | 18187 | 5dcd9d3ef38118b863307381a8946c0ed6e7cce03937d7ed1c6bdbf104ec1d55 | 849202e2aa6be655e1f15c618e1530718004d072 |
| family.m3u | 35069 | 8c7a5181483f5e29de021e345ab8fe961bfff39dba41357fe84d06f84d8d9265 | 3fc0b00504609159a3a56699f78573058093f988 |
| final-publish-report.md | 11302 | ad413d5aac45917026fa10244bd41a93f477d4a6f2f6439d72f115401875922e | 51d8c141efaba3cb8e49aef2e46d8becce2e4dd4 |
| coverage-report.md | 2200 | 8a1047c307e5e5147d4c8b69a5e27149454c10844dc9870aa0537f9e10b7f791 | 47f0ec7e3d4d4c77e9e3f90aa1b2bc60b2ebe741 |
| quality-audit-report.md | 4682 | cf4a125465b18d159bd7036edbf51ef2f4c74c9651b69f39e47672076984e461 | ffc0d1fd59a9d33c878a1289b48f7fca8fe08a94 |
| publish-guard-report.md | 1585 | a2efa4a46ff9884781782c0a8fd33ac501d8141f4a823cf7c32b39c7781b13b4 | 89ea79af7890b8bf838987c6ef0858d2a6a833ca |
| published-recheck-report.md | 26867 | c8200d38874ac08e2c756814759b7ee4d36c6f926c75cb973ac70c03cf015888 | ff814bf396f12d1a63a0fd2d0bacf3b4626903db |
| source-report.md | 8137 | 721a89ed98d0a375de41369abc86ffcf0c256c427a8b62a75e2a32bf65e7f6c6 | f23e1ac07c0668a58b5834542184295d3b00f611 |
| check-report.md | 8137 | 721a89ed98d0a375de41369abc86ffcf0c256c427a8b62a75e2a32bf65e7f6c6 | f23e1ac07c0668a58b5834542184295d3b00f611 |
| curated-report.md | 1814 | 77c9eea130a9bd93f0ec4f3523a6c0491640a460883bcaaab809abce2ae3597e | 790526f804398533986172a7846f8dc87751503e |
| sources_status.csv | 4181 | 2f9a114ff07f1e9537d47a084ad15fb4de3a7c7a0d5f96b532af45efb0d52a79 | 1f0d5179488b8189e2cf7922b9e1426e2211af2b |
| tv-coverage.m3u | 50080 | 35056e039432fa83cfede4655d59d9db24ba607e45f472a9fc32b6553e70ac62 | 982b2aaa5ae2f29ea6c4d11afdcd5a26c8a68dbe |
| tv-review-report.json | 17403 | 5a1aef46051b85b8de2fbf442b02fd8cdc1a7d8483c1b8240a7dbb87f57c7f1f | b2a92e089be386a49ad4a396361a02cebd34056a |
| tv-review-report.md | 9858 | f745b5ba15a044d446f2442294c8a5e4f79553d0ed3625ebbbd4ec04d43c4865 | 2ee2070d5c3cfc45f751dc73d6b2e05b03fad87e |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
