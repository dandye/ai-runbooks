---
title: "Persona: Compliance Manager"
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

## Relevant Runbooks

Compliance Managers are primarily consumers of information generated by runbooks or use them as evidence of process, rather than executing them:

*   Outputs from `cloud_vulnerability_triage_and_contextualization.md` can provide evidence of vulnerability management processes.
*   Documentation within `create_an_investigation_report.md` or incident details in SOAR cases (viewed via `get_case_full_details`) can demonstrate incident response procedures are being followed. Specific IR runbooks like `compromised_user_account_response.md`, `basic_endpoint_triage_isolation.md`, `phishing_response.md`, and `ransomware_response.md` serve as documented procedures.
*   Runbooks related to specific compliance tasks (e.g., evidence gathering for PCI DSS audit - *if such runbooks exist*).
*   They are more likely to reference runbooks as documented procedures during audits rather than executing them.
