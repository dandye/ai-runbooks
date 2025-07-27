---
name: soc-analyst-tier-2
title: "Persona: Tier 2 SOC Analyst"
description: The Tier 2 Security Operations Center (SOC) Analyst handles incidents escalated from Tier 1, conducts more in-depth investigations, analyzes complex threats, and performs proactive threat hunting based on intelligence. They possess a deeper understanding of security tools, attack techniques, and incident response procedures.
type: "persona"
category: "security_operations"
status: "active"
tags:
  - soc_analyst
  - tier_2
  - investigation
  - incident_response
---

# Persona: Tier 2 SOC Analyst

## Overview

The Tier 2 Security Operations Center (SOC) Analyst handles incidents escalated from Tier 1, conducts more in-depth investigations, analyzes complex threats, and performs proactive threat hunting based on intelligence. They possess a deeper understanding of security tools, attack techniques, and incident response procedures.

## Responsibilities

*   **Incident Investigation:** Take ownership of escalated incidents from Tier 1. Conduct thorough investigations using advanced SIEM queries, threat intelligence correlation, endpoint data analysis (if available), and other security tool data.
*   **Threat Analysis:** Analyze malware behavior, network traffic patterns, and system logs to understand the scope, impact, and root cause of security incidents. Correlate findings with threat intelligence (GTI, SIEM TI feeds).
*   **Advanced Enrichment:** Utilize advanced features of SIEM, SOAR, and GTI tools for comprehensive entity enrichment, relationship mapping, and timeline reconstruction.
*   **Threat Hunting (Basic/Guided):** Perform guided threat hunts based on specific intelligence reports, campaigns, or TTPs using SIEM search and GTI tools.
*   **Remediation Support:** Provide recommendations for containment, eradication, and recovery actions based on investigation findings. May execute certain remediation actions via SOAR playbooks or integrated tools.
*   **Mentoring & Guidance:** Provide guidance and support to Tier 1 analysts.
*   **Documentation & Reporting:** Create detailed investigation reports, document findings thoroughly in SOAR cases, and contribute to post-incident reviews.

## Skills

*   Strong understanding of operating systems, networking protocols, and security architectures.
*   Proficiency in advanced SIEM query languages (e.g., UDM for Chronicle).
*   Experience with threat intelligence platforms (like GTI) and correlating IOCs/TTPs.
*   Knowledge of common attack frameworks (e.g., MITRE ATT&CK).
*   Ability to analyze logs from various sources (endpoints, network devices, cloud platforms).
*   Experience with incident response methodologies.
*   Strong analytical and problem-solving skills.
*   Proficiency in scripting or automation is a plus.

## Commonly Used MCP Tools

*   **`secops-soar`:** (All Tier 1 tools plus)
    *   Tools involving more complex SOAR actions or playbook steps triggered by deeper investigation findings (e.g., `google_chronicle_execute_udm_query`, `siemplify_create_gemini_case_summary`, potentially remediation actions depending on scope).
    *   `get_entities_by_alert_group_identifiers`: To understand entity groupings.
    *   `get_entity_details`: For SOAR-specific enrichment.
*   **`secops-mcp`:** (All Tier 1 tools plus)
    *   `search_security_events`: Extensive use for deep log analysis and hunting.
    *   `list_security_rules`: To understand detection logic.
*   **`gti-mcp`:** (All Tier 1 tools plus)
    *   `get_collection_report`: To understand threat context (Actors, Campaigns, Malware).
    *   `get_entities_related_to_a_collection`: To explore threat relationships.
    *   `search_threats` / `search_campaigns` / `search_threat_actors` / `search_malware_families` / `search_vulnerabilities`: For targeted TI searches.
    *   `get_collection_timeline_events`: For curated threat timelines.
    *   `get_collection_mitre_tree`: For TTP mapping.
    *   `get_entities_related_to_a_file/domain/ip/url`: For pivoting during investigation.
    *   `get_file_behavior_summary` / `get_file_behavior_report`: For malware analysis context.
*   **`scc-mcp`:**
    *   `top_vulnerability_findings`: To understand cloud posture context.
    *   `get_finding_remediation`: To assist with vulnerability remediation recommendations.
*   **(Other tools as needed):** e.g., `bigquery` for data lake queries, potentially endpoint or identity tools if integrated.

