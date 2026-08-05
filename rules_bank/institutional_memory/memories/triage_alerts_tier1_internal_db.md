---
runbook: "run_books/triage_alerts.md"
persona: "personas/soc_analyst_tier_1.md"
source_step: "Step 7: Basic Enrichment"
confidence: 0.85
last_updated: "2025-08-23"
feedback_source: "analyst_d_anderson"
validation_count: 8
success_rate: 0.875
related_cases: ["CASE-2024-001", "CASE-2024-045", "CASE-2024-089"]
memory_type: "procedure_addition"
tags: ["internal_enrichment", "threat_database", "efficiency_optimization"]
prerequisites: ["internal_db_access", "threatdb_connectivity"]
priority: "high"
applies_to_sensors: ["xyz_sensor", "network_monitor", "endpoint_detection"]
organizational_context: "Organization maintains comprehensive internal threat database with historical incident data"
---

# Memory: Internal Database Check for Alert Triage

## Analyst Feedback

"For our organization, when triaging alerts from sensors like XYZ, we must always perform a historical lookup in our internal 'ThreatDB' before proceeding with public enrichment. This catches repeat offenders and provides crucial organizational context that external sources miss. I've seen too many cases where we wasted time on external enrichment for IOCs we already knew were bad actors."

## Context Analysis

**Original Procedure Issue**: Standard enrichment workflow jumps directly to external GTI/public sources without checking internal organizational knowledge, leading to redundant analysis and missed context.

**Organizational Context**: The organization maintains a comprehensive ThreatDB containing previous incidents, approved/blocked lists, and organizational-specific threat intelligence that provides faster and more relevant context than external sources.

**Risk Impact**: Without internal database check, analysts may miss previous incidents involving the same IOCs, leading to slower response times and potentially missing campaign patterns or repeat attacks.

**Frequency**: Applies to approximately 60% of alert triage cases, particularly those from network monitoring and endpoint detection systems.

## Original Procedure (for context)

- **Tool**: `secops-mcp enrich_ioc`
- **Parameters**: `ioc={ioc_value}`
- **Expected Output**: External threat intelligence and reputation data

## Derived Procedure

1. **Internal Database Lookup**:
   - **Tool**: `internal_db query`
   - **Parameters**: `database=ThreatDB, query={ioc_value}, include_metadata=true`
   - **Validation**: Response time < 5 seconds, includes threat_level and incident_history
   - **Fallback**: If internal DB unavailable, log error and proceed to external enrichment

2. **Internal Context Analysis**:
   - **Condition**: If internal lookup returns results
   - **Analysis**: Review threat_level, previous_incidents, organizational_impact
   - **Decision**: If threat_level >= "medium" OR previous_incidents > 0, escalate priority

3. **Conditional External Enrichment**:
   - **Condition**: If internal lookup returns no results OR confidence < 0.8 OR threat_level = "unknown"
   - **Tool**: `secops-mcp enrich_ioc`
   - **Parameters**: `ioc={ioc_value}`
   - **Integration**: Combine external data with internal context for complete picture

## Application Criteria

**Alert Types**: Network alerts, malware detection, suspicious domains/IPs, file hash alerts
**Sensor Sources**: XYZ sensor, network monitoring systems, endpoint detection platforms
**Threat Categories**: All categories benefit, particularly effective for repeat threats and campaign tracking
**Time Constraints**: Only apply when internal DB response time < 10 seconds to maintain efficiency

## Validation Metrics

**Success Indicators**: 
- Internal DB query completes successfully
- Relevant internal context retrieved (when available)
- Combined internal/external analysis provides more comprehensive threat picture

**Performance Metrics**:
- Average time savings: 2-4 minutes per triage (when internal data available)
- Context completeness: 85% improvement in threat context quality
- Escalation accuracy: 23% reduction in false positive escalations

**Quality Metrics**:
- Threat detection rate improved by catching previously seen indicators
- Campaign correlation improved through historical incident linking
- Analyst confidence increased with organizational context

## Application Log

- **2025-07-15**: Memory created based on feedback from analyst D. Anderson
- **2025-07-16**: Successfully applied to Alert #4512 - caught repeat Ursnif C2, saved 3 minutes analysis time
- **2025-07-17**: Applied to Alert #4520 - no internal results, proceeded to external enrichment as designed
- **2025-07-18**: Applied to Alert #4521 - identified campaign pattern from 3 previous incidents, escalated appropriately
- **2025-07-20**: Applied to Alert #4535 - internal DB timeout, fallback worked correctly
- **2025-07-22**: Applied to Alert #4567 - found approved business domain, prevented false positive escalation
- **2025-07-25**: Applied to Alert #4589 - caught previously blocked IP attempting new technique
- **2025-08-01**: Applied to Alert #4612 - combined internal/external data provided complete threat picture
- **2025-08-10**: Memory refined based on validation results - confidence increased to 0.85
- **2025-08-15**: Applied to Alert #4678 - internal context helped identify legitimate software update process