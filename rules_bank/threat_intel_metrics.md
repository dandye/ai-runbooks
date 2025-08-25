# Threat Intelligence Metrics Framework

## Overview
This framework defines key metrics for measuring the effectiveness, efficiency, and business value of threat intelligence programs. It provides standardized KPIs and KRIs for tracking intelligence quality, operational impact, and strategic alignment.

## Metric Categories

### 1. Intelligence Collection Metrics
Measure the breadth and depth of threat intelligence gathering

### 2. Intelligence Quality Metrics  
Assess accuracy, relevance, and timeliness of intelligence

### 3. Operational Impact Metrics
Track how intelligence improves security operations

### 4. Strategic Value Metrics
Demonstrate business value and risk reduction

### 5. Program Maturity Metrics
Evaluate threat intelligence program evolution

---

## 1. Intelligence Collection Metrics

### Volume Metrics
Track the quantity of intelligence collected:

```yaml
collection_volume:
  total_indicators_collected:
    description: "Total IoCs collected per period"
    measurement: count
    frequency: daily
    benchmark: 10000+ per day
    
  unique_threat_actors_tracked:
    description: "Distinct threat actors monitored"
    measurement: count
    frequency: monthly
    benchmark: 50+ active actors
    
  intelligence_sources_active:
    description: "Number of active intel feeds"
    measurement: count
    frequency: weekly
    benchmark: 15+ diverse sources
    
  vulnerabilities_monitored:
    description: "CVEs tracked for relevance"
    measurement: count
    frequency: daily
    benchmark: 100+ per day assessed
```

### Coverage Metrics
Assess intelligence coverage gaps:

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Geographic Coverage | Countries monitored / Operating countries | 100% | Monthly |
| Industry Coverage | Sectors tracked / Relevant sectors | 100% | Monthly |
| Technology Coverage | Tech stacks monitored / Tech in use | 95%+ | Weekly |
| Threat Actor Coverage | Actors tracked / Actors targeting sector | 90%+ | Weekly |
| MITRE ATT&CK Coverage | Techniques monitored / Relevant techniques | 85%+ | Monthly |

### Source Diversity Index
```
Source Diversity = 1 - Σ(source_contribution²)

Where source_contribution = indicators_from_source / total_indicators
Higher score (closer to 1) = better diversity
Target: > 0.75
```

---

## 2. Intelligence Quality Metrics

### Accuracy Metrics
Measure intelligence reliability:

```yaml
accuracy_metrics:
  true_positive_rate:
    formula: "Confirmed threats / Total threat alerts"
    target: "> 85%"
    measurement_period: weekly
    
  false_positive_rate:
    formula: "False alerts / Total alerts"
    target: "< 10%"
    measurement_period: weekly
    
  intelligence_confidence_score:
    formula: "(Source reliability + Information credibility) / 2"
    scale: 1-5
    target: "> 3.5 average"
    
  validation_rate:
    formula: "Validated intelligence / Total intelligence"
    target: "> 70%"
    measurement_period: daily
```

### Timeliness Metrics
Track intelligence speed and freshness:

| Metric | Description | Target | Measurement |
|--------|-------------|--------|-------------|
| Time to Intelligence (TTI) | Discovery to dissemination | < 2 hours | Per threat |
| Intelligence Age | Average age of active IoCs | < 30 days | Weekly |
| Zero-Day Discovery | Time from wild to detection | < 24 hours | Per zero-day |
| Threat Actor Detection | New actor to identification | < 7 days | Per actor |
| Feed Latency | Feed update to ingestion | < 15 minutes | Continuous |

### Relevance Scoring
```python
relevance_score = (
    (industry_match * 0.3) +
    (technology_match * 0.3) +
    (geographic_match * 0.2) +
    (threat_severity * 0.2)
) * 100

# Where each factor is 0-1
# Target: Average relevance > 70%
```

### Actionability Index
```yaml
actionability_factors:
  contains_iocs: weight: 0.25
  includes_detection_logic: weight: 0.25
  provides_mitigation: weight: 0.25
  maps_to_controls: weight: 0.25
  
actionability_index: sum(factors * weights)
target: "> 0.75"
```

---

## 3. Operational Impact Metrics

### Detection Enhancement
Measure intelligence impact on detection:

