# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2418418
Unique payload blob bytes: 1685416
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 630174

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 210058 | c9087c7a2382cdf6550f6cb3ed0b8589e22bab34fde37e164480e66b7b82317e | e7128a4f92a72d8a4720d5e6128da58a1094612c |
| live.txt | 210058 | c9087c7a2382cdf6550f6cb3ed0b8589e22bab34fde37e164480e66b7b82317e | e7128a4f92a72d8a4720d5e6128da58a1094612c |
| live-verified.txt | 210058 | c9087c7a2382cdf6550f6cb3ed0b8589e22bab34fde37e164480e66b7b82317e | e7128a4f92a72d8a4720d5e6128da58a1094612c |
| ku9-live.txt | 210058 | c9087c7a2382cdf6550f6cb3ed0b8589e22bab34fde37e164480e66b7b82317e | e7128a4f92a72d8a4720d5e6128da58a1094612c |
| live.m3u | 378451 | c70175e3e1e9cb5cc22afdaa8dd046c581975e08b2231f994651b1e2d5d583fe | 0a2acdb8b9f85ea8f741686d528c0007f129688d |
| ku9-family.txt | 96960 | 6dead7c1a515f200b80987dfae712d33890e09f0c31833138809bf85e889fc4f | f2c6ae8a21f2c6b45c8740093496796fac4a9fef |
| live-family.txt | 96960 | 6dead7c1a515f200b80987dfae712d33890e09f0c31833138809bf85e889fc4f | f2c6ae8a21f2c6b45c8740093496796fac4a9fef |
| family.m3u | 176131 | 5df2f1407a10688c2e19c49d95aa88ff7a3b76d19dcf707ece37ac34b90ef842 | 2f5272ede4d86a315d594a7f939aa4b9d6eb601d |
| stability-history.tsv | 755174 | 0637af4e99eb533dea455a57688c0577d1936a5bd272a9d08c5468f5f14d2745 | 7d77a29e902d4f9283e6521b9e800f11de864799 |
| final-publish-report.md | 11627 | 055517a80a02357b92c19333a385c903487f182cf0988bab28f26600ddb6611f | a4cd8d1fd7dcb6f43d98f2bd7c2e90801228bd55 |
| stability-report.md | 12084 | 4c3e0977b8b92973307baddfa76e9b97a1b544b5ad8c208f6ccbe4065f7ec685 | 6795dd3c6407b0f3cca90c261532129d6315da91 |
| coverage-report.md | 1291 | 5ff254cea88d94defc4eb93cefd4d14d1d9469e260ba1603a3eeb3fc64a58a99 | 911371c841dc1a2bfe83c830324064c6c5213cd6 |
| quality-audit-report.md | 1435 | dc65443b463c0780cf86a10290f7140965081700d60f3b6150c2f8ac514513e5 | 5d4c8d45854ae348a18f5cc387236f71ffcd9357 |
| publish-guard-report.md | 870 | 8cf02cb51991c9f73ab89a8cc837d18adde8a42ba50ddb2947d150c79b53884a | b445915ec8f65f70e814798ba458f4d50eafa98b |
| published-recheck-report.md | 29293 | b0a15b7b38c38f64d0c8f44cd48022dfce19d0b9b9c21fd1bbbedaedd5927f0d | 478106a9e9ac6753b28c6e4635ee0f9924a80476 |
| source-report.md | 5868 | e092a07efdf4213b4f3d70a0a403354fe4f67890ff30abb21bec6ff8c2675d5b | db6172ae4ae8b94e8a6649b5edf4a1e99ed2950b |
| check-report.md | 5868 | e092a07efdf4213b4f3d70a0a403354fe4f67890ff30abb21bec6ff8c2675d5b | db6172ae4ae8b94e8a6649b5edf4a1e99ed2950b |
| curated-report.md | 3518 | d3fbad7fde4221d1fb8eff91275c8852d770e0fabf2f1fc54b9dea85897dc234 | d95f6924ac43f7dcec13fd112f7cef39000c0e5a |
| sources_status.csv | 2656 | 2965e0c62623d3072e888f83800c82276ea1fe6a870bf0a503727a3678bfcd35 | cfc254357ec146991d81f59b64b31ac355adc498 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
