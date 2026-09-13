# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 282378
Unique payload blob bytes: 187055
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65628

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21876 | 6adcd8c1d5056ed06fb1451c3eeabf5bf84b98183cdc76b93d309ccad04e498e | 0b78e057a105fd0639cd77a8a15963aee352cfda |
| live.txt | 21876 | 6adcd8c1d5056ed06fb1451c3eeabf5bf84b98183cdc76b93d309ccad04e498e | 0b78e057a105fd0639cd77a8a15963aee352cfda |
| live-verified.txt | 21876 | 6adcd8c1d5056ed06fb1451c3eeabf5bf84b98183cdc76b93d309ccad04e498e | 0b78e057a105fd0639cd77a8a15963aee352cfda |
| ku9-live.txt | 21876 | 6adcd8c1d5056ed06fb1451c3eeabf5bf84b98183cdc76b93d309ccad04e498e | 0b78e057a105fd0639cd77a8a15963aee352cfda |
| live.m3u | 41894 | 2f3ef310f2c31475a232db2b7489bfdc5a5cfc5e734402da0292997c264d1ad5 | cab49f112f3fca77c9845ef0c13988c77b3d1586 |
| ku9-family.txt | 21611 | a24c4d86338e828787f00192cdb2968371fec87d76b218f960063054c7faac5b | 78324feee05e39a3e6d9a8b240046273bf85bbc7 |
| live-family.txt | 21611 | a24c4d86338e828787f00192cdb2968371fec87d76b218f960063054c7faac5b | 78324feee05e39a3e6d9a8b240046273bf85bbc7 |
| family.m3u | 41381 | 2ac7b9561b072f435e42933adcb84906841f5691200c059a284813f2fd0716f9 | 14d723aa7567496bdcdfb65a1a9c617888605461 |
| final-publish-report.md | 10675 | c4de3af3e4c23478f5b76a92db7ba32cbaf3091afb1e66c2dfce5d8abf064ac4 | f0a899a678f472c93ffdef54af24dbf87ef70a97 |
| coverage-report.md | 2215 | 0563ac94f5a1fd9e859f160db25d8db88793d4450a5f0a53ef56b68cb706125b | 6a634bb6a216f7a066938a9d5179b9669ccb9c5b |
| quality-audit-report.md | 4727 | 90ae8146f2dda88b6ad3076951a716d4f5a55be961421b1a27992c901bc809cb | 4f4bdfaddc6745a5183166a7da9b2e6f1340845c |
| publish-guard-report.md | 1560 | 441b3897b871ce0dea0d95e97b9093b3ac71659ae8249d5b4d0ff0b521429b9f | 23697c78acecb85cd8c9c1d4d2eb5b03419f1c7d |
| published-recheck-report.md | 27032 | 2dce50f5f849bfffdb4aa4b7d5de16c36cce1a4ad617b239635e69d146fdc4e9 | 60b7f6a1a40d38b17958220ae750823d58b8a387 |
| source-report.md | 8084 | 3b6eca8eab9c4bd3082fcd9958796d692bad4bcaa1e5e73074d50f23497e2bb2 | 4843f4ec6f96e473a3fc5b37cc3c93c3a6b97438 |
| check-report.md | 8084 | 3b6eca8eab9c4bd3082fcd9958796d692bad4bcaa1e5e73074d50f23497e2bb2 | 4843f4ec6f96e473a3fc5b37cc3c93c3a6b97438 |
| curated-report.md | 1861 | 335902039bfa8e50d31c9b93ac062511ca4c530db166d3fa370ce099676c0cbf | 596c2c143782024545210e874e2c41719a129c3a |
| sources_status.csv | 4139 | 7a47a2141e489085e89a02cfb58565106e0dc502129d96b197d4931a6ea2f80b | a00d552f9020ca9023ac239f5c9ffd8356e4dc09 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
