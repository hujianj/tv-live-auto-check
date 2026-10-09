# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 290436
Unique payload blob bytes: 192768
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 67383

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22461 | d2687150cabd71e0ef8647ad9b5741966aaaf808ab4e58bb56729f01fd15638e | e39453366facc9430055d06a5979dc1072e56a59 |
| live.txt | 22461 | d2687150cabd71e0ef8647ad9b5741966aaaf808ab4e58bb56729f01fd15638e | e39453366facc9430055d06a5979dc1072e56a59 |
| live-verified.txt | 22461 | d2687150cabd71e0ef8647ad9b5741966aaaf808ab4e58bb56729f01fd15638e | e39453366facc9430055d06a5979dc1072e56a59 |
| ku9-live.txt | 22461 | d2687150cabd71e0ef8647ad9b5741966aaaf808ab4e58bb56729f01fd15638e | e39453366facc9430055d06a5979dc1072e56a59 |
| live.m3u | 43095 | 3358d2261338b0e97e79eb8ce835ea8d7251721f1f08355e8f2b74edee03aafd | 632ebdc85bbfb81a2afa4f0c1fa942adcac5d1f4 |
| ku9-family.txt | 22183 | 3387405f1b10b7182297b938c7dea6d24ef0241ff264e9154fcc2c111b9b2013 | 83c83d96ae0b18907c522255beb931799e82f057 |
| live-family.txt | 22183 | 3387405f1b10b7182297b938c7dea6d24ef0241ff264e9154fcc2c111b9b2013 | 83c83d96ae0b18907c522255beb931799e82f057 |
| family.m3u | 42569 | cfa2a879ac7ca27515ccf792a73c37e7e3944b49884635d75354665804de04bc | bac7a4a2f102edba9cb47d5504f797f53d2a18fc |
| final-publish-report.md | 10722 | 8147916f75d965cfd311b502af920f5c891bef2740d66b21a7b30382ac298fc1 | 36cd97d15d4c3ace50128d13dad3f76b0f4d2e61 |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4720 | 9e0a924d172bbdad11cc4300f21ab35a57776059a98d433a4b05af1c1dd4c056 | f04d7b15adadf02061d19c996c4bf9ec48246fcd |
| publish-guard-report.md | 1616 | 9c70d81782055bd5f35e8759bb5e719960a179cf26e53921d2c2d9aab952b76d | fe6c72daf58c3cc8739de83e4b71b8640b8150e2 |
| published-recheck-report.md | 29128 | 0c7fe28c1e31c3b78088d5e6f882413b6e51e8e425e94757470abace28bfd0ba | 0f5d6f08fd8a7d7f21b15987ad8aa57db0c58b64 |
| source-report.md | 8102 | 1fb3ce6ed2bf33dfb9140001e6401c2d4da79c2aa1d868a2279d1622a86efb58 | cad434627d0f2de8442c848bed751043b6a9713c |
| check-report.md | 8102 | 1fb3ce6ed2bf33dfb9140001e6401c2d4da79c2aa1d868a2279d1622a86efb58 | cad434627d0f2de8442c848bed751043b6a9713c |
| curated-report.md | 1804 | e7d05d9777bfe199010f0485dd410e93f328f0305f674a932d0e1aab2a9b17a1 | fa69af5cd074213fce53130d15ddcb0abe88c45d |
| sources_status.csv | 4138 | 99def15b9bcb7d7799e25d2ccda7fa49a2dbc09b4a370a2160e20a932f247577 | f3542239c9941bff43226acb1070dabdfc812fab |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
