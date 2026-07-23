# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2479912
Unique payload blob bytes: 1724294
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 653436

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 217812 | 0c7399bbeab5743870bebc886ebbf44323fde70c63dcd001737b8582c32eb913 | e70a9c09fd13bcc8370027f147a0411d70f62763 |
| live.txt | 217812 | 0c7399bbeab5743870bebc886ebbf44323fde70c63dcd001737b8582c32eb913 | e70a9c09fd13bcc8370027f147a0411d70f62763 |
| live-verified.txt | 217812 | 0c7399bbeab5743870bebc886ebbf44323fde70c63dcd001737b8582c32eb913 | e70a9c09fd13bcc8370027f147a0411d70f62763 |
| ku9-live.txt | 217812 | 0c7399bbeab5743870bebc886ebbf44323fde70c63dcd001737b8582c32eb913 | e70a9c09fd13bcc8370027f147a0411d70f62763 |
| live.m3u | 389884 | 80c76da8ecd85c57b48ed61de14aa7f3974c3095f9be909e09112494980d0d6c | a114098772e6cf9b89f02db9041f517a77e9c24e |
| ku9-family.txt | 96356 | fedbf5967f9a4080f76785bcbbf6ce43584f56ac5622a4ef10425e3aa9eaf52e | 3806e6e19a1e881beaaf84df0052252cef411381 |
| live-family.txt | 96356 | fedbf5967f9a4080f76785bcbbf6ce43584f56ac5622a4ef10425e3aa9eaf52e | 3806e6e19a1e881beaaf84df0052252cef411381 |
| family.m3u | 174104 | f69b9c39d6cddd42e83224174681212da6219a7ea291e82ffe9311e6bd15545a | 4325cc71561a97905fd1dd543391c6f0dfb147ed |
| stability-history.tsv | 779344 | 1e5e61e9a2caa5ab13ed45a51e32c5e3985aff31d55842f2f905de3284a89074 | 6e3970d4e7947cbac973641deb4097752c075e9c |
| final-publish-report.md | 12477 | 1e8157d650b999f01510c1909ab100200e1cd6ca100b3984bf52dcfac94fb286 | 3a9ad435c2913d34d2e9fb46cd772d315d096fb3 |
| stability-report.md | 10263 | 72947e28ca4ad3c50eaa9e999a6634bc3b4d6a257707e23fb2816a13762818bd | 295ee31225fa5ab8564d142b7843c92d680aebcf |
| coverage-report.md | 1329 | bacfa63a6266c909ca18a0a5aa78112a2d885350435d449345e01b3339ed92dc | 1185fcf7438f9939d2e330390c16b4963b255ca1 |
| quality-audit-report.md | 1504 | c64ce36e23bd8099282bbf5758e046eb3c3957357082421b433b47e7b8f4cda9 | f196757165cb881ec5034d3318d372e81d421c7b |
| publish-guard-report.md | 788 | 9cdd0235f3ed63f53fe7e9ae382e3c16ff58d20d1449e0e536ad07c316e7d3e5 | 6cae1bee8a611d43ce6087fa61084fc8efaad9d1 |
| published-recheck-report.md | 28394 | 20f902527d11736f60fc9aaa9be8951e8355f8f9adb14e7172e0c3e73c37e1b4 | 1d113a94b9faa31b27341da6bc6aab8ff4478ac0 |
| source-report.md | 5826 | ff6195e02bb07e3eb8af866f4f32e8ad88a5393b7b98a6a533ef5c0fb8a81c71 | 69119c1e75394e3ce87523881ba309fa15cb4176 |
| check-report.md | 5826 | ff6195e02bb07e3eb8af866f4f32e8ad88a5393b7b98a6a533ef5c0fb8a81c71 | 69119c1e75394e3ce87523881ba309fa15cb4176 |
| curated-report.md | 3612 | 359189656caca28ef0576119a354142a68329361bc9c2f23c99b74d38b0ec128 | 87150230e9925151b6fcd11e3cf0b025cf52b5bb |
| sources_status.csv | 2601 | b02b1e8e08b0183fe940500dc60d120150bd329b9a7b4e4ef89779d4c8877b2a | 2c619b1c036be65062a27cf796e4d93961924b67 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