```yaml
detection_metrics:
  new_detections_from_intel:
    description: "Detection rules created from intelligence"
    measurement: count per month
    target: 20+ high-quality rules
    
  detection_coverage_improvement:
    formula: "New MITRE techniques covered / Total techniques"
    target: "5% monthly improvement"
    
  alert_enrichment_rate:
    formula: "Alerts enriched with intel / Total alerts"
    target: "> 80%"
    
  mean_time_to_detect_reduction:
    formula: "(MTTD_before - MTTD_after) / MTTD_before"
    target: "20% reduction"
```

### Response Improvement
Track intelligence impact on incident response:

| Metric | Formula | Target | Impact |
|--------|---------|--------|--------|
| Investigation Acceleration | Time saved per investigation | 30% reduction | Efficiency |
| Context Enrichment Rate | Incidents with intel context / Total | > 90% | Quality |
| Threat Attribution Success | Attributed incidents / Total | > 60% | Understanding |
| Containment Speed | Time to contain with intel | 50% faster | Speed |
| Recovery Optimization | Recovery time reduction | 25% faster | Resilience |

### Prevention Metrics
```yaml
prevention_impact:
  threats_prevented:
    formula: "Blocked based on intel / Total attempts"
    target: "> 70%"
    value: "Incidents prevented * Average incident cost"
    
  proactive_patching:
    formula: "Patches applied before exploit / Critical patches"
    target: "> 90%"
    value: "Prevented breaches * Breach cost"
    
  preemptive_blocking:
    formula: "IoCs blocked before first attempt"
    target: "> 60%"
    value: "Prevented connections * Investigation cost"
```

---

## 4. Strategic Value Metrics

### Risk Reduction Metrics
Quantify risk mitigation:

```python
risk_reduction_score = {
    'threat_visibility': {
        'before': 3,  # Scale 1-10
        'after': 8,
        'improvement': 5,
        'value': '$500K risk reduction'
    },
    'attack_surface_reduction': {
        'before': 7,
        'after': 4,
        'improvement': 3,
        'value': '$300K risk reduction'
    },
    'incident_likelihood': {
        'before': 0.4,  # Probability
        'after': 0.15,
        'improvement': 0.25,
        'value': '$2M risk reduction'
    }
}

total_risk_reduction = sum(category['value'])
```

### Business Alignment
Measure intelligence alignment with business:

```yaml
business_alignment:
  critical_asset_coverage:
    formula: "Critical assets monitored / Total critical assets"
    target: "100%"
    
  business_threat_briefings:
    frequency: monthly
    satisfaction_score: "> 4/5"
    
  strategic_decision_support:
    formula: "Decisions influenced by intel / Major decisions"
    target: "> 80%"
    
  compliance_support:
    formula: "Compliance requirements met via intel"
    target: "100%"
```

### ROI Calculation
```
Threat Intelligence ROI = (Value Generated - Program Cost) / Program Cost * 100

Where Value Generated includes:
- Incidents prevented * average incident cost
- Investigation time saved * hourly rate
- Breach prevention value
- Compliance penalty avoidance
- Insurance premium reductions

Target ROI: > 300%
```

### Cost Avoidance
| Category | Calculation | Annual Value |
|----------|-------------|--------------|
| Incident Prevention | Prevented incidents × $150K avg cost | $3M |
| Breach Avoidance | Breach probability reduction × $4.5M | $2M |
| Efficiency Gains | Hours saved × $150/hour | $500K |
| Compliance | Penalties avoided | $1M |
| **Total Cost Avoidance** | Sum of categories | **$6.5M** |

---

## 5. Program Maturity Metrics

### Maturity Assessment Model
Based on capability maturity model (1-5 scale):

```yaml
maturity_dimensions:
  people:
    level_1: "Ad-hoc intelligence consumption"
    level_2: "Dedicated analyst"
    level_3: "Intelligence team"
    level_4: "Specialized roles"
    level_5: "Center of excellence"
    
  process:
    level_1: "Reactive intelligence use"
    level_2: "Basic procedures"
    level_3: "Standardized workflows"
    level_4: "Optimized processes"
    level_5: "Continuous improvement"
    
  technology:
    level_1: "Manual intelligence handling"
    level_2: "Basic automation"
    level_3: "Integrated platform"
    level_4: "Advanced analytics"
    level_5: "AI/ML enhancement"
    
  integration:
    level_1: "Isolated intelligence"
    level_2: "Security team integration"
    level_3: "Cross-functional integration"
    level_4: "Business integration"
    level_5: "Ecosystem integration"
```

