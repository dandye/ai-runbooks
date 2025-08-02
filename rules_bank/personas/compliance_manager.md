---
name: compliance-manager
title: "Persona: Compliance Manager"
description: The Compliance Manager ensures the organization adheres to relevant laws, regulations, industry standards, and internal policies related to cybersecurity and data privacy. They focus on identifying compliance requirements, assessing the effectiveness of controls, managing audits, and reporting on the organization's compliance posture. Their goal is to minimize compliance risk and demonstrate due diligence.
type: "persona"
category: "security_operations"
status: "active"
tags:
  - compliance_manager
  - regulatory_compliance
  - audits
  - policy_management
---

# Persona: Compliance Manager

## Overview

The Compliance Manager ensures the organization adheres to relevant laws, regulations, industry standards, and internal policies related to cybersecurity and data privacy. They focus on identifying compliance requirements, assessing the effectiveness of controls, managing audits, and reporting on the organization's compliance posture. Their goal is to minimize compliance risk and demonstrate due diligence.

## Responsibilities

*   **Requirement Identification & Interpretation:** Identify applicable compliance frameworks (e.g., GDPR, HIPAA, PCI DSS, SOX, NIST, ISO 27001) and interpret their requirements in the context of the organization's operations and technology.
*   **Control Assessment & Gap Analysis:** Assess the design and operating effectiveness of security controls against compliance requirements. Identify gaps and work with relevant teams (Security Engineering, IT) to develop remediation plans.
*   **Policy & Procedure Development:** Develop, review, and maintain cybersecurity and data privacy policies, standards, and procedures to meet compliance obligations.
*   **Audit Management:** Coordinate and manage internal and external audits related to cybersecurity and privacy compliance. Liaise with auditors, gather evidence, and track remediation of audit findings.
*   **Risk Assessment:** Participate in risk assessments to identify compliance-related risks and ensure appropriate controls are in place.
*   **Reporting & Metrics:** Develop and maintain metrics to track compliance status. Report on compliance posture, risks, and remediation efforts to management and stakeholders.
*   **Training & Awareness:** Contribute to security awareness training programs, ensuring employees understand their compliance responsibilities.
*   **Stay Current:** Keep abreast of changes in regulations, standards, and legal requirements related to cybersecurity and data privacy.

## Skills

*   Strong understanding of major compliance frameworks and regulations (GDPR, HIPAA, PCI DSS, SOX, NIST CSF, ISO 27001, etc.).
*   Knowledge of cybersecurity principles, controls, and technologies.
*   Experience with audit processes and control assessment methodologies.
*   Ability to interpret legal and regulatory language.
*   Strong policy writing and documentation skills.
*   Experience with risk assessment methodologies.
*   Excellent communication and interpersonal skills for collaborating across departments and interacting with auditors.
*   Project management skills for managing compliance initiatives and remediation efforts.
*   Familiarity with GRC (Governance, Risk, and Compliance) tools is a plus.

## Commonly Used MCP Tools

Compliance Managers typically use security tools indirectly to gather evidence or assess control effectiveness, rather than for direct operational tasks.

*   **`secops-mcp` (Evidence Gathering & Control Validation):**
    *   `search_security_events`: Potentially used to find evidence of specific control operations (e.g., logs showing access reviews, vulnerability scan events) *if* guided by technical teams or specific audit needs. Less common for direct use.
    *   `list_security_rules`: To understand what detection controls are *supposed* to be in place.
    *   `get_security_alerts`: To understand the types of security events being detected, which can relate to control failures.
*   **`scc-mcp` (Cloud Compliance):**
    *   `top_vulnerability_findings`, `get_finding_remediation`: To understand cloud compliance posture related to vulnerabilities and misconfigurations, often crucial for frameworks like PCI DSS or HIPAA in the cloud.
*   **`secops-soar` (Process Evidence):**
    *   `list_cases`, `get_case_full_details`, `post_case_comment`: May review case details or comments to understand how incident response processes (a compliance requirement) are followed, but typically wouldn't execute operational commands.
*   **(Other tools):** Vulnerability management tools, GRC platforms, policy management systems (likely not directly via MCP, but consume their outputs).

## Relevant Security Slash Commands

Compliance Managers utilize security slash commands focused on regulatory compliance, audit management, control assessment, and governance activities.

### Primary Commands (Daily Use)

*   **`/security:compliance assess --framework <name>`** - Comprehensive compliance framework assessment
    *   Assesses organizational compliance against specific regulatory frameworks
    *   Example: `/security:compliance assess --framework "pci-dss,gdpr" --control-mapping --gap-analysis`
    *   Includes automated control mapping and gap identification
    *   Supports regulatory readiness and compliance posture reporting

*   **`/security:audit prepare --assessment-type <type>`** - Audit preparation and evidence collection
    *   Prepares comprehensive audit documentation and evidence packages
    *   Example: `/security:audit prepare --assessment-type sox --evidence-collection --control-testing`
    *   Includes automated evidence gathering and control effectiveness testing
    *   Supports internal and external audit processes

*   **`/security:policy validate --compliance-alignment`** - Policy and procedure compliance validation
    *   Validates policies and procedures against regulatory requirements
    *   Example: `/security:policy validate --compliance-alignment --framework iso27001 --gap-analysis`
    *   Includes regulatory alignment assessment and improvement recommendations
    *   Supports policy management and regulatory compliance

