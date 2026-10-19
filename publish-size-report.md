# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 305077
Unique payload blob bytes: 201303
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 72093

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24031 | deeccdce6a7c4e39f9aaa2c3c1364bab38fc473c71e21db7b4c1db4cc263716c | e5754bb390d1ceae961bb969b09be65dc8e7d841 |
| live.txt | 24031 | deeccdce6a7c4e39f9aaa2c3c1364bab38fc473c71e21db7b4c1db4cc263716c | e5754bb390d1ceae961bb969b09be65dc8e7d841 |
| live-verified.txt | 24031 | deeccdce6a7c4e39f9aaa2c3c1364bab38fc473c71e21db7b4c1db4cc263716c | e5754bb390d1ceae961bb969b09be65dc8e7d841 |
| ku9-live.txt | 24031 | deeccdce6a7c4e39f9aaa2c3c1364bab38fc473c71e21db7b4c1db4cc263716c | e5754bb390d1ceae961bb969b09be65dc8e7d841 |
| live.m3u | 45945 | 3d30760b6ab3e33ce52b40c96060158d5fbaea376f60250f60348b6a4796a8c9 | 27559362c476364749ad37b0d941cf7e31bf0ecc |
| ku9-family.txt | 23595 | 11eb14da96556f29e45b6eaf2c7dd856bfdbc51fe000752778c37431ec786b32 | cb8c2abb333255906a570050988c7d372b187075 |
| live-family.txt | 23595 | 11eb14da96556f29e45b6eaf2c7dd856bfdbc51fe000752778c37431ec786b32 | cb8c2abb333255906a570050988c7d372b187075 |
| family.m3u | 45137 | a91528b110b1e91a29fc0162264c8036f81834655f15afe04d9ee5c082fdaa1c | 283a16fc4be09835d3df16a8daac3b1bf00c3079 |
| final-publish-report.md | 10816 | 4316c6617f9a8f419933bbf52e4513267e4f40dd4f0f9310cfb3aba0fdf668ff | 1648e7c3852f8c01a5db68220238aebd19ac3caf |
| coverage-report.md | 2205 | c31ba503fde072709ac0257c2c024f8f894e23fb4ba4822372ebc3326e54af52 | 2addf45ee6af55b76535536f709950e6d446c19f |
| quality-audit-report.md | 4717 | 8b55b3c3b051bfcc24c24d10b48b1bea778c2711544d415fe0241c24c2b6f4b5 | 92e0aa941dd441a9e2f78a23eb2420e8d12a9ab6 |
| publish-guard-report.md | 1618 | 4b2026d94c9e1eccf0d2be7faa2b3f3197f19081c4b8669cc31c15d280f533bf | e6399451888032296aadf6e6678be8edbf614542 |
| published-recheck-report.md | 29209 | 73cb94f0eb3c42e17545c80b7f9e113b7fcee5ef1c973b217f68b4f7cedbc45e | 424b9c49828174483f52621dfe9e87161ff9e31a |
| source-report.md | 8086 | f3623cb1b8ea47cd2df3e4e4cfdfefcaaa5d8b9a58c9ac6891afeaac8866b499 | ec3ada445c1d239ac399797f14f932f08d21ee84 |
| check-report.md | 8086 | f3623cb1b8ea47cd2df3e4e4cfdfefcaaa5d8b9a58c9ac6891afeaac8866b499 | ec3ada445c1d239ac399797f14f932f08d21ee84 |
| curated-report.md | 1806 | 4dcc1971a7196db200aee1190131b7b9a8f8d557b34622c60af32666f8ae6ae8 | f0597f90b796a160aba85c58c77d72b9aa5ad221 |
| sources_status.csv | 4138 | 7219965ffa70a9e61a5bba3579eef0cdb3470d80ce661be35d594033eb572687 | b53e61bd2fbd5cf9a8e7d09687fa1bf2cd32ccdf |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
