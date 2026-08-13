# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 2117118
Unique payload blob bytes: 1530151
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 493290

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 164430 | 6a65a4d7732decd8757fe14d81c7682b47e035f0a0bc60630df8adab0c31b082 | 1d9e556ac0a98b8979b985144c209c0b9cfcc44f |
| live.txt | 164430 | 6a65a4d7732decd8757fe14d81c7682b47e035f0a0bc60630df8adab0c31b082 | 1d9e556ac0a98b8979b985144c209c0b9cfcc44f |
| live-verified.txt | 164430 | 6a65a4d7732decd8757fe14d81c7682b47e035f0a0bc60630df8adab0c31b082 | 1d9e556ac0a98b8979b985144c209c0b9cfcc44f |
| ku9-live.txt | 164430 | 6a65a4d7732decd8757fe14d81c7682b47e035f0a0bc60630df8adab0c31b082 | 1d9e556ac0a98b8979b985144c209c0b9cfcc44f |
| live.m3u | 296210 | a2de636ab8ba4bfe13c749d4b7f57acf2a2039bff11df9965b3ff693ba7e9119 | 8704407d57604b4680c3677a451503b0c6f0861e |
| ku9-family.txt | 87114 | 3509088524c1ad08ffe0fca6d4cf764c4b5d7fc37b9a9c85e6ef0efe875826ad | 94b0cbf628ce76eca647607fce70606c6ede45e8 |
| live-family.txt | 87114 | 3509088524c1ad08ffe0fca6d4cf764c4b5d7fc37b9a9c85e6ef0efe875826ad | 94b0cbf628ce76eca647607fce70606c6ede45e8 |
| family.m3u | 155805 | e5aba4688a652ce8c665b0401e2e0a0ddab9e49f61f02b4f17f236ad8eba44fd | cd394ec9fc14e30f565edbacd885bad1157fb052 |
| stability-history.tsv | 759490 | b085acb1b0c675ae331be160053b39e3d2dc9a7dae6e9c266e42fb8bf68078d2 | 7270ecda903211ab6027b3d1b5ae9e5f1fc88fff |
| final-publish-report.md | 11584 | 07dc93510ec31f3b7af882269768dfd137fa44fbffde43777c001dff67fb3411 | 5083e72685b7be0cd1900dda7096cb8301afa9e6 |
| stability-report.md | 12037 | bd29fc717e9981fa1e5b30e9f159973b6db716265d65ca293ccd90a6f8462ff0 | 2a38db3755c231e885150b1c6fc8d5af279e488d |
| coverage-report.md | 1291 | 2a34d201ff7cbb7ee57f36dd5a5312ccbd7fa6365400cd7d3db56cf47dfe1666 | 66bf42f3c71c5de341156773d1654dfb628e0040 |
| quality-audit-report.md | 2163 | 2f804318742ba5cac7e08677a130ca95e804ad7c4ee3a827c602950de022aa71 | 8acc71822cb619579e6a2b877df55be26b553221 |
| publish-guard-report.md | 1143 | 44c63f4d4bd31223c9fa5a254fea9eaba748cec119b48c38fd49dfe0085bfb95 | 2dc7c8d9451e2861d7bb2d7fdaa88ec0c579f774 |
| published-recheck-report.md | 25837 | 60ce18ba7825dff6f1522e09fee186f17134094c77df40780137ea2d010ab383 | 56b376f67eac410f1938882ca554a4cacfa57bb0 |
| source-report.md | 6563 | d7e14de5676f4e8727a7a124688aa35f9dbe4d049e842844650a20b521996e29 | 88625d2bd2bd3fa022e9175bcd593777bb07f6bf |
| check-report.md | 6563 | d7e14de5676f4e8727a7a124688aa35f9dbe4d049e842844650a20b521996e29 | 88625d2bd2bd3fa022e9175bcd593777bb07f6bf |
| curated-report.md | 3345 | 5d8e23febda753333216e3152733a06fc294893cff7fa966d212c569ff527c43 | ba99874003d72f2e019cb385b08f0033193e01e9 |
| sources_status.csv | 3139 | 1645fd31ba06c847328a40b661dfaeff5b4cd8cb9127c09d52956606705695a8 | 3e02c89b0dc20020a6b71f6ad94650c8e4d3a2ed |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
