# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 300002
Unique payload blob bytes: 198338
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 70479

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 23493 | c9d669fa86477dd807d2aaccaf720906da52fcb6220c09492404d3fc33eec16e | 417389db6d6a0d2de49f96bba99bf8688d9c8b3b |
| live.txt | 23493 | c9d669fa86477dd807d2aaccaf720906da52fcb6220c09492404d3fc33eec16e | 417389db6d6a0d2de49f96bba99bf8688d9c8b3b |
| live-verified.txt | 23493 | c9d669fa86477dd807d2aaccaf720906da52fcb6220c09492404d3fc33eec16e | 417389db6d6a0d2de49f96bba99bf8688d9c8b3b |
| ku9-live.txt | 23493 | c9d669fa86477dd807d2aaccaf720906da52fcb6220c09492404d3fc33eec16e | 417389db6d6a0d2de49f96bba99bf8688d9c8b3b |
| live.m3u | 44987 | 7a0b893c28e21cb0d04c6082f6d0c7736e085d0f557f7d63c5e41b0bd96ac7f5 | c7c239f0fde07906dcc541c04b4dd97fb467e43c |
| ku9-family.txt | 23077 | f7116daa4954dbcde651ca1d80960baa79b92d26ddc48c140ac3276ed588b9f7 | 5889022c8b98a09d51d41a43f3896c98d4a8d803 |
| live-family.txt | 23077 | f7116daa4954dbcde651ca1d80960baa79b92d26ddc48c140ac3276ed588b9f7 | 5889022c8b98a09d51d41a43f3896c98d4a8d803 |
| family.m3u | 44199 | fe4ae5565e78ee007f3433e4974e5b7248102216ec7506be28be101b454842e9 | a26239d3b221b7cd0c7623760ce415ebadd51783 |
| final-publish-report.md | 10751 | d774199c91de58afc98e70cb467f45025b6e15db844fdecf3f2a347a99b47e7d | 82fd3f06af8b39064fe71367c954293cd25cb6f1 |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4720 | 60364e3aeb2bb82c9134ce9ae95c80a474961e37dd8818a8a62e58bd164333e5 | a1d124a0c0da5d8034b99deb5ecf17ceb6e04b2e |
| publish-guard-report.md | 1609 | f8bc5bf556ef490386eb539ed0df842860cf12ae4132b1de23975319e2b38734 | f2a2663de74f4aaab293d0c7309129a4a180f649 |
| published-recheck-report.md | 29222 | a918a9577d409ad98b625501de5228e007f67cd4fa92e91c1275f76305bdb6c6 | 1108beac7bfc972dd2d3545f0637f9744cb4520d |
| source-report.md | 8108 | 8b3535724703ffb28e94a53cf945d4919fa63a4fb2e90dea4253324a99779866 | a0d52418c7a7a2a9e67b642a89cdd384f9a2c9bd |
| check-report.md | 8108 | 8b3535724703ffb28e94a53cf945d4919fa63a4fb2e90dea4253324a99779866 | a0d52418c7a7a2a9e67b642a89cdd384f9a2c9bd |
| curated-report.md | 1804 | 8bbc36ef6fd516f4154214a7117e2d6ec87370aa7c8c5cba325cd40d1102af3e | 5a61c3c9bf7180dea07c8edb7b16a8edf0c07a59 |
| sources_status.csv | 4138 | 22512071a52eebcfc305acf486fd324fe613c5f5f15fd55a1b05014457300bfc | cc3da8ab3be6c317803243ce7b172ea765f24fd7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
