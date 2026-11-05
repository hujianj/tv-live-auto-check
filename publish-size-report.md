# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 267525
Unique payload blob bytes: 216784
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 28652

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 14326 | c1d2bd4a62aeff2d6882a183a388af0288b8c567c6683cd13e7270ddcf4020b8 | 60a5ea3a6efc830b3fc702460c0b5ed4a96b3f48 |
| live.txt | 14326 | c1d2bd4a62aeff2d6882a183a388af0288b8c567c6683cd13e7270ddcf4020b8 | 60a5ea3a6efc830b3fc702460c0b5ed4a96b3f48 |
| live-verified.txt | 14326 | c1d2bd4a62aeff2d6882a183a388af0288b8c567c6683cd13e7270ddcf4020b8 | 60a5ea3a6efc830b3fc702460c0b5ed4a96b3f48 |
| ku9-live.txt | 16505 | eead121a6e7fc50aff0408fc986d01acf1daca36c00ce74778ac2795ecea4600 | c39224a3f59cc9ddfefbe5ebb269adf62787f081 |
| live.m3u | 26943 | 4dafe3bca9c99340cf7f3eeff9b5616f9d48277f79bb45237d1a868422837cae | 88d9fbb679c9218bf09bf8c21d9cddfec5c9d2a7 |
| ku9-family.txt | 13967 | db7b80569673c8203d3e7a474c0dcfa4cee77e89a8e52c1d9b36281cd8e3fca7 | 080f7d38ce26389aec7420abf4344454236318cf |
| live-family.txt | 13967 | db7b80569673c8203d3e7a474c0dcfa4cee77e89a8e52c1d9b36281cd8e3fca7 | 080f7d38ce26389aec7420abf4344454236318cf |
| family.m3u | 26274 | b0190a78eb3b5a69ef2019cfedd24db4c930cb1748d619e46620a7435961b65b | 9966b262d39d088ef64871185ea04d1ad322625c |
| final-publish-report.md | 10893 | 8fcb0ca2038aca160c3d92048c3da96a760609359b9dafa381c793e05075ad64 | 0a5294daef48056abeb3b830229bba1a009d1faa |
| coverage-report.md | 2200 | 14ba06b125687c3af4837349f2efefbf1e8b9a283251dfb82577e57b19ee4ced | 97574bba842647b0e789639aef330cd5cc4f79c3 |
| quality-audit-report.md | 4687 | 7e5064a4e3fa88b968d6ef436130d87483496a119ba5dcef551a219cc3dd8821 | 489f4a0d95e7ce02c51353f2cd0d16434561916d |
| publish-guard-report.md | 1529 | 5de79948cec13a82ce7ae586f45f21f7800a8ced4da9636840c8e8ca3098d6a1 | 3d586b858ca3357acb4af819c0266a88f63ff132 |
| published-recheck-report.md | 31005 | f1b3d9cb86eca7c8fc2f4f1ee3d8b94973eed01e36ba53dc3125a075c42a9c2e | a232cf46357e77580fa244dd3a5ee817fc1c1dc0 |
| source-report.md | 8122 | 7954ba8cc70a6dfb028182a7fffa2cb3b6795751bd84a8f44e9646ea52434967 | d9a6c32fe79e6d961b43299b6b8295f1113a0824 |
| check-report.md | 8122 | 7954ba8cc70a6dfb028182a7fffa2cb3b6795751bd84a8f44e9646ea52434967 | d9a6c32fe79e6d961b43299b6b8295f1113a0824 |
| curated-report.md | 1808 | c70de74ffdb8b23a94611c70442e14c03b73b8512229e31795770925f285c693 | b6c84df5acf2d47fc622a96c0b3853a841b0f3ec |
| sources_status.csv | 4121 | 235b49a66f1671968b339fe31417e14364ee49eee977d791ed3e4fffd5ebfa55 | becffb522dc64a4309bd4bd1028a65892905f5ed |
| tv-coverage.m3u | 37029 | 38f8c64f5d6b320ce8910b804a69817da9f77388d93507b3c446c0e37630187d | 8ed7390647f77d5f757527ef551aaab02d3e5b21 |
| tv-review-report.json | 11290 | 02f92117e03d084669c6b471601d9cbb0b5c2cd357f00372b397c05ae0646362 | 5c1b6d33065afabb27e49ec1f10b259842346200 |
| tv-review-report.md | 6085 | 7294dd5e01bcedce4bbb3d69b39328eb4ad0e25a4cf3d5e4ddbe2c62b44aad78 | 8f5259e5403705e9dcacf16399f7818eb4b1a305 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
