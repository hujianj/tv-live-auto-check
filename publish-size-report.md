# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 282307
Unique payload blob bytes: 187491
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 65235

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21745 | c00b59c05d81f0aa18bedc7d4a0c343120f92738ecacbee4caf5ef9145c937a6 | ba7f9529f090be816628a8f96381f3110548588f |
| live.txt | 21745 | c00b59c05d81f0aa18bedc7d4a0c343120f92738ecacbee4caf5ef9145c937a6 | ba7f9529f090be816628a8f96381f3110548588f |
| live-verified.txt | 21745 | c00b59c05d81f0aa18bedc7d4a0c343120f92738ecacbee4caf5ef9145c937a6 | ba7f9529f090be816628a8f96381f3110548588f |
| ku9-live.txt | 21745 | c00b59c05d81f0aa18bedc7d4a0c343120f92738ecacbee4caf5ef9145c937a6 | ba7f9529f090be816628a8f96381f3110548588f |
| live.m3u | 41782 | fdde0b9f04179e0497d9425845c8c3b00398b0a803fff81a18253fb1ff86cc2c | 57238cc4e313d54d51dca870f2366ec7a3dd9003 |
| ku9-family.txt | 21473 | b67760cedacbb1f3e1ed1efce9a3bb5ac504a674ae5335e6c4b8a978b72bfd35 | bfc351d6c493f186d744c8412648ccb5a2b89456 |
| live-family.txt | 21473 | b67760cedacbb1f3e1ed1efce9a3bb5ac504a674ae5335e6c4b8a978b72bfd35 | bfc351d6c493f186d744c8412648ccb5a2b89456 |
| family.m3u | 41262 | 1b399c955f3d259baff4d1755821d5eec14f7ef7a709c928f744b31440ec974f | 767ff7ec5ea6113ee51eb785dbcaa1394efa282b |
| final-publish-report.md | 10722 | c57c127e6c62a850a528c4f89dd814f802be9c1936396f797fcecf1c572973e1 | cc7fccb552ccfcf0e7d19140ac161a5b377a2116 |
| coverage-report.md | 2230 | 5e70478be9925aa5c5f0f1b96725e8ece693a48e6437a302da928d5ca8ec950a | 93fe7392d8d59adb8257539be9031cfba187e403 |
| quality-audit-report.md | 4730 | 9b303019b4fe789fa457d2d2c887b2e4575a8b450d0e169a37a35eb6c3430f79 | 3304dd4a7af854f4bd447765499d42f7bb0a5870 |
| publish-guard-report.md | 1609 | 12273b5e3d533dd465a5a464d00b8c6ccfdab60afcc6ca07d4bcffe518126b9e | 7a8ca39c973ecfaca16226f7f71228284cc652e3 |
| published-recheck-report.md | 27894 | f6bf0c626053e4ad64c1c84af79ba309c3b7823c572d09a1fd5157bee72addd8 | 49ba90962165c7e6a738a076b4d4fec4ef064159 |
| source-report.md | 8108 | af96192267732a887d99df43a01dd6dfb15bae97ef6bfd0bf67464221fe11e48 | 5b3865dc2fce30b834ec884d8f9c8d86381d2afc |
| check-report.md | 8108 | af96192267732a887d99df43a01dd6dfb15bae97ef6bfd0bf67464221fe11e48 | 5b3865dc2fce30b834ec884d8f9c8d86381d2afc |
| curated-report.md | 1804 | a53e2b6f89f1e41a39d19f8deebe01b36b7a834fa46bd793402de7de9bb01b7c | f7ca2b8614d22353c174844064dd4785cd32bb89 |
| sources_status.csv | 4132 | b5dba905c71696d29e51505d0fc9dd6f296f901c9e14464b14dc3569ca97b0a6 | 14d1e4c955912773df20c07dad7c9eefa99f809a |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
