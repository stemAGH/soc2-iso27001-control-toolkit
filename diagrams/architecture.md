# Proposed architecture and data flow

**Design only. No deployment or live connector is claimed.**

```mermaid
flowchart LR
  HR[HR lifecycle and managers] --> AD[Active Directory identities and GPO]
  AD --> WIN[Windows endpoints and servers]
  SOP[Sophos protection and response] --> WIN
  AD -->|Configured Windows event collection| WZ[Wazuh monitoring and alerting]
  WIN -->|Agent events and inventory| WZ
  SOP -->|Configured export or connector required| WZ
  AWS[AWS workload and IAM] --> CT[CloudTrail to protected S3 logs]
  AWS --> CFG[AWS Config findings]
  CT -->|Scoped Wazuh AWS integration| WZ
  CFG -->|Configured collection or separate review| SOC[SOC case management]
  WZ --> SOC
  SOC -->|Authorized actions and verification| RESP[Endpoint identity and cloud owners]
  AD --> EV[Restricted evidence store]
  SOP --> EV
  CT --> EV
  CFG --> EV
  SOC --> EV
  FAC[Facilities and provider assurance] --> EV
  EV --> GRC[GRC review and tests]
  GRC --> MAP[Control mapping and risk treatment]
  MAP --> OWN[Accountable control owners]
```

Telemetry detects events; source systems enforce controls. GRC reviews evidence rather than claiming enforcement.
Production logs remain in protected source/evidence stores; only fabricated examples belong in public Git.
Sophos and AWS Config paths require explicit configuration and product/permission review. AWS supplies provider
infrastructure assurance while customer owners configure their workloads and review inherited-control dependencies.