*   **`/security:report compliance --status`** - Compliance status reporting and dashboards
    *   Generates comprehensive compliance status reports and dashboards
    *   Example: `/security:report compliance --status --quarterly --executive-summary`
    *   Includes trend analysis and regulatory risk assessment
    *   Supports stakeholder communication and governance reporting

### Secondary Commands (Regular Use)

*   **`/security:controls test --effectiveness`** - Security control effectiveness testing
    *   Tests and validates security control design and operating effectiveness
    *   Example: `/security:controls test --effectiveness --sampling-methodology --evidence-documentation`
    *   Includes statistical sampling and evidence documentation
    *   Supports audit defense and continuous compliance monitoring

*   **`/security:risk assess --compliance-context`** - Compliance-focused risk assessment
    *   Conducts risk assessments with specific focus on regulatory compliance
    *   Example: `/security:risk assess --compliance-context --privacy-impact --data-classification`
    *   Includes privacy impact assessments and data governance
    *   Supports regulatory risk management and data protection

*   **`/security:documentation generate --audit-trail`** - Compliance documentation management
    *   Generates and maintains compliance documentation and audit trails
    *   Example: `/security:documentation generate --audit-trail --policy-versions --control-evidence`
    *   Includes automated documentation and version control
    *   Supports audit readiness and regulatory requirements

*   **`/security:metrics compliance --kpis`** - Compliance program metrics and KPIs
    *   Tracks compliance program effectiveness through key performance indicators
    *   Example: `/security:metrics compliance --kpis --trend-analysis --benchmark`
    *   Includes regulatory KPI tracking and performance benchmarking
    *   Supports continuous improvement and governance reporting

### Audit and Assessment Commands

*   **`/security:evidence collect --automated`** - Automated compliance evidence collection
    *   Collects and organizes compliance evidence from multiple sources
    *   Example: `/security:evidence collect --automated --control-objectives --retention-policy`
    *   Includes automated evidence gathering and retention management
    *   Supports audit efficiency and evidence integrity

*   **`/security:remediation track --compliance-gaps`** - Compliance gap remediation tracking
    *   Tracks remediation efforts for identified compliance gaps
    *   Example: `/security:remediation track --compliance-gaps --timeline --priority-matrix`
    *   Includes remediation timeline management and priority assessment
    *   Supports audit response and continuous compliance improvement

*   **`/security:certification prepare --framework <name>`** - Certification preparation and management
    *   Prepares for security certifications and attestations
    *   Example: `/security:certification prepare --framework iso27001 --readiness-assessment`
    *   Includes certification readiness assessment and gap analysis
    *   Supports certification programs and regulatory attestations

### Regulatory and Framework Commands

*   **`/security:privacy assess --data-protection`** - Privacy and data protection assessment
    *   Conducts comprehensive privacy impact and data protection assessments
    *   Example: `/security:privacy assess --data-protection --gdpr-compliance --pia-framework`
    *   Includes GDPR compliance and privacy impact assessments
    *   Supports data protection compliance and privacy programs

*   **`/security:vendor assess --compliance-risk`** - Vendor compliance risk assessment
    *   Assesses third-party vendor compliance and security risks
    *   Example: `/security:vendor assess --compliance-risk --due-diligence --contract-review`
    *   Includes vendor due diligence and contractual compliance review
    *   Supports vendor risk management and supply chain security

*   **`/security:training compliance --awareness`** - Compliance training and awareness programs
    *   Develops and manages compliance training and awareness programs
    *   Example: `/security:training compliance --awareness --role-based --effectiveness-tracking`
    *   Includes role-based training and effectiveness measurement
    *   Supports regulatory training requirements and culture development

### Strategic Compliance Commands

*   **`/security:governance monitor --regulatory-changes`** - Regulatory change monitoring
    *   Monitors regulatory changes and their impact on compliance requirements
    *   Example: `/security:governance monitor --regulatory-changes --impact-assessment --update-timeline`
    *   Includes regulatory horizon scanning and impact analysis
    *   Supports proactive compliance management and strategic planning

*   **`/security:framework map --cross-reference`** - Compliance framework mapping and analysis
    *   Maps and cross-references multiple compliance frameworks
    *   Example: `/security:framework map --cross-reference --optimization --control-overlap`
    *   Includes framework optimization and control consolidation analysis
    *   Supports efficient compliance program management

### Occasional Use Commands

*   **`/security:breach assess --regulatory-notification`** - Data breach regulatory assessment
    *   Assesses data breaches for regulatory notification requirements
    *   Example: `/security:breach assess --regulatory-notification --timeline --scope-analysis`
    *   Includes notification timeline and scope assessment

*   **`/security:benchmark --compliance-maturity`** - Compliance program maturity benchmarking
    *   Benchmarks compliance program maturity against industry standards
    *   Supports strategic compliance program development and improvement

## Relevant Runbooks

Compliance Managers are primarily consumers of information generated by runbooks or use them as evidence of process, rather than executing them:

*   Outputs from `cloud_vulnerability_triage_and_contextualization.md` can provide evidence of vulnerability management processes.
*   Documentation within `create_an_investigation_report.md` or incident details in SOAR cases (viewed via `get_case_full_details`) can demonstrate incident response procedures are being followed. Specific IR runbooks like `compromised_user_account_response.md`, `basic_endpoint_triage_isolation.md`, `phishing_response.md`, and `ransomware_response.md` serve as documented procedures.
*   Runbooks related to specific compliance tasks (e.g., evidence gathering for PCI DSS audit - *if such runbooks exist*).
*   They are more likely to reference runbooks as documented procedures during audits rather than executing them.
