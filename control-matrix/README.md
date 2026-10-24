# Control mapping matrix

This readable index summarizes [the canonical matrix](control-matrix.csv). Use [mapping relationships](mapping-relationships.csv) for each individual Direct or Partial edge and its rationale. All 14 controls are designed only; no live deployment is claimed.

| Control | Objective | SOC 2 | ISO/IEC 27001:2022 Annex A | Owner |
| --- | --- | --- | --- | --- |
| CTL-001 | Logical access architecture | CC6.1 | A.5.15; A.8.5 | IAM Lead |
| CTL-002 | Joiner and leaver authorization | CC6.2 | A.5.16; A.5.18 | IAM Lead |
| CTL-003 | Role changes and access recertification | CC6.3 | A.5.18; A.8.2; A.5.3 | System Owner |
| CTL-004 | Physical entry authorization | CC6.4 | A.7.2; A.7.4 | Facilities Lead |
| CTL-005 | Sanitization before asset release | CC6.5 | A.7.14; A.8.10 | IT Operations Lead |
| CTL-006 | External network access boundaries | CC6.6 | A.8.20; A.8.22 | Cloud Security Lead |
| CTL-007 | Authorized information transfer | CC6.7 | A.5.14; A.8.24; A.8.12 | Data Owner |
| CTL-008 | Malware and unauthorized software prevention | CC6.8 | A.8.7; A.8.19 | Endpoint Security Lead |
| CTL-009 | Vulnerability and configuration drift detection | CC7.1 | A.8.8; A.8.9 | Vulnerability Management Lead |
| CTL-010 | Security telemetry and anomaly monitoring | CC7.2 | A.8.15; A.8.16; A.8.17 | SOC Lead |
| CTL-011 | Event evaluation and incident declaration | CC7.3 | A.5.25; A.6.8 | Incident Commander |
| CTL-012 | Incident containment and response | CC7.4 | A.5.24; A.5.26; A.5.28 | Incident Commander |
| CTL-013 | Recovery and lessons learned | CC7.5 | A.5.27; A.8.13; A.5.30 | Service Owner |
| CTL-014 | Authorized and tested change lifecycle | CC8.1 | A.8.32; A.8.29; A.8.31; A.8.9 | Change Manager |

Direct is objective-level alignment, never full equivalence. Partial is supporting overlap. Neither is an official crosswalk. All edges require licensed-text and practitioner review. See [methodology](../docs/mapping-methodology.md).
