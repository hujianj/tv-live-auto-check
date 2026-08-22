# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2040445
Unique payload blob bytes: 1470979
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 478239

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 159413 | 834d7efaa6c43fa5c85718f173868a9173b8c008045aac55d16125ea0002e8ec | 16b5479f3bc069beb5aa1aeeea234059b99f8156 |
| live.txt | 159413 | 834d7efaa6c43fa5c85718f173868a9173b8c008045aac55d16125ea0002e8ec | 16b5479f3bc069beb5aa1aeeea234059b99f8156 |
| live-verified.txt | 159413 | 834d7efaa6c43fa5c85718f173868a9173b8c008045aac55d16125ea0002e8ec | 16b5479f3bc069beb5aa1aeeea234059b99f8156 |
| ku9-live.txt | 159413 | 834d7efaa6c43fa5c85718f173868a9173b8c008045aac55d16125ea0002e8ec | 16b5479f3bc069beb5aa1aeeea234059b99f8156 |
| live.m3u | 285289 | 054d145eaee06db77ce8ddf3d786b1c1bbbd864ca0b6a3b72427ca48daff35dc | 7f55773856f56c0c316594c3c6ab9abcd4fdd407 |
| ku9-family.txt | 84593 | a38b648b7cc1f2713d548ed18462f47582b3bc93fbad7d2159e766dfccaeb8eb | b185c6a8d756e70c98bbf9140fbda4ecdad3b6dc |
| live-family.txt | 84593 | a38b648b7cc1f2713d548ed18462f47582b3bc93fbad7d2159e766dfccaeb8eb | b185c6a8d756e70c98bbf9140fbda4ecdad3b6dc |
| family.m3u | 150348 | a2b6c87170227b56fd80dc0e9aaa0e01ec63e874d8996a504d1978b26eeea0b8 | d9c0aa0d075392b537c9e26489d7c56506b48e5f |
| stability-history.tsv | 723016 | acfb36a17e3d3c38fa32084c8f84cc9ead0f0232361152549c338cfe005a0327 | 03df0b6c479c8be0732ea52f903218767355b1a6 |
| final-publish-report.md | 11790 | 57c36b8d44a90e2af27e99b0601d67920c204091ca86baddecf123722bc30def | 8a254d67fa05305c9ac1a71918d14ce19b323b98 |
| stability-report.md | 11916 | 3c357cb9f7e125402c08596a3bc5a6dc54976ae6cd2234540a29ec56077c2fd1 | 8a72a720041ea6970c497a9b9b91a530d9000fc3 |
| coverage-report.md | 1291 | 89a4512f4950f006e60c2e42c1f0115e30b9f3ffc146f3f0e659781a988c1f00 | a8f39dd75b36ed851447f1d2f8323abc20c8730e |
| quality-audit-report.md | 2062 | b2e31dc5896c3142b5fefdd398d977192f0953b62952aea4d124ed54d75d7091 | e80cd32c9658ca04df28c5493ab00157bafbadff |
| publish-guard-report.md | 1140 | 338b009f56f067704ca9963f20feca1f058858a0cb0c88a6852b9c0e280a2cf2 | 23a77cd588be93b195cc0ad4df39465fb1cbfb35 |
| published-recheck-report.md | 27005 | fbe61a00b9a9b69417a8754d5ef4ee095594d9e442c5f04e7948bc901f4586c1 | 5a28c64f2aa24b6a0f011025f51d4d366bf0cb66 |
| source-report.md | 6634 | 5d89c4d8cf37587013ca7567dd9c5071522ef670e484d2f095c6e6552b14bf37 | 97d349009a3cb448583aa4c26b7984d136075b74 |
| check-report.md | 6634 | 5d89c4d8cf37587013ca7567dd9c5071522ef670e484d2f095c6e6552b14bf37 | 97d349009a3cb448583aa4c26b7984d136075b74 |
| curated-report.md | 3347 | 427f4629b9471598f144182894647c0b94d95eeb41cd27ce0a8087f4d5698ca1 | b5293a4bb13410fb88cc2c70e771ba50ca9f0229 |
| sources_status.csv | 3135 | d05502d0f7d303de95b3c0de821ff7acb775f2a26f19cacb132b49f828ec6863 | 52b193178190335543360cc6492da2a41ec1c2f6 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
