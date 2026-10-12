# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 166236
Unique payload blob bytes: 117925
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 30480

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 10160 | 37ab80af91a79654fc510c75eb301eed33e8b92b682f19b7ffb59b311b8dd65d | 6c60f4ac26dc8ba68d4600d28d2907a6b71a23a3 |
| live.txt | 10160 | 37ab80af91a79654fc510c75eb301eed33e8b92b682f19b7ffb59b311b8dd65d | 6c60f4ac26dc8ba68d4600d28d2907a6b71a23a3 |
| live-verified.txt | 10160 | 37ab80af91a79654fc510c75eb301eed33e8b92b682f19b7ffb59b311b8dd65d | 6c60f4ac26dc8ba68d4600d28d2907a6b71a23a3 |
| ku9-live.txt | 10160 | 37ab80af91a79654fc510c75eb301eed33e8b92b682f19b7ffb59b311b8dd65d | 6c60f4ac26dc8ba68d4600d28d2907a6b71a23a3 |
| live.m3u | 18860 | 9f7f4f5a37d73588dfd81b08af17c043d6a0e5ff72fa01d50d41c31dc544e922 | 3e92e83c87f2fa3e0a99f8126b7b66c88ad5a912 |
| ku9-family.txt | 9821 | a352fba9afe8561e63a486be8435e260d98dabada1d244c7158f5718c32e22fa | f709718340863bd881cd11d9c5ced74d2f0c7734 |
| live-family.txt | 9821 | a352fba9afe8561e63a486be8435e260d98dabada1d244c7158f5718c32e22fa | f709718340863bd881cd11d9c5ced74d2f0c7734 |
| family.m3u | 18211 | 38a817493f6f6095964210f33a54b356f5cfd3b31472f1d42b1e155f5a30cf69 | 9ca592dc35c271bb98b1ac2411d09c5f920f4501 |
| final-publish-report.md | 10625 | 9442dac60fdcc85ef9f024874e84066ad3399818cca73b85ee64992454996c87 | 666eb27020a14ee1faaca92c0be9cae4adf79fa9 |
| coverage-report.md | 2265 | fa4dfc92a20a6783829c75d5e5687092216cbf12d7a46147c7a6a7084918db23 | ce8d773a2c40bcbfd01c476e952a25a91d0a0ae6 |
| quality-audit-report.md | 4731 | c26cd95dd702f62af8895881d5cb3c23e22367b0bfa22287986e0a00ac0aa1d9 | 7eda4255caba56730e0b94de95f6378bed1e5c47 |
| publish-guard-report.md | 1725 | 516b36dd6ed384e6278b0e5954a46a70e5dafcc4330adec6cde6d19e5b033e02 | 4d8b276fba62e0e256dbe92036474bfd96717b86 |
| published-recheck-report.md | 27703 | 054cb583b086db4ac33184666837b5c89d8a52c6e394347571aa03e3276eb77d | ecbd9dc5562baa30863ec4c73067d63479013744 |
| source-report.md | 8010 | aff9452c0eebdfd09c48eb8fd747fc3c155dd926587931e50106e45612ffc22e | a9c89a84c0a055e7ddd77687c7667ed65479023a |
| check-report.md | 8010 | aff9452c0eebdfd09c48eb8fd747fc3c155dd926587931e50106e45612ffc22e | a9c89a84c0a055e7ddd77687c7667ed65479023a |
| curated-report.md | 1736 | c01d6feb01a6765728a2f27cebb7fdb9fc0a07b48febfff70bac922c64ea8c78 | 1ad6c9017304cc0ed67b02a6a191079a493037d3 |
| sources_status.csv | 4078 | 97870b18a218c598ceacca84072c5aa15b5164f2d565cb0503fb65a078870e27 | 939e127d44806b21aae9b5321652b5bc30d36fed |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
