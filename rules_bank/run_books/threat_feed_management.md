# Threat Feed Management and Research

## Summary
Establish and maintain a comprehensive threat intelligence feed management system through continuous research and evaluation to ensure high-quality, relevant, and actionable intelligence flows into security operations. This runbook covers feed research, selection, integration, quality assessment, deduplication, normalization, reporting, and lifecycle management of threat intelligence feeds.

## Prerequisites
- Threat Intelligence Platform (TIP) or SIEM with TI capabilities
- API access to threat intelligence sources
- Understanding of intelligence confidence levels and TLP
- Storage capacity for historical threat data
- Established intelligence requirements (IRs)

## Procedure

### Step 1: Intelligence Research Requirements Definition

#### 1.1 Establish Priority Intelligence Research Requirements (PIRs)
Define what intelligence research and data collection is needed:
```yaml
priority_intelligence_requirements:
  threat_actors:
    focus: "Groups targeting our sector"
    specifics:
      - Financial crime groups
      - Nation-state actors
      - Ransomware operators
    priority: CRITICAL
    
  technical_indicators:
    focus: "IoCs relevant to our environment"
    types:
      - IP addresses
      - Domains
      - File hashes
      - Email addresses
    priority: HIGH
    
  vulnerabilities:
    focus: "CVEs affecting our technology stack"
    criteria:
      - CVSS >= 7.0
      - Exploited in wild
      - Affects our products
    priority: CRITICAL
    
  ttps:
    focus: "Attack techniques used against peers"
    framework: "MITRE ATT&CK"
    priority: HIGH
```

#### 1.2 Define Collection Requirements
Specify what to collect and retain:
```yaml
collection_requirements:
  data_types:
    mandatory:
      - Active C2 infrastructure
      - Malware signatures
      - Phishing indicators
      - Vulnerability intelligence
      
    optional:
      - Threat actor profiles
      - Geopolitical analysis
      - Dark web intelligence
      
  retention_policy:
    active_indicators: "90 days"
    expired_indicators: "365 days"
    threat_actor_data: "Indefinite"
    vulnerability_data: "Until patched + 90 days"
```

#### 1.3 Set Quality Standards
Define acceptable feed quality:
```yaml
quality_standards:
  timeliness:
    critical_feeds: "< 15 minutes latency"
    standard_feeds: "< 1 hour latency"
    strategic_feeds: "< 24 hours latency"
    
  accuracy:
    false_positive_rate: "< 5%"
    validation_rate: "> 80%"
    
  completeness:
    context_required: true
    confidence_scores: required
    tlp_marking: required
    
  relevance:
    minimum_relevance_score: 60
    industry_specific: preferred
    geographic_alignment: required
```

### Step 2: Feed Source Research, Evaluation and Selection

#### 2.1 Research and Inventory Available Feeds
Conduct research to catalog potential threat feeds:
```yaml
feed_inventory:
  commercial_feeds:
    - name: "Google Threat Intelligence"
      type: "Comprehensive"
      cost: "$$$"
      coverage: "Global"
      
    - name: "Vendor Threat Feed"
      type: "Product-specific"
      cost: "Included"
      coverage: "Product vulnerabilities"
      
  open_source_feeds:
    - name: "CISA Alerts"
      type: "Government"
      cost: "Free"
      coverage: "US-focused"
      
    - name: "AlienVault OTX"
      type: "Community"
      cost: "Free"
      coverage: "Global crowdsourced"
      
  industry_feeds:
    - name: "FS-ISAC"
      type: "Industry sharing"
      cost: "Membership"
      coverage: "Financial sector"
      
  internal_feeds:
    - name: "Honeypot Network"
      type: "Deception"
      cost: "Operational"
      coverage: "Targeted attacks"
```

#### 2.2 Evaluate Feed Quality
Assess each feed against criteria:
```python
feed_evaluation_matrix = {
    'feed_name': 'Example Feed',
    'evaluation_criteria': {
        'coverage': 8,  # 1-10 scale
        'timeliness': 9,
        'accuracy': 7,
        'relevance': 8,
        'context_depth': 6,
        'integration_ease': 9,
        'cost_effectiveness': 7,
        'support_quality': 8
    },
    'overall_score': 7.75,
    'recommendation': 'ADOPT',
    'limitations': ['Limited context', 'US-focused'],
    'use_cases': ['Real-time blocking', 'Incident enrichment']
}
```

