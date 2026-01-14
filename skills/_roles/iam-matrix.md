# IAM Roles & Permissions Matrix

This document defines the IAM role requirements for skills and personas in the security operations workflow system.

## MCP Tool → IAM Role Reference

### Chronicle SIEM (secops-mcp)

| Role | Description | Typical Use Case |
|------|-------------|------------------|
| `roles/chronicle.viewer` | Read-only access to logs, alerts, entities | Tier 1 triage, basic lookups |
| `roles/chronicle.limitedViewer` | Read-only, excludes detection rules/retrohunts | Restricted analysts |
| `roles/chronicle.editor` | Create/update cases, run queries, manage rules | Tier 2+, Threat Hunters |
| `roles/chronicle.admin` | Full access including settings, data RBAC | Tier 3, IR leads, Admins |
| `roles/chronicle.restrictedDataAccessViewer` | Scoped data visibility via data RBAC | Compartmentalized access |

### Chronicle SOAR (secops-soar)

| Role | Description | Typical Use Case |
|------|-------------|------------------|
| `roles/chronicle.editor` | Case comments, priority changes, basic case mgmt | All analysts |
| `roles/chronicle.soarAdmin` | Full SOAR control, playbooks, integrations | IR leads, SOC Manager |
| `roles/chronicle.soarThreatManager` | Threat collection and findings management | CTI Researcher |
| `roles/chronicle.soarVulnerabilityManager` | Vulnerability findings management | Security Engineer |

### Google Threat Intelligence (gti-mcp)

| License Tier | Capabilities | Typical Use Case |
|--------------|--------------|------------------|
| GTI Standard | IOC lookups, file/domain/IP/URL reports | Tier 1-2 analysts |
| GTI Enterprise | + Threat actors, campaigns, collections | Tier 3, Hunters |
| GTI Enterprise+ | + Full relationship graphs, attribution, pivoting | CTI Researchers, Advanced hunting |

### Security Command Center (scc-mcp)

| Role | Description | Typical Use Case |
|------|-------------|------------------|
| `roles/securitycenter.findingsViewer` | Read-only access to findings | All analysts |
| `roles/securitycenter.findingsEditor` | Modify findings, set marks, mute | Tier 2+, IR |
| `roles/securitycenter.adminViewer` | Full SCC visibility including posture | SOC Manager |
| `roles/securitycenter.adminEditor` | Full SCC write access | Security Engineer, IR |

---

## Skill → Required Roles Matrix

Each skill requires specific IAM roles to function. Skills will fail or have limited functionality if the executing service account lacks the required roles.

| Skill | Chronicle | SOAR | GTI | SCC |
|-------|-----------|------|-----|-----|
| `triage-alert` | viewer | editor | Standard | - |
| `enrich-ioc` | viewer | - | Standard | - |
| `check-duplicates` | - | editor | - | - |
| `document-in-soar` | - | editor | - | - |
| `close-soar-artifact` | - | editor | - | - |
| `find-relevant-case` | - | editor | - | - |
| `correlate-ioc` | viewer | editor | - | - |
| `triage-suspicious-login` | viewer | editor | Standard | - |
| `triage-malware` | viewer | editor | Enterprise | - |
| `deep-dive-ioc` | editor | editor | Enterprise | - |
| `pivot-on-ioc` | - | - | Enterprise+ | - |
| `hunt-threat` | editor | - | Enterprise | - |
| `hunt-apt` | editor | - | Enterprise+ | - |
| `hunt-ioc` | editor | - | Enterprise | - |
| `hunt-lateral-movement` | editor | - | Standard | - |
| `hunt-credential-access` | editor | - | Standard | - |
| `respond-ransomware` | admin | soarAdmin | Enterprise | adminEditor |
| `respond-malware` | admin | soarAdmin | Enterprise | findingsEditor |
| `respond-phishing` | editor | soarAdmin | Enterprise | - |
| `respond-compromised-account` | editor | soarAdmin | Standard | - |
| `generate-report` | - | - | - | - |
| `confirm-action` | - | - | - | - |

**Legend:**
- `-` = Not required for this skill
- `viewer` = `roles/chronicle.viewer`
- `editor` = `roles/chronicle.editor`
- `admin` = `roles/chronicle.admin`
- `soarAdmin` = `roles/chronicle.soarAdmin`
- `findingsViewer` = `roles/securitycenter.findingsViewer`
- `findingsEditor` = `roles/securitycenter.findingsEditor`
- `adminEditor` = `roles/securitycenter.adminEditor`

---

## Persona → IAM Role Mapping

Each persona operates within defined IAM boundaries based on their responsibilities.

| Persona | Chronicle | SOAR | GTI | SCC |
|---------|-----------|------|-----|-----|
| Tier 1 SOC Analyst | viewer | editor | Standard | - |
| Tier 2 SOC Analyst | editor | editor | Enterprise | findingsViewer |
| Tier 3 SOC Analyst | admin | editor | Enterprise+ | findingsEditor |
| Threat Hunter | editor | viewer | Enterprise+ | findingsViewer |
| Incident Responder | admin | soarAdmin | Enterprise | adminEditor |
| CTI Researcher | viewer | soarThreatManager | Enterprise+ | - |
| Detection Engineer | admin | editor | Enterprise | - |
| SOC Manager | viewer | soarAdmin | Enterprise | adminViewer |
| Security Engineer | admin | soarAdmin | Enterprise | adminEditor |
| Compliance Manager | viewer | viewer | Standard | adminViewer |
| CISO | viewer | viewer | Enterprise | adminViewer |

---

## Role Escalation Paths

When a skill requires higher privileges than the persona typically has:

1. **Escalate to higher-tier analyst** - Tier 1 → Tier 2 → Tier 3
2. **Invoke Incident Responder** - For containment/eradication actions
3. **Request temporary elevation** - Document justification, get approval
4. **Use confirm-action skill** - Ensures human approval before privileged operations

---

## External References

- [Chronicle IAM Roles](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle)
- [Chronicle Feature Access Control](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access)
- [SOAR Access Control](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform)
- [Security Command Center IAM](https://cloud.google.com/security-command-center/docs/access-control)
- [Google Threat Intelligence API](https://gtidocs.virustotal.com/reference/api-overview)
