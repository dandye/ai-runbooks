# Security Investigation Report: Case 3519
## BigQuery Data Exfiltration to Google Drive with DLP Context

**Report Date:** 2025-07-20  
**Case ID:** 3519  
**Priority:** High  
**Status:** Open - In Triage  
**Analyst:** Security Operations Team

---

## Executive Summary

Four correlated security alerts were triggered on July 19, 2025, indicating potential unauthorized data exfiltration from BigQuery to Google Drive. The activity involves an administrator account (ADMIN@WSEXAMPLE.ORG) accessing sensitive data from an external IP address. The presence of DLP (Data Loss Prevention) context suggests that sensitive or classified data may have been involved in this incident.

## Incident Details

### Timeline
- **Alert Window:** 2025-07-19 15:09:18 - 15:10:18 UTC (1 minute window)
- **Case Created:** 2025-07-20 02:21:12 UTC
- **Detection Rule:** SCC: BigQuery Exfiltration to Google Drive with DLP Context

### Key Indicators

**Primary Entities:**
- **User Account:** ADMIN@WSEXAMPLE.ORG (Administrator role)
- **Source IP:** 104.132.138.65 (External, non-corporate IP)
- **BigQuery Job ID:** job_KS_ojKuGfLdamxxDrO4G-N-pc4fa
- **Target Project:** analytics-project
- **Dataset Accessed:** chronicle/tables/ip

**Additional User Accounts Observed:**
- ADMIN@DEMO.WSEXAMPLE.ORG
- ADMIN@WSEXAMPLE.ORG.TEST-GOOGLE-A.COM
- RECOVERY@WSEXAMPLE.ORG

### MITRE ATT&CK Mapping
- **Tactic:** TA0010 - Exfiltration
- **Technique:** T1537 - Transfer Data to Cloud Account

## Technical Analysis

### Alert Correlation
Four distinct alerts were generated with unique ticket IDs:
1. de_9c49f199-37c2-cfb2-57fe-439a0950bc5e
2. de_951b2da3-b335-2b95-a45e-ea52e55224c3
3. de_2bb3c4fc-fe49-f607-d2cd-89889b05e57f
4. de_6fad8a67-bd32-259b-cb7c-9a234818db3e

Each alert contains 8 underlying security events, totaling 32 events across all alerts.

### Data Access Pattern
The incident involves:
- Access to BigQuery analytics data containing IP address information
- Query execution from an external IP address
- Potential export of query results to Google Drive
- DLP policy triggers indicating sensitive data involvement

### Risk Assessment
- **Risk Score:** 60/100 (Medium-High)
- **Severity:** Medium (per alert metadata)
- **Impact:** Potentially High due to:
  - Administrator-level access
  - External IP source
  - Sensitive data indicators (DLP)
  - Data exfiltration to personal cloud storage

## Findings and Observations

1. **Unusual Access Pattern:** Administrator accessing BigQuery from external IP (104.132.138.65) rather than corporate network
2. **Multiple User Variants:** Several variations of admin accounts observed, suggesting potential account enumeration or testing
3. **Sensitive Data Involved:** DLP context indicates classified or sensitive information was accessed
4. **Rapid Activity:** All alerts triggered within a 1-minute window, suggesting automated or scripted activity

## Recommendations

### Immediate Actions
1. **Verify Authorization:** Contact ADMIN@WSEXAMPLE.ORG to verify if this activity was authorized
2. **Review BigQuery Logs:** Examine the specific query executed in job_KS_ojKuGfLdamxxDrO4G-N-pc4fa
3. **Check Google Drive:** Review Google Drive activity for data uploads during the incident timeframe
4. **IP Investigation:** Investigate the source IP 104.132.138.65 for reputation and geolocation

### Follow-up Actions
1. **DLP Review:** Examine DLP findings to determine exact data classification and sensitivity
2. **Access Review:** Audit administrator permissions for BigQuery and Google Drive
3. **Policy Enforcement:** Consider restricting BigQuery access to corporate IP ranges only
4. **MFA Verification:** Ensure multi-factor authentication is enabled for administrator accounts

### Long-term Improvements
1. Implement real-time alerting for BigQuery exports to external destinations
2. Create allowlists for authorized IP addresses accessing sensitive datasets
3. Enhance monitoring for administrator account usage patterns
4. Review and update data classification and DLP policies

## Case Status and Next Steps

**Current Status:** Case remains open pending investigation completion

**Required Actions:**
1. Obtain detailed event logs from Chronicle SIEM
2. Interview the account owner (ADMIN@WSEXAMPLE.ORG)
3. Review Google Workspace audit logs
4. Coordinate with data governance team on data classification
5. Update case priority based on findings

**Escalation Criteria:**
- Confirmation of unauthorized access
- Evidence of actual data exfiltration
- Discovery of additional compromised accounts
- Indication of broader security breach

---

*This report will be updated as additional information becomes available through the investigation process.*