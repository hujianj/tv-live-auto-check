# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2427517
Unique payload blob bytes: 1694756
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 630267

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 210089 | d2d4e085cb74644b30b2a593de7dadc02e4d118fa237602b0d808aa7e97a3d7b | a0f59ad73d63afc6e4166ae72e02358f80b54052 |
| live.txt | 210089 | d2d4e085cb74644b30b2a593de7dadc02e4d118fa237602b0d808aa7e97a3d7b | a0f59ad73d63afc6e4166ae72e02358f80b54052 |
| live-verified.txt | 210089 | d2d4e085cb74644b30b2a593de7dadc02e4d118fa237602b0d808aa7e97a3d7b | a0f59ad73d63afc6e4166ae72e02358f80b54052 |
| ku9-live.txt | 210089 | d2d4e085cb74644b30b2a593de7dadc02e4d118fa237602b0d808aa7e97a3d7b | a0f59ad73d63afc6e4166ae72e02358f80b54052 |
| live.m3u | 378416 | 354a3665bb8656e267762fc74b172c9cc42a5182e466c6016a6a6b53cfdf35b7 | 06fefe6ae608a118c518125ab8135534ec0fb68f |
| ku9-family.txt | 96640 | b7d984dad5e8ad9c6eaabf617dfc328e887e41abca286ddbc6ac14b25a561db9 | b48f76455233db56e98a296b41975b0e04abf90d |
| live-family.txt | 96640 | b7d984dad5e8ad9c6eaabf617dfc328e887e41abca286ddbc6ac14b25a561db9 | b48f76455233db56e98a296b41975b0e04abf90d |
| family.m3u | 175005 | 430f292e2007f86c49d2c378764afac91c47c0b31f5f18c22b9e2ec92e861251 | 3b9c681bec62835c6b0803b5c97b0e7b3670fcef |
| stability-history.tsv | 765040 | 83db49de8629279ed6782a16c87fbbf9ba2b9541707e76eb4d69630628cd1904 | 1a4622ac487ededac11985ef7286f1238472508a |
| final-publish-report.md | 12090 | e3151d0c1f66997d271a3dfe399fd8485084d96a5d938b8e47bf3363d6dbe8db | 3163ae26ec2a8122337b4e522fb0864c36ec1c8e |
| stability-report.md | 12868 | a16beb1e145bda2d93ae35efd3f4302afa7fef070dce2e6bf7ec92d8705b8ce6 | 898cffc8466308e7f57d4c1780156d44a7f5ab96 |
| coverage-report.md | 1348 | f4d5c11a2f38e0a6437408515065351dc30e3e7dd1145be0b73e202dbb4aff5a | b0636ff7e6ad78311d84f3a3a0f5f832fa542ab7 |
| quality-audit-report.md | 1435 | a5b1da7f782bb0e8937b4a4e7267f6b7bc47fa7328c10cbfdd52d535eb3e5740 | 976cca4a91bcc883324c8ce3652464bfe69febdd |
| publish-guard-report.md | 786 | 7f89e79ea4b0e7340e6bdb6bc7798b7edd38e9735864a8316af7fceffc5d019b | c48fa17e41964685d326c4cc870f093e02428739 |
| published-recheck-report.md | 28998 | 8b96457af527ef789243d18e8eb509961fe9f8009d0f132c671ec92ab54d10a9 | fc605e3634049eff87d2dd25299ea434b25993e4 |
| source-report.md | 5854 | 88a7c7865d82619f66c629dd20215fc5f1d3b020823e451ca66f36bf0af46ad4 | f0446834a51e1fb0114ebe7a8e8b35c5db9818fe |
| check-report.md | 5854 | 88a7c7865d82619f66c629dd20215fc5f1d3b020823e451ca66f36bf0af46ad4 | f0446834a51e1fb0114ebe7a8e8b35c5db9818fe |
| curated-report.md | 3586 | 3c3a3747dc333e5711be046078df139be9b735ab143cdf9bbc8ea9717c63e91a | 865c5506ea54dca3eab61fd9a6d111c794eb8b46 |
| sources_status.csv | 2601 | b9f8fe0533235753e3d1222625613174c9a685bce5089cfb0a7e2b0b7a62f106 | 99329b10c89b5c6c18d1f201a9c52beab27d1aa3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
