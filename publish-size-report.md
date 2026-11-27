# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 330751
Unique payload blob bytes: 267185
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 37238

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18619 | fcd2deaa9d27874b87fc758e55359c0b6acb1acc8ce538b6465f5b7e05bec8d6 | 35e611e1ee10b76c7d43c365994841a83c5e2dec |
| live.txt | 18619 | fcd2deaa9d27874b87fc758e55359c0b6acb1acc8ce538b6465f5b7e05bec8d6 | 35e611e1ee10b76c7d43c365994841a83c5e2dec |
| live-verified.txt | 18619 | fcd2deaa9d27874b87fc758e55359c0b6acb1acc8ce538b6465f5b7e05bec8d6 | 35e611e1ee10b76c7d43c365994841a83c5e2dec |
| ku9-live.txt | 21934 | 9a45a8bf5ec94d80b72787075099db444e2d21899e640befcc8f3332b713417a | 30320b9eefc70db5f59b456f46795c354d6ed332 |
| live.m3u | 35912 | 964fb53638fe469aa4aa4d2d34ec5fecc395ac689cb4a31836faba640ee87c2d | 7f8c85265980c07b7d4e68ad39b46c4f31790c0c |
| ku9-family.txt | 18191 | 10ef37e4b51956445a1188fe8c1bc925cff098bc70bbbe6137a390727e0798aa | 7e062c7908ca5085aff89e36dca3d1ed53afae8f |
| live-family.txt | 18191 | 10ef37e4b51956445a1188fe8c1bc925cff098bc70bbbe6137a390727e0798aa | 7e062c7908ca5085aff89e36dca3d1ed53afae8f |
| family.m3u | 35115 | ae081ee08b4ecce2711effae9239602d5dbb97e7358bed7c96bb661313a56cee | 197b44700d350be03bd618cc683871087a432c9b |
| final-publish-report.md | 11371 | 4ae5792c768ca712a7d3aac59e322c2f00e2f103f5a8da5e6c1bcbbf27340899 | 1d934c127387b5483a9b533659669703fb926f53 |
| coverage-report.md | 2200 | 5a95d798c45f1404b715713fd30623d6eb85ed2870cac909cb1d505a3b90888f | 6f28feced5a592a1c365739ff51557b5efdd185d |
| quality-audit-report.md | 4710 | 9cf651193ede2566805477aa22d1f2a4112fbd0be42bb9d6e7f05eb3149ba223 | e46568b8abb6e7d42873ea0a07300dfdac1d3d61 |
| publish-guard-report.md | 1567 | 6b552e14b25f3d735aa81a43c656a64e3f3e3f3ba8cf524ffe91a4030d4dd659 | 68c74c2046abb768ddb7c19221d3187aaeed6aa8 |
| published-recheck-report.md | 29211 | c5985e8f3f9ccf01a25216c07fc5c0f6c126f541e680c996b041a6f976871fa8 | 2ab84222fb2e59872afb6a29e39c0381c17b0153 |
| source-report.md | 8137 | 82c3e1f2942bae23b933e9df4a895dd7c80d318d5cc5b5be6fb005a3aafd64f5 | f9fb1455140c69a6a805beda6dfd23b7bdb2ed2e |
| check-report.md | 8137 | 82c3e1f2942bae23b933e9df4a895dd7c80d318d5cc5b5be6fb005a3aafd64f5 | f9fb1455140c69a6a805beda6dfd23b7bdb2ed2e |
| curated-report.md | 1854 | 2c3bd75805c283b62625f4c36deb2f87dfb1965fad3f9618c544877a0d410a41 | 0cb083e5b11c97438bf62e8b4be476bf8e87d04a |
| sources_status.csv | 4179 | c3cb727424aa7c8388fd17a0eba5985b082817a212b25998b6c737e8a93393d8 | 23574be04c39c75b0f24a5739bbed98c3110a3c5 |
| tv-coverage.m3u | 49800 | 276f965a2638d2c8c08d513324be7ec266eb9562f0998db94bf8088f29d67e70 | 16f5ad02f0a1f4a04d344e983bd547b5bd2798d4 |
| tv-review-report.json | 15575 | 06d60a92b8efe5d68ceb9386fca6e577d37924f52ff3af6f3827a671b7d0522d | ed790bf5170f0bad9f507b2443e39475c0e630a3 |
| tv-review-report.md | 8810 | 0a02a496a8fe9c31f07f9d16b4b4ef5231ddf8c0f698c87407a2c37c335bb4d1 | a691e43c534efaa6c1a6fc44a339cbbf622c9ecc |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
