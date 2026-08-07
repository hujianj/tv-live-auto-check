# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2476898
Unique payload blob bytes: 1718899
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 655344

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 218448 | 4a873ddb216314e3deaca6ef25fe49c1ab9aa3194b930d1aa1508e194d4fd757 | 3f2a67abcb0013d5bef45e13fb2e7382fcf708c9 |
| live.txt | 218448 | 4a873ddb216314e3deaca6ef25fe49c1ab9aa3194b930d1aa1508e194d4fd757 | 3f2a67abcb0013d5bef45e13fb2e7382fcf708c9 |
| live-verified.txt | 218448 | 4a873ddb216314e3deaca6ef25fe49c1ab9aa3194b930d1aa1508e194d4fd757 | 3f2a67abcb0013d5bef45e13fb2e7382fcf708c9 |
| ku9-live.txt | 218448 | 4a873ddb216314e3deaca6ef25fe49c1ab9aa3194b930d1aa1508e194d4fd757 | 3f2a67abcb0013d5bef45e13fb2e7382fcf708c9 |
| live.m3u | 393675 | 76e7124eb7a5f088c9235fb4469a869fd987bd1a7a3bcbd505a1b9ba6b0547b7 | e9b8f9958308841048dd9493246fab6ce88834c4 |
| ku9-family.txt | 96797 | 9377ade1626905cab8a0dd978dab0b46de8cf49b766130ee271f6f3464925e52 | 8f0d931c8a818c5966e1bf8bedaa3f34d1c2272d |
| live-family.txt | 96797 | 9377ade1626905cab8a0dd978dab0b46de8cf49b766130ee271f6f3464925e52 | 8f0d931c8a818c5966e1bf8bedaa3f34d1c2272d |
| family.m3u | 176314 | 0dd45908d401372124339232480c1a7acb845038ebcc23bf204881e469b3a627 | e9f13da8f5029eebf22db3f70bcb4a9c561a9e97 |
| stability-history.tsv | 764633 | b272eafcddcb0262ddcf18a6ee38f5a0f70d459d5ee4d0fea8167b9983797b0d | 86f7705b3a2842b4cd571417c04f3744cb938f08 |
| final-publish-report.md | 11362 | a0618fca079362af98d3557871a24781a1a6f9873b012aa08d7017e50ac17356 | 2fe2f6781457d8ec321b96c6402bf65996187745 |
| stability-report.md | 12816 | 3a46129fb24728076e9005f30dca47fdc4e01ce4822df2799343c59dba5394d5 | 492e3e71fc7b63663fb09711a60ef6f330ce0a21 |
| coverage-report.md | 1310 | c98f775d6d247ba0ce8cdb4309814d0a15f8aeb429bdb2ada05a5648380a785c | d0d893dcb6adb97624aa8ea58b8d86bb6b2ff015 |
| quality-audit-report.md | 1435 | 2ef02b64d242926561078fba8d80cfc38527938a9295b031974ac172f520b653 | f49ea1578babf8bed71b19707bf945c41fdd020f |
| publish-guard-report.md | 786 | 8ae8af30881c63f464d84d2a8075de9a85c2612b9bc54fb63e3ac571d7c3df1b | e5bee0f5297b0931274f3533c94b1b8bc9d7e9e6 |
| published-recheck-report.md | 29267 | 353ca6d00f0c6e614e34da9cc2f53ff27d1bdab47d5200ebd45562918c404176 | 84f2809f829aabb363ba391f33b499699f0df8d1 |
| source-report.md | 5858 | a13ad5bf6c16b40b68bfdd2469b43f0af51772d491684d09d33cd973f5739172 | 127211b51ae13f0a1e529a5b09ebae71345237a6 |
| check-report.md | 5858 | a13ad5bf6c16b40b68bfdd2469b43f0af51772d491684d09d33cd973f5739172 | 127211b51ae13f0a1e529a5b09ebae71345237a6 |
| curated-report.md | 3597 | c7d62b669fec363aeae99a3eb60bcbc065fac832b80514dab6456eb49b46d81b | 2dfbd852de6e4d0fe47f94941ec3f4ca716ca753 |
| sources_status.csv | 2601 | 6406b44c323824c397e65524c1ae2777f4a1699bc8fcdb5a064ae81246efa7e1 | 57f253285fb4ab2143d82256366e4920aab97919 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
