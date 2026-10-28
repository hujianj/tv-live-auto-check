# Publish size and alias safety report

Status: ok
Measurement scope: publication payload files only; summary, this report, and the manifest are checked separately
Working-tree payload bytes: 264858
Unique payload blob bytes: 176766
Max unique payload blob bytes: 2500000
TXT alias same hash: True
Family TXT alias same hash: True
Duplicate TXT working-tree bytes: 60333

## Public files

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| live-curated.txt | 20111 | f6794e78791addf0a7b3e4553dfb2524f3081ac4fe653bc0ab857e51b6d59350 | 826d3cfb06e109100349b69a0465c3238fac5a09 |
| live.txt | 20111 | f6794e78791addf0a7b3e4553dfb2524f3081ac4fe653bc0ab857e51b6d59350 | 826d3cfb06e109100349b69a0465c3238fac5a09 |
| live-verified.txt | 20111 | f6794e78791addf0a7b3e4553dfb2524f3081ac4fe653bc0ab857e51b6d59350 | 826d3cfb06e109100349b69a0465c3238fac5a09 |
| ku9-live.txt | 20111 | f6794e78791addf0a7b3e4553dfb2524f3081ac4fe653bc0ab857e51b6d59350 | 826d3cfb06e109100349b69a0465c3238fac5a09 |
| live.m3u | 37942 | 15fe72e6fd0f87a25b3f50ff71d65dbc636c49e55a3beb1f8022222b4cb1aae7 | 136abea1fbbd399e689881fca292d7e963448b87 |
| ku9-family.txt | 19690 | 9399590eb111d2819647f28ceabd8f97e60f9fa8c22a11f069adb9e12bde4c82 | 5e546617d5dbf5116f6d2d03ee502c0bfad422c1 |
| live-family.txt | 19690 | 9399590eb111d2819647f28ceabd8f97e60f9fa8c22a11f069adb9e12bde4c82 | 5e546617d5dbf5116f6d2d03ee502c0bfad422c1 |
| family.m3u | 37149 | 3b8ae6fac75ab1aaa03cb671bf8b5b0694eaabeaa8b004ac7812622688ee1dbf | c3db636f048ae7df004eca8fc039595af63ccf10 |
| final-publish-report.md | 10216 | 1a9471dd78c709d4ab8190b8d30501860f51add552083e760c2986a463ef8f34 | 208ecc8cfb3dbb7596fe484d7dd7968df36507f5 |
| coverage-report.md | 2200 | 5e6e4fbd878df7e1b17b4737d3da99a30148c7487ad46e55b623e38cb56b4676 | cf4b55026a42906c8e113c80be5eb3e63e727f19 |
| quality-audit-report.md | 4690 | 0ad9908a4cfeb59ed392ceb65d612174e177ce70db78fdf5a92d1df2ded544d1 | ad57ee54c131daf7c3df6c460751a2cc668ba7ba |
| publish-guard-report.md | 1501 | e7c2f9ca1573dcba3e09ced12ef5ccd324bcbab3a565fefafe0dab6c235e6c52 | bf73392e654e11e35caa2455073b8859bfc77279 |
| published-recheck-report.md | 29185 | f0496a615f9dfef25bfa10a0513e2e0f73b98fd7cdffd33e660032c34c21125d | fb07c6b78c78b21f3618427c5f4e6286a3f1153e |
| source-report.md | 8069 | f97d525fc4e47a04310620f844a79476ffa97eaf63d953e86329e5fca94c2c16 | bdce17ac5d86a445a68707830c0e78ecee8556be |
| check-report.md | 8069 | f97d525fc4e47a04310620f844a79476ffa97eaf63d953e86329e5fca94c2c16 | bdce17ac5d86a445a68707830c0e78ecee8556be |
| curated-report.md | 1895 | 2f71861253c2d5ba6b672dec27860439feb5bdb61f58a5c535f45ac0e968bfbd | f6915d08234e0466b13645cdca6fcabf0695c8b3 |
| sources_status.csv | 4118 | a5b33ae975b71adf748aee9e699235b377e5ccb64758cf654a347c463ea3441c | 8907eec34f77c72429770682b29247fcc6a793c7 |

## Warnings

- TXT aliases occupy duplicate working-tree bytes for compatibility, but Git stores their identical content as one blob.
