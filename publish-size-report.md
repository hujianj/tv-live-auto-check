# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 254259
Unique payload blob bytes: 170404
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 57102

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19034 | 255eafed617a4de8931b9c017cb4aa7c148b1e1bae9c6563c478d68f9f66bf68 | 892c2a6a77dfaf123946b61dff0fdbe33f3a5001 |
| live.txt | 19034 | 255eafed617a4de8931b9c017cb4aa7c148b1e1bae9c6563c478d68f9f66bf68 | 892c2a6a77dfaf123946b61dff0fdbe33f3a5001 |
| live-verified.txt | 19034 | 255eafed617a4de8931b9c017cb4aa7c148b1e1bae9c6563c478d68f9f66bf68 | 892c2a6a77dfaf123946b61dff0fdbe33f3a5001 |
| ku9-live.txt | 19034 | 255eafed617a4de8931b9c017cb4aa7c148b1e1bae9c6563c478d68f9f66bf68 | 892c2a6a77dfaf123946b61dff0fdbe33f3a5001 |
| live.m3u | 35902 | ee41dacc7b11c0d72750c20a924277ed5911491492e94218c0013e4b6694fa9c | bdff051acfbc1136f3e5d82937635a8922087e0d |
| ku9-family.txt | 18615 | 25422941efeec9f56adf7b9e44426b77d4c5f1f20649eb31239a91c9d9d60757 | a750029a12b78b67761488815b43052d728ae193 |
| live-family.txt | 18615 | 25422941efeec9f56adf7b9e44426b77d4c5f1f20649eb31239a91c9d9d60757 | a750029a12b78b67761488815b43052d728ae193 |
| family.m3u | 35111 | c6b8da78e306e4241dfb693f65df5de2953c2df3c125b11c7c8ebac858bee4bd | 0916f084bfe4cd5bd9d90d6fccfd0deb98bb9d62 |
| final-publish-report.md | 11235 | d22e1cb7be379b0bd790e393fca9efa69e1750a8a27bc78ad8f2255a602dfeeb | 1d8789e33ce06c85e5b8241d8ccbaa0699a8af7d |
| coverage-report.md | 2210 | d0f42f123d2b9fca93c69af3829fb1bb2acd20d7c4b3411edf4dceeb0f2b18f5 | b5e6ce86c360ff20d1f36e40a390f5465f61394f |
| quality-audit-report.md | 4724 | 3eb6745cf753cce9f212e664330ae0e4fb42c780e958ab4703a347ca54940410 | 6a57fa0a50b31b48487c6d52757b20175eabea42 |
| publish-guard-report.md | 1556 | 04d28d643513f766c6b00415bc5846ff01b48be38baf830a348d4ce6da5bb465 | 1df3d30d5af7f65e7b4fc1a32344eee13d791839 |
| published-recheck-report.md | 27867 | d65621eae1f3b27fd6529e05e8adf381ba8202b967518906e373e740ad6b1cd0 | 174246c13ec197fd1f2c78f45f77b6f3d10c0194 |
| source-report.md | 8138 | a852cf12875940063dc429bc4475d5e157565668d2b30dfd43775de9add336f3 | 340fc202804fc46a2fbbe295fb3d1a0995ae29ed |
| check-report.md | 8138 | a852cf12875940063dc429bc4475d5e157565668d2b30dfd43775de9add336f3 | 340fc202804fc46a2fbbe295fb3d1a0995ae29ed |
| curated-report.md | 1895 | 49dc4458e467cae46700d0d8789896123e91d6dc695caac4b1bfed117eac4553 | e1ce6f5edf9731e1ea7d80515e832777782d95ac |
| sources_status.csv | 4117 | b717d619f18fad5aaa669385b9338b78fa746c42e1ac982318cd911c0c0a70fc | 18f37db0de6ddc99f99b0e6937025405b7f68434 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
