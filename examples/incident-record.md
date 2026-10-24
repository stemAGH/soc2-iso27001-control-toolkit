# SYN-INC-001 — lab identity and endpoint investigation

**SYNTHETIC tabletop case. Every event, person, action and outcome below is fabricated.**
Period: 2026-10-20 through 2026-10-22 UTC. Scope: SYN-WS-01, SYN-DC-01 and AWS lab account 111122223333.
Owner: Synthetic Incident Commander. Status: Closed tabletop; linked cloud finding remains open.

| UTC on 2026-10-20 | Decision or action | Supporting fixture |
| --- | --- | --- |
| 08:58 | Privileged global-group addition observed | SYN-AD-001 in ad-events.jsonl |
| 09:00 | Failed logon burst and AWS ingress change observed | SYN-WZ-001; SYN-CT-001 |
| 09:02 | Wazuh lab alert delivered | SYN-WZ-001 |
| 09:03 | Separate harmless endpoint test detection | SYN-SP-001 |
| 09:05 | Analyst acknowledged alert and began correlation | Fictional case note |
| 09:10 | SEV2 incident declared; possible privileged misuse, business impact unconfirmed | Fictional commander decision |
| 09:11 | Event exports preserved before containment; lab-only custody opened | evidence/chain-of-custody.csv |
| 09:12 | Commander approved host isolation and identity restriction | Fictional authorization |
| 09:14 | Host isolation confirmed | SYN-SP-002 |
| 09:16 | Account disabled; group removed and active remote sessions ended separately | SYN-AD-002; fictional operator case receipt |
| 09:18 | AWS role sessions investigated separately; no federation link proven; no unsupported cross-system identity conclusion | Fictional cloud case note |
| 10:00 | Persistence review completed; rebuild chosen for lab host | Fictional endpoint investigation note |
| 11:00 | Rebuilt from approved clean image; rotated exposed lab authentication material | Fictional recovery receipt |
| 12:00 | Service tests, endpoint health and logging verified; owner accepted return to service | Fictional acceptance |

Classification: possible privileged misuse in a tabletop; harmless endpoint detection is a parallel signal, not proof of malware or causation. IP and time overlap do not prove the AD and AWS actors are the same identity.

Impact: one isolated lab workstation; no substantiated exfiltration. Preserve uncertainty rather than assert no breach.
Communications: commander informed synthetic SOC and service owners at 09:10; legal/privacy reviewer documented that the fictional case has no real notification obligation. A live event requires jurisdiction, contractual and privacy review; there is no universal deadline in this toolkit.

Recovery: 09:00 to 12:00 = 3 hours against a fictional 4-hour RTO. No data restore required; fictional RPO is 24 hours and was not exercised by this rebuild. Thirty-minute lab observation ended 12:30 without repeated test alerts; this does not establish durable recovery.

Post-incident review on 2026-10-22: unmatched group change requires stronger approval reconciliation. Follow-up SYN-LESSON-001 assigned to IAM Lead due 2026-10-30; SYN-LESSON-002 feed-outage exercise assigned to SOC Lead due 2026-11-05. Both open at portfolio review. Open ingress finding SYN-CF-001 is tracked in RSK-002; case closure does not assert its remediation.

Separate non-incident example SYN-EVT-002: a 2026-10-20T10:00Z lab rule-maintenance alert was evaluated at 10:10Z; analyst matched the documented SYN-CHG-001 maintenance scope and closed as authorized activity. This rationale requires verification in a live environment.
