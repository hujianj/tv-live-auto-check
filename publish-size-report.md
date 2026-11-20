# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 311054
Unique payload blob bytes: 249291
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36046

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18023 | eaa200b72e5b8c06ec9170689f28ffeef70cdc6551f8edce940c7fc2a9843072 | fc643ae144c51ef765a610a09098ebda97dd4f2e |
| live.txt | 18023 | eaa200b72e5b8c06ec9170689f28ffeef70cdc6551f8edce940c7fc2a9843072 | fc643ae144c51ef765a610a09098ebda97dd4f2e |
| live-verified.txt | 18023 | eaa200b72e5b8c06ec9170689f28ffeef70cdc6551f8edce940c7fc2a9843072 | fc643ae144c51ef765a610a09098ebda97dd4f2e |
| ku9-live.txt | 20226 | 77476dcfd2fc661fca46504674fa1c214528286e7b2685044ab8cddbca47f7ca | 4b8e4ca8fc352839b10628d870f61a46b9f515ec |
| live.m3u | 34768 | 54b1933cc3ee4a026da60a5dd05ec0718710560386dda5a72e1473889f6e79b0 | cf327d01f28a7695a9f599abffffbc0f708552a4 |
| ku9-family.txt | 17588 | 7520b3d25aaf80979fc191327ef71c2985eed7671243c8bc0ff51d18bb967efe | ee6ae947cb0bb263b1c8e42df30c0bc01df43607 |
| live-family.txt | 17588 | 7520b3d25aaf80979fc191327ef71c2985eed7671243c8bc0ff51d18bb967efe | ee6ae947cb0bb263b1c8e42df30c0bc01df43607 |
| family.m3u | 33961 | 4f058efb8ecf17bff34c554d8f089da165141173d05299ccd8f2bdb0e7449fe6 | beeebe42cd7d0180e5064e667b77ab59db4cc8f2 |
| final-publish-report.md | 11150 | 0410f1a9c074496b8cf8cabec04ac362c316bd8ab8bd45ddad046ff7f1e34351 | a239187379ef5374ca44ada5eb7d8e1ce07de0c1 |
| coverage-report.md | 2200 | e42ce53f3c682e7978aa696e4e4923c5e6dcd5581f3e3bd947904a5ed920a174 | 0d3bb34b189c896a48393167fc78a904daad4e2e |
| quality-audit-report.md | 4709 | c9dcb11783655bd1ef7c46ac7c408c9e9f471da2f5385472cbd809483f765a67 | c7c2c54164b7924c3469decb7908f789c4436250 |
| publish-guard-report.md | 1541 | bc46fadc7dc005b6699a522a85353a12a0683f6cf05d8051b2c45e8230789c4a | 558a2cf2b8e01fb1e4ab52b8d98a4e3f78b63e02 |
| published-recheck-report.md | 26810 | 94a51ad73cbff59b89e4776e2dfada1d315a7653b3c56eee37ee0984d2f8bb13 | cbde4ee68930a8d00117ddf325c5086a8f0a1fb0 |
| source-report.md | 8129 | 2bcb506e0a18e02d848fcc94659b204c5b37da4bf708d9ed5bb0902e5e3d3edc | f05e23cb0de78958f568e9aafb047f724cef6ee0 |
| check-report.md | 8129 | 2bcb506e0a18e02d848fcc94659b204c5b37da4bf708d9ed5bb0902e5e3d3edc | f05e23cb0de78958f568e9aafb047f724cef6ee0 |
| curated-report.md | 1833 | 56ac6361efcede12f2a4f2305c987f01431a5b78fa8388d52097890546927352 | 726074b995fd43c2f3de1885f09182c19d7d3781 |
| sources_status.csv | 4181 | bb68a70d89ba301fb4ac68316d835bcd941ff7d53776347b5000c7be1de4eaad | 02117c10a4e9472e9ef64c6f300cd1062bfa7861 |
| tv-coverage.m3u | 46634 | 8a0c2e8f7b0da5bac6f57fa4b5f20bee92ad3266e79b4fa4be20b31c0ef80982 | 4c24109d9e1db71cca08244d016c754e56d8601f |
| tv-review-report.json | 11469 | 87cfcb32dd9fa3f02c2d1a377724c374a93458e1cda2dfaf6a4427e242b28309 | 89c429635daa9a2442ab399fb0d551ecc43a80ba |
| tv-review-report.md | 6069 | 313bef0f18d05be21739eb8625c4a3223275d9ead6b2584d52b8023d4d38e678 | 49b907417c4e8929989702b835b71092e99f3e19 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