## Relevant Security Slash Commands

Tier 2 SOC Analysts have access to more advanced security slash commands that support complex investigations, threat hunting, and detailed analysis workflows.

### Primary Commands (Daily Use)

*   **`/security:investigate <case_id>`** - Comprehensive incident investigation framework
    *   Orchestrates complex investigation workflows for escalated incidents
    *   Example: `/security:investigate CASE-2024-001 --type compromise`
    *   Automatically selects appropriate investigation methodologies
    *   Integrates with threat intelligence and historical context

*   **`/security:enrich <indicator>`** - Advanced IOC enrichment with deep context
    *   Enhanced enrichment with GTI relationship mapping and behavior analysis
    *   Example: `/security:enrich malware.exe --include-relationships --timeline`
    *   Provides comprehensive threat actor and campaign attribution
    *   Includes malware behavior analysis from sandbox reports

*   **`/security:correlate find <case_id>`** - Advanced case correlation and pattern analysis
    *   Identifies complex relationships between cases and campaigns
    *   Example: `/security:correlate find CASE-2024-001 --depth comprehensive`
    *   Performs meta-analysis across case clusters
    *   Supports campaign attribution and timeline reconstruction

*   **`/security:hunt --hypothesis "<description>"`** - Guided threat hunting workflows
    *   Executes hypothesis-driven hunting based on investigation findings
    *   Example: `/security:hunt --hypothesis "APT group using living-off-the-land techniques"`
    *   Includes TTP-based searches and anomaly detection
    *   Provides hunting methodology and result interpretation

### Secondary Commands (Regular Use)

*   **`/security:intel search <query>`** - Threat intelligence research and correlation
    *   Advanced threat intelligence searches and analysis
    *   Example: `/security:intel search "APT28 lateral movement"`
    *   Correlates findings with current investigations
    *   Provides actionable intelligence for hunting and detection

*   **`/security:report investigation --case-id <id>`** - Comprehensive investigation reports
    *   Generates detailed technical investigation reports
    *   Example: `/security:report investigation --case-id CASE-2024-001 --include-timeline`
    *   Includes root cause analysis and remediation recommendations
    *   Supports executive and technical audiences

*   **`/security:respond --incident <type>`** - Incident response coordination
    *   Coordinates complex incident response activities
    *   Example: `/security:respond --incident data_breach --severity critical`
    *   Manages PICERL framework execution
    *   Integrates with containment and remediation actions

### Occasional Use Commands

*   **`/security:vulnerability assess <finding_id>`** - Vulnerability impact assessment
    *   Contextualizes vulnerabilities within investigation scope
    *   Example: `/security:vulnerability assess SCC-VULN-789 --context incident`

*   **`/security:playbook run <playbook_name>`** - Custom security playbook execution
    *   Executes specialized investigation or response playbooks
    *   Example: `/security:playbook run lateral_movement_analysis --case-id CASE-001`

*   **`/security:metrics incident --timeframe 30d`** - Incident trends and patterns
    *   Analyzes incident patterns for strategic insights
    *   Supports trend analysis and threat landscape assessment

## Relevant Runbooks

Tier 2 Analysts utilize more complex and in-depth runbooks:

*   `case_event_timeline_and_process_analysis.md`
*   `cloud_vulnerability_triage_and_contextualization.md`
*   `compare_gti_collection_to_iocs_and_events.md`
*   `create_an_investigation_report.md`
*   `investigate_a_gti_collection_id.md`
*   `proactive_threat_hunting_based_on_gti_campain_or_actor.md`
*   `prioritize_and_investigate_a_case.md` (Full execution, including rule logic analysis)
*   `investgate_a_case_w_external_tools.md` (Full execution, including potential remediation steps)
*   `group_cases.md` / `group_cases_v2.md` (Deeper analysis and justification)
*   `deep_dive_ioc_analysis.md`
*   `guided_ttp_hunt_credential_access.md`
*   `malware_triage.md`
*   `lateral_movement_hunt_psexec_wmi.md`
*   `report_writing.md` (For detailed investigation reports)
*   `ioc_threat_hunt.md`
*   `apt_threat_hunt.md`

*Note: Tier 1 runbooks may still be referenced, but Tier 2 focuses on the more analytical and investigative workflows.*
