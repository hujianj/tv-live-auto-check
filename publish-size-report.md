# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 348533
Unique payload blob bytes: 281321
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 39662

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19831 | 65af0a9e82ac1294ff87e0fdcafd5a103c368ec17b6582a5b5f204bce0a78cd8 | 77e1625cfc97f3d80cc0dab9dc095f8a795863f5 |
| live.txt | 19831 | 65af0a9e82ac1294ff87e0fdcafd5a103c368ec17b6582a5b5f204bce0a78cd8 | 77e1625cfc97f3d80cc0dab9dc095f8a795863f5 |
| live-verified.txt | 19831 | 65af0a9e82ac1294ff87e0fdcafd5a103c368ec17b6582a5b5f204bce0a78cd8 | 77e1625cfc97f3d80cc0dab9dc095f8a795863f5 |
| ku9-live.txt | 23340 | 260cbcab69d49d58b9364cf9da67d4e35ab306d6e97aa0e06843435cf2c95606 | dbd2a9516abb92a578f6b6e21e543ce15ac83db9 |
| live.m3u | 38078 | c2e751a837f6d3d0d556f4cefb700d64cd28f55ea710081c0a332eec80009050 | 9d818c4594798aca9fd885035a14cdc923f0e673 |
| ku9-family.txt | 19395 | 50e00099190b1d06734a1e6c33da60ce36d7fd9473b6196d86b3a2f063bd1463 | e00e6c2726ce2a025a85f08fb0e0cd33695ca232 |
| live-family.txt | 19395 | 50e00099190b1d06734a1e6c33da60ce36d7fd9473b6196d86b3a2f063bd1463 | e00e6c2726ce2a025a85f08fb0e0cd33695ca232 |
| family.m3u | 37270 | 55569b0122a942bbf9d91d3af60b9dfc0d31b2c76605ce5e5906ccbcd30cd18d | da9f408e1ce411394efe7ad2b045da03b5dafaef |
| final-publish-report.md | 10901 | fa6f4bd5beccd2b01e4600d4aaf057e0879951a49737deb0f9bf71c9f3bcfd02 | 006fd0d24f1abe82270590955450b53ffb65c95a |
| coverage-report.md | 2190 | 53f9cad59b1afd7cfed23520aa8f62d3d278154d4096e74d647f5e06c98a1322 | 852cdedeb74c01cb0688c554559ba1624e03ec13 |
| quality-audit-report.md | 4663 | dafa9896d080af9cadde564c41accdb497f7833eb5fb0fc0891e05ac70dc973a | ab198ea2df0e7ed2a065ac8b80f32eb9a44e0ce4 |
| publish-guard-report.md | 1537 | f34bfa174f07f8fd0cc93ae26f28321e494b5c5d608b9649b08bc8e72702bbb0 | 7d5a6c38fc34f3bdecadd87f7ae3208fcb463258 |
| published-recheck-report.md | 30797 | 814e6c6cc853e287db40d9a65c9dd4fc0707d93df3f7fbab4a045ddbdbbde23b | a495948519ec1fda43cbd87c30e226e746458a4b |
| source-report.md | 8155 | 23c210625903bb61e3d553818b599a29b0fe2eaf8edee7ad857c2ba6e7684846 | 50065ee6a24da8cd7841884772e870cabf9751af |
| check-report.md | 8155 | 23c210625903bb61e3d553818b599a29b0fe2eaf8edee7ad857c2ba6e7684846 | 50065ee6a24da8cd7841884772e870cabf9751af |
| curated-report.md | 1833 | 271e8384d2d7620d9c741b2ed7f5e05d2e1bf4b1dd72c466d94471102c5daad1 | 372179ff16732790dd8d0960b9e23e188d45570f |
| sources_status.csv | 4242 | 740cceb4e2115ea674e6f191b2404aebefcb52d8d0a47436dbc8aeb3d08d2938 | 09815a5b9a8e538352ff559a364ccad177e6c6c6 |
| tv-coverage.m3u | 52758 | 079bf98d1d1e8db0131af3beb4c05873d683c439156fb10c9bb29170541d795c | e24cbb84db44599c933f43ea997ec7f128db060a |
| tv-review-report.json | 16743 | 2a4116e11e33c5fa6eb5de1d604952ec518d3c0e6f9bc8e4442fa875da8ec08b | 80145a73a4d4a7f281fabbe5f117d0d5c0116d2b |
| tv-review-report.md | 9588 | b324795f831f6912bddb85d0e2075068534f325d573d92e4f74657d65df456c7 | 9ea663547a180b6c865194a7aa8fb901ec5afc59 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
