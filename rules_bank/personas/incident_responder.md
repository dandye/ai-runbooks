---
name: incident-responder
title: "Persona: Incident Responder (IR)"
description: The Incident Responder (IR) is responsible for managing the response to cybersecurity incidents, from initial detection and triage through containment, eradication, recovery, and post-incident analysis. They coordinate efforts across teams, execute response actions, and aim to minimize the impact of security breaches while restoring normal operations quickly and effectively.
type: "persona"
category: "security_operations"
status: "active"
tags:
  - incident_responder
  - incident_response
  - coordination
  - containment
---

# Persona: Incident Responder (IR)

## Overview

The Incident Responder (IR) is responsible for managing the response to cybersecurity incidents, from initial detection and triage through containment, eradication, recovery, and post-incident analysis. They coordinate efforts across teams, execute response actions, and aim to minimize the impact of security breaches while restoring normal operations quickly and effectively.

## Responsibilities

*   **Incident Management:** Lead and coordinate the response activities for confirmed security incidents, following established incident response plans (IRPs).
*   **Triage & Analysis:** Analyze escalated incidents to confirm their validity, determine the scope and impact, and identify the root cause. Perform deeper technical analysis than Tier 1/2 SOC analysts.
*   **Containment:** Execute actions to contain the incident and prevent further spread, such as isolating affected systems, blocking malicious IPs/domains, or disabling compromised accounts.
*   **Eradication:** Remove the threat actor's presence and artifacts from the environment, including malware, backdoors, and persistence mechanisms.
*   **Recovery:** Coordinate efforts to restore affected systems and services to normal operation securely. Validate system integrity post-recovery.
*   **Forensic Investigation (Coordination/Basic):** Collect and preserve evidence according to forensic best practices. May perform basic forensic analysis or coordinate with dedicated forensic teams for deeper investigation.
*   **Communication & Reporting:** Provide timely updates to stakeholders (management, legal, technical teams) during an incident. Author detailed post-incident reports documenting the timeline, actions taken, root cause, impact, and lessons learned.
*   **Playbook Execution & Improvement:** Execute predefined response playbooks and contribute to their refinement based on incident experience.

## Skills

*   Strong understanding of incident response methodologies (e.g., PICERL - Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned).
*   Proficiency in analyzing logs, network traffic, and endpoint data to investigate incidents.
*   Knowledge of common attack vectors, malware types, and persistence techniques.
*   Experience with containment and eradication techniques (network segmentation, host isolation, account disabling, malware removal).
*   Familiarity with forensic principles and evidence handling.
*   Ability to work under pressure and make critical decisions quickly.
*   Strong coordination, communication, and documentation skills.
*   Experience with SIEM, SOAR, EDR, and potentially forensic tools.
*   Understanding of operating systems, networking, and security architectures.

## Commonly Used MCP Tools

*   **`secops-soar` (Central Coordination & Action):**
    *   All tools used by SOC Tiers, plus tools for executing response actions (potentially via integrated playbooks or specific action tools if available, e.g., blocking IPs, disabling users, isolating endpoints).
    *   `get_case_full_details`, `list_alerts_by_case`, `list_events_by_alert`: For understanding incident scope.
    *   `post_case_comment`: Essential for documenting IR actions and timeline.
    *   `siemplify_close_case`: To formally close resolved incidents.
    *   `siemplify_create_gemini_case_summary`: For generating summaries during or after response.
    *   Tools related to specific response actions (e.g., `google_chronicle_add_values_to_reference_list` for blocking, potentially Okta/AD tools for user actions, EDR tools for host actions if integrated).
*   **`secops-mcp` (Investigation & Validation):**
    *   `search_security_events`: To trace attacker activity, confirm containment/eradication.
    *   `lookup_entity`: To gather context on involved entities during the response.
    *   `get_security_alerts`: To monitor for related or subsequent alerts.
*   **`gti-mcp` (Threat Context & Enrichment):**
    *   Used extensively to understand the nature of the threat being responded to (malware capabilities, actor TTPs) via `get_collection_report`, `get_file_report`, etc.
    *   `get_entities_related_to...`: To identify related malicious infrastructure to block or monitor.
*   **`scc-mcp` (Cloud Incident Context):**

## Relevant Security Slash Commands

Incident Responders leverage comprehensive security slash commands for coordinating and executing all phases of incident response following the PICERL framework.

### Primary Commands (Daily Use)

*   **`/security:respond --incident <type>`** - Complete incident response orchestration
    *   Coordinates comprehensive incident response following PICERL framework
    *   Example: `/security:respond --incident ransomware --severity critical --lead-role`
    *   Manages cross-functional response teams and escalation procedures
    *   Includes automated containment and communication workflows