### Capability Evolution Tracking
```python
capability_growth = {
    'quarter': 'Q1 2024',
    'capabilities': {
        'threat_actor_tracking': {'before': 2, 'after': 4},
        'vulnerability_intelligence': {'before': 3, 'after': 4},
        'strategic_intelligence': {'before': 1, 'after': 3},
        'tactical_intelligence': {'before': 3, 'after': 5},
        'operational_intelligence': {'before': 2, 'after': 4}
    },
    'overall_maturity': 3.6  # Average across all dimensions
}
```

### Innovation Metrics
```yaml
innovation_tracking:
  new_intelligence_techniques:
    count: 5
    examples: ["ML clustering", "Graph analysis", "NLP extraction"]
    
  process_improvements:
    count: 12
    time_saved: "40 hours/month"
    
  tool_development:
    custom_tools: 3
    integrations: 8
    
  community_contribution:
    shared_intelligence: 150
    research_papers: 2
    conference_presentations: 4
```

---

## Dashboard Template

### Executive Dashboard
```markdown
# Threat Intelligence Program Dashboard
Period: [Month Year]

## Program Value
- **ROI**: 425%
- **Cost Avoidance**: $6.5M
- **Incidents Prevented**: 47
- **Risk Reduction**: 35%

## Intelligence Quality
- **Accuracy**: 89% (↑ 3%)
- **Relevance**: 76% (↑ 5%)
- **Timeliness**: < 2 hrs average
- **Coverage**: 94% of attack surface

## Operational Impact
- **MTTD Improvement**: -32%
- **MTTR Improvement**: -28%
- **Detection Coverage**: +15%
- **False Positive Reduction**: -40%

## Program Maturity
- **Current Level**: 3.6/5.0
- **Target Level**: 4.2/5.0
- **Gap to Target**: 0.6
- **Projected Achievement**: Q3 2024
```

### Operational Dashboard
```yaml
real_time_metrics:
  active_threats: 12
  relevance_score: 82%
  new_iocs_today: 1,847
  alerts_enriched: 94%
  investigations_accelerated: 67%
  
weekly_trends:
  threat_actor_activity: "↑ 15%"
  vulnerability_disclosure_rate: "↑ 8%"
  intelligence_consumption: "↑ 22%"
  detection_rule_creation: "+18 rules"
  
monthly_achievements:
  zero_days_detected: 2
  campaigns_discovered: 5
  attribution_success: 73%
  prevented_incidents: 47
```

---

## Reporting Cadence

### Daily Metrics
- New threat indicators
- Alert enrichment rate
- Intelligence feed status
- Active threat tracking

### Weekly Metrics
- Intelligence quality scores
- Detection improvements
- Operational impact
- Coverage analysis

### Monthly Metrics
- Program ROI
- Risk reduction
- Maturity assessment
- Strategic alignment

### Quarterly Metrics
- Executive value report
- Program evolution
- Capability roadmap
- Budget justification

---

## Implementation Guide

### Phase 1: Foundation (Months 1-3)
1. Implement collection metrics
2. Establish quality baselines
3. Create basic dashboards
4. Define target values

### Phase 2: Operational (Months 4-6)
1. Deploy impact metrics
2. Integrate with security tools
3. Automate metric collection
4. Regular reporting cadence

### Phase 3: Strategic (Months 7-12)
1. Implement value metrics
2. Develop ROI models
3. Create executive dashboards
4. Continuous optimization

---

## Best Practices

1. **Start Simple**: Begin with 5-10 core metrics
2. **Automate Collection**: Use APIs and scripts
3. **Validate Data**: Ensure metric accuracy
4. **Set Realistic Targets**: Based on industry benchmarks
5. **Regular Review**: Monthly metric review sessions
6. **Stakeholder Alignment**: Metrics that matter to leadership
7. **Continuous Improvement**: Refine metrics based on feedback
8. **Benchmark Externally**: Compare with industry peers

## Related Documents
- [Threat Intelligence Briefing](run_books/threat_intelligence_briefing.md)
- [Strategic Threat Assessment](run_books/strategic_threat_assessment.md)
- [Reporting Templates](reporting_templates.md)
- [Program Maturity Model](program_maturity_model.md)

## References
- SANS Threat Intelligence Metrics
- Gartner Threat Intelligence Program Metrics
- FIRST CTI Metrics SIG
- CIS Controls Metrics
- MITRE ATT&CK Metrics