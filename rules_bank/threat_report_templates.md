# Threat Intelligence Report Templates

## Overview
This document provides standardized templates for threat intelligence research and reporting tailored to different audiences and use cases. Each template is designed to communicate threat intelligence research findings effectively while maintaining appropriate detail levels and focusing on audience-specific priorities. These templates support the research, analysis, and reporting phases of threat intelligence work.

## Template Categories

### 1. Executive Report Template
**Audience**: C-Suite, Board Members, Senior Leadership  
**Length**: 1-2 pages  
**Focus**: Business impact, strategic risks, high-level metrics from research  
**Frequency**: Weekly/Monthly

### 2. Technical Analyst Report Template
**Audience**: SOC Analysts, Threat Hunters, Security Engineers  
**Length**: 5-10 pages  
**Focus**: Technical research findings, IOCs, detection methods, response procedures  
**Frequency**: Daily/Weekly

### 3. Operational Team Report Template
**Audience**: IT Operations, System Administrators, Network Teams  
**Length**: 2-3 pages  
**Focus**: Actionable tasks from research, patch requirements, configuration changes  
**Frequency**: As needed/Weekly

### 4. Incident Command Report Template
**Audience**: Incident Response Team, Crisis Management  
**Length**: 2-4 pages  
**Focus**: Active incident research, immediate threats, response coordination  
**Frequency**: As needed/During incidents

### 5. Board Presentation Template
**Audience**: Board of Directors  
**Length**: 3-5 slides  
**Focus**: Risk posture, compliance, strategic investments  
**Frequency**: Quarterly

---

## 1. Executive Report Template

```markdown
# Threat Intelligence Executive Report

**Date**: [YYYY-MM-DD]  
**Period**: [Date Range]  
**Prepared By**: [CTI Team/Analyst Name]  
**Classification**: TLP:WHITE

## Threat Landscape Overview
[One paragraph summary of the current threat environment, major trends, and relevance to organization]

## Top 3 Threats to Our Organization

### 1. [Threat Name]
**Business Impact**: [One sentence on potential business disruption]  
**Current Exposure**: [High/Medium/Low]  
**Mitigation Status**: [Percentage complete or status]  
**Investment Required**: [Yes/No - amount if applicable]

### 2. [Threat Name]
**Business Impact**: [One sentence on potential business disruption]  
**Current Exposure**: [High/Medium/Low]  
**Mitigation Status**: [Percentage complete or status]  
**Investment Required**: [Yes/No - amount if applicable]

### 3. [Threat Name]
**Business Impact**: [One sentence on potential business disruption]  
**Current Exposure**: [High/Medium/Low]  
**Mitigation Status**: [Percentage complete or status]  
**Investment Required**: [Yes/No - amount if applicable]

## Risk Assessment

| Risk Category | Current Level | Trend | Action Required |
|--------------|---------------|-------|-----------------|
| Ransomware | [High/Med/Low] | [↑→↓] | [Yes/No] |
| Data Breach | [High/Med/Low] | [↑→↓] | [Yes/No] |
| Supply Chain | [High/Med/Low] | [↑→↓] | [Yes/No] |
| Insider Threat | [High/Med/Low] | [↑→↓] | [Yes/No] |

## Key Metrics

- **Threats Detected**: [Number] ([Change]% from last period)
- **Incidents Prevented**: [Number]
- **Mean Time to Detect**: [Hours/Days]
- **Security Posture Score**: [Score/100]

## Required Executive Decisions

1. **[Decision Item]**  
   Context: [Brief context]  
   Recommendation: [Specific recommendation]  
   Timeline: [When needed by]

2. **[Decision Item]**  
   Context: [Brief context]  
   Recommendation: [Specific recommendation]  
   Timeline: [When needed by]

## Next Period Outlook
[2-3 sentences on expected threats and preparation recommendations]
```

---

## 2. Technical Analyst Report Template