#### 2.3 Perform Feed Trials
Test feeds before commitment:
```yaml
feed_trial_process:
  duration: "30 days"
  
  metrics_to_track:
    - unique_indicators_provided
    - overlap_with_existing_feeds
    - false_positive_rate
    - true_positive_detections
    - enrichment_value
    - operational_impact
    
  success_criteria:
    unique_value: "> 20% unique indicators"
    accuracy: "> 90% true positives"
    operational_value: "Measurable improvement"
    
  trial_outcome:
    adopt: "Meets all criteria"
    reject: "Fails criteria"
    extend_trial: "Needs more data"
```

### Step 3: Feed Integration and Configuration

#### 3.1 Technical Integration
Connect feeds to security infrastructure:
```yaml
integration_configuration:
  api_integration:
    endpoint: "https://threatfeed.example.com/api/v2"
    authentication: "Bearer token"
    poll_frequency: "5 minutes"
    batch_size: 1000
    timeout: 30
    retry_policy:
      attempts: 3
      backoff: "exponential"
      
  file_based_integration:
    protocol: "SFTP"
    schedule: "*/15 * * * *"
    format: "STIX 2.1"
    compression: "gzip"
    
  streaming_integration:
    protocol: "Kafka"
    topic: "threat-intelligence"
    consumer_group: "security-operations"
    offset: "latest"
```

#### 3.2 Data Normalization
Standardize feed data:
```python
normalization_rules = {
    'ip_addresses': {
        'format': 'IPv4/IPv6',
        'validation': 'regex_pattern',
        'enrichment': ['geoip', 'asn', 'reputation']
    },
    'domains': {
        'format': 'FQDN',
        'normalization': 'lowercase',
        'validation': 'dns_resolution',
        'enrichment': ['whois', 'category', 'age']
    },
    'file_hashes': {
        'types': ['md5', 'sha1', 'sha256'],
        'preferred': 'sha256',
        'normalization': 'lowercase'
    },
    'timestamps': {
        'timezone': 'UTC',
        'format': 'ISO8601'
    }
}
```

#### 3.3 Confidence Scoring and Tagging
Apply confidence levels and metadata:
```yaml
confidence_scoring:
  source_reliability:
    A: "Completely reliable"  # Weight: 1.0
    B: "Usually reliable"     # Weight: 0.8
    C: "Fairly reliable"      # Weight: 0.6
    D: "Not usually reliable" # Weight: 0.4
    E: "Unreliable"          # Weight: 0.2
    F: "Cannot be judged"    # Weight: 0.5
    
  information_credibility:
    1: "Confirmed"           # Weight: 1.0
    2: "Probably true"       # Weight: 0.75
    3: "Possibly true"       # Weight: 0.5
    4: "Doubtful"           # Weight: 0.25
    5: "Improbable"         # Weight: 0.1
    6: "Cannot be judged"   # Weight: 0.5
    
  combined_confidence:
    formula: "(source_reliability * 0.4) + (information_credibility * 0.6)"
    threshold_for_action: 0.6
```

### Step 4: Feed Quality Management

#### 4.1 Deduplication
Remove duplicate indicators:
```python
deduplication_process = {
    'exact_match': {
        'method': 'hash_comparison',
        'action': 'keep_highest_confidence'
    },
    'fuzzy_match': {
        'method': 'similarity_scoring',
        'threshold': 0.95,
        'action': 'merge_context'
    },
    'temporal_dedup': {
        'window': '24_hours',
        'action': 'keep_most_recent'
    },
    'cross_feed_dedup': {
        'priority': ['premium_feeds', 'validated_feeds', 'open_feeds'],
        'action': 'aggregate_confidence'
    }
}
```

#### 4.2 Validation and Verification
Verify indicator quality:
```yaml
validation_checks:
  technical_validation:
    ip_addresses:
      - "Not in bogon ranges"
      - "Not in RFC1918 (unless internal)"
      - "Active in last 30 days"
      
    domains:
      - "Valid DNS record exists"
      - "Not in Alexa top 10k (unless compromised)"
      - "Age check (not brand new unless DGA)"
      
    file_hashes:
      - "Format validation"
      - "Not in whitelist"
      - "VirusTotal check if available"
      
  contextual_validation:
    - "Threat actor attribution consistency"
    - "TTP alignment with known patterns"
    - "Temporal consistency"
    - "Geographic relevance"
```

