# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2111581
Unique payload blob bytes: 1525558
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 492219

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 164073 | 75db980fba0256244c4fed3d981596c107ca885e367cab94241155ae55113181 | c94e95644532f6b146036246121f13b39be23a9a |
| live.txt | 164073 | 75db980fba0256244c4fed3d981596c107ca885e367cab94241155ae55113181 | c94e95644532f6b146036246121f13b39be23a9a |
| live-verified.txt | 164073 | 75db980fba0256244c4fed3d981596c107ca885e367cab94241155ae55113181 | c94e95644532f6b146036246121f13b39be23a9a |
| ku9-live.txt | 164073 | 75db980fba0256244c4fed3d981596c107ca885e367cab94241155ae55113181 | c94e95644532f6b146036246121f13b39be23a9a |
| live.m3u | 295946 | 2cf66d56d5405ac374153fbd8ff5e2a59f5eff2dee19d71b77d36be787085787 | c90ae9bf80b6b952ab95250ab87bbf4b5e8a7f02 |
| ku9-family.txt | 87236 | 189a4e681498463ae31e15736c8f302cb7750b1d013f70087afecef065fe7946 | 027d07f95f068808e29b483c22536a290b636483 |
| live-family.txt | 87236 | 189a4e681498463ae31e15736c8f302cb7750b1d013f70087afecef065fe7946 | 027d07f95f068808e29b483c22536a290b636483 |
| family.m3u | 156173 | 2febe214d2ff34a47231b9aed2b1eb242461cdac6af2c6804a0648f69d80cff9 | 03b31f63470fd8b0c990c16c3075ed0b830c68d2 |
| stability-history.tsv | 755206 | b02474d9d7998b29e3b3af6c8d02921aec142507569fd4b5a4bfb54b965c74cd | 6f525af2085a025ed882dddd4e6f36fed3e78462 |
| final-publish-report.md | 11596 | 3ec70140a37798323345d1dcf4e2121db269c3ed6fd225c9e53a51da8c5ac0e1 | de9dedd87add12c088842cedf6721c948789e98a |
| stability-report.md | 11188 | 4e4d90acc8d23578a540311dd4b6a5a661d24d821bbadfa44be43ac7c4073931 | 571e7b7ad3080cffcc1e22ae344a8013a2d5c9f9 |
| coverage-report.md | 1291 | 538b545c146dfdf733ccf4f9592de52ba4799181aa484fa923658f8926d6b838 | 9fa8604d2e4fd155d031a9b96d9e1c4502c66ab0 |
| quality-audit-report.md | 2063 | d44c1c5c353d96ed43140d2c70f7b381533e8645363f7f9881e104006d95ce2c | c9092f72a2b32492dcb29bd1e4f2e727221bec8e |
| publish-guard-report.md | 1143 | 98d1771a3ff7ac9ef44f44db4b32e854ffcf539b379b78355c6837ec86d5f522 | 57a10c0d14d61be412778bef3482dc31faf2fd4d |
| published-recheck-report.md | 26552 | f325e1fc4f36c71fd40e3e0bdc1a7f3683e69f9306775acef4a23baeb79a0056 | 17c7b6baec3eabbadbba125e7d016adf9bf48287 |
| source-report.md | 6568 | eec0fabf0dc0fe857bc696839d473dd5eb1c0a02bc41455317fc8ee033ec249d | e401e485259e146b5f3a2082107faecfbe478242 |
| check-report.md | 6568 | eec0fabf0dc0fe857bc696839d473dd5eb1c0a02bc41455317fc8ee033ec249d | e401e485259e146b5f3a2082107faecfbe478242 |
| curated-report.md | 3382 | 0d4d34105ce675501ea1fde93cc23ce7cc347fa22b015b0628178793ece51e44 | 7cd037a7664d2d004fbab172b53b7899cb08ff74 |
| sources_status.csv | 3141 | 8043cb9fb747b915478dd77de2f416b21929408cf128ad0f8fa9155752edc121 | f41faf6be0df17955c245c1b60aa216316c327d3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