```markdown
# Threat Intelligence Technical Report

**Date**: [YYYY-MM-DD]  
**Shift**: [Morning/Evening/Night]  
**Analyst**: [Name]  
**Classification**: TLP:AMBER

## Priority Intelligence Requirements (PIRs)

### Critical
1. [Specific threat or campaign to monitor]
2. [Specific threat actor activity]

### High
1. [Vulnerability or exploit to track]
2. [Suspicious activity patterns]

## Active Threat Campaigns

### Campaign: [Campaign Name]
**Threat Actor**: [Actor Name/Unknown]  
**First Seen**: [Date]  
**Last Activity**: [Date/Time]  
**Targeted Sectors**: [Industries]  
**Attack Vector**: [Email/Web/Network]

#### Tactics, Techniques, and Procedures (TTPs)
| Tactic | Technique | Procedure | MITRE ATT&CK |
|--------|-----------|-----------|--------------|
| [Tactic] | [Technique] | [Specific implementation] | [TID] |

#### Indicators of Compromise (IOCs)
```yaml
file_hashes:
  - md5: [hash]
    sha256: [hash]
    filename: [name]
    first_seen: [date]

network_indicators:
  - ip: [IP address]
    port: [port]
    protocol: [protocol]
    direction: [inbound/outbound]
    
  - domain: [domain]
    resolved_ips: [IPs]
    registration_date: [date]

email_indicators:
  - sender: [email]
    subject_pattern: [pattern]
    attachment_name: [pattern]
```

#### Detection Opportunities
```yaml
detection_rule_1:
  name: [Rule Name]
  platform: [SIEM/EDR/NDR]
  logic: |
    [Detection logic/query]
  
detection_rule_2:
  name: [Rule Name]
  platform: [SIEM/EDR/NDR]
  logic: |
    [Detection logic/query]
```

#### Response Procedures
1. **Containment**:
   - [Specific containment action]
   - [Specific containment action]

2. **Eradication**:
   - [Specific eradication step]
   - [Specific eradication step]

3. **Recovery**:
   - [Recovery procedure]
   - [Validation step]

## Vulnerability Intelligence

### Critical Vulnerabilities

#### CVE-[YYYY-NNNNN]
**Product**: [Affected product]  
**CVSS Score**: [Score]  
**Exploit Available**: [Yes/No/PoC]  
**Patch Available**: [Yes/No]  
**Exploitation ITW**: [Yes/No]  

**Technical Details**:
[Vulnerability description and technical impact]

**Detection**:
```
[Detection method or query]
```

**Mitigation**:
1. [Primary mitigation]
2. [Alternative mitigation]

## Threat Hunting Directives

### Hunt 1: [Hunt Name]
**Hypothesis**: [What we're looking for]  
**Data Sources**: [Logs/telemetry needed]  
**Query**:
```sql
[Hunting query]
```
**Expected Results**: [What indicates positive finding]

## Tool Updates and Signatures

### New YARA Rules
```yara
rule [Rule_Name] {
    meta:
        description = "[Description]"
        author = "[Author]"
        date = "[Date]"
        
    strings:
        $s1 = "[String]"
        $s2 = "[String]"
        
    condition:
        [Condition]
}
```

### Updated Detection Content
- **[Platform]**: [Number] new rules added
- **[Platform]**: [Number] rules updated
- **[Platform]**: [Number] false positive tunings

## Shift Handover Notes
[Important information for next shift]
```

---

## 3. Operational Team Report Template

```markdown
# Operational Security Report

**Date**: [YYYY-MM-DD]  
**To**: IT Operations Team  
**Priority**: [URGENT/High/Normal]  
**Action Required By**: [Date/Time]

## Immediate Actions Required

### 1. Critical Patches
| System/Application | CVE | Severity | Patch | Deadline |
|-------------------|-----|----------|-------|----------|
| [System] | CVE-YYYY-NNNNN | CRITICAL | [KB/Version] | [Date] |
| [System] | CVE-YYYY-NNNNN | HIGH | [KB/Version] | [Date] |

**Patching Instructions**:
1. [Step-by-step instruction]
2. [Step-by-step instruction]
3. [Validation step]

### 2. Configuration Changes
| System | Current Config | Required Config | Reason |
|--------|---------------|-----------------|--------|
| [System] | [Current] | [Required] | [Security reason] |

**Implementation Steps**:
```bash
# Example commands
[Command 1]
[Command 2]
```

### 3. Firewall Rules
| Action | Source | Destination | Port | Protocol | Reason |
|--------|--------|-------------|------|----------|--------|
| BLOCK | [IP/Range] | ANY | [Port] | [Protocol] | [Threat] |
| BLOCK | ANY | [IP/Domain] | [Port] | [Protocol] | [Threat] |

## Monitoring Requirements

### New Alert Rules
**Alert Name**: [Name]  
**System**: [System to monitor]  
**Condition**: [What triggers alert]  
**Action**: [What to do when triggered]  
**Escalation**: [Who to contact]

### Log Collection Changes
- **Add**: [New log source]
- **Increase**: [Log source] retention to [days]
- **Enable**: [Specific logging feature]

## Validation Checklist

- [ ] All critical patches applied
- [ ] Patch validation completed
- [ ] Configuration changes implemented
- [ ] Firewall rules active
- [ ] Monitoring alerts configured
- [ ] Log collection verified
- [ ] Backup completion confirmed
- [ ] Change tickets updated

## Point of Contact
**Primary**: [Name] - [Phone] - [Email]  
**Backup**: [Name] - [Phone] - [Email]  
**Escalation**: [Security Team Contact]

## References
- Change Request: [CR Number]
- Security Advisory: [Link]
- Vendor Bulletin: [Link]
```

