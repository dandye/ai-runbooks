# Security Operations Skills

Claude Code skills for security operations workflows. Converted from runbooks in `rules_bank/run_books/`.

## Directory Structure

```
skills/
├── _personas/              # Persona manifest files (YAML)
│   ├── tier1-analyst.yaml
│   ├── tier2-analyst.yaml
│   ├── threat-hunter.yaml
│   └── incident-responder.yaml
├── _workflows/             # Composite/orchestration skills
│   ├── full-alert-triage/
│   └── full-investigation/
├── _roles/                 # IAM role documentation
│   └── iam-matrix.md
└── <skill-name>/           # Individual atomic skills
    └── SKILL.md
```

## Skill Schema

Each skill's `SKILL.md` file contains YAML frontmatter with the following fields:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Skill identifier (kebab-case) |
| `description` | Yes | Brief description for tool registration |
| `required_roles` | Yes | IAM roles needed (chronicle, soar, gti, scc) |
| `personas` | Yes | Which personas can use this skill |

### Skill Outputs

Outputs are documented in the **markdown body** of each skill under a `## Required Outputs` section, not in the YAML frontmatter. This ensures the LLM reads and follows the output instructions.

Example format in skill body:
```markdown
## Required Outputs

**After completing this skill, you MUST report these outputs:**

| Output | Description |
|--------|-------------|
| `GTI_FINDINGS` | Summary of GTI report |
| `MALICIOUS_CONFIDENCE` | Confidence level: high, medium, low, none |
```

**Naming Convention:** Use `UPPER_SNAKE_CASE` for all output variables.

---

## Prerequisites

MCP servers required:
- `secops-mcp` - Chronicle SIEM
- `secops-soar` - SOAR platform
- `gti-mcp` - Google Threat Intelligence

### IAM Roles

Skills require specific IAM roles. See `_roles/iam-matrix.md` for the complete mapping. Summary:

| Persona | Chronicle | SOAR | GTI |
|---------|-----------|------|-----|
| Tier 1 Analyst | `roles/chronicle.viewer` | `roles/chronicle.editor` | GTI Standard |
| Tier 2 Analyst | `roles/chronicle.editor` | `roles/chronicle.editor` | GTI Enterprise |
| Threat Hunter | `roles/chronicle.editor` | `roles/chronicle.viewer` | GTI Enterprise+ |
| Incident Responder | `roles/chronicle.admin` | `roles/chronicle.soarAdmin` | GTI Enterprise |

## Quick Reference

| Skill | Invocation | Purpose |
|-------|------------|---------|
| `alert-triage` | `/alert-triage CASE_ID=X` | Triage alerts, determine FP/TP |
| `suspicious-login-triage` | `/suspicious-login-triage USER_ID=X` | Investigate login anomalies |
| `malware-triage` | `/malware-triage FILE_HASH=X` | Analyze suspicious files |
| `deep-dive-ioc` | `/deep-dive-ioc IOC_VALUE=X` | Comprehensive IOC investigation |
| `threat-hunt` | `/threat-hunt HUNT_HYPOTHESIS="..."` | Hypothesis-driven hunting |
| `apt-hunt` | `/apt-hunt THREAT_ACTOR_ID=X` | Hunt for specific threat actor |
| `ioc-hunt` | `/ioc-hunt IOC_LIST="X,Y,Z"` | Search for IOCs in environment |
| `lateral-movement-hunt` | `/lateral-movement-hunt` | Hunt for lateral movement |
| `credential-access-hunt` | `/credential-access-hunt TECHNIQUE_IDS="T1003"` | Hunt credential theft TTPs |
| `ransomware-response` | `/ransomware-response CASE_ID=X` | Full ransomware IR workflow |
| `malware-response` | `/malware-response CASE_ID=X` | Full malware IR workflow |
| `phishing-response` | `/phishing-response CASE_ID=X` | Full phishing IR workflow |
| `compromised-account-response` | `/compromised-account-response USER_ID=X` | Account compromise response |
| `enrich-ioc` | `/enrich-ioc 198.51.100.10` | GTI + SIEM enrichment |
| `pivot-on-ioc` | `/pivot-on-ioc evil.com` | Explore GTI relationships |
| `correlate-ioc` | `/correlate-ioc 198.51.100.10` | Find related alerts/cases |
| `check-duplicates` | `/check-duplicates CASE_ID=X` | Find duplicate cases |
| `find-relevant-case` | `/find-relevant-case` | Search for related cases |
| `document-in-soar` | `/document-in-soar CASE_ID=X` | Add case comments |
| `close-soar-artifact` | `/close-soar-artifact` | Close cases/alerts |
| `generate-report` | `/generate-report` | Save findings to file |
| `confirm-action` | `/confirm-action` | Request user confirmation |

