# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 36325
Unique payload blob bytes: 23976
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 2850

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 950 | d77ed6b46dcf2b0735036c90b30bd3a299ce887301f62f19a731e73308de2638 | 54a9b6cf0ad9a3490954eda69d1037741796c51b |
| live.txt | 950 | d77ed6b46dcf2b0735036c90b30bd3a299ce887301f62f19a731e73308de2638 | 54a9b6cf0ad9a3490954eda69d1037741796c51b |
| live-verified.txt | 950 | d77ed6b46dcf2b0735036c90b30bd3a299ce887301f62f19a731e73308de2638 | 54a9b6cf0ad9a3490954eda69d1037741796c51b |
| ku9-live.txt | 950 | d77ed6b46dcf2b0735036c90b30bd3a299ce887301f62f19a731e73308de2638 | 54a9b6cf0ad9a3490954eda69d1037741796c51b |
| live.m3u | 1785 | 3ea321d9e413e46dca040a6917317aa89bbd30c68f7f45a8ee814f27c1123bfe | 667c9e394f445b4dbb9e8980c3ae091834284c76 |
| ku9-family.txt | 950 | d77ed6b46dcf2b0735036c90b30bd3a299ce887301f62f19a731e73308de2638 | 54a9b6cf0ad9a3490954eda69d1037741796c51b |
| live-family.txt | 950 | d77ed6b46dcf2b0735036c90b30bd3a299ce887301f62f19a731e73308de2638 | 54a9b6cf0ad9a3490954eda69d1037741796c51b |
| family.m3u | 1785 | 3ea321d9e413e46dca040a6917317aa89bbd30c68f7f45a8ee814f27c1123bfe | 667c9e394f445b4dbb9e8980c3ae091834284c76 |
| final-publish-report.md | 2899 | 7b500f9f478d54e68f1cf16b95580f0c5b7c70fda4ba6904535aeba747dc4c62 | b23789122b743a0526adcd571031220b0f3ce5cb |
| coverage-report.md | 1418 | 69a5a4973fc17df2a0fdb0d2febc4adfa0423023dbf65807d0821b8203c11f49 | e7da8e1ce8b8df3a4d4c8556a0375f089f233b56 |
| quality-audit-report.md | 3029 | f5f6b0d51bef63f4433268edfcb7ba6c1694914c299fe45cc552f92afc880243 | 20aa276025773f21995581a6aab5b5693757a76c |
| publish-guard-report.md | 1590 | 2ab61695e47a3816848e60880c515dc049e1885c5202965edffc47de6fdf9ca0 | d9d2917cddd63992e494b85b9117440d223067c7 |
| published-recheck-report.md | 927 | de690c27b105516502cd20b73080dc46b1decea50b560ff430c3cbfa7057a781 | e8eb2b047f7cb7596668eaea4b1ae7c777906aa9 |
| source-report.md | 5814 | 3c7fddf717d601123cb3040545d037a331124bdcb4f68bf5b8a8ef4c404a7ae4 | 1c6efa893ebf29abe8a6a765719a5519efbe3d7c |
| check-report.md | 5814 | 3c7fddf717d601123cb3040545d037a331124bdcb4f68bf5b8a8ef4c404a7ae4 | 1c6efa893ebf29abe8a6a765719a5519efbe3d7c |
| curated-report.md | 1425 | ffcf10237d18a2d63434d4b5e3c6de4f0d3018ee80a8e9f37edce5896e2ddafa | 06e3644dfb15d01af6c293710e8e01a29cba9de2 |
| sources_status.csv | 4139 | 5c11b9b9ef8c85cf95fdcdd8a440f333f6d028c7090223229a320a3bd746e657 | 1578db74395bf8eae8e0617404425e1ec4d04fd1 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
