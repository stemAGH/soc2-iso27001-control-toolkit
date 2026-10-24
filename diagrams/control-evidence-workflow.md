# Control-to-evidence workflow

```mermaid
flowchart TD
  OBJ[Service commitments and risk] --> CTL[CTL objective and accountable owner]
  CTL --> MAP[Per-edge SOC 2 and ISO mapping with gaps]
  MAP --> REQ[EV request with scope period and collection method]
  REQ --> COL[Collector exports source and population metadata]
  COL --> STORE[Restricted originals hashes and custody ledger]
  STORE --> REV[Independent completeness and quality review]
  REV --> TEST[TST design and period operating tests]
  TEST --> DEC{All expected results evidenced?}
  DEC -->|Yes| PASS[Record scoped pass with limitations]
  DEC -->|Observed exception| FAIL[Record fail and remediation ticket]
  DEC -->|Missing evidence| NT[Record not tested and evidence gap]
  FAIL --> RISK[Risk owner treatment deadline and escalation]
  NT --> RISK
  RISK --> RETEST[Verify fix and retest without erasing history]
  RETEST --> REV
  PASS --> ASSESS[Separate assessor evaluation for each framework]
```

Worked example: CTL-003 → CC6.3 / A.5.18 (Direct) → EV-003 → SYN-AR-002 → TST-003 Fail → RSK-001.
The reviewer found a removal decision but no closure evidence; the residual risk remains Critical until verified treatment.
Reuse the roster and approval evidence across frameworks only when scope, period and evidence quality fit both assessments.
