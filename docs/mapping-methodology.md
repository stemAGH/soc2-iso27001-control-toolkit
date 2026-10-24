# Mapping methodology and coverage boundary

Version 1.0; prepared 2026-10-24. Fictional scope: a small hybrid organization with AD-managed Windows endpoints,
Sophos endpoint protection, a Wazuh monitoring tier and an AWS workload. No live environment is represented.

## Method

1. Define the service, assets, people, locations, accounts, Regions, period and business commitments. Record exclusions and dependencies.
2. Translate a selected SOC 2 criterion into an organization-specific control objective and implementation, without reproducing normative wording.
3. Identify related ISO/IEC 27001:2022 Annex A references; evaluate each relationship individually in mapping-relationships.csv.
4. Mark **Direct** when the control objective materially aligns; mark **Partial** for a supporting or narrower relationship. Neither means equivalence or satisfied requirements. These are author judgments, not an AICPA or ISO approved crosswalk.
5. Describe implementation expectations, owner, expected evidence, testing and separate treatment. Reject speculative links that have no clear causal relationship to the objective.
6. Collect once where scope and period align; evaluate evidence separately against each framework's requirements. Keep independent gaps open.
7. Obtain licensed-text review, practitioner challenge and management approval before operational reliance. Record version and change rationale when sources or scope change.

## Coverage

There is one illustrative control for each of CC6.1–CC6.8, CC7.1–CC7.5 and CC8.1. Covering identifiers does not fully address every criterion or point of focus. More controls may be needed for actual service commitments and risks.
CC1–CC5, CC9, the system description and management assertion, and additional category-specific criteria are outside this portfolio subset.
The project is neither a complete SOC 2 readiness assessment nor a complete ISO ISMS.

ISO/IEC 27001 clauses 4–10 require an ISMS: context, leadership, planning, support, operation, evaluation and improvement.
A risk assessment and treatment process must consider necessary controls and compare with Annex A so needed controls are not omitted.
A Statement of Applicability records necessary controls, inclusion justification, implementation and exclusion rationale.
This subset is not that complete statement; controls outside this crosswalk are **not assessed**, not automatically excluded.
The 2024 climate-action amendment needs consideration in an operational ISMS context review; this toolkit does not perform that review.

## Why evidence is not interchangeable

| Example | Reusable evidence | Separate assessment |
| --- | --- | --- |
| CTL-003 / CC6.3 / A.5.18 | Complete identity roster, signed decisions, verified removals | Scope, authorization, review frequency, duty conflicts, service identities and full-period operation |
| CTL-010 / CC7.2 / A.8.15 and A.8.16 | Telemetry, health and alert records | Logging alone is partial: analyze anomalies, detect feed gaps and evaluate effects on commitments |
| CTL-014 / CC8.1 / A.8.32 | Ticket, tests, approvals, deployment record | Cloud API logs do not prove prior approval; inspect changes to GPOs, endpoint policies, procedures and rules too |
| CTL-004 / CC6.4 / A.7.2 | Badge and visitor approvals; provider assurance | Provider facility responsibility and customer office controls have distinct owners and evidence |

## Reference confidence

Official publisher landing pages establish editions. Vendor documentation supports the described operational capabilities.
Full normative text was not available in this session: AICPA download access and ISO browsing previews were limited.
The identifiers, titles, summaries and all crosswalk judgments therefore remain **pending licensed-text and practitioner review**.
Automated validation confirms internal referential consistency, not normative accuracy or control effectiveness.
See [source register](sources.md). Do not replace these qualifications with a claim of verified certification readiness.
