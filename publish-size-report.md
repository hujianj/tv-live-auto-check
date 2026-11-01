# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 303194
Unique payload blob bytes: 244004
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 34244

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 17122 | 55c9d2a4f63b770319ea357071e16d4ff99a64c9acf6913cf8c2df34d40578f6 | 20af75ff97f1deef0037ae278660bfa354c1e699 |
| live.txt | 17122 | 55c9d2a4f63b770319ea357071e16d4ff99a64c9acf6913cf8c2df34d40578f6 | 20af75ff97f1deef0037ae278660bfa354c1e699 |
| live-verified.txt | 17122 | 55c9d2a4f63b770319ea357071e16d4ff99a64c9acf6913cf8c2df34d40578f6 | 20af75ff97f1deef0037ae278660bfa354c1e699 |
| ku9-live.txt | 19359 | a02d971219390976944fcbbd4b36d62b0f3b14892de805def10f1c7cacb3cb83 | 3d5cee281e15fa07bbd1b02b15c167c88fea7215 |
| live.m3u | 32356 | 343c04bfb62d6443729759f09c19915d7f5d4b37b92cdef8e3c3b0c7e435b0b9 | 9cb0bc492e756b152a199e06ef91a6362858e0aa |
| ku9-family.txt | 16763 | aa578f664182ca0a56caaacfcd9ae027e22e4f378c6643b42be99704251f1b3f | 4e58da84185fba51dfcd4bd371c76d25fbba12ed |
| live-family.txt | 16763 | aa578f664182ca0a56caaacfcd9ae027e22e4f378c6643b42be99704251f1b3f | 4e58da84185fba51dfcd4bd371c76d25fbba12ed |
| family.m3u | 31687 | 5b7f7b196c3a19977480145907eadab586f38baf60acbd582533ef75697dea91 | 8606ade3ce7ff53c04327012ef74f3ab4d3302d5 |
| final-publish-report.md | 10979 | 3ae9127e0020a4b442e0207c034be437474cefb9c9b80271d8e2c8519d87d774 | 10a709e79865e4c982744ed5e03bc1eeb09b413d |
| coverage-report.md | 2200 | 8acf5411124d29dcf0fe15bc5ca03eca8f7cd9b963dbec5981436b8091730033 | 29ba5159d5cce2eeed3d899938f68ca3f41855f3 |
| quality-audit-report.md | 4667 | 85731280861fb3c3b117526ab7aecf5adbbc16eb622967c8c11ff58c7e9ad780 | 8a2fc89eddc859d021decfaa4fc37be40ae161ea |
| publish-guard-report.md | 1577 | ecdc8ccd32daad9c5415ea3e586380f13218689955f448fe0b7a448d45dc6d69 | 0bd6f230959286cb9648930a21620b5735f2bff7 |
| published-recheck-report.md | 31328 | bbbd77445d5bdec3c203a6ee5e9be7aa1239e5baa6ab283f807285df688b467a | a7369359a03112cffdf6505fb14f744b4485ecd1 |
| source-report.md | 8183 | ffe4f7f4802be03431080df0ac249315e8f855eaef396911cacd995549611a46 | e02e55d05e3889f770c6078988257c0c63ab8099 |
| check-report.md | 8183 | ffe4f7f4802be03431080df0ac249315e8f855eaef396911cacd995549611a46 | e02e55d05e3889f770c6078988257c0c63ab8099 |
| curated-report.md | 1830 | 642b6dd9f1441a0873e76af9f50160b513de329806f45c92d4bc1a687d3020e6 | 9a1a404e3f5a8078deb253af84fac42caf1d6bc7 |
| sources_status.csv | 4240 | ee0470e015ef011882562ed6dc3d179decea113c2ce60a7e56728cdab7763029 | 04373766cd09635e56b3409b492b3bbafc8ac682 |
| tv-coverage.m3u | 43483 | aaab018e45c2e66486ceabe6f51e1af7743465f87deb091743426aea48a0b626 | 6b60afaba2c98078ee70b9a6420ebd34df9c7109 |
| tv-review-report.json | 11815 | f90d12b7aba3128b5ff7f18b1b64606e512a240b5e664ce6c388be7164baa464 | 08c6aac16604bc1ada3f5bd9ed7047f24188fd89 |
| tv-review-report.md | 6415 | 7b1726601c007892d4380e9e0fa5c17f3de2201f87e9c53b37f4236440e683d8 | de72c060467f710fbe7b2fbef19f7c4343cde6f5 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
