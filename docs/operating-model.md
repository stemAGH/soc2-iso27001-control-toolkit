# Operating model, assumptions and evidence governance

## Scope and responsibilities

This is a design and synthetic desk-review portfolio. No Wazuh server, AD domain, Sophos tenant or AWS resource was accessed.
Control owner roles in the matrix are fictional assignments; a real organization must name accountable people and alternates.
GRC coordinates evidence and quality checks; system owners operate controls; an independent reviewer challenges conclusions;
management accepts risk within delegated authority; external assessors determine their own procedures and sufficiency.

AWS protects provider infrastructure under shared responsibility. The customer still configures IAM, workload exposure,
logging and data protection, and must review provider assurance, complementary customer controls and scope.
Do not copy confidential supplier assurance reports into a public portfolio.

## Local policy assumptions, not framework mandates

| Topic | Fictional operating target |
| --- | --- |
| Review period | 2026-10-01 through 2026-10-24 UTC; a short demonstration, not a SOC 2 Type 2 period |
| Access | Prior grant approval; revoke by effective termination; quarterly complete review and monthly privileged review |
| Review remediation | Five business days after decision, using Monday–Friday and no holidays for this fictional exercise |
| Monitoring | Benign lab anomaly alert within 15 minutes; missed-feed alert within 30 minutes |
| Recovery | Illustrative service RTO 4 hours and RPO 24 hours; business owners must set actual values |
| Emergency change | Record emergency authority and independent review next business day |
| Retention | 12 months after evidence period end; lawful schedule, contracts, privacy and legal hold take precedence |

## Evidence lifecycle

Request evidence by EV ID and CTL ID. Collector records source, filter/query, accounts/Regions, population count,
period, event time, export time, timezone and any collection error. Preserve originals in a restricted evidence store,
create redacted reviewer copies and record hashes at collection in a separately controlled ledger.
Verify completeness against independent inventories before selecting samples. Review scope, relevance, provenance,
accuracy and period coverage; a screenshot alone rarely establishes a population or continuous operation.
Record missing, rejected, accepted or superseded status and reviewer identity. A hash detects modification relative
to its trusted baseline; it does not establish authenticity. Repository manifests are not independent custody attestations.

Restrict production evidence to named roles; encrypt transfer and storage; audit access; separate collectors and reviewers.
Follow approved deletion and legal-hold procedures. This repository is public-safe synthetic material only.
Use an external restricted store for live evidence; .gitignore is a convenience, never an access-control boundary.
Run a mature secret scanner and human sensitivity review before publishing any later real-world adaptation.

## Test interpretation

Design inspection asks whether the control could achieve its objective. Operating-effectiveness testing asks whether
it actually worked throughout a defined period. The supplied desk-review outcomes assess only fictional cases.
They do not establish either live implementation or operating effectiveness.

For a live exercise, reconcile the complete population, test all events if 25 or fewer; otherwise select 25 across the
period plus all high-risk and emergency events, and document rationale. This is an instructional starting point,
not an audit sampling standard or statistically representative sample. Agree appropriate extent with the assessor;
expand for exceptions and missing evidence. Preventive controls need authorized negative tests; repeated controls need
period coverage. Do not infer a pass from one successful event or no observed alerts.
