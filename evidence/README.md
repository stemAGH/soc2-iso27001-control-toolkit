# Evidence index and integrity

This directory stores the public synthetic-pack index, not production evidence.
[Checklist](../templates/audit-evidence-checklist.csv) connects each CTL to EV and sample narrative.
[Manifest](manifest.csv) records SHA-256 digests of every examples/ file for local tamper detection.
[Custody example](chain-of-custody.csv) demonstrates handling metadata; all entries are fictional.

The manifest was calculated during assembly; it is not a signed, independently trusted provenance record.
The validation script verifies digests but cannot prove the author did not change both file and manifest.
If deliberately adapting fixtures, regenerate the manifest using the documented command in scripts/README.md
and review the entire diff. Never use this command to conceal an evidence alteration.

Do not store live evidence here. .gitignore excludes several common local evidence names but cannot prevent
an operator from committing sensitive files elsewhere. Run sensitivity review before every publication.