---

## Skills by Category

### Triage (4 skills)

| Skill | Inputs | When to Use |
|-------|--------|-------------|
| `alert-triage` | `CASE_ID` or `ALERT_ID` | Initial alert assessment |
| `suspicious-login-triage` | `USER_ID`, `CASE_ID` | Impossible travel, failed logins |
| `malware-triage` | `FILE_HASH`, `CASE_ID` | Malware detection alerts |
| `deep-dive-ioc` | `IOC_VALUE`, `IOC_TYPE` | Escalated IOC investigation |

### Threat Hunting (5 skills)

| Skill | Inputs | When to Use |
|-------|--------|-------------|
| `threat-hunt` | `HUNT_HYPOTHESIS` | General hypothesis-driven hunting |
| `apt-hunt` | `THREAT_ACTOR_ID` or `COLLECTION_ID` | Hunt specific threat actor |
| `ioc-hunt` | `IOC_LIST` | Check IOCs from threat intel |
| `lateral-movement-hunt` | `TIME_FRAME_HOURS` | Hunt PsExec, WMI, RDP abuse |
| `credential-access-hunt` | `TECHNIQUE_IDS` | Hunt LSASS dumps, credential theft |

### Incident Response (4 skills)

| Skill | Inputs | When to Use |
|-------|--------|-------------|
| `ransomware-response` | `CASE_ID`, indicators | Ransomware detected |
| `malware-response` | `CASE_ID`, `FILE_HASH` | Malware on endpoints |
| `phishing-response` | `CASE_ID`, email artifacts | Phishing email reported |
| `compromised-account-response` | `USER_ID`, `CASE_ID` | Account compromise suspected |

### Enrichment (3 skills)

| Skill | Inputs | When to Use |
|-------|--------|-------------|
| `enrich-ioc` | `IOC_VALUE`, `IOC_TYPE` | Quick reputation lookup |
| `pivot-on-ioc` | `IOC_VALUE`, `RELATIONSHIP_NAMES` | Expand investigation via GTI |
| `correlate-ioc` | `IOC_LIST` | Find related alerts/cases |

### Case Management (4 skills)

| Skill | Inputs | When to Use |
|-------|--------|-------------|
| `check-duplicates` | `CASE_ID` | Before deep investigation |
| `find-relevant-case` | `SEARCH_TERMS` | Find related investigations |
| `document-in-soar` | `CASE_ID`, `COMMENT_TEXT` | Document findings |
| `close-soar-artifact` | `ARTIFACT_ID`, `REASON` | Close FP/BTP cases |

### Utility (2 skills)

| Skill | Inputs | When to Use |
|-------|--------|-------------|
| `generate-report` | `REPORT_TYPE`, findings | Save investigation to file |
| `confirm-action` | `QUESTION_TEXT` | Before containment actions |

---

## Common Workflows

### Alert Triage Flow
```
/alert-triage CASE_ID=1234
  → /check-duplicates
  → /enrich-ioc (for each entity)
  → /document-in-soar
  → /close-soar-artifact (if FP)
```

