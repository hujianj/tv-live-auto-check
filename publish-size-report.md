# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 265316
Unique payload blob bytes: 177040
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 60444

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20148 | 11513bab27a195471409ee91b4811bfecbdac0a67ec0f28a8f8210b6a07c9cde | f7e7ef4d1f35816f7e9fec9a7d8117d678842209 |
| live.txt | 20148 | 11513bab27a195471409ee91b4811bfecbdac0a67ec0f28a8f8210b6a07c9cde | f7e7ef4d1f35816f7e9fec9a7d8117d678842209 |
| live-verified.txt | 20148 | 11513bab27a195471409ee91b4811bfecbdac0a67ec0f28a8f8210b6a07c9cde | f7e7ef4d1f35816f7e9fec9a7d8117d678842209 |
| ku9-live.txt | 20148 | 11513bab27a195471409ee91b4811bfecbdac0a67ec0f28a8f8210b6a07c9cde | f7e7ef4d1f35816f7e9fec9a7d8117d678842209 |
| live.m3u | 37923 | 1eb348b22c052e5ccfbb957adc576703951cefe9cd77851ec66909d84cfbfcbd | f3e724fc3c3cf2f28a8fbca5206fd6a973b2ec32 |
| ku9-family.txt | 19714 | 5a2b71996babf970f52e7c200efe1b4b74e398ddcd9e430ca70d076fb8437b96 | 2b4ad03f6c441fff9c09d41129e3259763e2ab95 |
| live-family.txt | 19714 | 5a2b71996babf970f52e7c200efe1b4b74e398ddcd9e430ca70d076fb8437b96 | 2b4ad03f6c441fff9c09d41129e3259763e2ab95 |
| family.m3u | 37117 | bf8a70b8ba96619b02ccbc0500843a03ae30b22dd3f1f1b2f145d09f2f86d3ea | b7fa291496aa0f9beee270e2778b189555135659 |
| final-publish-report.md | 10277 | d2e21ccddb8a4ae7a0d599266c21c89a0e65e5fc76744a422eb607ff22068be9 | ea7e6968060754dc1455ab748fe3f795f5dbceda |
| coverage-report.md | 2205 | b31cb8f482216df0c1a6c50ea77f96e10d386592e06153bd0099d24fc2a86d22 | 24a2b1ca88c72fa50968d168de63b741d4cbad9e |
| quality-audit-report.md | 4691 | fc0677bb43a9a967c5b7bd650c0a3ca1daecd2c0bf2cbc18dd9c1b1fb6ebd013 | b7141469c00f0f9f38ac22626c003e08b0f7ab8c |
| publish-guard-report.md | 1575 | e59a877fa6ae31f90278b17cd4d7e064af7b1ef1ff1b6d2e834af5fe7c65f2f0 | 439601e75c4654f679c1495dca70a7a5f8a5e2f5 |
| published-recheck-report.md | 29200 | fd3cdabdb10640e2e0a45a9c98ced8f477caff354ec35010e92915ad2d6b30c1 | 24e2c0223407973cf72133adf6ce9880cc160c80 |
| source-report.md | 8118 | 05ba5c12863e14901596c4fd0ed57647d1958972e4004f264ebf33913d860862 | 975d8934c436f2703c387970e647b724b568ec9d |
| check-report.md | 8118 | 05ba5c12863e14901596c4fd0ed57647d1958972e4004f264ebf33913d860862 | 975d8934c436f2703c387970e647b724b568ec9d |
| curated-report.md | 1895 | f8163539387f74b4022c4f313c3bb37e1810da595428df9ec4ab087b603ec2e7 | 89e5da36fc61c5d1cd67624843b585c0ee40c2fb |
| sources_status.csv | 4177 | ec32737ad08793331cd767acf2618da63660da13b3de42a518b9cae98f61088b | 70fb444be48c0e02cc46f8fdc393867dff05209f |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
