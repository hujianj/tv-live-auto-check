# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 343467
Unique payload blob bytes: 278749
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38072

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19036 | 0fe7fff824e17e35d912fc5b9fcbfb03e37658d4baea3b55e7dad7d89bc3c854 | 59ad0b755db77aab1dbe1681100136748b28a677 |
| live.txt | 19036 | 0fe7fff824e17e35d912fc5b9fcbfb03e37658d4baea3b55e7dad7d89bc3c854 | 59ad0b755db77aab1dbe1681100136748b28a677 |
| live-verified.txt | 19036 | 0fe7fff824e17e35d912fc5b9fcbfb03e37658d4baea3b55e7dad7d89bc3c854 | 59ad0b755db77aab1dbe1681100136748b28a677 |
| ku9-live.txt | 22939 | ff3d238e4c1489c99964d40e2cb260ab67d93d401623292a8afd08b22440d5ed | 10aa1e402ca0c51fd959796088e8e537bbb6886a |
| live.m3u | 36625 | c5bbcba54b887c5732bbb291913e022a9e58386d6cfd8e83c6018ef6c0e0ae07 | b3dd13b8968aacf41f08a0cfcb6065ab00ce694e |
| ku9-family.txt | 18600 | fc024c72579dc3821c45d4ba56db06c8412dd489f18d0ecd19db5caa87413a57 | 17ceaa9330d7d0641be17382fd043a7b2cf08c58 |
| live-family.txt | 18600 | fc024c72579dc3821c45d4ba56db06c8412dd489f18d0ecd19db5caa87413a57 | 17ceaa9330d7d0641be17382fd043a7b2cf08c58 |
| family.m3u | 35817 | fa73b5f45d8895165baa69af2a328da6ac165d45bae1b111cfb76a08934c8663 | 88cd2b7d85c751e3d74607bb88ee8bcf28877ca2 |
| final-publish-report.md | 10839 | e8038422d18af02a179027295892bbbfe0b1fc72d040f34363036d5f1bcabda4 | db90c76d32f82b7f84dfa1c01efd6b02b3f758d7 |
| coverage-report.md | 2200 | 06f4f3c3a1610648b597622be3ab592ebfeaa74dbbc0dfbb60a78fe1a799166a | e37d870c7d8687e85bd5af2fb40587ad1b5cc4cf |
| quality-audit-report.md | 4670 | 8093f60a67d7963ba11a6c0c8f1f97cfa6f602e495291202282abba82535a6c8 | 17beddf5ee07a5bd27a5ebd11d9f2135ad510619 |
| publish-guard-report.md | 1485 | bdca3510e432be67e7380235a6c76287a8a6c216a84e0f1d09db7346456db620 | 0dc483b42a9a20d661d877e06cb8facba05565e7 |
| published-recheck-report.md | 29835 | 5281a382b14c43ff3ee532a60925a3890fa11671d09dad61ec6807def26a5548 | 9d956e7ef57216c14ff947bb8fdd037b7dda6935 |
| source-report.md | 8046 | 33e6916b50765c4fd040a832211f989884d6e3f94e078fe741fa1c51ee4e57cc | e5928c704531e24e0a7e688c8b4df0629a867e05 |
| check-report.md | 8046 | 33e6916b50765c4fd040a832211f989884d6e3f94e078fe741fa1c51ee4e57cc | e5928c704531e24e0a7e688c8b4df0629a867e05 |
| curated-report.md | 1833 | 87c7d492e3a2c5f52392e3c62edf196cd9a8e24446e7bd26d76d8f1e4d79c88b | 3a1e6a342b04d131f0df36514e4943da8fc87a20 |
| sources_status.csv | 4121 | 3017adf595b3a81fa16190bcec46db1e9883621116dfea79bd56ba8f49cfceff | 12c89ad0cabccc14c996e6a5218b7dc2e4925388 |
| tv-coverage.m3u | 51927 | 66ce1b535a331a415437616d8a9d51eca1e68e015fca1949caa445cb2d1341e7 | 4d1846e97e562bdbd9a03e21ee2fd176551d5b2c |
| tv-review-report.json | 19453 | f652c78cc5be7de2e1536de87d1ab8da333a1ddf3a5be060aee6b0cf44bef5db | a3b03fe3c755605f859d4ddcd331233383b3c7d3 |
| tv-review-report.md | 11323 | 6c0a6056285288b09253665b805b085a1fe39f9dec9a6f7dbf992866663da937 | c87374c6eacf3bcf0485d3376d78532dba165282 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
