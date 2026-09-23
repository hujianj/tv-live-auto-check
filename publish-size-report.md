# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 273720
Unique payload blob bytes: 181756
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63117

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21039 | d9e26bb5fb2651e17e2c09e3094fc177d21017509dbff3f14c2089265a8333ca | d9e142c7836891d0bb44bfdd55c19fbcce94894d |
| live.txt | 21039 | d9e26bb5fb2651e17e2c09e3094fc177d21017509dbff3f14c2089265a8333ca | d9e142c7836891d0bb44bfdd55c19fbcce94894d |
| live-verified.txt | 21039 | d9e26bb5fb2651e17e2c09e3094fc177d21017509dbff3f14c2089265a8333ca | d9e142c7836891d0bb44bfdd55c19fbcce94894d |
| ku9-live.txt | 21039 | d9e26bb5fb2651e17e2c09e3094fc177d21017509dbff3f14c2089265a8333ca | d9e142c7836891d0bb44bfdd55c19fbcce94894d |
| live.m3u | 40555 | 76b33d6defe8b09ddd1de91af276715d8c50a7975520f4289363a98d89500fdf | 9ed458200db9703e74b7236bd93ee5b18cc935a7 |
| ku9-family.txt | 20774 | 93bbdad724a859d0ba8e7ce53a9ff6334a8f7eccf1494bb64612bdb0d45bbb02 | 3a2768412f7d1ab157887aae1955840af3e26c97 |
| live-family.txt | 20774 | 93bbdad724a859d0ba8e7ce53a9ff6334a8f7eccf1494bb64612bdb0d45bbb02 | 3a2768412f7d1ab157887aae1955840af3e26c97 |
| family.m3u | 40042 | bc760c80ce7b8798ed84244b6b3a7564b2385f5800d7c82ad8f04651413b0439 | 0e83ee1f2718d96f5ebfe14d01b657187b1c33e9 |
| final-publish-report.md | 10612 | 157d88615462472de34b3249fe4fcaeb2ecac19dd793ca3a37dbf9d58254433a | 1f1a2a02094dfbf503a88f7ce15416499e1fa3fc |
| coverage-report.md | 2230 | 2ec4f90d8ec79c70cafc0835dc4fc024ab07e99f6317b8f88371b06b1b8169e7 | e504d613e4fd672a2764c3609353c5c8f8cec9a1 |
| quality-audit-report.md | 4730 | 2d387935d0cd2e57f16977a374dcb89a52bdcc521d9d2fdf0a4e21ed50704908 | 4d00c6ad1cf3fb43c1f1ca12bbdead69ad7656c6 |
| publish-guard-report.md | 1556 | 06054275bbcb6bb4826109d36cb3cdcb441235b6da401be813c31e0dc920e7be | f122722a98cc070791f90253bb09e2d72b966cd9 |
| published-recheck-report.md | 26208 | 03003f8fcf20afc45b47443791c92f44dd0ce1fccc8e42136e819edcf70a6752 | 5056c3d86763254747738a8132938ce4934ea7a6 |
| source-report.md | 8073 | 674cb5ec9eea427ccb1af12fd0eab7ea0b3a58a41fb0bcd259778934795022a6 | 2525afc21d1baad66761dcff7a22e41464b8fee4 |
| check-report.md | 8073 | 674cb5ec9eea427ccb1af12fd0eab7ea0b3a58a41fb0bcd259778934795022a6 | 2525afc21d1baad66761dcff7a22e41464b8fee4 |
| curated-report.md | 1805 | 05da74289f4f31b09eec4c1be99adf9c133e92a9bba6f2dfe615bd468f648dac | 140044bb1a4ee31f880893de345e376afffddac1 |
| sources_status.csv | 4132 | 6c795920b1d7ec7ff951a95f027b29518f62a2e8b26bbfcba23f65d179adf5c9 | 98a5f538c7753c45ff6a388de7ec6a77a21fac7b |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
