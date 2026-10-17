# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 321168
Unique payload blob bytes: 210140
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 77649

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 25883 | a92f083f11d08f2a672149b4b1fb32ae84218c76cdc38eb1b8961f6747dad8f9 | b3446389fb9b3375ad8f9c8da6de8dea4c616b28 |
| live.txt | 25883 | a92f083f11d08f2a672149b4b1fb32ae84218c76cdc38eb1b8961f6747dad8f9 | b3446389fb9b3375ad8f9c8da6de8dea4c616b28 |
| live-verified.txt | 25883 | a92f083f11d08f2a672149b4b1fb32ae84218c76cdc38eb1b8961f6747dad8f9 | b3446389fb9b3375ad8f9c8da6de8dea4c616b28 |
| ku9-live.txt | 25883 | a92f083f11d08f2a672149b4b1fb32ae84218c76cdc38eb1b8961f6747dad8f9 | b3446389fb9b3375ad8f9c8da6de8dea4c616b28 |
| live.m3u | 48978 | 4d8ae44407b97c9ebb24b6df4680772d6aa06518f785e28f6ec510845469d990 | 094e80d454e14ea7a84f912cf94428316daddcb1 |
| ku9-family.txt | 25423 | 08f254c733419f17736a228b1ddbb4723f9bbe1ea0a428c54ddb2453f9cf57c5 | 80b31eb45ce051f754f632b09693986a1308dfe1 |
| live-family.txt | 25423 | 08f254c733419f17736a228b1ddbb4723f9bbe1ea0a428c54ddb2453f9cf57c5 | 80b31eb45ce051f754f632b09693986a1308dfe1 |
| family.m3u | 48146 | 9bdf1b87e22874a8bcd9a069faae2c0cedc2455bb73f5ef8e3a71172afec2a1d | 785024054f4169a661cff8ed6a7722a5899b092e |
| final-publish-report.md | 10827 | 6bb71497e7adc430a60db07de91eb1156b287dc688fce1f9ef7ca09b18bf71e5 | 594553ffba83c943c470efa3f16a2fe85e740589 |
| coverage-report.md | 2175 | 5e0ffa5627c812937f5e43b31925c7b4c605a36efd9ac61c1eb3c5dd8a9c533a | cf488e8f435ab4016055cf3667f4c5dd71a884b9 |
| quality-audit-report.md | 4682 | 18119863e48d0ee0dd86f24486d4256a85ff67597fa1c5f4ad6965c2c7c202ec | c4c6c93f5684982449fdc4430a602b85b5071739 |
| publish-guard-report.md | 1565 | ad2181d780d35e903bc87d98ce3abb6448045c42e632c4bbc05027958e05a93e | 92fa34ec112ef399c04d17e248ed7965e650b621 |
| published-recheck-report.md | 28563 | 3d3d657f0c80bea9393def9b96bf5706c3b01a9e885f1c03a168d316233aa75d | b886a6a86282a2e53abbd6c73a47ad72254c9730 |
| source-report.md | 7956 | de72c949deccca98093774a83bdffa89cd496809912123a906f181a86f1fb94b | 55f001849ff19b4eaef2a3c72db5b9dc46fe2dd5 |
| check-report.md | 7956 | de72c949deccca98093774a83bdffa89cd496809912123a906f181a86f1fb94b | 55f001849ff19b4eaef2a3c72db5b9dc46fe2dd5 |
| curated-report.md | 1804 | 5dc4e6851e0ef1a308adf2b036f13e7a8dffd40e217791d3e6bdf12957fddafc | 36c6ffe17c32d9969aa51eaf7234688e5ae1969b |
| sources_status.csv | 4138 | 1b7e50a2e5bbe09dca0292625dfe3dd6cb293f80f0904af4dee005ed0114b7cf | aee59ff8f60107e3da4fa5e0e5c114a429cec4e8 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
