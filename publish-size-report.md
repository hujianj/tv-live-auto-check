# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 282320
Unique payload blob bytes: 186462
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 66117

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22039 | d91439b46404909ac1173a60b96bf37fae027038fdbded02f3667745cf192764 | d9c3622ab7d59091ff98dccd1dd482fdafe5a06c |
| live.txt | 22039 | d91439b46404909ac1173a60b96bf37fae027038fdbded02f3667745cf192764 | d9c3622ab7d59091ff98dccd1dd482fdafe5a06c |
| live-verified.txt | 22039 | d91439b46404909ac1173a60b96bf37fae027038fdbded02f3667745cf192764 | d9c3622ab7d59091ff98dccd1dd482fdafe5a06c |
| ku9-live.txt | 22039 | d91439b46404909ac1173a60b96bf37fae027038fdbded02f3667745cf192764 | d9c3622ab7d59091ff98dccd1dd482fdafe5a06c |
| live.m3u | 42383 | 65fca18bc2329c53e87f5b50eeb6f11ec55cef668ca874586bcec28d8cdd87ae | fbd0ba23bec66bfe26eb1214df1dba0762b5146f |
| ku9-family.txt | 21774 | 76b3ff25b144af65ccff2fef587d2a739c4f961a8ae00eda8322ddf3e11fc73f | eedde82207a8f7b7d83c119b66b379746c3fcfb7 |
| live-family.txt | 21774 | 76b3ff25b144af65ccff2fef587d2a739c4f961a8ae00eda8322ddf3e11fc73f | eedde82207a8f7b7d83c119b66b379746c3fcfb7 |
| family.m3u | 41870 | df2005ec6725d6af6152d4308fa0699624a72692f917975383452e915b143a36 | 50cabb3486d77ab3359e0e7a2b5f911c75abbff6 |
| final-publish-report.md | 10616 | 9765cdbe989db1a6dce3876302a5a6715de4e0ae80c0986c8d14fa2de97900f4 | 7a66ec1b0a916fbbbe0cc1e219464e16dbf423ee |
| coverage-report.md | 2230 | d1d020684cf697d4d536c96bfeef041cf18cd5ef19053ba4c7329e180cc8fb60 | f83c90434d6d9565835b202c6b57a63d7b9e81ac |
| quality-audit-report.md | 4724 | 89f47bfef1e8d441e9adbb137eaa614f9609b1aaba4495617b3df7fddc010454 | 170b877b9f0cf1646477cb7754883b464289f102 |
| publish-guard-report.md | 1552 | 31df86e8ba42a464e5e026086acc6fdde861c69bd7398ce5874afd835c3486fe | 39cf21c980500407026838d5bf43dec0d1fbbf16 |
| published-recheck-report.md | 25480 | cdd2dac8761a40abb4fe9b9bab27772d65a2e10c6ee69a79978370d9ee074e8a | b3c6268695ddc6e46c2ed8624a708bccdd72d105 |
| source-report.md | 7967 | e81d7c3842dc0c40c4c032ed3c28d6de1b612f1ca97c16128c0cfbbdc770b0da | 5e0945c226dbb8ee4c78bc393afc4896bbd80aef |
| check-report.md | 7967 | e81d7c3842dc0c40c4c032ed3c28d6de1b612f1ca97c16128c0cfbbdc770b0da | 5e0945c226dbb8ee4c78bc393afc4896bbd80aef |
| curated-report.md | 1805 | 43e5259bf86f6d08661d1010555ebbf090be2e40088b384e1555d9f0510757cf | da7b19dea6606b2d3456f438298d5307e12c6093 |
| sources_status.csv | 4022 | c4a1b60d68103831e6e5393b6d8865ee7f548bdde9e2c9539db9c6e772ca198d | 77908602ab2434944cd3283fa467bd9f7e906f16 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
