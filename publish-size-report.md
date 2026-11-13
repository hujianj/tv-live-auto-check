# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 326085
Unique payload blob bytes: 265087
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 35542

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 17771 | fadfe1c46808bdf40a3e97cc5db127695ed3578838894f8fa36bf2544f69e08d | 83a7336c603a80483e474833d6f61e25c9ebc88a |
| live.txt | 17771 | fadfe1c46808bdf40a3e97cc5db127695ed3578838894f8fa36bf2544f69e08d | 83a7336c603a80483e474833d6f61e25c9ebc88a |
| live-verified.txt | 17771 | fadfe1c46808bdf40a3e97cc5db127695ed3578838894f8fa36bf2544f69e08d | 83a7336c603a80483e474833d6f61e25c9ebc88a |
| ku9-live.txt | 21784 | 07edb2e5c0944e81b35b70a23c8f8f819ca1af10d89449d8df3d6509e97c919f | fd2eb1cb205892561d51f45d0153209737ab8a73 |
| live.m3u | 34196 | 8823fd51ab446bb91ce2afe922d85925ea89ad929c576d410d2bd5282ce97677 | 20ae9b8a2588534da1dc6f67a23e0f727e3049ae |
| ku9-family.txt | 17335 | 13be8070048270c4a2746db49ffdd249ad123c21e04c28cbaa18608fcf6d47bc | dd767cf2c8a982cf10bb14b5bfe673e9d6c8148e |
| live-family.txt | 17335 | 13be8070048270c4a2746db49ffdd249ad123c21e04c28cbaa18608fcf6d47bc | dd767cf2c8a982cf10bb14b5bfe673e9d6c8148e |
| family.m3u | 33388 | ece978101c0943df0fe75e6fa36492aaf03b429fc0c9cec3c97661709b2f5dc8 | 31e1ef0ea9fe6e31cfe44b3013485f7e506152a8 |
| final-publish-report.md | 11218 | 4c72a10016ee32bf9ee531552519a650ed83795d827d45c1e3863d850bd49c90 | 5b08c27628ffc51c624273e45bbdf2108dadd335 |
| coverage-report.md | 2200 | 4b4edf56027e536bf3912f0e87e6bc7a2df4e284381dee655c9bc6a56c41c1f1 | a7325bc8e2d46b383c65f6f5a0afcc87585f66a5 |
| quality-audit-report.md | 4700 | 067014ffb836bb00c98bbe8ae9ac732e584baf3aa1bcd5a4ded91a25e9168979 | 0d806948b431f34b2afe95d1b8f9199417466404 |
| publish-guard-report.md | 1501 | 3c2fa419407b81fc226e0e8cf5bd5c3a99a9427d3a47e8c27942d1b84a0dee3a | 063be9abe737feedc922a569f6935855021087c5 |
| published-recheck-report.md | 28625 | 51eb3c8903295105f9c109219cf21bedb540c6df719566dcd5bfabd49e320de8 | cf487ee941727a1ca6a6ac738a978ffd06d0b8be |
| source-report.md | 8121 | 225cb9fb7fe36ed3844ab0659b13eb71f64b606a2d418a6f45c9ddac4f3196d6 | 5d60306eac4f60ea41812a896c1868536acc942d |
| check-report.md | 8121 | 225cb9fb7fe36ed3844ab0659b13eb71f64b606a2d418a6f45c9ddac4f3196d6 | 5d60306eac4f60ea41812a896c1868536acc942d |
| curated-report.md | 1831 | 4b718ca35d0da07c925e6be82439d8f86081ac5cb0a0a1e75f87a168572df3bd | f821ec2140ac414f3c8c928d0e96e4a31d9f9b31 |
| sources_status.csv | 4182 | 4b0318bcf13e1fc1a589de7ab2c0a467549bf5fa41acd42b7f80a1b69fc5a3ca | 6bcf1954df71eacb634182ecc9d8ab30bc1633cc |
| tv-coverage.m3u | 49014 | 0c587eafea6b1da8b7395adf2e503ee46c6b441d685f36b31b6ee22a787e5ace | 284b4b1091fd3205a1e748b9bcba9c594148d159 |
| tv-review-report.json | 18578 | e299a85918ed37a3fb00b41542fdf7d23cf0964c3e0ea2fa095c9c8f2a642fb7 | d57d8521212ebd1030a5f61d19a5c56e283513ad |
| tv-review-report.md | 10643 | 297eb5bfcb451950a82f80e2dda414d1d1201f62a37ca64d14b9b969c9754538 | 816cbdc0935f7c253d5631f00707a4090587ca40 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
