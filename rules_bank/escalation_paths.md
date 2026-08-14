---
name: escalation_paths
description: Defines who to notify and escalate to under specific incident circumstances, by severity and incident type.
type: "reference"
category: "security_operations"
status: "draft"
tags:
  - escalation
  - incident_response
  - communication
generated:
  by: human:dandye
  at: 2026-08-14T21:35:00Z
---

# Escalation Paths

Referenced by the IRP runbooks (malware, ransomware, phishing, compromised account). This is an organization-specific template — replace the placeholder roles and thresholds with your own on-call structure.

## Severity-Based Escalation

| Severity | Trigger examples | Escalate to | Timeframe |
|----------|------------------|-------------|-----------|
| Critical | Confirmed ransomware, active data exfiltration, PII exposure | SOC Manager + Incident Responder + CISO | Immediately |
| High | Confirmed malware on critical asset, compromised privileged account | Tier 3 Analyst + SOC Manager | Within 30 minutes |
| Medium | Confirmed malware on standard asset, suspicious lateral movement | Tier 2 Analyst | Within 2 hours |
| Low | Unconfirmed suspicious activity, policy violations | Tier 1 queue (normal triage) | Normal SLA |

## Incident-Type Escalation

- **Ransomware (confirmed):** SOC Manager and CISO immediately; legal/comms per organization policy before any external statement. See `run_books/irps/ransomware_response.md`.
- **PII / regulated-data exposure:** CISO and compliance manager; regulatory notification clocks may apply.
- **Compromised privileged account:** Incident Responder and identity/IAM team owner; see `run_books/irps/compromised_user_account_response.md`.
- **Phishing with credential submission:** Tier 2 Analyst; escalate to Incident Responder if credentials were privileged. See `run_books/irps/phishing_response.md`.

## Contacts

Role-to-person mapping lives in `key_contacts.md` (organization-specific; not committed with real data).
