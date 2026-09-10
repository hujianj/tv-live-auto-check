# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 209570
Unique payload blob bytes: 144185
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 43275

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 14425 | aea6b4b4140358cded02462cf190a9cd2445018db44191f2b97d7892f982d712 | 7e34070992394ffad90f00d09931cc04fe0649ec |
| live.txt | 14425 | aea6b4b4140358cded02462cf190a9cd2445018db44191f2b97d7892f982d712 | 7e34070992394ffad90f00d09931cc04fe0649ec |
| live-verified.txt | 14425 | aea6b4b4140358cded02462cf190a9cd2445018db44191f2b97d7892f982d712 | 7e34070992394ffad90f00d09931cc04fe0649ec |
| ku9-live.txt | 14425 | aea6b4b4140358cded02462cf190a9cd2445018db44191f2b97d7892f982d712 | 7e34070992394ffad90f00d09931cc04fe0649ec |
| live.m3u | 27685 | d1f8a2d91d7aff8c90d326386139119493c08fab71a07455c4055ce77e049a6a | 58fa7f23d3a6a36cc9d6fc56374c1c229186413e |
| ku9-family.txt | 14160 | 0de0893a31dd548855d2959c1891d88b0e13c0655f19d9fa18641659961e3a83 | e4ebb0d885b5bab2e371a753ab8d14b67110f6f0 |
| live-family.txt | 14160 | 0de0893a31dd548855d2959c1891d88b0e13c0655f19d9fa18641659961e3a83 | e4ebb0d885b5bab2e371a753ab8d14b67110f6f0 |
| family.m3u | 27172 | b1944bb269ef308e5e117f6382fb86d3cdf6daa20e02dae41be0e58f72cac3ed | 81ef820644216a8249bf3a9348615ea9e05b2df4 |
| final-publish-report.md | 10556 | da688ddc7ec5e058959f29855db2d2305629f9f620ff1cf46731cf4606d2050a | debafdc3ccde475d1f01543c235b7128510a17a7 |
| coverage-report.md | 2235 | 3cacc220042a590a092b589db68f6d2143975c2312118a0a8aac6dfa234cef55 | c60f6595b94caf0af6a637c7d219582ab286e5be |
| quality-audit-report.md | 4722 | 555b05a0c111a34d46fb18407529c798cdd2b9534299706622122e3c9b5463d2 | 77ed84fb6ad60a7eaacc075bc5c47538f4d00548 |
| publish-guard-report.md | 1685 | e5330ddea540a952891c19487eaaa3edd2f19bf345cf9471dedb49d37b0bfca0 | 5bb0ad31ac0eba81ac8939af4e159f2d66caf5bf |
| published-recheck-report.md | 27631 | a8e7b7b35ef651bcde3fb808aa0d9e6cd9a5cbd5e1a9fbf3c7f1b6cbf54e4aa1 | 4d3b7dfee9c58315624198753b96459584d3fd8e |
| source-report.md | 7950 | 61f2b3645489361dfd76b0a89d227325df413fd247d48bf64597776af12e5fc2 | 0422209325532d5b6067aac0b3ef827350832191 |
| check-report.md | 7950 | 61f2b3645489361dfd76b0a89d227325df413fd247d48bf64597776af12e5fc2 | 0422209325532d5b6067aac0b3ef827350832191 |
| curated-report.md | 1858 | 8421faa42c669b115ab4e3b79598f2f1d534c84e669fbdf8944a2549ca6103c3 | de9da8614c77f5d5d3b5c3062331eb84c6415c1c |
| sources_status.csv | 4106 | 78f80ebeda34250b2b13a344a28ecfcbeb1b3b726703213ffa9586a5afd740f2 | 464bdc211592c26b8d961f09e13a7a7a14d82536 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
