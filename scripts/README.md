# Validation and fixture integrity

Use Python 3.10+; standard library only. Run from the repository root:

```powershell
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator returns exit code 1 on errors. It checks required and readable files, simple Markdown links and
table shapes, CSV/JSON structure, formula-leading CSV cells, control/test/evidence IDs, complete selected criterion
coverage, per-edge mapping agreement, allowed reference ranges, current design-only status, risk arithmetic,
synthetic markers and manifest digests. Common AWS/GitHub key and private-key patterns are checked heuristically.
Header-only blank templates and fields explicitly marked for completion in blank forms are intentional.

Ten tests include deliberate mutations for missing files, broken links, mismatched mapping edges, wrong risk scores,
altered evidence, removed synthetic markers, a fake key pattern and malformed Markdown tables, plus clean-repository
and risk-boundary checks. Tests work in temporary copies and do not change the original toolkit.

After an intentional review of changes to fabricated examples only:

```powershell
python scripts/update_manifest.py
python scripts/validate.py
git diff -- examples evidence/manifest.csv
```

Do not regenerate a digest to hide unexpected changes. A separately trusted baseline is required for real evidence.
The manifest tool has an end-to-end self-check through the validator's coverage/digest checks and clean fixture test.
Repository text uses LF line endings through .gitattributes so fixture digests survive Windows/Linux checkouts.

Limits: internal consistency does not establish framework reference meaning or complete normative coverage.
External URLs, Mermaid rendering, actual security integrations, live operating effectiveness and exhaustive secret
or personal-data detection are outside this validator. Use qualified review and a mature scanner for operational data.

Desktop verification used the bundled Python interpreter because `python` resolved to an unavailable Windows Store
alias. The first test run was blocked by the sandbox temporary-directory permissions. Rerunning with TEMP and TMP
set to the writable workspace work/ directory passed all tests; no application-code repair was needed.