---

## 4. Incident Command Report Template

```markdown
# Incident Command Report

**Incident ID**: INC-[NUMBER]  
**Date/Time**: [YYYY-MM-DD HH:MM UTC]  
**Severity**: [CRITICAL/HIGH/MEDIUM]  
**Status**: [ACTIVE/CONTAINED/RESOLVED]  
**Incident Commander**: [Name]

## Situation Overview
[2-3 sentences describing the incident, impact, and current status]

## Timeline
| Time (UTC) | Event |
|------------|-------|
| [HH:MM] | Initial detection |
| [HH:MM] | Incident declared |
| [HH:MM] | Containment started |
| [HH:MM] | [Significant event] |

## Affected Systems
| System | Status | Impact | Recovery ETA |
|--------|--------|--------|--------------|
| [System] | [Compromised/At Risk/Clear] | [Impact] | [Time] |

## Threat Actor Profile
**Attribution**: [Known Actor/Unknown]  
**Motivation**: [Financial/Espionage/Destruction]  
**Sophistication**: [High/Medium/Low]  
**Previous Activity**: [Yes/No - details if yes]

## Current Actions

### Containment
- [x] [Completed action]
- [ ] [In progress action]
- [ ] [Planned action]

### Investigation
- [x] [Completed action]
- [ ] [In progress action]
- [ ] [Planned action]

### Communication
- [x] Internal stakeholders notified
- [ ] External communications required
- [ ] Regulatory notifications

## Resource Allocation
| Team | Members Assigned | Status |
|------|-----------------|--------|
| Incident Response | [Number] | [Active/Standby] |
| SOC | [Number] | [Active/Standby] |
| IT Operations | [Number] | [Active/Standby] |
| Legal/Compliance | [Number] | [Active/Standby] |

## Decision Points

### Immediate Decisions Required
1. **[Decision]**  
   Options: [A, B, C]  
   Recommendation: [Option]  
   Deadline: [Time]

### Upcoming Decisions
1. **[Future decision]**  
   Timeline: [When needed]  
   Dependencies: [What must happen first]

## Next Update
**Time**: [HH:MM UTC]  
**Format**: [Call/Email/Slack]  
**Participants**: [Who should attend]
```

---

## 5. Board Presentation Template

