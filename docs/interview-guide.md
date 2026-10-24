# Interview notes

Use the records to explain the work. The access-removal example gives a clearer starting point than a list of framework names.

## Opening explanation

“The question behind this project is: what evidence would convince me a control actually worked?
I used an access review as the main example. The reviewer says to remove an account's administrator access,
but nobody has recorded that removal. The review exists, yet the test fails and the risk stays open.

From there, I built a control matrix for SOC 2 CC6, CC7 and CC8, linked it to relevant ISO 27001 Annex A controls,
and added evidence requests, tests, risk records and an incident runbook. AD, Sophos, Wazuh and AWS define the
proposed environment. The examples are synthetic; I have not deployed or tested that stack in this project.”

## Questions to prepare for

### Does an ISO control satisfy a SOC 2 criterion?

No. For example, logging under A.8.15 gives inputs for CC7.2, but producing logs does not show that anomalies
are detected or evaluated. That relationship is Partial. I record the shared objective and what still needs
separate treatment. Even a Direct relationship needs evidence suited to each framework's scope and assessment.

### How would you test an access review?

First reconcile the review population against source identities, including nested groups, service accounts and
cloud effective permissions. Then inspect who reviewed the access and why. For a Remove decision, check the
actual rights and applicable sessions after remediation. Finally, check repeated reviews across the period.
SYN-AR-002 fails because there is no verified removal. A signed review is not enough.

### What would you do when Wazuh raises an alert?

Check the source event, ingestion time, rule context, affected asset and related activity. Use Sophos for endpoint
context, AD for account and group changes, and CloudTrail or Config for cloud activity. Similar names or IPs
are not proof of the same actor. Preserve evidence, record the incident decision and get authorized owners to
perform and verify containment. Disabling an AD account does not end every existing session.

### Why hash the evidence files?

To detect a change relative to a trusted baseline. A hash does not prove who collected a file, whether the export
was complete or whether its contents are genuine. Real evidence also needs source and query details, a defined
period, population checks, controlled originals and custody records. The repository manifest checks fixture integrity only.

### What would you improve first?

I would verify the mappings against authorized framework texts, then implement a small authorized lab and test
the collection paths. The monitoring example includes an alert but no feed-outage exercise; that is a useful first
test because silence can mean either no events or a broken collector. I would also verify account removal and
session handling before treating the access-review process as effective. The full ISO ISMS and other SOC 2 areas
remain outside this project's scope.

## Demo order

1. Open the architecture and identify which systems enforce controls and which collect evidence.
2. Follow CTL-003 → EV-003 → SYN-AR-002 → TST-003 → RSK-001. Explain why the risk remains Critical.
3. Compare Direct A.5.18 with Partial A.8.2 in the mapping relationships.
4. Open the incident timeline. Point out the separate detection, authorization and action receipts.
5. Run the validator. Explain the difference between a passing repository check and a working security control.

Keep the scope clear when discussing results: the control outcomes are fictional desk reviews. Do not describe
the incident as something handled in production, or imply that the project earned an audit opinion or certification.
