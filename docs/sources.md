# Source register and verification limits

Checked 2026-10-24. References support edition identity and operational design; the crosswalk is author interpretation.
No licensed framework text is redistributed. Control descriptions are concise original summaries.

| ID | Primary source | Supported use and access result |
| --- | --- | --- |
| SRC-TSC-01 | [AICPA: 2017 TSC with revised points of focus 2022](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022) | Publisher edition page accessible; full download limited. Exact criterion wording and point-of-focus completeness require authorized review. |
| SRC-ISO-01 | [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | Publisher confirms edition and amendment; full Annex A normative text not inspected. |
| SRC-ISO-02 | [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html) | Publisher confirms guidance edition; full text and control-title comparison remain pending. |
| SRC-ISO-03 | [ISO/IEC 27001:2022/Amd 1:2024](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec%3A27001%3Aed-3%3Av1%3Aamd%3A1%3Av1%3Aen) | Official amendment record; climate-action context requires separate ISMS review. |
| SRC-WAZUH-01 | [Wazuh AWS supported services](https://documentation.wazuh.com/current/cloud-security/amazon/services/supported-services/index.html) | CloudTrail S3 collection is a configured integration, not a deployment claim. |
| SRC-WAZUH-02 | [Wazuh default active responses](https://documentation.wazuh.com/current/user-manual/capabilities/active-response/default-active-response-scripts.html) | Platform-specific response capabilities; no assumption of native AD session containment. |
| SRC-MS-01 | [Microsoft event 4625](https://learn.microsoft.com/windows/security/threat-protection/auditing/event-4625) | Failed logon semantics and target-host collection. |
| SRC-MS-02 | [Microsoft AD events to monitor: official source](https://github.com/MicrosoftDocs/windowsserverdocs/blob/main/WindowsServerDocs/identity/ad-ds/plan/Appendix-L--Events-to-Monitor.md) | Account and group event semantics; auditing prerequisites still apply. The Microsoft Learn route was unavailable; its official source was accessible. |
| SRC-SOPHOS-01 | [Sophos computer details and actions](https://docs.sophos.com/central/customer/help/en-us/PeopleAndDevices/Devices/Computers/DeviceDetailsComputers/index.html) | Administrative isolation is license- and permission-dependent. |
| SRC-AWS-01 | [CloudTrail integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) | Enabling digest delivery does not itself validate integrity. |
| SRC-AWS-02 | [CloudTrail CLI validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-cli.html) | Original S3 location and access prerequisites; downloaded local files are not validated by this CLI. |

Reference confidence is intentionally explicit: official edition metadata checked; source capabilities reviewed;
normative wording, complete coverage, the mapping judgments and live effectiveness are not independently verified.
Before operational use, a qualified reviewer with authorized copies must confirm every mapped reference and rationale,
consider all applicable requirements, sign a versioned review record and adapt tests to the real scope.
No mapping relationship should be treated as authoritative merely because its identifier is syntactically valid.