#### 4.3 False Positive Management
Track and reduce false positives:
```yaml
false_positive_handling:
  detection:
    - source: "SOC analyst feedback"
      method: "Manual reporting"
    - source: "Automated validation"
      method: "Benign domain checking"
    - source: "User reports"
      method: "Ticketing system"
      
  tracking:
    database: "FP tracking system"
    fields:
      - indicator
      - feed_source
      - report_date
      - validation_status
      - business_impact
      
  remediation:
    whitelist_addition: "After 2 confirmations"
    feed_tuning: "Adjust confidence scores"
    vendor_feedback: "Report to feed provider"
    
  metrics:
    fp_rate_by_feed: "Track monthly"
    improvement_trend: "Quarter over quarter"
    cost_of_fps: "Hours spent * hourly rate"
```

### Step 5: Feed Lifecycle Management

#### 5.1 Performance Monitoring
Track feed effectiveness:
```python
feed_metrics = {
    'operational_metrics': {
        'availability': 'Uptime percentage',
        'latency': 'Time from publication to ingestion',
        'volume': 'Indicators per day',
        'unique_contribution': 'Unique indicators vs total'
    },
    'quality_metrics': {
        'true_positive_rate': 'Confirmed detections / Total alerts',
        'false_positive_rate': 'False alerts / Total alerts',
        'enrichment_value': 'Additional context provided',
        'relevance_score': 'Applicable indicators / Total indicators'
    },
    'business_metrics': {
        'incidents_prevented': 'Count of blocked attacks',
        'investigation_acceleration': 'Time saved in hours',
        'cost_per_indicator': 'Feed cost / Unique indicators',
        'roi': '(Value generated - Cost) / Cost'
    }
}
```

#### 5.2 Feed Optimization
Continuously improve feed configuration:
```yaml
optimization_activities:
  regular_tuning:
    frequency: "Weekly"
    activities:
      - "Adjust confidence thresholds"
      - "Update filtering rules"
      - "Refine relevance scoring"
      
  periodic_review:
    frequency: "Monthly"
    activities:
      - "Analyze feed overlap"
      - "Evaluate cost-benefit"
      - "Review use cases"
      
  strategic_assessment:
    frequency: "Quarterly"
    activities:
      - "Feed portfolio review"
      - "Vendor performance evaluation"
      - "Contract negotiations"
```

#### 5.3 Feed Retirement
Process for removing feeds:
```yaml
retirement_criteria:
  triggers:
    - "Consistent poor quality (< 50% accuracy)"
    - "Excessive false positives (> 20%)"
    - "Limited unique value (< 5% unique)"
    - "Cost exceeds value"
    - "Vendor support issues"
    
  retirement_process:
    1: "Document retirement decision"
    2: "Identify indicator dependencies"
    3: "Find replacement coverage"
    4: "Gradual phase-out (30 days)"
    5: "Archive historical data"
    6: "Update documentation"
    7: "Notify stakeholders"
```

### Step 6: Intelligence Distribution

#### 6.1 Feed Routing
Route intelligence to appropriate systems:
```yaml
distribution_matrix:
  real_time_blocking:
    feeds: ["Critical IoCs", "Active C2"]
    destinations: ["Firewall", "Proxy", "EDR"]
    latency: "< 1 minute"
    
  detection_enrichment:
    feeds: ["All tactical feeds"]
    destinations: ["SIEM", "SOAR"]
    latency: "< 5 minutes"
    
  strategic_analysis:
    feeds: ["Threat reports", "Actor profiles"]
    destinations: ["TIP", "Analyst workbench"]
    latency: "< 1 hour"
    
  threat_hunting:
    feeds: ["Historical IoCs", "TTPs"]
    destinations: ["Hunting platform", "Data lake"]
    latency: "< 24 hours"
```

#### 6.2 Access Control
Manage feed access:
```yaml
access_control:
  role_based_access:
    soc_analyst:
      - view: "All feeds"
      - modify: "Confidence scores"
      - export: "With approval"
      
    threat_hunter:
      - view: "All feeds + historical"
      - modify: "Hunt indicators"
      - export: "Unlimited"
      
    incident_responder:
      - view: "All feeds"
      - modify: "Case-specific"
      - export: "Case-related"
      
  data_classification:
    tlp_white: "Unrestricted"
    tlp_green: "Community only"
    tlp_amber: "Organization only"
    tlp_red: "Named recipients only"
```

