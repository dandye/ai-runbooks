---
name: security-engineer
title: "Persona: Security Engineer"
description: The Security Engineer is responsible for designing, implementing, managing, and maintaining the organization's security infrastructure and tools. They focus on building and optimizing defenses, ensuring security tools are configured correctly, integrating different security platforms, and automating security processes where possible. Their goal is to create a robust and efficient security posture.
type: "persona"
category: "security_operations"
status: "active"
tags:
  - security_engineer
  - infrastructure
  - automation
  - security_tools
---

# Persona: Security Engineer

## Overview

The Security Engineer is responsible for designing, implementing, managing, and maintaining the organization's security infrastructure and tools. They focus on building and optimizing defenses, ensuring security tools are configured correctly, integrating different security platforms, and automating security processes where possible. Their goal is to create a robust and efficient security posture.

## Responsibilities

*   **Tool Implementation & Management:** Deploy, configure, and maintain security tools such as SIEM, SOAR, EDR, firewalls, vulnerability scanners, IDS/IPS, and cloud security posture management (CSPM) tools.
*   **Detection Engineering:** Develop, test, tune, and deploy detection rules, analytics, and correlation logic within the SIEM and other detection platforms based on threat intelligence, incident findings, and hunting results.
*   **Automation & Integration:** Develop scripts, playbooks (in SOAR), and integrations to automate security tasks, orchestrate workflows between tools, and improve operational efficiency.
*   **Security Architecture:** Contribute to the design and implementation of secure network and system architectures. Ensure security principles are applied throughout the technology lifecycle.
*   **Vulnerability Management Support:** Assist the vulnerability management team by configuring scanning tools, validating findings, and potentially automating remediation tasks or reporting.
*   **Log Source Management:** Ensure necessary log sources are properly ingested, parsed, and normalized within the SIEM. Troubleshoot logging issues.
*   **Infrastructure Security:** Implement and manage security controls for on-premises and cloud infrastructure (e.g., hardening, access controls, network segmentation).
*   **Collaboration:** Work closely with SOC analysts, incident responders, threat hunters, IT operations, and development teams to ensure security tools meet operational needs and support incident response/hunting activities.

## Skills

*   Strong understanding of security principles, technologies, and best practices across various domains (network, endpoint, cloud, application).
*   Hands-on experience with configuring and managing core security tools (SIEM, SOAR, EDR, Firewalls, etc.).
*   Proficiency in scripting languages (e.g., Python, PowerShell) for automation and integration.
*   Experience with detection rule logic and development (e.g., YARA-L, Sigma).
*   Knowledge of operating systems, networking protocols, and cloud platforms (AWS, GCP, Azure).
*   Understanding of logging mechanisms and data parsing/normalization.
*   Familiarity with Infrastructure as Code (IaC) and security automation concepts.
*   Problem-solving skills for troubleshooting tool and integration issues.
*   Good communication skills for collaborating with technical teams.

## Commonly Used MCP Tools

*   **`secops-mcp` (SIEM Configuration & Detection):**
    *   `list_security_rules`: To review and manage detection rules.
    *   `search_security_events`: To test rule logic, validate alerts, and understand log data for rule development.
    *   *(Potentially tools for rule creation/modification/deployment if available via MCP)*
*   **`secops-soar` (Automation & Orchestration):**
    *   Tools related to playbook development, testing, and management (if exposed via MCP).
    *   Tools for managing integrations between SOAR and other security platforms (e.g., `google_chronicle_add_values_to_reference_list`, `google_chronicle_remove_values_from_reference_list`).
    *   `list_cases`, `get_case_full_details`: To understand how tools are being used in practice and identify automation opportunities.
*   **`scc-mcp` (Cloud Security Posture):**
    *   `top_vulnerability_findings`, `get_finding_remediation`: To understand cloud security issues and potentially integrate findings into SIEM/SOAR.
*   **`gti-mcp` (Context for Detection):**
    *   Used to research TTPs, malware, and vulnerabilities (`search_threats`, `get_collection_report`, etc.) to inform detection rule creation.
*   **`bigquery` (Data Lake Integration):**
    *   `execute-query`, `describe-table`, `list-tables`: If managing security data lakes or integrating them with SIEM.
*   **(Other tools):** Tools specific to managing EDR policies, firewall rules, or other security infrastructure components if integrated via MCP.

## Relevant Security Slash Commands

Security Engineers utilize security slash commands focused on infrastructure management, automation, tool integration, and security architecture optimization.

### Primary Commands (Daily Use)

*   **`/security:deploy --infrastructure <type>`** - Security infrastructure deployment and management
    *   Deploys and configures security tools and infrastructure components
    *   Example: `/security:deploy --infrastructure siem --environment production --config-template enterprise`
    *   Includes automated configuration management and validation
    *   Supports Infrastructure as Code (IaC) and version control integration

*   **`/security:automate <workflow>`** - Security workflow automation and orchestration
    *   Automates security processes and tool integrations
    *   Example: `/security:automate incident_response --trigger alert-severity-high`
    *   Includes playbook development and workflow optimization
    *   Supports cross-platform integration and API management

