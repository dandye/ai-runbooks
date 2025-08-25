---
title: "Reporting Templates & Guidelines"
type: "guideline"
category: "security_operations"
status: "active"
tags:
  - reporting
  - templates
  - documentation
  - standards
---

# Reporting Templates & Guidelines

This file outlines standard formats and required elements for common reports generated during security operations.

## General Report Metadata Requirements

*   **File Location:** All reports **must** be saved to the `./reports/` directory
*   **File Naming Convention:** Use the format: `<report_type>_<identifier>_<YYYYMMDD_HHMM>.md`
    *   Examples: `alert_triage_report_2194_20250504_1807.md`, `rule_triage_report_ru_99d1f620_20250720_0215.md`
*   **Runbook Reference:** All reports generated via runbook execution **must** clearly state which runbook was used at the beginning of the report.
    *   *Example:* `**Runbook Used:** Alert Investigation Summary Report Runbook`
*   **Timestamp:** Include a generation timestamp in a consistent format (e.g., YYYY-MM-DD HH:MM Timezone).
*   **Case ID:** Reference the relevant SOAR Case ID(s).
*   **Workflow Diagram:** Include a Mermaid sequence diagram from the executed runbook, showing the actual MCP Servers and Tools used.
*   **Memory Enhancement Tracking:** Document any institutional memory applications, pattern recognitions, or adaptive learning contributions used during the investigation.

## Common Report Types (Placeholders - To be defined)

### Daily SOC Summary

*   *(Define required sections, e.g., Key Metrics, Notable Alerts, Ongoing Incidents, Shift Handover Notes)*

### Post-Incident Report

*   *(Define required sections, e.g., Executive Summary, Incident Timeline, Root Cause Analysis, Impact Assessment, Actions Taken, Lessons Learned, Recommendations)*

### Threat Hunt Summary Report

*   *(Define required sections, e.g., Hunt Hypothesis, Scope, Timeframe, Queries Used, Findings (Positive/Negative), Enrichment Details, Recommendations/Escalation)*

### Vulnerability Triage Report

*   *(Define required sections, e.g., Vulnerability Details (CVE), Affected Assets, GTI/SIEM Context, Remediation Steps, Prioritization)*

### Memory-Enhanced Alert Triage Report Template

**Required Sections:**
- **Executive Summary** with memory enhancement impact
- **Alert Details** and initial context
- **Memory Applications** - institutional memories used and their effectiveness  
- **Pattern Recognition** - organizational patterns identified
- **Enhanced Analysis** - findings with institutional context
- **Decision Rationale** - memory-informed reasoning
- **Performance Metrics** - time savings and quality improvements from memory use
- **Recommendations** - including memory feedback for future improvements

**Sample Memory Enhancement Section:**
```markdown
## Memory Enhancement Summary

### Institutional Memories Applied
- **Memory:** `memories/triage_alerts_tier1_internal_db.md` (Confidence: 0.85)
- **Application:** Internal database check before external enrichment
- **Outcome:** Successfully identified approved internal domain, saved 12 minutes analysis time
- **Effectiveness:** High - prevented unnecessary escalation

### Pattern Recognition
- **Pattern Matched:** "Automated Backup System Logins" from `patterns/false_positive_login_patterns.md`
- **Confidence:** 0.98
- **Classification:** Routine backup activity
- **Impact:** Immediate identification of benign activity

### Performance Impact
- **Time Savings:** 12 minutes (70% reduction from standard workflow)
- **Quality Enhancement:** Complete organizational context provided
- **Decision Confidence:** Increased from Low to High
- **Escalation Avoided:** Yes - resolved at Tier 1 level

### Memory System Feedback
- **Memory Validation:** Successful application logged for confidence adjustment
- **Pattern Reinforcement:** Backup system pattern validated
- **Analyst Learning:** Enhanced understanding of organizational systems
```

### Memory Effectiveness Metrics Report Template

**Purpose:** Track and measure institutional memory system performance

**Required Sections:**
- **Executive Summary** of memory system performance
- **Application Statistics** - usage frequency, success rates, confidence trends
- **Performance Impact** - time savings, quality improvements, escalation reduction
- **Memory Lifecycle** - creation, validation, retirement activity
- **Analyst Feedback** - user satisfaction and contribution to memory development
- **System Health** - memory accuracy, pattern recognition effectiveness
- **Recommendations** - memory system improvements and optimization opportunities

**Sample Metrics Section:**
```markdown
## Monthly Memory System Performance - August 2025

### Application Statistics
- **Total Memory Applications:** 47
- **Success Rate:** 87% (41 successful, 6 failed)
- **Average Confidence:** 0.82
- **High-Confidence Auto-Applications:** 23 (49%)
- **Medium-Confidence Approvals:** 18 (38%)

### Performance Impact  
- **Average Time Savings:** 8.3 minutes per application
- **Total Time Saved:** 391 minutes (6.5 hours)
- **Quality Improvement Rate:** 73% of applications
- **Escalations Avoided:** 12 (26% of applications)

### Memory Development
- **New Memories Created:** 3
- **Memory Validations:** 28 confidence adjustments
- **Memory Retirements:** 1 (outdated backup pattern)
- **Feedback Items Processed:** 5

### Top Performing Memories
1. `triage_alerts_tier1_internal_db.md` - 0.87 confidence, 15 applications
2. `false_positive_login_patterns.md` - 0.98 confidence, 8 applications  
3. `hunt_timeframe_optimization.md` - 0.75 confidence, 3 applications
```

*(Add other relevant report templates as needed)*
