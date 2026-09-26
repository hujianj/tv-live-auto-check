# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 276816
Unique payload blob bytes: 184052
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63705

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21235 | 4f2ff5732c99b1dfd1909b6125e52037cb99374ae2458503e97119c1a8fac8d7 | 45e74fda3917bb4ffea225a9673f764c222fe07c |
| live.txt | 21235 | 4f2ff5732c99b1dfd1909b6125e52037cb99374ae2458503e97119c1a8fac8d7 | 45e74fda3917bb4ffea225a9673f764c222fe07c |
| live-verified.txt | 21235 | 4f2ff5732c99b1dfd1909b6125e52037cb99374ae2458503e97119c1a8fac8d7 | 45e74fda3917bb4ffea225a9673f764c222fe07c |
| ku9-live.txt | 21235 | 4f2ff5732c99b1dfd1909b6125e52037cb99374ae2458503e97119c1a8fac8d7 | 45e74fda3917bb4ffea225a9673f764c222fe07c |
| live.m3u | 40953 | fc4138f5b459c9122c867a9c102705417cb0c6b1c6e234c8137bb3fe60198445 | 8b96bf5fc644b7f5a658f874d2ebf679331c575e |
| ku9-family.txt | 20970 | 3c30f12bb760e76742258282ce85dac5147378dc021d34549cff9b71013389a1 | 09bc61f77abb58af3c4fe791227ef5e422a6cba4 |
| live-family.txt | 20970 | 3c30f12bb760e76742258282ce85dac5147378dc021d34549cff9b71013389a1 | 09bc61f77abb58af3c4fe791227ef5e422a6cba4 |
| family.m3u | 40440 | 515ddea07e789d20a2dd62be2f6afff2bd429ab34b631a3a0da9f7504977cae0 | 21758360e6059d542e2c2966130224360903882d |
| final-publish-report.md | 10722 | e98b43b288e5ba828711941d3b3f5cfa3c09264c25ac681d441f1434b43729ee | 1611d55d0f4230775c8362bad6c7baf7a56a516f |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4730 | be5daca1321a1526b4b8d918a5556c2378c892131ac8dc9f51f565a1d6498887 | ccbde66e9f468f8c32881a2609ec74adcec203d4 |
| publish-guard-report.md | 1610 | a813d6b8fa31b73a80ab7c64c21fa5bb00f7fc4dca99dc474d2bb61a4950d1b8 | 80b58966d54f8dd18f45851bba1ce4d9e732f45a |
| published-recheck-report.md | 27137 | f37d8e7f9c05f57e65e12cfdf98aec6d57b8a9526474fcc05cd512d7511627c5 | ae3c5834d175765603723a63cd85162ec03d7d60 |
| source-report.md | 8089 | 8432a64494e6bc791dcc25ff4432fd08d0fbc744aa3e77794f2564ee857b80dc | ca2bec690c7166b716e927959582e567bb593f55 |
| check-report.md | 8089 | 8432a64494e6bc791dcc25ff4432fd08d0fbc744aa3e77794f2564ee857b80dc | ca2bec690c7166b716e927959582e567bb593f55 |
| curated-report.md | 1804 | e019e71a80d5c293d7a76f7eee82500c348402457aff141c93c759f434162bc7 | a6518f159f8386d8b0215f4956eb71d9e411e054 |
| sources_status.csv | 4132 | 4155a9246d7d0637ec47c82db7bf06204609104a2f5642431a015667ac51fdda | 51d8d99428e91c41ea5400d97e6312dbe874a1e6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
