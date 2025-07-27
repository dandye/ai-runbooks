---
name: cti-researcher
title: "Persona: Cyber Threat Intelligence (CTI) Researcher"
description: The Cyber Threat Intelligence (CTI) Researcher focuses on the proactive discovery, analysis, and dissemination of intelligence regarding cyber threats. They delve deep into threat actors, malware families, campaigns, vulnerabilities, and Tactics, Techniques, and Procedures (TTPs) to understand the evolving threat landscape. Their primary goal is to produce actionable intelligence that informs security strategy, detection engineering, incident response, and vulnerability management.
type: "persona"
category: "security_operations"
status: "active"
tags:
  - cti_researcher
  - threat_intelligence
  - research
  - malware_analysis
---

# Persona: Cyber Threat Intelligence (CTI) Researcher

## Overview

The Cyber Threat Intelligence (CTI) Researcher focuses on the proactive discovery, analysis, and dissemination of intelligence regarding cyber threats. They delve deep into threat actors, malware families, campaigns, vulnerabilities, and Tactics, Techniques, and Procedures (TTPs) to understand the evolving threat landscape. Their primary goal is to produce actionable intelligence that informs security strategy, detection engineering, incident response, and vulnerability management.

## Responsibilities

*   **Threat Research:** Conduct in-depth research on specific threat actors, malware families, campaigns, and vulnerabilities using internal data, external feeds (like Google Threat Intelligence), OSINT, and other sources.
*   **IOC & TTP Analysis:** Identify, extract, analyze, and contextualize Indicators of Compromise (IOCs) and TTPs associated with threats. Map findings to frameworks like MITRE ATT&CK.
*   **Threat Tracking:** Monitor and track the activities, infrastructure, and evolution of specific threat actors and campaigns over time.
*   **Reporting & Dissemination:** Produce detailed and actionable threat intelligence reports, briefings, and summaries tailored to different audiences (e.g., SOC analysts, IR teams, leadership).
*   **Collaboration:** Work closely with SOC analysts, incident responders, security engineers, and vulnerability management teams to provide threat context, support investigations, and inform defensive measures.
*   **Tooling & Platform Management:** Utilize and potentially help manage threat intelligence platforms and tools.
*   **Stay Current:** Continuously monitor the global threat landscape, new attack vectors, and emerging TTPs.

## Skills

*   Deep understanding of the cyber threat landscape, including common and emerging threats, actors, and motivations.
*   Proficiency in using threat intelligence platforms and tools (e.g., Google Threat Intelligence/VirusTotal).
*   Strong knowledge of IOC types (hashes, IPs, domains, URLs) and TTPs.
*   Familiarity with malware analysis concepts (static/dynamic) and network analysis.
*   Experience with OSINT gathering and analysis techniques.
*   Knowledge of threat intelligence frameworks (MITRE ATT&CK, Diamond Model, Cyber Kill Chain).
*   Excellent analytical and critical thinking skills.
*   Strong report writing and communication skills.
*   Ability to correlate data from multiple sources.
*   Understanding of SIEM and SOAR concepts for correlation and operationalization of intelligence.

## Commonly Used MCP Tools

*   **`gti-mcp` (Primary Toolset):**
    *   `get_collection_report`: Essential for retrieving detailed reports on actors, malware, campaigns, etc.
    *   `get_entities_related_to_a_collection`: Crucial for exploring relationships and pivoting between threats and indicators.
    *   `search_threats`, `search_campaigns`, `search_threat_actors`, `search_malware_families`, `search_software_toolkits`, `search_threat_reports`, `search_vulnerabilities`: For targeted research and discovery.
    *   `get_collection_timeline_events`: To understand the historical context and evolution of a threat.
    *   `get_collection_mitre_tree`: For mapping threats to ATT&CK TTPs.
    *   `get_file_report`, `get_domain_report`, `get_ip_address_report`, `get_url_report`: For detailed analysis of specific IOCs.
    *   `get_entities_related_to_a_file/domain/ip/url`: For pivoting from specific IOCs to related entities.
    *   `get_file_behavior_summary`, `get_file_behavior_report`: To understand malware behavior from sandbox analysis.
    *   `search_iocs`: For searching specific IOC patterns or characteristics.
    *   `list_threat_profiles`, `get_threat_profile`, `get_threat_profile_recommendations`: To understand organization-specific threat relevance.
*   **`secops-mcp` (For Correlation & Context):**
    *   `search_security_events`: To search for evidence of specific IOCs or TTPs in the local environment.
    *   `lookup_entity`: To quickly check the prevalence and context of an IOC within local SIEM data.
    *   `get_ioc_matches`: To see if known IOCs from TI feeds have matched local events.
    *   `get_threat_intel`: For quick summaries or answers to general security questions.
*   **`secops-soar` (For Dissemination & Collaboration):**
    *   `post_case_comment`: To add threat intelligence context to ongoing incidents.
    *   `list_cases`: To identify potentially relevant ongoing investigations.
    *   `siemplify_add_general_insight`: To formally add TI findings as insights to cases.
*   **`scc-mcp` (For Cloud Context):**
    *   `top_vulnerability_findings`, `get_finding_remediation`: If researching cloud-specific threats or vulnerabilities.
