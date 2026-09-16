# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 308302
Unique payload blob bytes: 202870
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 73428

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 24476 | 9467f0f69077ccd52a5038cd755e19006ae66ca66086d53f489fe3723f80214e | 4aa2487d4d65150b85b52d56de7932261ac73db7 |
| live.txt | 24476 | 9467f0f69077ccd52a5038cd755e19006ae66ca66086d53f489fe3723f80214e | 4aa2487d4d65150b85b52d56de7932261ac73db7 |
| live-verified.txt | 24476 | 9467f0f69077ccd52a5038cd755e19006ae66ca66086d53f489fe3723f80214e | 4aa2487d4d65150b85b52d56de7932261ac73db7 |
| ku9-live.txt | 24476 | 9467f0f69077ccd52a5038cd755e19006ae66ca66086d53f489fe3723f80214e | 4aa2487d4d65150b85b52d56de7932261ac73db7 |
| live.m3u | 46578 | 2e2366b30c378474a4ac301b886a19925828dfcc135084a0ee12bd67abece4ad | 8f88e9db7cafa5d54370e3e5e0daba36b6870f8c |
| ku9-family.txt | 24053 | 3c47288ef24a7c0291029e4503b4a847a185438446ed6eee29b2e988039f825e | e2da7974009a31af40358c60ba13198bc04ab358 |
| live-family.txt | 24053 | 3c47288ef24a7c0291029e4503b4a847a185438446ed6eee29b2e988039f825e | e2da7974009a31af40358c60ba13198bc04ab358 |
| family.m3u | 45783 | 16ac9bb5d069c8b70f5f425ffa2693fc67d6787cb9520d3471a5d3570fce8843 | 4f98e4c4823466496a6e1bfa0d314873e15c0e27 |
| final-publish-report.md | 10464 | 3e9ef75938fd04219486b4ed7e354c6569160f4943fe6845aa7a178b33a3a1a4 | b27a58fe548b4d47b15b949cafbd0f8c9db9c767 |
| coverage-report.md | 2210 | df6df39f88b7386f36d9e3d3b15918afb33c6a81a00434664c2a7df3f0b2f362 | 08b3b28040586fe83cb2537851d39a167048d1e4 |
| quality-audit-report.md | 4716 | 04797839498896f4d7e85f6c59e8aa25bcb9012c48e709c6ff3f561ecef780e9 | bc56bbf294ef0455af4982ec1dd3e5754f8a4837 |
| publish-guard-report.md | 1500 | 0919c7420db49355de347a6265b5102760ebe9fcddd546e36c87267e922de95f | c44ff556ddae15b9b9240e366ae2258e985fd719 |
| published-recheck-report.md | 29259 | 6cde5e20d06610ac331c5083ed71f3498d47f2bba0fe5f6af288691fac3522ed | 98fda27a1f25f1c3170019e26f3f29512d3120a6 |
| source-report.md | 7951 | 29b4877e0cd518a7e2352554b47d0c43d5479855531f9351a19db64cfe56bb2b | 0d34f2525dcdf24ee01bfec9eeca32c085a13315 |
| check-report.md | 7951 | 29b4877e0cd518a7e2352554b47d0c43d5479855531f9351a19db64cfe56bb2b | 0d34f2525dcdf24ee01bfec9eeca32c085a13315 |
| curated-report.md | 1860 | 991f7ab8eacedb7d672eb3a80adf886f7b04c8324f6f7d169fbfd68d4a4f46c5 | 24cd930f3f7efd43828b2b1eb8b8781c7109aa61 |
| sources_status.csv | 4020 | 5724b1818169222a68c4c9ea04458e0b05003867930934ae2ba6f165e06a0448 | caaf9c0946159e1a285d713f2eca468c667718c3 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