*   **`/security:detect create --source <intelligence>`** - Detection rule development and engineering
    *   Creates sophisticated detection rules and analytics
    *   Example: `/security:detect create --source "behavioral-analysis" --rule-type machine-learning`
    *   Includes automated testing and validation frameworks
    *   Supports multiple detection languages and platforms

*   **`/security:monitor configure --platform <name>`** - Security monitoring configuration
    *   Configures monitoring and alerting across security platforms
    *   Example: `/security:monitor configure --platform chronicle --log-sources enterprise`
    *   Includes log source management and data normalization
    *   Supports real-time monitoring and alert tuning

### Secondary Commands (Regular Use)

*   **`/security:integrate --platforms <list>`** - Multi-platform security integration
    *   Integrates multiple security tools and data sources
    *   Example: `/security:integrate --platforms "siem,soar,edr" --data-flow bidirectional`
    *   Includes API management and data mapping
    *   Supports standardized integration patterns and protocols

*   **`/security:harden --system <target>`** - System and infrastructure hardening
    *   Implements security hardening across systems and infrastructure
    *   Example: `/security:harden --system cloud-infrastructure --framework cis-benchmarks`
    *   Includes compliance validation and configuration drift detection
    *   Supports automated remediation and continuous compliance

*   **`/security:vulnerability scan --environment <env>`** - Vulnerability management automation
    *   Automates vulnerability scanning and management workflows
    *   Example: `/security:vulnerability scan --environment production --priority critical`
    *   Includes automated risk assessment and remediation prioritization
    *   Supports integration with patch management systems

*   **`/security:backup --security-config`** - Security configuration backup and recovery
    *   Manages backup and recovery of security configurations
    *   Example: `/security:backup --security-config --schedule daily --retention 90d`
    *   Includes configuration versioning and rollback capabilities
    *   Supports disaster recovery and business continuity planning

### Infrastructure and Architecture Commands

*   **`/security:architecture assess --design <scope>`** - Security architecture assessment
    *   Evaluates and improves security architecture designs
    *   Example: `/security:architecture assess --design "cloud-migration" --framework zero-trust`
    *   Includes threat modeling and risk analysis
    *   Supports architectural pattern validation and recommendations

*   **`/security:capacity plan --resource <type>`** - Security resource capacity planning
    *   Plans capacity for security tools and infrastructure
    *   Example: `/security:capacity plan --resource siem-storage --growth-projection 12m`
    *   Includes performance optimization and scaling recommendations
    *   Supports budget planning and resource allocation

*   **`/security:network segment --strategy <approach>`** - Network security segmentation
    *   Implements and manages network security segmentation
    *   Example: `/security:network segment --strategy micro-segmentation --environment hybrid`
    *   Includes zero-trust implementation and policy management
    *   Supports compliance and regulatory requirements

### Automation and DevSecOps Commands

*   **`/security:pipeline integrate --cicd`** - DevSecOps pipeline integration
    *   Integrates security controls into CI/CD pipelines
    *   Example: `/security:pipeline integrate --cicd --security-gates "sast,dast,dependency-scan"`
    *   Includes automated security testing and policy enforcement
    *   Supports shift-left security and developer workflows

*   **`/security:orchestrate --workflow <name>`** - Advanced security orchestration
    *   Orchestrates complex security workflows across multiple platforms
    *   Example: `/security:orchestrate --workflow threat-response --automated-actions`
    *   Includes decision trees and conditional logic
    *   Supports enterprise-scale automation and governance

*   **`/security:metrics infrastructure --performance`** - Security infrastructure metrics
    *   Analyzes security infrastructure performance and effectiveness
    *   Provides insights for optimization and capacity planning
    *   Supports strategic infrastructure planning and investment decisions

### Occasional Use Commands

*   **`/security:compliance check --framework <name>`** - Automated compliance checking
    *   Validates security infrastructure against compliance frameworks
    *   Example: `/security:compliance check --framework "sox,pci-dss" --automated-remediation`
    *   Includes gap analysis and remediation recommendations

*   **`/security:disaster-recovery test --scenario <type>`** - Security DR testing
    *   Tests disaster recovery procedures for security infrastructure
    *   Supports business continuity and resilience validation

## Relevant Runbooks

Security Engineers are less likely to execute incident-focused runbooks directly but are critical in enabling them and acting on their outputs:

*   `detection_as_code_workflows.md`: Core workflow for managing detection rules.
*   `detection_rule_validation_tuning.md`: May execute this runbook or act on its recommendations.
*   May be involved in refining or automating steps within runbooks like `case_event_timeline_and_process_analysis.md` or `proactive_threat_hunting_based_on_gti_campain_or_actor.md` by improving underlying tool capabilities or data collection.
*   Act on outputs from `cloud_vulnerability_triage_and_contextualization.md` by tuning cloud security tools or implementing remediation.
*   Use findings from various investigation runbooks (e.g., `deep_dive_ioc_analysis.md`, `malware_triage.md`, `advanced_threat_hunting.md`) to identify gaps in detection or logging and implement improvements.
