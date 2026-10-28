# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 250617
Unique payload blob bytes: 168370
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 55872

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18624 | 00ccda1f0b0f3980b754cc6ccfc3c7878a71bc64ba859ddf124002cbe7b68c8a | 834c8bf5d3f6cf56a251ea6163006f7f2b4d9349 |
| live.txt | 18624 | 00ccda1f0b0f3980b754cc6ccfc3c7878a71bc64ba859ddf124002cbe7b68c8a | 834c8bf5d3f6cf56a251ea6163006f7f2b4d9349 |
| live-verified.txt | 18624 | 00ccda1f0b0f3980b754cc6ccfc3c7878a71bc64ba859ddf124002cbe7b68c8a | 834c8bf5d3f6cf56a251ea6163006f7f2b4d9349 |
| ku9-live.txt | 18624 | 00ccda1f0b0f3980b754cc6ccfc3c7878a71bc64ba859ddf124002cbe7b68c8a | 834c8bf5d3f6cf56a251ea6163006f7f2b4d9349 |
| live.m3u | 34911 | 5f9bd496f40cea19da2a26dd7de403308f29970cd33fa91a87c33bf2d269fc68 | 506218d4e5c547cee7b5ed6c799f5f029a371c2a |
| ku9-family.txt | 18202 | 34ebf8c9519ef955ada3dcb9db967abbc7a3d537b56da4d985a3f3a8b1585061 | 0072c053a8b461eab4e189d28dab033e3d5f0685 |
| live-family.txt | 18202 | 34ebf8c9519ef955ada3dcb9db967abbc7a3d537b56da4d985a3f3a8b1585061 | 0072c053a8b461eab4e189d28dab033e3d5f0685 |
| family.m3u | 34117 | 474187a7d6d00df4a718c65a72025042983a04172ddc2da910074fb027cc26e0 | 3e567055cedd62b7236ac90bb19150e7df4b9b8a |
| final-publish-report.md | 10780 | 98e6d3e3a0113cb962dac2fb05357cd3f98bc8185c9d9560332bf566ba08ca53 | 92b084b1800e435b8f866d5c46cbeda22ff21d75 |
| coverage-report.md | 2240 | 99250a887b91ffba8f8c6b9504f4daf5bfd7250cf6e172d2f4f61ce7fb1a587f | b4a51c3b1fdb77d73a919c3202071d855b1c0df5 |
| quality-audit-report.md | 4782 | 5af18b459a3f481f40ca089c9eda1cd41d943a788bc2aa0338597be5718489c1 | 2f7c636bb551b330d5def5f5ccdfa36a4ddaec53 |
| publish-guard-report.md | 1604 | 1915763cf067b863655738a096f2dd968ecc826847dbb4a152799d364b3f83ad | a9e8238842bc9ed18c1b9d99c0aee9999a3e5bab |
| published-recheck-report.md | 28897 | 0f13d490e06b07770cd09019ed5597ed37075b99ae0109911c635d9e363b13a1 | d13900d199e6ec2c3187785073651ea7f384e42a |
| source-report.md | 8173 | f149e0aca7598485a5906659480c41d9f87a8514a7a8b25e3a7e672f1e83f835 | 17f94d90686e4a8f759e627e78560ef9607a2f44 |
| check-report.md | 8173 | f149e0aca7598485a5906659480c41d9f87a8514a7a8b25e3a7e672f1e83f835 | 17f94d90686e4a8f759e627e78560ef9607a2f44 |
| curated-report.md | 1804 | 059550cde724f4e114c0aaaa6b7768997a4d80ae7d0b99d18620fb51032ed207 | 2d050f8fa6a0c3588271547176b06e06d5f31567 |
| sources_status.csv | 4236 | 20ff4bb36b5f7bccb707c7a85caeab7fafabb8d101f4a8e454d48f73defde937 | 345112bdda04d7079f8cb2b3dc55fa1f70484358 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
