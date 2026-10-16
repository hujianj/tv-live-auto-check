# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 276355
Unique payload blob bytes: 183398
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 63879

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21293 | d98b35cc9d6dde5c9f0760b95af6702ed7e6d3b73cc0b26bfe01336531676cf3 | f7c9f23893eb561a96e03e31097584c5b0d161b0 |
| live.txt | 21293 | d98b35cc9d6dde5c9f0760b95af6702ed7e6d3b73cc0b26bfe01336531676cf3 | f7c9f23893eb561a96e03e31097584c5b0d161b0 |
| live-verified.txt | 21293 | d98b35cc9d6dde5c9f0760b95af6702ed7e6d3b73cc0b26bfe01336531676cf3 | f7c9f23893eb561a96e03e31097584c5b0d161b0 |
| ku9-live.txt | 21293 | d98b35cc9d6dde5c9f0760b95af6702ed7e6d3b73cc0b26bfe01336531676cf3 | f7c9f23893eb561a96e03e31097584c5b0d161b0 |
| live.m3u | 41068 | 1d6511d40f7fe55b53b9da1df05c77b2ab1ddf4c9f9a0def691410e1b79b00ff | ccc2fc243f04ecd1e6448efdc90cbc06e4ed7ae1 |
| ku9-family.txt | 21021 | 51477702e0cf6f783487c8279850089f15b04802d58e16757621289914603c0b | 3920c0800267af011426543c31eb2fd6a8304788 |
| live-family.txt | 21021 | 51477702e0cf6f783487c8279850089f15b04802d58e16757621289914603c0b | 3920c0800267af011426543c31eb2fd6a8304788 |
| family.m3u | 40548 | 77c3d0c13b4c90b7d86df202486b1493470fd2c66b92181e300a93eb43192fb8 | c67523962eec8401f0abcb52df3df955a7fc45c4 |
| final-publish-report.md | 10650 | 338d3769891f4f210050bea2ad45ee8917509f9604c37ce0a02cbebedaa072f8 | fc5166d60c1d6e8b773f2ad6f4d122a5f9c93878 |
| coverage-report.md | 2225 | d4945e58b0a9c684e0262a8f4106e6d1bd761c5d8c7688c6690179fa78bb4c7e | bfc254d72eecd1e15a03953f8d9040c317a79805 |
| quality-audit-report.md | 4723 | 6e521068975f3ced4c32303c20a79dfe72041359a5175f0b2d105b73110885c1 | eeee7a16f45c02ed8274c299581f848754a705ce |
| publish-guard-report.md | 1531 | 462bb1c21470e7c8b8c4b746059aac1091d848a68ba87d1e73f392aa60ea41c4 | 606ccd3d7fd86ee1e6d9ca9a6e789729ddfb0efe |
| published-recheck-report.md | 26400 | cc0606f03002a35fd5cce7b93afee6541734d6ba47424ba1695c6911da49f5d4 | adb113a160410617aa89c96b14caef325a8554b8 |
| source-report.md | 8057 | 30b1441b9a66f636ca7c5bc20a31291af2d6b28f5b105c11362adb07843d38d7 | 6107e55ad0808aac26a0106fc018a086c7306fc1 |
| check-report.md | 8057 | 30b1441b9a66f636ca7c5bc20a31291af2d6b28f5b105c11362adb07843d38d7 | 6107e55ad0808aac26a0106fc018a086c7306fc1 |
| curated-report.md | 1804 | da8e180c43d81d682ab9bdd4c7240e4c1eaa1e62bd313d2f417692a2bc93113d | ba6c93062cc56eacad93673248ce7892333ff031 |
| sources_status.csv | 4078 | 9edbbfe0b7eaa5ca317b2fcd4a00b563ce647d751799e6dda512c55a069344c6 | 62b5a5ddde014bc7bd28f1674b273b9b60d8aeb7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
