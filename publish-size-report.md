# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 342796
Unique payload blob bytes: 277244
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 38584

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 19292 | 45815a9f5ae670764f62698613ce84ba72e4de131a4e2bbe38055d15c9fe01b5 | 788658b43bcc18bfb506eb324f6e1775aeb5d68f |
| live.txt | 19292 | 45815a9f5ae670764f62698613ce84ba72e4de131a4e2bbe38055d15c9fe01b5 | 788658b43bcc18bfb506eb324f6e1775aeb5d68f |
| live-verified.txt | 19292 | 45815a9f5ae670764f62698613ce84ba72e4de131a4e2bbe38055d15c9fe01b5 | 788658b43bcc18bfb506eb324f6e1775aeb5d68f |
| ku9-live.txt | 22887 | 5d8ca0ecdb5836d2c6d7048cb1ad166c5c35d16911ba62e20a71b84df626263d | bc81a380825a4fdfac8d19b55c51db1597224db1 |
| live.m3u | 36934 | 2c61e03b242d6e35c5618d0af257370f89397f283e8836055be0e1ce998722ba | 2c00ecf84dc60041b7909623cb7028cf350656da |
| ku9-family.txt | 18856 | 412461fda0e54ea00792fb7785307e4578075debb554fafbce506cdc53384b95 | e8c485d5a816208d35e551626ff5ac53c1cc3e5c |
| live-family.txt | 18856 | 412461fda0e54ea00792fb7785307e4578075debb554fafbce506cdc53384b95 | e8c485d5a816208d35e551626ff5ac53c1cc3e5c |
| family.m3u | 36126 | 9a34dc9f25a119633d0fa44d295eb55497d3ba03aad95c3e47a6c8d8fe052ed1 | 12b6d6091f4c4ac226f7df816450f3d87948774d |
| final-publish-report.md | 10926 | 76ab19718d445c1d320c8b4c974021af2182a370337875c0ae25e6025fc91ae6 | 471bfec4704b9c29d359359ed8e2904075b77776 |
| coverage-report.md | 2195 | 998537819151a9fd18f448a97a5a1a5dee3735998d4af71fec41935facc2af5a | 020376fa5993c7a651284cff8e0217eb6aca986d |
| quality-audit-report.md | 4664 | 4ee2105c06cee03237d2c9b6407010f1893c7bd19fc077eea8847d2b36db5c8d | 7251f5771f67f410a21e693329a498d6d175eec9 |
| publish-guard-report.md | 1504 | 0237802b10f8340a8f3e2d6d70256777567090cca7e731a1f48c702b75492aef | 704a81a55bc1c5f9de0467fd56cd640e39f0139c |
| published-recheck-report.md | 31298 | a561e768281c89800aac1c9e2e67f578b6490ac461d987c16e8926f4ddcf3fc5 | 9b64b7a0532e97056a1e284ff42069f7249b2e9f |
| source-report.md | 8112 | 2d43ec18f47c9448c0765926303f4d3ddf4a943c2d1dd56b11c02a520f42d11f | f7a0fcceb49cf5677f62b1dd42cf572bb53d6bd6 |
| check-report.md | 8112 | 2d43ec18f47c9448c0765926303f4d3ddf4a943c2d1dd56b11c02a520f42d11f | f7a0fcceb49cf5677f62b1dd42cf572bb53d6bd6 |
| curated-report.md | 1833 | 650e21e337877ace9366834f69419ca8162955539cbf14cfd8cd8eb32750230b | b1dc4a961f6812fc4a57a8f4cfcf1ce4d04f5039 |
| sources_status.csv | 4182 | 4aa7d20f2e96477e13d64d1651e9248083adf5fb21d9b6b8ad24ebfad04cf3be | 64e1e8d3a8f3d17e23d3fa5fce7cf6c35c37645f |
| tv-coverage.m3u | 51563 | 5b6d9e3e94b4f2e3e4c2e23ebe7ec9786fa91cd07f45b8fcccf2e20dd7ac5496 | 0ce3ce32087ad6f8ba7ab61866dac742f6d9310d |
| tv-review-report.json | 17111 | d48262a4906cee39563f3cf8aedb0e2db77277c2433c67f8f1fb08ce89089229 | 71db6a3e6807a5f4c363abb7bd3f859d792b0493 |
| tv-review-report.md | 9761 | 31c3c56abb1ea6c64fc4d1ec762682eb6f2e06237f3a5be7ffd3738711a45b1b | 8b39a79b32dc85da1ef740f8a93851acc7cfb204 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
