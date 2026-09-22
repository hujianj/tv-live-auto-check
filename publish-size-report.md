# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 291072
Unique payload blob bytes: 192899
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67851

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22617 | 800bb39ca511df21c082f91f781c2194b1bc0440cada5d8df317471f6b3fb13c | 4fc12436d877077fac3cffb43806aed5d71b2dbd |
| live.txt | 22617 | 800bb39ca511df21c082f91f781c2194b1bc0440cada5d8df317471f6b3fb13c | 4fc12436d877077fac3cffb43806aed5d71b2dbd |
| live-verified.txt | 22617 | 800bb39ca511df21c082f91f781c2194b1bc0440cada5d8df317471f6b3fb13c | 4fc12436d877077fac3cffb43806aed5d71b2dbd |
| ku9-live.txt | 22617 | 800bb39ca511df21c082f91f781c2194b1bc0440cada5d8df317471f6b3fb13c | 4fc12436d877077fac3cffb43806aed5d71b2dbd |
| live.m3u | 42997 | 929d22f1419d62818248328fcff1202c35a93f5af93c9e32c9e9d85686d194fc | 9dfb554d9edc5ebb6d7dcdb83594b43a8db4688d |
| ku9-family.txt | 22194 | 3e47fd6a8f100564c43418d3c7acf98d31089546bde30f47e42e43c05ed4719e | 98d449e7372d748f60ec214d7658c68f3b19b346 |
| live-family.txt | 22194 | 3e47fd6a8f100564c43418d3c7acf98d31089546bde30f47e42e43c05ed4719e | 98d449e7372d748f60ec214d7658c68f3b19b346 |
| family.m3u | 42202 | 69f385598e18098f23875e1ddf769a1dadb7b06649861af18a9082b1de595064 | 867f4c81ff4441ef241c09d5486dc1194e5b98f0 |
| final-publish-report.md | 10834 | 00aea985716671d40472405763ee52323f99400aba0cc71552de5d2faf5e92eb | bb0a5a78f125a1657bf70a3557ff18bd658f2e28 |
| coverage-report.md | 2230 | ba8e9e21781f7b79658ebc13078ffa4770a9a21bf872c7f6e1db40ac77832bdb | 880dee96e5e07c35177f2d36c1e171434d3e6403 |
| quality-audit-report.md | 4728 | 4d2acc2731e84f55b8ccefd922db79eb4d1219f1cb776cc6128fc0acf8e5c67f | c611dc2f510158cbe4a5e42981c1e7d95266436e |
| publish-guard-report.md | 1615 | 44fd414f48a29337a645981e0fbaaed7e2f8c04842d66198ebd792ab7c96d275 | b562d0982eb168131e2d5eb7196513d72484bcbf |
| published-recheck-report.md | 29418 | c12bf7bf4ed128a471a4998bc5a6e885617b82ce1267e2ae38a5a1cc38249a88 | dcf76f44d55e481777bd4fdd02ed5bad0db757a0 |
| source-report.md | 8128 | 67a7f1b31b20da9b0aa1d6a67d113044f6c6d40640e8cc6ac1785fd2c1229d92 | 79271b3541204758f2b53add726ac868fdf8c16a |
| check-report.md | 8128 | 67a7f1b31b20da9b0aa1d6a67d113044f6c6d40640e8cc6ac1785fd2c1229d92 | 79271b3541204758f2b53add726ac868fdf8c16a |
| curated-report.md | 1804 | 326752dfcf9c4711068ebec6b7121b149e1742f2cf064eb19d202e896e63a133 | 2b012bab17d9330332c7cbbb534b9efddee7d809 |
| sources_status.csv | 4132 | 0d2d5bfe34cfcad3f996b150c58b320d527dbcc9b2044ac6df2cd869cdcb9139 | 9f7326a72b4a4a247d73697c97db767dffc2451e |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
