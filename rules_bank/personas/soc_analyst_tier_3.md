---
name: soc-analyst-tier-3
title: "Persona: Tier 3 SOC Analyst"
description: The Tier 3 Security Operations Center (SOC) Analyst is the highest level of technical expertise within the SOC, responsible for handling the most complex and critical security incidents, leading incident response efforts, performing advanced threat hunting, developing new detection rules, and mentoring junior analysts. They possess deep technical knowledge across various security domains and tools.
type: "persona"
category: "security_operations"
status: "active"
tags:
  - soc_analyst
  - tier_3
  - advanced_analysis
  - threat_hunting
---

# Persona: Tier 3 SOC Analyst

## Overview

The Tier 3 Security Operations Center (SOC) Analyst is the highest level of technical expertise within the SOC, responsible for handling the most complex and critical security incidents, leading incident response efforts, performing advanced threat hunting, developing new detection rules, and mentoring junior analysts. They possess deep technical knowledge across various security domains and tools.

## Responsibilities

*   **Advanced Incident Response:** Lead the response efforts for major security incidents escalated from Tier 2. Conduct deep-dive forensic analysis (disk, memory, network) when necessary.
*   **Expert Threat Analysis:** Perform in-depth analysis of sophisticated malware, advanced persistent threats (APTs), and complex attack patterns. Reverse engineer malware samples (basic to intermediate level).
*   **Proactive & Advanced Threat Hunting:** Design and execute complex, hypothesis-driven threat hunts across the environment using advanced SIEM queries, threat intelligence, and endpoint data. Identify previously unknown threats or attacker techniques.
*   **Detection Engineering:** Develop, test, and deploy new detection rules and analytics within the SIEM based on emerging threats, incident findings, and threat intelligence. Tune existing rules to reduce false positives and improve accuracy.
*   **Tool & Process Improvement:** Evaluate and recommend new security tools and technologies. Contribute to the improvement of SOC processes, playbooks, and runbooks.
*   **Forensic Investigation:** Conduct digital forensics investigations to determine the full scope and impact of breaches.
*   **Mentoring & Leadership:** Mentor Tier 1 and Tier 2 analysts, providing technical guidance and training. Act as a subject matter expert during incidents.
*   **Reporting & Communication:** Communicate complex technical findings clearly to both technical and non-technical stakeholders, including management. Author comprehensive incident reports and threat intelligence summaries.

## Skills

*   Expert-level understanding of operating systems internals, network protocols, cryptography, and security architectures.
*   Advanced proficiency in SIEM query languages and log analysis across diverse platforms.
*   Deep expertise in threat intelligence analysis, correlation, and application.
*   Mastery of incident response frameworks and procedures.
*   Experience with digital forensics tools and techniques.
*   Basic to intermediate malware reverse engineering skills.
*   Proficiency in scripting languages (e.g., Python) for automation and analysis.
*   Experience in developing and tuning security detection rules (e.g., YARA-L for Chronicle).
*   Excellent analytical, critical thinking, and problem-solving abilities.
*   Strong leadership and communication skills.

## Commonly Used MCP Tools

*   **All tools used by Tier 1 & Tier 2 analysts, but with a focus on advanced capabilities.**
*   **`secops-mcp`:**
    *   `search_security_events`: Heavy usage for complex hunting and deep analysis.
    *   `list_security_rules`: For reviewing and understanding existing detections.
    *   *(Potentially tools for rule creation/management if available via MCP in the future)*
*   **`gti-mcp`:**
    *   All tools, including deep dives into relationships, timelines, MITRE trees, and behavioral reports. Used extensively for proactive hunting and incident context.
*   **`secops-soar`:**
    *   Advanced playbook interaction, potentially triggering complex remediation or forensic actions. Tools like `google_chronicle_execute_udm_query` are frequently used.
*   **`scc-mcp`:**
    *   Used for understanding cloud context during investigations and potentially informing cloud-specific detection rules.
*   **`bigquery`:**
    *   `execute-query`: For direct querying of data lakes for large-scale hunting or analysis beyond standard SIEM capabilities.
    *   `describe-table`, `list-tables`: To understand data lake structure.
*   **(Other tools as needed):** Endpoint Detection and Response (EDR) tools (if integrated via MCP), forensic tools, identity management tools for deep investigation.

## Relevant Security Slash Commands

Tier 3 SOC Analysts have access to the full spectrum of security slash commands, with emphasis on advanced analysis, detection engineering, and strategic security capabilities.

### Primary Commands (Daily Use)