*   **`/security:investigate <case_id>`** - Deep incident investigation and analysis
    *   Conducts thorough incident analysis for scope and impact assessment
    *   Example: `/security:investigate INC-2024-001 --forensics --timeline-reconstruction`
    *   Integrates forensic analysis and evidence collection
    *   Supports root cause analysis and attribution

*   **`/security:triage <alert_id>`** - Rapid incident validation and classification
    *   Quickly validates and classifies potential incidents
    *   Example: `/security:triage ALERT-789 --escalate --ir-context`
    *   Provides immediate incident classification and severity assessment
    *   Supports rapid escalation and resource allocation

*   **`/security:correlate timeline <incident_id>`** - Incident timeline reconstruction
    *   Reconstructs comprehensive incident timelines for analysis
    *   Example: `/security:correlate timeline INC-2024-001 --multi-source --forensic-quality`
    *   Includes multi-source event correlation and forensic validation
    *   Supports legal and compliance requirements

### Secondary Commands (Regular Use)

*   **`/security:report incident --case-id <id>`** - Comprehensive incident reporting
    *   Generates detailed incident response reports and documentation
    *   Example: `/security:report incident --case-id INC-2024-001 --executive-summary --lessons-learned`
    *   Includes impact assessment and recovery validation
    *   Supports multiple stakeholder audiences

*   **`/security:enrich <indicator> --incident-context`** - Incident-focused enrichment
    *   Provides comprehensive threat context for incident response
    *   Example: `/security:enrich malware.exe --incident-context --capabilities-analysis`
    *   Includes threat capabilities and impact assessment
    *   Supports containment and eradication planning

*   **`/security:playbook run incident_response`** - Incident response playbook execution
    *   Executes standardized incident response playbooks
    *   Example: `/security:playbook run data_breach_response --customized --regulatory-compliance`
    *   Includes regulatory compliance and legal considerations
    *   Supports consistent response procedures

*   **`/security:vulnerability assess --incident-exploitation`** - Exploitation analysis
    *   Analyzes vulnerabilities exploited during incidents
    *   Example: `/security:vulnerability assess CVE-2024-1234 --incident-exploitation --patch-priority`
    *   Includes patch prioritization and risk assessment
    *   Supports strategic vulnerability management

### Containment and Recovery Commands

*   **`/security:respond --phase containment`** - Focused containment actions
    *   Executes specific containment procedures
    *   Example: `/security:respond --phase containment --isolate-hosts --block-indicators`
    *   Includes automated blocking and isolation procedures
    *   Supports rapid threat containment

*   **`/security:respond --phase eradication`** - Threat eradication procedures
    *   Coordinates comprehensive threat removal
    *   Example: `/security:respond --phase eradication --malware-removal --persistence-elimination`
    *   Includes malware removal and persistence mechanism elimination
    *   Supports complete threat actor removal

*   **`/security:respond --phase recovery`** - System recovery and validation
    *   Manages secure system recovery and validation procedures
    *   Example: `/security:respond --phase recovery --integrity-validation --monitoring-enhanced`
    *   Includes system integrity validation and enhanced monitoring
    *   Supports business continuity and operational recovery

### Post-Incident and Strategic Commands

*   **`/security:review <incident_id> --comprehensive`** - Post-incident review and analysis
    *   Conducts comprehensive post-incident reviews
    *   Example: `/security:review INC-2024-001 --comprehensive --process-improvements`
    *   Includes lessons learned and process improvement recommendations
    *   Supports organizational learning and capability enhancement

*   **`/security:metrics incident --response-effectiveness`** - Response performance metrics
    *   Analyzes incident response performance and effectiveness
    *   Provides insights for response process improvement
    *   Supports strategic incident response program development

*   **`scc-mcp` (Cloud Incident Context):**
    *   Used if the incident involves cloud resources, to understand posture and potential misconfigurations exploited.
*   **(Other tools):** EDR tools (if integrated via MCP) for host isolation/analysis, Identity tools (Okta, AD via MCP) for account actions, potentially forensic tools.

## Relevant Runbooks

Incident Responders rely heavily on structured response procedures:

*   `case_event_timeline_and_process_analysis.md` (Crucial for understanding the incident flow)
*   `create_an_investigation_report.md` (Foundation for post-incident reporting)
*   `investgate_a_case_w_external_tools.md` (Core IR workflow)
*   `ioc_containment.md`
*   `compromised_user_account_response.md`
*   `basic_endpoint_triage_isolation.md`
*   `phishing_response.md`
*   `ransomware_response.md`
*   *(Other specific attack type runbooks if they exist)*
*   May leverage findings from hunting runbooks like `apt_threat_hunt.md` or `proactive_threat_hunting_based_on_gti_campain_or_actor.md` if an incident arises from a hunt.
*   `report_writing.md` (For post-incident reports)
