# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 284958
Unique payload blob bytes: 188653
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 66405

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22135 | 08cee52171234fd0ecca588ab698f68bf9cbbbdd550b871b04767129198832e6 | 4cffe069fec993b6cfa019b2b5037953b1fcb98b |
| live.txt | 22135 | 08cee52171234fd0ecca588ab698f68bf9cbbbdd550b871b04767129198832e6 | 4cffe069fec993b6cfa019b2b5037953b1fcb98b |
| live-verified.txt | 22135 | 08cee52171234fd0ecca588ab698f68bf9cbbbdd550b871b04767129198832e6 | 4cffe069fec993b6cfa019b2b5037953b1fcb98b |
| ku9-live.txt | 22135 | 08cee52171234fd0ecca588ab698f68bf9cbbbdd550b871b04767129198832e6 | 4cffe069fec993b6cfa019b2b5037953b1fcb98b |
| live.m3u | 42533 | b8303865c5dd3e4f09ec114ae01dbd08cdd3b05f15894194a2690a6e639febbf | 712245c370699840ab0120a38267d3589bd63e16 |
| ku9-family.txt | 21870 | b517ba2fdb0a73dc4ee8ea0fac70227117a0f7add96e257b2444acf532f30a5b | 6eae1a6bd90fe34c41878c21d037c3c9f1ceddf3 |
| live-family.txt | 21870 | b517ba2fdb0a73dc4ee8ea0fac70227117a0f7add96e257b2444acf532f30a5b | 6eae1a6bd90fe34c41878c21d037c3c9f1ceddf3 |
| family.m3u | 42020 | 393312a683f17be258b9f39aa8fa3b85adc5eb05d539587be1ea303c32e4fd83 | b1715eb81054c83e6ad7da09a754fb8f9fb30080 |
| final-publish-report.md | 10653 | 16f051c206a6af2737d1fb45be26dea84d3dca5b7ef379797bf89529c5db2926 | 850a84fd658b97c531591f91dd035d5ef02c956d |
| coverage-report.md | 2220 | a6531e157c5f17edc7b0be3b1b319e9c162078728ab19a87ab19d07f26c2c10e | eaadf19cd99cb0d70f799ffb467bd020ab4f6af9 |
| quality-audit-report.md | 4723 | 6aa52a90068df4f8a08e10c85e5a3cbc8cc4627c3fea242c5b4e670d4a28e6b2 | e22258504b8a59fcbfdc4bfee1b4b8faa2dc44fc |
| publish-guard-report.md | 1565 | 5aaa5c38c4c862c8d4f264a55cd74b833833e134c3c8909e9f6d3c6104d91237 | 2665280f6df7c4a403fddda3d85ae330237f5832 |
| published-recheck-report.md | 26999 | 7291242b9c977b4227bc489f59fb72edde0e899a459f756dead7d064ebb2f8be | 09086193673d82ad38584747a035b8790342b063 |
| source-report.md | 8030 | cb1b59dbba9b701eba2cda5a46a0aab69eac054c6fdd0f7b545d7d12d2000ac2 | 92de1eb7c6bca91dcd09ff1d7ceba0c0490ec07b |
| check-report.md | 8030 | cb1b59dbba9b701eba2cda5a46a0aab69eac054c6fdd0f7b545d7d12d2000ac2 | 92de1eb7c6bca91dcd09ff1d7ceba0c0490ec07b |
| curated-report.md | 1804 | 0dcf5f7c04c0871884d02c64fec05a7cc2e1098e67d2598328bc1495e6bad323 | 80696913188a47d043f3f628f2dd273aae89b396 |
| sources_status.csv | 4101 | fe5411aa57784f3b1e76453c08486a6431b31d6c8d61058e8f2083211bcd1793 | c0851cd535636372f3fa54aa38194965c184a7c3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
