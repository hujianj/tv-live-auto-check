# Publish size and alias safety report

Status: ok
Working-tree public bytes: 1938490
Unique public blob bytes: 1204391
Max unique public blob bytes: 2500000
TXT alias same hash: True
Duplicate TXT working-tree bytes: 728442

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 242814 | 21b39a62072abd4df13ff7de0107a71d49a5a16a2060c5a017da01f24916b496 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| live.txt | 242814 | 21b39a62072abd4df13ff7de0107a71d49a5a16a2060c5a017da01f24916b496 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| live-verified.txt | 242814 | 21b39a62072abd4df13ff7de0107a71d49a5a16a2060c5a017da01f24916b496 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| ku9-live.txt | 242814 | 21b39a62072abd4df13ff7de0107a71d49a5a16a2060c5a017da01f24916b496 | 2b2d423dbb9f48a28731d7f134d0b121b70ac452 |
| live.m3u | 427012 | 1c2ce25d3ee73d888eea49a4a64a70988c122d917232b1273d08b326fcac51a0 | 38d3523720b192a286bb18f96db17580de417d20 |
| stability-history.tsv | 480069 | ae7ee8d3b77627d911d871058d028c9f68029a5042334d8222b46a132bb5c0f0 | 72f8aad381b33c10c57ba0cd9b29a38366d9aa1e |
| full-check-summary.json | 11244 | 945539a3e4b6a4e6fa935d0cbd4a5889a20cbaa4eb18b7439fd0ae3d66838c99 | 09c612dbe430aa15c23e1754b566750598dc9525 |
| final-publish-report.md | 11262 | ff14d22e17c6c7ed0f47a216607341ae302394f2306e8011583f703a0711f501 | 03cdf8e60e66db43b731c6bca2c9605ef9316dc2 |
| stability-report.md | 7544 | 07b7f166f969558756b7fa99ec65744562d0db028d11228d2a2eebfb4c65f8b3 | 55f6f598f2fa42945686c5dabaa1eda4bcd07290 |
| coverage-report.md | 935 | 6c4eab74f13f63ec59b27da7cba23edd61c8ff896294dd276143cd79c1f253c0 | e6df60c667cc41880bcf7b7b6f1467148f585497 |
| publish-guard-report.md | 795 | d4f9b4516f648744177cc57531898b7cdc63ab7e3cbeecd460381b73f9b4f645 | aa14c815879af87328835b455d5d67e5634d77e5 |
| published-recheck-report.md | 11290 | 63ec284b4cf9b3bba406e3edb67efbdeba3e29a7362e226ba75e55abf6d981c2 | 4f9c74e3eb581fb897810d7e2fe92c8d01197761 |
| source-report.md | 5657 | ad5067d826a08e135d8dd039e2651b03175e7f2b432870b9cd9b70dec3ea9e09 | ed11cfc67b6f04c4a5b8ac16d7243764b0de1f22 |
| check-report.md | 5657 | ad5067d826a08e135d8dd039e2651b03175e7f2b432870b9cd9b70dec3ea9e09 | ed11cfc67b6f04c4a5b8ac16d7243764b0de1f22 |
| curated-report.md | 3321 | 3272c9278e5859e4f5b067b07cab3e300549a8759ec3d6897d97a12618b44029 | fe1404fa94c50f94d5fa133c82b89dfa7650d6d3 |
| sources_status.csv | 2448 | 1dcab581e8d63eb1935bd4286b718bf9b6fdf900ec4414e0ee594e9fc34526d4 | b30300644f19aa1d8b85e84ad1569cd777a9f6bf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
