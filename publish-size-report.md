# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2409887
Unique payload blob bytes: 1685343
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 623553

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 207851 | d9a38039022ce9f6a86137d663eaa779d6675cfb2dfb527f6c07b55fe0f1dacd | e99e7a7eacb660b99f7a30413a14b83a6d4f9b43 |
| live.txt | 207851 | d9a38039022ce9f6a86137d663eaa779d6675cfb2dfb527f6c07b55fe0f1dacd | e99e7a7eacb660b99f7a30413a14b83a6d4f9b43 |
| live-verified.txt | 207851 | d9a38039022ce9f6a86137d663eaa779d6675cfb2dfb527f6c07b55fe0f1dacd | e99e7a7eacb660b99f7a30413a14b83a6d4f9b43 |
| ku9-live.txt | 207851 | d9a38039022ce9f6a86137d663eaa779d6675cfb2dfb527f6c07b55fe0f1dacd | e99e7a7eacb660b99f7a30413a14b83a6d4f9b43 |
| live.m3u | 375012 | 65799ff19d3e620241f109b82910bedf31f49759785abde49313f363fae900a0 | 89c95bcf67e72af7b3669a18d4873810fa14853b |
| ku9-family.txt | 95168 | 79a52cadc8880a15c05399d1fa4674bfd7d96d14e2ab5cded9a3dfb823e79c73 | b2faca804f1ab279dd0117ca5060b58dad5c7172 |
| live-family.txt | 95168 | 79a52cadc8880a15c05399d1fa4674bfd7d96d14e2ab5cded9a3dfb823e79c73 | b2faca804f1ab279dd0117ca5060b58dad5c7172 |
| family.m3u | 173545 | 488dd68a6ecb91112effd334b11ccfd7cae0fc93ff66d044645b6f036e7be203 | 95bf8f49c6a5842515a750e10ca29207c6b5fe89 |
| stability-history.tsv | 767653 | c75ca69e73be4b7e59ad0a799797755f684be4fa455c84a37fc726826bfde39e | cb826664be1cbd044d845d9d67c6418bef8a8bb7 |
| final-publish-report.md | 11347 | ef72d29bfcea0dd0b75846c00855916a8542e70fe078063a14eb447b192c8d2d | b642b835b2ef5ebdb19f282bdbecdc32d6825ec9 |
| stability-report.md | 12830 | 909cf1f1d6407705154701911ee3fee242673e0b7e3c6d70a1d40fd193486ad5 | ef3abe11a9f66c1d610244a44d545cd6cb83fc8c |
| coverage-report.md | 1329 | 57d689be088cca855dad9817f30cf2a76cd6cee9addadbc874590e7e0858fcb1 | de5865794d7b8d9ff080fd7bc7829ed6b6e5d7e2 |
| quality-audit-report.md | 1435 | e407a26137c799e6f0828376fc0a7611d3938157b340eb6949d36a1a9d17f2d4 | d0a3124e5f282d9fa13a46743c855ccc19fe5af9 |
| publish-guard-report.md | 787 | f05a666d24489e84acb928c3b9ba2e32e5749f7457be5bb5e38fbe1b6f7bd9a3 | 399e70f46c20559778475056caa40b7503e8f412 |
| published-recheck-report.md | 26380 | b39031e570750a7acde1b852c3ecedb728646e7b39d9e5d722fc31bf78e74786 | de34792cc38c5f2ec8fbe2b575956b39f5826084 |
| source-report.md | 5823 | aea748cfb18ab01bde1033db8daac3f3cfa75061631e3348d0438be556c37929 | d3f8fe8dc38f6f2e892c2f81b7658b44ac33f6f7 |
| check-report.md | 5823 | aea748cfb18ab01bde1033db8daac3f3cfa75061631e3348d0438be556c37929 | d3f8fe8dc38f6f2e892c2f81b7658b44ac33f6f7 |
| curated-report.md | 3584 | 31626cd333a914fe2f9c7ed7bd51573ce6495c4beb8a3cf8284668252d926ffe | 95ad1c2a25268604b105671f414e5f720fa93a82 |
| sources_status.csv | 2599 | 0fe106a5903faee0518ba9b8a0fb5e45d3169e55f6e8d2115d996da9bf9edd53 | 8a7d6dd262a0af63cab3ed6ed39a7ffa2619c69c |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
