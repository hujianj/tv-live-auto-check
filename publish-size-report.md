# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2467657
Unique payload blob bytes: 1688777
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 674775

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 224925 | 8699c7a1e0350b92b2b222e5431e722b8829be2a2f2dc999ebe13a668ca80c14 | e31f70e7e974c488f6ea9a5bdec11757c29ee1f0 |
| live.txt | 224925 | 8699c7a1e0350b92b2b222e5431e722b8829be2a2f2dc999ebe13a668ca80c14 | e31f70e7e974c488f6ea9a5bdec11757c29ee1f0 |
| live-verified.txt | 224925 | 8699c7a1e0350b92b2b222e5431e722b8829be2a2f2dc999ebe13a668ca80c14 | e31f70e7e974c488f6ea9a5bdec11757c29ee1f0 |
| ku9-live.txt | 224925 | 8699c7a1e0350b92b2b222e5431e722b8829be2a2f2dc999ebe13a668ca80c14 | e31f70e7e974c488f6ea9a5bdec11757c29ee1f0 |
| live.m3u | 401969 | 4f1c840353b00974d0d91de1682262bfb4bdd408246d21e7a46dad3f3a23f505 | 54d1418478a4f6500176c85eca3cd8aebaf81369 |
| ku9-family.txt | 98249 | 1b5f481a55bed4e7a2ad2ac273769d7f3e00fb182ceedcc68be3e68d9d3f501f | 3ef74c28ec7a630eb75c576b0547127152a92d48 |
| live-family.txt | 98249 | 1b5f481a55bed4e7a2ad2ac273769d7f3e00fb182ceedcc68be3e68d9d3f501f | 3ef74c28ec7a630eb75c576b0547127152a92d48 |
| family.m3u | 177934 | 35279c9c6b18177d0068734ea2cb59d0e9d53c878764b39efc16db7160964a6b | 5721cba9e5907a995f280fc64828a05e09821cdf |
| stability-history.tsv | 720401 | 9e134ae42c8f9437ab8c47fd792313deed7b51e0a1fe018dc7910cf79cb0aebc | c20dff26db5f80c0e3ea103fae432b9684585147 |
| final-publish-report.md | 11872 | 070d20ec2225ca0093f1892e7b3936690583c8eaf8235e0ee7018c9181f6119c | ced46e60b918e3dc78f38e28d8e552116a6d0b5f |
| stability-report.md | 9569 | a2ac59202e2a98b4a5ec9fb3eac7bbc8299d26f6ebb4767de0616858d727ac4b | db1e7eea0640cf5086aaaf34c67f906e83386467 |
| coverage-report.md | 1329 | 260d1d65351fec1724a4c644a4d07a6c0f18d6034682f708b56173382314f945 | ec839b13d59b78bd6421d8f23e70cf2ae6f1e6d1 |
| quality-audit-report.md | 1435 | 7ab069377ac0a075ee410cd9f69dc3dc40ca5618714b7a6eaba282f2804a909d | 0fa63757aae257a9c052bf50d0578b188e5ae7aa |
| publish-guard-report.md | 790 | d5f2714ec7cc9e7738ab805c54bdc7e81e5ae145effd8fb25664d6910d835f78 | 80801d9aa57c94ca1991fc33d814551e2c2d05a0 |
| published-recheck-report.md | 28231 | 7b0c9caacfa03319bf16ffda04ffaf9ef607ac2d8a875e0c9cf84cdf6b9e3cb1 | 0132aa4bed5282ff20b13401d2d6a4eb72293a7f |
| source-report.md | 5856 | 56936bbed5a224533dc1df0b6dc7f593d676e5272e24ff1e88c3520ec7b9ae37 | 4b9073fcea3c8528dbce24268ba6f8d1a1c2e572 |
| check-report.md | 5856 | 56936bbed5a224533dc1df0b6dc7f593d676e5272e24ff1e88c3520ec7b9ae37 | 4b9073fcea3c8528dbce24268ba6f8d1a1c2e572 |
| curated-report.md | 3614 | 1160548e36e1360612432bef167f45df6dedb1d80867c854ae28fc54d6dec69e | 05fecb73233debf45231ba3c2d532602264c2668 |
| sources_status.csv | 2603 | b76e4a83f34d048257f08c64afdebc9989206f02b3078a816fe45407230831ed | 945c1054c779698f62b997d3b20748803af7b504 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