### Step 7: Research Reporting and Communication

#### 7.1 Feed Performance Research Report
Regular feed research and assessment reporting:
```markdown
# Threat Feed Performance Research Report
Period: [Month Year]
Research Conducted: [Research activities performed]

## Feed Portfolio Overview
- Total Active Feeds: 15
- New Feeds Added: 2
- Feeds Retired: 1
- Total Investment: $50,000/month

## Performance Metrics

### Top Performing Feeds
| Feed Name | Unique IoCs | True Positives | False Positives | ROI |
|-----------|-------------|----------------|-----------------|-----|
| GTI | 25,000 | 95% | 2% | 450% |
| CISA | 5,000 | 92% | 3% | N/A |
| Vendor X | 10,000 | 88% | 5% | 220% |

### Feed Quality Trends
- Overall Accuracy: 91% (↑ 3%)
- Deduplication Rate: 35% (→ stable)
- Average Latency: 8 minutes (↓ 2 min)
- Coverage Gaps: 2 identified

## Operational Impact
- Threats Detected: 347
- Incidents Prevented: 28
- Investigation Hours Saved: 120
- Estimated Value: $850,000

## Recommendations
1. Increase Feed X polling frequency
2. Retire Feed Y due to low value
3. Trial new vulnerability feed
4. Implement ML-based deduplication
```

#### 7.2 Stakeholder Communication
Keep stakeholders informed:
```yaml
communication_plan:
  executive_updates:
    frequency: "Quarterly"
    content: "ROI and risk reduction"
    format: "Dashboard + presentation"
    
  operational_updates:
    frequency: "Weekly"
    content: "Feed status and issues"
    format: "Email summary"
    
  technical_updates:
    frequency: "Daily"
    content: "Feed health and metrics"
    format: "Dashboard + alerts"
```

## Output Format

### Feed Management Dashboard:
```yaml
feed_status:
  operational:
    total_feeds: 15
    active: 14
    degraded: 1
    offline: 0
    
  quality_metrics:
    average_accuracy: 91%
    unique_coverage: 65%
    latency: "8 minutes average"
    dedup_rate: 35%
    
  volume_metrics:
    daily_indicators: 150000
    unique_daily: 97500
    actionable: 45000
    blocked: 12000
    
  business_value:
    monthly_cost: $50000
    incidents_prevented: 28
    value_generated: $850000
    roi: 1700%
```

## Automation Opportunities

```python
# Automated feed management pipeline
class FeedManager:
    def daily_operations(self):
        # Collect from all feeds
        for feed in active_feeds:
            data = feed.collect()
            normalized = self.normalize(data)
            deduplicated = self.deduplicate(normalized)
            validated = self.validate(deduplicated)
            enriched = self.enrich(validated)
            self.distribute(enriched)
            
    def quality_monitoring(self):
        # Track feed performance
        for feed in active_feeds:
            metrics = self.calculate_metrics(feed)
            if metrics['accuracy'] < threshold:
                self.alert_team(feed)
            if metrics['value'] < cost:
                self.mark_for_review(feed)
                
    def optimization(self):
        # Continuous improvement
        self.tune_confidence_scores()
        self.update_filtering_rules()
        self.rebalance_feed_portfolio()
```

## Best Practices

1. **Research-Driven Selection**: Base feed choices on thorough research
2. **Quality Over Quantity**: Better to have fewer high-quality feeds
3. **Continuous Validation**: Regularly verify feed accuracy through research
4. **Deduplicate Aggressively**: Reduce noise and operational burden
5. **Context Is King**: Prefer feeds with rich context and research value
6. **Measure Everything**: Track metrics to justify investments
7. **Automate Handling**: Minimize manual processing
8. **Regular Reviews**: Quarterly feed portfolio research and assessment
9. **Vendor Relationships**: Maintain good communication with providers

## Related Runbooks
- [Threat Intelligence Research and Reporting](threat_intelligence_briefing.md)
- [Emerging Threat Detection](emerging_threat_detection.md)
- [Intelligence Requirements](intelligence_requirements.md)
- [Threat Intelligence Metrics](../threat_intel_metrics.md)
- [IOC Management](ioc_management.md)

## References
- STIX/TAXII Standards
- Traffic Light Protocol (TLP)
- MITRE ATT&CK Framework
- Intelligence Confidence Levels (NATO)
- Threat Intelligence Platform Best Practices