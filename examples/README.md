# Synthetic evidence pack

All files in this directory are fabricated for an interview demonstration. No tool was deployed or connected.
JSON and JSONL use simplified, explicitly labeled toolkit schemas, not import-ready vendor payloads.
Names beginning SYN or syn, example.invalid domains, documentation IP ranges and AWS account 111122223333 are fictional identifiers.
The public-ingress CIDR 0.0.0.0/0 is an intentional insecure configuration example, not a source identity.

| File | What it demonstrates |
| --- | --- |
| [Control evidence](control-evidence/) | Fourteen evidence narratives with scope, timestamps, gaps and test outcomes |
| [Access review](access-review.csv) | Human and service identities, review approval and an overdue removal |
| [Risk register](risk-register.csv) | Six scored risks; current residual exposure remains until treatment is verified |
| [Wazuh alerts](wazuh-alerts.jsonl) | Correlation and event-versus-alert timing |
| [AD events](ad-events.jsonl) | Global-group addition 4728 and account disable 4725 |
| [Sophos events](sophos-events.jsonl) | Harmless test detection and authorized isolation receipt |
| [CloudTrail events](cloudtrail-events.json) | Simplified management API event; no AWS credentials |
| [AWS findings](aws-findings.json) | Open public SSH exposure and incomplete monitoring evidence |
| [Change records](change-record.json) | Standard and emergency changes; emergency sample uses a different resource than the open finding |
| [Incident record](incident-record.md) | Timeline, authority, containment, recovery and open lessons |
| [Test results](control-test-results.csv) | Desk reviews of fabricated cases, never live operating-effectiveness conclusions |

The case set deliberately includes failures and missing evidence. Do not present these files as production logs,
actual implementation achievements, independent assurance, or evidence of employment experience.
