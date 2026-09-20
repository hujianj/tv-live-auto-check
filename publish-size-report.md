# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 166978
Unique payload blob bytes: 118795
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 30495

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 10165 | c235bc084d16a3a6ed4c24d150041d923dbda16b3f1e87d2365c9239bedd01cc | 3d0181e1135aae07bf5d84f7773f8c864d49d5a8 |
| live.txt | 10165 | c235bc084d16a3a6ed4c24d150041d923dbda16b3f1e87d2365c9239bedd01cc | 3d0181e1135aae07bf5d84f7773f8c864d49d5a8 |
| live-verified.txt | 10165 | c235bc084d16a3a6ed4c24d150041d923dbda16b3f1e87d2365c9239bedd01cc | 3d0181e1135aae07bf5d84f7773f8c864d49d5a8 |
| ku9-live.txt | 10165 | c235bc084d16a3a6ed4c24d150041d923dbda16b3f1e87d2365c9239bedd01cc | 3d0181e1135aae07bf5d84f7773f8c864d49d5a8 |
| live.m3u | 18711 | f7a50e5b40e91ade98dccf9c7e2228455b6554a14972bb030b612dfd6abb3e91 | dd725ca0290dabbea805f290d22551ad41637e91 |
| ku9-family.txt | 9749 | 5d924c2a586d84249b66daf9ae943fec06978be27a10074eb5bc88c3c4459a13 | 387da514001bd1ae406f8179a4eff155226a1113 |
| live-family.txt | 9749 | 5d924c2a586d84249b66daf9ae943fec06978be27a10074eb5bc88c3c4459a13 | 387da514001bd1ae406f8179a4eff155226a1113 |
| family.m3u | 17923 | b20e61ec0fb7e7066419f76f62fde4526a76690f7125d50f147b21df840bd8e0 | 93ab246073b510d51f7caa19fc400b28da809f28 |
| final-publish-report.md | 10728 | 05b78ab46538a24288dbf6618b1c244736da8bd4865d87b36a0df7b7e383625c | 877b232da4145266cb7e47dc09091a434136a6f6 |
| coverage-report.md | 2265 | 5cf32a774a9680ba1edf356795c3bd6ff1f04058107948d2878caaba4783334f | 9cdfddd6fa8f7d3d1b935ff0a170daef7ce6156f |
| quality-audit-report.md | 4730 | 5e1895f2777f5bfb4e5c70ea26e2751b727c20d0c956eb6e568b778d4646fff0 | 3f4077073abccd1a38f807c9a1f29e949cfe0589 |
| publish-guard-report.md | 1779 | c2b828af33f4a9b7765aee22e55ecc46e99375180d811d14e3fde2c2de24c9c6 | 5398a20f077455e4384f46345e12ed25333c2feb |
| published-recheck-report.md | 29058 | aac1787fb1c1d310fc9b08eac54f09c2ef63b4d930bc7eb53ad0600ce152f2f6 | 6f8899ec42d0a5672d293a777ed18d37f4253133 |
| source-report.md | 7939 | b2dcb98f0b1535dd7a91d6038868dc109a2b51c010b6b0357b6e3474e0aa588d | cf2b740b34c0fdbbed7a1ba21494b71fde510efc |
| check-report.md | 7939 | b2dcb98f0b1535dd7a91d6038868dc109a2b51c010b6b0357b6e3474e0aa588d | cf2b740b34c0fdbbed7a1ba21494b71fde510efc |
| curated-report.md | 1736 | 63be6b9bfd58a06056fd0537637594af05fe04e8ce34aef6ba4d5555a54e30a4 | 9675145791ce18071faf06ceb2d7664bc8c13cef |
| sources_status.csv | 4012 | b7f903472b05494555a6917b93f46e23eeb316210883a1e1f0e04ccfa03ddfa1 | 90212f043b48502b164416e335b0e0a6549b8f1b |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
