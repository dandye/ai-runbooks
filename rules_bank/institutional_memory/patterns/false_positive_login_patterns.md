---
title: "Pattern: False Positive Login Patterns"
type: "pattern"
category: "false_positive_identification"
status: "active"
tags:
  - false_positives
  - login_analysis
  - pattern_recognition
  - noise_reduction
confidence: 0.90
last_updated: "2025-08-21"
pattern_source: "collective_analyst_experience"
validation_count: 15
effectiveness_rate: 0.87
applicable_runbooks: ["suspicious_login_triage.md", "triage_alerts.md"]
applicable_personas: ["soc_analyst_tier_1.md", "soc_analyst_tier_2.md"]
---

# Pattern: False Positive Login Patterns

## Pattern Description

This document captures recurring login patterns that consistently generate security alerts but represent benign, authorized activity within our organization. Recognizing these patterns enables faster triage and reduces false positive escalations.

## Organizational Context

Our environment includes legitimate use cases that trigger security alerts due to their deviation from typical user behavior patterns. These have been validated through multiple investigations and represent normal business operations that should not be escalated as security incidents.

## Identified Patterns

### 1. Weekend Software Deployment Logins

**Pattern Signature**:
- Login time: Saturday/Sunday 6 AM - 10 AM
- Source locations: Corporate datacenter IPs (10.x.x.x range)
- User accounts: Service accounts ending in "-deploy" or "-svc"
- Login frequency: 2-6 times per weekend session
- Geographic consistency: Always from primary datacenter location

**Business Context**: Automated deployment system performs software updates during off-hours maintenance windows

**Validation History**: 15 investigations, 0 confirmed threats, all tied to legitimate deployment activities

**Recognition Criteria**:
```
IF (login_time BETWEEN "Saturday 06:00" AND "Sunday 10:00") 
   AND (source_ip MATCHES "10.0.0.0/8")
   AND (username MATCHES "*-deploy" OR username MATCHES "*-svc")
   AND (login_count < 10)
THEN classification = "deployment_activity" confidence = 0.95
```

### 2. Executive Travel Login Anomalies

**Pattern Signature**:
- Unusual geographic locations for C-level accounts
- Login times outside normal business hours due to timezone differences
- Short-duration sessions (< 30 minutes)
- Email and calendar application access only
- Consistent with known executive travel schedules

**Business Context**: Senior executives accessing corporate resources while traveling internationally

**Validation History**: 8 investigations, 0 confirmed threats, all correlated with documented business travel

**Recognition Criteria**:
```
IF (user_level = "executive")
   AND (geographic_distance > 500_miles_from_normal)
   AND (session_duration < 30_minutes)
   AND (applications = ["email", "calendar"])
   AND (travel_schedule_correlation = true)
THEN classification = "executive_travel" confidence = 0.85
```

### 3. Vendor Remote Access Sessions

**Pattern Signature**:
- Login source: Specific approved vendor IP ranges
- User accounts: Vendor-specific service accounts with "-vendor" suffix
- Access pattern: Direct connection to specific application servers
- Session duration: 1-4 hours (typical maintenance window)
- Always during scheduled maintenance hours

**Business Context**: Approved vendors performing scheduled maintenance on critical business applications

**Validation History**: 12 investigations, 0 confirmed threats, all matched vendor maintenance schedules

**Recognition Criteria**:
```
IF (source_ip IN approved_vendor_ranges)
   AND (username MATCHES "*-vendor")
   AND (login_time IN maintenance_windows)
   AND (destination_systems IN vendor_approved_systems)
THEN classification = "vendor_maintenance" confidence = 0.92
```

### 4. Automated Backup System Logins

**Pattern Signature**:
- Daily occurrence at 2 AM - 4 AM
- Service account: "backup-system-01"
- Source: Backup infrastructure (192.168.100.x)
- Target: File servers and database systems
- Consistent timing and duration

**Business Context**: Nightly backup processes require authentication to access protected data sources

**Validation History**: 20+ investigations, 0 confirmed threats, all tied to backup schedule

**Recognition Criteria**:
```
IF (login_time BETWEEN "02:00" AND "04:00")
   AND (username = "backup-system-01")
   AND (source_ip MATCHES "192.168.100.0/24")
   AND (target_systems IN backup_target_list)
THEN classification = "backup_process" confidence = 0.98
```

## Usage Guidelines

### Integration with Alert Triage

When triaging suspicious login alerts, check against these patterns:

1. **Extract Key Attributes**: Time, user, source IP, destination, session characteristics
2. **Pattern Matching**: Compare against recognition criteria above
3. **Confidence Assessment**: Apply pattern confidence scores to triage decision
4. **Documentation**: Log pattern match in case notes for audit trail

### Escalation Decision Matrix

```
Pattern Match Confidence >= 0.90: Close as false positive
Pattern Match Confidence 0.70-0.89: Reduce priority, brief validation
Pattern Match Confidence < 0.70: Standard triage procedure
No Pattern Match: Standard triage procedure
```

### Pattern Validation Process

Patterns should be periodically validated to ensure continued accuracy:

- **Monthly Review**: Check pattern match accuracy against closed cases
- **Quarterly Update**: Update recognition criteria based on environmental changes
- **Annual Assessment**: Comprehensive review of all patterns for continued relevance

## Pattern Evolution

### Adding New Patterns

New false positive patterns should be added when:
- 3+ similar false positive cases identified within 30 days
- Clear business justification for the activity exists
- Pattern characteristics are specific enough to avoid false matches
- SME validation confirms pattern legitimacy

### Pattern Retirement

Patterns should be retired when:
- Business process changes eliminate the underlying activity
- Pattern match accuracy falls below 0.80 for 3+ months
- Pattern becomes too broad and catches legitimate threats
- Organizational context changes making pattern irrelevant

## Effectiveness Metrics

**Current Performance**:
- False positive reduction: 43% decrease in login-related escalations
- Triage efficiency: Average 4.2 minutes saved per matching alert
- Accuracy rate: 87% of pattern matches confirmed as legitimate
- Analyst satisfaction: 4.3/5 rating for pattern utility

**Quality Indicators**:
- Zero false negatives (missed threats) attributed to pattern matching
- 15% reduction in weekend/off-hours analyst callbacks
- Improved consistency in triage decisions across analysts

## Maintenance Log

- **2025-07-01**: Initial pattern collection and documentation
- **2025-07-15**: Added executive travel pattern based on recurring false positives
- **2025-08-01**: Refined backup system pattern timing after infrastructure change
- **2025-08-15**: Updated vendor IP ranges after new vendor onboarding
- **2025-08-21**: Quarterly pattern validation completed, all patterns confirmed effective