```markdown
# Cybersecurity Threat Report
## Board of Directors
### [Quarter Year]

---

### Slide 1: Executive Summary

**Current Threat Level: [HIGH/ELEVATED/NORMAL]**

Key Points:
• [Major threat or incident this quarter]
• [Significant security achievement]
• [Important risk or investment need]

Speaker Notes:
[Detailed talking points for presenter]

---

### Slide 2: Threat Landscape

**Industry Threats**
| Threat | Our Exposure | Peer Impact | Our Response |
|--------|--------------|-------------|--------------|
| [Threat] | [Level] | [Companies affected] | [Status] |

**Emerging Risks**
• [Risk 1]: [One-line description]
• [Risk 2]: [One-line description]
• [Risk 3]: [One-line description]

Speaker Notes:
[Context about industry trends and our position]

---

### Slide 3: Security Posture

**Maturity Assessment**

[Visual: Maturity chart showing current vs target state across domains]

| Domain | Current | Target | Investment Needed |
|--------|---------|--------|-------------------|
| Identity & Access | [1-5] | [1-5] | [$Amount] |
| Data Protection | [1-5] | [1-5] | [$Amount] |
| Incident Response | [1-5] | [1-5] | [$Amount] |
| Threat Intelligence | [1-5] | [1-5] | [$Amount] |

Speaker Notes:
[Explanation of gaps and improvement plans]

---

### Slide 4: Compliance & Risk

**Regulatory Compliance**
• [Regulation]: [Status] - [Any issues]
• [Regulation]: [Status] - [Any issues]

**Risk Register Top 5**
1. [Risk]: [Mitigation status]
2. [Risk]: [Mitigation status]
3. [Risk]: [Mitigation status]
4. [Risk]: [Mitigation status]
5. [Risk]: [Mitigation status]

**Audit Findings**: [Number] High, [Number] Medium, [Number] Low

Speaker Notes:
[Details on compliance challenges and risk mitigation]

---

### Slide 5: Investment Recommendations

**Proposed Security Investments FY[Year]**

| Initiative | Cost | Risk Reduced | ROI Period |
|------------|------|--------------|------------|
| [Initiative] | [$Amount] | [Risk type] | [Months] |
| [Initiative] | [$Amount] | [Risk type] | [Months] |
| [Initiative] | [$Amount] | [Risk type] | [Months] |

**Total Investment**: [$Amount]  
**Risk Reduction**: [Percentage]  
**Compliance Achievement**: [Percentage]

**Board Approval Requested For**:
1. [Specific approval item]
2. [Specific approval item]

Speaker Notes:
[Business case for each investment]
```

---

## Usage Guidelines

### Selecting the Right Template
1. **Consider your audience's technical level**
   - Executives need business impact
   - Technical teams need actionable details
   - Board needs strategic overview

2. **Match frequency to audience needs**
   - Daily for operational teams during incidents
   - Weekly for security teams
   - Monthly/Quarterly for executives

3. **Adjust detail level appropriately**
   - Executive: Focus on impact and decisions
   - Technical: Include all IOCs and procedures
   - Operational: Emphasize specific actions

### Customization Guidelines

#### Adding Organization-Specific Elements
- Include company logo and branding
- Add department-specific sections
- Incorporate organizational risk categories
- Use company-standard classification labels

#### Adapting for Incident Types
- Ransomware: Emphasize recovery timelines
- Data breach: Focus on affected records
- APT: Detail attribution and long-term impact
- Insider threat: Highlight access reviews

### Distribution Best Practices

1. **Secure Distribution**
   - Use encrypted channels for TLP:RED/AMBER
   - Verify recipient list before sending
   - Track document access and sharing

2. **Timing Considerations**
   - Executive reports: Start of business day
   - Technical reports: Shift handovers
   - Incident reports: As events unfold

3. **Follow-up Actions**
   - Track action items from reports
   - Measure effectiveness of recommendations
   - Collect feedback for improvement

## Template Automation

### Integration Points
```yaml
automation:
  data_sources:
    - gti_platform
    - chronicle_siem
    - scc_vulnerabilities
    - soar_cases
    
  scheduling:
    executive_report:
      frequency: weekly
      day: monday
      time: "08:00"
      
    technical_report:
      frequency: daily
      time: "06:00"
      
    board_presentation:
      frequency: quarterly
      advance_notice: 2_weeks
      
  distribution:
    executive_report:
      method: secure_email
      recipients: leadership_dl
      
    technical_report:
      method: soar_case
      recipients: soc_team
      
    operational_report:
      method: ticketing_system
      recipients: it_operations
```

## Quality Checklist

Before distributing any report, verify:

- [ ] All data is current (within specified timeframe)
- [ ] Classifications are correctly applied
- [ ] Technical details are accurate
- [ ] Business impacts are validated
- [ ] Recommendations are actionable
- [ ] Distribution list is appropriate
- [ ] Format matches audience needs
- [ ] Follow-up actions are assigned
- [ ] Contact information is current
- [ ] References and sources are included

## Related Documents
- [Threat Intelligence Research and Reporting Runbook](run_books/threat_intelligence_briefing.md)
- [Reporting Templates](reporting_templates.md)
- [Strategic Threat Assessment](run_books/strategic_threat_assessment.md)
- [Threat Intelligence Workflows](run_books/threat_intel_workflows.md)