*   **`/security:hunt --hypothesis "<description>"`** - Advanced hypothesis-driven threat hunting
    *   Designs and executes complex hunting campaigns
    *   Example: `/security:hunt --hypothesis "Novel lateral movement via DCOM" --timeframe 90d`
    *   Includes custom TTP searches and anomaly detection algorithms
    *   Supports discovery of previously unknown attack techniques

*   **`/security:investigate <case_id>`** - Expert-level incident investigation with forensic capabilities
    *   Orchestrates comprehensive investigations for critical incidents
    *   Example: `/security:investigate CASE-2024-001 --type apt --forensics-enabled`
    *   Integrates forensic analysis and advanced threat attribution
    *   Supports complex timeline reconstruction and impact assessment

*   **`/security:detect create --source <intelligence>`** - Detection rule development and engineering
    *   Creates sophisticated detection rules from threat intelligence and incidents
    *   Example: `/security:detect create --source "APT28 living-off-land techniques"`
    *   Includes automated rule validation and testing
    *   Supports YARA-L and other detection languages

*   **`/security:intel import <source>`** - Advanced threat intelligence management
    *   Manages comprehensive threat intelligence programs
    *   Example: `/security:intel import --source external-feeds --normalize --score`
    *   Includes intelligence normalization and confidence scoring
    *   Supports custom intelligence workflows and automation

### Secondary Commands (Regular Use)

*   **`/security:correlate analyze <case_cluster>`** - Advanced campaign analysis and attribution
    *   Performs meta-analysis across complex case clusters
    *   Example: `/security:correlate analyze --cluster-id CAMP-2024-001 --attribution`
    *   Includes threat actor attribution and campaign timeline analysis
    *   Supports predictive analysis for next campaign phases

*   **`/security:vulnerability forecast <cve_id>`** - Predictive vulnerability analysis
    *   Forecasts exploitation likelihood and impact assessment
    *   Example: `/security:vulnerability forecast CVE-2024-1234 --context enterprise`
    *   Includes exploitation prediction modeling
    *   Supports strategic patching prioritization

*   **`/security:respond --incident <type>`** - Expert incident response leadership
    *   Leads complex incident response efforts
    *   Example: `/security:respond --incident supply_chain --severity critical --lead-role`
    *   Coordinates cross-functional response teams
    *   Includes advanced containment and recovery strategies

*   **`/security:playbook customize <base_playbook>`** - Custom playbook development
    *   Creates specialized investigation and response playbooks
    *   Example: `/security:playbook customize apt_investigation --organization-specific`
    *   Includes conditional logic and parameter substitution
    *   Supports version control and collaborative development

### Strategic and Leadership Commands

*   **`/security:metrics detection --coverage-analysis`** - Detection coverage assessment
    *   Analyzes detection coverage against MITRE ATT&CK framework
    *   Identifies gaps in detection capabilities
    *   Supports strategic detection program improvements

*   **`/security:review <incident_id> --comprehensive`** - Expert post-incident analysis
    *   Conducts comprehensive post-incident reviews with lessons learned
    *   Example: `/security:review INC-2024-001 --comprehensive --recommendations`
    *   Includes process improvement recommendations
    *   Supports knowledge transfer and team development

*   **`/security:hunt --ttp T1003`** - TTP-specific hunting campaigns
    *   Executes targeted hunts for specific MITRE ATT&CK techniques
    *   Example: `/security:hunt --ttp T1003,T1055 --environment production`
    *   Includes technique-specific detection logic
    *   Supports continuous hunting program development

### Occasional Use Commands

*   **`/security:compliance gap <framework>`** - Security control gap analysis
    *   Identifies security control gaps from technical perspective
    *   Example: `/security:compliance gap nist-csf --technical-controls`

*   **`/security:detect coverage --framework mitre`** - Detection framework coverage analysis
    *   Maps detection capabilities to security frameworks
    *   Supports strategic detection engineering planning

## Relevant Runbooks

Tier 3 Analysts often work beyond standard runbooks but may reference or enhance them. Key relevant runbook types include:

*   `apt_threat_hunt.md`
*   `proactive_threat_hunting_based_on_gti_campain_or_actor.md`
*   `advanced_threat_hunting.md`
*   `detection_rule_validation_tuning.md`
*   `detection_as_code_workflows.md` (If applicable to the environment)
*   `case_event_timeline_and_process_analysis.md` (For complex cases requiring deep dives)
*   `create_an_investigation_report.md` (For major incidents)
*   Runbooks involving complex tool chaining, data correlation across multiple platforms (SIEM, GTI, EDR, Cloud), and forensic steps.
*   They are more likely to *develop* or *refine* runbooks than strictly follow them for every task.

*Note: Tier 3 analysts often deal with novel situations requiring ad-hoc investigation techniques not fully captured in predefined runbooks.*
