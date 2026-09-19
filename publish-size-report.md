# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 305045
Unique payload blob bytes: 201259
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72087

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24029 | 46059e2bdce2ceb9c276c180b9a5e9991939e25f54ba6093aff8a3d50cf72aa7 | 0e950e7d92443799070e667bbc4060b2c40ea1f0 |
| live.txt | 24029 | 46059e2bdce2ceb9c276c180b9a5e9991939e25f54ba6093aff8a3d50cf72aa7 | 0e950e7d92443799070e667bbc4060b2c40ea1f0 |
| live-verified.txt | 24029 | 46059e2bdce2ceb9c276c180b9a5e9991939e25f54ba6093aff8a3d50cf72aa7 | 0e950e7d92443799070e667bbc4060b2c40ea1f0 |
| ku9-live.txt | 24029 | 46059e2bdce2ceb9c276c180b9a5e9991939e25f54ba6093aff8a3d50cf72aa7 | 0e950e7d92443799070e667bbc4060b2c40ea1f0 |
| live.m3u | 45889 | 44ff201b12fdf57e132581cc20b9e52a6321010620c3bd74801fe1fe09f89fa2 | 691e3a76032b4834d42b4a190aadb0541a1d9e73 |
| ku9-family.txt | 23663 | 3adadc4fa924425220469816d537351e63382ad322c893959f114f868f7d3e1b | 9e91dfadf103e51d08e4496040ce714bc1bf987d |
| live-family.txt | 23663 | 3adadc4fa924425220469816d537351e63382ad322c893959f114f868f7d3e1b | 9e91dfadf103e51d08e4496040ce714bc1bf987d |
| family.m3u | 45213 | bfcfb811bcaac53fb8d6ba5d005988a7c7a7930a057687f3b8bd59251cf96783 | d21312e11b72b6d91b77e00edacec0f1a76b87be |
| final-publish-report.md | 10774 | eda731d8221030515741c07d4f598c629c5d9304990766d67135822e19b389bd | 61e2a5124c37170197bdef9ddd35950b735dc15b |
| coverage-report.md | 2225 | 578e95bdbd7ab2b6d8601c6724aa91edf800897cf62735c505497d7db4a3a50a | ad016eb7485cedb4497bba7ac21407363c323507 |
| quality-audit-report.md | 4719 | c50432dcfdb75a8a7f0c5389cb09bceaf52c7cd4df1b0531c6bbbe0cb2790ff9 | 18475f5397cb507955d94b04ba2ab47eb8132466 |
| publish-guard-report.md | 1581 | 3174ff12e5223f597913b3f07d6c2d25fac0ac956e7b9120705279e8b6fd3721 | 143f7c6f982bffb692b6e0177c5a5759c382e8db |
| published-recheck-report.md | 29252 | 98aa23aee3c6ea16d7d9709f293b4210c905a89a767ebd935d436867b63e2140 | 90b06f3ba539d3d07ed7c8da45e1f3b5082adbc4 |
| source-report.md | 8036 | 1e34c0f3408d535bf74d73f7d38d292d39329506279f1d4e6a22d2a72a231650 | 130373d62999a1349fa775ab022c8b78c0661d52 |
| check-report.md | 8036 | 1e34c0f3408d535bf74d73f7d38d292d39329506279f1d4e6a22d2a72a231650 | 130373d62999a1349fa775ab022c8b78c0661d52 |
| curated-report.md | 1804 | 6f4656c48514143b0a2387e60e375daa53ff9803d55af08bd4ebe483a8b5ab9d | 9f248e0e7040e6f36d18403d1c18dbf57a18a076 |
| sources_status.csv | 4074 | 2b6f90673360ba2f04dffed2a574ca10fa7d5844743796fa898f0882272329d3 | a8dbd97e4ce21c80c2689ba0983f41b83c302d1e |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
