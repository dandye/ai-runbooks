---
generated: 2025-07-15T20:02:00Z
directory: rules_bank
total_files: 69
total_directories: 4
depth: 3
---

# Site Map for Security Operations Center (SOC) Rules Bank

## Overview
This directory contains a comprehensive collection of security operations documentation, including runbooks, personas, incident response plans, and procedural guidelines. It serves as the master knowledge repository for AI-assisted security operations, providing standardized workflows for SOC analysts, threat hunters, incident responders, and security engineers.

## Structure

rules_bank/
├── [INDEX] readme.md [HIGH] <- Main entry point and directory overview
├── [DOC] project_plan.md [HIGH] <- Enhancement roadmap for LLM agent context
├── [CONFIG] agent_tool_mapping.md -> references: run_books/*.md
├── [CONFIG] coding_conventions.md
├── [CONFIG] reporting_templates.md <- referenced by: run_books/guidelines/report_writing.md
├── [DOC] suggested_mcp_tools.md
├── [DOC] documentation_links.md [PLACEHOLDER]
├── [DOC] model_selection.md [PLACEHOLDER]
├── [DOC] CONTENT_AUDIT_20250715_1952.md [ANALYSIS]
├── [DOC] CONTENT_INVENTORY_20250715_1939.md [ANALYSIS]
├── [DOC] CONTENT_RELATIONSHIPS_20250715_1957.md [ANALYSIS]
├── personas/ [HIGH]
│   ├── [INDEX] personas.md [HIGH] -> references: all persona files
│   ├── [DOC] ciso.md
│   ├── [DOC] compliance_manager.md
│   ├── [DOC] cti_researcher.md
│   ├── [DOC] detection_engineer.md -> references: run_books/detection_*.md
│   ├── [DOC] incident_responder.md -> references: run_books/irps/*.md
│   ├── [DOC] red_team.md
│   ├── [DOC] security_engineer.md
│   ├── [DOC] soc_analyst_tier_1.md -> references: run_books/triage_alerts.md, basic_*.md
│   ├── [DOC] soc_analyst_tier_2.md -> references: run_books/deep_dive_*.md, hunt_*.md
│   ├── [DOC] soc_analyst_tier_3.md -> references: run_books/advanced_*.md
│   ├── [DOC] soc_manager.md
│   └── [DOC] threat_hunter.md -> references: run_books/threat_hunting_*.md, hunt_*.md
└── run_books/ [HIGH]
    ├── [DOC] advanced_threat_hunting.md [HIGH]
    ├── [DOC] alert_report.md
    ├── [DOC] apt_threat_hunt.md
    ├── [DOC] basic_endpoint_triage_isolation.md [HIGH] <- referenced by: irps/*.md
    ├── [DOC] basic_ioc_enrichment.md [HIGH] -> references: common_steps/enrich_ioc.md
    ├── [DOC] case_event_timeline_and_process_analysis.md
    ├── [DOC] case_report.md [PLACEHOLDER]
    ├── [DOC] close_duplicate_or_similar_cases.md
    ├── [DOC] cloud_vulnerability_triage_and_contextualization.md
    ├── common_steps/ [HIGH]
    │   ├── [DOC] check_duplicate_cases.md [HIGH] <- referenced by: triage_alerts.md, irps/*.md
    │   ├── [DOC] close_soar_artifact.md <- referenced by: triage_alerts.md
    │   ├── [DOC] confirm_action.md <- referenced by: irps/compromised_user_account_response.md
    │   ├── [DOC] correlate_ioc_with_alerts_cases.md
    │   ├── [DOC] document_in_soar.md [HIGH] <- referenced by: ALL procedural runbooks
    │   ├── [DOC] enrich_ioc.md [HIGH] <- referenced by: basic_ioc_enrichment.md, irps/*.md
    │   ├── [DOC] find_relevant_soar_case.md [HIGH] <- referenced by: ALL case-related runbooks
    │   ├── [DOC] generate_report_file.md <- referenced by: investigation_report.md
    │   └── [DOC] pivot_on_ioc_gti.md
    ├── [DOC] compare_gti_collection_to_iocs_and_events.md
    ├── [DOC] create_an_investigation_report.md -> references: common_steps/generate_report_file.md
    ├── [DOC] data_lake_queries.md [PLACEHOLDER]
    ├── [DOC] deep_dive_ioc_analysis.md -> references: common_steps/pivot_on_ioc_gti.md
    ├── [DOC] detection_as_code_workflows.md [PLACEHOLDER]
    ├── [DOC] detection_report.md [PLACEHOLDER]
    ├── [DOC] detection_rule_validation_tuning.md
    ├── [DOC] group_cases.md
    ├── [DOC] group_cases_v2.md [PLACEHOLDER]
    ├── [DOC] guided_ttp_hunt_credential_access.md
    ├── guidelines/
    │   ├── [DOC] report_writing.md -> references: ../reporting_templates.md
    │   ├── [DOC] runbook_guidelines.md [HIGH]
    │   ├── [DOC] soc_analyst_workflows.md -> references: common_steps/*.md
    │   └── [DOC] threat_intel_workflows.md [PLACEHOLDER]
    ├── [DOC] investgate_a_case_w_external_tools.md
    ├── [DOC] investigate_a_gti_collection_id.md
    ├── [DOC] ioc_containment.md <- referenced by: irps/*.md
    ├── [DOC] ioc_threat_hunt.md [PLACEHOLDER]
    ├── irps/ [HIGH]
    │   ├── [DOC] compromised_user_account_response.md [HIGH] -> references: ../common_steps/*.md
    │   ├── [DOC] malware_incident_response.md [HIGH] -> references: ../basic_endpoint_triage_isolation.md
    │   ├── [DOC] phishing_response.md [HIGH] -> references: ../common_steps/enrich_ioc.md
    │   └── [DOC] ransomware_response.md [HIGH] -> references: ../ioc_containment.md
    ├── [DOC] lateral_movement_hunt_psexec_wmi.md
    ├── [DOC] malware_triage.md -> references: common_steps/enrich_ioc.md
    ├── [DOC] metaanalysis.md [PLACEHOLDER]
    ├── [DOC] post_incident_review.md
    ├── [DOC] prioritize_and_investigate_a_case.md
    ├── [DOC] proactive_threat_hunting_based_on_gti_campain_or_actor.md
    ├── [DOC] suspicious_login_triage.md -> references: common_steps/enrich_ioc.md
    ├── [DOC] triage_alerts.md [HIGH] -> references: common_steps/check_duplicate_cases.md
    └── [DOC] ueba_report.md [PLACEHOLDER]

## Key Navigation Paths

### 1. New SOC Analyst Journey
```
readme.md → personas/soc_analyst_tier_1.md → run_books/triage_alerts.md → 
run_books/basic_ioc_enrichment.md → run_books/common_steps/enrich_ioc.md
```

### 2. Incident Response Activation
```
run_books/triage_alerts.md → [Incident Type Classification] → run_books/irps/[specific_response].md → 
run_books/basic_endpoint_triage_isolation.md → run_books/common_steps/document_in_soar.md
```

### 3. Threat Hunting Workflow
```
personas/threat_hunter.md → run_books/advanced_threat_hunting.md → 
run_books/apt_threat_hunt.md → run_books/deep_dive_ioc_analysis.md
```

### 4. Case Investigation Flow
```
run_books/prioritize_and_investigate_a_case.md → run_books/case_event_timeline_and_process_analysis.md → 
run_books/create_an_investigation_report.md → run_books/common_steps/generate_report_file.md
```

## Content Clusters

### Core Operational Cluster (High Traffic)
- **Hub Documents**: `run_books/common_steps/` (all files)
- **Primary Procedures**: `run_books/triage_alerts.md`, `run_books/basic_ioc_enrichment.md`
- **Response Plans**: `run_books/irps/` (all files)

### Analysis & Investigation Cluster
- **IOC Analysis**: `basic_ioc_enrichment.md`, `deep_dive_ioc_analysis.md`, `malware_triage.md`
- **Case Management**: `group_cases.md`, `case_event_timeline_and_process_analysis.md`
- **Threat Intelligence**: `investigate_a_gti_collection_id.md`, `compare_gti_collection_to_iocs_and_events.md`

### Proactive Security Cluster
- **Threat Hunting**: `advanced_threat_hunting.md`, `apt_threat_hunt.md`, `guided_ttp_hunt_credential_access.md`
- **Detection Engineering**: `detection_rule_validation_tuning.md`, `detection_as_code_workflows.md`
- **Lateral Movement**: `lateral_movement_hunt_psexec_wmi.md`

### Human Resources Cluster
- **Role Definitions**: `personas/` (all persona files)
- **Workflow Guidance**: `run_books/guidelines/soc_analyst_workflows.md`
- **Training Pathways**: Skill progression from Tier 1 → Tier 2 → Tier 3

### Documentation & Standards Cluster
- **Templates**: `reporting_templates.md`, `run_books/guidelines/report_writing.md`
- **Conventions**: `coding_conventions.md`, `run_books/guidelines/runbook_guidelines.md`
- **Tool Integration**: `agent_tool_mapping.md`, `suggested_mcp_tools.md`

## Cross-References

### High-Frequency References
- **`run_books/common_steps/document_in_soar.md`**: Referenced by 28+ procedural runbooks
- **`run_books/common_steps/enrich_ioc.md`**: Referenced by all IOC-related procedures
- **`run_books/common_steps/find_relevant_soar_case.md`**: Referenced by all case management workflows

### Critical Dependencies
- **IRP to Procedures**: `run_books/irps/*.md` → `run_books/basic_endpoint_triage_isolation.md`
- **Personas to Runbooks**: `personas/*.md` → relevant `run_books/*.md`
- **Guidelines to Implementation**: `run_books/guidelines/*.md` → procedural runbooks

### Bidirectional Relationships
- **Triage ↔ Enrichment**: `triage_alerts.md` ↔ `basic_ioc_enrichment.md`
- **Investigation ↔ Reporting**: `create_an_investigation_report.md` ↔ `guidelines/report_writing.md`

## Orphaned Content

### Placeholder Files (Requiring Development)
- `documentation_links.md` - Empty file, needs external reference compilation
- `model_selection.md` - Empty file, needs AI model selection criteria
- `run_books/case_report.md` - Placeholder status, needs completion
- `run_books/data_lake_queries.md` - Placeholder status, needs query examples
- `run_books/detection_as_code_workflows.md` - Placeholder status, needs workflow definition
- `run_books/detection_report.md` - Placeholder status, needs reporting templates
- `run_books/group_cases_v2.md` - Placeholder status, successor to group_cases.md
- `run_books/ioc_threat_hunt.md` - Placeholder status, needs hunt procedures
- `run_books/metaanalysis.md` - Placeholder status, needs analysis framework
- `run_books/guidelines/threat_intel_workflows.md` - Placeholder status, needs CTI workflows
- `run_books/ueba_report.md` - Placeholder status, needs UEBA analysis procedures

### Weakly Connected Content
- `project_plan.md` - Strategic document with limited operational connections
- `CONTENT_*.md` files - Analysis reports, valuable but separate from operational workflows

## Content Type Distribution
- **[DOC]**: 65 files (94%) - Primary content type
- **[CONFIG]**: 3 files (4%) - Configuration and mapping files
- **[INDEX]**: 2 files (3%) - Entry point and navigation files
- **[PLACEHOLDER]**: 11 files (16%) - Requiring completion
- **[HIGH]**: 15 files (22%) - High-traffic or critical documents

## Maintenance Recommendations

### Immediate Actions
1. **Complete placeholder content** to eliminate orphaned nodes
2. **Strengthen persona-to-runbook mappings** for better navigation
3. **Add cross-references** between related procedures

### Structural Improvements
1. **Create index files** for major clusters (e.g., `run_books/INDEX.md`)
2. **Develop progressive disclosure** pathways for complex procedures
3. **Implement consistent cross-referencing** patterns throughout documentation

### Navigation Enhancements
1. **Add "Related Procedures"** sections to each runbook
2. **Create skill-based learning paths** linking personas to appropriate runbooks
3. **Implement consistent tagging** for content discovery and filtering