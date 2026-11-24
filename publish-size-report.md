# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 330686
Unique payload blob bytes: 268375
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 36392

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18196 | 2a556c25d271f520491841b751b8e440768db8792e8cdb591ef9ef3f8906d8b5 | 06bf39953995e93daa2913252873746b534b401e |
| live.txt | 18196 | 2a556c25d271f520491841b751b8e440768db8792e8cdb591ef9ef3f8906d8b5 | 06bf39953995e93daa2913252873746b534b401e |
| live-verified.txt | 18196 | 2a556c25d271f520491841b751b8e440768db8792e8cdb591ef9ef3f8906d8b5 | 06bf39953995e93daa2913252873746b534b401e |
| ku9-live.txt | 21751 | adec7484b224da192a6dbb1ee1f4f03503ca684ebe451a4190805e415197cd41 | e77cc348e59375bab20b8b9b7641018e5798b0bd |
| live.m3u | 34950 | 68e9b25902464e3073bdd49edeeaefa4338d5b686a4c4c5aee15af6d2a4d3c71 | e032f995cc513e8fa121b2f96b146ea0e759ca2e |
| ku9-family.txt | 17761 | 13eb33f6aae7d9e4a053f215404b4b4eae99fbd4a1f2a0ea6b54c1df66e690e5 | 55ba2ab58acc1fb3ccf9b3a3d502c1609d26bd47 |
| live-family.txt | 17761 | 13eb33f6aae7d9e4a053f215404b4b4eae99fbd4a1f2a0ea6b54c1df66e690e5 | 55ba2ab58acc1fb3ccf9b3a3d502c1609d26bd47 |
| family.m3u | 34143 | 70ceb7f86b2af97563856faa6ab3bff9080783ba1a13b42e6f1c8b46f3e9f6af | 4ef255bb85f5a83abaf2ed04eb403b76e9896f9c |
| final-publish-report.md | 11475 | 6b2694df2beac3d7526ac409fb25494ff0f93f75b19eab9f6d7146fba576b80b | b03ca5f4e58b87e5523ced97323021ab33c2bad3 |
| coverage-report.md | 2205 | 480a49c6cc230b0a9a00faeb09a2a9c1db9bff14468a35888921cce08e6a5be7 | 6214514affd62ebf5cea0e0cce99da4b093372f7 |
| quality-audit-report.md | 4686 | a1fc9937e32d9a0e9a8e7795343babbaf8e6fec4b749517cda403684fed714c1 | 73d4b25e2788dc10ba8bc12b54e497ef1fc3ef9e |
| publish-guard-report.md | 1587 | 36c7e9f0c0915d10e17c7170678e0f166ba6c011c650d7c756d997a45faaa382 | 16efc10b4c3bfbb85da258891a44210c97051aa9 |
| published-recheck-report.md | 31670 | 63aa57af5e2ed0a4b89931c22e60fcfba00a329e7732dff4cf15619dd1ffe32c | e4c02768ad8a99bc4eca0ad7cef26f8b804e5b2f |
| source-report.md | 8158 | d2bf3547e197fd6c1a880beaca91244bbe96a120129a53469e7cd9198b2efeb9 | 4299046dc2fce11053f3f80c0a5c872b0390d539 |
| check-report.md | 8158 | d2bf3547e197fd6c1a880beaca91244bbe96a120129a53469e7cd9198b2efeb9 | 4299046dc2fce11053f3f80c0a5c872b0390d539 |
| curated-report.md | 1833 | fbf6dc51295fa87e831bc5d386b7928d6a3e83cc490f5788d299f4c96b05e5bb | 59a1005cc56fb2ba79a09f909340c74dc907df66 |
| sources_status.csv | 4181 | 9361d508b63c32c35ce82ceb2e3e99501c4d3767ad7587dfe9dd27d48890c463 | bc9cb5e99218ce2e36851e9bc8cd7600d2683f72 |
| tv-coverage.m3u | 49218 | 93347223260112c4c88f19d169c3fbeca81181170386728ce316908221ab2b87 | b98a195a04d37f5a9cddc5c226421c6164757a29 |
| tv-review-report.json | 17053 | 61d62f1a83c3ac9d0bf91cb4c24746e4a1c6c63b871086845f8e70a57f06fbe7 | 1b0012dbbeae7738e6a92b55441a5d90967ebec2 |
| tv-review-report.md | 9508 | 78f6677581871c6950577ac5e02472b7dbb656f8bd2f34ee95f367c97a6ca373 | 393ddbb7d89f0c722209081edb72033944be53ca |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
