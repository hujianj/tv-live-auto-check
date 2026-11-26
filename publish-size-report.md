# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 318361
Unique payload blob bytes: 255813
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36588

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18294 | 1b190ddbe187a5c78b88ad955cbb2d45954cdf9ba62c7b8c595a910518ed5bec | 17a948eef0f95e38ebbcd778f1bf46c8ce9d9aaf |
| live.txt | 18294 | 1b190ddbe187a5c78b88ad955cbb2d45954cdf9ba62c7b8c595a910518ed5bec | 17a948eef0f95e38ebbcd778f1bf46c8ce9d9aaf |
| live-verified.txt | 18294 | 1b190ddbe187a5c78b88ad955cbb2d45954cdf9ba62c7b8c595a910518ed5bec | 17a948eef0f95e38ebbcd778f1bf46c8ce9d9aaf |
| ku9-live.txt | 20404 | 2fd8b941a1b33b49782558829992463e4e2ea770d35ff128d2b40d7fcea600ff | 905925860a6ed49dc1cc26d8a19b1642991e32b7 |
| live.m3u | 35282 | 22f874981b1c140c278c0bb97fa41f1dc5b58ccb8c5d6225ebf9c67b7cec1e50 | 2a09908bc52803fb7e5890c76e8437401b7a6368 |
| ku9-family.txt | 17810 | cc0618b46eb6060455719b67f946dc3d2c4a651d09f26ac4ca2c2dfce45913d1 | af7c97b59c10f30b2c6723edcf13fbbb3312d446 |
| live-family.txt | 17810 | cc0618b46eb6060455719b67f946dc3d2c4a651d09f26ac4ca2c2dfce45913d1 | af7c97b59c10f30b2c6723edcf13fbbb3312d446 |
| family.m3u | 34367 | 6bdb4fca600d9239782976facf3c3d67bb5d6b6c0bf8400d2ebff9df44b576bc | 09ba69fe5d47be80a9d8165c69dc495a0db71e9b |
| final-publish-report.md | 11369 | bd2b5524347cc12b6751a1683028c389d7d74dc4b6f435f66ab1f6e41edef645 | 5052b6e65ffa7a2409b39c8c6121b7d984590d53 |
| coverage-report.md | 2200 | 7d1a0be6cf12769f0c5a9a42b8b7840a395116c921b828d7b87be92c97ad67a0 | 1f8c6e92d6a2c3d65cdc16b3ba3c98ec749e17a8 |
| quality-audit-report.md | 4720 | 2bf3236ccbd0cd4d2393f7044d654954354e78512a4af68d171e4865bf8647f2 | cf1190e1513fb22d9000390b9743f3e43b898eb5 |
| publish-guard-report.md | 1569 | 9a9e6456b6f1291702209dc414b91c7f428ace7727ed07d9a16de316658d8e88 | 48070618af8946a489a95b28bdeab6859380fc3d |
| published-recheck-report.md | 31855 | 138d9ba6596819b6af592f43fb4e663db7bb1ef4728d10fc07b0ec748ee4681d | 4ef00d4f7ebe7c5f8748e1e43f50e8dca81176d2 |
| source-report.md | 8150 | 657ae1b6393e124f830cb46a287a254ef20881856d3799c9241688dc5bce91ec | a0184e107af54737f58c23c76c59b2d7e50055c4 |
| check-report.md | 8150 | 657ae1b6393e124f830cb46a287a254ef20881856d3799c9241688dc5bce91ec | a0184e107af54737f58c23c76c59b2d7e50055c4 |
| curated-report.md | 1835 | 5420aee5a5871559984fcfe0884b31745676fcd29f7cf228399399cb56a893da | 77dab70762dca068390c7d523e2d68d1ac04f88d |
| sources_status.csv | 4181 | c85a0f1ccba4fa74e10f55902830d5b5f5a841f380bffa9b7c4eadc5947ffd4d | fe940c8b648d704318de7f324d5712a605db6ebb |
| tv-coverage.m3u | 47062 | 7852ebafd8fce554b36781c2c40c801e7c1618f14e5f8e5dcf185c40c4c8b34e | 227e8a21a8f1dc7cdf008d045f453f27fd25f7de |
| tv-review-report.json | 10960 | 8c2dfdd6a499c198c7a4cfd91f393c343e277a781e86688a63b2b5914c6c0d5b | 9cfa0bbdb17990551ea5a61fda0aa5e5c47006c6 |
| tv-review-report.md | 5755 | 7234269bfcea92c0628bc28059444483697842e38c02e11c2a68be563bd0f1d2 | bdbb98a68c1b2803bf5f69e6e27a44770c20205d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
