# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 314117
Unique payload blob bytes: 206066
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 75453

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 25151 | 997000383c89c79ef40fad994248048a8f2fd0b34dd668b8293d2b15286322d9 | 609382f03eee631d7a914bcfee073f9f4f679d61 |
| live.txt | 25151 | 997000383c89c79ef40fad994248048a8f2fd0b34dd668b8293d2b15286322d9 | 609382f03eee631d7a914bcfee073f9f4f679d61 |
| live-verified.txt | 25151 | 997000383c89c79ef40fad994248048a8f2fd0b34dd668b8293d2b15286322d9 | 609382f03eee631d7a914bcfee073f9f4f679d61 |
| ku9-live.txt | 25151 | 997000383c89c79ef40fad994248048a8f2fd0b34dd668b8293d2b15286322d9 | 609382f03eee631d7a914bcfee073f9f4f679d61 |
| live.m3u | 47710 | da90f2473bfa3e907f803b7d19fc98214c4891a31bdaaa646d0101e31078ff6b | b3f2f4be152f369c3c928320774d818f3d02ab3f |
| ku9-family.txt | 24729 | 05945134c909bb0811ccab722cf0272a0f76cb94fede5f300adfb0740c87f740 | c2c609fce08117aa2b361fced8ac412a065d5201 |
| live-family.txt | 24729 | 05945134c909bb0811ccab722cf0272a0f76cb94fede5f300adfb0740c87f740 | c2c609fce08117aa2b361fced8ac412a065d5201 |
| family.m3u | 46916 | 4de8814cdfe73815c1f837e02b86e3371d49b39f161b0efcf0ebd9f61851175c | 27742bc2267af8e2a8ff6b6422a2c8ebd9aa80cc |
| final-publish-report.md | 10510 | 9844ec2b1a18d3e0bf23fbe117b55ce660f5ce9c48e871970c78d5b2f8cfb6e7 | 2de2ed6d35550ac32684f011c6def866400f1329 |
| coverage-report.md | 2200 | e47edf0c24405dde0d2d315bd90434408a1c50b6c8d41c5851b2569148b1a2ce | 91f641bece66aae64cd9271d558e68a109754433 |
| quality-audit-report.md | 4676 | 87ecd300dec0519f92f1d8178b6f9f276ce52cc7039c6e3cd38d1d4e8e536e55 | 8991015f44e793f66063abaf88d055ba268c0a96 |
| publish-guard-report.md | 1588 | 567ac417c5ca3732226a09459a23074c90f74220e716ba780a6c5c64f3de4c6c | 8d7e509a2c8252da4d2f3e037c05651863abf06d |
| published-recheck-report.md | 28663 | 42ef11dd7f618ffe69bf089f6a1a1922d401b3966dc4a64b57df339163c826c0 | 63d1f8c1141d1e514dd226759bc3a49a59d326a7 |
| source-report.md | 7869 | 1621ed7864a2dd89c1a732465d157e40c2585ac181a2bc8808a44b2a17924899 | 5ed6a9f3e8209d501eba4f149cc354e16808add0 |
| check-report.md | 7869 | 1621ed7864a2dd89c1a732465d157e40c2585ac181a2bc8808a44b2a17924899 | 5ed6a9f3e8209d501eba4f149cc354e16808add0 |
| curated-report.md | 1861 | 4225ad950d62157a6ff773dd0c93c72ea54b5f711c9654d0396659287964696b | 33ea82000cbfc39359057da07effd3a0d0daf523 |
| sources_status.csv | 4193 | fe1dbb7901bfe507060cea282f1611d3f75152f13a62301f88f679e84b5843b5 | 25e25d7f75d2a7e3a5998df03cf79edc963a85b5 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
