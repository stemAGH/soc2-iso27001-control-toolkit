# Incident response runbook

Owner: Incident Commander. Version 1.0, 2026-10-24. Review semiannually and after material incidents.
This is a tabletop-ready design. Adapt scope, contacts, authority, tool versions and legal obligations before live use.
Use [incident template](../templates/incident-record.md) and [fictional worked case](../examples/incident-record.md).

## Identify and triage

SOC analyst opens a case for a Wazuh alert, Sophos detection, AD anomaly, AWS finding or user report.
Capture alert ID, event and ingestion times in UTC, source, user/device identifiers, rule version and affected service.
Check feed health, asset criticality, approved maintenance and corroborating events. Preserve the original alert.
Distinguish an event from an incident: document a justified declaration or non-incident disposition.
An alert severity is an input; the commander evaluates actual and potential business impact.

| Severity | Illustrative trigger | Internal acknowledgment target | Escalation and updates |
| --- | --- | --- | --- |
| SEV1 Critical | Active destructive spread, confirmed privileged takeover or major service/data impact | 15 minutes, on-call coverage required | Page commander, security and service executives immediately; updates every 30 minutes |
| SEV2 High | Credible privileged misuse or contained compromise with material potential | 30 minutes, on-call coverage required | Commander and affected owners immediately; hourly updates |
| SEV3 Medium | Suspicious limited activity requiring investigation, no established material impact | 4 business hours | SOC Lead and system owner; daily updates |
| SEV4 Low | Low-risk anomaly needing tracked follow-up | Next business day | Assign analyst; update on disposition |

These are fictional service targets, not SOC 2, ISO or legal deadlines. Upgrade severity as evidence changes.
The SOC Lead maintains primary and backup on-call routes in a restricted directory, tests them quarterly and
confirms them before any operational exercise. No real emergency contact details are embedded in this portfolio.
If the primary fails to acknowledge within the severity target, page the backup commander and service executive.

## Escalation and communication

Commander owns incident decisions, timeline and incident channel. System owners execute authorized technical actions.
Evidence Custodian preserves originals; legal/privacy lead determines notification duties, required recipients and
timelines based on contracts, jurisdictions and facts. Executive or designated communications lead approves external
statements; analysts do not make unsupported no-breach claims. Record decision, approver, recipients, time and next update.
Use an out-of-band route if identity or messaging infrastructure may be compromised. Assign a scribe and backup commander.

## Investigate by technology

| Technology | Read and correlate | Limit and preservation step |
| --- | --- | --- |
| Wazuh | Alert details, rule ID/version, agent status, source events, file-integrity and inventory changes; compare event and arrival time | Export raw source and alert; check gaps and clock offset. A rule match is not proof of compromise. Validate rule behavior for deployed version. |
| Active Directory | Account and nested group state; events 4624/4625, 4720/4725, 4728/4729 and 4732/4733 where configured; GPO and admin changes | 4625 occurs on the attempted-logon target; collect appropriate hosts/DCs. Enable required audit policy. Replicated lastLogonTimestamp is approximate; exact activity needs broader evidence. |
| Sophos | Device health, assigned protection policy, detection context and available investigation details; isolation/action history | Preserve details before cleanup. Isolation and EDR/XDR features depend on license, OS, role and product version; confirm availability and management connectivity. |
| AWS | CloudTrail actor/session, event source/name, account/Region, API parameters, IAM and role policies; Config history and relevant GuardDuty findings if enabled | Check event selectors and all scoped Regions/accounts. Event history alone is not durable full-scope logging; selected data events need explicit coverage. Preserve S3 originals and digest records where enabled. |

Do not infer that similar names/IPs prove a shared actor. Verify federation and session identifiers separately.
Use read-only scoped roles for collection; never place access keys or console tokens in case notes or public Git.

## Preserve evidence

Collect volatile evidence when justified and authorized, documenting method and impact. Export original logs and
case metadata with source, query, scope and UTC times; hash at acquisition; record transfer, handler, access and disposition.
Store originals read-only in an access-controlled repository with an independently protected integrity ledger.
Create working copies for analysis and mask sensitive values for reviewers. Preserve relevant legal holds.
CloudTrail digest delivery must be enabled and actual validation executed; the toggle alone does not validate logs.
AWS CLI validation uses original S3 locations, not local downloaded fixtures. A local SHA-256 is only a local integrity check.

## Contain, eradicate and recover

1. Commander chooses proportional containment after assessing scope, safety, dependencies and evidence loss. Preserve first where feasible; urgent harm can justify documented exceptions.
2. Endpoint owner may isolate using Sophos when licensed/authorized; confirm the receipt. Avoid indiscriminately isolating domain controllers or critical services. If unavailable, use a preapproved network containment method and verify connectivity impact.
3. IAM owner restricts affected accounts, removes unauthorized rights and rotates exposed secrets safely. Disabling AD does not invalidate every existing ticket/session. Address active sessions and service dependencies separately. Do not assume Wazuh active response supplies AD containment.
4. Cloud owner evaluates affected IAM/federated sessions, role trust, policies and resources; revoke or restrict through an approved procedure that considers existing sessions. Preserve CloudTrail and Config before modification. Keep emergency access available under controlled authority.
5. Identify persistence and initial access, remove unauthorized configuration, patch the exploited path and rebuild from trusted media when confidence in host integrity is insufficient. Reimage or deletion needs recorded authorization and preserved evidence.
6. Restore into an isolated, validated environment. Check integrity, dependencies, service health, protection policy and logging. Test against approved RTO/RPO; successful backup alone is insufficient.
7. Service owner authorizes reconnection, with commander concurrence. Monitor for recurrence; define observation duration based on incident risk. Link all emergency changes to independent retrospective review.

## Post-incident review

Hold a review within five business days after recovery as a local target. Record facts and uncertainty, root cause,
timeline, detection delay, containment results, impact, communications, recovery performance and evidence gaps.
Assign every corrective action an owner, due date and verification step. Update risks, mappings, detection rules,
training and runbook. Retest material fixes; closing the case does not close unrelated risks or treatment tickets.
