# Using the templates

CSV files are UTF-8 with headers. Open in a CSV-aware editor or spreadsheet; semicolons separate multiple values
inside a quoted CSV field. Preserve IDs as text. Treat any future imported cells beginning with =, +, - or @ as
untrusted spreadsheet formulas; the included fixtures do not contain formula cells.

| Template | Start here |
| --- | --- |
| [Control matrix](../control-matrix/control-matrix.csv) | Copy and adapt designed controls; assign real owners and record scope before changing status |
| [Evidence checklist](audit-evidence-checklist.csv) | One populated request per control; sample references are synthetic, live review is uncollected |
| [Access review](access-review.csv) | Header-only reusable form; examples are in examples/access-review.csv |
| [Risk register](risk-register.csv) | Header-only reusable form; use docs/risk-methodology.md to score consistently |
| [Control testing procedures](control-testing-procedures.csv) | Fourteen procedures with population, sampling, expected results and remediation |
| [Test execution record](test-execution-record.md) | Record live scope, samples, exceptions and reviewer conclusion separately |
| [Incident record](incident-record.md) | Use with the incident runbook; keep operational contacts in a restricted directory |
| [Change request](change-request.md) | Standard and emergency change approvals, tests and rollback |

Copy blank forms into a restricted work area. Replace demonstration policy assumptions through documented approval;
never silently overwrite supplied synthetic examples with real evidence. Read [operating model](../docs/operating-model.md).
