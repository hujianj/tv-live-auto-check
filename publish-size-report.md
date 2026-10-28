# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 245192
Unique payload blob bytes: 164284
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 54786

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 18262 | 2c331eb0bc31e82d7477e9db0f697fada68324e204b9babdaa75cc416998a005 | 03d3e10245701a2397e56f607b916bb1706cab31 |
| live.txt | 18262 | 2c331eb0bc31e82d7477e9db0f697fada68324e204b9babdaa75cc416998a005 | 03d3e10245701a2397e56f607b916bb1706cab31 |
| live-verified.txt | 18262 | 2c331eb0bc31e82d7477e9db0f697fada68324e204b9babdaa75cc416998a005 | 03d3e10245701a2397e56f607b916bb1706cab31 |
| ku9-live.txt | 18262 | 2c331eb0bc31e82d7477e9db0f697fada68324e204b9babdaa75cc416998a005 | 03d3e10245701a2397e56f607b916bb1706cab31 |
| live.m3u | 34185 | 47a0e462685d8e1df82fb879392bdc7e27efae6ee96e756d7abebc5af9c56976 | 94410502e159ccd60ddbd79065349555826650f8 |
| ku9-family.txt | 17914 | 61a6c3d9e0c4d219dfa7b773ca14edbd37abf136040c0412dd4b1e09a9cf6f8b | 5e88979f27e4f85674b8c4317a55641d33e98d42 |
| live-family.txt | 17914 | 61a6c3d9e0c4d219dfa7b773ca14edbd37abf136040c0412dd4b1e09a9cf6f8b | 5e88979f27e4f85674b8c4317a55641d33e98d42 |
| family.m3u | 33527 | e499398bb02ebfc2079f3af9b681968f9159f0cfae37b7d5f15bac7d76f52f63 | d3b5eaffaec2b71aec6f1563538ca883aacb1b08 |
| final-publish-report.md | 10775 | 5a38a806c3cc70f625a1064175db429bb58715a6571c6b3969b8129888b450ee | 0f6de5f4d8615b61654b76d59da77a3d283a84bd |
| coverage-report.md | 2235 | bca6a3c905d7e3f8bbeba2dab0c5c7e0eb25ce48bdc73f2d0ebf39c4bed79e8c | c3b262a1fdc886c1f874562ea61cac8c49b8c278 |
| quality-audit-report.md | 4780 | 40eff979586ed9801822575414e093f35015a47b42f13f12f3d68ec4d68fe6f8 | 50d0ca6389490602fed3c625bb256a0759efc19e |
| publish-guard-report.md | 1571 | b403fb295305bccb47624334a541ad8cc78a464097ba6681873c69a6f4528235 | 48f5101ccdbfcb2bd49984ad3d7f3c1936b66e61 |
| published-recheck-report.md | 26728 | b1be66a9f5df8d1c12865799270bcb4b1fb5defddc485312c47468718b300641 | 1837ef79d6226529a98792d1c78846651d2d4d6a |
| source-report.md | 8208 | 259587ae9581a4444f25086961bb015da157ef574a21b2293326349dba8b11a1 | 9f1938c6ee009da4f5c32a39e3edc40f7b7db19d |
| check-report.md | 8208 | 259587ae9581a4444f25086961bb015da157ef574a21b2293326349dba8b11a1 | 9f1938c6ee009da4f5c32a39e3edc40f7b7db19d |
| curated-report.md | 1806 | 24648edc6fccb03497c09ee8336c35015409e298429e44925d3b431dbc95fa1d | cfe83288f1e45ed64c0e1cd73e0bceb3a8a1336f |
| sources_status.csv | 4293 | d6363ab5bd074fe73a7c12810c727ec5eba5e0894f6275e0f79aef8b808ac303 | 09fec4e79a4cdf636e359de235066f22f687e96d |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
