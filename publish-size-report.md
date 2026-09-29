# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 280072
Unique payload blob bytes: 185798
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65103

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21701 | 53159a70993dab882ef5f954e920c57459d48b4b30adbb3da426e8a416095251 | 2104424172963809691613562c79bec2599e04d8 |
| live.txt | 21701 | 53159a70993dab882ef5f954e920c57459d48b4b30adbb3da426e8a416095251 | 2104424172963809691613562c79bec2599e04d8 |
| live-verified.txt | 21701 | 53159a70993dab882ef5f954e920c57459d48b4b30adbb3da426e8a416095251 | 2104424172963809691613562c79bec2599e04d8 |
| ku9-live.txt | 21701 | 53159a70993dab882ef5f954e920c57459d48b4b30adbb3da426e8a416095251 | 2104424172963809691613562c79bec2599e04d8 |
| live.m3u | 41599 | 467639289f60cc31118e3290aa96c7888c15946ebd918b2f8a2e5cb95652b355 | 229f5db5bdafacb22192c8833c1dc9b906119a73 |
| ku9-family.txt | 21429 | ad9c4a6699e2da61de366176186dfd9b3a5e9360755a1342af09209dfeae6b3f | f7bbf59fc582faa1d657796f540c76b4cfdc43df |
| live-family.txt | 21429 | ad9c4a6699e2da61de366176186dfd9b3a5e9360755a1342af09209dfeae6b3f | f7bbf59fc582faa1d657796f540c76b4cfdc43df |
| family.m3u | 41079 | e85bd77202b83aeda54f2e179b3b4b92f5d89027bd950c883b9453ffb6bc56fa | 2c2d53112fdcbdf6058be40578c97e08fdc941e8 |
| final-publish-report.md | 10741 | d5225aac3107298a8d3aa126f485a67c082ac1f30aa4f259a31e34033368525d | 4fff3cb61efdf83de32d069e9b104bdb62139610 |
| coverage-report.md | 2230 | e739595ab8a6953b2a833b1a9854753beefd0417cc110297d840672a91a0d5a6 | 43c8efe7f333d2a974b2211f9d50a12d2be073c7 |
| quality-audit-report.md | 4725 | b5103e2cfa8326d52f281aa6baee016ff2fc9f76267fea1565234b77aa25ccdc | d505edf6dd922f8944463c235d3e0099928df168 |
| publish-guard-report.md | 1553 | 8b0df6dedd1e42cbb605a33061eda1203f9eec45d1b87d71f3e2932bdc7c4a48 | b920029433adf55dda030fa6efdcfc206f72c041 |
| published-recheck-report.md | 27180 | 32117179727a3c8340043b9ed71e4d0e8ef7fb3cce0a4ba6a13107d70bebb123 | 0f6efa3afd2f1d9e03784511ca9587b7382f97be |
| source-report.md | 7742 | d0d3935a595e4414c8b6c6940a5a98557325bec6cb812a913493376974e7347f | f99f9b9ff7eed5d15f4b00eb14a10e2616a631ec |
| check-report.md | 7742 | d0d3935a595e4414c8b6c6940a5a98557325bec6cb812a913493376974e7347f | f99f9b9ff7eed5d15f4b00eb14a10e2616a631ec |
| curated-report.md | 1805 | d60b0fe9d61892fa4e889fdeb01ca49922f6f1515d544e1a95feaf5317368554 | 5fff0b3ebecd762fb64a20dde408416a37f88ca2 |
| sources_status.csv | 4014 | 5a177ef3aa91e66f5791164daa54065cf73f97358dec1974021b5b21b190e3f8 | 951635d0f61a2c1534f868d9b9825b125c2ee205 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
