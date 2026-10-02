# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 275604
Unique payload blob bytes: 181409
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 64884

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21628 | d43c3d17847f16ece5ac110a9a1b63997e5fb9327bacc5beecf41319eb30e230 | d7145d45ae694360420199f12140de5a8c28f6f4 |
| live.txt | 21628 | d43c3d17847f16ece5ac110a9a1b63997e5fb9327bacc5beecf41319eb30e230 | d7145d45ae694360420199f12140de5a8c28f6f4 |
| live-verified.txt | 21628 | d43c3d17847f16ece5ac110a9a1b63997e5fb9327bacc5beecf41319eb30e230 | d7145d45ae694360420199f12140de5a8c28f6f4 |
| ku9-live.txt | 21628 | d43c3d17847f16ece5ac110a9a1b63997e5fb9327bacc5beecf41319eb30e230 | d7145d45ae694360420199f12140de5a8c28f6f4 |
| live.m3u | 41541 | f5385d7cae3e0cc1a3e643ce274827f550ed2ee693fd08084d8605c38aa52530 | ce4bd92e56a510505d5aee2ac3fb94e2929ae295 |
| ku9-family.txt | 21363 | 0e31545db30cc41c9549f87acda4214bea0456d8f738a26237df1c764b19ad0a | bc2add99ac4177410e47270b70151777d55fc78c |
| live-family.txt | 21363 | 0e31545db30cc41c9549f87acda4214bea0456d8f738a26237df1c764b19ad0a | bc2add99ac4177410e47270b70151777d55fc78c |
| family.m3u | 41028 | 410ef770cd85af89600f570aa44eee386000c32af8d32c01e821ae1e7d3d4e5e | 62861ad5a3bf9f9f9af5d2372d51a19ba23784d2 |
| final-publish-report.md | 10765 | cdb21b5a285a0a29df9c37867e7a1968aed0df79e5f6a1cb1e36e75ea093fa89 | b6639b78d28b47a5102c3be084890c112c88eb51 |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4725 | 425da8ab6a15be0a439f70f83420540f6f435a636617345fdef760fea5004127 | 7d2af9429fcf6b1d4e651ec305061501ad65ae51 |
| publish-guard-report.md | 1554 | 516a01fe7a2309180529f6cd83ce461c27f89f10b4ce4ad7fb48f6a0725e3aad | b44b22b0c81ca6ef711d0e360ba09f932c203570 |
| published-recheck-report.md | 22804 | 0bfe3709140d927a66d7f6f9e45a260deafe7ab742a321d062d372877d9f7187 | 23a8a460e4c1dea8026a982329ae5fcd89489995 |
| source-report.md | 7948 | 9235f40fe7983e8d0203702758e64dddf014137ff7c70d55a99e12078c703836 | c0ec06102c6164e5f610d155e73a1862551efebe |
| check-report.md | 7948 | 9235f40fe7983e8d0203702758e64dddf014137ff7c70d55a99e12078c703836 | c0ec06102c6164e5f610d155e73a1862551efebe |
| curated-report.md | 1805 | 6c1a6eb360f226cb00f29817e9e6aee71e0752ab1eda318cba1004b0de24b1d3 | 6168be7d0155f41e64a5c79ed0e6c7dbccd59fbc |
| sources_status.csv | 4018 | d19beef9f75189eeaccf17ecec03150133ad7cce164a7a68a929d8a109a36bf7 | 9b28e4af8e1207886c60108065389ba57faee239 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
