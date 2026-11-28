# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 319133
Unique payload blob bytes: 257839
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 35666

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 17833 | 06af1baf8b01d9fb2cda27ac33f6a6e6b3e1e191719468980b9f36646c488dff | d07f61e83a40054544f2e48e21829fdff8d4432b |
| live.txt | 17833 | 06af1baf8b01d9fb2cda27ac33f6a6e6b3e1e191719468980b9f36646c488dff | d07f61e83a40054544f2e48e21829fdff8d4432b |
| live-verified.txt | 17833 | 06af1baf8b01d9fb2cda27ac33f6a6e6b3e1e191719468980b9f36646c488dff | d07f61e83a40054544f2e48e21829fdff8d4432b |
| ku9-live.txt | 21121 | 6d2f390a23fabca87bc35852c88ce9f526c124af1f52acad5f992b7430246768 | 1f9fc01285b7d654d24d7717a7db0f7bc72ff3a3 |
| live.m3u | 34540 | 8ca3108024bbbeca464b89a98dce9377929f6b775f6d2489b19237dee05224ce | 9af913cfe9cf85e51c88f911472a24ab34ee483a |
| ku9-family.txt | 17506 | 32e181697f75577c76ada7c8f8709d83de69c7d27b5006726391392da2547366 | 47890539b30722e8be811fb50de23d08bda01232 |
| live-family.txt | 17506 | 32e181697f75577c76ada7c8f8709d83de69c7d27b5006726391392da2547366 | 47890539b30722e8be811fb50de23d08bda01232 |
| family.m3u | 33906 | b51828fe8d82c3ac5977040a7630d973526b447eae81226f53f23f8db0747491 | a8200f5c04a06b1394a02d171ee07f3afe3bc6a0 |
| final-publish-report.md | 11436 | a3ccdcd9884c629614ee7b5273705e815f4870aa808b91d1300f7d87ef8ea303 | c8f9c0f7e2fff48f00f7186c30329ce46f59d885 |
| coverage-report.md | 2200 | cbad01cf52a45b469faf1b27360f623fac43780931b1a7052ab5fa6ace5fa019 | 8ad8e167f9fe0b124af7551ae7789ed89303c8a7 |
| quality-audit-report.md | 4696 | 9d3ca1a02bc95d29bd193774e1f55fb964415afa4da386dc0ed7bc5dd09397eb | 2250bb849c3ceeeb809dc62579b0de100bfd6506 |
| publish-guard-report.md | 1583 | 4d40cb6a81926ad929e9aa93f0b418eaff6fa907f1aa8071d520e48105b88f1a | 62c42bbee33bfdfe720aa661c8673a518c1bc7ee |
| published-recheck-report.md | 26606 | 50097b2bf74f029961db8eac3f8fa9e78c09d06c1e3405fdf4b6a8929f57867a | 3f02d57dc58bcc33e73399573d7ba27ce224c2a5 |
| source-report.md | 8122 | ba6702f72ab5277b8af161c1b4127b434e18cfa7123e92e67ea45b81696bc00a | 56881783725b763de9d2aede02da81f49783bed5 |
| check-report.md | 8122 | ba6702f72ab5277b8af161c1b4127b434e18cfa7123e92e67ea45b81696bc00a | 56881783725b763de9d2aede02da81f49783bed5 |
| curated-report.md | 1835 | 549a49d946fb30a924ba2e6e4365d903e459a70fb435da492c54bf6fe5136553 | 23d292983ffdc3305f4cd5b40986a59d3afa0acd |
| sources_status.csv | 4179 | e02cc259d8fe431f65892184a79dda7dc44e3767d86d5e53d636eec1b3cceaf6 | a2ebaa20564beca54b1610d36c7dbc47d46a41c2 |
| tv-coverage.m3u | 48171 | d6d4c6ea3945a5a54e701be13623608eed2fab8ec97cc4af7743ee4406e7d52a | d9014622768b437f32235f9689a62a7d0ce07996 |
| tv-review-report.json | 15435 | 5274d56b9934f1f8d1a57ae1e59c01b0163ce1bb97a30526b8ee5b2b2afaabab | 2245c93a6056da930cd846f3ded1ec8ec8b4a0f7 |
| tv-review-report.md | 8670 | dd4d4566760f7e00b9366a1c88f440249c0e56143cf37a7a34bb2a417690a57b | 0f5bebbf0cf71a52449854a725e461ab370748ef |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
