# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 289765
Unique payload blob bytes: 191155
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 68112

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 22704 | f995e2cecbd0a1c66566989c193b608fb4d1ec06b8e1a8f5293f7557217607c6 | 6cc24580aa05c588005cc37cdf4467434551906f |
| live.txt | 22704 | f995e2cecbd0a1c66566989c193b608fb4d1ec06b8e1a8f5293f7557217607c6 | 6cc24580aa05c588005cc37cdf4467434551906f |
| live-verified.txt | 22704 | f995e2cecbd0a1c66566989c193b608fb4d1ec06b8e1a8f5293f7557217607c6 | 6cc24580aa05c588005cc37cdf4467434551906f |
| ku9-live.txt | 22704 | f995e2cecbd0a1c66566989c193b608fb4d1ec06b8e1a8f5293f7557217607c6 | 6cc24580aa05c588005cc37cdf4467434551906f |
| live.m3u | 43471 | b49ca021a9b6f8c2cf57d7ad3dd96908c2d3d73b07d613ecbc99c5db8a806878 | f4a0f3656b37c3173ec9d6520459aceaa34ca496 |
| ku9-family.txt | 22439 | c4917c8e82268ffecd524ee14f2d01bfd880dbb400d87e08b3bbed479fb65956 | 63bb149bcfed6af1cfbb8d20b12734ddd44e144d |
| live-family.txt | 22439 | c4917c8e82268ffecd524ee14f2d01bfd880dbb400d87e08b3bbed479fb65956 | 63bb149bcfed6af1cfbb8d20b12734ddd44e144d |
| family.m3u | 42958 | e2561f9482ffdeb0a7a673f95b36aa8d73d99488bfd832739de4155900241b06 | 4d5af3f90be71c2888dcb09c3a01faf5aafe3dfb |
| final-publish-report.md | 10740 | 9bdf7ba811cae301d04c09fb07c82353c6da0f21d7808b076c66ed077ff656f7 | f09460c431e3ed75144e57052142422962f468a7 |
| coverage-report.md | 2225 | b1e14528116f20101289f4af92e1051570a0ca5605b0b46cbd09a684147fd4cd | 9cbed4d3ceb68a9a4453073d147c8a95a37e726a |
| quality-audit-report.md | 4718 | 5723272c95016bc9886d36182d8046e05fdcefb6dda99c437dec980940c04f8c | a65ca1a2a00580c06936ac66b5a3c22eee70fc46 |
| publish-guard-report.md | 1611 | c45f8c45d15d36cb8c50e57345cc0ba9900bec2b9cf6dad9f26e8e46f6f6b10d | 93ff71877071ad464b3876c01a1ffb67621d1f7d |
| published-recheck-report.md | 26294 | cfae922011c97b67f94a32754392b1ce909506ba6d5a82a9f13a729b9be3d5dc | 1ad4531a9532be6b2d70bf71c8207fdd0cced8df |
| source-report.md | 8059 | ebce8a9f80c9e1c212616399673319d95d3d3e7cb6a4c5fe1107eca5d696a88a | b35ba88780519e1de80344e83147b2a8696e283c |
| check-report.md | 8059 | ebce8a9f80c9e1c212616399673319d95d3d3e7cb6a4c5fe1107eca5d696a88a | b35ba88780519e1de80344e83147b2a8696e283c |
| curated-report.md | 1804 | 9bd4c4e43bf52af4a9dd97be327f5c40c9089077f07d5b6442cca6c3cca6f021 | 24f8cf9d0a53108697ca00abe21cdd0604f8c23c |
| sources_status.csv | 4132 | b71720e5d630a6e376f764307e4d45677af0d4a0f802c772b87b0feedb187bed | 4ca809765f8c6df5cf9d669c1d7dfa5707ebea30 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
