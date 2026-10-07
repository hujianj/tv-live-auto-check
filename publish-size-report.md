# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 277600
Unique payload blob bytes: 184409
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 64047

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 21349 | 7a6abc4124074298424983353a86558c04c6f14c7bab5dc6648bbba5a9a8b2d7 | eee844525317377088431444d6cb2ee6532d585d |
| live.txt | 21349 | 7a6abc4124074298424983353a86558c04c6f14c7bab5dc6648bbba5a9a8b2d7 | eee844525317377088431444d6cb2ee6532d585d |
| live-verified.txt | 21349 | 7a6abc4124074298424983353a86558c04c6f14c7bab5dc6648bbba5a9a8b2d7 | eee844525317377088431444d6cb2ee6532d585d |
| ku9-live.txt | 21349 | 7a6abc4124074298424983353a86558c04c6f14c7bab5dc6648bbba5a9a8b2d7 | eee844525317377088431444d6cb2ee6532d585d |
| live.m3u | 40987 | 7853428d882a11b115e45ea03533efedf0b61c2a42222f57ec789c5b3e1593ee | 0a85fa52ffd76f6ea6ed93bd1a53e2bb05d86439 |
| ku9-family.txt | 21084 | e0e6703205d6e4c10cd4019f55f6844b65cc1d5f2188b54a9f60f3ad238d9259 | d9c2aa10102e5642e8f753c91d28160bd00f4a10 |
| live-family.txt | 21084 | e0e6703205d6e4c10cd4019f55f6844b65cc1d5f2188b54a9f60f3ad238d9259 | d9c2aa10102e5642e8f753c91d28160bd00f4a10 |
| family.m3u | 40474 | 4fa0455c6e6389480afac2f53c222e9d0070f39c054e211cc2a72a03a2c44fba | f65a74fefb61fef1b0c95eb2a9125e778d8cc349 |
| final-publish-report.md | 10781 | 16172c78dd6f245d94a68bf79af70c29cb356ff1c6a4378957a87034457d45cd | 08393f8cdb0b9f21e5b7cb2ee0f2dfd2cbaf4cc7 |
| coverage-report.md | 2235 | 0ffa5e713b9a342a015ec4c6daf46aed5b15a200857fddeddbb516fbed105326 | 9aca8c4854c4c4a947591d567ca0c1562f8656c6 |
| quality-audit-report.md | 4731 | 154b9a1c7793703a3b4468dff7230d15f38082bd9508468266809b029a2feb93 | 312d2696e24cab6a6fe4f33975cb83cf4c8953ea |
| publish-guard-report.md | 1609 | 28c603f504cd4c90c7b559d551a75b5d0f6f5e38a5f729c6f7c7f2ee8287707b | 0d2bcb1ed6a18442debbf9c16332b26150e75ab9 |
| published-recheck-report.md | 27188 | 2a3d3df8072ad18be3e068ac7b4fac53750f9219e2d7d6a718674e95e35ccdf3 | b0672efba98fa85987f58a45fae7d927112a996e |
| source-report.md | 8060 | 3aa4dffbdb7b61843e4ef454630df1c06da24b3c353e64aa9cdfe6d01399b952 | dd47b0073ee679c9f543b46f9b5b02598176bbe1 |
| check-report.md | 8060 | 3aa4dffbdb7b61843e4ef454630df1c06da24b3c353e64aa9cdfe6d01399b952 | dd47b0073ee679c9f543b46f9b5b02598176bbe1 |
| curated-report.md | 1804 | c10be32229c9f332d30c0ae20556bb7bba044d2fd85c74d77714f98b574744f2 | eca468b2ef0a6d80567ae44faa606fbf863bb77f |
| sources_status.csv | 4107 | 4c6c89b5993a35515ac4e3e55cdd2cf813ead06260f88cbf042e2b2cf288de07 | cf06b4eed064534556fdb6383cbd2b769e74ba72 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
