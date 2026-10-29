# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 225199
Unique payload blob bytes: 153072
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 48258

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 16086 | a5cc5f99e91e085eab78b850f7bd8396118c30ccb2c47a0583727d97625748ce | 3644e11203458b024243a28d2ad90210c5ce667f |
| live.txt | 16086 | a5cc5f99e91e085eab78b850f7bd8396118c30ccb2c47a0583727d97625748ce | 3644e11203458b024243a28d2ad90210c5ce667f |
| live-verified.txt | 16086 | a5cc5f99e91e085eab78b850f7bd8396118c30ccb2c47a0583727d97625748ce | 3644e11203458b024243a28d2ad90210c5ce667f |
| ku9-live.txt | 16086 | a5cc5f99e91e085eab78b850f7bd8396118c30ccb2c47a0583727d97625748ce | 3644e11203458b024243a28d2ad90210c5ce667f |
| live.m3u | 30089 | c63b9f4b95bee4af456da351051df826c1d840359903eeab5b919ed02124bfd9 | 577394e792573e9da66982d93785a8e2604e76ee |
| ku9-family.txt | 15665 | 0567c04bdbdf0c9b6bfaeba1566dbd3e9ca235ab9f3f7e93dc78da05869682a9 | 5ffead3b0f85e17031e91bbd306791d144c293ee |
| live-family.txt | 15665 | 0567c04bdbdf0c9b6bfaeba1566dbd3e9ca235ab9f3f7e93dc78da05869682a9 | 5ffead3b0f85e17031e91bbd306791d144c293ee |
| family.m3u | 29296 | ce44de37c1cd8a20917be5cec6376d2a2eb6a163f63ecfc9762a323d628c38e9 | 979940b21a97258802d0d50636645756eeeaf0b0 |
| final-publish-report.md | 10609 | 3c78293664bc4e3f9ba98f5ace5f2ebc7dc1cfba79dd8ad7eb3e3a1ec07c54a6 | 1e252628921422a764ec0771f5a094c6a38c9d95 |
| coverage-report.md | 2210 | 55882e1539c45cd7436a9357638d752d8fd756ee8f8d40cd6b7cb64ddb61a3fa | 8fe232ee6c363f36bffdebd6243ea0b3f54be8bd |
| quality-audit-report.md | 4713 | 42ad956e0e3667ed942f4c98db4669a68c3837236791f8b3cb166fb9ae782e93 | 8eb51dbd08dbb45f4cea1662cc1bba80b130c95a |
| publish-guard-report.md | 1642 | 4d409b60909a8a6b67a69ab804f7e5c54cba9ba66f58060393cc202abd400c46 | a94a1b9e7bd3befeebc7038799641eb68994940e |
| published-recheck-report.md | 28491 | b51dc2355604fafc6fa77b922487df86c26c642921f9b6bf87516f607f896d24 | 9cd987c5de84114709c68bed6923adb33aa9c7b4 |
| source-report.md | 8204 | 1dbbb9e6ace2417b3b5691bdc92f2aeb8ab7e4dac5a291ee949270955169de73 | 923612c5854983d326a802e6b716efb3c946fc83 |
| check-report.md | 8204 | 1dbbb9e6ace2417b3b5691bdc92f2aeb8ab7e4dac5a291ee949270955169de73 | 923612c5854983d326a802e6b716efb3c946fc83 |
| curated-report.md | 1831 | fcf03972c3e2e69d4ebd43a2f32dfce18a889c5c45c958512ce7bad0980da1c2 | 48530a2bf29bd6e98708432b3d224776d915f4e1 |
| sources_status.csv | 4236 | 604340774dfc13ee89bd2b27abd099494705cd8bdef57524179873f9a1f0f541 | 92c2e254121f7345784ebc58828f5c0c1f8abc6d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
