# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 285642
Unique payload blob bytes: 188896
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 66768

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22256 | be00653575e42669096ffe7209fd70b83c05a8801afc06e38d55dc12d68ac04d | 9145d7925c091a5873364dfce9245c69d128d0e2 |
| live.txt | 22256 | be00653575e42669096ffe7209fd70b83c05a8801afc06e38d55dc12d68ac04d | 9145d7925c091a5873364dfce9245c69d128d0e2 |
| live-verified.txt | 22256 | be00653575e42669096ffe7209fd70b83c05a8801afc06e38d55dc12d68ac04d | 9145d7925c091a5873364dfce9245c69d128d0e2 |
| ku9-live.txt | 22256 | be00653575e42669096ffe7209fd70b83c05a8801afc06e38d55dc12d68ac04d | 9145d7925c091a5873364dfce9245c69d128d0e2 |
| live.m3u | 42737 | fa8b7b9ecfc0b08d5aaea2d1276e81e59de65e47fd5afa29e1a684c7c11717da | a8465329502ae8fcc019a59df78f88be7f063b59 |
| ku9-family.txt | 22047 | 84fcddb54b06b00af41c9e8b447a123b777d5ef217967b7acc8f600e4ad82743 | 9efd429e69374c4cb8966d77d746fed58a344f2c |
| live-family.txt | 22047 | 84fcddb54b06b00af41c9e8b447a123b777d5ef217967b7acc8f600e4ad82743 | 9efd429e69374c4cb8966d77d746fed58a344f2c |
| family.m3u | 42342 | 75edd7e7445b0f0139658e5f46e05539592b3c30bf1a903d723cf5eb9109b3b7 | 1b79700181b95241b4530c1a2f13432264f8ac90 |
| final-publish-report.md | 10688 | 77a001436c0f04e730feb1a43c4bd65d22e693aa55c8b155aeebc16dcf1d6831 | 4bf9252c5c7c3a55479c1c3bda40a3ffa74f87fb |
| coverage-report.md | 2234 | 947eccfbcb2736e8588a05d0a0a5ec28aff0d0c17e4c6c6376ee81226fd3f5c5 | 161a0f7fcf4101a0adf367d2c190fa9ea1b96557 |
| quality-audit-report.md | 4727 | 6ab12a38f72772242b66c8586e931d7960f4b9b9383688f7cf8250c6c62ae561 | 0d35920117c770f62743d0c2a86f0e96c0752389 |
| publish-guard-report.md | 1571 | 0afc996dfd674df42f23a20eeb161d1d907623eeddcd53ee44fd6ffa0df581ca | cb4fe10a80eaeac04b5c1de827d2f76b48860902 |
| published-recheck-report.md | 26364 | 572197cfe763a55dc90d8503b539f0462082e8689133f301b416abd7780e46eb | ffe8cf002e8d4d3c3dfb8dee6f2ae9440b9b2101 |
| source-report.md | 7931 | d7a3305f3316a1515f165defdefdbc90933d93fcc9c81cfbc782d081bc7543aa | f982172c07e4344c8a453f1fb35cbe5bbe4ff2b3 |
| check-report.md | 7931 | d7a3305f3316a1515f165defdefdbc90933d93fcc9c81cfbc782d081bc7543aa | f982172c07e4344c8a453f1fb35cbe5bbe4ff2b3 |
| curated-report.md | 1861 | 783c173c928ec93bcfc3dd80e10c717532090a68efa3596ca4e0d6b9bf241dc8 | 475ce930ff20b4853b7935b7b354670f36cde94f |
| sources_status.csv | 4138 | 8b15ca4582baabb7e1862fbc9dffe0d85fbbae3fb1a1c1f576018a727ae11a8b | 4ddfdb2a41f0f2e82299c16451479b991ec5441a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