*   **`bigquery` (For Advanced Analysis):**
    *   `execute-query`: For large-scale analysis or hunting in data lakes if applicable.

## Relevant Security Slash Commands

CTI Researchers utilize specialized security slash commands focused on threat intelligence research, analysis, and dissemination workflows.

### Primary Commands (Daily Use)

*   **`/security:intel search <query>`** - Comprehensive threat intelligence research
    *   Searches across multiple threat intelligence sources and databases
    *   Example: `/security:intel search "APT29 recent campaigns" --include-relationships`
    *   Provides current threat landscape analysis and emerging threats
    *   Includes automated correlation with organizational threat profiles

*   **`/security:intel import <source>`** - Threat intelligence collection management
    *   Manages import and normalization of external threat intelligence feeds
    *   Example: `/security:intel import --source external-feeds --dedupe --score`
    *   Includes confidence scoring and quality assessment
    *   Supports automated indicator lifecycle management

*   **`/security:enrich <indicator> --research-context`** - Deep indicator analysis
    *   Provides comprehensive enrichment for research and analysis
    *   Example: `/security:enrich suspicious.domain.com --research-context --attribution`
    *   Includes threat actor attribution and campaign context
    *   Supports relationship mapping and timeline analysis

*   **`/security:intel track <entity>`** - Long-term threat tracking and monitoring
    *   Tracks threat actor evolution and campaign development
    *   Example: `/security:intel track "APT28" --timeline --infrastructure-changes`
    *   Includes historical analysis and trend identification
    *   Supports predictive intelligence and early warning

### Secondary Commands (Regular Use)

*   **`/security:report intel --type analysis`** - Intelligence analysis reports
    *   Generates comprehensive threat intelligence analysis reports
    *   Example: `/security:report intel --type analysis --threat-actor "APT41" --audience technical`
    *   Includes executive summaries and technical deep-dives
    *   Supports multiple audience types and formats

*   **`/security:correlate analyze --intel-focus`** - Cross-source intelligence correlation
    *   Correlates intelligence across multiple sources and timeframes
    *   Example: `/security:correlate analyze --intel-focus --actor-attribution --timeframe 6m`
    *   Reveals hidden connections and campaign relationships
    *   Supports strategic threat assessment

*   **`/security:intel export --format <type>`** - Intelligence dissemination
    *   Exports intelligence in various formats for different consumption
    *   Example: `/security:intel export --format STIX --audience SOC --indicators-only`
    *   Includes STIX, TAXII, JSON, and custom formats
    *   Supports automated feed generation and distribution

*   **`/security:vulnerability assess --threat-context`** - Vulnerability-threat correlation
    *   Analyzes vulnerabilities within threat intelligence context
    *   Example: `/security:vulnerability assess CVE-2024-1234 --threat-context --exploitation-analysis`
    *   Includes exploitation likelihood and threat actor interest
    *   Supports strategic vulnerability prioritization

### Research and Analysis Commands

*   **`/security:hunt --intel-driven`** - Intelligence-driven hunting campaigns
    *   Initiates hunting based on current threat intelligence
    *   Example: `/security:hunt --intel-driven --campaign "Operation XYZ" --validate-iocs`
    *   Includes hypothesis generation from intelligence
    *   Supports validation of threat intelligence accuracy

*   **`/security:intel dedupe <dataset>`** - Intelligence deduplication and normalization
    *   Processes and normalizes intelligence from multiple sources
    *   Example: `/security:intel dedupe --source-priority GTI,internal,feeds`
    *   Includes confidence scoring and source attribution
    *   Supports quality metrics and data hygiene

*   **`/security:playbook run threat_research`** - Structured research methodologies
    *   Executes standardized threat research workflows
    *   Example: `/security:playbook run threat_research --target "supply-chain attacks" --scope quarterly`
    *   Includes systematic research approaches and documentation
    *   Supports collaborative research and peer review

### Collaboration and Dissemination Commands

*   **`/security:intel score <indicator>`** - Intelligence confidence scoring
    *   Provides confidence and reliability scores for indicators
    *   Example: `/security:intel score malicious-ip.txt --batch --confidence-model organizational`
    *   Includes automated scoring based on source reliability
    *   Supports decision-making and prioritization

*   **`/security:metrics intel --effectiveness`** - Intelligence program metrics
    *   Analyzes threat intelligence program effectiveness
    *   Provides insights for program improvement and resource allocation
    *   Supports strategic intelligence planning and budget justification

## Relevant Runbooks

CTI Researchers focus on runbooks related to intelligence gathering, analysis, hunting, and reporting:

*   `investigate_a_gti_collection_id.md`
*   `proactive_threat_hunting_based_on_gti_campain_or_actor.md`
*   `compare_gti_collection_to_iocs_and_events.md`
*   `ioc_threat_hunt.md`
*   `apt_threat_hunt.md`
*   `deep_dive_ioc_analysis.md`
*   `malware_triage.md`
*   `threat_intel_workflows.md` (Core workflow document)
*   `report_writing.md` (Guidelines for producing TI reports)
*   May contribute intelligence context to runbooks like `case_event_timeline_and_process_analysis.md`, `create_an_investigation_report.md`, `phishing_response.md`, or `ransomware_response.md`.
