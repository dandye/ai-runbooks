---
title: IOC Enrichment Report - superstarts.top
type: IOC Enrichment
indicator: superstarts.top
indicator_type: domain
analyst: Claude SOC Analyst
timestamp: 2025-07-20T08:30:00Z
risk_level: HIGH
confidence: HIGH
---

# IOC Enrichment Report: superstarts.top

## Executive Summary

**Domain:** `superstarts.top`  
**Risk Level:** HIGH  
**Confidence:** HIGH  
**Threat Classification:** Malicious Infrastructure  

The domain `superstarts.top` is assessed as malicious infrastructure with HIGH confidence based on threat intelligence analysis. The domain shows strong associations with malware families including Ursnif/Gozi banking trojan and has been flagged by multiple security vendors.

## Threat Intelligence Summary

### Google Threat Intelligence Assessment
- **Reputation Score:** -57 (Malicious)
- **Mandiant IC Score:** 94/100 (Very High Risk)
- **Detection Stats:** 10 malicious, 1 suspicious, 32 undetected, 51 harmless
- **Community Votes:** 3 malicious, 0 harmless
- **Threat Severity:** SEVERITY_NONE (less than 2 detections threshold, but note multiple malicious classifications)

### Key Indicators
- **First Seen ITW:** August 17, 2022
- **Last Seen ITW:** July 5, 2025 (Recent activity)
- **Domain Status:** clientHold, pendingDelete, redemptionPeriod
- **Registration:** Russia (RU)

### Infrastructure Details
- **Creation Date:** August 16, 2022
- **Expiration Date:** August 16, 2023 (Expired, in redemption period)
- **Registrar:** ERANET INTERNATIONAL LIMITED
- **Current IPs:** 
  - 31.41.44.27
  - 62.173.149.9
- **Name Servers:** a.dnspod.com, b.dnspod.com, c.dnspod.com

## Malware Associations

### Identified Threats
The domain has strong associations with the following malware families:
- **Ursnif/Gozi Banking Trojan** (threatfox_win_gozi)
- **ZenBox Ursnif Variant** (analysis_virustotal_zenbox_ursnif)
- Multiple unknown malware samples (hash-based collections)

### Related Collections
- `malware--36934694-2d74-5d63-af3c-c4a9686ba6e2`
- `malware--b2bd3b57-8820-5c18-a383-990cc3d97c72`
- `threatfox_win_gozi`
- `analysis_virustotal_zenbox_ursnif`

## Risk Assessment

### Risk Factors
1. **Active Malware Infrastructure:** Associated with Ursnif banking trojan
2. **Recent Activity:** Last seen in July 2025
3. **High Mandiant Score:** 94/100 indicates sophisticated threat
4. **Multiple Detections:** 10 security vendors flagged as malicious
5. **Suspicious Registration:** Russian registration with privacy protection

### Recommended Actions
1. **IMMEDIATE:** Block domain at network perimeter
2. **IMMEDIATE:** Search logs for any connections to this domain
3. **HIGH:** Hunt for Ursnif/Gozi indicators in environment
4. **MEDIUM:** Review any systems that may have accessed this domain
5. **LOW:** Monitor for related domains and infrastructure

## IOC Package

### Primary Indicators
```
Domain: superstarts.top
IPs: 31.41.44.27, 62.173.149.9
```

### Related Infrastructure
```
Nameservers:
- a.dnspod.com
- b.dnspod.com  
- c.dnspod.com
```

### Hunt Queries
```yaml
Chronicle_UDM:
  - 'network.dns.questions.name="superstarts.top"'
  - 'network.http.parsed_user_agent contains "superstarts.top"'
  - 'target.ip in ["31.41.44.27", "62.173.149.9"]'

Splunk:
  - 'index=* "superstarts.top"'
  - 'index=dns query="superstarts.top"'
```

## Technical Details

### WHOIS Information
- **Registrant Country:** Russia (RU)
- **Admin Email:** 76f2e07d3b953101s@bk.ru
- **Domain Status:** clientHold, pendingDelete, redemptionPeriod
- **DNSSEC:** unsigned

### DNS Records
```
A Records:
- 31.41.44.27 (TTL: 326)
- 62.173.149.9 (TTL: 326)

NS Records:
- a.dnspod.com
- b.dnspod.com
- c.dnspod.com
```

### JARM Fingerprint
`29d29d15d29d29d21c29d29d29d29d0a517dfdbcfdef7b8cfc7b7c8731464c`

## Historical Context

- **Registration:** August 16, 2022
- **First Malicious Activity:** August 17, 2022 (1 day after registration)
- **Recent Activity:** July 5, 2025
- **Domain Lifecycle:** Currently in redemption period after expiration

## Recommendations

### Immediate Actions (0-4 hours)
- Block domain at DNS and web proxy level
- Search SIEM for any historical connections
- Alert SOC to monitor for related activity

### Short-term Actions (4-24 hours)
- Hunt for Ursnif/Gozi banking trojan indicators
- Review endpoint logs for potential infections
- Check email security logs for phishing attempts

### Long-term Actions (1-7 days)
- Monitor for similar domain registrations
- Update threat intelligence feeds
- Review and update security controls

## Confidence Assessment

**Overall Confidence: HIGH**
- Multiple vendor detections
- Strong malware associations
- Recent threat activity
- Consistent threat intelligence sources

---

**Report Generated:** 2025-07-20T08:30:00Z  
**Sources:** Google Threat Intelligence, VirusTotal  
**Analyst:** Claude SOC Analyst  
**Next Review:** 2025-07-27T08:30:00Z