### Threat Hunt Flow
```
/apt-hunt THREAT_ACTOR_ID=UNC1234
  → GTI intelligence gathering
  → /ioc-hunt (for actor IOCs)
  → /enrich-ioc (for hits)
  → /generate-report
```

### Incident Response Flow
```
/phishing-response CASE_ID=1234
  → /enrich-ioc (URLs, domains)
  → /confirm-action (block IOCs?)
  → /compromised-account-response (for clickers)
  → /generate-report
```

---

## Common Input Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `CASE_ID` | SOAR case identifier | `1234` |
| `ALERT_ID` | Alert identifier | `alert-5678` |
| `IOC_VALUE` | Indicator value | `evil.com`, `198.51.100.10` |
| `IOC_TYPE` | Type of indicator | `Domain`, `IP Address`, `File Hash`, `URL` |
| `USER_ID` | Username or email | `jsmith`, `jsmith@example.com` |
| `FILE_HASH` | SHA256/MD5/SHA1 hash | `abc123...` |
| `HUNT_HYPOTHESIS` | Hunt objective | `"DNS tunneling for C2"` |
| `TIME_FRAME_HOURS` | Search lookback | `72`, `168` |
| `TECHNIQUE_IDS` | MITRE ATT&CK IDs | `"T1003.001,T1555.003"` |

---

## Persona-Based Orchestration

### Available Personas

| Persona | File | Primary Skills | Use Case |
|---------|------|----------------|----------|
| **Tier 1 Analyst** | `_personas/tier1-analyst.yaml` | alert-triage, enrich-ioc, check-duplicates | Initial alert triage |
| **Tier 2 Analyst** | `_personas/tier2-analyst.yaml` | deep-dive-ioc, correlate-ioc, malware-triage | Escalated investigations |
| **Threat Hunter** | `_personas/threat-hunter.yaml` | apt-hunt, ioc-hunt, threat-hunt | Proactive hunting |
| **Incident Responder** | `_personas/incident-responder.yaml` | ransomware-response, malware-response | IR lifecycle |

### Composite Workflows

| Workflow | Location | Description |
|----------|----------|-------------|
| **Full Alert Triage** | `_workflows/full-alert-triage/` | Complete Tier 1 workflow: check-duplicates → alert-triage → enrich-ioc → close/escalate |
| **Full Investigation** | `_workflows/full-investigation/` | Complete Tier 2 workflow: deep-dive-ioc → correlate → specialized triage → report |

### Using Personas

**Claude Code:**
```
Use Task tool with subagent_type matching the persona:
- soc-analyst-tier-1
- soc-analyst-tier-2
- threat-hunter
- incident-responder
```

**Gemini CLI:**
```bash
gemini -p "@skills/_personas/tier1-analyst.yaml Triage CASE-1234 following this persona workflow"
```

**Other LLMs:**
Read the persona YAML and follow the defined workflow chains.

### Persona Workflow Chains

**Tier 1 (Alert Triage):**
```
check-duplicates → alert-triage → enrich-ioc → [close OR escalate to Tier 2]
```

**Tier 2 (Investigation):**
```
deep-dive-ioc → correlate-ioc → [malware-triage | suspicious-login-triage] → pivot-on-ioc → report
```

**Threat Hunter:**
```
threat-hunt → [apt-hunt | ioc-hunt | lateral-movement-hunt] → enrich-ioc → pivot-on-ioc → report
```

**Incident Responder (PICERL):**
```
[ransomware | malware | phishing | account]-response → confirm-action → [containment] → generate-report
```

---

## Source Runbooks

These skills were converted from runbooks in `rules_bank/run_books/`. For detailed workflow diagrams, rubrics, and completion criteria, refer to the original runbooks.

## References

- `_roles/iam-matrix.md` - IAM role requirements for each skill
- `_personas/*.yaml` - Persona definitions with workflows
- `_workflows/*/SKILL.md` - Composite workflow documentation
- `rules_bank/personas/` - Detailed persona descriptions
