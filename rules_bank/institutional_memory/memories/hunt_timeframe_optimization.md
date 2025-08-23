---
runbook: "run_books/advanced_threat_hunting.md"
persona: "personas/threat_hunter.md"
source_step: "Step 2: Define Hunt Scope and Timeframe"
confidence: 0.72
last_updated: "2025-08-20"
feedback_source: "senior_hunter_m_rodriguez"
validation_count: 5
success_rate: 0.80
related_cases: ["HUNT-2024-003", "HUNT-2024-007", "HUNT-2024-012"]
memory_type: "performance_optimization"
tags: ["hunt_optimization", "timeframe_selection", "efficiency_improvement"]
prerequisites: ["hunting_tools_access", "data_retention_7days_minimum"]
priority: "normal"
applies_to_sensors: ["all_sensors"]
organizational_context: "Most threat actor activity occurs during business hours due to target environment characteristics"
---

# Memory: Optimized Timeframe Selection for Threat Hunting

## Analyst Feedback

"I've noticed that our threat hunting is much more effective when we start with a focused 7-day lookback during business hours (9 AM - 5 PM) rather than the default 30-day full-time hunt. Most of our actual threats show activity during business hours because that's when our users are active and when attackers get the best camouflage. Starting focused and expanding only when we find something saves hours of analysis time and reduces noise significantly."

## Context Analysis

**Original Procedure Issue**: Default 30-day, 24/7 hunting timeframes generate excessive noise and require significant analysis time to process, often diluting focus from actual threat patterns.

**Organizational Context**: Organization's user activity is heavily concentrated during business hours (9 AM - 5 PM), making threat actor activity during these periods more likely and easier to camouflage within normal operations.

**Risk Impact**: Overly broad initial timeframes lead to analyst fatigue, longer investigation times, and potentially missed threats buried in noise. Focused approach improves threat detection efficiency and analyst effectiveness.

**Frequency**: Applies to most proactive threat hunting activities, particularly those targeting user-focused attack techniques.

## Original Procedure (for context)

- **Scope**: 30-day lookback period
- **Time Range**: 24/7 continuous monitoring
- **Analysis**: Full dataset analysis from start
- **Expected Output**: Comprehensive but potentially noisy results

## Derived Procedure

1. **Initial Focused Hunt**:
   - **Timeframe**: 7-day lookback period
   - **Time Constraint**: Business hours (9 AM - 5 PM, Monday-Friday)
   - **Rationale**: Captures most relevant user-centric threat activity
   - **Tools**: Standard hunting queries with time constraints

2. **Results Assessment**:
   - **Condition**: If initial hunt yields suspicious activity or confirmed threats
   - **Action**: Expand timeframe incrementally (14 days, then 30 days)
   - **Focus**: Maintain business hours focus unless off-hours activity confirmed

3. **Conditional Expansion**:
   - **Trigger 1**: Confirmed threat activity in initial timeframe
   - **Trigger 2**: Suspicious patterns suggesting longer campaign
   - **Trigger 3**: Evidence of off-hours activity requiring broader scope
   - **Expansion Strategy**: Gradual increase with continued focus on high-activity periods

4. **Noise Reduction Validation**:
   - **Metric**: Compare alert volume and false positive rate
   - **Target**: Reduce initial analysis volume by 60-80% while maintaining detection coverage
   - **Quality Check**: Ensure no critical threats missed due to timeframe constraints

## Application Criteria

**Hunt Types**: User-focused techniques (credential access, lateral movement, data exfiltration)
**Threat Categories**: APT campaigns, insider threats, business email compromise, credential harvesting
**Data Availability**: Requires minimum 7-day data retention with good coverage
**Time Constraints**: Most effective when hunting time is limited or analyst capacity is constrained

## Validation Metrics

**Success Indicators**:
- Reduced initial analysis time while maintaining or improving threat detection
- Higher signal-to-noise ratio in hunt results
- Faster time-to-discovery for business-hours threats

**Performance Metrics**:
- Analysis time reduction: 65% average decrease in initial analysis time
- False positive reduction: 70% fewer irrelevant results in initial hunt
- Detection efficiency: Same or better threat detection rate with focused approach

**Quality Metrics**:
- Time-to-detection improved for business-hours threats
- Analyst satisfaction higher due to reduced noise
- Hunt completion rate increased due to more manageable scope

## Application Log

- **2025-07-28**: Memory created based on feedback from Senior Hunter M. Rodriguez
- **2025-08-01**: Applied to Hunt HUNT-2024-003 (credential access) - found 3 suspicious login patterns in 7-day/business-hours scope, expanded to 14 days, confirmed campaign
- **2025-08-05**: Applied to Hunt HUNT-2024-007 (lateral movement) - initial 7-day scope clean, expanded to 30 days due to intelligence indicating long-term campaign, found historical activity
- **2025-08-08**: Applied to Hunt HUNT-2024-009 (data exfiltration) - 7-day business hours hunt revealed consistent pattern, no expansion needed, case closed efficiently
- **2025-08-12**: Applied to Hunt HUNT-2024-012 (APT persistence) - focused approach missed critical off-hours activity, expanded correctly but noted lesson learned about APT timing
- **2025-08-18**: Applied to Hunt HUNT-2024-015 (insider threat) - business hours focus perfect for user-centric activity, detected threat in initial scope, saved 6 hours analysis time