# Delivery and validation report

Prepared 2026-10-24. This is a design and synthetic desk-review portfolio, not a deployed security environment.

## Delivered

The original workspace had no project or Git repository. A new toolkit was created without replacing unrelated files.
The project contains 14 illustrative controls covering CC6.1–CC6.8, CC7.1–CC7.5 and CC8.1; 35 mapping edges
(16 Direct, 19 Partial) across 33 distinct ISO/IEC 27001:2022 Annex A references; 14 evidence requests and test
procedures; blank access-review and risk forms; three fictional access-review records; six scored risks; an incident
runbook and case; normal and emergency change examples; synthetic Wazuh, AD, Sophos and AWS records;
two detailed Mermaid diagrams; supporting methodology, glossary and source register; and interview preparation.

All control implementation statuses are designed only. The fictional case desk reviews show **9 Pass, 3 Fail and
2 Not tested**. Those are example outcomes, not local software test failures and not live control conclusions.
Deliberate failures are legacy privileged access, overdue access removal and public SSH exposure. Missing tests
are provider physical-assurance evidence and monitoring feed-outage detection. Open risks are preserved.

## Validation results

| Check | Result and limit |
| --- | --- |
| Required artifacts and UTF-8 readability | Passed; all required files present |
| CSV/JSON parsing and table shape | Passed; blank access/risk CSV templates are intentionally header-only |
| Relative Markdown links | Passed; no missing local targets found |
| Control/test/evidence IDs | Passed; each selected criterion has an illustrative control and test |
| Mapping relationships | Passed internal CSV/index/edge consistency; 35 edges classified with rationale and separate treatment |
| Framework accuracy | Publisher edition metadata reviewed; full licensed-text comparison and practitioner crosswalk review remain pending |
| Risk scoring | Passed inherent and residual rating, product and band checks |
| Synthetic markers | Passed in example prose, CSV and JSON; all records were authored as fictional material |
| Evidence manifest | Passed digests and file coverage for all 25 examples/ files |
| Common secret patterns | No matching AWS/GitHub/private-key or assigned-secret patterns found; this is not exhaustive scanning |
| Regression suite | All 10 tests passed after sandbox TEMP/TMP configuration; deliberate error mutations detected |
| Git whitespace check | git diff --cached --check passed before final commit |
| Cross-platform bytes | LF policy added so Git line-ending conversion does not invalidate evidence digests |
| Live systems and audit effectiveness | Not assessed; no tenant, domain, endpoint or cloud account accessed |
| Mermaid rendering, every external URL and remote CI | Not independently validated; source access limits are recorded |

The first test run encountered desktop sandbox temporary-directory permissions. Setting TEMP and TMP to the
writable workspace work/ directory resolved the environment restriction; the validator then passed and all 10
regression tests passed. Windows' python alias was unavailable, so checks used the bundled Python 3.12.14 runtime.

## Git and publication

Initial local commit: **6f9cfed** on **main**. The source ZIP excludes Git metadata.
Public repository: [stemAGH/soc2-iso27001-control-toolkit](https://github.com/stemAGH/soc2-iso27001-control-toolkit).
The owner confirmed the stemAGH account and public visibility. Repository creation used the signed-in browser;
uploads use the GitHub connector as stemAGH because the local CLI uses a different account.
The earlier CLI authentication error was caused by sandbox network restrictions, not an invalid token.
Check the repository main branch for the latest published commit and Actions results.
See [publication instructions](publishing.md) for account and history handling.

The README and interview notes were revised around the access-removal finding, with less repetition and
more explanation of the reasoning. Synthetic labels and framework-review limits are retained.

Actions before operational reliance: authorized full-text and practitioner review; actual scope/owner approval;
lawful retention and contact configuration; live implementation and independently reviewed period evidence.

## Final structure and complete created-file inventory

All files below were newly created; no existing project files were overwritten. Supporting content explains
scope, evidence ownership, collection, testing, remediation and limitations. The interview guide includes a concise
project explanation, five technically grounded questions with answers and a five-minute demonstration sequence.

60 source files:

```text
.gitattributes
.github/workflows/validate.yml
.gitignore
LICENSE
README.md
control-matrix/README.md
control-matrix/control-matrix.csv
control-matrix/iso-reference-catalog.csv
control-matrix/mapping-relationships.csv
diagrams/architecture.md
diagrams/control-evidence-workflow.md
docs/delivery-report.md
docs/glossary.md
docs/incident-response-runbook.md
docs/interview-guide.md
docs/mapping-methodology.md
docs/operating-model.md
docs/publishing.md
docs/risk-methodology.md
docs/sources.md
evidence/README.md
evidence/chain-of-custody.csv
evidence/manifest.csv
examples/README.md
examples/access-review.csv
examples/ad-events.jsonl
examples/aws-findings.json
examples/change-record.json
examples/cloudtrail-events.json
examples/control-evidence/ev-001.md
examples/control-evidence/ev-002.md
examples/control-evidence/ev-003.md
examples/control-evidence/ev-004.md
examples/control-evidence/ev-005.md
examples/control-evidence/ev-006.md
examples/control-evidence/ev-007.md
examples/control-evidence/ev-008.md
examples/control-evidence/ev-009.md
examples/control-evidence/ev-010.md
examples/control-evidence/ev-011.md
examples/control-evidence/ev-012.md
examples/control-evidence/ev-013.md
examples/control-evidence/ev-014.md
examples/control-test-results.csv
examples/incident-record.md
examples/risk-register.csv
examples/sophos-events.jsonl
examples/wazuh-alerts.jsonl
scripts/README.md
scripts/update_manifest.py
scripts/validate.py
templates/README.md
templates/access-review.csv
templates/audit-evidence-checklist.csv
templates/change-request.md
templates/control-testing-procedures.csv
templates/incident-record.md
templates/risk-register.csv
templates/test-execution-record.md
tests/test_validate.py
```

Start with [README](../README.md), then [interview guide](interview-guide.md) and [publication guide](publishing.md).
