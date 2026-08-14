---
name: common_benign_alerts
description: Describes alert patterns often triggered by known benign activity and how to handle them during triage. Organization-specific template.
type: "reference"
category: "security_operations"
status: "draft"
tags:
  - triage
  - false_positives
  - alert_tuning
generated:
  by: human:dandye
  at: 2026-08-14T21:35:00Z
---

# Common Benign Alerts

Referenced by `run_books/triage_alerts.md` during initial assessment and documented in `readme.md`. This is an organization-specific template — populate with your environment's known-benign patterns. Every entry should name the alert, the benign cause, how to confirm it is the benign case, and the standard disposition.

| Alert pattern | Known benign cause | Confirmation check | Disposition |
|---------------|--------------------|--------------------|-------------|
| Port scan from internal host | Authorized vulnerability scanner (name scanner host) | Source IP matches scanner inventory | Close as expected activity |
| Mass file reads by service account | Backup agent (name agent and schedule) | Process path and schedule match backup window | Close as expected activity |
| PowerShell execution on admin workstation | Approved admin automation scripts (name script repo) | Script hash matches approved list | Close as expected activity |
| Impossible travel for VPN user | Split-tunnel VPN egress geography | Egress IP belongs to corporate VPN range | Close as expected activity |

Never auto-close on pattern match alone — the confirmation check must pass, and any deviation (unexpected source, changed hash, off-schedule) reverts to standard triage in `run_books/triage_alerts.md`.
