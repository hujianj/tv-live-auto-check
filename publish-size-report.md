# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 275813
Unique payload blob bytes: 183442
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63420

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21140 | 95b2e7401f99a80894b533f8cd7059ad3ea0489a0daf7e312e4fe6d7897a9edf | bf662401cdf67187cf1e159ff33160fdeffdae3b |
| live.txt | 21140 | 95b2e7401f99a80894b533f8cd7059ad3ea0489a0daf7e312e4fe6d7897a9edf | bf662401cdf67187cf1e159ff33160fdeffdae3b |
| live-verified.txt | 21140 | 95b2e7401f99a80894b533f8cd7059ad3ea0489a0daf7e312e4fe6d7897a9edf | bf662401cdf67187cf1e159ff33160fdeffdae3b |
| ku9-live.txt | 21140 | 95b2e7401f99a80894b533f8cd7059ad3ea0489a0daf7e312e4fe6d7897a9edf | bf662401cdf67187cf1e159ff33160fdeffdae3b |
| live.m3u | 40636 | dd90e4d993f327b68856d75f24bc6d2b01841943f0710e8fb7b96f3f26817dc7 | fd4ff0352742557dcff93318179150b6dfff1934 |
| ku9-family.txt | 20919 | bd62d1b5ab3e9a03989f88cdf3a478036607a1b15a1362581bb671cd96e636f1 | 56447a0bc4738d57829385525e7ea2073c7339a3 |
| live-family.txt | 20919 | bd62d1b5ab3e9a03989f88cdf3a478036607a1b15a1362581bb671cd96e636f1 | 56447a0bc4738d57829385525e7ea2073c7339a3 |
| family.m3u | 40229 | 66b8cb19a75e414b157fd9bd08922a547238a7cdea4b273a4ae3bcc1d0594184 | 0054e0efcf8ec048dace105cef2a905293f8311e |
| final-publish-report.md | 10891 | 1641cb71fa80b20fcbf715fa47b265b8e5cb58749ae444eb87c23226ae2cf377 | c8a2d480318a46d1d90d3d46b90fa2d6db0a08f6 |
| coverage-report.md | 2240 | c83a0a801b1fd84331556ad69ef018de216057844825f95003f66921b7fcad71 | 29cba6c7cc5d27881423e1b5b4eea9d00f678eec |
| quality-audit-report.md | 4730 | eb3981b4abc15bd147fbbaed0ad675652507e689609f14ed59416163ea4cd065 | b92e4ed77285c64456cb95e2b9257877bb15e5c6 |
| publish-guard-report.md | 1588 | 78456a21e6871b2ec784d8145ba7b08f15b836904596387d8087dfe7c8e4a417 | ef194fc8f165dcdc42975ff5b737d881b99d8367 |
| published-recheck-report.md | 27147 | 4a04418d9490b4c28ba12d287e515af7aeb0f0e3fadb5479c1f93c0131c7e9f4 | 563b2f0e4a9331da3d4f7e8fb4bd3a44d7d300cb |
| source-report.md | 8032 | 3da0d345effab6e4cca40a0959be6576b8a8fdb98771f1c3143d2db03cebf2fe | 985050b85044840e066de2dd1111df0edeb126de |
| check-report.md | 8032 | 3da0d345effab6e4cca40a0959be6576b8a8fdb98771f1c3143d2db03cebf2fe | 985050b85044840e066de2dd1111df0edeb126de |
| curated-report.md | 1806 | 678a3a5c6ed0edd87570497126decd3165cdf26bf2d1ed9e9a5a3f1f99a6aee9 | 87d4f880ef33adb8a50ea505e3fbd0107e858d0f |
| sources_status.csv | 4084 | b4f276cc3bdc30bf3aef93d6ee3febcb1d4d935102bec83934ba1d28d725d99b | 2da0b70b2583a380864ef296c2c4c420466fbeb9 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
