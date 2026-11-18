# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 348919
Unique payload blob bytes: 280812
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 40352

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20176 | 21c68ad208a15b7cfa0555aa0e308ba8d463629024a594e17c557831f80ccb2f | 1f38861c419292ee0f430d2d7ef738dec2dfc46e |
| live.txt | 20176 | 21c68ad208a15b7cfa0555aa0e308ba8d463629024a594e17c557831f80ccb2f | 1f38861c419292ee0f430d2d7ef738dec2dfc46e |
| live-verified.txt | 20176 | 21c68ad208a15b7cfa0555aa0e308ba8d463629024a594e17c557831f80ccb2f | 1f38861c419292ee0f430d2d7ef738dec2dfc46e |
| ku9-live.txt | 23405 | baed7827b09281e739617b9c76118ec9bf9f3112768b03ff45b8f1afbb7a59e0 | 360894721fb381f2e1deb1961d13c1524aba84cd |
| live.m3u | 38755 | 4555b2861e568635bdc32b14c60a9fc9d46a57cccb5881eec6a1ac7ccc909879 | 0baf609b195d668260747a842a2b9119c920a00c |
| ku9-family.txt | 19740 | dc82cef15927b769b3da286f20d9ee9c5b93ec259f228a26ad3bd4f1abbd746c | 46a998150ec3d1b4c2e58ca2b8f4b73735474bf5 |
| live-family.txt | 19740 | dc82cef15927b769b3da286f20d9ee9c5b93ec259f228a26ad3bd4f1abbd746c | 46a998150ec3d1b4c2e58ca2b8f4b73735474bf5 |
| family.m3u | 37947 | 8c79dde2d2ba0c170838b7dc363ecd1d5e7fd22b59951a649b521b47ca11fe8e | 9056a3786eeec5b48ee35eb9da6d15e885315935 |
| final-publish-report.md | 10867 | 3f1e2fdf0c7f1cf3d7cf5bbd9433eb8d6532e125c31a9548ba826f8252b42874 | 951ceb7e165e859d71ac749a07e1c51090d44353 |
| coverage-report.md | 2185 | b28674326bd91763c3e7b870586cc1afab1a3b48b926f33de0362db3dae08f97 | 7456e3146115f3583445e4628c2aa30ef6845a46 |
| quality-audit-report.md | 4652 | 09ba1217dd04022d12366cf140bd965d6e6550315816efce370fdf2193c08235 | 96e83161f7ab2e67fd6a498fc07955d384af989b |
| publish-guard-report.md | 1475 | 422a53c8df9e7fba12dc01c6bfcdeb2e3527ef22a0e0db045c9fde946350e437 | a1614b938ae818343035f0c4ce0acd1db20601bc |
| published-recheck-report.md | 30340 | 76dc87a0d4f6d7ff1b68abaa98a85b324fcce552dc8a245b185f26238d0cf761 | 8b6285190c490cfc040db373bb9e95ec5626da7c |
| source-report.md | 8015 | e995fc4a82883422297bb8a94678cf64b0c6c5e8e55593aa3ca5b7242fbc9623 | fa21a73b28a1b2b303af5f9692ea88a16f16042d |
| check-report.md | 8015 | e995fc4a82883422297bb8a94678cf64b0c6c5e8e55593aa3ca5b7242fbc9623 | fa21a73b28a1b2b303af5f9692ea88a16f16042d |
| curated-report.md | 1834 | 95684e6959df873d523aeb5aa716885f111cd00719f494bd71b404ed0109e916 | 6965925623766ac75f4f9662452a1d521e5aed21 |
| sources_status.csv | 4123 | 3dadb570999fd4bf8981e63c3453f85f3142d08dde7b52a91e898e87713580ca | 9efc96b48db577b43ff95e5561ca716fad4405be |
| tv-coverage.m3u | 52943 | 0b13660fa14abc675b8199737c5b700f5d29947ba04195c171651e2f2fe9bfb4 | edbeed064392c8aadc0957c3ef3a894c5c2051d4 |
| tv-review-report.json | 15365 | 9fbb1a78d7f50bf96b8208d5f8c8495ea1be5dde9e68d4d969f3ffc61874fdec | 8d1b5603f5f1f8a5aaaf69f77aa83176862215a6 |
| tv-review-report.md | 8990 | 46bea6c7d289557fa264758b86e5f33113a321ac24c4769ac23bff51c38807b0 | d8db6a3bbe4bf145066e49e157410800d9b05e89 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
